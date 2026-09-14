"""Starter graph-oracle scenario matrix for the LIC-DSF IDA21 workbook.

Keep this sweep small: workbook defaults plus a few single-axis shocks on
graph **leaf** inputs that are already public in ``inputs.bindings.yaml``.
Expand with Input 3/4/5 projection grids and categorical factorials once the
starter sweep is green.
"""

from __future__ import annotations

from typing import Any

from .differential_types import Axis, AxisPoint, Scenario

# Input cells — confirmed leaves on the Chart Data extraction graph.
INPUT_DISCOUNT_RATE = "'Input 1 - Basics'!C25"
INPUT_DEBT_DEFINITION = "'Input 1 - Basics'!C33"
INPUT_REER_OVERVALUATION = "'Input 1 - Basics'!C31"
INPUT_TAILORED_TESTS_ENABLED = "'Input 6 - Tailored Tests'!C6"

# Starter outputs — Chart Data risk-rating / fiscal-space scalars only.
STARTER_OUTPUT_CELLS: tuple[tuple[str, str], ...] = (
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
    )


def build_scenarios() -> tuple[Scenario, ...]:
    """Flat view of the starter axes (for harnesses that prefer a tuple)."""
    return tuple(point.scenario for axis in build_axes() for point in axis.points)


def output_cell_labels() -> tuple[tuple[str, str], ...]:
    """``(label, address)`` pairs compared in the graph-oracle sweep."""
    return STARTER_OUTPUT_CELLS


def inputs_for_excel(scenario: Scenario) -> dict[str, Any]:
    """Scenario inputs are already Excel address → value maps."""
    return dict(scenario.inputs)
