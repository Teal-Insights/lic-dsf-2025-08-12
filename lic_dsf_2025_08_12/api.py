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
    """Compute the Realism 1 external debt-creating-flow decomposition components.

    Translate the external debt-flow decomposition into coordinate-aligned component labels for downstream realism analysis.

    Args:
        inputs: The typed Realism1ExternalDebtFlowComponentsInputs dataclass of coordinate-aligned data.* series providing the external debt-creating-flow values and labels required by the decomposition.

    Returns:
        A data.Realism1ExternalDebtFlowComponents typed result containing the translated component labels for the external debt-creating-flow decomposition over the catalog coordinate axes.
    """
    if not isinstance(inputs, Realism1ExternalDebtFlowComponentsInputs):
        raise TypeError(f"compute_realism1_external_debt_flow_components() expected Realism1ExternalDebtFlowComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_debt_flow_components


@publish(data.REALISM1_EXTERNAL_DEBT_CREATING_FLOWS.schema, constants=_CONSTANTS_1, cells=data.REALISM1_EXTERNAL_DEBT_CREATING_FLOWS.cells)
def compute_realism1_external_debt_creating_flows(inputs: Realism1ExternalDebtCreatingFlowsInputs) -> data.Realism1ExternalDebtCreatingFlows:
    """Compute the Realism 1 external PPG debt-creating-flow decomposition from its model inputs.

    Provide the Realism 1 chart series comparing five historical years with projected external debt-creating flows.

    Args:
        inputs: Realism1ExternalDebtCreatingFlowsInputs dataclass bundling the typed data.* series and scalar parameters needed for the external PPG debt-creating-flow calculation.

    Returns:
        data.Realism1ExternalDebtCreatingFlows typed data series containing the decomposed external PPG debt-creating flows across the 5-year historical and projection horizon.
    """
    if not isinstance(inputs, Realism1ExternalDebtCreatingFlowsInputs):
        raise TypeError(f"compute_realism1_external_debt_creating_flows() expected Realism1ExternalDebtCreatingFlowsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_debt_creating_flows


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENT_LABELS.schema, constants=_CONSTANTS_0, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENT_LABELS.cells)
def compute_realism1_external_forecast_error_component_labels(inputs: Realism1ExternalForecastErrorComponentLabelsInputs) -> data.Realism1ExternalForecastErrorComponentLabels:
    """Compute the Realism 1 external forecast-error component labels.

    Derive chart-legend component names for the external forecast-error pack from authored coordinate identities.

    Args:
        inputs: A Realism1ExternalForecastErrorComponentLabelsInputs dataclass providing the authored coordinate identities used to resolve the Realism 1 external forecast-error component labels.

    Returns:
        A data.Realism1ExternalForecastErrorComponentLabels series containing the chart-legend component names for the external forecast-error pack.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorComponentLabelsInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_component_labels() expected Realism1ExternalForecastErrorComponentLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_component_labels


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENTS.schema, constants=_CONSTANTS_2, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENTS.cells)
def compute_realism1_external_forecast_error_components(inputs: Realism1ExternalForecastErrorComponentsInputs) -> data.Realism1ExternalForecastErrorComponents:
    """Compute external forecast-error components for the Realism 1 chart.

    Derive stacked-bar forecast-error values by debt-creating-flow component from authored Realism 1 inputs.

    Args:
        inputs: A Realism1ExternalForecastErrorComponentsInputs instance containing the source data and assumptions required to compute the external forecast-error component series.

    Returns:
        A data.Realism1ExternalForecastErrorComponents instance containing external forecast-error stacked-bar values by debt-creating-flow component.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorComponentsInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_components() expected Realism1ExternalForecastErrorComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_components


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION_LABELS.schema, constants=_CONSTANTS_3, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION_LABELS.cells)
def compute_realism1_external_forecast_error_distribution_labels(inputs: Realism1ExternalForecastErrorDistributionLabelsInputs) -> data.Realism1ExternalForecastErrorDistributionLabels:
    """Compute Realism 1 external forecast-error distribution labels.

    Derive the label series for the external forecast-error median and PPG-debt-change overlay via authored coordinate identities.

    Args:
        inputs: Inputs dataclass of named-axis series supplying the Realism 1 external forecast-error distribution coordinates.

    Returns:
        Typed data.Realism1ExternalForecastErrorDistributionLabels series of labels for the external forecast-error median and PPG-debt-change overlay.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorDistributionLabelsInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_distribution_labels() expected Realism1ExternalForecastErrorDistributionLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_distribution_labels


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION.schema, constants=_CONSTANTS_2, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION.cells)
def compute_realism1_external_forecast_error_distribution(inputs: Realism1ExternalForecastErrorDistributionInputs) -> data.Realism1ExternalForecastErrorDistribution:
    """Compute the Realism 1 external forecast-error distribution.

    Derives the external forecast-error median series and its country PPG-debt-change overlay published by the Realism 1 tool.

    Args:
        inputs: Typed dataclass of keyword-only inputs supplying named-axis series over catalog coordinates (forecast-error decompositions and vintage paths) plus any scalar toggles.

    Returns:
        data.Realism1ExternalForecastErrorDistribution carrying the external forecast-error median and country PPG-debt-change overlay series.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorDistributionInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_distribution() expected Realism1ExternalForecastErrorDistributionInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_distribution


