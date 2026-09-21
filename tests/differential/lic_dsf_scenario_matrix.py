"""Starter graph-oracle scenario matrix for the LIC-DSF IDA21 workbook.

Keep this sweep small: workbook defaults plus a few single-axis shocks on
graph **leaf** inputs that are already public in ``inputs.bindings.yaml``,
plus one filled LIC-style country path. Expand with Input 6 factorials once
that path is green.
"""

from __future__ import annotations

from functools import cache
from pathlib import Path
from typing import Any

import yaml
from excel_grapher.series_bindings.ranges import series_data_ranges
from fastpyxl.utils.cell import column_index_from_string, coordinate_from_string

from src.workbook_constraints import (
    expand_sheet_qualified_range,
    parse_sheet_qualified_spec,
)

from .differential_types import Axis, AxisPoint, Scenario
from .lic_dsf_filled_scenario import INPUT_FIRST_PROJECTION_YEAR, filled_lic_writes

_BINDINGS = Path(__file__).resolve().parents[2] / "bindings"
_CHART_HEADER_YEAR0 = 2024
_CHART_HEADER_COL0 = "D"

# Input cells — confirmed leaves on the Chart Data extraction graph.
INPUT_DISCOUNT_RATE = "'Input 1 - Basics'!C25"
INPUT_DEBT_DEFINITION = "'Input 1 - Basics'!C33"
INPUT_REER_OVERVALUATION = "'Input 1 - Basics'!C31"
INPUT_TAILORED_TESTS_ENABLED = "'Input 6 - Tailored Tests'!C6"
INPUT_WORKING_LANGUAGE = "START!K10"

# Rating scalars still collapse to the most-extreme shock; the SCENARIO×year
# tables below are the per-path points that those ratings hide.
RATING_OUTPUT_CELLS: tuple[tuple[str, str], ...] = (
    ("external_dsa_risk_rating_signal", "'Chart Data'!D10"),
    ("external_dsa_risk_rating_numeric", "'Chart Data'!D11"),
    ("external_baseline_breach", "'Chart Data'!D12"),
    ("external_shock_breach", "'Chart Data'!D13"),
    ("fiscal_risk_rating_signal", "'Chart Data'!I10"),
    ("fiscal_risk_rating_numeric", "'Chart Data'!I11"),
    ("fiscal_baseline_breach", "'Chart Data'!I12"),
    ("fiscal_shock_breach", "'Chart Data'!I13"),
    ("overall_risk_rating_signal", "'Chart Data'!L10"),
    ("overall_risk_rating_numeric", "'Chart Data'!L11"),
    ("fiscal_space_moderate_risk_signal", "'Chart Data'!D23"),
)

SHOCK_TABLE_SERIES_IDS: tuple[str, ...] = (
    "chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp",
    "chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue",
    "chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue",
    "chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio",
)


