# LIC-DSF 2025-08-12 graph-oracle parity validation

This folder ships the exported-library differential test, the workbook fixture,
bindings, a graph-build snapshot, and reference parity reports produced against
excel-grapher's FormulaEvaluator.

## Reference results

`results/reference/` contains the last committed parity report from the
extraction pipeline. These reports document that the exported `lic_dsf_2025_08_12`
package matched the extraction graph for the configured scenario sweep.

## Re-run from the extraction repository

The test compares `compute_*` results (via `{Output}Inputs.from_defaults(...)`)
to FormulaEvaluator. It does not drive Microsoft Excel.

```pwsh
uv run python -m tests.differential.differential_test_exported_library
```

## Re-run from this exported project

Install the `validation` extra (excel-grapher at the same requirement used to
generate `lic_dsf_2025_08_12`), then rebuild the graph from the shipped
workbook, bindings, and snapshot:

```pwsh
uv sync --group validation
uv run --group validation python -m tests.differential.differential_test_exported_library --layout exported
```

The first run rebuilds the extraction graph (slow). Later runs reuse
`tests/.cache/`. Local reports write to `results/local/`.