@publish(data.REALISM1_EXTERNAL_VINTAGE_YEARS.schema, constants=_CONSTANTS_4, cells=data.REALISM1_EXTERNAL_VINTAGE_YEARS.cells)
def compute_realism1_external_vintage_years(inputs: Realism1ExternalVintageYearsInputs) -> data.Realism1ExternalVintageYears:
    """Compute the Realism 1 external vintage debt-path year axis.

    Derive the year coordinates copied into the external vintage debt-path chart block.

    Args:
        inputs: Typed inputs for the Realism 1 external vintage years calculation, supplying the source series and scalar controls used to assemble the year axis.

    Returns:
        A `data.Realism1ExternalVintageYears` series containing the year axis copied into the external vintage debt-path chart block.
    """
    if not isinstance(inputs, Realism1ExternalVintageYearsInputs):
        raise TypeError(f"compute_realism1_external_vintage_years() expected Realism1ExternalVintageYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_vintage_years


@publish(data.REALISM1_EXTERNAL_VINTAGE_DEBT_PATHS.schema, constants=_CONSTANTS_2, cells=data.REALISM1_EXTERNAL_VINTAGE_DEBT_PATHS.cells)
def compute_realism1_external_vintage_debt_paths(inputs: Realism1ExternalVintageDebtPathsInputs) -> data.Realism1ExternalVintageDebtPaths:
    """Compute current, previous, and five-year-ago DSA paths of PPG external debt for the Realism 1 vintage.

    Extracts Realism 1 external vintage debt paths used to compare DSA debt trajectories across vintages.

    Args:
        inputs: Typed input bundle of catalog-coordinate data.* series and scalar settings required for the Realism 1 external vintage debt path calculation.

    Returns:
        A typed data.Realism1ExternalVintageDebtPaths bundle of catalog-coordinate series containing the current, previous, and five-year-ago DSA paths of PPG external debt.
    """
    if not isinstance(inputs, Realism1ExternalVintageDebtPathsInputs):
        raise TypeError(f"compute_realism1_external_vintage_debt_paths() expected Realism1ExternalVintageDebtPathsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_vintage_debt_paths


@publish(data.REALISM1_PUBLIC_DEBT_FLOW_COMPONENTS.schema, constants=_CONSTANTS_5, cells=data.REALISM1_PUBLIC_DEBT_FLOW_COMPONENTS.cells)
def compute_realism1_public_debt_flow_components(inputs: Realism1PublicDebtFlowComponentsInputs) -> data.Realism1PublicDebtFlowComponents:
    """Compute the Realism 1 public debt flow components decomposition.

    Translate workbook-labeled public debt-creating-flow component identities into coordinate series used by the Realism 1 forecast-error charts.

    Args:
        inputs: Keyword-only input bundle of typed data.* series and scalars supplying the coordinate-bound assumptions, workbook labels, and year grid required for the public debt flow component decomposition.

    Returns:
        data.Realism1PublicDebtFlowComponents series holding the translated component labels for the public debt-creating-flow decomposition.
    """
    if not isinstance(inputs, Realism1PublicDebtFlowComponentsInputs):
        raise TypeError(f"compute_realism1_public_debt_flow_components() expected Realism1PublicDebtFlowComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_debt_flow_components


@publish(data.REALISM1_PUBLIC_DEBT_CREATING_FLOWS.schema, constants=_CONSTANTS_6, cells=data.REALISM1_PUBLIC_DEBT_CREATING_FLOWS.cells)
def compute_realism1_public_debt_creating_flows(inputs: Realism1PublicDebtCreatingFlowsInputs) -> data.Realism1PublicDebtCreatingFlows:
    """Compute the Realism 1 public debt-creating-flow decomposition.

    Derive five-year historical versus projected public debt-creating flows from authored coordinate identities so the Realism 1 forecast-error analysis can be reproduced outside the workbook.

    Args:
        inputs: Keyword-only bundle of Realism 1 public debt-creating-flow inputs: the named-axis data.* series and scalar settings over catalog coordinates that define the debt-creating-flow decomposition, five-year historical window, and projection horizon.

    Returns:
        A data.Realism1PublicDebtCreatingFlows series holding the public debt-creating-flow decomposition across the five-year historical and projected periods.
    """
    if not isinstance(inputs, Realism1PublicDebtCreatingFlowsInputs):
        raise TypeError(f"compute_realism1_public_debt_creating_flows() expected Realism1PublicDebtCreatingFlowsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_debt_creating_flows


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENT_LABELS.schema, constants=_CONSTANTS_5, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENT_LABELS.cells)
def compute_realism1_public_forecast_error_component_labels(inputs: Realism1PublicForecastErrorComponentLabelsInputs) -> data.Realism1PublicForecastErrorComponentLabels:
    """Compute chart-legend component labels for the public forecast-error pack.

    Derives realism-1 public forecast-error component labels from authored coordinate identities.

    Args:
        inputs: Typed `Realism1PublicForecastErrorComponentLabelsInputs` dataclass supplying the component-label coordinates.

    Returns:
        A `data.Realism1PublicForecastErrorComponentLabels` series of chart-legend component names for the public forecast-error pack.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorComponentLabelsInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_component_labels() expected Realism1PublicForecastErrorComponentLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_component_labels


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENTS.schema, constants=_CONSTANTS_7, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENTS.cells)
def compute_realism1_public_forecast_error_components(inputs: Realism1PublicForecastErrorComponentsInputs) -> data.Realism1PublicForecastErrorComponents:
    """Compute public forecast-error components for the Realism 1 tool.

    Produces the debt-creating-flow decomposition of public forecast errors used by the Realism 1 stacked-bar output.

    Args:
        inputs: Typed input container of data.* series holding the public forecast-error source values by debt-creating-flow component.

    Returns:
        A data.Realism1PublicForecastErrorComponents series of public forecast-error stacked-bar values by debt-creating-flow component.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorComponentsInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_components() expected Realism1PublicForecastErrorComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_components


@publish(key=(), domain=None, constants=_CONSTANTS_8, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_LOWER_QUARTILE_CELLS)
def compute_realism1_public_forecast_error_lower_quartile(inputs: Realism1PublicForecastErrorLowerQuartileInputs) -> float | str:
    """Compute the Realism 1 public forecast-error lower-quartile marker.

    Resolves the public forecast-error lower-quartile marker from authored coordinate identities.

    Args:
        inputs: Typed input dataclass of coordinate series and scalars for the Realism 1 public forecast-error lower-quartile calculation.

    Returns:
        The Realism 1 public forecast-error lower-quartile marker, returned as a float or as a string when the source value is textual.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorLowerQuartileInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_lower_quartile() expected Realism1PublicForecastErrorLowerQuartileInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_lower_quartile


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION_LABELS.schema, constants=_CONSTANTS_9, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION_LABELS.cells)
def compute_realism1_public_forecast_error_distribution_labels(inputs: Realism1PublicForecastErrorDistributionLabelsInputs) -> data.Realism1PublicForecastErrorDistributionLabels:
    """Compute Realism 1 public forecast-error distribution labels.

    Return the label output for the public forecast-error median and change-in-debt overlay.

    Args:
        inputs: The typed Realism1PublicForecastErrorDistributionLabelsInputs bundle of catalog-coordinate series and scalar settings.

    Returns:
        The computed data.Realism1PublicForecastErrorDistributionLabels, containing labels for the public forecast-error median and change-in-debt overlay.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorDistributionLabelsInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_distribution_labels() expected Realism1PublicForecastErrorDistributionLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_distribution_labels


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION.schema, constants=_CONSTANTS_7, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION.cells)
def compute_realism1_public_forecast_error_distribution(inputs: Realism1PublicForecastErrorDistributionInputs) -> data.Realism1PublicForecastErrorDistribution:
    """Compute the Realism 1 public forecast-error distribution from authored coordinate identities.

    Produce the public forecast-error median and country change-in-debt overlay used by Realism 1 chart outputs.

    Args:
        inputs: Typed Realism1PublicForecastErrorDistributionInputs bundle carrying named-axis tensors over catalog coordinates, with scalar settings kept as scalars and no per-cell expansion.

    Returns:
        A data.Realism1PublicForecastErrorDistribution typed result containing the public forecast-error median and country change-in-debt overlay.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorDistributionInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_distribution() expected Realism1PublicForecastErrorDistributionInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_distribution


@publish(data.REALISM1_PUBLIC_VINTAGE_YEARS.schema, constants=_CONSTANTS_4, cells=data.REALISM1_PUBLIC_VINTAGE_YEARS.cells)
def compute_realism1_public_vintage_years(inputs: Realism1PublicVintageYearsInputs) -> data.Realism1PublicVintageYears:
    """Compute realism 1 public vintage years from authored coordinate identities.

    Extracts the year axis carried into the public vintage debt-path chart block for Realism 1 forecast-error paths.

    Args:
        inputs: Keyword-only typed inputs bundle supplying the authored series and scalars needed to resolve the Realism 1 public vintage year coordinates.

    Returns:
        A data.Realism1PublicVintageYears series holding the year axis copied into the public vintage debt-path chart block.
    """
    if not isinstance(inputs, Realism1PublicVintageYearsInputs):
        raise TypeError(f"compute_realism1_public_vintage_years() expected Realism1PublicVintageYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_vintage_years


@publish(data.REALISM1_PUBLIC_VINTAGE_DEBT_PATHS.schema, constants=_CONSTANTS_7, cells=data.REALISM1_PUBLIC_VINTAGE_DEBT_PATHS.cells)
def compute_realism1_public_vintage_debt_paths(inputs: Realism1PublicVintageDebtPathsInputs) -> data.Realism1PublicVintageDebtPaths:
    """Compute Realism 1 public vintage total public debt paths.

    Derive current, previous, and five-year-ago DSA paths of total public debt for the Realism 1 forecast-error vintage analysis.

    Args:
        inputs: Typed dataclass of named-axis data.* series and scalars supplying the Realism 1 public vintage debt paths computation inputs.

    Returns:
        A data.Realism1PublicVintageDebtPaths dataclass of named-axis tensors over catalog coordinates for the current, previous, and five-year-ago DSA total public debt paths.
    """
    if not isinstance(inputs, Realism1PublicVintageDebtPathsInputs):
        raise TypeError(f"compute_realism1_public_vintage_debt_paths() expected Realism1PublicVintageDebtPathsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_vintage_debt_paths


@publish(data.REALISM2_FISCAL_ADJUSTMENT_MULTIPLIER_LABELS.schema, constants=_CONSTANTS_10, cells=data.REALISM2_FISCAL_ADJUSTMENT_MULTIPLIER_LABELS.cells)
def compute_realism2_fiscal_adjustment_multiplier_labels(inputs: Realism2FiscalAdjustmentMultiplierLabelsInputs) -> data.Realism2FiscalAdjustmentMultiplierLabels:
    """Compute multiplier-column legends for the fiscal-adjustment-on-growth panel.

    Build the Realism 2 fiscal-adjustment multiplier label series from authored coordinate identities.

    Args:
        inputs: Typed input container carrying the coordinate identities and source series required to resolve the multiplier-column legends.

    Returns:
        A typed data series of multiplier-column legends for the fiscal-adjustment-on-growth panel.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentMultiplierLabelsInputs):
        raise TypeError(f"compute_realism2_fiscal_adjustment_multiplier_labels() expected Realism2FiscalAdjustmentMultiplierLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_fiscal_adjustment_multiplier_labels


@publish(data.REALISM2_UNDERLYING_GROWTH_MULTIPLIER_LABELS.schema, constants=_CONSTANTS_10, cells=data.REALISM2_UNDERLYING_GROWTH_MULTIPLIER_LABELS.cells)
def compute_realism2_underlying_growth_multiplier_labels(inputs: Realism2UnderlyingGrowthMultiplierLabelsInputs) -> data.Realism2UnderlyingGrowthMultiplierLabels:
    """Compute multiplier-column legends for the Realism 2 underlying-growth panel from authored coordinate identities.

    Derives display labels for the fiscal-multiplier columns used by the Realism 2 chart and its downstream Output 4-2 write-up.

    Args:
        inputs: Realism2UnderlyingGrowthMultiplierLabelsInputs dataclass of typed data series over catalog coordinates, carrying the Realism 2 - Fiscal multiplier sheet ranges (`A44:P52`) and coordinate identities needed to resolve multiplier-column legends.

    Returns:
        data.Realism2UnderlyingGrowthMultiplierLabels series of multiplier-column legends for the underlying-growth panel, indexed by the Realism 2 fiscal-multiplier chart coordinates.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthMultiplierLabelsInputs):
        raise TypeError(f"compute_realism2_underlying_growth_multiplier_labels() expected Realism2UnderlyingGrowthMultiplierLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_underlying_growth_multiplier_labels


@publish(data.REALISM2_FISCAL_ADJUSTMENT_YEARS.schema, constants=_CONSTANTS_4, cells=data.REALISM2_FISCAL_ADJUSTMENT_YEARS.cells)
def compute_realism2_fiscal_adjustment_years(inputs: Realism2FiscalAdjustmentYearsInputs) -> data.Realism2FiscalAdjustmentYears:
    """Computes the fiscal-adjustment-on-growth year series from the Realism 2 fiscal-multiplier panel.

    Produces the year axis used by the Realism 2 fiscal-adjustment-on-growth chart so downstream DSA realism outputs can be aligned to the workbook's projection grid.

    Args:
        inputs: A Realism2FiscalAdjustmentYearsInputs dataclass of typed data.* series and scalar parameters supplying the Realism 2 fiscal-multiplier panel and year-axis configuration used to derive the fiscal-adjustment years.

    Returns:
        A data.Realism2FiscalAdjustmentYears series giving the year axis for the fiscal-adjustment-on-growth panel.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentYearsInputs):
        raise TypeError(f"compute_realism2_fiscal_adjustment_years() expected Realism2FiscalAdjustmentYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_fiscal_adjustment_years


@publish(data.REALISM2_UNDERLYING_GROWTH_YEARS.schema, constants=_CONSTANTS_4, cells=data.REALISM2_UNDERLYING_GROWTH_YEARS.cells)
def compute_realism2_underlying_growth_years(inputs: Realism2UnderlyingGrowthYearsInputs) -> data.Realism2UnderlyingGrowthYears:
    """Compute the Realism 2 underlying-growth years panel from authored coordinate identities.

    Derive the year-indexed underlying-growth series used by the fiscal-multiplier realism chart.

    Args:
        inputs: Input dataclass carrying the Realism 2 underlying-growth source series and scalar controls; its keyword-only fields are typed data.* series or scalars.

    Returns:
        A data.Realism2UnderlyingGrowthYears typed series holding the underlying-growth panel, with the year axis copied from the source coordinate.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthYearsInputs):
        raise TypeError(f"compute_realism2_underlying_growth_years() expected Realism2UnderlyingGrowthYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_underlying_growth_years


@publish(data.REALISM2_BASELINE_GROWTH.schema, constants=_CONSTANTS_4, cells=data.REALISM2_BASELINE_GROWTH.cells)
def compute_realism2_baseline_growth(inputs: Realism2BaselineGrowthInputs) -> data.Realism2BaselineGrowth:
    """Compute the Realism 2 baseline real GDP growth path.

    Evaluates the fiscal-multiplier inputs to produce the baseline growth series used by the Realism 2 chart.

    Args:
        inputs: Typed input dataclass containing the coordinate-aligned series and scalar settings required for the Realism 2 baseline growth calculation.

    Returns:
        A `data.Realism2BaselineGrowth` series containing the baseline real GDP growth path shown on the fiscal-multiplier chart.
    """
    if not isinstance(inputs, Realism2BaselineGrowthInputs):
        raise TypeError(f"compute_realism2_baseline_growth() expected Realism2BaselineGrowthInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_baseline_growth


@publish(data.REALISM2_GROWTH_T_MINUS_1.schema, constants=_CONSTANTS_4, cells=data.REALISM2_GROWTH_T_MINUS_1.cells)
def compute_realism2_growth_t_minus_1(inputs: Realism2GrowthTMinus1Inputs) -> data.Realism2GrowthTMinus1:
    """Compute the Realism 2 pre-projection growth path at t−1 for the underlying-growth panel.

    Evaluate the authored coordinate identities that carry pre-projection growth into the underlying-growth panel.

    Args:
        inputs: Typed `Realism2GrowthTMinus1Inputs` dataclass bundling the coordinate-aligned input series and scalar assumptions required to compute the Realism 2 growth path.

    Returns:
        `data.Realism2GrowthTMinus1` series containing pre-projection growth carried into the underlying-growth panel.
    """
    if not isinstance(inputs, Realism2GrowthTMinus1Inputs):
        raise TypeError(f"compute_realism2_growth_t_minus_1() expected Realism2GrowthTMinus1Inputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_growth_t_minus_1


@publish(data.REALISM2_FISCAL_ADJUSTMENT_GROWTH_IMPACT.schema, constants=_CONSTANTS_10, cells=data.REALISM2_FISCAL_ADJUSTMENT_GROWTH_IMPACT.cells)
def compute_realism2_fiscal_adjustment_growth_impact(inputs: Realism2FiscalAdjustmentGrowthImpactInputs) -> data.Realism2FiscalAdjustmentGrowthImpact:
    """Compute the growth impact of the planned fiscal adjustment under alternative fiscal multipliers.

    Derive the Realism 2 fiscal-multiplier adjustment growth-impact series from authored coordinate identities.

    Args:
        inputs: Keyword-only input bundle of typed data.* series and scalars holding the planned fiscal adjustment path, alternative multiplier assumptions, and supporting baseline macro series over the catalog coordinates.

    Returns:
        A data.Realism2FiscalAdjustmentGrowthImpact dataclass of named-axis series giving the projected growth impact of the fiscal adjustment for each multiplier scenario over the projection years.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentGrowthImpactInputs):
        raise TypeError(f"compute_realism2_fiscal_adjustment_growth_impact() expected Realism2FiscalAdjustmentGrowthImpactInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_fiscal_adjustment_growth_impact


@publish(data.REALISM2_UNDERLYING_GROWTH.schema, constants=_CONSTANTS_10, cells=data.REALISM2_UNDERLYING_GROWTH.cells)
def compute_realism2_underlying_growth(inputs: Realism2UnderlyingGrowthInputs) -> data.Realism2UnderlyingGrowth:
    """Compute realism2 underlying growth paths under alternative fiscal-multiplier assumptions.

    Derives the realism2 underlying growth series from authored coordinate identities using the supplied inputs.

    Args:
        inputs: Keyword-only input dataclass of typed series and scalars carrying the fiscal-multiplier assumptions and coordinate inputs for the realism2 underlying growth computation.

    Returns:
        Typed series of underlying growth paths under alternative fiscal-multiplier assumptions, indexed over catalog coordinates.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthInputs):
        raise TypeError(f"compute_realism2_underlying_growth() expected Realism2UnderlyingGrowthInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_underlying_growth


@publish(data.REALISM3_INVESTMENT_YEARS.schema, constants=_CONSTANTS_4, cells=data.REALISM3_INVESTMENT_YEARS.cells)
def compute_realism3_investment_years(inputs: Realism3InvestmentYearsInputs) -> data.Realism3InvestmentYears:
    """Compute the Realism 3 investment vintage-year series.

    Produces the year axis used by the public/private investment vintage-comparison chart.

    Args:
        inputs: A keyword-only Realism3InvestmentYearsInputs bundle supplying the Realism 3 investment/growth chart configuration.

    Returns:
        A data.Realism3InvestmentYears typed series holding the vintage year axis for the public/private investment comparison chart.
    """
    if not isinstance(inputs, Realism3InvestmentYearsInputs):
        raise TypeError(f"compute_realism3_investment_years() expected Realism3InvestmentYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_investment_years


@publish(data.REALISM3_INVESTMENT_PATH_LABELS.schema, constants=_CONSTANTS_11, cells=data.REALISM3_INVESTMENT_PATH_LABELS.cells)
def compute_realism3_investment_path_labels(inputs: Realism3InvestmentPathLabelsInputs) -> data.Realism3InvestmentPathLabels:
    """Build the Realism 3 investment-path row labels.

    Provide the row legends distinguishing previous from current DSA public and private investment paths for the Realism 3 Invest-Growth chart.

    Args:
        inputs: Realism3InvestmentPathLabelsInputs dataclass of typed data.* series and scalars supplying the workbook coordinates and labels from which the investment-path legends are derived.

    Returns:
        A data.Realism3InvestmentPathLabels series of the Realism 3 investment-path row legends (previous vs current DSA public and private paths).
    """
    if not isinstance(inputs, Realism3InvestmentPathLabelsInputs):
        raise TypeError(f"compute_realism3_investment_path_labels() expected Realism3InvestmentPathLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_investment_path_labels


@publish(data.REALISM3_PUBLIC_PRIVATE_INVESTMENT_PATHS.schema, constants=_CONSTANTS_12, cells=data.REALISM3_PUBLIC_PRIVATE_INVESTMENT_PATHS.cells)
def compute_realism3_public_private_investment_paths(inputs: Realism3PublicPrivateInvestmentPathsInputs) -> data.Realism3PublicPrivateInvestmentPaths:
    """Compute public and private investment paths as a share of GDP for the current and previous DSA vintages.

    Produce Realism 3 investment-growth chart inputs for the LIC-DSF IDA21 template.

    Args:
        inputs: Typed Realism3PublicPrivateInvestmentPathsInputs bundle supplying the public and private investment assumptions and vintage coordinates used for the Realism 3 investment-growth calculation.

    Returns:
        A typed data.Realism3PublicPrivateInvestmentPaths series set containing public and private investment (% of GDP) paths for the current and previous DSA vintages.
    """
    if not isinstance(inputs, Realism3PublicPrivateInvestmentPathsInputs):
        raise TypeError(f"compute_realism3_public_private_investment_paths() expected Realism3PublicPrivateInvestmentPathsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_public_private_investment_paths


@publish(data.REALISM3_GROWTH_ACCOUNTING_VINTAGES.schema, constants=_CONSTANTS_13, cells=data.REALISM3_GROWTH_ACCOUNTING_VINTAGES.cells)
def compute_realism3_growth_accounting_vintages(inputs: Realism3GrowthAccountingVintagesInputs) -> data.Realism3GrowthAccountingVintages:
    """Compute Realism 3 investment-growth accounting vintage paths from authored coordinate identities.

    Derive the Realism 3 investment-growth accounting summary series used by the LIC-DSF Realism 3 Invest-Growth charts.

    Args:
        inputs: Dataclass of keyword-only `data.*` series over catalog coordinates and scalar controls supplying the inputs for the Realism 3 growth-accounting vintages.

    Returns:
        A `data.Realism3GrowthAccountingVintages` result containing the vintage-header series for the investment-growth accounting summary.
    """
    if not isinstance(inputs, Realism3GrowthAccountingVintagesInputs):
        raise TypeError(f"compute_realism3_growth_accounting_vintages() expected Realism3GrowthAccountingVintagesInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_growth_accounting_vintages


@publish(data.REALISM3_GROWTH_ACCOUNTING_CONTRIBUTIONS.schema, constants=_CONSTANTS_14, cells=data.REALISM3_GROWTH_ACCOUNTING_CONTRIBUTIONS.cells)
def compute_realism3_growth_accounting_contributions(inputs: Realism3GrowthAccountingContributionsInputs) -> data.Realism3GrowthAccountingContributions:
    """Compute Realism 3 growth-accounting contributions.

    Produce the five-year-average contribution of government capital and other factors to growth for the Realism 3 invest-growth tool.

    Args:
        inputs: Typed input bundle of named-axis data series and scalar settings for the Realism 3 growth-accounting calculation.

    Returns:
        A data.Realism3GrowthAccountingContributions dataclass of five-year-average contributions of government capital and other factors to growth.
    """
    if not isinstance(inputs, Realism3GrowthAccountingContributionsInputs):
        raise TypeError(f"compute_realism3_growth_accounting_contributions() expected Realism3GrowthAccountingContributionsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_growth_accounting_contributions


@publish(key=(), domain=None, constants=_CONSTANTS_15, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_LABEL_CELLS)
def compute_realism4_projected_3yr_adjustment_label(inputs: Realism4Projected3yrAdjustmentLabelInputs) -> str | int | float | bool:
    """Return the projected 3-year fiscal-adjustment label from Realism 4 inputs.

    Classifies the country's projected three-year fiscal-adjustment marker for the Realism 4 output.

    Args:
        inputs: Typed Realism4Projected3yrAdjustmentLabelInputs dataclass containing the Realism 4 fiscal-adjustment placement and distribution series used to derive the label.

    Returns:
        Scalar label for the country's projected 3-year fiscal-adjustment marker, as str, int, float, or bool.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentLabelInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_label() expected Realism4Projected3yrAdjustmentLabelInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_label


@publish(key=(), domain=None, constants=_CONSTANTS_4, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_CELLS)
def compute_realism4_projected_3yr_adjustment(inputs: Realism4Projected3yrAdjustmentInputs) -> float | str:
    """Compute the Realism 4 projected 3-year fiscal adjustment.

    Evaluates the Realism 4 fiscal-adjustment identity to place the projected 3-year adjustment used by the Realism 4 chart series.

    Args:
        inputs: Keyword-only Realism4Projected3yrAdjustmentInputs dataclass of typed data.* series and scalars supplying the Realism 4 fiscal-adjustment placement grid and distribution inputs.

    Returns:
        Projected 3-year fiscal adjustment as a float in percentage points of GDP, or a str when the adjustment is not defined for the supplied inputs.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment() expected Realism4Projected3yrAdjustmentInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment


@publish(key=(), domain=None, constants=_CONSTANTS_4, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_BIN_CELLS)
def compute_realism4_projected_3yr_adjustment_bin(inputs: Realism4Projected3yrAdjustmentBinInputs) -> float | str:
    """Compute the Realism 4 projected 3-year fiscal-adjustment histogram bin.

    Places the projected 3-year fiscal adjustment on the Realism 4 histogram bin edge for fiscal-adjustment distribution analysis.

    Args:
        inputs: Typed Realism 4 projected 3-year adjustment bin inputs carrying the coordinate series and scalar options used to evaluate the histogram bin.

    Returns:
        The projected 3-year adjustment rounded to the histogram bin edge, as a float, or a string when the resolved workbook value is textual.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentBinInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_bin() expected Realism4Projected3yrAdjustmentBinInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_bin


@publish(key=(), domain=None, constants=_CONSTANTS_16, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_CATEGORY_CELLS)
def compute_realism4_projected_3yr_adjustment_category(inputs: Realism4Projected3yrAdjustmentCategoryInputs) -> float | str:
    """Compute the Realism 4 projected 3-year fiscal-adjustment category.

    Places a country's projected 3-year fiscal adjustment on the Realism 4 histogram category axis.

    Args:
        inputs: Typed Realism4Projected3yrAdjustmentCategoryInputs dataclass bundling the named-axis series over catalog coordinates for the Realism 4 projected adjustment category computation, not a bare list of per-cell values.

    Returns:
        A float or str histogram category index (X) for the country's projected adjustment.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentCategoryInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_category() expected Realism4Projected3yrAdjustmentCategoryInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_category


@publish(key=(), domain=None, constants=_CONSTANTS_16, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_SAMPLE_SHARE_CELLS)
def compute_realism4_projected_3yr_adjustment_sample_share(inputs: Realism4Projected3yrAdjustmentSampleShareInputs) -> float | str:
    """Compute the Realism 4 projected 3-year fiscal-adjustment sample share from authored coordinate identities.

    Return the percent-of-sample position at the country's projected-adjustment bin for the Realism 4 fiscal-adjustment distribution.

    Args:
        inputs: A Realism4Projected3yrAdjustmentSampleShareInputs dataclass of named-axis tensors over catalog coordinates supplying the Realism 4 fiscal-adjustment placement and distribution data.

    Returns:
        A float giving the percent-of-sample at the country's projected-adjustment bin, or a string status where the workbook yields text or a blank.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentSampleShareInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_sample_share() expected Realism4Projected3yrAdjustmentSampleShareInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_sample_share


@publish(key=(), domain=None, constants=_CONSTANTS_17, cells=data.REALISM4_FISCAL_ADJUSTMENT_TOP_BIN_LABEL_CELLS)
def compute_realism4_fiscal_adjustment_top_bin_label(inputs: Realism4FiscalAdjustmentTopBinLabelInputs) -> str | int | float | bool:
    """Return the open-ended top-bin label for the Realism 4 fiscal-adjustment histogram.

    Resolve the top-bin label of the fiscal-adjustment distribution from authored coordinate identities for Realism 4 / Output 4-2 extraction.

    Args:
        inputs: Dataclass of named-axis series over catalog coordinates containing the fiscal-adjustment histogram inputs needed to resolve the open-ended top-bin label.

    Returns:
        The open-ended top-bin label, as a string, integer, float, or boolean matching the source cell's type.
    """
    if not isinstance(inputs, Realism4FiscalAdjustmentTopBinLabelInputs):
        raise TypeError(f"compute_realism4_fiscal_adjustment_top_bin_label() expected Realism4FiscalAdjustmentTopBinLabelInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_fiscal_adjustment_top_bin_label


@publish(data.REALISM4_FISCAL_ADJUSTMENT_SAMPLE_SHARE.schema, constants=_CONSTANTS_18, cells=data.REALISM4_FISCAL_ADJUSTMENT_SAMPLE_SHARE.cells)
def compute_realism4_fiscal_adjustment_sample_share(inputs: Realism4FiscalAdjustmentSampleShareInputs) -> data.Realism4FiscalAdjustmentSampleShare:
    """Compute the Realism 4 fiscal-adjustment sample share series.

    Derives the percent of the LIC sample falling in each 3-year fiscal-adjustment bin for the Realism 4 fiscal-adjustment distribution charts.

    Args:
        inputs: Keyword-only input series over catalog coordinates supplying the Realism 4 fiscal-adjustment placement and distribution data.

    Returns:
        A data.Realism4FiscalAdjustmentSampleShare series giving the percent of the LIC sample in each 3-year fiscal-adjustment bin.
    """
    if not isinstance(inputs, Realism4FiscalAdjustmentSampleShareInputs):
        raise TypeError(f"compute_realism4_fiscal_adjustment_sample_share() expected Realism4FiscalAdjustmentSampleShareInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_fiscal_adjustment_sample_share


@publish(data.REALISM4_FISCAL_ADJUSTMENT_CUMULATIVE_SHARE.schema, constants=_CONSTANTS_18, cells=data.REALISM4_FISCAL_ADJUSTMENT_CUMULATIVE_SHARE.cells)
def compute_realism4_fiscal_adjustment_cumulative_share(inputs: Realism4FiscalAdjustmentCumulativeShareInputs) -> data.Realism4FiscalAdjustmentCumulativeShare:
    """Compute the Realism 4 fiscal-adjustment cumulative sample share.

    Calculate the cumulative percent of the LIC sample up to each fiscal-adjustment bin for the LIC-DSF Realism 4 chart outputs.

    Args:
        inputs: A typed dataclass of named-axis series over catalog coordinates holding the Realism 4 fiscal-adjustment distribution inputs.

    Returns:
        A data.Realism4FiscalAdjustmentCumulativeShare named-axis series giving the cumulative percent of the LIC sample up to each fiscal-adjustment bin.
    """
    if not isinstance(inputs, Realism4FiscalAdjustmentCumulativeShareInputs):
        raise TypeError(f"compute_realism4_fiscal_adjustment_cumulative_share() expected Realism4FiscalAdjustmentCumulativeShareInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_fiscal_adjustment_cumulative_share


@publish(data.PROBABILITY_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_19, cells=data.PROBABILITY_PV_DEBT_TO_GDP.cells)
def compute_probability_pv_debt_to_gdp(inputs: ProbabilityPvDebtToGdpInputs) -> data.ProbabilityPvDebtToGdp:
    """Compute the probability-approach path for PV of PPG external debt to GDP.

    Derive the LIC-DSF probability indicator for the PV of PPG external debt-to-GDP ratio using authored coordinate identities.

    Args:
        inputs: Typed ProbabilityPvDebtToGdpInputs dataclass supplying data.* series and scalar parameters for the PV of PPG external debt-to-GDP baseline, historical, MX shock, threshold, and bands.

    Returns:
        A data.ProbabilityPvDebtToGdp series containing the computed probability path for the PV of PPG external debt-to-GDP ratio across the projection year grid.
    """
    if not isinstance(inputs, ProbabilityPvDebtToGdpInputs):
        raise TypeError(f"compute_probability_pv_debt_to_gdp() expected ProbabilityPvDebtToGdpInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_gdp


@publish(data.PROBABILITY_PV_DEBT_TO_EXPORTS.schema, constants=_CONSTANTS_20, cells=data.PROBABILITY_PV_DEBT_TO_EXPORTS.cells)
def compute_probability_pv_debt_to_exports(inputs: ProbabilityPvDebtToExportsInputs) -> data.ProbabilityPvDebtToExports:
    """Compute the probability-approach PV of PPG external debt-to-exports output series.

    Derive the PV debt-to-exports indicator paths used by the LIC-DSF probability approach from the supplied model inputs.

    Args:
        inputs: Typed input bundle providing the probability-approach PV debt-to-exports assumptions and coordinate data.

    Returns:
        A data.ProbabilityPvDebtToExports series with baseline, historical, MX shock, threshold, and band values over the catalog coordinates.
    """
    if not isinstance(inputs, ProbabilityPvDebtToExportsInputs):
        raise TypeError(f"compute_probability_pv_debt_to_exports() expected ProbabilityPvDebtToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_exports


@publish(data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS.schema, constants=_CONSTANTS_21, cells=data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS.cells)
def compute_probability_debt_service_to_exports(inputs: ProbabilityDebtServiceToExportsInputs) -> data.ProbabilityDebtServiceToExports:
    """Compute the probability-based PPG external debt service-to-exports result series.

    Derives probability-approach debt service-to-exports outputs from typed, coordinate-aware inputs.

    Args:
        inputs: Typed inputs dataclass containing named-axis series over catalog coordinates that supply the baseline, historical, MX shock, threshold, and band data for the probability calculation.

    Returns:
        Typed data.ProbabilityDebtServiceToExports result containing baseline, historical, MX shock, threshold, and band series over catalog coordinates for PPG external debt service to exports.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToExportsInputs):
        raise TypeError(f"compute_probability_debt_service_to_exports() expected ProbabilityDebtServiceToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_exports


@publish(data.PROBABILITY_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_22, cells=data.PROBABILITY_DEBT_SERVICE_TO_REVENUE.cells)
def compute_probability_debt_service_to_revenue(inputs: ProbabilityDebtServiceToRevenueInputs) -> data.ProbabilityDebtServiceToRevenue:
    """Compute the PPG external debt service-to-revenue probability series.

    Calculate the probability debt service-to-revenue output using the authored coordinate identities.

    Args:
        inputs: Typed input dataclass containing the named-axis series and scalar assumptions (including baseline, historical, MX shock, threshold, and band inputs) required for the probability debt service-to-revenue calculation.

    Returns:
        A data.ProbabilityDebtServiceToRevenue result containing the computed PPG external debt service-to-revenue baseline, historical, MX shock, threshold, and band series.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToRevenueInputs):
        raise TypeError(f"compute_probability_debt_service_to_revenue() expected ProbabilityDebtServiceToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_revenue


@publish(data.PROBABILITY_PV_DEBT_TO_GDP_DISTRESS.schema, constants=_CONSTANTS_23, cells=data.PROBABILITY_PV_DEBT_TO_GDP_DISTRESS.cells)
def compute_probability_pv_debt_to_gdp_distress(inputs: ProbabilityPvDebtToGdpDistressInputs) -> data.ProbabilityPvDebtToGdpDistress:
    """Compute probability of external-debt distress for the PV debt-to-GDP indicator.

    Derive baseline, historical, MX, and threshold distress probabilities from the PV debt-to-GDP probability inputs.

    Args:
        inputs: ProbabilityPvDebtToGdpDistressInputs dataclass of named-axis series over catalog coordinates supplying the PV debt-to-GDP probability inputs.

    Returns:
        data.ProbabilityPvDebtToGdpDistress series of external-debt distress probabilities for PV debt-to-GDP under baseline, historical, MX, and threshold.
    """
    if not isinstance(inputs, ProbabilityPvDebtToGdpDistressInputs):
        raise TypeError(f"compute_probability_pv_debt_to_gdp_distress() expected ProbabilityPvDebtToGdpDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_gdp_distress


@publish(data.PROBABILITY_PV_DEBT_TO_EXPORTS_DISTRESS.schema, constants=_CONSTANTS_24, cells=data.PROBABILITY_PV_DEBT_TO_EXPORTS_DISTRESS.cells)
def compute_probability_pv_debt_to_exports_distress(inputs: ProbabilityPvDebtToExportsDistressInputs) -> data.ProbabilityPvDebtToExportsDistress:
    """Compute the probability of external-debt distress for the PV of debt-to-exports ratio.

    Derive the distress probability series for the PV debt-to-exports indicator under baseline, historical, MX, and threshold scenarios.

    Args:
        inputs: Typed input series for the PV debt-to-exports probability calculation, spanning the catalog coordinates required by the baseline, historical, MX, and threshold variants.

    Returns:
        A data.ProbabilityPvDebtToExportsDistress series of distress probabilities for the PV debt-to-exports indicator across baseline, historical, MX, and threshold variants.
    """
    if not isinstance(inputs, ProbabilityPvDebtToExportsDistressInputs):
        raise TypeError(f"compute_probability_pv_debt_to_exports_distress() expected ProbabilityPvDebtToExportsDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_exports_distress


@publish(data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS_DISTRESS.schema, constants=_CONSTANTS_25, cells=data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS_DISTRESS.cells)
def compute_probability_debt_service_to_exports_distress(inputs: ProbabilityDebtServiceToExportsDistressInputs) -> data.ProbabilityDebtServiceToExportsDistress:
    """Compute the probability of external-debt distress for the debt service-to-exports ratio.

    Evaluate the probability-approach indicator for debt service to exports under baseline, historical, MX, and threshold scenarios.

    Args:
        inputs: Dataclass of named-axis series over catalog coordinates supplying the baseline, historical, MX, and threshold debt service-to-exports paths.

    Returns:
        Probability of external-debt distress for debt service/exports under baseline, historical, MX, and threshold, as a typed data series over catalog coordinates.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToExportsDistressInputs):
        raise TypeError(f"compute_probability_debt_service_to_exports_distress() expected ProbabilityDebtServiceToExportsDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_exports_distress


@publish(data.PROBABILITY_DEBT_SERVICE_TO_REVENUE_DISTRESS.schema, constants=_CONSTANTS_26, cells=data.PROBABILITY_DEBT_SERVICE_TO_REVENUE_DISTRESS.cells)
def compute_probability_debt_service_to_revenue_distress(inputs: ProbabilityDebtServiceToRevenueDistressInputs) -> data.ProbabilityDebtServiceToRevenueDistress:
    """Compute the probability of external-debt distress for the debt service-to-revenue ratio.

    Produces baseline, historical, MX, and threshold probability paths for the LIC-DSF probability approach.

    Args:
        inputs: Input bundle of named-axis series and scalar assumptions required for the debt service-to-revenue probability-distress calculation.

    Returns:
        A typed `data.ProbabilityDebtServiceToRevenueDistress` result containing the probability of external-debt distress for the debt service-to-revenue ratio under baseline, historical, MX, and threshold scenarios.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToRevenueDistressInputs):
        raise TypeError(f"compute_probability_debt_service_to_revenue_distress() expected ProbabilityDebtServiceToRevenueDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_revenue_distress


@publish(key=(), domain=None, constants=_CONSTANTS_27, cells=data.EXTERNAL_DSA_RISK_RATING_SIGNAL_CELLS)
def compute_external_dsa_risk_rating_signal(inputs: ExternalDsaRiskRatingSignalInputs) -> str | int | float | bool:
    """Computes the external DSA risk-rating signal from authored workbook coordinates.

    Derives the Chart Data external risk-rating signal for LIC-DSF external debt sustainability analysis.

    Args:
        inputs: Typed ExternalDsaRiskRatingSignalInputs dataclass supplying the named-axis coordinate series and scalar settings required to evaluate the external DSA risk-rating signal.

    Returns:
        Scalar external DSA risk-rating signal value typed as str | int | float | bool, corresponding to the Chart Data external risk-rating text/numeric signal (Chart Data!D10).
    """
    if not isinstance(inputs, ExternalDsaRiskRatingSignalInputs):
        raise TypeError(f"compute_external_dsa_risk_rating_signal() expected ExternalDsaRiskRatingSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_dsa_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_28, cells=data.EXTERNAL_DSA_RISK_RATING_NUMERIC_CELLS)
def compute_external_dsa_risk_rating_numeric(inputs: ExternalDsaRiskRatingNumericInputs) -> float | str:
    """Compute the external DSA risk-rating numeric code from authored coordinate identities.

    Produces the Chart Data external risk-rating signal as a numeric code or text label.

    Args:
        inputs: Keyword-only input dataclass carrying the external DSA risk-rating numeric coordinate signals and any associated typed data series.

    Returns:
        External DSA risk-rating numeric code as a float when numeric, otherwise the text signal string.
    """
    if not isinstance(inputs, ExternalDsaRiskRatingNumericInputs):
        raise TypeError(f"compute_external_dsa_risk_rating_numeric() expected ExternalDsaRiskRatingNumericInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_dsa_risk_rating_numeric


@publish(key=(), domain=None, constants=_CONSTANTS_28, cells=data.EXTERNAL_BASELINE_BREACH_CELLS)
def compute_external_baseline_breach(inputs: ExternalBaselineBreachInputs) -> float | str:
    """Compute the external baseline breach flag from typed external-baseline inputs.

    Evaluate whether the external baseline breaches the applicable threshold, excluding one-year breaches, and return the 0/1 signal used in the LIC-DSF risk-rating block.

    Args:
        inputs: Keyword-only input bundle of typed data.* series and scalar settings over the external-baseline catalog coordinates.

    Returns:
        External baseline breach flag as a float or str: 0/0.0 for no breach, 1/1.0 for breach, excluding one-year breaches, corresponding to Chart Data!D12.
    """
    if not isinstance(inputs, ExternalBaselineBreachInputs):
        raise TypeError(f"compute_external_baseline_breach() expected ExternalBaselineBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_baseline_breach


@publish(key=(), domain=None, constants=_CONSTANTS_28, cells=data.EXTERNAL_SHOCK_BREACH_CELLS)
def compute_external_shock_breach(inputs: ExternalShockBreachInputs) -> float | str:
    """Compute the external shock breach flag from LIC-DSF external shock inputs.

    Evaluate the Chart Data!D13 external shock breach status, excluding one-year breaches.

    Args:
        inputs: ExternalShockBreachInputs dataclass of named-axis data series over catalog coordinates, supplying the external shock, baseline, and stress-test quantities required for the breach rule.

    Returns:
        External shock breach indicator as a scalar: 0/no-breach or 1/breach, excluding one-year breaches, returned as float or str.
    """
    if not isinstance(inputs, ExternalShockBreachInputs):
        raise TypeError(f"compute_external_shock_breach() expected ExternalShockBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_shock_breach


@publish(key=(), domain=None, constants=_CONSTANTS_29, cells=data.EXTERNAL_PV_DEBT_TO_GDP_MX_SHOCK_CELLS)
def compute_external_pv_debt_to_gdp_mx_shock(inputs: ExternalPvDebtToGdpMxShockInputs) -> str | int | float | bool:
    """Return the external PV debt-to-GDP MX shock label from Chart Data!D14.

    Provide the published scalar signal for the PV of debt-to-GDP ratio MX shock used in external DSA risk-rating output.

    Args:
        inputs: Keyword-only typed input bundle containing the named-axis data-series and scalar coordinates required for the external PV debt-to-GDP MX shock calculation; do not expand into per-cell arguments.

    Returns:
        Scalar value at Chart Data!D14 for the external PV debt-to-GDP MX shock label/signal, typed as str, int, float, or bool.
    """
    if not isinstance(inputs, ExternalPvDebtToGdpMxShockInputs):
        raise TypeError(f"compute_external_pv_debt_to_gdp_mx_shock() expected ExternalPvDebtToGdpMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_pv_debt_to_gdp_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_30, cells=data.EXTERNAL_PV_DEBT_TO_EXPORTS_MX_SHOCK_CELLS)
def compute_external_pv_debt_to_exports_mx_shock(inputs: ExternalPvDebtToExportsMxShockInputs) -> str | int | float | bool:
    """Compute the external PV debt-to-exports MX shock label.

    Return the Chart Data!D15 MX shock label for the PV of debt-to-exports ratio.

    Args:
        inputs: Typed input bundle carrying the coordinate-aligned series and scalar assumptions used by the external PV debt-to-exports MX shock calculation.

    Returns:
        The external PV debt-to-exports MX shock label (Chart Data!D15) as a scalar str, int, float, or bool.
    """
    if not isinstance(inputs, ExternalPvDebtToExportsMxShockInputs):
        raise TypeError(f"compute_external_pv_debt_to_exports_mx_shock() expected ExternalPvDebtToExportsMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_pv_debt_to_exports_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_31, cells=data.EXTERNAL_DEBT_SERVICE_TO_EXPORTS_MX_SHOCK_CELLS)
def compute_external_debt_service_to_exports_mx_shock(inputs: ExternalDebtServiceToExportsMxShockInputs) -> str | int | float | bool:
    """Compute the external debt service-to-exports MX shock label.

    Return the Chart Data MX-shock label used in the LIC-DSF external risk-rating signals.

    Args:
        inputs: Inputs dataclass for the external debt service-to-exports MX shock computation.

    Returns:
        Scalar external debt service-to-exports MX shock label or flag from Chart Data!D16, typed as str, int, float, or bool.
    """
    if not isinstance(inputs, ExternalDebtServiceToExportsMxShockInputs):
        raise TypeError(f"compute_external_debt_service_to_exports_mx_shock() expected ExternalDebtServiceToExportsMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_debt_service_to_exports_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_32, cells=data.EXTERNAL_DEBT_SERVICE_TO_REVENUE_MX_SHOCK_CELLS)
def compute_external_debt_service_to_revenue_mx_shock(inputs: ExternalDebtServiceToRevenueMxShockInputs) -> str | int | float | bool:
    """Compute the external debt service-to-revenue MX shock label from Chart Data!D17 inputs.

    Extract the Debt service to revenue MX shock (market-financing) risk-rating signal used in the LIC-DSF external DSA write-up.

    Args:
        inputs: Keyword-only ExternalDebtServiceToRevenueMxShockInputs series bundle supplying the authored coordinate identities for the Chart Data!D17 MX shock label.

    Returns:
        The external debt service-to-revenue MX shock label scalar (str, int, float, or bool) as read from the model.
    """
    if not isinstance(inputs, ExternalDebtServiceToRevenueMxShockInputs):
        raise TypeError(f"compute_external_debt_service_to_revenue_mx_shock() expected ExternalDebtServiceToRevenueMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_debt_service_to_revenue_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_33, cells=data.FISCAL_RISK_RATING_SIGNAL_CELLS)
def compute_fiscal_risk_rating_signal(inputs: FiscalRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute the fiscal risk-rating signal from the fiscal risk-rating inputs.

    Return the Chart Data fiscal risk-rating signal used by the LIC-DSF DSA.

    Args:
        inputs: Fiscal risk-rating calculation inputs as a FiscalRiskRatingSignalInputs dataclass of data.* series and scalar configuration values.

    Returns:
        The fiscal risk-rating text signal for Chart Data!I10 (external risk-rating signal) as a scalar str, int, float, or bool.
    """
    if not isinstance(inputs, FiscalRiskRatingSignalInputs):
        raise TypeError(f"compute_fiscal_risk_rating_signal() expected FiscalRiskRatingSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_34, cells=data.FISCAL_RISK_RATING_NUMERIC_CELLS)
def compute_fiscal_risk_rating_numeric(inputs: FiscalRiskRatingNumericInputs) -> float | str:
    """Compute the fiscal risk-rating numeric code from the authored Chart Data fiscal-risk identities.

    Resolve the fiscal (total public debt) risk-rating signal for the DSA output surface.

    Args:
        inputs: Keyword-only fiscal risk-rating numeric input bundle, providing the typed data.* coordinate series and scalar signals that identify the Chart Data fiscal rating cells and breach flags.

    Returns:
        A float numeric risk-rating code when the identity resolves numerically, or the authored text signal string from Chart Data!I11; otherwise the model's stored value for the fiscal risk-rating numeric field.
    """
    if not isinstance(inputs, FiscalRiskRatingNumericInputs):
        raise TypeError(f"compute_fiscal_risk_rating_numeric() expected FiscalRiskRatingNumericInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_risk_rating_numeric


@publish(key=(), domain=None, constants=_CONSTANTS_34, cells=data.FISCAL_BASELINE_BREACH_CELLS)
def compute_fiscal_baseline_breach(inputs: FiscalBaselineBreachInputs) -> float | str:
    """Compute the fiscal baseline breach flag from the fiscal risk-rating signals.

    Indicate whether the baseline public debt path breaches the applicable fiscal threshold, excluding one-year breaches.

    Args:
        inputs: Fiscal risk-rating inputs and configuration needed to evaluate the fiscal baseline breach condition.

    Returns:
        Fiscal baseline breach flag as a float (0.0 for no breach, 1.0 for breach, excluding one-year breaches) or its string representation.
    """
    if not isinstance(inputs, FiscalBaselineBreachInputs):
        raise TypeError(f"compute_fiscal_baseline_breach() expected FiscalBaselineBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_baseline_breach


@publish(key=(), domain=None, constants=_CONSTANTS_34, cells=data.FISCAL_SHOCK_BREACH_CELLS)
def compute_fiscal_shock_breach(inputs: FiscalShockBreachInputs) -> float | str:
    """Compute the fiscal shock breach flag for the LIC-DSF IDA21 template.

    Returns the Chart Data fiscal shock breach indicator used in the fiscal risk-rating signal.

    Args:
        inputs: FiscalShockBreachInputs dataclass containing the scalar and data.* series inputs needed to evaluate the fiscal shock breach calculation.

    Returns:
        Fiscal shock breach flag as a float (0 = no breach, 1 = breach, excluding 1-year breaches), or a str when the source cell evaluates to a non-numeric marker.
    """
    if not isinstance(inputs, FiscalShockBreachInputs):
        raise TypeError(f"compute_fiscal_shock_breach() expected FiscalShockBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_shock_breach


@publish(key=(), domain=None, constants=_CONSTANTS_35, cells=data.FISCAL_PV_DEBT_TO_GDP_MX_SHOCK_CELLS)
def compute_fiscal_pv_debt_to_gdp_mx_shock(inputs: FiscalPvDebtToGdpMxShockInputs) -> str | int | float | bool:
    """Compute the fiscal PV debt-to-GDP MX shock label from authored coordinate identities.

    Extracts the Chart Data fiscal PV debt-to-GDP MX shock label used in LIC-DSF public-debt reporting.

    Args:
        inputs: FiscalPvDebtToGdpMxShockInputs dataclass containing the typed data.* series and scalar values for the fiscal PV debt-to-GDP MX shock calculation.

    Returns:
        The fiscal PV debt-to-GDP MX shock label (Chart Data!I14) as a scalar str, int, float, or bool.
    """
    if not isinstance(inputs, FiscalPvDebtToGdpMxShockInputs):
        raise TypeError(f"compute_fiscal_pv_debt_to_gdp_mx_shock() expected FiscalPvDebtToGdpMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_pv_debt_to_gdp_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_36, cells=data.TAILORED_STRESS_NATURAL_DISASTER_APPLICABLE_CELLS)
def compute_tailored_stress_natural_disaster_applicable(inputs: TailoredStressNaturalDisasterApplicableInputs) -> float | str:
    """Compute the natural-disaster tailored-stress applicability flag.

    Evaluate whether the natural-disaster tailored stress test applies for the current LIC-DSF scenario.

    Args:
        inputs: Typed inputs bundle for the natural-disaster tailored-stress applicability signal (Chart Data!I17; debt service-to-revenue MX shock — market-financing).

    Returns:
        The applicability signal as a 0/1 float, or a string label when the workbook cell resolves to text.
    """
    if not isinstance(inputs, TailoredStressNaturalDisasterApplicableInputs):
        raise TypeError(f"compute_tailored_stress_natural_disaster_applicable() expected TailoredStressNaturalDisasterApplicableInputs, got {type(inputs).__name__}")
    return model.Model(inputs).tailored_stress_natural_disaster_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_37, cells=data.TAILORED_STRESS_COMMODITY_PRICE_APPLICABLE_CELLS)
def compute_tailored_stress_commodity_price_applicable(inputs: TailoredStressCommodityPriceApplicableInputs) -> float | str:
    """Computes the commodity-price tailored stress applicability flag for the LIC-DSF template.

    Evaluates authored coordinate identities to determine whether the commodity-price tailored stress test applies, excluding 1-year breaches.

    Args:
        inputs: Typed input dataclass carrying the authored coordinate identities required to compute the commodity-price tailored stress applicability flag.

    Returns:
        Scalar float or string encoding the commodity-price tailored stress applicable flag (0/1; Chart Data!I18), with 1-year breaches excluded.
    """
    if not isinstance(inputs, TailoredStressCommodityPriceApplicableInputs):
        raise TypeError(f"compute_tailored_stress_commodity_price_applicable() expected TailoredStressCommodityPriceApplicableInputs, got {type(inputs).__name__}")
    return model.Model(inputs).tailored_stress_commodity_price_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_38, cells=data.TAILORED_STRESS_MARKET_FINANCING_APPLICABLE_CELLS)
def compute_tailored_stress_market_financing_applicable(inputs: TailoredStressMarketFinancingApplicableInputs) -> float | str:
    """Determine whether the market-financing tailored stress test applies.

    Resolve the market-financing tailored-stress applicability flag from authored Chart Data coordinates.

    Args:
        inputs: Typed input bundle carrying the market-financing tailored-stress applicability coordinates.

    Returns:
        Scalar 0/1 applicability indicator for the market-financing tailored stress test (or its string label), from Chart Data!I19 under Market financing.
    """
    if not isinstance(inputs, TailoredStressMarketFinancingApplicableInputs):
        raise TypeError(f"compute_tailored_stress_market_financing_applicable() expected TailoredStressMarketFinancingApplicableInputs, got {type(inputs).__name__}")
    return model.Model(inputs).tailored_stress_market_financing_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_39, cells=data.FISCAL_SPACE_MODERATE_RISK_SIGNAL_CELLS)
def compute_fiscal_space_moderate_risk_signal(inputs: FiscalSpaceModerateRiskSignalInputs) -> str | int | float | bool:
    """Compute the moderate-risk fiscal-space signal from the supplied fiscal-space inputs.

    Returns the Chart Data fiscal-space signal used to classify total public debt risk as moderate.

    Args:
        inputs: Fiscal-space input series and scalars, provided as a typed FiscalSpaceModerateRiskSignalInputs bundle of data.* series over catalog coordinates.

    Returns:
        Scalar moderate-risk fiscal-space signal (text or numeric rating) from Chart Data D23; Moderate risk category.
    """
    if not isinstance(inputs, FiscalSpaceModerateRiskSignalInputs):
        raise TypeError(f"compute_fiscal_space_moderate_risk_signal() expected FiscalSpaceModerateRiskSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_space_moderate_risk_signal


@publish(key=(), domain=None, constants=_CONSTANTS_40, cells=data.OVERALL_RISK_RATING_SIGNAL_CELLS)
def compute_overall_risk_rating_signal(inputs: OverallRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute the combined external and fiscal overall risk-rating signal.

    Derive the Chart Data overall rating signal used in the LIC-DSF write-up.

    Args:
        inputs: Typed calculation inputs carrying the catalog-coordinate series and scalar parameters required for the overall risk-rating signal model.

    Returns:
        Overall combined risk-rating signal as a scalar string, integer, float, or boolean, corresponding to the Chart Data overall rating signal.
    """
    if not isinstance(inputs, OverallRiskRatingSignalInputs):
        raise TypeError(f"compute_overall_risk_rating_signal() expected OverallRiskRatingSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).overall_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_41, cells=data.OVERALL_RISK_RATING_NUMERIC_CELLS)
def compute_overall_risk_rating_numeric(inputs: OverallRiskRatingNumericInputs) -> float | str:
    """Compute the overall combined LIC-DSF risk-rating numeric code from authored coordinate identities.

    Resolve the Chart Data!L11 overall risk-rating signal used in the DSA write-up.

    Args:
        inputs: Input dataclass of named-axis `data.*` series and scalar catalog coordinates that define the overall external-plus-fiscal risk-rating model; series remain typed coordinate tensors, not bare Python lists or per-cell arguments.

    Returns:
        Overall combined risk-rating numeric code as a `float`, or a `str` when the workbook outcome is textual.
    """
    if not isinstance(inputs, OverallRiskRatingNumericInputs):
        raise TypeError(f"compute_overall_risk_rating_numeric() expected OverallRiskRatingNumericInputs, got {type(inputs).__name__}")
    return model.Model(inputs).overall_risk_rating_numeric


@publish(data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_GDP_RATIO_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_35, cells=data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_GDP_RATIO_PV_DEBT_TO_GDP.cells)
def compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp(inputs: ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs) -> data.ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdp:
    """Compute the PV of Debt-to-GDP Ratio chart-data output for public debt stress blocks.

    Returns the scenario-keyed PV of Debt-to-GDP Ratio series from the LIC-DSF Chart Data public-debt stress ladder.

    Args:
        inputs: ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs instance carrying the scenario coordinates and calculation inputs required for the PV of Debt-to-GDP Ratio chart-data output.

    Returns:
        A data.ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdp series of PV of Debt-to-GDP Ratio values keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs):
        raise TypeError(f"compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp() expected ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp


@publish(data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_REVENUE_RATIO_PV_DEBT_TO_REVENUE.schema, constants=_CONSTANTS_42, cells=data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_REVENUE_RATIO_PV_DEBT_TO_REVENUE.cells)
def compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue(inputs: ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs) -> data.ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenue:
    """Compute the Chart Data PV of Debt-to-Revenue Ratio series, keyed by scenario.

    Produces the PV of Debt-to-Revenue Ratio output used by the LIC-DSF IDA21 Chart Data surface.

    Args:
        inputs: Keyword-only `ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs` bundle containing the scenario-keyed data-series and scalar inputs required to compute the Chart Data PV of Debt-to-Revenue Ratio output.

    Returns:
        A `data.ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenue` typed result containing the PV of Debt-to-Revenue Ratio Chart Data output, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs):
        raise TypeError(f"compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue() expected ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue


@publish(data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_REVENUE_RATIO_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_43, cells=data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_REVENUE_RATIO_DEBT_SERVICE_TO_REVENUE.cells)
def compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue(inputs: ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs) -> data.ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenue:
    """Compute the Chart Data Debt Service-to-Revenue Ratio series via authored coordinate identities.

    Derives the scenario-keyed Debt Service-to-Revenue Ratio published on Chart Data for the public-debt stress ladder.

    Args:
        inputs: Inputs dataclass supplying the named-axis coordinate series over catalog coordinates needed to evaluate the Debt Service-to-Revenue Ratio across the Chart Data scenario ladder.

    Returns:
        A data.ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenue series holding the Debt Service-to-Revenue Ratio keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs):
        raise TypeError(f"compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue() expected ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue


@publish(data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_GDP_RATIO_DEBT_SERVICE_GDP_RATIO.schema, constants=_CONSTANTS_43, cells=data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_GDP_RATIO_DEBT_SERVICE_GDP_RATIO.cells)
def compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio(inputs: ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs) -> data.ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatio:
    """Compute the Chart Data Debt Service-to-GDP Ratio series by scenario.

    Evaluate the authored coordinate identities that define the Debt Service-to-GDP Ratio on Chart Data.

    Args:
        inputs: Typed, scenario-keyed input definition containing the coordinate series and scalars required to evaluate the Debt Service-to-GDP Ratio identity.

    Returns:
        A `data.ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatio` series holding the Debt Service-to-GDP Ratio from Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs):
        raise TypeError(f"compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio() expected ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio


@publish(data.CHART_PV_DEBT_GDP_RATIO_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_44, cells=data.CHART_PV_DEBT_GDP_RATIO_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_pv_debt_gdp_ratio_custom_alternative_scenario(inputs: ChartPvDebtGdpRatioCustomAlternativeScenarioInputs) -> data.ChartPvDebtGdpRatioCustomAlternativeScenario:
    """Compute the PV of debt-to-GDP ratio for the customized A2 alternative scenario.

    Generates the Chart Data A2 customized alternative-scenario series used in the LIC-DSF public-debt stress charts.

    Args:
        inputs: Inputs dataclass supplying the customized alternative-scenario assumptions and the Chart Data projection-year grid required to compute the PV of debt-to-GDP ratio path.

    Returns:
        A data.ChartPvDebtGdpRatioCustomAlternativeScenario series containing the PV of debt-to-GDP ratio under the A2 customized alternative scenario, indexed over the projection years from Chart Data row 35.
    """
    if not isinstance(inputs, ChartPvDebtGdpRatioCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_pv_debt_gdp_ratio_custom_alternative_scenario() expected ChartPvDebtGdpRatioCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_pv_debt_gdp_ratio_custom_alternative_scenario


@publish(data.CHART_OUTPUT_PV_DEBT_GDP_RATIO.schema, constants=_CONSTANTS_45, cells=data.CHART_OUTPUT_PV_DEBT_GDP_RATIO.cells)
def compute_chart_output_pv_debt_gdp_ratio(inputs: ChartOutputPvDebtGdpRatioInputs) -> data.ChartOutputPvDebtGdpRatio:
    """Compute the PV of debt-to-GDP ratio chart output series.

    Derive the scenario-keyed PV of debt-to-GDP ratio Chart Data series from the authored input bundle.

    Args:
        inputs: Typed input bundle supplying the scenario and parameter values required to compute the Chart Data PV of debt-to-GDP ratio series.

    Returns:
        A data.ChartOutputPvDebtGdpRatio series containing the PV of debt-to-GDP ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputPvDebtGdpRatioInputs):
        raise TypeError(f"compute_chart_output_pv_debt_gdp_ratio() expected ChartOutputPvDebtGdpRatioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_pv_debt_gdp_ratio


@publish(data.CHART_PV_DEBT_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_44, cells=data.CHART_PV_DEBT_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_pv_debt_to_exports_custom_alternative_scenario(inputs: ChartPvDebtToExportsCustomAlternativeScenarioInputs) -> data.ChartPvDebtToExportsCustomAlternativeScenario:
    """Compute the customized A2 alternative-scenario path for the PV of the debt-to-exports ratio.

    Produce the Chart Data row 93 projection series used in the customized alternative-scenario chart for PV of debt-to-exports.

    Args:
        inputs: Keyword-only ChartPvDebtToExportsCustomAlternativeScenarioInputs dataclass of coordinate-aligned input series and scalar assumptions that parameterize the customized alternative-scenario PV debt-to-exports calculation.

    Returns:
        A data.ChartPvDebtToExportsCustomAlternativeScenario named-axis series containing the PV of debt-to-exports ratio under the A2 Alternative Scenario with customized title, indexed by the Chart Data projection years from row 35.
    """
    if not isinstance(inputs, ChartPvDebtToExportsCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_pv_debt_to_exports_custom_alternative_scenario() expected ChartPvDebtToExportsCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_pv_debt_to_exports_custom_alternative_scenario


@publish(data.CHART_OUTPUT_PV_DEBT_TO_EXPORTS.schema, constants=_CONSTANTS_30, cells=data.CHART_OUTPUT_PV_DEBT_TO_EXPORTS.cells)
def compute_chart_output_pv_debt_to_exports(inputs: ChartOutputPvDebtToExportsInputs) -> data.ChartOutputPvDebtToExports:
    """Compute the PV of debt-to-exports ratio series on Chart Data.

    Return the scenario-keyed PV of debt-to-exports chart series used in LIC-DSF public-debt stress outputs.

    Args:
        inputs: Typed input container with scenario-keyed data-series fields and scalar settings required to evaluate the PV of debt-to-exports ratio on Chart Data.

    Returns:
        A typed data.ChartOutputPvDebtToExports series of PV of debt-to-exports ratios on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputPvDebtToExportsInputs):
        raise TypeError(f"compute_chart_output_pv_debt_to_exports() expected ChartOutputPvDebtToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_pv_debt_to_exports


@publish(data.CHART_DEBT_SERVICE_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_46, cells=data.CHART_DEBT_SERVICE_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_debt_service_to_exports_custom_alternative_scenario(inputs: ChartDebtServiceToExportsCustomAlternativeScenarioInputs) -> data.ChartDebtServiceToExportsCustomAlternativeScenario:
    """Compute the customized alternative-scenario debt service-to-exports ratio series.

    Produces the Chart Data row 135 ratio path for the A2 alternative scenario over projection years from row 35.

    Args:
        inputs: Dataclass of keyword-only calculation inputs, including the named-axis data.* series and scalar assumptions that define the customized alternative scenario.

    Returns:
        A data.ChartDebtServiceToExportsCustomAlternativeScenario named-axis series of debt service-to-exports ratios over the catalog year coordinates.
    """
    if not isinstance(inputs, ChartDebtServiceToExportsCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_debt_service_to_exports_custom_alternative_scenario() expected ChartDebtServiceToExportsCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_debt_service_to_exports_custom_alternative_scenario


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_EXPORTS.schema, constants=_CONSTANTS_31, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_EXPORTS.cells)
def compute_chart_output_debt_service_to_exports(inputs: ChartOutputDebtServiceToExportsInputs) -> data.ChartOutputDebtServiceToExports:
    """Compute the debt service-to-exports ratio series for the Chart Data output surface.

    Provides the Chart Data debt service-to-exports ratio keyed by scenario for LIC-DSF charting.

    Args:
        inputs: Typed keyword-only inputs dataclass containing the scenario coordinate series and scalars required to evaluate the debt service-to-exports ratio.

    Returns:
        A data.ChartOutputDebtServiceToExports series containing debt service-to-exports ratios keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputDebtServiceToExportsInputs):
        raise TypeError(f"compute_chart_output_debt_service_to_exports() expected ChartOutputDebtServiceToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_debt_service_to_exports


@publish(data.CHART_DEBT_SERVICE_TO_REVENUE_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_46, cells=data.CHART_DEBT_SERVICE_TO_REVENUE_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_debt_service_to_revenue_custom_alternative_scenario(inputs: ChartDebtServiceToRevenueCustomAlternativeScenarioInputs) -> data.ChartDebtServiceToRevenueCustomAlternativeScenario:
    """Compute the customized A2 alternative-scenario Debt service-to-revenue ratio series.

    Derives the Chart Data Debt service-to-revenue ratio path for the custom alternative scenario from authored coordinate identities.

    Args:
        inputs: Dataclass of named-axis `data.*` series and scalar assumptions over catalog coordinates for the custom alternative scenario.

    Returns:
        A `data.ChartDebtServiceToRevenueCustomAlternativeScenario` named-axis series containing the Debt service-to-revenue ratio for the A2 customized alternative scenario, aligned to the Chart Data projection years from row 35.
    """
    if not isinstance(inputs, ChartDebtServiceToRevenueCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_debt_service_to_revenue_custom_alternative_scenario() expected ChartDebtServiceToRevenueCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_debt_service_to_revenue_custom_alternative_scenario


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_32, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE.cells)
def compute_chart_output_debt_service_to_revenue(inputs: ChartOutputDebtServiceToRevenueInputs) -> data.ChartOutputDebtServiceToRevenue:
    """Compute the Chart Data debt service-to-revenue ratio series.

    Produces the scenario-keyed debt service-to-revenue output for the LIC-DSF chart surface.

    Args:
        inputs: Typed input bundle (`ChartOutputDebtServiceToRevenueInputs`) carrying the scenario-keyed source series and configuration needed to compute the debt service-to-revenue ratio.

    Returns:
        A `data.ChartOutputDebtServiceToRevenue` series holding the debt service-to-revenue ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputDebtServiceToRevenueInputs):
        raise TypeError(f"compute_chart_output_debt_service_to_revenue() expected ChartOutputDebtServiceToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_debt_service_to_revenue


@publish(data.CHART_OUTPUT_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_35, cells=data.CHART_OUTPUT_PV_DEBT_TO_GDP.cells)
def compute_chart_output_pv_debt_to_gdp(inputs: ChartOutputPvDebtToGdpInputs) -> data.ChartOutputPvDebtToGdp:
    """Compute the PV of Debt-to-GDP Ratio on Chart Data keyed by scenario.

    Resolve authored coordinate identities into the LIC-DSF public-debt stress-block chart output.

    Args:
        inputs: Typed input container of data.* series and scalar configuration values required to compute the Chart Data PV of debt-to-GDP ratio.

    Returns:
        Typed data.ChartOutputPvDebtToGdp series containing the PV of Debt-to-GDP Ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputPvDebtToGdpInputs):
        raise TypeError(f"compute_chart_output_pv_debt_to_gdp() expected ChartOutputPvDebtToGdpInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_pv_debt_to_gdp


@publish(data.CHART_PV_DEBT_TO_REVENUE_MX_SHOCK_STANDARD_TAILORED.schema, constants=_CONSTANTS_42, cells=data.CHART_PV_DEBT_TO_REVENUE_MX_SHOCK_STANDARD_TAILORED.cells)
def compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored(inputs: ChartPvDebtToRevenueMxShockStandardTailoredInputs) -> data.ChartPvDebtToRevenueMxShockStandardTailored:
    """Compute the PV of the Debt-to-Revenue Ratio under the standard-and-tailored MX shock scenario.

    Provide the Chart Data row 306 series of the PV of debt-to-revenue path under the standard-and-tailored market-financing MX shock scenario for the DSA stress charts.

    Args:
        inputs: Keyword-only input bundle of named-axis data series over catalog coordinates supplying the macro, debt, financing, and stress assumptions required for this series.

    Returns:
        A data.ChartPvDebtToRevenueMxShockStandardTailored series holding the projected PV of the debt-to-revenue ratio along the standard-and-tailored MX shock scenario across the projection-year coordinates.
    """
    if not isinstance(inputs, ChartPvDebtToRevenueMxShockStandardTailoredInputs):
        raise TypeError(f"compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored() expected ChartPvDebtToRevenueMxShockStandardTailoredInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_pv_debt_to_revenue_mx_shock_standard_tailored


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE_FISCAL.schema, constants=_CONSTANTS_43, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE_FISCAL.cells)
def compute_chart_output_debt_service_to_revenue_fiscal(inputs: ChartOutputDebtServiceToRevenueFiscalInputs) -> data.ChartOutputDebtServiceToRevenueFiscal:
    """Compute the fiscal Debt Service-to-Revenue Ratio series for the Chart Data output surface.

    Projects the fiscal (total public debt) debt service-to-revenue ratio over catalog coordinates so it can be read alongside the other Chart Data chart series.

    Args:
        inputs: Structured fiscal-scenario inputs holding the keyword-only typed series that define the debt service-to-revenue projection, evaluated over catalog coordinates.

    Returns:
        The `chart_output_debt_service_to_revenue_fiscal` chart series on Chart Data, a typed series of the debt service-to-revenue ratio keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputDebtServiceToRevenueFiscalInputs):
        raise TypeError(f"compute_chart_output_debt_service_to_revenue_fiscal() expected ChartOutputDebtServiceToRevenueFiscalInputs, got {type(inputs).__name__}")
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
