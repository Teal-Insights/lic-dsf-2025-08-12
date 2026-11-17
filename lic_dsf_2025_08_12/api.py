"""Generated functions accepting and returning named-coordinate values."""

from __future__ import annotations

from . import data, model
from .data import (
    _CONSTANTS_0,
    _CONSTANTS_1,
    _CONSTANTS_2,
    _CONSTANTS_3,
    _CONSTANTS_4,
    _CONSTANTS_5,
    _CONSTANTS_6,
    _CONSTANTS_7,
    _CONSTANTS_8,
    _CONSTANTS_9,
    _CONSTANTS_10,
    _CONSTANTS_11,
    _CONSTANTS_12,
    _CONSTANTS_13,
    _CONSTANTS_14,
    _CONSTANTS_15,
    _CONSTANTS_16,
    _CONSTANTS_17,
    _CONSTANTS_18,
    _CONSTANTS_19,
    _CONSTANTS_20,
    _CONSTANTS_21,
    _CONSTANTS_22,
    _CONSTANTS_23,
    _CONSTANTS_24,
    _CONSTANTS_25,
    _CONSTANTS_26,
    _CONSTANTS_27,
    _CONSTANTS_28,
    _CONSTANTS_29,
    _CONSTANTS_30,
    _CONSTANTS_31,
    _CONSTANTS_32,
    _CONSTANTS_33,
    _CONSTANTS_34,
    _CONSTANTS_35,
    _CONSTANTS_36,
    _CONSTANTS_37,
    _CONSTANTS_38,
    _CONSTANTS_39,
    _CONSTANTS_40,
    _CONSTANTS_41,
    _CONSTANTS_42,
    _CONSTANTS_43,
    _CONSTANTS_44,
    _CONSTANTS_45,
    _CONSTANTS_46,
    _CONSTANTS_47,
    _CONSTANTS_48,
    _CONSTANTS_49,
    _CONSTANTS_50,
    _CONSTANTS_51,
    _CONSTANTS_52,
    _CONSTANTS_53,
)
from .model import (
    Realism1ExternalDebtFlowComponentsInputs,
    Realism1ExternalDebtCreatingFlowsInputs,
    Realism1ExternalForecastErrorComponentLabelsInputs,
    Realism1ExternalForecastErrorComponentsInputs,
    Realism1ExternalForecastErrorDistributionLabelsInputs,
    Realism1ExternalForecastErrorDistributionInputs,
    Realism1ExternalVintageYearsInputs,
    Realism1ExternalVintageDebtPathsInputs,
    Realism1PublicDebtFlowComponentsInputs,
    Realism1PublicDebtCreatingFlowsInputs,
    Realism1PublicForecastErrorComponentLabelsInputs,
    Realism1PublicForecastErrorComponentsInputs,
    Realism1PublicForecastErrorLowerQuartileInputs,
    Realism1PublicForecastErrorDistributionLabelsInputs,
    Realism1PublicForecastErrorDistributionInputs,
    Realism1PublicVintageYearsInputs,
    Realism1PublicVintageDebtPathsInputs,
    Realism2FiscalAdjustmentMultiplierLabelsInputs,
    Realism2UnderlyingGrowthMultiplierLabelsInputs,
    Realism2FiscalAdjustmentYearsInputs,
    Realism2UnderlyingGrowthYearsInputs,
    Realism2BaselineGrowthInputs,
    Realism2GrowthTMinus1Inputs,
    Realism2FiscalAdjustmentGrowthImpactInputs,
    Realism2UnderlyingGrowthInputs,
    Realism3InvestmentYearsInputs,
    Realism3InvestmentPathLabelsInputs,
    Realism3PublicPrivateInvestmentPathsInputs,
    Realism3GrowthAccountingVintagesInputs,
    Realism3GrowthAccountingContributionsInputs,
    Realism4Projected3yrAdjustmentLabelInputs,
    Realism4Projected3yrAdjustmentInputs,
    Realism4Projected3yrAdjustmentBinInputs,
    Realism4Projected3yrAdjustmentCategoryInputs,
    Realism4Projected3yrAdjustmentSampleShareInputs,
    Realism4FiscalAdjustmentTopBinLabelInputs,
    Realism4FiscalAdjustmentSampleShareInputs,
    Realism4FiscalAdjustmentCumulativeShareInputs,
    ProbabilityPvDebtToGdpInputs,
    ProbabilityPvDebtToExportsInputs,
    ProbabilityDebtServiceToExportsInputs,
    ProbabilityDebtServiceToRevenueInputs,
    ProbabilityPvDebtToGdpDistressInputs,
    ProbabilityPvDebtToExportsDistressInputs,
    ProbabilityDebtServiceToExportsDistressInputs,
    ProbabilityDebtServiceToRevenueDistressInputs,
    ExternalDsaRiskRatingSignalInputs,
    ExternalDsaRiskRatingNumericInputs,
    ExternalBaselineBreachInputs,
    ExternalShockBreachInputs,
    ExternalPvDebtToGdpMxShockInputs,
    ExternalPvDebtToExportsMxShockInputs,
    ExternalDebtServiceToExportsMxShockInputs,
    ExternalDebtServiceToRevenueMxShockInputs,
    FiscalRiskRatingSignalInputs,
    FiscalRiskRatingNumericInputs,
    FiscalBaselineBreachInputs,
    FiscalShockBreachInputs,
    FiscalPvDebtToGdpMxShockInputs,
    TailoredStressNaturalDisasterApplicableInputs,
    TailoredStressCommodityPriceApplicableInputs,
    TailoredStressMarketFinancingApplicableInputs,
    FiscalSpaceModerateRiskSignalInputs,
    OverallRiskRatingSignalInputs,
    OverallRiskRatingNumericInputs,
    ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs,
    ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs,
    ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs,
    ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs,
    ChartPvDebtGdpRatioCustomAlternativeScenarioInputs,
    ChartOutputPvDebtGdpRatioInputs,
    ChartPvDebtToExportsCustomAlternativeScenarioInputs,
    ChartOutputPvDebtToExportsInputs,
    ChartDebtServiceToExportsCustomAlternativeScenarioInputs,
    ChartOutputDebtServiceToExportsInputs,
    ChartDebtServiceToRevenueCustomAlternativeScenarioInputs,
    ChartOutputDebtServiceToRevenueInputs,
    ChartOutputPvDebtToGdpInputs,
    ChartPvDebtToRevenueMxShockStandardTailoredInputs,
    ChartOutputDebtServiceToRevenueFiscalInputs,
)
from .runtime import publish


