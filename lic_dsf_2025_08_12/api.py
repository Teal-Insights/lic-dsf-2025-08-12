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
    """Compute realism1 external debt flow components.

    Derive translated component labels for the external debt-creating-flow decomposition via authored coordinate identities.

    Args:
        inputs: Realism1 external debt flow component inputs as typed data series over catalog coordinates, not a bare Python list.

    Returns:
        The typed data.Realism1ExternalDebtFlowComponents result containing translated component labels for the external debt-creating-flow decomposition.
    """
    if not isinstance(inputs, Realism1ExternalDebtFlowComponentsInputs):
        raise TypeError(f"compute_realism1_external_debt_flow_components() expected Realism1ExternalDebtFlowComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_debt_flow_components


@publish(data.REALISM1_EXTERNAL_DEBT_CREATING_FLOWS.schema, constants=_CONSTANTS_1, cells=data.REALISM1_EXTERNAL_DEBT_CREATING_FLOWS.cells)
def compute_realism1_external_debt_creating_flows(inputs: Realism1ExternalDebtCreatingFlowsInputs) -> data.Realism1ExternalDebtCreatingFlows:
    """Compute the external PPG debt-creating-flow decomposition for Realism 1.

    Produces the 5-year historical and projected external PPG debt-creating-flow decomposition from the supplied inputs.

    Args:
        inputs: Inputs dataclass providing the series and scalar parameters required to compute the external PPG debt-creating-flow decomposition.

    Returns:
        A `data.Realism1ExternalDebtCreatingFlows` series containing the external PPG debt-creating-flow decomposition with historical and projected values.
    """
    if not isinstance(inputs, Realism1ExternalDebtCreatingFlowsInputs):
        raise TypeError(f"compute_realism1_external_debt_creating_flows() expected Realism1ExternalDebtCreatingFlowsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_debt_creating_flows


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENT_LABELS.schema, constants=_CONSTANTS_0, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENT_LABELS.cells)
def compute_realism1_external_forecast_error_component_labels(inputs: Realism1ExternalForecastErrorComponentLabelsInputs) -> data.Realism1ExternalForecastErrorComponentLabels:
    """Compute chart-legend component labels for the Realism 1 external forecast-error pack.

    Return authored coordinate identities for external forecast-error component labels.

    Args:
        inputs: Typed structured inputs dataclass of data.* series over catalog coordinates for the external forecast-error component labels computation.

    Returns:
        A typed data.Realism1ExternalForecastErrorComponentLabels series of chart-legend component names for the external forecast-error pack.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorComponentLabelsInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_component_labels() expected Realism1ExternalForecastErrorComponentLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_component_labels


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENTS.schema, constants=_CONSTANTS_2, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENTS.cells)
def compute_realism1_external_forecast_error_components(inputs: Realism1ExternalForecastErrorComponentsInputs) -> data.Realism1ExternalForecastErrorComponents:
    """Compute external forecast-error components for the Realism 1 stacked-bar chart.

    Derives component-wise external forecast-error values from the supplied Realism 1 input bundle.

    Args:
        inputs: A typed input bundle of named-axis catalog-coordinate series supplying the Realism 1 external forecast-error source data.

    Returns:
        A `data.Realism1ExternalForecastErrorComponents` series of external forecast-error stacked-bar values by debt-creating-flow component, aligned over catalog coordinates.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorComponentsInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_components() expected Realism1ExternalForecastErrorComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_components


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION_LABELS.schema, constants=_CONSTANTS_3, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION_LABELS.cells)
def compute_realism1_external_forecast_error_distribution_labels(inputs: Realism1ExternalForecastErrorDistributionLabelsInputs) -> data.Realism1ExternalForecastErrorDistributionLabels:
    """Compute the Realism 1 external forecast-error distribution labels from authored coordinate identities.

    Derives the label series used to annotate the external forecast-error median and PPG-debt-change overlay in the Realism 1 chart.

    Args:
        inputs: Typed input bundle of named-axis data.* series (and any scalars) over catalog coordinates that supply the Realism 1 external forecast-error values and overlay metadata.

    Returns:
        A data.Realism1ExternalForecastErrorDistributionLabels series of labels for the external forecast-error median and PPG-debt-change overlay, indexed by the output catalog coordinates.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorDistributionLabelsInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_distribution_labels() expected Realism1ExternalForecastErrorDistributionLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_distribution_labels


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION.schema, constants=_CONSTANTS_2, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION.cells)
def compute_realism1_external_forecast_error_distribution(inputs: Realism1ExternalForecastErrorDistributionInputs) -> data.Realism1ExternalForecastErrorDistribution:
    """Compute the Realism 1 external forecast-error distribution and its country PPG-debt-change overlay.

    Derive the realism-tool distribution of external forecast errors alongside the country's PPG-debt-change path from authored coordinate identities.

    Args:
        inputs: Typed input dataclass grouping the external forecast-error median series and the country PPG-debt-change overlay series over catalog coordinates, with scalars kept as scalars.

    Returns:
        A data.Realism1ExternalForecastErrorDistribution series holding the computed external forecast-error distribution and country PPG-debt-change overlay.
    """
    if not isinstance(inputs, Realism1ExternalForecastErrorDistributionInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_distribution() expected Realism1ExternalForecastErrorDistributionInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_distribution


@publish(data.REALISM1_EXTERNAL_VINTAGE_YEARS.schema, constants=_CONSTANTS_4, cells=data.REALISM1_EXTERNAL_VINTAGE_YEARS.cells)
def compute_realism1_external_vintage_years(inputs: Realism1ExternalVintageYearsInputs) -> data.Realism1ExternalVintageYears:
    """Compute the Realism 1 external vintage years series for the LIC-DSF chart block.

    Derives the year axis copied into the external vintage debt-path chart from the supplied realism-tool inputs.

    Args:
        inputs: Typed Realism1ExternalVintageYearsInputs dataclass carrying the realism-1 external vintage year configuration, including any scalar settings and series over catalog coordinates needed to produce the result.

    Returns:
        A data.Realism1ExternalVintageYears typed series containing the year axis for the external vintage debt-path chart block.
    """
    if not isinstance(inputs, Realism1ExternalVintageYearsInputs):
        raise TypeError(f"compute_realism1_external_vintage_years() expected Realism1ExternalVintageYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_vintage_years


@publish(data.REALISM1_EXTERNAL_VINTAGE_DEBT_PATHS.schema, constants=_CONSTANTS_2, cells=data.REALISM1_EXTERNAL_VINTAGE_DEBT_PATHS.cells)
def compute_realism1_external_vintage_debt_paths(inputs: Realism1ExternalVintageDebtPathsInputs) -> data.Realism1ExternalVintageDebtPaths:
    """Compute Realism 1 external vintage debt paths.

    Derives the current, previous, and five-year-ago DSA paths of PPG external debt from authored coordinate identities.

    Args:
        inputs: Keyword-only input dataclass carrying the Realism 1 external vintage debt path inputs.

    Returns:
        Typed data.Realism1ExternalVintageDebtPaths result containing the current, previous, and five-year-ago DSA paths of PPG external debt.
    """
    if not isinstance(inputs, Realism1ExternalVintageDebtPathsInputs):
        raise TypeError(f"compute_realism1_external_vintage_debt_paths() expected Realism1ExternalVintageDebtPathsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_vintage_debt_paths


@publish(data.REALISM1_PUBLIC_DEBT_FLOW_COMPONENTS.schema, constants=_CONSTANTS_5, cells=data.REALISM1_PUBLIC_DEBT_FLOW_COMPONENTS.cells)
def compute_realism1_public_debt_flow_components(inputs: Realism1PublicDebtFlowComponentsInputs) -> data.Realism1PublicDebtFlowComponents:
    """Compute the Realism 1 public debt-creating-flow component labels.

    Translate and return the component labels for the Realism 1 decomposition of public debt-creating flows.

    Args:
        inputs: Typed dataclass of named-axis input series and scalars supplying the Realism 1 public debt-creating-flow decomposition inputs.

    Returns:
        A data.Realism1PublicDebtFlowComponents dataclass of named-axis series containing translated component labels for the public debt-creating-flow decomposition.
    """
    if not isinstance(inputs, Realism1PublicDebtFlowComponentsInputs):
        raise TypeError(f"compute_realism1_public_debt_flow_components() expected Realism1PublicDebtFlowComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_debt_flow_components


@publish(data.REALISM1_PUBLIC_DEBT_CREATING_FLOWS.schema, constants=_CONSTANTS_6, cells=data.REALISM1_PUBLIC_DEBT_CREATING_FLOWS.cells)
def compute_realism1_public_debt_creating_flows(inputs: Realism1PublicDebtCreatingFlowsInputs) -> data.Realism1PublicDebtCreatingFlows:
    """Compute the Realism 1 public debt-creating-flow decomposition from authored coordinate identities.

    Produce the 5-year historical-versus-projected public debt-creating-flow decomposition used by the Realism 1 forecast-error tool.

    Args:
        inputs: Dataclass of named-axis data.* series supplying the public debt-creating-flow decomposition inputs over historical and projection coordinates.

    Returns:
        A typed data.Realism1PublicDebtCreatingFlows series holding the public debt-creating-flow decomposition over the 5-year historical versus projected coordinate grid.
    """
    if not isinstance(inputs, Realism1PublicDebtCreatingFlowsInputs):
        raise TypeError(f"compute_realism1_public_debt_creating_flows() expected Realism1PublicDebtCreatingFlowsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_debt_creating_flows


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENT_LABELS.schema, constants=_CONSTANTS_5, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENT_LABELS.cells)
def compute_realism1_public_forecast_error_component_labels(inputs: Realism1PublicForecastErrorComponentLabelsInputs) -> data.Realism1PublicForecastErrorComponentLabels:
    """Resolve the chart-legend component labels for the Realism 1 public forecast-error pack.

    Map authored coordinate identities to the labels that identify each public forecast-error component in the Realism 1 output.

    Args:
        inputs: Typed `Realism1PublicForecastErrorComponentLabelsInputs` dataclass of `data.*` series and scalars supplying the catalog-keyed coordinates used to resolve the Realism 1 public forecast-error component labels.

    Returns:
        A `data.Realism1PublicForecastErrorComponentLabels` series of chart-legend component names for the public forecast-error pack, indexed over the catalog coordinates.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorComponentLabelsInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_component_labels() expected Realism1PublicForecastErrorComponentLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_component_labels


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENTS.schema, constants=_CONSTANTS_7, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENTS.cells)
def compute_realism1_public_forecast_error_components(inputs: Realism1PublicForecastErrorComponentsInputs) -> data.Realism1PublicForecastErrorComponents:
    """Compute Realism 1 public forecast-error components by debt-creating flow.

    Produce the stacked-bar public forecast-error decomposition series used by the Realism 1 chart data.

    Args:
        inputs: Typed input bundle of Realism 1 public forecast-error component series and scalar assumptions, supplied as Realism1PublicForecastErrorComponentsInputs.

    Returns:
        data.Realism1PublicForecastErrorComponents containing the public forecast-error stacked-bar values by debt-creating-flow component.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorComponentsInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_components() expected Realism1PublicForecastErrorComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_components


@publish(key=(), domain=None, constants=_CONSTANTS_8, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_LOWER_QUARTILE_CELLS)
def compute_realism1_public_forecast_error_lower_quartile(inputs: Realism1PublicForecastErrorLowerQuartileInputs) -> float | str:
    """Compute the Realism 1 public forecast-error lower-quartile marker.

    Evaluate the workbook-authored Realism 1 public forecast-error lower-quartile identity.

    Args:
        inputs: Typed Realism1PublicForecastErrorLowerQuartileInputs object bundling the public forecast-error lower-quartile marker series and any scalar settings required for its evaluation.

    Returns:
        The public forecast-error lower-quartile marker, returned as a float when numeric or as a str when the workbook provides a textual signal.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorLowerQuartileInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_lower_quartile() expected Realism1PublicForecastErrorLowerQuartileInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_lower_quartile


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION_LABELS.schema, constants=_CONSTANTS_9, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION_LABELS.cells)
def compute_realism1_public_forecast_error_distribution_labels(inputs: Realism1PublicForecastErrorDistributionLabelsInputs) -> data.Realism1PublicForecastErrorDistributionLabels:
    """Compute labels for the public forecast-error median and change-in-debt overlay.

    Build authored coordinate-identity labels for the Realism 1 public forecast-error distribution outputs.

    Args:
        inputs: Typed inputs for the public forecast-error distribution labels computation, including the coordinate identities required to derive the published labels.

    Returns:
        Typed data.Realism1PublicForecastErrorDistributionLabels series containing labels for the public forecast-error median and change-in-debt overlay.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorDistributionLabelsInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_distribution_labels() expected Realism1PublicForecastErrorDistributionLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_distribution_labels


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION.schema, constants=_CONSTANTS_7, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION.cells)
def compute_realism1_public_forecast_error_distribution(inputs: Realism1PublicForecastErrorDistributionInputs) -> data.Realism1PublicForecastErrorDistribution:
    """Compute the Realism 1 public forecast-error error distribution.

    Derive the public forecast-error median and country change-in-debt overlay from the supplied Realism 1 inputs.

    Args:
        inputs: Realism 1 public forecast-error distribution inputs, supplying the public forecast-error median and country change-in-debt overlay series over catalog coordinates plus any scalar configuration.

    Returns:
        A data.Realism1PublicForecastErrorDistribution dataclass of series holding the public forecast-error median and country change-in-debt overlay over catalog coordinates.
    """
    if not isinstance(inputs, Realism1PublicForecastErrorDistributionInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_distribution() expected Realism1PublicForecastErrorDistributionInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_distribution


@publish(data.REALISM1_PUBLIC_VINTAGE_YEARS.schema, constants=_CONSTANTS_4, cells=data.REALISM1_PUBLIC_VINTAGE_YEARS.cells)
def compute_realism1_public_vintage_years(inputs: Realism1PublicVintageYearsInputs) -> data.Realism1PublicVintageYears:
    """Compute the Realism 1 public vintage debt-path year axis.

    Derive the year coordinate series used by the public vintage debt-path chart block from authored coordinate identities.

    Args:
        inputs: Typed input bundle of coordinate series and scalar assumptions needed to resolve the public vintage debt-path year axis.

    Returns:
        Typed data.Realism1PublicVintageYears series containing the public vintage debt-path year axis for chart-output extraction.
    """
    if not isinstance(inputs, Realism1PublicVintageYearsInputs):
        raise TypeError(f"compute_realism1_public_vintage_years() expected Realism1PublicVintageYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_vintage_years


@publish(data.REALISM1_PUBLIC_VINTAGE_DEBT_PATHS.schema, constants=_CONSTANTS_7, cells=data.REALISM1_PUBLIC_VINTAGE_DEBT_PATHS.cells)
def compute_realism1_public_vintage_debt_paths(inputs: Realism1PublicVintageDebtPathsInputs) -> data.Realism1PublicVintageDebtPaths:
    """Compute Realism 1 public vintage total-public-debt paths.

    Derive the current, previous, and five-year-ago DSA paths of total public debt from the supplied Realism 1 inputs.

    Args:
        inputs: Keyword-only typed input bundle for Realism 1 public vintage debt paths, supplying the catalog-coordinate data needed for the DSA vintage projection.

    Returns:
        A typed data.Realism1PublicVintageDebtPaths result containing the current, previous, and five-year-ago DSA paths of total public debt over catalog coordinates.
    """
    if not isinstance(inputs, Realism1PublicVintageDebtPathsInputs):
        raise TypeError(f"compute_realism1_public_vintage_debt_paths() expected Realism1PublicVintageDebtPathsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_vintage_debt_paths


@publish(data.REALISM2_FISCAL_ADJUSTMENT_MULTIPLIER_LABELS.schema, constants=_CONSTANTS_10, cells=data.REALISM2_FISCAL_ADJUSTMENT_MULTIPLIER_LABELS.cells)
def compute_realism2_fiscal_adjustment_multiplier_labels(inputs: Realism2FiscalAdjustmentMultiplierLabelsInputs) -> data.Realism2FiscalAdjustmentMultiplierLabels:
    """Compute Realism 2 fiscal-adjustment multiplier labels.

    Build the multiplier-column legends used by the fiscal-adjustment-on-growth panel.

    Args:
        inputs: Keyword-only typed inputs dataclass carrying the Realism 2 fiscal-adjustment multiplier source series and scalars.

    Returns:
        A data.Realism2FiscalAdjustmentMultiplierLabels series of multiplier-column legends for the fiscal-adjustment-on-growth panel.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentMultiplierLabelsInputs):
        raise TypeError(f"compute_realism2_fiscal_adjustment_multiplier_labels() expected Realism2FiscalAdjustmentMultiplierLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_fiscal_adjustment_multiplier_labels


@publish(data.REALISM2_UNDERLYING_GROWTH_MULTIPLIER_LABELS.schema, constants=_CONSTANTS_10, cells=data.REALISM2_UNDERLYING_GROWTH_MULTIPLIER_LABELS.cells)
def compute_realism2_underlying_growth_multiplier_labels(inputs: Realism2UnderlyingGrowthMultiplierLabelsInputs) -> data.Realism2UnderlyingGrowthMultiplierLabels:
    """Compute the Realism 2 underlying-growth multiplier-column legend labels.

    Build the multiplier-column legends for the underlying-growth panel from the provided Realism 2 coordinate inputs.

    Args:
        inputs: Typed inputs dataclass carrying the coordinate series required to compute the Realism 2 underlying-growth multiplier-column legend labels.

    Returns:
        Realism2UnderlyingGrowthMultiplierLabels series containing the multiplier-column legends for the underlying-growth panel.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthMultiplierLabelsInputs):
        raise TypeError(f"compute_realism2_underlying_growth_multiplier_labels() expected Realism2UnderlyingGrowthMultiplierLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_underlying_growth_multiplier_labels


@publish(data.REALISM2_FISCAL_ADJUSTMENT_YEARS.schema, constants=_CONSTANTS_4, cells=data.REALISM2_FISCAL_ADJUSTMENT_YEARS.cells)
def compute_realism2_fiscal_adjustment_years(inputs: Realism2FiscalAdjustmentYearsInputs) -> data.Realism2FiscalAdjustmentYears:
    """Compute the Realism 2 fiscal-adjustment years series.

    Produce the year-axis coordinates for the fiscal-adjustment-on-growth panel used by the Realism 2 fiscal-multiplier charts.

    Args:
        inputs: Typed input dataclass containing the Realism 2 fiscal-adjustment scenario inputs.

    Returns:
        A `data.Realism2FiscalAdjustmentYears` series on the fiscal-adjustment-on-growth year axis.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentYearsInputs):
        raise TypeError(f"compute_realism2_fiscal_adjustment_years() expected Realism2FiscalAdjustmentYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_fiscal_adjustment_years


@publish(data.REALISM2_UNDERLYING_GROWTH_YEARS.schema, constants=_CONSTANTS_4, cells=data.REALISM2_UNDERLYING_GROWTH_YEARS.cells)
def compute_realism2_underlying_growth_years(inputs: Realism2UnderlyingGrowthYearsInputs) -> data.Realism2UnderlyingGrowthYears:
    """Compute the Realism 2 underlying-growth years panel from catalog-coordinate inputs.

    Provide the year-aligned underlying-growth series used by the Realism 2 fiscal-multiplier tool.

    Args:
        inputs: Realism2UnderlyingGrowthYearsInputs dataclass of catalog-coordinate inputs defining the Realism 2 underlying-growth calculation.

    Returns:
        data.Realism2UnderlyingGrowthYears typed series containing the year axis copied into the underlying-growth panel.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthYearsInputs):
        raise TypeError(f"compute_realism2_underlying_growth_years() expected Realism2UnderlyingGrowthYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_underlying_growth_years


@publish(data.REALISM2_BASELINE_GROWTH.schema, constants=_CONSTANTS_4, cells=data.REALISM2_BASELINE_GROWTH.cells)
def compute_realism2_baseline_growth(inputs: Realism2BaselineGrowthInputs) -> data.Realism2BaselineGrowth:
    """Compute the Realism 2 baseline real GDP growth path for the fiscal-multiplier chart.

    Produces the baseline growth series used by the Realism 2 fiscal-multiplier calculation from the supplied scenario inputs.

    Args:
        inputs: Typed input bundle providing the scenario series and scalar settings required to evaluate the baseline real GDP growth calculation.

    Returns:
        Data series containing the baseline real GDP growth path over the projection coordinates shown on the fiscal-multiplier chart.
    """
    if not isinstance(inputs, Realism2BaselineGrowthInputs):
        raise TypeError(f"compute_realism2_baseline_growth() expected Realism2BaselineGrowthInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_baseline_growth


@publish(data.REALISM2_GROWTH_T_MINUS_1.schema, constants=_CONSTANTS_4, cells=data.REALISM2_GROWTH_T_MINUS_1.cells)
def compute_realism2_growth_t_minus_1(inputs: Realism2GrowthTMinus1Inputs) -> data.Realism2GrowthTMinus1:
    """Compute the Realism 2 growth t-minus-1 series from typed catalog-coordinate inputs.

    Carry pre-projection growth into the underlying-growth panel for Realism 2.

    Args:
        inputs: Keyword-only input bundle, typed as Realism2GrowthTMinus1Inputs, supplying the catalog-coordinate series and scalars needed to derive the pre-projection growth values.

    Returns:
        A data.Realism2GrowthTMinus1 series containing pre-projection growth carried into the underlying-growth panel.
    """
    if not isinstance(inputs, Realism2GrowthTMinus1Inputs):
        raise TypeError(f"compute_realism2_growth_t_minus_1() expected Realism2GrowthTMinus1Inputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_growth_t_minus_1


@publish(data.REALISM2_FISCAL_ADJUSTMENT_GROWTH_IMPACT.schema, constants=_CONSTANTS_10, cells=data.REALISM2_FISCAL_ADJUSTMENT_GROWTH_IMPACT.cells)
def compute_realism2_fiscal_adjustment_growth_impact(inputs: Realism2FiscalAdjustmentGrowthImpactInputs) -> data.Realism2FiscalAdjustmentGrowthImpact:
    """Compute the growth impact of the planned fiscal adjustment under alternative multipliers.

    Produces the Realism 2 fiscal-adjustment growth-impact result from the supplied multiplier-scenario inputs.

    Args:
        inputs: Typed `Realism2FiscalAdjustmentGrowthImpactInputs` dataclass of named-axis series over catalog coordinates supplying the planned fiscal adjustment and alternative multiplier assumptions.

    Returns:
        Typed `data.Realism2FiscalAdjustmentGrowthImpact` result containing the growth-impact series of the planned fiscal adjustment under alternative multipliers.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentGrowthImpactInputs):
        raise TypeError(f"compute_realism2_fiscal_adjustment_growth_impact() expected Realism2FiscalAdjustmentGrowthImpactInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_fiscal_adjustment_growth_impact


@publish(data.REALISM2_UNDERLYING_GROWTH.schema, constants=_CONSTANTS_10, cells=data.REALISM2_UNDERLYING_GROWTH.cells)
def compute_realism2_underlying_growth(inputs: Realism2UnderlyingGrowthInputs) -> data.Realism2UnderlyingGrowth:
    """Compute Realism 2 underlying growth paths.

    Derives underlying growth projections under alternative fiscal-multiplier assumptions from the supplied Realism 2 inputs.

    Args:
        inputs: Typed `Realism2UnderlyingGrowthInputs` dataclass of `data.*` series supplying the fiscal-multiplier assumptions and supporting macro-debt paths for the calculation.

    Returns:
        A `data.Realism2UnderlyingGrowth` series of underlying growth paths under alternative fiscal-multiplier assumptions.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthInputs):
        raise TypeError(f"compute_realism2_underlying_growth() expected Realism2UnderlyingGrowthInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_underlying_growth


@publish(data.REALISM3_INVESTMENT_YEARS.schema, constants=_CONSTANTS_4, cells=data.REALISM3_INVESTMENT_YEARS.cells)
def compute_realism3_investment_years(inputs: Realism3InvestmentYearsInputs) -> data.Realism3InvestmentYears:
    """Compute the Realism 3 investment vintage-comparison year axis.

    Returns the year-axis series used in the public/private investment vintage-comparison chart.

    Args:
        inputs: A Realism3InvestmentYearsInputs instance providing the workbook-derived inputs needed to compute the year-axis series.

    Returns:
        A data.Realism3InvestmentYears typed series containing the year axis for the public/private investment vintage-comparison chart.
    """
    if not isinstance(inputs, Realism3InvestmentYearsInputs):
        raise TypeError(f"compute_realism3_investment_years() expected Realism3InvestmentYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_investment_years


@publish(data.REALISM3_INVESTMENT_PATH_LABELS.schema, constants=_CONSTANTS_11, cells=data.REALISM3_INVESTMENT_PATH_LABELS.cells)
def compute_realism3_investment_path_labels(inputs: Realism3InvestmentPathLabelsInputs) -> data.Realism3InvestmentPathLabels:
    """Compute the Realism 3 investment-path labels from the supplied input bundle.

    Resolve the authored coordinate identities into row legends comparing previous and current DSA public and private investment paths.

    Args:
        inputs: A Realism3InvestmentPathLabelsInputs dataclass of keyword-only input series and scalars used to resolve the Realism 3 investment-path coordinate identities.

    Returns:
        A data.Realism3InvestmentPathLabels value containing the row legends for previous versus current DSA public and private investment paths.
    """
    if not isinstance(inputs, Realism3InvestmentPathLabelsInputs):
        raise TypeError(f"compute_realism3_investment_path_labels() expected Realism3InvestmentPathLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_investment_path_labels


@publish(data.REALISM3_PUBLIC_PRIVATE_INVESTMENT_PATHS.schema, constants=_CONSTANTS_12, cells=data.REALISM3_PUBLIC_PRIVATE_INVESTMENT_PATHS.cells)
def compute_realism3_public_private_investment_paths(inputs: Realism3PublicPrivateInvestmentPathsInputs) -> data.Realism3PublicPrivateInvestmentPaths:
    """Compute Realism 3 public and private investment paths as percent of GDP across current and prior DSA vintages.

    Provide the realism-tool investment paths needed for the Realism 3 comparison of current and previous DSA assumptions.

    Args:
        inputs: A Realism3PublicPrivateInvestmentPathsInputs bundle containing the coordinate inputs and assumptions required to evaluate public and private investment (% of GDP) paths.

    Returns:
        A data.Realism3PublicPrivateInvestmentPaths value carrying the computed public and private investment (% of GDP) paths for the current and previous DSA vintage.
    """
    if not isinstance(inputs, Realism3PublicPrivateInvestmentPathsInputs):
        raise TypeError(f"compute_realism3_public_private_investment_paths() expected Realism3PublicPrivateInvestmentPathsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_public_private_investment_paths


@publish(data.REALISM3_GROWTH_ACCOUNTING_VINTAGES.schema, constants=_CONSTANTS_13, cells=data.REALISM3_GROWTH_ACCOUNTING_VINTAGES.cells)
def compute_realism3_growth_accounting_vintages(inputs: Realism3GrowthAccountingVintagesInputs) -> data.Realism3GrowthAccountingVintages:
    """Compute Realism 3 investment-growth accounting vintage headers.

    Produce the vintage-labelled investment-growth accounting summary series from the authored Realism 3 inputs.

    Args:
        inputs: Typed Realism3GrowthAccountingVintagesInputs bundle containing the Realism 3 investment-growth accounting vintage inputs and their coordinate metadata.

    Returns:
        A data.Realism3GrowthAccountingVintages series of vintage headers for the investment-growth accounting summary, indexed by the authored vintage coordinates.
    """
    if not isinstance(inputs, Realism3GrowthAccountingVintagesInputs):
        raise TypeError(f"compute_realism3_growth_accounting_vintages() expected Realism3GrowthAccountingVintagesInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_growth_accounting_vintages


@publish(data.REALISM3_GROWTH_ACCOUNTING_CONTRIBUTIONS.schema, constants=_CONSTANTS_14, cells=data.REALISM3_GROWTH_ACCOUNTING_CONTRIBUTIONS.cells)
def compute_realism3_growth_accounting_contributions(inputs: Realism3GrowthAccountingContributionsInputs) -> data.Realism3GrowthAccountingContributions:
    """Compute the five-year-average contributions of government capital and other factors to growth for the Realism 3 invest-growth tool.

    Derive the Realism 3 growth-accounting contribution series from the bound inputs so the invest-growth chart and its summary can be charted.

    Args:
        inputs: Keyword-only bundle of Realism 3 growth-accounting inputs, supplying the investment, growth, and factor-share series over catalog coordinates needed to decompose contributions.

    Returns:
        A data.Realism3GrowthAccountingContributions series holding the five-year-average contribution of government capital and other factors to growth.
    """
    if not isinstance(inputs, Realism3GrowthAccountingContributionsInputs):
        raise TypeError(f"compute_realism3_growth_accounting_contributions() expected Realism3GrowthAccountingContributionsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_growth_accounting_contributions


@publish(key=(), domain=None, constants=_CONSTANTS_15, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_LABEL_CELLS)
def compute_realism4_projected_3yr_adjustment_label(inputs: Realism4Projected3yrAdjustmentLabelInputs) -> str | int | float | bool:
    """Compute the Realism 4 projected 3-year fiscal-adjustment label from authored coordinate identities.

    Resolve the country's projected 3-year fiscal-adjustment marker for the Realism 4 fiscal-adjustment output.

    Args:
        inputs: Typed Realism4Projected3yrAdjustmentLabelInputs bundle of named-axis coordinate data series and scalar settings needed to identify the projected 3-year fiscal-adjustment label.

    Returns:
        The Realism 4 projected 3-year fiscal-adjustment label as a scalar str, int, float, or bool.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentLabelInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_label() expected Realism4Projected3yrAdjustmentLabelInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_label


@publish(key=(), domain=None, constants=_CONSTANTS_4, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_CELLS)
def compute_realism4_projected_3yr_adjustment(inputs: Realism4Projected3yrAdjustmentInputs) -> float | str:
    """Computes the Realism 4 projected 3-year fiscal adjustment.

    Evaluates the Realism 4 fiscal-adjustment placement and distribution identities to obtain the projected 3-year adjustment used by Output 4-2.

    Args:
        inputs: Typed Realism 4 projected 3-year fiscal adjustment inputs dataclass containing the required coordinate series and scalar settings.

    Returns:
        Projected 3-year fiscal adjustment (ppt of GDP), returned as a float or a str.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment() expected Realism4Projected3yrAdjustmentInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment


@publish(key=(), domain=None, constants=_CONSTANTS_4, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_BIN_CELLS)
def compute_realism4_projected_3yr_adjustment_bin(inputs: Realism4Projected3yrAdjustmentBinInputs) -> float | str:
    """Compute the Realism 4 projected 3-year fiscal adjustment bin.

    Places the projected 3-year fiscal adjustment onto its histogram bin by rounding to the bin edge.

    Args:
        inputs: Dataclass containing the named-axis data.* series and scalar values required to derive the projected 3-year fiscal-adjustment measure and its histogram bin placement.

    Returns:
        The projected 3-year adjustment rounded to the histogram bin edge, returned as a float when numeric or a str when the bin edge is represented as text.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentBinInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_bin() expected Realism4Projected3yrAdjustmentBinInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_bin


@publish(key=(), domain=None, constants=_CONSTANTS_16, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_CATEGORY_CELLS)
def compute_realism4_projected_3yr_adjustment_category(inputs: Realism4Projected3yrAdjustmentCategoryInputs) -> float | str:
    """Compute the Realism 4 projected three-year fiscal adjustment histogram category.

    Places a country's projected three-year fiscal adjustment into its Realism 4 distribution bin for the fiscal-adjustment chart.

    Args:
        inputs: Typed input bundle of named-axis series over catalog coordinates supplying the projected fiscal-adjustment path for the country's projection years.

    Returns:
        Histogram category index (X) of the country's projected adjustment, returned as a numeric index or its textual category label.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentCategoryInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_category() expected Realism4Projected3yrAdjustmentCategoryInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_category


@publish(key=(), domain=None, constants=_CONSTANTS_16, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_SAMPLE_SHARE_CELLS)
def compute_realism4_projected_3yr_adjustment_sample_share(inputs: Realism4Projected3yrAdjustmentSampleShareInputs) -> float | str:
    """Compute the Realism 4 projected 3-year adjustment sample share.

    Return the percent-of-sample at the country's projected-adjustment bin from authored coordinate identities.

    Args:
        inputs: Typed input bundle of coordinate identity values for the Realism 4 projected 3-year adjustment sample-share calculation.

    Returns:
        The percent-of-sample (Y) at the country's projected-adjustment bin, returned as a float or string.
    """
    if not isinstance(inputs, Realism4Projected3yrAdjustmentSampleShareInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_sample_share() expected Realism4Projected3yrAdjustmentSampleShareInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_sample_share


@publish(key=(), domain=None, constants=_CONSTANTS_17, cells=data.REALISM4_FISCAL_ADJUSTMENT_TOP_BIN_LABEL_CELLS)
def compute_realism4_fiscal_adjustment_top_bin_label(inputs: Realism4FiscalAdjustmentTopBinLabelInputs) -> str | int | float | bool:
    """Return the open-ended top-bin label for the Realism 4 fiscal-adjustment histogram.

    Provide the scalar label that identifies the highest fiscal-adjustment bin used in the Realism 4 distribution.

    Args:
        inputs: Typed Realism4FiscalAdjustmentTopBinLabelInputs bundle containing the authored coordinate inputs for the Realism 4 fiscal-adjustment top-bin label calculation.

    Returns:
        The scalar top-bin label, returned as str, int, float, or bool according to the authored workbook coordinate value.
    """
    if not isinstance(inputs, Realism4FiscalAdjustmentTopBinLabelInputs):
        raise TypeError(f"compute_realism4_fiscal_adjustment_top_bin_label() expected Realism4FiscalAdjustmentTopBinLabelInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_fiscal_adjustment_top_bin_label


@publish(data.REALISM4_FISCAL_ADJUSTMENT_SAMPLE_SHARE.schema, constants=_CONSTANTS_18, cells=data.REALISM4_FISCAL_ADJUSTMENT_SAMPLE_SHARE.cells)
def compute_realism4_fiscal_adjustment_sample_share(inputs: Realism4FiscalAdjustmentSampleShareInputs) -> data.Realism4FiscalAdjustmentSampleShare:
    """Compute the LIC sample share in each three-year fiscal-adjustment bin.

    Derive the Realism 4 fiscal-adjustment distribution used by the corresponding chart data.

    Args:
        inputs: Typed `data.*` series bundle over catalog coordinates supplying the fiscal-adjustment binning and sample membership inputs.

    Returns:
        Typed `data.Realism4FiscalAdjustmentSampleShare` series reporting the percent of the LIC sample in each three-year fiscal-adjustment bin.
    """
    if not isinstance(inputs, Realism4FiscalAdjustmentSampleShareInputs):
        raise TypeError(f"compute_realism4_fiscal_adjustment_sample_share() expected Realism4FiscalAdjustmentSampleShareInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_fiscal_adjustment_sample_share


@publish(data.REALISM4_FISCAL_ADJUSTMENT_CUMULATIVE_SHARE.schema, constants=_CONSTANTS_18, cells=data.REALISM4_FISCAL_ADJUSTMENT_CUMULATIVE_SHARE.cells)
def compute_realism4_fiscal_adjustment_cumulative_share(inputs: Realism4FiscalAdjustmentCumulativeShareInputs) -> data.Realism4FiscalAdjustmentCumulativeShare:
    """Compute the Realism 4 fiscal-adjustment cumulative share.

    Return the cumulative percent of the LIC sample up to each fiscal-adjustment bin.

    Args:
        inputs: Typed Realism 4 fiscal-adjustment cumulative-share inputs, containing named-axis data.* series and scalars over catalog coordinates needed for the calculation.

    Returns:
        A data.Realism4FiscalAdjustmentCumulativeShare typed series containing the cumulative percent of the LIC sample up to each fiscal-adjustment bin.
    """
    if not isinstance(inputs, Realism4FiscalAdjustmentCumulativeShareInputs):
        raise TypeError(f"compute_realism4_fiscal_adjustment_cumulative_share() expected Realism4FiscalAdjustmentCumulativeShareInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_fiscal_adjustment_cumulative_share


@publish(data.PROBABILITY_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_19, cells=data.PROBABILITY_PV_DEBT_TO_GDP.cells)
def compute_probability_pv_debt_to_gdp(inputs: ProbabilityPvDebtToGdpInputs) -> data.ProbabilityPvDebtToGdp:
    """Compute the probability-approach PV of PPG external debt-to-GDP series.

    Derive baseline, historical, MX shock, threshold, and band paths for the PV of PPG external debt-to-GDP probability indicator.

    Args:
        inputs: ProbabilityPvDebtToGdpInputs dataclass of named-axis data.* series over catalog coordinates supplying the baseline, historical, MX shock, threshold, and band inputs for the PV of PPG external debt-to-GDP probability calculation.

    Returns:
        A data.ProbabilityPvDebtToGdp named-axis series over catalog coordinates containing the resulting baseline, historical, MX shock, threshold, and band paths for the PV of PPG external debt to GDP.
    """
    if not isinstance(inputs, ProbabilityPvDebtToGdpInputs):
        raise TypeError(f"compute_probability_pv_debt_to_gdp() expected ProbabilityPvDebtToGdpInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_gdp


@publish(data.PROBABILITY_PV_DEBT_TO_EXPORTS.schema, constants=_CONSTANTS_20, cells=data.PROBABILITY_PV_DEBT_TO_EXPORTS.cells)
def compute_probability_pv_debt_to_exports(inputs: ProbabilityPvDebtToExportsInputs) -> data.ProbabilityPvDebtToExports:
    """Compute the probability PV of PPG external debt-to-exports paths.

    Evaluate the probability-approach debt-to-exports indicator from an authored input bundle.

    Args:
        inputs: Authored ProbabilityPvDebtToExportsInputs bundle supplying the model inputs for the probability PV debt-to-exports calculation.

    Returns:
        A data.ProbabilityPvDebtToExports series containing the baseline, historical, MX shock, threshold, and band values for PV of PPG external debt to exports.
    """
    if not isinstance(inputs, ProbabilityPvDebtToExportsInputs):
        raise TypeError(f"compute_probability_pv_debt_to_exports() expected ProbabilityPvDebtToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_exports


@publish(data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS.schema, constants=_CONSTANTS_21, cells=data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS.cells)
def compute_probability_debt_service_to_exports(inputs: ProbabilityDebtServiceToExportsInputs) -> data.ProbabilityDebtServiceToExports:
    """Compute probability debt service to exports paths.

    Derives the PPG external debt service-to-exports probability output series from supplied model inputs.

    Args:
        inputs: Typed ProbabilityDebtServiceToExportsInputs bundle containing the coordinate-aligned input series and scalar assumptions required by the calculation.

    Returns:
        A typed ProbabilityDebtServiceToExports series over catalog coordinates with baseline, historical, MX-shock, threshold, and band paths for PPG external debt service to exports.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToExportsInputs):
        raise TypeError(f"compute_probability_debt_service_to_exports() expected ProbabilityDebtServiceToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_exports


@publish(data.PROBABILITY_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_22, cells=data.PROBABILITY_DEBT_SERVICE_TO_REVENUE.cells)
def compute_probability_debt_service_to_revenue(inputs: ProbabilityDebtServiceToRevenueInputs) -> data.ProbabilityDebtServiceToRevenue:
    """Compute the probability-approach PPG external debt service-to-revenue series.

    Derive the Chart Data debt service-to-revenue indicator path that drives the probability-approach charts and DSA write-up.

    Args:
        inputs: Input bundle of typed, named-axis data series over catalog coordinates carrying the baseline, historical, MX shock, threshold, and band assumptions for the PPG external debt service-to-revenue indicator; scalars remain scalars.

    Returns:
        A data.ProbabilityDebtServiceToRevenue named-axis series holding the computed PPG external debt service-to-revenue path, including baseline, historical, MX shock, threshold, and band coordinates.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToRevenueInputs):
        raise TypeError(f"compute_probability_debt_service_to_revenue() expected ProbabilityDebtServiceToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_revenue


@publish(data.PROBABILITY_PV_DEBT_TO_GDP_DISTRESS.schema, constants=_CONSTANTS_23, cells=data.PROBABILITY_PV_DEBT_TO_GDP_DISTRESS.cells)
def compute_probability_pv_debt_to_gdp_distress(inputs: ProbabilityPvDebtToGdpDistressInputs) -> data.ProbabilityPvDebtToGdpDistress:
    """Compute the probability of external-debt distress for PV debt-to-GDP.

    Derive the PV debt-to-GDP distress probability path under baseline, historical, MX, and threshold scenarios.

    Args:
        inputs: Typed inputs dataclass bundling the probability-approach series and scalar assumptions required to evaluate PV debt-to-GDP distress.

    Returns:
        A data.ProbabilityPvDebtToGdpDistress series giving the probability of external-debt distress for PV debt-to-GDP under baseline, historical, MX, and threshold scenarios.
    """
    if not isinstance(inputs, ProbabilityPvDebtToGdpDistressInputs):
        raise TypeError(f"compute_probability_pv_debt_to_gdp_distress() expected ProbabilityPvDebtToGdpDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_gdp_distress


@publish(data.PROBABILITY_PV_DEBT_TO_EXPORTS_DISTRESS.schema, constants=_CONSTANTS_24, cells=data.PROBABILITY_PV_DEBT_TO_EXPORTS_DISTRESS.cells)
def compute_probability_pv_debt_to_exports_distress(inputs: ProbabilityPvDebtToExportsDistressInputs) -> data.ProbabilityPvDebtToExportsDistress:
    """Compute the probability of external-debt distress for PV debt-to-exports under baseline, historical, MX, and threshold scenarios.

    Derives the LIC-DSF probability path for PV debt-to-exports distress from pre-bound input series.

    Args:
        inputs: ProbabilityPvDebtToExportsDistressInputs dataclass containing the pre-bound named-axis series required for the PV debt-to-exports distress calculation.

    Returns:
        data.ProbabilityPvDebtToExportsDistress series giving the probability of external-debt distress for PV debt-to-exports under baseline, historical, MX, and threshold scenarios.
    """
    if not isinstance(inputs, ProbabilityPvDebtToExportsDistressInputs):
        raise TypeError(f"compute_probability_pv_debt_to_exports_distress() expected ProbabilityPvDebtToExportsDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_exports_distress


@publish(data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS_DISTRESS.schema, constants=_CONSTANTS_25, cells=data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS_DISTRESS.cells)
def compute_probability_debt_service_to_exports_distress(inputs: ProbabilityDebtServiceToExportsDistressInputs) -> data.ProbabilityDebtServiceToExportsDistress:
    """Compute the probability of external-debt distress for debt service-to-exports under baseline, historical, MX, and threshold conditions.

    Evaluates the debt service-to-exports distress probability from the provided input assumptions.

    Args:
        inputs: Typed input dataclass containing the named-axis series and scalar parameters required for the debt service-to-exports probability calculation.

    Returns:
        data.ProbabilityDebtServiceToExportsDistress: named-axis series of external-debt distress probabilities for debt service/exports under baseline, historical, MX, and threshold.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToExportsDistressInputs):
        raise TypeError(f"compute_probability_debt_service_to_exports_distress() expected ProbabilityDebtServiceToExportsDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_exports_distress


@publish(data.PROBABILITY_DEBT_SERVICE_TO_REVENUE_DISTRESS.schema, constants=_CONSTANTS_26, cells=data.PROBABILITY_DEBT_SERVICE_TO_REVENUE_DISTRESS.cells)
def compute_probability_debt_service_to_revenue_distress(inputs: ProbabilityDebtServiceToRevenueDistressInputs) -> data.ProbabilityDebtServiceToRevenueDistress:
    """Compute the probability of external-debt distress for the debt service-to-revenue ratio.

    Evaluate debt service-to-revenue distress probabilities under baseline, historical, MX, and threshold scenarios.

    Args:
        inputs: Input dataclass supplying the debt service-to-revenue probability scenario parameters and catalog-coordinate series needed for computation.

    Returns:
        A data.ProbabilityDebtServiceToRevenueDistress series giving distress probabilities for the debt service-to-revenue ratio under baseline, historical, MX, and threshold scenarios.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToRevenueDistressInputs):
        raise TypeError(f"compute_probability_debt_service_to_revenue_distress() expected ProbabilityDebtServiceToRevenueDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_revenue_distress


@publish(key=(), domain=None, constants=_CONSTANTS_27, cells=data.EXTERNAL_DSA_RISK_RATING_SIGNAL_CELLS)
def compute_external_dsa_risk_rating_signal(inputs: ExternalDsaRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute the external DSA risk-rating text signal.

    Extracts the baseline external risk-rating signal from the Chart Data risk-rating block.

    Args:
        inputs: Typed input bundle containing the external DSA risk-rating signal series over catalog coordinates, plus any scalar controls required by the model.

    Returns:
        The external DSA risk-rating signal from Chart Data!D10 as a string, integer, float, or boolean value.
    """
    if not isinstance(inputs, ExternalDsaRiskRatingSignalInputs):
        raise TypeError(f"compute_external_dsa_risk_rating_signal() expected ExternalDsaRiskRatingSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_dsa_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_28, cells=data.EXTERNAL_DSA_RISK_RATING_NUMERIC_CELLS)
def compute_external_dsa_risk_rating_numeric(inputs: ExternalDsaRiskRatingNumericInputs) -> float | str:
    """Compute the external DSA risk-rating numeric signal from the typed inputs bundle.

    Resolve the Chart Data external DSA risk-rating numeric code through the model's authored coordinate identities.

    Args:
        inputs: Typed input bundle for the external DSA risk-rating numeric calculation, providing the named-axis data.* series and scalar values consumed by the model.

    Returns:
        The external DSA risk-rating numeric signal from Chart Data!D11, returned as a float numeric code or a str textual rating.
    """
    if not isinstance(inputs, ExternalDsaRiskRatingNumericInputs):
        raise TypeError(f"compute_external_dsa_risk_rating_numeric() expected ExternalDsaRiskRatingNumericInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_dsa_risk_rating_numeric


@publish(key=(), domain=None, constants=_CONSTANTS_28, cells=data.EXTERNAL_BASELINE_BREACH_CELLS)
def compute_external_baseline_breach(inputs: ExternalBaselineBreachInputs) -> float | str:
    """Compute the external baseline breach flag from model inputs.

    Evaluates whether the external DSA baseline breaches its threshold, excluding one-year breaches, for downstream risk-rating signals.

    Args:
        inputs: Typed external baseline breach inputs, provided as an ExternalBaselineBreachInputs model series or dataclass.

    Returns:
        Scalar float or str external baseline breach flag: 0 for no breach, 1 for breach, excluding 1-year breaches (Chart Data!D12).
    """
    if not isinstance(inputs, ExternalBaselineBreachInputs):
        raise TypeError(f"compute_external_baseline_breach() expected ExternalBaselineBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_baseline_breach


@publish(key=(), domain=None, constants=_CONSTANTS_28, cells=data.EXTERNAL_SHOCK_BREACH_CELLS)
def compute_external_shock_breach(inputs: ExternalShockBreachInputs) -> float | str:
    """Compute the external shock breach flag from external shock breach inputs.

    Returns the Chart Data external shock breach indicator under the authored coordinate identities.

    Args:
        inputs: External shock breach inputs as an ExternalShockBreachInputs instance.

    Returns:
        The external shock breach flag: a float 0/1 (0=no breach, 1=breach, excluding 1-year breaches) or a string when a text signal is carried through.
    """
    if not isinstance(inputs, ExternalShockBreachInputs):
        raise TypeError(f"compute_external_shock_breach() expected ExternalShockBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_shock_breach


@publish(key=(), domain=None, constants=_CONSTANTS_29, cells=data.EXTERNAL_PV_DEBT_TO_GDP_MX_SHOCK_CELLS)
def compute_external_pv_debt_to_gdp_mx_shock(inputs: ExternalPvDebtToGdpMxShockInputs) -> str | int | float | bool:
    """Compute the external PV debt-to-GDP MX-shock label.

    Resolve the Chart Data!D14 MX-shock signal used by external DSA risk-rating outputs.

    Args:
        inputs: Keyword-only `ExternalPvDebtToGdpMxShockInputs` dataclass containing the coordinate inputs for the external PV debt-to-GDP MX-shock calculation.

    Returns:
        The external PV debt-to-GDP MX-shock label from Chart Data!D14, returned as a scalar with annotation `str | int | float | bool`.
    """
    if not isinstance(inputs, ExternalPvDebtToGdpMxShockInputs):
        raise TypeError(f"compute_external_pv_debt_to_gdp_mx_shock() expected ExternalPvDebtToGdpMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_pv_debt_to_gdp_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_30, cells=data.EXTERNAL_PV_DEBT_TO_EXPORTS_MX_SHOCK_CELLS)
def compute_external_pv_debt_to_exports_mx_shock(inputs: ExternalPvDebtToExportsMxShockInputs) -> str | int | float | bool:
    """Compute the external PV of debt-to-exports MX shock label.

    Extracts the Chart Data!D15 external PV debt-to-exports MX shock signal for the LIC-DSF external risk rating and chart series.

    Args:
        inputs: Dataclass of named-axis series and scalar fields carrying the external PV debt-to-exports MX shock coordinates (Chart Data!D15).

    Returns:
        The external PV debt-to-exports MX shock signal as a str, int, float, or bool, typically the PV of debt-to-exports ratio MX shock label or numeric value from Chart Data!D15.
    """
    if not isinstance(inputs, ExternalPvDebtToExportsMxShockInputs):
        raise TypeError(f"compute_external_pv_debt_to_exports_mx_shock() expected ExternalPvDebtToExportsMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_pv_debt_to_exports_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_31, cells=data.EXTERNAL_DEBT_SERVICE_TO_EXPORTS_MX_SHOCK_CELLS)
def compute_external_debt_service_to_exports_mx_shock(inputs: ExternalDebtServiceToExportsMxShockInputs) -> str | int | float | bool:
    """Compute the external debt service-to-exports MX shock label using authored coordinate identities.

    Derive the Chart Data signal for the external debt service-to-exports ratio under the MX shock scenario.

    Args:
        inputs: Keyword-only ExternalDebtServiceToExportsMxShockInputs dataclass supplying the coordinate inputs required to evaluate the external debt service-to-exports MX shock calculation.

    Returns:
        The external debt service-to-exports MX shock label (Chart Data!D16; debt service-to-exports ratio MX shock), returned as a scalar str, int, float, or bool.
    """
    if not isinstance(inputs, ExternalDebtServiceToExportsMxShockInputs):
        raise TypeError(f"compute_external_debt_service_to_exports_mx_shock() expected ExternalDebtServiceToExportsMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_debt_service_to_exports_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_32, cells=data.EXTERNAL_DEBT_SERVICE_TO_REVENUE_MX_SHOCK_CELLS)
def compute_external_debt_service_to_revenue_mx_shock(inputs: ExternalDebtServiceToRevenueMxShockInputs) -> str | int | float | bool:
    """Compute the external debt service-to-revenue MX shock label.

    Reads the Market-financing shock label used in the external DSA risk-rating signal.

    Args:
        inputs: ExternalDebtServiceToRevenueMxShockInputs dataclass containing the typed data.* series coordinates and scalar settings required for this MX shock output.

    Returns:
        The Chart Data!D17 value for Debt service to revenue MX shock - Market, as a scalar str, int, float, or bool.
    """
    if not isinstance(inputs, ExternalDebtServiceToRevenueMxShockInputs):
        raise TypeError(f"compute_external_debt_service_to_revenue_mx_shock() expected ExternalDebtServiceToRevenueMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_debt_service_to_revenue_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_33, cells=data.FISCAL_RISK_RATING_SIGNAL_CELLS)
def compute_fiscal_risk_rating_signal(inputs: FiscalRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute the fiscal risk-rating signal from authored coordinate identities.

    Resolve the Chart Data fiscal risk-rating text/numeric signal for the total public debt DSA.

    Args:
        inputs: Fiscal risk-rating signal inputs as a FiscalRiskRatingSignalInputs dataclass of catalog-coordinate series that supply the rating context.

    Returns:
        Fiscal risk-rating signal as a scalar value typed str | int | float | bool, matching the Chart Data!I10 rating text or associated numeric/boolean breach indicator.
    """
    if not isinstance(inputs, FiscalRiskRatingSignalInputs):
        raise TypeError(f"compute_fiscal_risk_rating_signal() expected FiscalRiskRatingSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_34, cells=data.FISCAL_RISK_RATING_NUMERIC_CELLS)
def compute_fiscal_risk_rating_numeric(inputs: FiscalRiskRatingNumericInputs) -> float | str:
    """Compute the fiscal risk-rating numeric code from authored coordinate identities.

    Extract the Chart Data!I11 fiscal risk-rating numeric signal for DSA charting and risk-rating propagation.

    Args:
        inputs: Typed FiscalRiskRatingNumericInputs dataclass grouping the named-axis catalog series and scalar controls required by the fiscal risk-rating numeric identity, with series supplied as data.* tensors rather than bare lists.

    Returns:
        The fiscal risk-rating numeric code (Chart Data!I11; signal for external risk rating (numeric)) as a float, or a string label when the rating is non-numeric.
    """
    if not isinstance(inputs, FiscalRiskRatingNumericInputs):
        raise TypeError(f"compute_fiscal_risk_rating_numeric() expected FiscalRiskRatingNumericInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_risk_rating_numeric


@publish(key=(), domain=None, constants=_CONSTANTS_34, cells=data.FISCAL_BASELINE_BREACH_CELLS)
def compute_fiscal_baseline_breach(inputs: FiscalBaselineBreachInputs) -> float | str:
    """Compute the fiscal baseline breach flag.

    Derive the 0/1 fiscal baseline breach signal from authored coordinate identities.

    Args:
        inputs: Typed input dataclass carrying the coordinate data series required to evaluate the fiscal baseline breach.

    Returns:
        Fiscal baseline breach flag (0 = no breach, 1 = breach), excluding one-year breaches, as a float or str.
    """
    if not isinstance(inputs, FiscalBaselineBreachInputs):
        raise TypeError(f"compute_fiscal_baseline_breach() expected FiscalBaselineBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_baseline_breach


@publish(key=(), domain=None, constants=_CONSTANTS_34, cells=data.FISCAL_SHOCK_BREACH_CELLS)
def compute_fiscal_shock_breach(inputs: FiscalShockBreachInputs) -> float | str:
    """Compute the fiscal shock breach flag for the LIC-DSF IDA21 template.

    Evaluate whether the total public debt metric breaches under the fiscal shock scenario, excluding one-year breaches.

    Args:
        inputs: Fiscal shock breach input bundle as a typed FiscalShockBreachInputs value carrying the required scalar and series inputs.

    Returns:
        The fiscal shock breach flag as a float value of 0 for no breach or 1 for breach, or a string indicator, excluding one-year breaches.
    """
    if not isinstance(inputs, FiscalShockBreachInputs):
        raise TypeError(f"compute_fiscal_shock_breach() expected FiscalShockBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_shock_breach


@publish(key=(), domain=None, constants=_CONSTANTS_35, cells=data.FISCAL_PV_DEBT_TO_GDP_MX_SHOCK_CELLS)
def compute_fiscal_pv_debt_to_gdp_mx_shock(inputs: FiscalPvDebtToGdpMxShockInputs) -> str | int | float | bool:
    """Compute the fiscal PV debt-to-GDP Mexico shock label.

    Derive the PV of debt-to-GDP ratio MX shock signal from the workbook's authored coordinate identities.

    Args:
        inputs: Structured FiscalPvDebtToGdpMxShockInputs dataclass supplying the named-axis series and scalar coordinates required by the fiscal PV debt-to-GDP MX shock calculation.

    Returns:
        Scalar fiscal PV debt-to-GDP MX shock label from Chart Data!I14, typed as str | int | float | bool, representing the PV of debt-to-GDP ratio MX shock.
    """
    if not isinstance(inputs, FiscalPvDebtToGdpMxShockInputs):
        raise TypeError(f"compute_fiscal_pv_debt_to_gdp_mx_shock() expected FiscalPvDebtToGdpMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_pv_debt_to_gdp_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_36, cells=data.TAILORED_STRESS_NATURAL_DISASTER_APPLICABLE_CELLS)
def compute_tailored_stress_natural_disaster_applicable(inputs: TailoredStressNaturalDisasterApplicableInputs) -> float | str:
    """Compute the natural-disaster tailored stress applicability indicator from authored Chart Data coordinate identities.

    Resolve the 0/1 flag marking whether the natural-disaster tailored stress test applies, using the debt service-to-revenue MX shock (Market) signal.

    Args:
        inputs: Keyword-only inputs bundle (TailoredStressNaturalDisasterApplicableInputs) holding the typed data.* series over catalog coordinates that carry the Chart Data identities for the natural-disaster tailored-stress applicability flag; a series bundle, not a bare Python list or per-cell argument.

    Returns:
        The natural-disaster tailored stress applicable (0/1) value read from Chart Data!I17 (debt service-to-revenue MX shock — Market), returned as a float for the numeric indicator or a str when the cell resolves to a text label.
    """
    if not isinstance(inputs, TailoredStressNaturalDisasterApplicableInputs):
        raise TypeError(f"compute_tailored_stress_natural_disaster_applicable() expected TailoredStressNaturalDisasterApplicableInputs, got {type(inputs).__name__}")
    return model.Model(inputs).tailored_stress_natural_disaster_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_37, cells=data.TAILORED_STRESS_COMMODITY_PRICE_APPLICABLE_CELLS)
def compute_tailored_stress_commodity_price_applicable(inputs: TailoredStressCommodityPriceApplicableInputs) -> float | str:
    """Compute the commodity-price tailored stress applicability flag for the LIC-DSF chart data.

    Resolve Chart Data!I18, indicating whether the commodity-price tailored stress test applies to the country's DSA.

    Args:
        inputs: Inputs dataclass of named-axis series over catalog coordinates and scalar parameters supplying the commodity-price tailored stress applicability calculation.

    Returns:
        Commodity-price tailored stress applicable (0/1; 1 excluding 1-year breaches), returned as a float or as a str when the source yields a text value.
    """
    if not isinstance(inputs, TailoredStressCommodityPriceApplicableInputs):
        raise TypeError(f"compute_tailored_stress_commodity_price_applicable() expected TailoredStressCommodityPriceApplicableInputs, got {type(inputs).__name__}")
    return model.Model(inputs).tailored_stress_commodity_price_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_38, cells=data.TAILORED_STRESS_MARKET_FINANCING_APPLICABLE_CELLS)
def compute_tailored_stress_market_financing_applicable(inputs: TailoredStressMarketFinancingApplicableInputs) -> float | str:
    """Compute the market-financing tailored stress applicability signal.

    Determine whether the market-financing tailored stress test applies for the current LIC-DSF scenario.

    Args:
        inputs: Typed inputs dataclass containing the market-financing tailored stress applicability series and scalar inputs.

    Returns:
        Market-financing tailored stress applicable (0/1) as a float or str, corresponding to Chart Data!I19 under Market financing.
    """
    if not isinstance(inputs, TailoredStressMarketFinancingApplicableInputs):
        raise TypeError(f"compute_tailored_stress_market_financing_applicable() expected TailoredStressMarketFinancingApplicableInputs, got {type(inputs).__name__}")
    return model.Model(inputs).tailored_stress_market_financing_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_39, cells=data.FISCAL_SPACE_MODERATE_RISK_SIGNAL_CELLS)
def compute_fiscal_space_moderate_risk_signal(inputs: FiscalSpaceModerateRiskSignalInputs) -> str | int | float | bool:
    """Compute the moderate-risk fiscal-space signal from Chart Data!D23.

    Extracts the moderate-risk category fiscal-space text signal used in the LIC-DSF Chart Data risk-rating surface.

    Args:
        inputs: Dataclass of named-axis series over catalog coordinates supplying the workbook inputs required for the moderate-risk fiscal-space signal calculation.

    Returns:
        Scalar moderate-risk fiscal-space signal from Chart Data!D23, expressed as a string, integer, float, or boolean depending on the workbook value.
    """
    if not isinstance(inputs, FiscalSpaceModerateRiskSignalInputs):
        raise TypeError(f"compute_fiscal_space_moderate_risk_signal() expected FiscalSpaceModerateRiskSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_space_moderate_risk_signal


@publish(key=(), domain=None, constants=_CONSTANTS_40, cells=data.OVERALL_RISK_RATING_SIGNAL_CELLS)
def compute_overall_risk_rating_signal(inputs: OverallRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute the overall combined risk-rating signal for the LIC-DSF DSA.

    Evaluate the external-plus-fiscal overall rating signal from the supplied input dataclass.

    Args:
        inputs: Input dataclass of typed data.* series over catalog coordinates supplying the external and fiscal risk-rating components used to compute the combined overall rating signal.

    Returns:
        The overall combined risk-rating signal (Chart Data!L10) as a scalar str, int, float, or bool.
    """
    if not isinstance(inputs, OverallRiskRatingSignalInputs):
        raise TypeError(f"compute_overall_risk_rating_signal() expected OverallRiskRatingSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).overall_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_41, cells=data.OVERALL_RISK_RATING_NUMERIC_CELLS)
def compute_overall_risk_rating_numeric(inputs: OverallRiskRatingNumericInputs) -> float | str:
    """Compute the overall combined risk-rating numeric code from the provided inputs.

    Derive the Chart Data!L11 overall rating signal from external and fiscal risk-rating inputs.

    Args:
        inputs: Typed `OverallRiskRatingNumericInputs` dataclass of named-axis `data.*` series over catalog coordinates, providing the external and fiscal risk-rating signals needed to compute the overall combined numeric code.

    Returns:
        Overall combined risk-rating numeric code (Chart Data!L11), returned as a float when numeric or as a str signal for the external risk rating when the workbook value is textual.
    """
    if not isinstance(inputs, OverallRiskRatingNumericInputs):
        raise TypeError(f"compute_overall_risk_rating_numeric() expected OverallRiskRatingNumericInputs, got {type(inputs).__name__}")
    return model.Model(inputs).overall_risk_rating_numeric


@publish(data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_GDP_RATIO_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_35, cells=data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_GDP_RATIO_PV_DEBT_TO_GDP.cells)
def compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp(inputs: ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs) -> data.ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdp:
    """Compute the Chart Data PV of Debt-to-GDP Ratio series using authored coordinate identities.

    Produce the scenario-keyed PV of Debt-to-GDP ratio row series for the public-debt stress block.

    Args:
        inputs: Typed input bundle carrying the scenario-keyed inputs required to evaluate the Chart Data PV of Debt-to-GDP Ratio series.

    Returns:
        A data.ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdp series containing the PV of Debt-to-GDP Ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs):
        raise TypeError(f"compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp() expected ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp


@publish(data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_REVENUE_RATIO_PV_DEBT_TO_REVENUE.schema, constants=_CONSTANTS_42, cells=data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_REVENUE_RATIO_PV_DEBT_TO_REVENUE.cells)
def compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue(inputs: ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs) -> data.ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenue:
    """Compute the Chart Data PV of debt-to-revenue ratio series keyed by scenario.

    Derives the chart's PV of debt-to-revenue path from authored coordinate identities for downstream stress-chart output.

    Args:
        inputs: Typed inputs dataclass `ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs` bundling the keyword-only series and scalars (scenario ladder and projection-year coordinates) required to evaluate the PV of debt-to-revenue ratio.

    Returns:
        A `data.ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenue` named-axis series of PV of debt-to-revenue ratios over catalog coordinates, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs):
        raise TypeError(f"compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue() expected ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue


@publish(data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_REVENUE_RATIO_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_43, cells=data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_REVENUE_RATIO_DEBT_SERVICE_TO_REVENUE.cells)
def compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue(inputs: ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs) -> data.ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenue:
    """Compute the Chart Data Debt Service-to-Revenue Ratio series using authored coordinate identities.

    Calculate the scenario-keyed Debt Service-to-Revenue Ratio chart output from the supplied coordinate inputs.

    Args:
        inputs: A ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs instance providing the coordinate and scenario inputs required for the Debt Service-to-Revenue Ratio chart-data computation.

    Returns:
        A data.ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenue series giving the Debt Service-to-Revenue Ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs):
        raise TypeError(f"compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue() expected ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue


@publish(data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_GDP_RATIO_DEBT_SERVICE_GDP_RATIO.schema, constants=_CONSTANTS_43, cells=data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_GDP_RATIO_DEBT_SERVICE_GDP_RATIO.cells)
def compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio(inputs: ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs) -> data.ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatio:
    """Compute the Chart Data Debt Service-to-GDP Ratio series keyed by scenario.

    Produces the public-debt chart series used in the LIC-DSF stress ladder for the Debt Service-to-GDP Ratio metric.

    Args:
        inputs: Typed input payload of scenario-keyed chart-data assumptions and model coordinates required for the Debt Service-to-GDP Ratio computation.

    Returns:
        A data.ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatio typed series containing Debt Service-to-GDP Ratio values on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs):
        raise TypeError(f"compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio() expected ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio


@publish(data.CHART_PV_DEBT_GDP_RATIO_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_44, cells=data.CHART_PV_DEBT_GDP_RATIO_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_pv_debt_gdp_ratio_custom_alternative_scenario(inputs: ChartPvDebtGdpRatioCustomAlternativeScenarioInputs) -> data.ChartPvDebtGdpRatioCustomAlternativeScenario:
    """Compute the customized A2 alternative-scenario PV of debt-to-GDP ratio series from Chart Data.

    Resolve the public-debt stress ladder entry for the customized A2 scenario as a typed Chart Data output series.

    Args:
        inputs: A ChartPvDebtGdpRatioCustomAlternativeScenarioInputs dataclass carrying the scalar and data.* series assumptions needed to evaluate the customized A2 alternative-scenario identity.

    Returns:
        A typed data.ChartPvDebtGdpRatioCustomAlternativeScenario series containing the PV of debt-to-GDP ratio for the customized A2 alternative scenario across the Chart Data projection years.
    """
    if not isinstance(inputs, ChartPvDebtGdpRatioCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_pv_debt_gdp_ratio_custom_alternative_scenario() expected ChartPvDebtGdpRatioCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_pv_debt_gdp_ratio_custom_alternative_scenario


@publish(data.CHART_OUTPUT_PV_DEBT_GDP_RATIO.schema, constants=_CONSTANTS_45, cells=data.CHART_OUTPUT_PV_DEBT_GDP_RATIO.cells)
def compute_chart_output_pv_debt_gdp_ratio(inputs: ChartOutputPvDebtGdpRatioInputs) -> data.ChartOutputPvDebtGdpRatio:
    """Compute the Chart Data PV of debt-to-GDP ratio series by scenario.

    Produce the public PV of debt-to-GDP ratio output used by the LIC-DSF Chart Data stress-chart ladder.

    Args:
        inputs: Typed input bundle containing the scenario and macro-financing assumptions required to evaluate the PV of debt-to-GDP ratio chart series.

    Returns:
        A data.ChartOutputPvDebtGdpRatio series holding the PV of debt-to-GDP ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputPvDebtGdpRatioInputs):
        raise TypeError(f"compute_chart_output_pv_debt_gdp_ratio() expected ChartOutputPvDebtGdpRatioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_pv_debt_gdp_ratio


@publish(data.CHART_PV_DEBT_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_44, cells=data.CHART_PV_DEBT_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_pv_debt_to_exports_custom_alternative_scenario(inputs: ChartPvDebtToExportsCustomAlternativeScenarioInputs) -> data.ChartPvDebtToExportsCustomAlternativeScenario:
    """Compute the customized alternative scenario (A2) PV of debt-to-exports ratio chart series.

    Extracts the PV of debt-to-exports ratio for the customized alternative scenario from Chart Data row 93.

    Args:
        inputs: The inputs container providing the scenario assumptions and projection years needed to compute the customized alternative scenario (A2) PV of debt-to-exports ratio series.

    Returns:
        A data.ChartPvDebtToExportsCustomAlternativeScenario typed series containing the PV of debt-to-exports ratio for the customized alternative scenario over the projection years.
    """
    if not isinstance(inputs, ChartPvDebtToExportsCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_pv_debt_to_exports_custom_alternative_scenario() expected ChartPvDebtToExportsCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_pv_debt_to_exports_custom_alternative_scenario


@publish(data.CHART_OUTPUT_PV_DEBT_TO_EXPORTS.schema, constants=_CONSTANTS_30, cells=data.CHART_OUTPUT_PV_DEBT_TO_EXPORTS.cells)
def compute_chart_output_pv_debt_to_exports(inputs: ChartOutputPvDebtToExportsInputs) -> data.ChartOutputPvDebtToExports:
    """Computes the Chart Data series for the present value of the debt-to-exports ratio.

    Evaluates the authored coordinate identities that produce the PV of debt-to-exports ratio used in LIC-DSF chart output.

    Args:
        inputs: A typed inputs dataclass containing the named-axis series and scalar settings needed to resolve the PV of debt-to-exports ratio across the Chart Data projection coordinates.

    Returns:
        A data.ChartOutputPvDebtToExports series giving the PV of debt-to-exports ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputPvDebtToExportsInputs):
        raise TypeError(f"compute_chart_output_pv_debt_to_exports() expected ChartOutputPvDebtToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_pv_debt_to_exports


@publish(data.CHART_DEBT_SERVICE_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_46, cells=data.CHART_DEBT_SERVICE_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_debt_service_to_exports_custom_alternative_scenario(inputs: ChartDebtServiceToExportsCustomAlternativeScenarioInputs) -> data.ChartDebtServiceToExportsCustomAlternativeScenario:
    """Compute the Debt service-to-exports ratio series for the A2 alternative (customized) scenario from Chart Data row 135.

    Project the customized-scenario debt service-to-exports path over the workbook year grid so it can drive the corresponding stress chart.

    Args:
        inputs: Inputs dataclass carrying the scenario and customization settings required to evaluate the Chart Data debt service-to-exports alternative-scenario series.

    Returns:
        A `data.ChartDebtServiceToExportsCustomAlternativeScenario` named-axis series of debt service-to-exports ratios over the projection years taken from the row 35 headers.
    """
    if not isinstance(inputs, ChartDebtServiceToExportsCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_debt_service_to_exports_custom_alternative_scenario() expected ChartDebtServiceToExportsCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_debt_service_to_exports_custom_alternative_scenario


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_EXPORTS.schema, constants=_CONSTANTS_31, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_EXPORTS.cells)
def compute_chart_output_debt_service_to_exports(inputs: ChartOutputDebtServiceToExportsInputs) -> data.ChartOutputDebtServiceToExports:
    """Compute the debt service-to-exports ratio chart output from the supplied chart input bundle.

    Produce the scenario-keyed Chart Data series for the debt service-to-exports ratio.

    Args:
        inputs: Typed input dataclass carrying the modeled chart-output specification and source data needed for the debt service-to-exports ratio computation.

    Returns:
        Typed data.ChartOutputDebtServiceToExports series containing the debt service-to-exports ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputDebtServiceToExportsInputs):
        raise TypeError(f"compute_chart_output_debt_service_to_exports() expected ChartOutputDebtServiceToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_debt_service_to_exports


@publish(data.CHART_DEBT_SERVICE_TO_REVENUE_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_46, cells=data.CHART_DEBT_SERVICE_TO_REVENUE_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_debt_service_to_revenue_custom_alternative_scenario(inputs: ChartDebtServiceToRevenueCustomAlternativeScenarioInputs) -> data.ChartDebtServiceToRevenueCustomAlternativeScenario:
    """Compute the customized alternative-scenario debt service-to-revenue ratio chart series.

    Populates the A2 Alternative Scenario debt service-to-revenue ratio row used by the LIC-DSF chart data.

    Args:
        inputs: Dataclass of customized alternative-scenario assumption series and scalars aligned to catalog coordinates, supplying the inputs needed for the debt service-to-revenue ratio calculation.

    Returns:
        Typed data series of debt service-to-revenue ratios for the customized alternative scenario, indexed by projection years on the Chart Data row 177 grid.
    """
    if not isinstance(inputs, ChartDebtServiceToRevenueCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_debt_service_to_revenue_custom_alternative_scenario() expected ChartDebtServiceToRevenueCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_debt_service_to_revenue_custom_alternative_scenario


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_32, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE.cells)
def compute_chart_output_debt_service_to_revenue(inputs: ChartOutputDebtServiceToRevenueInputs) -> data.ChartOutputDebtServiceToRevenue:
    """Compute the Chart Data debt service-to-revenue ratio output.

    Derive the scenario-keyed debt service-to-revenue series from the supplied chart output input bundle.

    Args:
        inputs: Input bundle containing the scenario-keyed source series used to compute the debt service-to-revenue chart output.

    Returns:
        A data.ChartOutputDebtServiceToRevenue series containing the debt service-to-revenue ratio on Chart Data, keyed by scenario.
    """
    if not isinstance(inputs, ChartOutputDebtServiceToRevenueInputs):
        raise TypeError(f"compute_chart_output_debt_service_to_revenue() expected ChartOutputDebtServiceToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_debt_service_to_revenue


@publish(data.CHART_OUTPUT_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_35, cells=data.CHART_OUTPUT_PV_DEBT_TO_GDP.cells)
def compute_chart_output_pv_debt_to_gdp(inputs: ChartOutputPvDebtToGdpInputs) -> data.ChartOutputPvDebtToGdp:
    """Compute the Chart Data PV of Debt-to-GDP ratio series, keyed by scenario.

    Evaluates the public-debt stress ladder's PV of Debt-to-GDP metric from the supplied inputs.

    Args:
        inputs: Keyword-only typed input dataclass carrying the series and scalars required to compute the PV of Debt-to-GDP ratio: the public-debt stress-block drivers and macro/financing projections over the Chart Data year grid, with the scenario axis identifying each baseline, standardized-shock, tailored-shock, and customized-scenario path.

    Returns:
        A data.ChartOutputPvDebtToGdp series (PV of Debt-to-GDP Ratio on Chart Data) of scenario-keyed debt-to-GDP present-value values over the projection year grid.
    """
    if not isinstance(inputs, ChartOutputPvDebtToGdpInputs):
        raise TypeError(f"compute_chart_output_pv_debt_to_gdp() expected ChartOutputPvDebtToGdpInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_pv_debt_to_gdp


@publish(data.CHART_PV_DEBT_TO_REVENUE_MX_SHOCK_STANDARD_TAILORED.schema, constants=_CONSTANTS_42, cells=data.CHART_PV_DEBT_TO_REVENUE_MX_SHOCK_STANDARD_TAILORED.cells)
def compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored(inputs: ChartPvDebtToRevenueMxShockStandardTailoredInputs) -> data.ChartPvDebtToRevenueMxShockStandardTailored:
    """Compute the Chart Data series for the PV of the Debt-to-Revenue Ratio under the MX shock Standard & Tailored treatment.

    Produce the row-306 public-debt stress-chart series over the projection year grid from the supplied input bundle.

    Args:
        inputs: Typed input dataclass bundling the named-axis data.* series and scalar options that identify the debt-to-revenue PV shock path to evaluate.

    Returns:
        A data.ChartPvDebtToRevenueMxShockStandardTailored series holding the PV of Debt-to-Revenue Ratio under the MX shock Standard & Tailored scenario, indexed over the Chart Data projection-year coordinates.
    """
    if not isinstance(inputs, ChartPvDebtToRevenueMxShockStandardTailoredInputs):
        raise TypeError(f"compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored() expected ChartPvDebtToRevenueMxShockStandardTailoredInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_pv_debt_to_revenue_mx_shock_standard_tailored


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE_FISCAL.schema, constants=_CONSTANTS_43, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE_FISCAL.cells)
def compute_chart_output_debt_service_to_revenue_fiscal(inputs: ChartOutputDebtServiceToRevenueFiscalInputs) -> data.ChartOutputDebtServiceToRevenueFiscal:
    """Compute the fiscal debt service-to-revenue ratio chart output series from authored coordinate identities.

    Produces the Chart Data series used to report the fiscal debt service-to-revenue ratio across scenarios.

    Args:
        inputs: Typed calculation inputs for the fiscal debt service-to-revenue chart output, containing the scenario-keyed assumptions and workbook coordinates required by the model.

    Returns:
        A data.ChartOutputDebtServiceToRevenueFiscal series of Debt Service-to-Revenue Ratio on Chart Data, keyed by scenario.
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