def build_axes() -> tuple[Axis, ...]:
    """Axis-organized starter sweep for graph-oracle parity."""
    return (
        Axis(
            name="baseline",
            points=(
                AxisPoint(
                    label="workbook_defaults",
                    scenario=Scenario(id="baseline", inputs={}),
                ),
            ),
        ),
        Axis(
            name="filled_lic",
            points=(
                AxisPoint(
                    label="ghana_style_fill",
                    scenario=Scenario(
                        id="filled_lic",
                        inputs=filled_lic_writes(),
                    ),
                ),
            ),
        ),
        Axis(
            name="discount_rate",
            points=(
                AxisPoint(
                    label="discount_4pct",
                    scenario=Scenario(
                        id="discount_rate_0_04",
                        inputs={INPUT_DISCOUNT_RATE: 0.04},
                    ),
                ),
                AxisPoint(
                    label="discount_6pct",
                    scenario=Scenario(
                        id="discount_rate_0_06",
                        inputs={INPUT_DISCOUNT_RATE: 0.06},
                    ),
                ),
            ),
        ),
        Axis(
            name="debt_definition",
            points=(
                AxisPoint(
                    label="currency_based",
                    scenario=Scenario(
                        id="debt_definition_currency_based",
                        inputs={INPUT_DEBT_DEFINITION: "Currency-based"},
                    ),
                ),
            ),
        ),
        Axis(
            name="tailored_tests",
            points=(
                AxisPoint(
                    label="tailored_off",
                    scenario=Scenario(
                        id="tailored_tests_off",
                        inputs={INPUT_TAILORED_TESTS_ENABLED: "Off"},
                    ),
                ),
            ),
        ),
        Axis(
            name="reer_overvaluation",
            points=(
                AxisPoint(
                    label="reer_0",
                    scenario=Scenario(
                        id="reer_overvaluation_0",
                        inputs={INPUT_REER_OVERVALUATION: 0},
                    ),
                ),
                AxisPoint(
                    label="reer_40",
                    scenario=Scenario(
                        id="reer_overvaluation_40",
                        inputs={INPUT_REER_OVERVALUATION: 40},
                    ),
                ),
            ),
        ),
        Axis(
            name="language",
            points=(
                AxisPoint(
                    label="french",
                    scenario=Scenario(
                        id="language_french",
                        inputs={INPUT_WORKING_LANGUAGE: "Français"},
                    ),
                ),
            ),
        ),
        Axis(
            name="first_projection_year",
            points=(
                AxisPoint(
                    label="year_2025",
                    scenario=Scenario(
                        id="first_projection_year_2025",
                        inputs={INPUT_FIRST_PROJECTION_YEAR: 2025},
                    ),
                ),
            ),
        ),
    )


def build_scenarios() -> tuple[Scenario, ...]:
    """Flat view of the starter axes (for harnesses that prefer a tuple)."""
    return tuple(point.scenario for axis in build_axes() for point in axis.points)


def _scenario_by_row(series: dict[str, Any]) -> dict[int, str]:
    for dimension in series["structure"]["dimensions"]:
        if dimension["id"] == "SCENARIO":
            return {
                int(row): str(name) for name, row in dimension["bind"]["values"].items()
            }
    raise LookupError(f"{series['id']} has no SCENARIO value_map")


@cache
def _shock_table_cell_labels() -> tuple[tuple[str, str], ...]:
    document = yaml.safe_load(
        (_BINDINGS / "outputs.bindings.yaml").read_text(encoding="utf-8")
    )
    by_id = {str(entry["id"]): entry for entry in document["series"]}
    year0_col = column_index_from_string(_CHART_HEADER_COL0)
    labels: list[tuple[str, str]] = []
    for series_id in SHOCK_TABLE_SERIES_IDS:
        try:
            series = by_id[series_id]
        except KeyError as exc:
            raise LookupError(
                f"outputs.bindings.yaml is missing shock-table series {series_id}"
            ) from exc
        scenario_by_row = _scenario_by_row(series)
        for data_range in series_data_ranges(series):
            for address in expand_sheet_qualified_range(data_range):
                _sheet, a1 = parse_sheet_qualified_spec(address)
                column, row = coordinate_from_string(a1)
                try:
                    scenario = scenario_by_row[row]
                except KeyError as exc:
                    raise LookupError(
                        f"{series_id} range {data_range} includes unbound row {row}"
                    ) from exc
                year = _CHART_HEADER_YEAR0 + (
                    column_index_from_string(column) - year0_col
                )
                labels.append((f"{series_id}[{scenario},{year}]", address))
    return tuple(labels)


def output_cell_labels() -> tuple[tuple[str, str], ...]:
    """``(label, address)`` pairs compared in the graph-oracle sweep."""
    return RATING_OUTPUT_CELLS + _shock_table_cell_labels()


def inputs_for_excel(scenario: Scenario) -> dict[str, Any]:
    """Scenario inputs are already Excel address → value maps."""
    return dict(scenario.inputs)