@publish(data.REALISM1_EXTERNAL_DEBT_FLOW_COMPONENTS.schema, constants=_CONSTANTS_0, cells=data.REALISM1_EXTERNAL_DEBT_FLOW_COMPONENTS.cells)
def compute_realism1_external_debt_flow_components(inputs: Realism1ExternalDebtFlowComponentsInputs) -> data.Realism1ExternalDebtFlowComponents:
    """Compute translated external debt-creating-flow component labels for the Realism 1 tool.

    Derive the Realism 1 external debt flow decomposition used in forecast-error analysis.

    Args:
        inputs: Input bundle of named-axis data series and scalar settings supplying the Realism 1 external debt flow decomposition inputs.

    Returns:
        A data.Realism1ExternalDebtFlowComponents series containing translated component labels for the external debt-creating-flow decomposition.
    """
    if not isinstance(inputs, Realism1ExternalDebtFlowComponentsInputs):
        raise TypeError(
            f"compute_realism1_external_debt_flow_components() expected Realism1ExternalDebtFlowComponentsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_external_debt_flow_components


@publish(data.REALISM1_EXTERNAL_DEBT_CREATING_FLOWS.schema, constants=_CONSTANTS_1, cells=data.REALISM1_EXTERNAL_DEBT_CREATING_FLOWS.cells)
def compute_realism1_external_debt_creating_flows(inputs: Realism1ExternalDebtCreatingFlowsInputs) -> data.Realism1ExternalDebtCreatingFlows:
    """Compute the Realism 1 external debt-creating-flow decomposition for 5-year historical and projected horizons.

    Derive the decomposition of external PPG debt-creating flows over the 5-year historical window and the corresponding projection path, conformed to the workbook's named coordinate axes.

    Args:
        inputs: Keyword-only dataclass of typed data series over catalog coordinates supplying the Realism 1 external debt-creating-flow inputs (historical and projected macro-debt and external financing quantities); scalars remain scalars.

    Returns:
        A data.Realism1ExternalDebtCreatingFlows series holding the external PPG debt-creating-flow decomposition across the 5-year historical and projected year grid.
    """
    if not isinstance(inputs, Realism1ExternalDebtCreatingFlowsInputs):
        raise TypeError(
            f"compute_realism1_external_debt_creating_flows() expected Realism1ExternalDebtCreatingFlowsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_external_debt_creating_flows


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENT_LABELS.schema, constants=_CONSTANTS_0, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENT_LABELS.cells)
def compute_realism1_external_forecast_error_component_labels(inputs: Realism1ExternalForecastErrorComponentLabelsInputs) -> data.Realism1ExternalForecastErrorComponentLabels:
    """Compute chart-legend component labels for the Realism 1 external forecast-error pack.

    Resolve the authored component-name series used to label the external forecast-error decomposition and vintage charts.

    Args:
        inputs: Typed input dataclass carrying the coordinate-identified series from which the external forecast-error component labels are resolved.

    Returns:
        A `data.Realism1ExternalForecastErrorComponentLabels` series of chart-legend component names for the external forecast-error pack.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorComponentLabelsInputs):
        raise TypeError(
            f"compute_realism1_external_forecast_error_component_labels() expected Realism1ExternalForecastErrorComponentLabelsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_external_forecast_error_component_labels


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENTS.schema, constants=_CONSTANTS_2, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENTS.cells)
def compute_realism1_external_forecast_error_components(inputs: Realism1ExternalForecastErrorComponentsInputs) -> data.Realism1ExternalForecastErrorComponents:
    """Compute the Realism 1 external forecast-error component series.

    Derives the external forecast-error decomposition, expressed as stacked-bar values by debt-creating-flow component, from authored coordinate identities.

    Args:
        inputs: Keyword-only input bundle of typed data.* series and scalars holding the Realism 1 external forecast-error assumptions and source coordinates.

    Returns:
        A data.Realism1ExternalForecastErrorComponents series: the external forecast-error stacked-bar values indexed by debt-creating-flow component.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorComponentsInputs):
        raise TypeError(
            f"compute_realism1_external_forecast_error_components() expected Realism1ExternalForecastErrorComponentsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_external_forecast_error_components


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION_LABELS.schema, constants=_CONSTANTS_3, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION_LABELS.cells)
def compute_realism1_external_forecast_error_distribution_labels(inputs: Realism1ExternalForecastErrorDistributionLabelsInputs) -> data.Realism1ExternalForecastErrorDistributionLabels:
    """Compute the Realism 1 external forecast-error distribution labels series.

    Derive the labels that annotate the external forecast-error median and PPG-debt-change overlay in the Realism 1 chart.

    Args:
        inputs: Dataclass of typed data series providing the Realism 1 external forecast-error inputs over catalog coordinates.

    Returns:
        A typed data series of labels for the external forecast-error median and PPG-debt-change overlay.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorDistributionLabelsInputs):
        raise TypeError(
            f"compute_realism1_external_forecast_error_distribution_labels() expected Realism1ExternalForecastErrorDistributionLabelsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_external_forecast_error_distribution_labels


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION.schema, constants=_CONSTANTS_4, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION.cells)
def compute_realism1_external_forecast_error_distribution(inputs: Realism1ExternalForecastErrorDistributionInputs) -> data.Realism1ExternalForecastErrorDistribution:
    """Compute the Realism 1 external forecast-error distribution.

    Derives the external forecast-error median and country PPG-debt-change overlay used by the Realism 1 forecast-error decomposition charts.

    Args:
        inputs: Keyword-only bundle of coordinate-series inputs supplying the catalog-aligned forecast-error observations and PPG debt-change overlay data needed to author the distribution.

    Returns:
        A data.Realism1ExternalForecastErrorDistribution series holding the external forecast-error median alongside the country PPG-debt-change overlay.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorDistributionInputs):
        raise TypeError(
            f"compute_realism1_external_forecast_error_distribution() expected Realism1ExternalForecastErrorDistributionInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_external_forecast_error_distribution


@publish(data.REALISM1_EXTERNAL_VINTAGE_YEARS.schema, constants=_CONSTANTS_5, cells=data.REALISM1_EXTERNAL_VINTAGE_YEARS.cells)
def compute_realism1_external_vintage_years(inputs: Realism1ExternalVintageYearsInputs) -> data.Realism1ExternalVintageYears:
    """Compute the Realism 1 external vintage debt-path year series.

    Derives the external vintage year coordinates for the Realism 1 forecast-error chart block from the authored macro current-account series.

    Args:
        inputs: Input bundle of typed data.* series supplying the macro current-account projections that determine the `TIME_PERIOD` keys of the vintage year axis.

    Returns:
        A `data.Realism1ExternalVintageYears` series giving the year axis copied into the Realism 1 external vintage debt-path chart block.
    """
    if not isinstance(inputs, Realism1ExternalVintageYearsInputs):
        raise TypeError(
            f"compute_realism1_external_vintage_years() expected Realism1ExternalVintageYearsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_external_vintage_years


@publish(data.REALISM1_EXTERNAL_VINTAGE_DEBT_PATHS.schema, constants=_CONSTANTS_2, cells=data.REALISM1_EXTERNAL_VINTAGE_DEBT_PATHS.cells)
def compute_realism1_external_vintage_debt_paths(inputs: Realism1ExternalVintageDebtPathsInputs) -> data.Realism1ExternalVintageDebtPaths:
    """Compute Realism 1 external vintage debt paths from authored coordinate identities.

    Derive the current, previous, and five-year-ago DSA vintage paths of PPG external debt for the forecast-error realism chart.

    Args:
        inputs: Dataclass of realism-1 external vintage inputs supplying the macro and external-debt series over catalog coordinates, with TIME_PERIOD keys aligned to the current-account macro series.

    Returns:
        A named-axis data series of PPG external debt vintage paths — current, previous, and five-year-ago DSA projections — indexed over catalog coordinates.
    """
    if not isinstance(inputs, Realism1ExternalVintageDebtPathsInputs):
        raise TypeError(
            f"compute_realism1_external_vintage_debt_paths() expected Realism1ExternalVintageDebtPathsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_external_vintage_debt_paths


@publish(data.REALISM1_PUBLIC_DEBT_FLOW_COMPONENTS.schema, constants=_CONSTANTS_6, cells=data.REALISM1_PUBLIC_DEBT_FLOW_COMPONENTS.cells)
def compute_realism1_public_debt_flow_components(inputs: Realism1PublicDebtFlowComponentsInputs) -> data.Realism1PublicDebtFlowComponents:
    """Compute translated public debt-creating-flow component labels for Realism 1.

    Resolve the Realism 1 public debt flow decomposition into a labeled output series from authored coordinate identities.

    Args:
        inputs: Inputs dataclass containing the Realism 1 public debt flow component coordinate inputs needed for the computation.

    Returns:
        A data.Realism1PublicDebtFlowComponents series of translated component labels for the public debt-creating-flow decomposition.
    """
    if not isinstance(inputs, Realism1PublicDebtFlowComponentsInputs):
        raise TypeError(
            f"compute_realism1_public_debt_flow_components() expected Realism1PublicDebtFlowComponentsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_public_debt_flow_components


@publish(data.REALISM1_PUBLIC_DEBT_CREATING_FLOWS.schema, constants=_CONSTANTS_7, cells=data.REALISM1_PUBLIC_DEBT_CREATING_FLOWS.cells)
def compute_realism1_public_debt_creating_flows(inputs: Realism1PublicDebtCreatingFlowsInputs) -> data.Realism1PublicDebtCreatingFlows:
    """Compute the Realism 1 public debt-creating-flow decomposition for the LIC-DSF template.

    Evaluates the authored coordinate identities that split public debt-creating flows over the 5-year historical window and the projection horizon for the Realism 1 forecast-error tool.

    Args:
        inputs: Keyword-only typed-input bundle of `data.*` series over catalog coordinates (macro, debt, and financing inputs for the country/vintage) supplying every leaf the public debt-creating-flow identities consume; passed as a single `Realism1PublicDebtCreatingFlowsInputs` instance rather than per-cell arguments.

    Returns:
        A `data.Realism1PublicDebtCreatingFlows` series holding the public debt-creating-flow decomposition across catalog coordinates, contrasting the 5-year historical values against the projected path.
    """
    if not isinstance(inputs, Realism1PublicDebtCreatingFlowsInputs):
        raise TypeError(
            f"compute_realism1_public_debt_creating_flows() expected Realism1PublicDebtCreatingFlowsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_public_debt_creating_flows


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENT_LABELS.schema, constants=_CONSTANTS_6, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENT_LABELS.cells)
def compute_realism1_public_forecast_error_component_labels(inputs: Realism1PublicForecastErrorComponentLabelsInputs) -> data.Realism1PublicForecastErrorComponentLabels:
    """Compute the Realism 1 public forecast-error chart-legend component labels.

    Derives the labelled components of the public forecast-error decomposition so they can be read off as named chart-legend entries.

    Args:
        inputs: Typed input bundle supplying the Realism 1 forecast-error decomposition data over catalog coordinates from which the component labels are derived.

    Returns:
        A `data.Realism1PublicForecastErrorComponentLabels` series of chart-legend component names for the public forecast-error pack.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorComponentLabelsInputs):
        raise TypeError(
            f"compute_realism1_public_forecast_error_component_labels() expected Realism1PublicForecastErrorComponentLabelsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_public_forecast_error_component_labels


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENTS.schema, constants=_CONSTANTS_8, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENTS.cells)
def compute_realism1_public_forecast_error_components(inputs: Realism1PublicForecastErrorComponentsInputs) -> data.Realism1PublicForecastErrorComponents:
    """Compute public forecast-error components for the Realism 1 stacked-bar chart.

    Derive the stacked-bar forecast-error values by debt-creating-flow component from authored coordinate identities.

    Args:
        inputs: Inputs dataclass carrying the Realism 1 coordinate series and scalars needed to resolve the public forecast-error decomposition.

    Returns:
        A data.Realism1PublicForecastErrorComponents series of public forecast-error stacked-bar values indexed by debt-creating-flow component.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorComponentsInputs):
        raise TypeError(
            f"compute_realism1_public_forecast_error_components() expected Realism1PublicForecastErrorComponentsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_public_forecast_error_components


@publish(key=(), domain=None, constants=_CONSTANTS_9, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_LOWER_QUARTILE_CELLS)
def compute_realism1_public_forecast_error_lower_quartile(inputs: Realism1PublicForecastErrorLowerQuartileInputs) -> float | str:
    """Compute the Realism 1 public forecast-error lower-quartile marker.

    Derive the public forecast-error lower-quartile marker from the authored coordinate identities for the Realism 1 tool.

    Args:
        inputs: Typed input dataclass containing the data.* series required to compute the public forecast-error lower-quartile marker.

    Returns:
        The public forecast-error lower-quartile marker as a float, or a string when the authored coordinate identity yields a text result.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorLowerQuartileInputs):
        raise TypeError(
            f"compute_realism1_public_forecast_error_lower_quartile() expected Realism1PublicForecastErrorLowerQuartileInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_public_forecast_error_lower_quartile


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION_LABELS.schema, constants=_CONSTANTS_10, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION_LABELS.cells)
def compute_realism1_public_forecast_error_distribution_labels(inputs: Realism1PublicForecastErrorDistributionLabelsInputs) -> data.Realism1PublicForecastErrorDistributionLabels:
    """Compute the labels for the public forecast-error median and change-in-debt overlay.

    Provide the chart labels used by the Realism 1 public forecast-error distribution results.

    Args:
        inputs: Typed inputs carrying the authored coordinate identities required for the Realism 1 public forecast-error distribution labels.

    Returns:
        A data.Realism1PublicForecastErrorDistributionLabels series containing labels for the public forecast-error median and change-in-debt overlay.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorDistributionLabelsInputs):
        raise TypeError(
            f"compute_realism1_public_forecast_error_distribution_labels() expected Realism1PublicForecastErrorDistributionLabelsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_public_forecast_error_distribution_labels


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION.schema, constants=_CONSTANTS_11, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION.cells)
def compute_realism1_public_forecast_error_distribution(inputs: Realism1PublicForecastErrorDistributionInputs) -> data.Realism1PublicForecastErrorDistribution:
    """Compute the Realism 1 public forecast-error distribution series.

    Derive the public forecast-error median and country change-in-debt overlay from the bound Realism 1 inputs, producing the chart series consumed by the Output 4-1 realism figure.

    Args:
        inputs: Realism1PublicForecastErrorDistributionInputs dataclass of named-axis `data.*` series and scalars holding the bound Realism 1 public forecast-error inputs, including the public forecast-error decomposition and vintage paths read over the country/year catalog coordinates.

    Returns:
        `data.Realism1PublicForecastErrorDistribution` dataclass of series carrying the public forecast-error median and the country change-in-debt overlay.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorDistributionInputs):
        raise TypeError(
            f"compute_realism1_public_forecast_error_distribution() expected Realism1PublicForecastErrorDistributionInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_public_forecast_error_distribution


@publish(data.REALISM1_PUBLIC_VINTAGE_YEARS.schema, constants=_CONSTANTS_5, cells=data.REALISM1_PUBLIC_VINTAGE_YEARS.cells)
def compute_realism1_public_vintage_years(inputs: Realism1PublicVintageYearsInputs) -> data.Realism1PublicVintageYears:
    """Compute the Realism 1 public-vintage year axis for the LIC-DSF chart series.

    Derives the year index used by the public vintage debt-path chart block, taking its periods from the authored current-account macro coordinates.

    Args:
        inputs: Inputs dataclass `Realism1PublicVintageYearsInputs` supplying the current-account macro coordinates (`input3_input_3_macro_current_account`) whose `TIME_PERIOD` keys determine the vintage year axis.

    Returns:
        A `data.Realism1PublicVintageYears` series holding the `TIME_PERIOD` year axis copied into the public vintage debt-path chart block.
    """
    if not isinstance(inputs, Realism1PublicVintageYearsInputs):
        raise TypeError(
            f"compute_realism1_public_vintage_years() expected Realism1PublicVintageYearsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_public_vintage_years


@publish(data.REALISM1_PUBLIC_VINTAGE_DEBT_PATHS.schema, constants=_CONSTANTS_8, cells=data.REALISM1_PUBLIC_VINTAGE_DEBT_PATHS.cells)
def compute_realism1_public_vintage_debt_paths(inputs: Realism1PublicVintageDebtPathsInputs) -> data.Realism1PublicVintageDebtPaths:
    """Compute Realism 1 public-debt vintage DSA paths.

    Derive current, previous, and five-year-ago total public debt paths for the Realism 1 forecast-error chart.

    Args:
        inputs: Typed input dataclass carrying the Realism 1 public-vintage debt-path parameters and coordinate series.

    Returns:
        Typed `data.Realism1PublicVintageDebtPaths` series bundle containing the current, previous, and five-year-ago DSA paths of total public debt.
    """
    if not isinstance(inputs, Realism1PublicVintageDebtPathsInputs):
        raise TypeError(
            f"compute_realism1_public_vintage_debt_paths() expected Realism1PublicVintageDebtPathsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism1_public_vintage_debt_paths


@publish(data.REALISM2_FISCAL_ADJUSTMENT_MULTIPLIER_LABELS.schema, constants=_CONSTANTS_12, cells=data.REALISM2_FISCAL_ADJUSTMENT_MULTIPLIER_LABELS.cells)
def compute_realism2_fiscal_adjustment_multiplier_labels(inputs: Realism2FiscalAdjustmentMultiplierLabelsInputs) -> data.Realism2FiscalAdjustmentMultiplierLabels:
    """Compute the fiscal-adjustment multiplier column labels for the Realism 2 panel.

    Derives the multiplier-column legend series for the fiscal-adjustment-on-growth chart from the supplied inputs.

    Args:
        inputs: Keyword-only input bundle of named-axis series and scalars supplying the Realism 2 fiscal-multiplier chart parameters.

    Returns:
        A data.Realism2FiscalAdjustmentMultiplierLabels series of multiplier-column legends for the fiscal-adjustment-on-growth panel.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentMultiplierLabelsInputs):
        raise TypeError(
            f"compute_realism2_fiscal_adjustment_multiplier_labels() expected Realism2FiscalAdjustmentMultiplierLabelsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism2_fiscal_adjustment_multiplier_labels


@publish(data.REALISM2_UNDERLYING_GROWTH_MULTIPLIER_LABELS.schema, constants=_CONSTANTS_12, cells=data.REALISM2_UNDERLYING_GROWTH_MULTIPLIER_LABELS.cells)
def compute_realism2_underlying_growth_multiplier_labels(inputs: Realism2UnderlyingGrowthMultiplierLabelsInputs) -> data.Realism2UnderlyingGrowthMultiplierLabels:
    """Compute Realism 2 underlying-growth multiplier-column legend labels.

    Builds the chart legend labels for the Realism 2 fiscal-multiplier underlying-growth panel.

    Args:
        inputs: Typed input object carrying the coordinate-scoped series and scalar values needed to identify and label the underlying-growth multiplier columns.

    Returns:
        A data.Realism2UnderlyingGrowthMultiplierLabels value containing the multiplier-column legends for the underlying-growth panel.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthMultiplierLabelsInputs):
        raise TypeError(
            f"compute_realism2_underlying_growth_multiplier_labels() expected Realism2UnderlyingGrowthMultiplierLabelsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism2_underlying_growth_multiplier_labels


@publish(data.REALISM2_FISCAL_ADJUSTMENT_YEARS.schema, constants=_CONSTANTS_5, cells=data.REALISM2_FISCAL_ADJUSTMENT_YEARS.cells)
def compute_realism2_fiscal_adjustment_years(inputs: Realism2FiscalAdjustmentYearsInputs) -> data.Realism2FiscalAdjustmentYears:
    """Compute the fiscal-adjustment-on-growth years panel for Realism 2.

    Derives the fiscal-adjustment year series used by the Realism 2 fiscal-multiplier chart.

    Args:
        inputs: Dataclass of typed input series that supply the macro and fiscal-adjustment coordinates needed to identify the `TIME_PERIOD` axis and values.

    Returns:
        A typed series over the `TIME_PERIOD` year axis containing the fiscal-adjustment years.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentYearsInputs):
        raise TypeError(
            f"compute_realism2_fiscal_adjustment_years() expected Realism2FiscalAdjustmentYearsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism2_fiscal_adjustment_years


@publish(data.REALISM2_UNDERLYING_GROWTH_YEARS.schema, constants=_CONSTANTS_5, cells=data.REALISM2_UNDERLYING_GROWTH_YEARS.cells)
def compute_realism2_underlying_growth_years(inputs: Realism2UnderlyingGrowthYearsInputs) -> data.Realism2UnderlyingGrowthYears:
    """Compute Realism 2 underlying growth years from authored coordinate identities.

    Derives the underlying-growth panel while preserving the year axis sourced from the macro current-account input.

    Args:
        inputs: Typed keyword-only dataclass of input series and scalars; its macro current-account series determines the TIME_PERIOD keys for the output.

    Returns:
        A data.Realism2UnderlyingGrowthYears series over TIME_PERIOD containing the underlying-growth panel with the year axis copied into it.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthYearsInputs):
        raise TypeError(
            f"compute_realism2_underlying_growth_years() expected Realism2UnderlyingGrowthYearsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism2_underlying_growth_years


@publish(data.REALISM2_BASELINE_GROWTH.schema, constants=_CONSTANTS_5, cells=data.REALISM2_BASELINE_GROWTH.cells)
def compute_realism2_baseline_growth(inputs: Realism2BaselineGrowthInputs) -> data.Realism2BaselineGrowth:
    """Compute the baseline real GDP growth path for the Realism 2 fiscal-multiplier chart.

    Derives the baseline growth series over the catalog `TIME_PERIOD` axis from the supplied Realism 2 inputs, feeding the fiscal-multiplier chart.

    Args:
        inputs: Typed `Realism2BaselineGrowthInputs` bundle of named-axis `data.*` series and scalars supplying the macro and coordinate inputs; time keys are inferred from the Input 3 macro current-account series.

    Returns:
        A `data.Realism2BaselineGrowth` series giving baseline real GDP growth along the catalog `TIME_PERIOD` coordinate.
    """
    if not isinstance(inputs, Realism2BaselineGrowthInputs):
        raise TypeError(
            f"compute_realism2_baseline_growth() expected Realism2BaselineGrowthInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism2_baseline_growth


@publish(data.REALISM2_GROWTH_T_MINUS_1.schema, constants=_CONSTANTS_5, cells=data.REALISM2_GROWTH_T_MINUS_1.cells)
def compute_realism2_growth_t_minus_1(inputs: Realism2GrowthTMinus1Inputs) -> data.Realism2GrowthTMinus1:
    """Compute the pre-projection growth series carried into the Realism 2 underlying-growth panel.

    Derive `realism2_growth_t_minus_1` from authored coordinate identities so the baseline historical growth path is available to the fiscal-multiplier realism check.

    Args:
        inputs: Dataclass of keyword-only `data.*` series and scalar parameters supplying the Realism 2 inputs; `TIME_PERIOD` keys are determined by `input3_input_3_macro_current_account`.

    Returns:
        `data.Realism2GrowthTMinus1` series of growth values indexed along `TIME_PERIOD`, giving the period t-1 growth carried into the underlying-growth panel.
    """
    if not isinstance(inputs, Realism2GrowthTMinus1Inputs):
        raise TypeError(
            f"compute_realism2_growth_t_minus_1() expected Realism2GrowthTMinus1Inputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism2_growth_t_minus_1


@publish(data.REALISM2_FISCAL_ADJUSTMENT_GROWTH_IMPACT.schema, constants=_CONSTANTS_13, cells=data.REALISM2_FISCAL_ADJUSTMENT_GROWTH_IMPACT.cells)
def compute_realism2_fiscal_adjustment_growth_impact(inputs: Realism2FiscalAdjustmentGrowthImpactInputs) -> data.Realism2FiscalAdjustmentGrowthImpact:
    """Compute the growth impact of the planned fiscal adjustment under alternative multipliers.

    Evaluate how GDP growth responds to the planned fiscal-adjustment path across alternative multiplier assumptions, yielding chart-ready series for the Realism 2 fiscal-multiplier output.

    Args:
        inputs: Keyword-only typed input bundle for the fiscal-adjustment growth impact computation, carrying the alternative-multiplier and adjustment assumptions as named-axis data series over catalog coordinates (not bare Python lists).

    Returns:
        A `data.Realism2FiscalAdjustmentGrowthImpact` typed series holding the alternative-multiplier growth-impact values aligned to the catalog time axis.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentGrowthImpactInputs):
        raise TypeError(
            f"compute_realism2_fiscal_adjustment_growth_impact() expected Realism2FiscalAdjustmentGrowthImpactInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism2_fiscal_adjustment_growth_impact


@publish(data.REALISM2_UNDERLYING_GROWTH.schema, constants=_CONSTANTS_13, cells=data.REALISM2_UNDERLYING_GROWTH.cells)
def compute_realism2_underlying_growth(inputs: Realism2UnderlyingGrowthInputs) -> data.Realism2UnderlyingGrowth:
    """Compute realism 2 underlying growth paths under alternative fiscal-multiplier assumptions.

    Derive the Realism 2 chart series for downstream DSA output and figure extraction.

    Args:
        inputs: Input dataclass bundling the fiscal-multiplier scenario assumptions and catalog-aligned source series required to derive the Realism 2 underlying growth paths.

    Returns:
        A data.Realism2UnderlyingGrowth series of underlying growth paths under alternative fiscal-multiplier assumptions, indexed over catalog coordinates including TIME_PERIOD.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthInputs):
        raise TypeError(
            f"compute_realism2_underlying_growth() expected Realism2UnderlyingGrowthInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism2_underlying_growth


@publish(data.REALISM3_INVESTMENT_YEARS.schema, constants=_CONSTANTS_5, cells=data.REALISM3_INVESTMENT_YEARS.cells)
def compute_realism3_investment_years(inputs: Realism3InvestmentYearsInputs) -> data.Realism3InvestmentYears:
    """Compute the Realism 3 investment-years series over the chart's year axis.

    Produce the year-indexed investment-vintage series used by the Realism 3 public/private investment comparison chart.

    Args:
        inputs: Typed input bundle supplying the authored coordinate identities and macro current-account series whose `TIME_PERIOD` keys define the output year grid.

    Returns:
        `data.Realism3InvestmentYears` series indexed by `TIME_PERIOD`, representing the public/private investment vintage-comparison years.
    """
    if not isinstance(inputs, Realism3InvestmentYearsInputs):
        raise TypeError(
            f"compute_realism3_investment_years() expected Realism3InvestmentYearsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism3_investment_years


@publish(data.REALISM3_INVESTMENT_PATH_LABELS.schema, constants=_CONSTANTS_14, cells=data.REALISM3_INVESTMENT_PATH_LABELS.cells)
def compute_realism3_investment_path_labels(inputs: Realism3InvestmentPathLabelsInputs) -> data.Realism3InvestmentPathLabels:
    """Compute row-legend labels for Realism 3 investment paths across previous and current DSA public and private series.

    Build the typed label series that identify previous versus current DSA public and private investment paths for Realism 3 chart output.

    Args:
        inputs: Keyword-only Realism3InvestmentPathLabelsInputs dataclass of typed data.* series supplying the coordinate-aligned previous and current DSA public and private investment path values from which row legends are derived.

    Returns:
        A data.Realism3InvestmentPathLabels typed series containing row legends that distinguish previous and current DSA public and private investment paths.
    """
    if not isinstance(inputs, Realism3InvestmentPathLabelsInputs):
        raise TypeError(
            f"compute_realism3_investment_path_labels() expected Realism3InvestmentPathLabelsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism3_investment_path_labels


@publish(data.REALISM3_PUBLIC_PRIVATE_INVESTMENT_PATHS.schema, constants=_CONSTANTS_15, cells=data.REALISM3_PUBLIC_PRIVATE_INVESTMENT_PATHS.cells)
def compute_realism3_public_private_investment_paths(inputs: Realism3PublicPrivateInvestmentPathsInputs) -> data.Realism3PublicPrivateInvestmentPaths:
    """Compute public and private investment paths as a share of GDP for the Realism 3 tool.

    Derive current- and previous-vintage public and private investment (% of GDP) series used by the Realism 3 invest-growth charts.

    Args:
        inputs: Dataclass of typed `data.*` series over catalog coordinates supplying the macro and investment inputs from which the Realism 3 public and private investment paths are derived; its `TIME_PERIOD` keys follow the Input 3 current-account macro series.

    Returns:
        `data.Realism3PublicPrivateInvestmentPaths` dataclass of typed series giving public and private investment (% of GDP) for the current and previous DSA vintages over the catalog time axis.
    """
    if not isinstance(inputs, Realism3PublicPrivateInvestmentPathsInputs):
        raise TypeError(
            f"compute_realism3_public_private_investment_paths() expected Realism3PublicPrivateInvestmentPathsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism3_public_private_investment_paths


@publish(data.REALISM3_GROWTH_ACCOUNTING_VINTAGES.schema, constants=_CONSTANTS_16, cells=data.REALISM3_GROWTH_ACCOUNTING_VINTAGES.cells)
def compute_realism3_growth_accounting_vintages(inputs: Realism3GrowthAccountingVintagesInputs) -> data.Realism3GrowthAccountingVintages:
    """Compute Realism 3 investment-growth accounting vintage headers with authored coordinate identities.

    Builds the Realism 3 growth-accounting summary vintage series from a typed input bundle.

    Args:
        inputs: Typed input object supplying the Realism 3 growth-accounting vintages inputs as named-axis data series over catalog coordinates.

    Returns:
        A data.Realism3GrowthAccountingVintages dataclass of named-axis series containing the investment-growth accounting summary vintage headers.
    """
    if not isinstance(inputs, Realism3GrowthAccountingVintagesInputs):
        raise TypeError(
            f"compute_realism3_growth_accounting_vintages() expected Realism3GrowthAccountingVintagesInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism3_growth_accounting_vintages


@publish(data.REALISM3_GROWTH_ACCOUNTING_CONTRIBUTIONS.schema, constants=_CONSTANTS_17, cells=data.REALISM3_GROWTH_ACCOUNTING_CONTRIBUTIONS.cells)
def compute_realism3_growth_accounting_contributions(inputs: Realism3GrowthAccountingContributionsInputs) -> data.Realism3GrowthAccountingContributions:
    """Compute Realism 3 five-year-average growth-accounting contributions.

    Derive the government-capital and other-factor contributions to growth for the Realism 3 invest-growth tool.

    Args:
        inputs: Typed input bundle containing the Realism 3 growth-accounting assumptions and named-axis series over catalog coordinates.

    Returns:
        data.Realism3GrowthAccountingContributions with the five-year-average contributions of government capital and other factors to growth, expressed as typed named-axis series over catalog coordinates.
    """
    if not isinstance(inputs, Realism3GrowthAccountingContributionsInputs):
        raise TypeError(
            f"compute_realism3_growth_accounting_contributions() expected Realism3GrowthAccountingContributionsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism3_growth_accounting_contributions


@publish(key=(), domain=None, constants=_CONSTANTS_18, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_LABEL_CELLS)
def compute_realism4_projected_3yr_adjustment_label(inputs: Realism4Projected3yrAdjustmentLabelInputs) -> str | int | float | bool:
    """Compute the Realism 4 projected 3-year fiscal-adjustment label.

    Derives the placement of the country's projected 3-year fiscal adjustment within the Realism 4 fiscal-adjustment chart and distribution.

    Args:
        inputs: Inputs dataclass bundling the Realism 4 fiscal-adjustment placement and distribution series along with the supporting named-axis catalog data needed to resolve the projected 3-year adjustment label.

    Returns:
        The projected 3-year fiscal-adjustment marker label for the country, returned as a str, int, float, or bool depending on the underlying cell value.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentLabelInputs):
        raise TypeError(
            f"compute_realism4_projected_3yr_adjustment_label() expected Realism4Projected3yrAdjustmentLabelInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism4_projected_3yr_adjustment_label


@publish(key=(), domain=None, constants=_CONSTANTS_5, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_CELLS)
def compute_realism4_projected_3yr_adjustment(inputs: Realism4Projected3yrAdjustmentInputs) -> float | str:
    """Compute the projected three-year fiscal adjustment from Realism 4 inputs.

    Evaluates the Realism 4 fiscal-adjustment tool to produce the projected three-year adjustment path used by the Output 4-2 fiscal-adjustment chart.

    Args:
        inputs: Realism4Projected3yrAdjustmentInputs dataclass bundling the Realism 4 fiscal-adjustment inputs — the placement and distribution series (typed data.* series over catalog coordinates) together with any scalar settings — consumed by the model; a TypeError is raised if a value of another type is supplied.

    Returns:
        Projected three-year fiscal adjustment expressed in percentage points of GDP, returned as a float, or as a string when the underlying workbook cell resolves to a text or label result rather than a numeric adjustment.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentInputs):
        raise TypeError(
            f"compute_realism4_projected_3yr_adjustment() expected Realism4Projected3yrAdjustmentInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism4_projected_3yr_adjustment


@publish(key=(), domain=None, constants=_CONSTANTS_5, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_BIN_CELLS)
def compute_realism4_projected_3yr_adjustment_bin(inputs: Realism4Projected3yrAdjustmentBinInputs) -> float | str:
    """Compute the Realism 4 histogram bin edge for the projected 3-year fiscal adjustment.

    Resolve the authored coordinate identities that place the projected 3-year fiscal adjustment into its Realism 4 distribution bin, feeding the Output 4-2 fiscal-adjustment chart series.

    Args:
        inputs: Realism4Projected3yrAdjustmentBinInputs dataclass of named-axis series and scalars over catalog coordinates holding the Realism 4 fiscal-adjustment inputs; must be an instance of that type, otherwise a TypeError is raised.

    Returns:
        float | str — the projected 3-year adjustment rounded to its histogram bin edge, or a string label when the bin resolves to a categorical/text cell.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentBinInputs):
        raise TypeError(
            f"compute_realism4_projected_3yr_adjustment_bin() expected Realism4Projected3yrAdjustmentBinInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism4_projected_3yr_adjustment_bin


@publish(key=(), domain=None, constants=_CONSTANTS_19, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_CATEGORY_CELLS)
def compute_realism4_projected_3yr_adjustment_category(inputs: Realism4Projected3yrAdjustmentCategoryInputs) -> float | str:
    """Compute the Realism 4 projected 3-year adjustment category.

    Derives the histogram category index for the country's projected fiscal adjustment under Realism 4.

    Args:
        inputs: Typed input bundle containing the authored coordinate identities required to compute the Realism 4 projected 3-year adjustment category.

    Returns:
        Histogram category index for the country's projected adjustment, returned as a numeric category or string label.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentCategoryInputs):
        raise TypeError(
            f"compute_realism4_projected_3yr_adjustment_category() expected Realism4Projected3yrAdjustmentCategoryInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism4_projected_3yr_adjustment_category


@publish(key=(), domain=None, constants=_CONSTANTS_19, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_SAMPLE_SHARE_CELLS)
def compute_realism4_projected_3yr_adjustment_sample_share(inputs: Realism4Projected3yrAdjustmentSampleShareInputs) -> float | str:
    """Computes the Realism 4 projected 3-year fiscal-adjustment sample share at the country's projected-adjustment bin.

    Provides the percent-of-sample coordinate used when placing a country within the Realism 4 fiscal-adjustment distribution.

    Args:
        inputs: Typed Realism 4 projected 3-year adjustment sample-share coordinate bundle supplying the country's projected-adjustment bin and associated authored identities.

    Returns:
        The percent-of-sample value at the country's projected-adjustment bin as a float, or a string when the authored result is non-numeric.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentSampleShareInputs):
        raise TypeError(
            f"compute_realism4_projected_3yr_adjustment_sample_share() expected Realism4Projected3yrAdjustmentSampleShareInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism4_projected_3yr_adjustment_sample_share


@publish(key=(), domain=None, constants=_CONSTANTS_20, cells=data.REALISM4_FISCAL_ADJUSTMENT_TOP_BIN_LABEL_CELLS)
def compute_realism4_fiscal_adjustment_top_bin_label(inputs: Realism4FiscalAdjustmentTopBinLabelInputs) -> str | int | float | bool:
    """Return the open-ended top-bin label for the Realism 4 fiscal-adjustment histogram.

    Resolve the top-bin label from the supplied typed Realism 4 fiscal-adjustment inputs.

    Args:
        inputs: Typed input dataclass containing the data.* series and scalars that identify the Realism 4 fiscal-adjustment histogram top bin.

    Returns:
        The open-ended top-bin label as a scalar string, integer, float, or boolean.
    """
    if not isinstance(inputs, Realism4FiscalAdjustmentTopBinLabelInputs):
        raise TypeError(
            f"compute_realism4_fiscal_adjustment_top_bin_label() expected Realism4FiscalAdjustmentTopBinLabelInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism4_fiscal_adjustment_top_bin_label


@publish(data.REALISM4_FISCAL_ADJUSTMENT_SAMPLE_SHARE.schema, constants=_CONSTANTS_21, cells=data.REALISM4_FISCAL_ADJUSTMENT_SAMPLE_SHARE.cells)
def compute_realism4_fiscal_adjustment_sample_share(inputs: Realism4FiscalAdjustmentSampleShareInputs) -> data.Realism4FiscalAdjustmentSampleShare:
    """Compute the share of the LIC sample in each three-year fiscal-adjustment bin.

    Produces the Realism 4 sample-share series used for the fiscal-adjustment distribution.

    Args:
        inputs: Dataclass of typed data series supplying the Realism 4 fiscal-adjustment inputs over catalog coordinates.

    Returns:
        A data.Realism4FiscalAdjustmentSampleShare series giving the percent of the LIC sample in each three-year fiscal-adjustment bin.
    """
    if not isinstance(inputs, Realism4FiscalAdjustmentSampleShareInputs):
        raise TypeError(
            f"compute_realism4_fiscal_adjustment_sample_share() expected Realism4FiscalAdjustmentSampleShareInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism4_fiscal_adjustment_sample_share


@publish(data.REALISM4_FISCAL_ADJUSTMENT_CUMULATIVE_SHARE.schema, constants=_CONSTANTS_21, cells=data.REALISM4_FISCAL_ADJUSTMENT_CUMULATIVE_SHARE.cells)
def compute_realism4_fiscal_adjustment_cumulative_share(inputs: Realism4FiscalAdjustmentCumulativeShareInputs) -> data.Realism4FiscalAdjustmentCumulativeShare:
    """Compute the cumulative share of the LIC sample across fiscal-adjustment bins.

    Derives the Realism 4 fiscal-adjustment cumulative distribution used in the fiscal-adjustment chart series.

    Args:
        inputs: Typed `Realism4FiscalAdjustmentCumulativeShareInputs` dataclass supplying the fiscal-adjustment bin distribution inputs over catalog coordinates.

    Returns:
        `data.Realism4FiscalAdjustmentCumulativeShare` series giving the cumulative percent of the LIC sample up to each fiscal-adjustment bin.
    """
    if not isinstance(inputs, Realism4FiscalAdjustmentCumulativeShareInputs):
        raise TypeError(
            f"compute_realism4_fiscal_adjustment_cumulative_share() expected Realism4FiscalAdjustmentCumulativeShareInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).realism4_fiscal_adjustment_cumulative_share


@publish(data.PROBABILITY_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_22, cells=data.PROBABILITY_PV_DEBT_TO_GDP.cells)
def compute_probability_pv_debt_to_gdp(inputs: ProbabilityPvDebtToGdpInputs) -> data.ProbabilityPvDebtToGdp:
    """Compute the PV of PPG external debt to GDP probability-approach series.

    Derives the PV of PPG external debt-to-GDP indicator path — baseline, historical, MX shock, threshold, and probability bands — from the authored coordinate identities.

    Args:
        inputs: Typed input bundle for the probability PV debt-to-GDP calculation, supplying the macro-debt, external-debt, and scenario assumptions over the catalog's `TIME_PERIOD` coordinates, whose key set follows `input3_old_debt_service`.

    Returns:
        A `data.ProbabilityPvDebtToGdp` series over the catalog coordinates giving the PV of PPG external debt-to-GDP path with its baseline, historical, MX shock, threshold, and band values.
    """
    if not isinstance(inputs, ProbabilityPvDebtToGdpInputs):
        raise TypeError(
            f"compute_probability_pv_debt_to_gdp() expected ProbabilityPvDebtToGdpInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).probability_pv_debt_to_gdp


@publish(data.PROBABILITY_PV_DEBT_TO_EXPORTS.schema, constants=_CONSTANTS_23, cells=data.PROBABILITY_PV_DEBT_TO_EXPORTS.cells)
def compute_probability_pv_debt_to_exports(inputs: ProbabilityPvDebtToExportsInputs) -> data.ProbabilityPvDebtToExports:
    """Compute the probability-approach PV of PPG external debt-to-exports series.

    Derive baseline, historical, MX shock, threshold, and band paths over the catalog time coordinate from the supplied inputs.

    Args:
        inputs: Typed keyword-only input bundle carrying the macro, external-debt, probability, and scenario assumptions required for the PV debt-to-exports probability calculation.

    Returns:
        A typed data.ProbabilityPvDebtToExports series containing the baseline, historical, MX shock, threshold, and band paths for PV of PPG external debt to exports over TIME_PERIOD.
    """
    if not isinstance(inputs, ProbabilityPvDebtToExportsInputs):
        raise TypeError(
            f"compute_probability_pv_debt_to_exports() expected ProbabilityPvDebtToExportsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).probability_pv_debt_to_exports


@publish(data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS.schema, constants=_CONSTANTS_24, cells=data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS.cells)
def compute_probability_debt_service_to_exports(inputs: ProbabilityDebtServiceToExportsInputs) -> data.ProbabilityDebtServiceToExports:
    """Compute the probability-approach debt service-to-exports indicator series from the supplied LIC-DSF input bundle.

    Evaluate authored coordinate identities to produce the baseline, historical, MX-shock, threshold, and band paths aligned to the TIME_PERIOD coordinate.

    Args:
        inputs: Keyword-only typed input bundle containing the LIC-DSF macro, financing, stress, and probability-approach data-series inputs required for the calculation, including the old debt service series that defines the TIME_PERIOD coordinate.

    Returns:
        A typed data series for probability debt service to exports over TIME_PERIOD, containing baseline, historical, MX-shock, threshold, and band outputs.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToExportsInputs):
        raise TypeError(
            f"compute_probability_debt_service_to_exports() expected ProbabilityDebtServiceToExportsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).probability_debt_service_to_exports


@publish(data.PROBABILITY_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_25, cells=data.PROBABILITY_DEBT_SERVICE_TO_REVENUE.cells)
def compute_probability_debt_service_to_revenue(inputs: ProbabilityDebtServiceToRevenueInputs) -> data.ProbabilityDebtServiceToRevenue:
    """Compute the probability-approach PPG external debt service-to-revenue series.

    Derives the debt service-to-revenue indicator path and its probability framing (baseline, historical, MX shock, threshold, and bands) from the supplied inputs, with `TIME_PERIOD` keys determined by `input3_old_debt_service`.

    Args:
        inputs: Keyword-only typed input bundle (`ProbabilityDebtServiceToRevenueInputs`) supplying the debt service and revenue components, including `input3_old_debt_service`, that establish the `TIME_PERIOD` coordinate grid and drive the indicator computation.

    Returns:
        A `data.ProbabilityDebtServiceToRevenue` series over `TIME_PERIOD` containing the baseline debt service-to-revenue path together with its historical average, MX shock, threshold, and probability bands.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToRevenueInputs):
        raise TypeError(
            f"compute_probability_debt_service_to_revenue() expected ProbabilityDebtServiceToRevenueInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).probability_debt_service_to_revenue


@publish(data.PROBABILITY_PV_DEBT_TO_GDP_DISTRESS.schema, constants=_CONSTANTS_26, cells=data.PROBABILITY_PV_DEBT_TO_GDP_DISTRESS.cells)
def compute_probability_pv_debt_to_gdp_distress(inputs: ProbabilityPvDebtToGdpDistressInputs) -> data.ProbabilityPvDebtToGdpDistress:
    """Compute the probability of external-debt distress for the PV of debt-to-GDP ratio.

    Derives baseline, historical, MX, and threshold distress probabilities for PV debt/GDP from the supplied scenario inputs.

    Args:
        inputs: Keyword-only bundle of probability-approach inputs; its `TIME_PERIOD` axis is taken from `input3_old_debt_service`, and its typed series supply the PV debt/GDP indicator paths and shock settings used to evaluate distress.

    Returns:
        A `data.ProbabilityPvDebtToGdpDistress` series holding the PV debt/GDP distress probabilities for baseline, historical, MX, and threshold cases along the `TIME_PERIOD` axis.
    """
    if not isinstance(inputs, ProbabilityPvDebtToGdpDistressInputs):
        raise TypeError(
            f"compute_probability_pv_debt_to_gdp_distress() expected ProbabilityPvDebtToGdpDistressInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).probability_pv_debt_to_gdp_distress


@publish(data.PROBABILITY_PV_DEBT_TO_EXPORTS_DISTRESS.schema, constants=_CONSTANTS_27, cells=data.PROBABILITY_PV_DEBT_TO_EXPORTS_DISTRESS.cells)
def compute_probability_pv_debt_to_exports_distress(inputs: ProbabilityPvDebtToExportsDistressInputs) -> data.ProbabilityPvDebtToExportsDistress:
    """Compute PV debt-to-exports distress probabilities across baseline, historical, MX, and threshold paths.

    Derive the probability of external-debt distress for the PV debt-to-exports indicator from the configured scenario inputs.

    Args:
        inputs: Keyword-only input series carrying the PV debt-to-exports indicator paths, shock scenarios, historical averages, and thresholds over the catalog's named-axis coordinates.

    Returns:
        A data.ProbabilityPvDebtToExportsDistress series giving the distress probability for each scenario path along the named-axis coordinates.
    """
    if not isinstance(inputs, ProbabilityPvDebtToExportsDistressInputs):
        raise TypeError(
            f"compute_probability_pv_debt_to_exports_distress() expected ProbabilityPvDebtToExportsDistressInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).probability_pv_debt_to_exports_distress


@publish(data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS_DISTRESS.schema, constants=_CONSTANTS_28, cells=data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS_DISTRESS.cells)
def compute_probability_debt_service_to_exports_distress(inputs: ProbabilityDebtServiceToExportsDistressInputs) -> data.ProbabilityDebtServiceToExportsDistress:
    """Compute external-debt distress probabilities from the debt service-to-exports ratio.

    Derive baseline, historical, MX, and threshold distress probability series for the debt service-to-exports indicator.

    Args:
        inputs: ProbabilityDebtServiceToExportsDistressInputs dataclass supplying the debt service-to-exports series and related macro/financing inputs for probability-path calculation.

    Returns:
        A data.ProbabilityDebtServiceToExportsDistress series containing baseline, historical, MX, and threshold distress probabilities.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToExportsDistressInputs):
        raise TypeError(
            f"compute_probability_debt_service_to_exports_distress() expected ProbabilityDebtServiceToExportsDistressInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).probability_debt_service_to_exports_distress


@publish(data.PROBABILITY_DEBT_SERVICE_TO_REVENUE_DISTRESS.schema, constants=_CONSTANTS_29, cells=data.PROBABILITY_DEBT_SERVICE_TO_REVENUE_DISTRESS.cells)
def compute_probability_debt_service_to_revenue_distress(inputs: ProbabilityDebtServiceToRevenueDistressInputs) -> data.ProbabilityDebtServiceToRevenueDistress:
    """Compute debt service-to-revenue distress probabilities across baseline, historical, MX, and threshold scenarios.

    Evaluates authored coordinate identities to derive the external-debt distress probability for the debt service-to-revenue indicator.

    Args:
        inputs: Typed input bundle containing the debt service-to-revenue probability assumptions and the coordinate identities used to define the TIME_PERIOD grid.

    Returns:
        A data.ProbabilityDebtServiceToRevenueDistress series of external-debt distress probabilities for debt service/revenue under baseline, historical, MX, and threshold scenarios over TIME_PERIOD.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToRevenueDistressInputs):
        raise TypeError(
            f"compute_probability_debt_service_to_revenue_distress() expected ProbabilityDebtServiceToRevenueDistressInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).probability_debt_service_to_revenue_distress


@publish(key=(), domain=None, constants=_CONSTANTS_30, cells=data.EXTERNAL_DSA_RISK_RATING_SIGNAL_CELLS)
def compute_external_dsa_risk_rating_signal(inputs: ExternalDsaRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute the external DSA risk-rating signal.

    Returns the Chart Data risk-rating text signal for the external debt sustainability assessment from the supplied inputs.

    Args:
        inputs: Typed input bundle of coordinate identities for the external DSA risk-rating signal calculation.

    Returns:
        The external DSA risk-rating signal as a string, integer, float, or boolean scalar.
    """
    if not isinstance(inputs, ExternalDsaRiskRatingSignalInputs):
        raise TypeError(
            f"compute_external_dsa_risk_rating_signal() expected ExternalDsaRiskRatingSignalInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).external_dsa_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_31, cells=data.EXTERNAL_DSA_RISK_RATING_NUMERIC_CELLS)
def compute_external_dsa_risk_rating_numeric(inputs: ExternalDsaRiskRatingNumericInputs) -> float | str:
    """Compute the numeric external DSA risk-rating signal from authored workbook coordinate identities.

    Resolve the external DSA risk-rating signal exposed on Chart Data!D11 as either a numeric code or a string label.

    Args:
        inputs: Typed input bundle of data.* series and scalars supplying the workbook-coordinate values required to resolve the external DSA risk-rating numeric signal.

    Returns:
        The external DSA risk-rating signal as a float numeric code when the source resolves numerically, or as a str label when it resolves as text.
    """
    if not isinstance(inputs, ExternalDsaRiskRatingNumericInputs):
        raise TypeError(
            f"compute_external_dsa_risk_rating_numeric() expected ExternalDsaRiskRatingNumericInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).external_dsa_risk_rating_numeric


@publish(key=(), domain=None, constants=_CONSTANTS_31, cells=data.EXTERNAL_BASELINE_BREACH_CELLS)
def compute_external_baseline_breach(inputs: ExternalBaselineBreachInputs) -> float | str:
    """Compute the Chart Data external baseline breach flag from bound LIC-DSF inputs.

    Evaluates the model’s external baseline breach signal, excluding 1-year breaches, as a scalar flag for downstream risk-rating outputs.

    Args:
        inputs: A typed ExternalBaselineBreachInputs dataclass containing the pre-bound coordinate series and scalars required to evaluate the external baseline breach calculation.

    Returns:
        The external baseline breach flag as 0 for no breach or 1 for breach, excluding 1-year breaches; the annotation permits a string when the model emits a textual value.
    """
    if not isinstance(inputs, ExternalBaselineBreachInputs):
        raise TypeError(
            f"compute_external_baseline_breach() expected ExternalBaselineBreachInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).external_baseline_breach


@publish(key=(), domain=None, constants=_CONSTANTS_31, cells=data.EXTERNAL_SHOCK_BREACH_CELLS)
def compute_external_shock_breach(inputs: ExternalShockBreachInputs) -> float | str:
    """Compute the external shock breach indicator from authored coordinate identities.

    Evaluate the LIC-DSF external shock breach flag used in Chart Data risk-rating signals.

    Args:
        inputs: Typed input dataclass bundling the data series and scalar parameters required to evaluate the external shock breach.

    Returns:
        External shock breach flag as 0.0/1.0 float or a string label, per Chart Data!D13, excluding one-year breaches.
    """
    if not isinstance(inputs, ExternalShockBreachInputs):
        raise TypeError(
            f"compute_external_shock_breach() expected ExternalShockBreachInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).external_shock_breach


@publish(key=(), domain=None, constants=_CONSTANTS_32, cells=data.EXTERNAL_PV_DEBT_TO_GDP_MX_SHOCK_CELLS)
def compute_external_pv_debt_to_gdp_mx_shock(inputs: ExternalPvDebtToGdpMxShockInputs) -> str | int | float | bool:
    """Return the external PV debt-to-GDP MX shock label for the supplied LIC-DSF inputs.

    Computes the Chart Data MX-shock scalar representing the PV of debt-to-GDP ratio shock value or label.

    Args:
        inputs: Typed external PV debt-to-GDP MX-shock inputs, carrying the model coordinates required to evaluate the Chart Data MX-shock identity.

    Returns:
        A scalar MX-shock result, typed as str, int, float, or bool, for the PV of debt-to-GDP ratio MX shock.
    """
    if not isinstance(inputs, ExternalPvDebtToGdpMxShockInputs):
        raise TypeError(
            f"compute_external_pv_debt_to_gdp_mx_shock() expected ExternalPvDebtToGdpMxShockInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).external_pv_debt_to_gdp_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_33, cells=data.EXTERNAL_PV_DEBT_TO_EXPORTS_MX_SHOCK_CELLS)
def compute_external_pv_debt_to_exports_mx_shock(inputs: ExternalPvDebtToExportsMxShockInputs) -> str | int | float | bool:
    """Compute the external PV debt-to-exports MX shock label.

    Extracts the Chart Data!D15 signal for the PV of debt-to-exports ratio MX shock.

    Args:
        inputs: Typed input dataclass carrying the external PV debt-to-exports MX shock computation inputs.

    Returns:
        Scalar external PV debt-to-exports MX shock label from Chart Data!D15, returned as str, int, float, or bool.
    """
    if not isinstance(inputs, ExternalPvDebtToExportsMxShockInputs):
        raise TypeError(
            f"compute_external_pv_debt_to_exports_mx_shock() expected ExternalPvDebtToExportsMxShockInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).external_pv_debt_to_exports_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_34, cells=data.EXTERNAL_DEBT_SERVICE_TO_EXPORTS_MX_SHOCK_CELLS)
def compute_external_debt_service_to_exports_mx_shock(inputs: ExternalDebtServiceToExportsMxShockInputs) -> str | int | float | bool:
    """Compute the external debt service-to-exports MX shock label from the Chart Data risk-rating block.

    Resolves the MX shock label for the debt service-to-exports indicator (Chart Data!D16) via authored coordinate identities over the typed input series.

    Args:
        inputs: Keyword-only ExternalDebtServiceToExportsMxShockInputs bundle of typed data.* series (named-axis tensors over catalog coordinates) supplying the coordinate identities needed to resolve the MX shock label.

    Returns:
        Scalar MX shock label for the external debt service-to-exports ratio, typed as str | int | float | bool as recorded on Chart Data!D16.
    """
    if not isinstance(inputs, ExternalDebtServiceToExportsMxShockInputs):
        raise TypeError(
            f"compute_external_debt_service_to_exports_mx_shock() expected ExternalDebtServiceToExportsMxShockInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).external_debt_service_to_exports_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_35, cells=data.EXTERNAL_DEBT_SERVICE_TO_REVENUE_MX_SHOCK_CELLS)
def compute_external_debt_service_to_revenue_mx_shock(inputs: ExternalDebtServiceToRevenueMxShockInputs) -> str | int | float | bool:
    """Return the external debt service-to-revenue MX shock label from the LIC-DSF Chart Data risk-rating block.

    Extracts the Market (MX) shock signal recorded at `Chart Data!D17` so downstream DSA write-up code can read the external debt service-to-revenue shock label without touching the workbook.

    Args:
        inputs: Keyword-only dataclass of `data.*` series and scalars supplying the external debt service-to-revenue inputs (debt service, revenue, and scenario assumptions) from which the Chart Data MX shock label is resolved.

    Returns:
        The external debt service-to-revenue MX shock label as a scalar — text or numeric rating, or a boolean flag — exactly as it appears on `Chart Data!D17`.
    """
    if not isinstance(inputs, ExternalDebtServiceToRevenueMxShockInputs):
        raise TypeError(
            f"compute_external_debt_service_to_revenue_mx_shock() expected ExternalDebtServiceToRevenueMxShockInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).external_debt_service_to_revenue_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_36, cells=data.FISCAL_RISK_RATING_SIGNAL_CELLS)
def compute_fiscal_risk_rating_signal(inputs: FiscalRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute the fiscal (total public debt) risk-rating signal from the Chart Data model.

    Resolve the Fiscal risk-rating text/numeric signal cell (Chart Data!I10) from authored coordinate identities so downstream DSA logic can read the external fiscal rating.

    Args:
        inputs: FiscalRiskRatingSignalInputs dataclass bundling the coordinate series and scalar overrides that feed the fiscal risk-rating identity.

    Returns:
        Scalar fiscal risk-rating signal (rating text or numeric code, or a breach/flag value), typed str | int | float | bool.
    """
    if not isinstance(inputs, FiscalRiskRatingSignalInputs):
        raise TypeError(
            f"compute_fiscal_risk_rating_signal() expected FiscalRiskRatingSignalInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).fiscal_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_37, cells=data.FISCAL_RISK_RATING_NUMERIC_CELLS)
def compute_fiscal_risk_rating_numeric(inputs: FiscalRiskRatingNumericInputs) -> float | str:
    """Compute the fiscal (total public debt) risk-rating numeric code from Chart Data signals.

    Resolve the fiscal risk-rating coordinate on Chart Data!I11 into its numeric or textual signal form.

    Args:
        inputs: A typed dataclass bundling the data.* series and scalar settings that identify the fiscal risk-rating coordinate and its model inputs.

    Returns:
        A float numeric risk-rating code, or a str when the rating is represented as text.
    """
    if not isinstance(inputs, FiscalRiskRatingNumericInputs):
        raise TypeError(
            f"compute_fiscal_risk_rating_numeric() expected FiscalRiskRatingNumericInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).fiscal_risk_rating_numeric


@publish(key=(), domain=None, constants=_CONSTANTS_37, cells=data.FISCAL_BASELINE_BREACH_CELLS)
def compute_fiscal_baseline_breach(inputs: FiscalBaselineBreachInputs) -> float | str:
    """Compute the fiscal baseline breach flag from a FiscalBaselineBreachInputs bundle.

    Evaluates the authored coordinate identities to determine whether total public debt breaches its baseline threshold, excluding one-year breaches.

    Args:
        inputs: FiscalBaselineBreachInputs bundle supplying the named-axis catalog coordinate series and scalars needed to evaluate the baseline breach identity.

    Returns:
        The fiscal baseline breach flag as a float of 0 (no breach) or 1 (breach, excluding one-year breaches), or a str where the workbook records a text label instead of a numeric flag.
    """
    if not isinstance(inputs, FiscalBaselineBreachInputs):
        raise TypeError(
            f"compute_fiscal_baseline_breach() expected FiscalBaselineBreachInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).fiscal_baseline_breach


@publish(key=(), domain=None, constants=_CONSTANTS_37, cells=data.FISCAL_SHOCK_BREACH_CELLS)
def compute_fiscal_shock_breach(inputs: FiscalShockBreachInputs) -> float | str:
    """Computes the fiscal shock breach flag from authored catalog coordinate identities.

    Returns the fiscal (total public debt) shock breach indicator used in Chart Data risk-rating signals.

    Args:
        inputs: A FiscalShockBreachInputs dataclass of typed data.* series and scalar inputs over catalog coordinates needed to evaluate the fiscal shock breach flag.

    Returns:
        The Chart Data!I13 shock breach signal as a 0/1 float, or a str when the indicator is represented textually; 0 means no breach and 1 means breach excluding 1-year breaches.
    """
    if not isinstance(inputs, FiscalShockBreachInputs):
        raise TypeError(
            f"compute_fiscal_shock_breach() expected FiscalShockBreachInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).fiscal_shock_breach


@publish(key=(), domain=None, constants=_CONSTANTS_38, cells=data.FISCAL_PV_DEBT_TO_GDP_MX_SHOCK_CELLS)
def compute_fiscal_pv_debt_to_gdp_mx_shock(inputs: FiscalPvDebtToGdpMxShockInputs) -> str | int | float | bool:
    """Compute the fiscal PV debt-to-GDP MX shock element from Chart Data!I14.

    Evaluates the authored coordinate identity for the public-debt PV of debt-to-GDP ratio MX shock shock level, resolving it from the fiscal shock inputs and returning the resulting scalar label.

    Args:
        inputs: FiscalPvDebtToGdpMxShockInputs dataclass holding the keyword-only fiscal public-debt shock parameters (country, vintage, debt coverage, macro-debt projections, and standardized stress options) that determine the Chart Data!I14 MX shock value.

    Returns:
        Scalar str | int | float | bool value of the fiscal PV debt-to-GDP MX shock element, either a text label or the corresponding numeric shock value as stored on Chart Data!I14.
    """
    if not isinstance(inputs, FiscalPvDebtToGdpMxShockInputs):
        raise TypeError(
            f"compute_fiscal_pv_debt_to_gdp_mx_shock() expected FiscalPvDebtToGdpMxShockInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).fiscal_pv_debt_to_gdp_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_39, cells=data.TAILORED_STRESS_NATURAL_DISASTER_APPLICABLE_CELLS)
def compute_tailored_stress_natural_disaster_applicable(inputs: TailoredStressNaturalDisasterApplicableInputs) -> float | str:
    """Compute the natural-disaster tailored-stress applicability flag from authored coordinate identities.

    Evaluate whether the natural-disaster tailored stress test applies for the current LIC-DSF scenario.

    Args:
        inputs: Dataclass of named-axis series and scalars supplying the authored coordinate identities needed to evaluate natural-disaster tailored-stress applicability.

    Returns:
        Applicability indicator for the natural-disaster tailored stress test, returned as a numeric 0/1 flag or a string label from the workbook.
    """
    if not isinstance(inputs, TailoredStressNaturalDisasterApplicableInputs):
        raise TypeError(
            f"compute_tailored_stress_natural_disaster_applicable() expected TailoredStressNaturalDisasterApplicableInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).tailored_stress_natural_disaster_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_40, cells=data.TAILORED_STRESS_COMMODITY_PRICE_APPLICABLE_CELLS)
def compute_tailored_stress_commodity_price_applicable(inputs: TailoredStressCommodityPriceApplicableInputs) -> float | str:
    """Compute the commodity-price tailored stress applicability indicator from authored coordinate identities.

    Resolves whether the commodity-price tailored stress test applies, returning the Chart Data 0/1 applicability flag or its string form.

    Args:
        inputs: Typed input dataclass carrying the authored coordinate identities and source series used to resolve the commodity-price tailored stress applicability flag.

    Returns:
        The commodity-price tailored stress applicability indicator as a float (0/1) or string representation from the model.
    """
    if not isinstance(inputs, TailoredStressCommodityPriceApplicableInputs):
        raise TypeError(
            f"compute_tailored_stress_commodity_price_applicable() expected TailoredStressCommodityPriceApplicableInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).tailored_stress_commodity_price_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_41, cells=data.TAILORED_STRESS_MARKET_FINANCING_APPLICABLE_CELLS)
def compute_tailored_stress_market_financing_applicable(inputs: TailoredStressMarketFinancingApplicableInputs) -> float | str:
    """Compute the market-financing tailored stress applicability flag from the authored input identities.

    Resolves whether the market-financing tailored stress test applies using the provided model inputs and returns the corresponding Chart Data signal.

    Args:
        inputs: Inputs dataclass containing the named-axis series and scalar values required to resolve market-financing tailored stress applicability.

    Returns:
        The market-financing tailored stress applicability value as a float or string, matching the annotated model output.
    """
    if not isinstance(inputs, TailoredStressMarketFinancingApplicableInputs):
        raise TypeError(
            f"compute_tailored_stress_market_financing_applicable() expected TailoredStressMarketFinancingApplicableInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).tailored_stress_market_financing_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_42, cells=data.FISCAL_SPACE_MODERATE_RISK_SIGNAL_CELLS)
def compute_fiscal_space_moderate_risk_signal(inputs: FiscalSpaceModerateRiskSignalInputs) -> str | int | float | bool:
    """Compute the moderate-risk fiscal-space signal from authored Chart Data coordinates.

    Resolves the fiscal-space moderate-risk indicator (Chart Data!D23) for the LIC-DSF template.

    Args:
        inputs: Typed inputs dataclass carrying the named-axis coordinate series and scalar settings needed to resolve the moderate-risk fiscal-space cell.

    Returns:
        Scalar moderate-risk fiscal-space signal from Chart Data!D23, returned as text or a numeric/boolean value per the computed cell.
    """
    if not isinstance(inputs, FiscalSpaceModerateRiskSignalInputs):
        raise TypeError(
            f"compute_fiscal_space_moderate_risk_signal() expected FiscalSpaceModerateRiskSignalInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).fiscal_space_moderate_risk_signal


@publish(key=(), domain=None, constants=_CONSTANTS_43, cells=data.OVERALL_RISK_RATING_SIGNAL_CELLS)
def compute_overall_risk_rating_signal(inputs: OverallRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute the overall combined external-plus-fiscal risk-rating signal.

    Reads the Chart Data overall rating cell as a text or scalar signal suitable for external risk-rating display.

    Args:
        inputs: Typed input bundle holding the overall risk-rating coordinate identities and scenario settings required to evaluate the combined rating.

    Returns:
        The overall risk-rating signal as a string rating label or a numeric/boolean scalar, depending on the resolved cell value.
    """
    if not isinstance(inputs, OverallRiskRatingSignalInputs):
        raise TypeError(
            f"compute_overall_risk_rating_signal() expected OverallRiskRatingSignalInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).overall_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_44, cells=data.OVERALL_RISK_RATING_NUMERIC_CELLS)
def compute_overall_risk_rating_numeric(inputs: OverallRiskRatingNumericInputs) -> float | str:
    """Compute the numeric overall risk-rating code from the combined external and fiscal rating signals.

    Resolve the Chart Data!L11 overall rating as a numeric code derived from authored risk-rating coordinate identities.

    Args:
        inputs: Dataclass of named-axis risk-rating series supplying the external and fiscal signals that form the combined overall rating.

    Returns:
        Overall combined risk-rating numeric code as a float, or a string when the workbook emits a text/qualitative signal instead of a numeric code.
    """
    if not isinstance(inputs, OverallRiskRatingNumericInputs):
        raise TypeError(
            f"compute_overall_risk_rating_numeric() expected OverallRiskRatingNumericInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).overall_risk_rating_numeric


@publish(data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_GDP_RATIO_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_45, cells=data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_GDP_RATIO_PV_DEBT_TO_GDP.cells)
def compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp(inputs: ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs) -> data.ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdp:
    """Compute the PV of Debt-to-GDP Ratio chart-data series for the LIC-DSF Chart Data sheet.

    Evaluates the authored coordinate identities that populate the public-debt PV of Debt-to-GDP chart block across the standard scenario ladder.

    Args:
        inputs: Dataclass of keyword-only inputs supplying the scenario ladder and projection-year coordinates that parameterize the PV of Debt-to-GDP Ratio chart series; it aggregates the bound input series rather than acting as a single series itself.

    Returns:
        `data.ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdp` series: the PV of Debt-to-GDP Ratio on Chart Data over the projection-year grid, keyed by scenario (Baseline, A1 historical, B1–B6, C1–C4, A2 customized).
    """
    if not isinstance(inputs, ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs):
        raise TypeError(
            f"compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp() expected ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp


@publish(data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_REVENUE_RATIO_PV_DEBT_TO_REVENUE.schema, constants=_CONSTANTS_46, cells=data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_REVENUE_RATIO_PV_DEBT_TO_REVENUE.cells)
def compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue(inputs: ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs) -> data.ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenue:
    """Compute the Chart Data PV of Debt-to-Revenue ratio series across scenarios.

    Evaluates the PV of public debt-to-revenue ratio projection ladder used by the LIC-DSF public-debt stress charts.

    Args:
        inputs: Keyword-only dataclass of input series supplying macro, debt, revenue, and stress-scenario assumptions that drive the PV of Debt-to-Revenue ratio identities, with the projection grid aligned to the debt-service history.

    Returns:
        A `data.ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenue` series of PV of Debt-to-Revenue ratios on the Chart Data year grid, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs):
        raise TypeError(
            f"compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue() expected ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue


@publish(data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_REVENUE_RATIO_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_47, cells=data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_REVENUE_RATIO_DEBT_SERVICE_TO_REVENUE.cells)
def compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue(inputs: ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs) -> data.ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenue:
    """Compute the Debt Service-to-Revenue Ratio chart series from authored coordinate identities.

    Derives the `Chart Data` Debt Service-to-Revenue Ratio series, keyed by scenario along `TIME_PERIOD`, from the supplied input series.

    Args:
        inputs: Typed input container holding the named-axis `data.*` series and scalars used to resolve the Debt Service-to-Revenue Ratio coordinates.

    Returns:
        A `data.ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenue` series of Debt Service-to-Revenue Ratio values keyed by scenario along `TIME_PERIOD`.
    """
    if not isinstance(inputs, ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs):
        raise TypeError(
            f"compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue() expected ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue


@publish(data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_GDP_RATIO_DEBT_SERVICE_GDP_RATIO.schema, constants=_CONSTANTS_47, cells=data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_GDP_RATIO_DEBT_SERVICE_GDP_RATIO.cells)
def compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio(inputs: ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs) -> data.ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatio:
    """Compute the Chart Data debt service-to-GDP ratio series from authored coordinate inputs.

    Builds the scenario-keyed debt service-to-GDP ratio output for the Chart Data surface.

    Args:
        inputs: Typed inputs dataclass containing the authored coordinate identities used to compute the Chart Data debt service-to-GDP ratio.

    Returns:
        A typed Chart Data debt service-to-GDP ratio series keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs):
        raise TypeError(
            f"compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio() expected ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio


@publish(data.CHART_PV_DEBT_GDP_RATIO_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_48, cells=data.CHART_PV_DEBT_GDP_RATIO_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_pv_debt_gdp_ratio_custom_alternative_scenario(inputs: ChartPvDebtGdpRatioCustomAlternativeScenarioInputs) -> data.ChartPvDebtGdpRatioCustomAlternativeScenario:
    """Compute the Chart Data PV of debt-to-GDP ratio path for the A2 customized alternative scenario.

    Evaluates the Chart Data row 51 series (PV of debt-to GDP ratio, A2 alternative scenario) over the projection year grid so the customized scenario can be charted alongside the baseline and standard stress ladder.

    Args:
        inputs: Typed input dataclass carrying the customized alternative-scenario assumptions and the upstream macro, debt, and discount-rate series required to evaluate the A2 scenario; its TIME_PERIOD axis is determined by input3_old_debt_service.

    Returns:
        A `data.ChartPvDebtGdpRatioCustomAlternativeScenario` series: PV of debt-to-GDP ratio values for the customized A2 scenario indexed along TIME_PERIOD, on the same year grid as Chart Data row 35.
    """
    if not isinstance(inputs, ChartPvDebtGdpRatioCustomAlternativeScenarioInputs):
        raise TypeError(
            f"compute_chart_pv_debt_gdp_ratio_custom_alternative_scenario() expected ChartPvDebtGdpRatioCustomAlternativeScenarioInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_pv_debt_gdp_ratio_custom_alternative_scenario


@publish(data.CHART_OUTPUT_PV_DEBT_GDP_RATIO.schema, constants=_CONSTANTS_49, cells=data.CHART_OUTPUT_PV_DEBT_GDP_RATIO.cells)
def compute_chart_output_pv_debt_gdp_ratio(inputs: ChartOutputPvDebtGdpRatioInputs) -> data.ChartOutputPvDebtGdpRatio:
    """Computes the Chart Data PV of debt-to-GDP ratio series by scenario.

    Produces the public-debt stress metric used in the LIC-DSF chart outputs from the authored input bundle.

    Args:
        inputs: Keyword-only input bundle supplying the scenario and model parameters required to compute the Chart Data PV of debt-to-GDP ratio series.

    Returns:
        A `data.ChartOutputPvDebtGdpRatio` data series containing PV of debt-to-GDP ratios on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputPvDebtGdpRatioInputs):
        raise TypeError(
            f"compute_chart_output_pv_debt_gdp_ratio() expected ChartOutputPvDebtGdpRatioInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_output_pv_debt_gdp_ratio


@publish(data.CHART_PV_DEBT_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_48, cells=data.CHART_PV_DEBT_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_pv_debt_to_exports_custom_alternative_scenario(inputs: ChartPvDebtToExportsCustomAlternativeScenarioInputs) -> data.ChartPvDebtToExportsCustomAlternativeScenario:
    """Compute the PV of debt-to-exports ratio for the customized alternative scenario.

    Evaluates Chart Data row 93, the A2 customized alternative-scenario PV of debt-to-exports path, from the supplied scenario inputs.

    Args:
        inputs: Typed input bundle of named-axis Chart Data series and scalar scenario settings used to compute the customized alternative-scenario debt-to-exports path.

    Returns:
        The computed data.ChartPvDebtToExportsCustomAlternativeScenario series, giving the PV of debt-to-exports ratio along the projection-year coordinate from Chart Data row 35.
    """
    if not isinstance(inputs, ChartPvDebtToExportsCustomAlternativeScenarioInputs):
        raise TypeError(
            f"compute_chart_pv_debt_to_exports_custom_alternative_scenario() expected ChartPvDebtToExportsCustomAlternativeScenarioInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_pv_debt_to_exports_custom_alternative_scenario


@publish(data.CHART_OUTPUT_PV_DEBT_TO_EXPORTS.schema, constants=_CONSTANTS_50, cells=data.CHART_OUTPUT_PV_DEBT_TO_EXPORTS.cells)
def compute_chart_output_pv_debt_to_exports(inputs: ChartOutputPvDebtToExportsInputs) -> data.ChartOutputPvDebtToExports:
    """Compute the PV of debt-to-exports ratio series for Chart Data.

    Produce the scenario-keyed PV debt-to-exports chart output from the supplied chart-output inputs.

    Args:
        inputs: The chart-output inputs dataclass supplying the typed data series and scalar settings needed to compute the PV debt-to-exports output.

    Returns:
        A data.ChartOutputPvDebtToExports series containing the PV of debt-to-exports ratio, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputPvDebtToExportsInputs):
        raise TypeError(
            f"compute_chart_output_pv_debt_to_exports() expected ChartOutputPvDebtToExportsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_output_pv_debt_to_exports


@publish(data.CHART_DEBT_SERVICE_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_51, cells=data.CHART_DEBT_SERVICE_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_debt_service_to_exports_custom_alternative_scenario(inputs: ChartDebtServiceToExportsCustomAlternativeScenarioInputs) -> data.ChartDebtServiceToExportsCustomAlternativeScenario:
    """Compute the customized alternative-scenario debt service-to-exports chart series.

    Produces the Chart Data row 135 A2 customized alternative-scenario series for the debt service-to-exports ratio over projection years from row 35.

    Args:
        inputs: Typed bundle of named-axis data-series inputs and scalar assumptions used for the customized alternative-scenario calculation.

    Returns:
        A data.ChartDebtServiceToExportsCustomAlternativeScenario series for Chart Data row 135, the debt service-to-exports ratio under the A2 customized alternative scenario, indexed over the projection years from row 35.
    """
    if not isinstance(inputs, ChartDebtServiceToExportsCustomAlternativeScenarioInputs):
        raise TypeError(
            f"compute_chart_debt_service_to_exports_custom_alternative_scenario() expected ChartDebtServiceToExportsCustomAlternativeScenarioInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_debt_service_to_exports_custom_alternative_scenario


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_EXPORTS.schema, constants=_CONSTANTS_52, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_EXPORTS.cells)
def compute_chart_output_debt_service_to_exports(inputs: ChartOutputDebtServiceToExportsInputs) -> data.ChartOutputDebtServiceToExports:
    """Compute the debt service-to-exports chart series from authored coordinate identities.

    Produce the Chart Data debt service-to-exports ratio series keyed by scenario over the projection time axis.

    Args:
        inputs: Input bundle of named-axis series and scalars supplying the debt service-to-exports chart calculation.

    Returns:
        A data.ChartOutputDebtServiceToExports named-axis series containing the debt service-to-exports ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputDebtServiceToExportsInputs):
        raise TypeError(
            f"compute_chart_output_debt_service_to_exports() expected ChartOutputDebtServiceToExportsInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_output_debt_service_to_exports


@publish(data.CHART_DEBT_SERVICE_TO_REVENUE_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_51, cells=data.CHART_DEBT_SERVICE_TO_REVENUE_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_debt_service_to_revenue_custom_alternative_scenario(inputs: ChartDebtServiceToRevenueCustomAlternativeScenarioInputs) -> data.ChartDebtServiceToRevenueCustomAlternativeScenario:
    """Compute the customized alternative-scenario debt service-to-revenue chart series.

    Derive the Chart Data row 177 customized-scenario ratio across projection years from the supplied inputs.

    Args:
        inputs: Typed input bundle containing the customized alternative-scenario assumptions and catalog-aligned series required to evaluate the chart calculation.

    Returns:
        The computed debt service-to-revenue customized alternative-scenario series for Chart Data row 177, aligned to the projection-year grid from row 35.
    """
    if not isinstance(inputs, ChartDebtServiceToRevenueCustomAlternativeScenarioInputs):
        raise TypeError(
            f"compute_chart_debt_service_to_revenue_custom_alternative_scenario() expected ChartDebtServiceToRevenueCustomAlternativeScenarioInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_debt_service_to_revenue_custom_alternative_scenario


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_53, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE.cells)
def compute_chart_output_debt_service_to_revenue(inputs: ChartOutputDebtServiceToRevenueInputs) -> data.ChartOutputDebtServiceToRevenue:
    """Computes the Chart Data debt service-to-revenue ratio series by scenario.

    Derives the published debt service-to-revenue chart output from the supplied input bundle using authored coordinate identities.

    Args:
        inputs: Keyword-only input bundle of named-axis series and scalar assumptions that supply the debt service and revenue identities, including the time-axis coverage for old debt service.

    Returns:
        A scenario-keyed Chart Data series containing the debt service-to-revenue ratio.
    """
    if not isinstance(inputs, ChartOutputDebtServiceToRevenueInputs):
        raise TypeError(
            f"compute_chart_output_debt_service_to_revenue() expected ChartOutputDebtServiceToRevenueInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_output_debt_service_to_revenue


@publish(data.CHART_OUTPUT_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_45, cells=data.CHART_OUTPUT_PV_DEBT_TO_GDP.cells)
def compute_chart_output_pv_debt_to_gdp(inputs: ChartOutputPvDebtToGdpInputs) -> data.ChartOutputPvDebtToGdp:
    """Compute the Chart Data PV of Debt-to-GDP ratio series by scenario.

    Projects public-debt PV-to-GDP ratios across the DSA scenario ladder for chart and stress-chart outputs.

    Args:
        inputs: Keyword-only input bundle of Chart Data coordinate series and scalars used to derive the PV of Debt-to-GDP projection paths.

    Returns:
        A data.ChartOutputPvDebtToGdp series of projected PV of Debt-to-GDP ratios on Chart Data, keyed by scenario over the projection time grid.
    """
    if not isinstance(inputs, ChartOutputPvDebtToGdpInputs):
        raise TypeError(
            f"compute_chart_output_pv_debt_to_gdp() expected ChartOutputPvDebtToGdpInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_output_pv_debt_to_gdp


@publish(data.CHART_PV_DEBT_TO_REVENUE_MX_SHOCK_STANDARD_TAILORED.schema, constants=_CONSTANTS_46, cells=data.CHART_PV_DEBT_TO_REVENUE_MX_SHOCK_STANDARD_TAILORED.cells)
def compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored(inputs: ChartPvDebtToRevenueMxShockStandardTailoredInputs) -> data.ChartPvDebtToRevenueMxShockStandardTailored:
    """Compute the PV of Debt-to-Revenue Ratio under the MX shock Standard&Tailored scenario from Chart Data row 306.

    Produces the named-axis stress-chart series over the workbook projection years for public Chart Data extraction.

    Args:
        inputs: Typed input bundle of named-axis series and scalar settings; `TIME_PERIOD` keys are determined by the old debt-service series.

    Returns:
        A `data.ChartPvDebtToRevenueMxShockStandardTailored` named-axis series over `TIME_PERIOD`, aligned to the Chart Data row 306 year grid.
    """
    if not isinstance(inputs, ChartPvDebtToRevenueMxShockStandardTailoredInputs):
        raise TypeError(
            f"compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored() expected ChartPvDebtToRevenueMxShockStandardTailoredInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_pv_debt_to_revenue_mx_shock_standard_tailored


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE_FISCAL.schema, constants=_CONSTANTS_47, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE_FISCAL.cells)
def compute_chart_output_debt_service_to_revenue_fiscal(inputs: ChartOutputDebtServiceToRevenueFiscalInputs) -> data.ChartOutputDebtServiceToRevenueFiscal:
    """Compute the Chart Data fiscal debt service-to-revenue ratio output.

    Build the fiscal debt service-to-revenue ratio series from authored coordinate identities and scenario-specific input series.

    Args:
        inputs: Dataclass of input series, including old debt service, that determines the `TIME_PERIOD` keys and values for the fiscal debt service-to-revenue calculation.

    Returns:
        `data.ChartOutputDebtServiceToRevenueFiscal` series containing Debt Service-to-Revenue Ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputDebtServiceToRevenueFiscalInputs):
        raise TypeError(
            f"compute_chart_output_debt_service_to_revenue_fiscal() expected ChartOutputDebtServiceToRevenueFiscalInputs, got {type(inputs).__name__}"
        )
    return model.Model(inputs).chart_output_debt_service_to_revenue_fiscal


__all__ = [
    "Realism1ExternalDebtFlowComponentsInputs",
    "Realism1ExternalDebtCreatingFlowsInputs",
    "Realism1ExternalForecastErrorComponentLabelsInputs",
    "Realism1ExternalForecastErrorComponentsInputs",
    "Realism1ExternalForecastErrorDistributionLabelsInputs",
    "Realism1ExternalForecastErrorDistributionInputs",
    "Realism1ExternalVintageYearsInputs",
    "Realism1ExternalVintageDebtPathsInputs",
    "Realism1PublicDebtFlowComponentsInputs",
    "Realism1PublicDebtCreatingFlowsInputs",
    "Realism1PublicForecastErrorComponentLabelsInputs",
    "Realism1PublicForecastErrorComponentsInputs",
    "Realism1PublicForecastErrorLowerQuartileInputs",
    "Realism1PublicForecastErrorDistributionLabelsInputs",
    "Realism1PublicForecastErrorDistributionInputs",
    "Realism1PublicVintageYearsInputs",
    "Realism1PublicVintageDebtPathsInputs",
    "Realism2FiscalAdjustmentMultiplierLabelsInputs",
    "Realism2UnderlyingGrowthMultiplierLabelsInputs",
    "Realism2FiscalAdjustmentYearsInputs",
    "Realism2UnderlyingGrowthYearsInputs",
    "Realism2BaselineGrowthInputs",
    "Realism2GrowthTMinus1Inputs",
    "Realism2FiscalAdjustmentGrowthImpactInputs",
    "Realism2UnderlyingGrowthInputs",
    "Realism3InvestmentYearsInputs",
    "Realism3InvestmentPathLabelsInputs",
    "Realism3PublicPrivateInvestmentPathsInputs",
    "Realism3GrowthAccountingVintagesInputs",
    "Realism3GrowthAccountingContributionsInputs",
    "Realism4Projected3yrAdjustmentLabelInputs",
    "Realism4Projected3yrAdjustmentInputs",
    "Realism4Projected3yrAdjustmentBinInputs",
    "Realism4Projected3yrAdjustmentCategoryInputs",
    "Realism4Projected3yrAdjustmentSampleShareInputs",
    "Realism4FiscalAdjustmentTopBinLabelInputs",
    "Realism4FiscalAdjustmentSampleShareInputs",
    "Realism4FiscalAdjustmentCumulativeShareInputs",
    "ProbabilityPvDebtToGdpInputs",
    "ProbabilityPvDebtToExportsInputs",
    "ProbabilityDebtServiceToExportsInputs",
    "ProbabilityDebtServiceToRevenueInputs",
    "ProbabilityPvDebtToGdpDistressInputs",
    "ProbabilityPvDebtToExportsDistressInputs",
    "ProbabilityDebtServiceToExportsDistressInputs",
    "ProbabilityDebtServiceToRevenueDistressInputs",
    "ExternalDsaRiskRatingSignalInputs",
    "ExternalDsaRiskRatingNumericInputs",
    "ExternalBaselineBreachInputs",
    "ExternalShockBreachInputs",
    "ExternalPvDebtToGdpMxShockInputs",
    "ExternalPvDebtToExportsMxShockInputs",
    "ExternalDebtServiceToExportsMxShockInputs",
    "ExternalDebtServiceToRevenueMxShockInputs",
    "FiscalRiskRatingSignalInputs",
    "FiscalRiskRatingNumericInputs",
    "FiscalBaselineBreachInputs",
    "FiscalShockBreachInputs",
    "FiscalPvDebtToGdpMxShockInputs",
    "TailoredStressNaturalDisasterApplicableInputs",
    "TailoredStressCommodityPriceApplicableInputs",
    "TailoredStressMarketFinancingApplicableInputs",
    "FiscalSpaceModerateRiskSignalInputs",
    "OverallRiskRatingSignalInputs",
    "OverallRiskRatingNumericInputs",
    "ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs",
    "ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs",
    "ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs",
    "ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs",
    "ChartPvDebtGdpRatioCustomAlternativeScenarioInputs",
    "ChartOutputPvDebtGdpRatioInputs",
    "ChartPvDebtToExportsCustomAlternativeScenarioInputs",
    "ChartOutputPvDebtToExportsInputs",
    "ChartDebtServiceToExportsCustomAlternativeScenarioInputs",
    "ChartOutputDebtServiceToExportsInputs",
    "ChartDebtServiceToRevenueCustomAlternativeScenarioInputs",
    "ChartOutputDebtServiceToRevenueInputs",
    "ChartOutputPvDebtToGdpInputs",
    "ChartPvDebtToRevenueMxShockStandardTailoredInputs",
    "ChartOutputDebtServiceToRevenueFiscalInputs",
    "compute_realism1_external_debt_flow_components",
    "compute_realism1_external_debt_creating_flows",
    "compute_realism1_external_forecast_error_component_labels",
    "compute_realism1_external_forecast_error_components",
    "compute_realism1_external_forecast_error_distribution_labels",
    "compute_realism1_external_forecast_error_distribution",
    "compute_realism1_external_vintage_years",
    "compute_realism1_external_vintage_debt_paths",
    "compute_realism1_public_debt_flow_components",
    "compute_realism1_public_debt_creating_flows",
    "compute_realism1_public_forecast_error_component_labels",
    "compute_realism1_public_forecast_error_components",
    "compute_realism1_public_forecast_error_lower_quartile",
    "compute_realism1_public_forecast_error_distribution_labels",
    "compute_realism1_public_forecast_error_distribution",
    "compute_realism1_public_vintage_years",
    "compute_realism1_public_vintage_debt_paths",
    "compute_realism2_fiscal_adjustment_multiplier_labels",
    "compute_realism2_underlying_growth_multiplier_labels",
    "compute_realism2_fiscal_adjustment_years",
    "compute_realism2_underlying_growth_years",
    "compute_realism2_baseline_growth",
    "compute_realism2_growth_t_minus_1",
    "compute_realism2_fiscal_adjustment_growth_impact",
    "compute_realism2_underlying_growth",
    "compute_realism3_investment_years",
    "compute_realism3_investment_path_labels",
    "compute_realism3_public_private_investment_paths",
    "compute_realism3_growth_accounting_vintages",
    "compute_realism3_growth_accounting_contributions",
    "compute_realism4_projected_3yr_adjustment_label",
    "compute_realism4_projected_3yr_adjustment",
    "compute_realism4_projected_3yr_adjustment_bin",
    "compute_realism4_projected_3yr_adjustment_category",
    "compute_realism4_projected_3yr_adjustment_sample_share",
    "compute_realism4_fiscal_adjustment_top_bin_label",
    "compute_realism4_fiscal_adjustment_sample_share",
    "compute_realism4_fiscal_adjustment_cumulative_share",
    "compute_probability_pv_debt_to_gdp",
    "compute_probability_pv_debt_to_exports",
    "compute_probability_debt_service_to_exports",
    "compute_probability_debt_service_to_revenue",
    "compute_probability_pv_debt_to_gdp_distress",
    "compute_probability_pv_debt_to_exports_distress",
    "compute_probability_debt_service_to_exports_distress",
    "compute_probability_debt_service_to_revenue_distress",
    "compute_external_dsa_risk_rating_signal",
    "compute_external_dsa_risk_rating_numeric",
    "compute_external_baseline_breach",
    "compute_external_shock_breach",
    "compute_external_pv_debt_to_gdp_mx_shock",
    "compute_external_pv_debt_to_exports_mx_shock",
    "compute_external_debt_service_to_exports_mx_shock",
    "compute_external_debt_service_to_revenue_mx_shock",
    "compute_fiscal_risk_rating_signal",
    "compute_fiscal_risk_rating_numeric",
    "compute_fiscal_baseline_breach",
    "compute_fiscal_shock_breach",
    "compute_fiscal_pv_debt_to_gdp_mx_shock",
    "compute_tailored_stress_natural_disaster_applicable",
    "compute_tailored_stress_commodity_price_applicable",
    "compute_tailored_stress_market_financing_applicable",
    "compute_fiscal_space_moderate_risk_signal",
    "compute_overall_risk_rating_signal",
    "compute_overall_risk_rating_numeric",
    "compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp",
    "compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue",
    "compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue",
    "compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio",
    "compute_chart_pv_debt_gdp_ratio_custom_alternative_scenario",
    "compute_chart_output_pv_debt_gdp_ratio",
    "compute_chart_pv_debt_to_exports_custom_alternative_scenario",
    "compute_chart_output_pv_debt_to_exports",
    "compute_chart_debt_service_to_exports_custom_alternative_scenario",
    "compute_chart_output_debt_service_to_exports",
    "compute_chart_debt_service_to_revenue_custom_alternative_scenario",
    "compute_chart_output_debt_service_to_revenue",
    "compute_chart_output_pv_debt_to_gdp",
    "compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored",
    "compute_chart_output_debt_service_to_revenue_fiscal",
]
