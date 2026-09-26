"""Derived-series output specs for the exported-library differential harness."""

from __future__ import annotations

from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from excel_grapher.core.address_keys import normalize_key


@dataclass(frozen=True)
class OutputCellSpec:
    """One bound output cell compared by the exported-library differential."""

    label: str
    address: str
    compute: str
    keys: tuple[tuple[str, Any], ...]


def specs_from_output_series(
    output_series: Sequence[Mapping[str, Any]],
) -> tuple[OutputCellSpec, ...]:
    """Build one spec per bound output cell from derived output-series payloads."""
    specs: list[OutputCellSpec] = []
    for series in output_series:
        series_id = str(series["id"])
        compute = str(series["compute_name"])
        key_fields = tuple(series["key_fields"])
        for cell in series["cells"]:
            key_values = tuple((field, cell["key"][field]) for field in key_fields)
            suffix = ",".join(str(value) for _, value in key_values)
            label = f"{series_id}[{suffix}]" if suffix else series_id
            specs.append(
                OutputCellSpec(
                    label=label,
                    address=str(cell["address"]),
                    compute=compute,
                    keys=key_values,
                )
            )
    return tuple(specs)


def specs_covering_addresses(
    output_series: Sequence[Mapping[str, Any]],
    addresses: Sequence[str],
) -> tuple[OutputCellSpec, ...]:
    """Return specs for ``addresses`` in request order; missing cells fail closed."""
    by_address = {
        normalize_key(spec.address): spec
        for spec in specs_from_output_series(output_series)
    }
    missing: list[str] = []
    selected: list[OutputCellSpec] = []
    for address in addresses:
        spec = by_address.get(normalize_key(address))
        if spec is None:
            missing.append(str(address))
            continue
        selected.append(spec)
    if missing:
        raise LookupError(
            "output series do not cover compared cell(s): " + ", ".join(missing)
        )
    return tuple(selected)


def outputs_from_named_axis_tensor(
    specs: tuple[OutputCellSpec, ...],
    tensor: Any,
) -> dict[str, Any]:
    """Look up ``spec.keys`` on a named-axis ``Series`` / ``Tensor``.

    Unlike catalog-order tuples, this may subset the tensor: compared cells
    need not exhaust the generated domain.
    """
    ambiguity = Counter((spec.compute, spec.keys) for spec in specs)
    values: dict[str, Any] = {}
    for spec in specs:
        if ambiguity[(spec.compute, spec.keys)] > 1:
            values[spec.label] = None
            continue
        by_field = dict(spec.keys)
        try:
            coord = tuple(by_field[axis.name] for axis in tensor.domain.axes)
            values[spec.label] = tensor[coord]
        except KeyError as exc:
            raise LookupError(
                f"{spec.compute} has no cell for {dict(spec.keys)}"
            ) from exc
    return values


def outputs_from_tuple(
    specs: tuple[OutputCellSpec, ...],
    values_by_compute: Mapping[str, Sequence[Any]],
) -> dict[str, Any]:
    """Zip catalog-order ``compute_*`` tuples onto specs sharing a compute name."""
    grouped: dict[str, list[OutputCellSpec]] = {}
    for spec in specs:
        grouped.setdefault(spec.compute, []).append(spec)

    values: dict[str, Any] = {}
    for compute, compute_specs in grouped.items():
        try:
            result = values_by_compute[compute]
        except KeyError as exc:
            raise LookupError(f"no tuple result for {compute}") from exc
        if len(result) != len(compute_specs):
            raise ValueError(
                f"{compute} returned {len(result)} value(s) for "
                f"{len(compute_specs)} bound cell(s)"
            )
        for spec, value in zip(compute_specs, result, strict=True):
            values[spec.label] = value
    return values


def outputs_from_records(
    specs: tuple[OutputCellSpec, ...],
    records_by_compute: Mapping[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    """Key-match compute_* records onto specs; missing/ambiguous → None.

    Specs whose ``(compute, keys)`` pair is shared by more than one spec are
    inherently ambiguous — several bound series collide on one generated
    function name with identical key shapes — so no record can be trusted to
    belong to any one of them. They resolve to ``None`` deterministically
    instead of silently receiving whichever series' records the surviving
    function returns.
    """
    indexed: dict[str, dict[tuple[tuple[str, Any], ...], Any]] = {}
    for compute, records in records_by_compute.items():
        spec_keys_for_compute = [spec.keys for spec in specs if spec.compute == compute]
        fields = (
            tuple(field for field, _ in spec_keys_for_compute[0])
            if spec_keys_for_compute
            else ()
        )
        indexed[compute] = {
            tuple((field, record.get(field)) for field in fields): record.get(
                "OBS_VALUE"
            )
            for record in records
        }
    ambiguity = Counter((spec.compute, spec.keys) for spec in specs)
    return {
        spec.label: (
            None
            if ambiguity[(spec.compute, spec.keys)] > 1
            else indexed.get(spec.compute, {}).get(spec.keys)
        )
        for spec in specs
    }


def _is_named_series(value: object) -> bool:
    """True for generated named-axis tensors that are not sequences."""
    if isinstance(value, (str, bytes, Sequence)):
        return False
    return getattr(value, "domain", None) is not None


def _named_series_value(result: object, spec: OutputCellSpec) -> Any:
    selectors = dict(spec.keys)
    sel = getattr(result, "sel", None)
    if callable(sel) and selectors:
        try:
            return sel(**selectors)
        except (KeyError, TypeError) as exc:
            raise LookupError(
                f"{spec.compute} has no value for {dict(spec.keys)}"
            ) from exc
    coord = tuple(value for _, value in spec.keys)
    key: Any = coord[0] if len(coord) == 1 else coord
    getitem = getattr(result, "__getitem__", None)
    if not callable(getitem):
        raise TypeError(
            f"{spec.compute} named series has no coordinate lookup, got {type(result)!r}"
        )
    try:
        return getitem(key)
    except (KeyError, TypeError, IndexError) as exc:
        raise LookupError(f"{spec.compute} has no value for {dict(spec.keys)}") from exc


def outputs_from_sequences(
    specs: tuple[OutputCellSpec, ...],
    values_by_compute: Mapping[str, object],
) -> dict[str, Any]:
    """Zip inverted-tree ``compute_*`` results onto specs.

    Sequence returns stay in catalog order. Named-axis series are read by
    spec keys. Fail closed when a compute is missing, a sequence length does
    not match the spec count, or a series lacks a requested coordinate.
    """
    grouped: dict[str, list[OutputCellSpec]] = {}
    for spec in specs:
        grouped.setdefault(spec.compute, []).append(spec)
    outputs: dict[str, Any] = {}
    for compute, compute_specs in grouped.items():
        try:
            raw = values_by_compute[compute]
        except KeyError as exc:
            raise LookupError(f"no values returned for {compute}") from exc
        if _is_named_series(raw):
            for spec in compute_specs:
                outputs[spec.label] = _named_series_value(raw, spec)
            continue
        if isinstance(raw, tuple):
            observed: tuple[Any, ...] = raw
        elif isinstance(raw, Sequence) and not isinstance(raw, (str, bytes)):
            observed = tuple(raw)
        else:
            raise TypeError(
                f"{compute} must return a sequence of values, got {type(raw)!r}"
            )
        if len(observed) != len(compute_specs):
            raise ValueError(
                f"{compute} returned {len(observed)} values but specs list "
                f"{len(compute_specs)} cells"
            )
        for spec, value in zip(compute_specs, observed, strict=True):
            outputs[spec.label] = value
    return outputs
