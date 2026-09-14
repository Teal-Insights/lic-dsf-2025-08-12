"""FormulaEvaluator graph driver with no extraction-repo imports.

Used by the exported-library harness ``--layout exported`` path so ``dist/``
can rebuild the graph from the shipped workbook, bindings, and graph-build
snapshot without ``src.*`` on ``PYTHONPATH``.
"""

from __future__ import annotations

import hashlib
import json
import pickle
from dataclasses import dataclass
from importlib.metadata import version
from pathlib import Path
from typing import Any

from excel_grapher.core.address_keys import normalize_key
from excel_grapher.evaluator import FormulaEvaluator
from excel_grapher.grapher import (
    DependencyGraph,
    DynamicRefConfig,
    create_dependency_graph,
    dump_graph,
    load_graph,
)

GRAPH_BUILD_META_FILENAME = "graph_build.meta.json"
GRAPH_BUILD_CONSTRAINTS_FILENAME = "graph_build.constraints.pkl"


@dataclass(frozen=True)
class GraphBuildSnapshot:
    """Graph-build inputs shipped beside the exported workbook fixture."""

    package_name: str
    library_name: str
    workbook_filename: str
    excel_grapher_version: str
    targets: tuple[str, ...]
    blank_ranges: tuple[str, ...]
    constraints: dict[str, object]


def load_graph_build(*, tests_root: Path) -> GraphBuildSnapshot:
    """Load the seed-time graph-build snapshot from ``tests/fixtures/``."""
    fixtures = tests_root / "fixtures"
    meta_path = fixtures / GRAPH_BUILD_META_FILENAME
    constraints_path = fixtures / GRAPH_BUILD_CONSTRAINTS_FILENAME
    if not meta_path.is_file():
        raise FileNotFoundError(
            f"Exported graph-build snapshot missing: {meta_path}. "
            "Re-run extraction export to seed dist/tests, or use --layout repo."
        )
    if not constraints_path.is_file():
        raise FileNotFoundError(
            f"Exported graph-build constraints missing: {constraints_path}. "
            "Re-run extraction export to seed dist/tests, or use --layout repo."
        )
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"invalid graph-build meta: {meta_path}")
    package_name = payload.get("package_name")
    library_name = payload.get("library_name")
    workbook_filename = payload.get("workbook_filename")
    excel_grapher_version = payload.get("excel_grapher_version")
    targets = payload.get("targets")
    blank_ranges = payload.get("blank_ranges")
    if not isinstance(package_name, str) or not package_name:
        raise ValueError(f"graph-build meta missing package_name: {meta_path}")
    if not isinstance(library_name, str) or not library_name:
        raise ValueError(f"graph-build meta missing library_name: {meta_path}")
    if not isinstance(workbook_filename, str) or not workbook_filename:
        raise ValueError(f"graph-build meta missing workbook_filename: {meta_path}")
    if not isinstance(excel_grapher_version, str) or not excel_grapher_version:
        raise ValueError(f"graph-build meta missing excel_grapher_version: {meta_path}")
    if not isinstance(targets, list) or not all(
        isinstance(item, str) for item in targets
    ):
        raise TypeError(
            f"graph-build meta targets must be a list of strings: {meta_path}"
        )
    if not isinstance(blank_ranges, list) or not all(
        isinstance(item, str) for item in blank_ranges
    ):
        raise TypeError(
            f"graph-build meta blank_ranges must be a list of strings: {meta_path}"
        )
    constraints = pickle.loads(constraints_path.read_bytes())
    if not isinstance(constraints, dict):
        raise TypeError(f"graph-build constraints must be a dict: {constraints_path}")
    return GraphBuildSnapshot(
        package_name=package_name,
        library_name=library_name,
        workbook_filename=workbook_filename,
        excel_grapher_version=excel_grapher_version,
        targets=tuple(targets),
        blank_ranges=tuple(blank_ranges),
        constraints=constraints,
    )


