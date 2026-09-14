# LIC-DSF IDA21 template (2025-08-12) — extraction guide

Human guide for the extraction pipeline. Describes the public I/O surface the
generated `lic_dsf_2025_08_12` package should expose. Source workbook:
`data/workbook.xlsm` (IMF–World Bank LIC-DSF IDA21 template).

Authoritative framework prose lives in the IMF Guidance Note PDF
(`data/guidance-note.pdf`); this file is the pipeline-facing catalog.

## Functional overview

The workbook computes Low-Income Country Debt Sustainability Framework (LIC-DSF)
external and public debt risk ratings, stress-test indicator paths, and related
chart/table series used in the standard DSA write-up.

**Almost all published outputs for this extraction live on the `Chart Data`
sheet.** Display tabs (`Output 2-1`, `Output 2-2`, `Output 7`, etc.) largely
mirror Chart Data. Extraction targets in `workbook_config.TARGETS` are therefore
Chart Data ranges only.

## Public outputs (Chart Data)

### Risk-rating signals

| Series | Chart Data range | Meaning |
| --- | --- | --- |
| External DSA risk rating | `D10:D17` | Text/numeric rating, baseline/shock breach flags, MX shock levels |
| Fiscal (total public debt) risk rating | `I10:I14` | Fiscal rating text/numeric and breach flags |
| Applicable tailored stress tests | `I17:I19` | Natural disaster / commodity / market-financing applicability (0/1) |
| Fiscal space (moderate risk) | `D23`, `E26:E27` | Space text signal (`D23`) plus Some/Substantial threshold markers |
| Overall rating | `L10:L11` | Combined external+fiscal overall rating |

### Stress-chart figure series (Figure 1 / Figure 2)

Row time series on `Chart Data` columns `D:X` (projection years from row 35
headers). Includes baseline, historical average, standardized shocks, tailored
shocks, thresholds, and customized-scenario rows used by
`Output 2-1 Stress_Charts_Ex` and `Output 2-2 Stress_Charts_Pub`.

Concrete rows are listed in `workbook_config._FIGURE_DATA_ROWS`.

### Public-debt stress blocks

Four metric blocks on Chart Data (also `D:X` row series), each with the standard
scenario ladder (Baseline, A1 historical, B1–B6, C1–C4, A2 customized):

| Metric | First row |
| --- | --- |
| PV of Debt-to-GDP Ratio | 239 |
| PV of Debt-to-Revenue Ratio | 281 |
| Debt Service-to-Revenue Ratio | 318 |
| Debt Service-to-GDP Ratio | 351 |

## Public inputs (draft)

Economist-facing entry points follow `Input-INSTRUCTIONS` (English text on
`translation!C5:C41`): Input 1–8 plus optional customized scenario sheets.
Yellow-shaded override cells on Input 6/7 and Output 7 judgement cells are
user-editable; green intermediate sheets (`Macro-Debt_Data`, `Ext_Debt_Data`,
`PV_Base`, `Chart Data`, stress/PV engine tabs) are calculation surfaces, not
public API.

Typical groups (to be bound iteratively in `bindings/inputs.bindings.yaml`):

- Country / vintage / debt coverage (`Input 1`, `Input 2`)
- Macro-debt history and projections (`Input 3`)
- External and local-currency financing (`Input 4`, `Input 5`)
- Standardized and tailored stress options (`Input 6`)
- Residual financing and SDR (`Input 7`, `Input 8`)
- Customized scenario assumptions (public / external)

### Leaf classification

`CONSTRAINTS` classify each leaf as `constant` (single-value `Literal`, including
`Literal[None]` blanks) or `input` (ranges / multi-value `Literal`). Engine/lookup
overlays freeze blanks and template snapshots to Literals; Input-sheet projection
grids keep `Annotated[…|None, …]` on blanks so OFFSET/AND abstract analysis stays
tractable.

After narrowing (full `CONSTRAINTS` map):

| Metric | Count |
| --- | ---: |
| Total constrained keys | ~219k |
| Classified `input` | ~21.5k |
| Of which on Input / Customized sheets | ~20.7k |
| Remaining non-public `input` | ~0.8k |

Engine/stress/lookup overlays freeze blanks and template snapshots to single-value
`Literal`s (PV Stress alone dropped from ~10k map inputs to ~50). Input-sheet
projection grids keep `Annotated[…|None, …]` on blanks so OFFSET/AND abstract
analysis stays tractable—those blanks classify as `input` mechanically but are
OFFSET placeholders, not economist parameters; bind only real entry cells next.

The non-public remainder is mostly hand-authored INDEX/OFFSET **controller**
domains on engine sheets (`PV_baseline_com`, `PV_Base`, `PV Stress`, `BLEND…`,
`Market_financing`, `CI Summary` coefficients, etc.) that must keep wide
`Annotated` domains for dynamic-ref resolution.

Re-run the audit anytime:

```bash
uv run python -m scripts.audit_leaf_classification
# optional: also classify graph.leaf_keys()
uv run python -m scripts.audit_leaf_classification --with-graph
```

## Configuration status

| Bundle | Status |
| --- | --- |
| Chart Data `TARGETS` | Declared in `workbook_config.py` (90 ranges) |
| Dynamic-ref `CONSTRAINTS` | Ported overlays in `src/lic_dsf_constraints.py` (~219k keys); leaf classification narrowed (~21.5k inputs, mostly Input sheets + ~0.8k engine controllers) |
| `bindings/outputs.bindings.yaml` | Chart Data public surface: 21 scalars (risk ratings, breaches, MX labels, tailored-stress flags, fiscal space) + 84 `D:X` row series (figure/stress ladders). Regenerated by `scripts.generate_chart_data_output_bindings` |
| `bindings/inputs.bindings.yaml` | Public Input/Customized graph leaves bound (~4.9k series; 10,501 leaves) |
| `bindings/constants.bindings.yaml` | Non-public graph input leaves bound as reader-only `constant: {}` (engine/lookup controllers) |
| `bindings/internals.bindings.yaml` | Semantic pass complete: 7,495 `internal: {}` series covering all 110,106 unbound formula cells (0 unbound). Drafted by `scripts.generate_internal_row_series`, then reshaped and renamed by `scripts.reshape_internal_bindings` — 5,570 `layout: series` keyed by `TIME_PERIOD`/`INDICATOR`, 1,925 `layout: scalar` anchors, ids and `series_context` drawn from workbook row labels |

## Scenario narrative

A representative use of the exported library:

1. Load or set country macro and financing inputs.
2. Optionally toggle tailored stress applicability and customized scenarios.
3. Compute Chart Data risk-rating signals and stress-chart series.
4. Read external, fiscal, and overall ratings plus the indicator paths that
   drive the DSA charts.

### Graph-oracle starter matrix

[`tests/differential/lic_dsf_scenario_matrix.py`](../tests/differential/lic_dsf_scenario_matrix.py)
ships a small pre-export sweep: workbook defaults plus single-axis shocks on
discount rate, external/domestic debt definition, tailored-tests enable, and
REER overvaluation. Compared outputs are the Chart Data risk-rating / fiscal-
space scalars. Expand after the starter is green.