def _graph_cache_key(
    *,
    workbook_path: Path,
    targets: tuple[str, ...],
    constraints: dict[str, object],
    blank_ranges: tuple[str, ...],
) -> str:
    digest = hashlib.sha256()
    digest.update(workbook_path.read_bytes())
    digest.update(b"\0")
    digest.update(json.dumps(list(targets)).encode())
    digest.update(b"\0")
    digest.update(pickle.dumps(dict(constraints), protocol=4))
    digest.update(b"\0")
    digest.update(json.dumps(list(blank_ranges)).encode())
    digest.update(b"\0")
    digest.update(version("excel-grapher").encode())
    digest.update(b"\0load_values=1,provenance=1")
    return digest.hexdigest()


def _load_or_build_graph(
    *,
    workbook_path: Path,
    targets: tuple[str, ...],
    constraints: dict[str, object],
    blank_ranges: tuple[str, ...],
    cache_dir: Path | None,
) -> DependencyGraph:
    dynamic_refs = DynamicRefConfig.from_constraints(constraints, {})

    def _build() -> DependencyGraph:
        return create_dependency_graph(
            workbook_path,
            list(targets),
            load_values=True,
            dynamic_refs=dynamic_refs,
            capture_dependency_provenance=True,
            blank_ranges=blank_ranges,
        )

    if cache_dir is None:
        return _build()

    cache_dir.mkdir(parents=True, exist_ok=True)
    payload_path = (
        cache_dir
        / f"{
            _graph_cache_key(
                workbook_path=workbook_path,
                targets=targets,
                constraints=constraints,
                blank_ranges=blank_ranges,
            )
        }.pkl.gz"
    )
    if payload_path.is_file():
        try:
            return load_graph(payload_path)
        except (OSError, EOFError, pickle.UnpicklingError, TypeError, ValueError):
            payload_path.unlink(missing_ok=True)
    graph = _build()
    dump_graph(graph, payload_path)
    return graph


class FormulaEvaluatorDriver:
    """In-memory FormulaEvaluator driver over a rebuilt dependency graph."""

    def __init__(
        self,
        workbook_path: Path,
        *,
        targets: tuple[str, ...],
        constraints: dict[str, object],
        blank_ranges: tuple[str, ...] = (),
        cache_dir: Path | None = None,
    ) -> None:
        if not targets:
            raise RuntimeError("targets is empty; cannot build the graph oracle.")
        if not constraints:
            raise RuntimeError("constraints is empty; cannot build the graph oracle.")
        self._graph = _load_or_build_graph(
            workbook_path=workbook_path,
            targets=targets,
            constraints=constraints,
            blank_ranges=blank_ranges,
            cache_dir=cache_dir,
        )
        self._evaluator = FormulaEvaluator(self._graph, blank_ranges=blank_ranges)
        self._known_keys = frozenset(self._graph.leaf_keys()) | frozenset(
            self._graph.formula_keys()
        )
        self.missing_cells: set[str] = set()
        self._input_baselines: dict[str, Any] = {}

    @property
    def graph(self) -> DependencyGraph:
        return self._graph

    def record_input_baselines(self, cells: frozenset[str]) -> None:
        """Snapshot baseline values for the union of all scenario input cells."""
        self._input_baselines = {
            normalize_key(cell): node.value
            for cell in cells
            if normalize_key(cell) in self._known_keys
            if (node := self._graph.get_node(normalize_key(cell))) is not None
        }

    def reset_inputs(self) -> None:
        """Restore scenario input cells to values captured at sweep start."""
        for key, value in self._input_baselines.items():
            self._graph.set_node_value(key, value)

    def set_inputs(self, inputs: dict[str, Any]) -> None:
        for key, value in inputs.items():
            canonical = normalize_key(key)
            if canonical in self._known_keys:
                self._graph.set_node_value(canonical, value)
            else:
                self.missing_cells.add(key)

    def read(self, cell: str) -> Any:
        return self._evaluator.evaluate(normalize_key(cell))
