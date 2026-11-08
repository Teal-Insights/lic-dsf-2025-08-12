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
    """Compute `realism1_external_debt_flow_components` using authored coordinate identities."""
    if not isinstance(inputs, Realism1ExternalDebtFlowComponentsInputs):
        raise TypeError(f"compute_realism1_external_debt_flow_components() expected Realism1ExternalDebtFlowComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_debt_flow_components


@publish(data.REALISM1_EXTERNAL_DEBT_CREATING_FLOWS.schema, constants=_CONSTANTS_1, cells=data.REALISM1_EXTERNAL_DEBT_CREATING_FLOWS.cells)
def compute_realism1_external_debt_creating_flows(inputs: Realism1ExternalDebtCreatingFlowsInputs) -> data.Realism1ExternalDebtCreatingFlows:
    """Compute `realism1_external_debt_creating_flows` using authored coordinate identities."""
    if not isinstance(inputs, Realism1ExternalDebtCreatingFlowsInputs):
        raise TypeError(f"compute_realism1_external_debt_creating_flows() expected Realism1ExternalDebtCreatingFlowsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_debt_creating_flows


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENT_LABELS.schema, constants=_CONSTANTS_0, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENT_LABELS.cells)
def compute_realism1_external_forecast_error_component_labels(inputs: Realism1ExternalForecastErrorComponentLabelsInputs) -> data.Realism1ExternalForecastErrorComponentLabels:
    """Compute `realism1_external_forecast_error_component_labels` using authored coordinate identities."""
    if not isinstance(inputs, Realism1ExternalForecastErrorComponentLabelsInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_component_labels() expected Realism1ExternalForecastErrorComponentLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_component_labels


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENTS.schema, constants=_CONSTANTS_2, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_COMPONENTS.cells)
def compute_realism1_external_forecast_error_components(inputs: Realism1ExternalForecastErrorComponentsInputs) -> data.Realism1ExternalForecastErrorComponents:
    """Compute `realism1_external_forecast_error_components` using authored coordinate identities."""
    if not isinstance(inputs, Realism1ExternalForecastErrorComponentsInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_components() expected Realism1ExternalForecastErrorComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_components


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION_LABELS.schema, constants=_CONSTANTS_3, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION_LABELS.cells)
def compute_realism1_external_forecast_error_distribution_labels(inputs: Realism1ExternalForecastErrorDistributionLabelsInputs) -> data.Realism1ExternalForecastErrorDistributionLabels:
    """Compute `realism1_external_forecast_error_distribution_labels` using authored coordinate identities."""
    if not isinstance(inputs, Realism1ExternalForecastErrorDistributionLabelsInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_distribution_labels() expected Realism1ExternalForecastErrorDistributionLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_distribution_labels


@publish(data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION.schema, constants=_CONSTANTS_4, cells=data.REALISM1_EXTERNAL_FORECAST_ERROR_DISTRIBUTION.cells)
def compute_realism1_external_forecast_error_distribution(inputs: Realism1ExternalForecastErrorDistributionInputs) -> data.Realism1ExternalForecastErrorDistribution:
    """Compute `realism1_external_forecast_error_distribution` using authored coordinate identities."""
    if not isinstance(inputs, Realism1ExternalForecastErrorDistributionInputs):
        raise TypeError(f"compute_realism1_external_forecast_error_distribution() expected Realism1ExternalForecastErrorDistributionInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_forecast_error_distribution


@publish(data.REALISM1_EXTERNAL_VINTAGE_YEARS.schema, constants=_CONSTANTS_5, cells=data.REALISM1_EXTERNAL_VINTAGE_YEARS.cells)
def compute_realism1_external_vintage_years(inputs: Realism1ExternalVintageYearsInputs) -> data.Realism1ExternalVintageYears:
    """Compute `realism1_external_vintage_years` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism1ExternalVintageYearsInputs):
        raise TypeError(f"compute_realism1_external_vintage_years() expected Realism1ExternalVintageYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_vintage_years


@publish(data.REALISM1_EXTERNAL_VINTAGE_DEBT_PATHS.schema, constants=_CONSTANTS_2, cells=data.REALISM1_EXTERNAL_VINTAGE_DEBT_PATHS.cells)
def compute_realism1_external_vintage_debt_paths(inputs: Realism1ExternalVintageDebtPathsInputs) -> data.Realism1ExternalVintageDebtPaths:
    """Compute `realism1_external_vintage_debt_paths` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism1ExternalVintageDebtPathsInputs):
        raise TypeError(f"compute_realism1_external_vintage_debt_paths() expected Realism1ExternalVintageDebtPathsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_external_vintage_debt_paths


@publish(data.REALISM1_PUBLIC_DEBT_FLOW_COMPONENTS.schema, constants=_CONSTANTS_6, cells=data.REALISM1_PUBLIC_DEBT_FLOW_COMPONENTS.cells)
def compute_realism1_public_debt_flow_components(inputs: Realism1PublicDebtFlowComponentsInputs) -> data.Realism1PublicDebtFlowComponents:
    """Compute `realism1_public_debt_flow_components` using authored coordinate identities."""
    if not isinstance(inputs, Realism1PublicDebtFlowComponentsInputs):
        raise TypeError(f"compute_realism1_public_debt_flow_components() expected Realism1PublicDebtFlowComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_debt_flow_components


@publish(data.REALISM1_PUBLIC_DEBT_CREATING_FLOWS.schema, constants=_CONSTANTS_7, cells=data.REALISM1_PUBLIC_DEBT_CREATING_FLOWS.cells)
def compute_realism1_public_debt_creating_flows(inputs: Realism1PublicDebtCreatingFlowsInputs) -> data.Realism1PublicDebtCreatingFlows:
    """Compute `realism1_public_debt_creating_flows` using authored coordinate identities."""
    if not isinstance(inputs, Realism1PublicDebtCreatingFlowsInputs):
        raise TypeError(f"compute_realism1_public_debt_creating_flows() expected Realism1PublicDebtCreatingFlowsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_debt_creating_flows


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENT_LABELS.schema, constants=_CONSTANTS_6, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENT_LABELS.cells)
def compute_realism1_public_forecast_error_component_labels(inputs: Realism1PublicForecastErrorComponentLabelsInputs) -> data.Realism1PublicForecastErrorComponentLabels:
    """Compute `realism1_public_forecast_error_component_labels` using authored coordinate identities."""
    if not isinstance(inputs, Realism1PublicForecastErrorComponentLabelsInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_component_labels() expected Realism1PublicForecastErrorComponentLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_component_labels


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENTS.schema, constants=_CONSTANTS_8, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_COMPONENTS.cells)
def compute_realism1_public_forecast_error_components(inputs: Realism1PublicForecastErrorComponentsInputs) -> data.Realism1PublicForecastErrorComponents:
    """Compute `realism1_public_forecast_error_components` using authored coordinate identities."""
    if not isinstance(inputs, Realism1PublicForecastErrorComponentsInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_components() expected Realism1PublicForecastErrorComponentsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_components


@publish(key=(), domain=None, constants=_CONSTANTS_9, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_LOWER_QUARTILE_CELLS)
def compute_realism1_public_forecast_error_lower_quartile(inputs: Realism1PublicForecastErrorLowerQuartileInputs) -> float | str:
    """Compute `realism1_public_forecast_error_lower_quartile` using authored coordinate identities."""
    if not isinstance(inputs, Realism1PublicForecastErrorLowerQuartileInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_lower_quartile() expected Realism1PublicForecastErrorLowerQuartileInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_lower_quartile


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION_LABELS.schema, constants=_CONSTANTS_10, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION_LABELS.cells)
def compute_realism1_public_forecast_error_distribution_labels(inputs: Realism1PublicForecastErrorDistributionLabelsInputs) -> data.Realism1PublicForecastErrorDistributionLabels:
    """Compute `realism1_public_forecast_error_distribution_labels` using authored coordinate identities."""
    if not isinstance(inputs, Realism1PublicForecastErrorDistributionLabelsInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_distribution_labels() expected Realism1PublicForecastErrorDistributionLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_distribution_labels


@publish(data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION.schema, constants=_CONSTANTS_11, cells=data.REALISM1_PUBLIC_FORECAST_ERROR_DISTRIBUTION.cells)
def compute_realism1_public_forecast_error_distribution(inputs: Realism1PublicForecastErrorDistributionInputs) -> data.Realism1PublicForecastErrorDistribution:
    """Compute `realism1_public_forecast_error_distribution` using authored coordinate identities."""
    if not isinstance(inputs, Realism1PublicForecastErrorDistributionInputs):
        raise TypeError(f"compute_realism1_public_forecast_error_distribution() expected Realism1PublicForecastErrorDistributionInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_forecast_error_distribution


@publish(data.REALISM1_PUBLIC_VINTAGE_YEARS.schema, constants=_CONSTANTS_5, cells=data.REALISM1_PUBLIC_VINTAGE_YEARS.cells)
def compute_realism1_public_vintage_years(inputs: Realism1PublicVintageYearsInputs) -> data.Realism1PublicVintageYears:
    """Compute `realism1_public_vintage_years` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism1PublicVintageYearsInputs):
        raise TypeError(f"compute_realism1_public_vintage_years() expected Realism1PublicVintageYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_vintage_years


@publish(data.REALISM1_PUBLIC_VINTAGE_DEBT_PATHS.schema, constants=_CONSTANTS_8, cells=data.REALISM1_PUBLIC_VINTAGE_DEBT_PATHS.cells)
def compute_realism1_public_vintage_debt_paths(inputs: Realism1PublicVintageDebtPathsInputs) -> data.Realism1PublicVintageDebtPaths:
    """Compute `realism1_public_vintage_debt_paths` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism1PublicVintageDebtPathsInputs):
        raise TypeError(f"compute_realism1_public_vintage_debt_paths() expected Realism1PublicVintageDebtPathsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism1_public_vintage_debt_paths


@publish(data.REALISM2_FISCAL_ADJUSTMENT_MULTIPLIER_LABELS.schema, constants=_CONSTANTS_12, cells=data.REALISM2_FISCAL_ADJUSTMENT_MULTIPLIER_LABELS.cells)
def compute_realism2_fiscal_adjustment_multiplier_labels(inputs: Realism2FiscalAdjustmentMultiplierLabelsInputs) -> data.Realism2FiscalAdjustmentMultiplierLabels:
    """Compute `realism2_fiscal_adjustment_multiplier_labels` using authored coordinate identities."""
    if not isinstance(inputs, Realism2FiscalAdjustmentMultiplierLabelsInputs):
        raise TypeError(f"compute_realism2_fiscal_adjustment_multiplier_labels() expected Realism2FiscalAdjustmentMultiplierLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_fiscal_adjustment_multiplier_labels


@publish(data.REALISM2_UNDERLYING_GROWTH_MULTIPLIER_LABELS.schema, constants=_CONSTANTS_12, cells=data.REALISM2_UNDERLYING_GROWTH_MULTIPLIER_LABELS.cells)
def compute_realism2_underlying_growth_multiplier_labels(inputs: Realism2UnderlyingGrowthMultiplierLabelsInputs) -> data.Realism2UnderlyingGrowthMultiplierLabels:
    """Compute `realism2_underlying_growth_multiplier_labels` using authored coordinate identities."""
    if not isinstance(inputs, Realism2UnderlyingGrowthMultiplierLabelsInputs):
        raise TypeError(f"compute_realism2_underlying_growth_multiplier_labels() expected Realism2UnderlyingGrowthMultiplierLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_underlying_growth_multiplier_labels


@publish(data.REALISM2_FISCAL_ADJUSTMENT_YEARS.schema, constants=_CONSTANTS_5, cells=data.REALISM2_FISCAL_ADJUSTMENT_YEARS.cells)
def compute_realism2_fiscal_adjustment_years(inputs: Realism2FiscalAdjustmentYearsInputs) -> data.Realism2FiscalAdjustmentYears:
    """Compute `realism2_fiscal_adjustment_years` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentYearsInputs):
        raise TypeError(f"compute_realism2_fiscal_adjustment_years() expected Realism2FiscalAdjustmentYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_fiscal_adjustment_years


@publish(data.REALISM2_UNDERLYING_GROWTH_YEARS.schema, constants=_CONSTANTS_5, cells=data.REALISM2_UNDERLYING_GROWTH_YEARS.cells)
def compute_realism2_underlying_growth_years(inputs: Realism2UnderlyingGrowthYearsInputs) -> data.Realism2UnderlyingGrowthYears:
    """Compute `realism2_underlying_growth_years` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthYearsInputs):
        raise TypeError(f"compute_realism2_underlying_growth_years() expected Realism2UnderlyingGrowthYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_underlying_growth_years


@publish(data.REALISM2_BASELINE_GROWTH.schema, constants=_CONSTANTS_5, cells=data.REALISM2_BASELINE_GROWTH.cells)
def compute_realism2_baseline_growth(inputs: Realism2BaselineGrowthInputs) -> data.Realism2BaselineGrowth:
    """Compute `realism2_baseline_growth` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism2BaselineGrowthInputs):
        raise TypeError(f"compute_realism2_baseline_growth() expected Realism2BaselineGrowthInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_baseline_growth


@publish(data.REALISM2_GROWTH_T_MINUS_1.schema, constants=_CONSTANTS_5, cells=data.REALISM2_GROWTH_T_MINUS_1.cells)
def compute_realism2_growth_t_minus_1(inputs: Realism2GrowthTMinus1Inputs) -> data.Realism2GrowthTMinus1:
    """Compute `realism2_growth_t_minus_1` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism2GrowthTMinus1Inputs):
        raise TypeError(f"compute_realism2_growth_t_minus_1() expected Realism2GrowthTMinus1Inputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_growth_t_minus_1


@publish(data.REALISM2_FISCAL_ADJUSTMENT_GROWTH_IMPACT.schema, constants=_CONSTANTS_13, cells=data.REALISM2_FISCAL_ADJUSTMENT_GROWTH_IMPACT.cells)
def compute_realism2_fiscal_adjustment_growth_impact(inputs: Realism2FiscalAdjustmentGrowthImpactInputs) -> data.Realism2FiscalAdjustmentGrowthImpact:
    """Compute `realism2_fiscal_adjustment_growth_impact` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, Realism2FiscalAdjustmentGrowthImpactInputs):
        raise TypeError(f"compute_realism2_fiscal_adjustment_growth_impact() expected Realism2FiscalAdjustmentGrowthImpactInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_fiscal_adjustment_growth_impact


@publish(data.REALISM2_UNDERLYING_GROWTH.schema, constants=_CONSTANTS_13, cells=data.REALISM2_UNDERLYING_GROWTH.cells)
def compute_realism2_underlying_growth(inputs: Realism2UnderlyingGrowthInputs) -> data.Realism2UnderlyingGrowth:
    """Compute `realism2_underlying_growth` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism2UnderlyingGrowthInputs):
        raise TypeError(f"compute_realism2_underlying_growth() expected Realism2UnderlyingGrowthInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism2_underlying_growth


@publish(data.REALISM3_INVESTMENT_YEARS.schema, constants=_CONSTANTS_5, cells=data.REALISM3_INVESTMENT_YEARS.cells)
def compute_realism3_investment_years(inputs: Realism3InvestmentYearsInputs) -> data.Realism3InvestmentYears:
    """Compute `realism3_investment_years` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism3InvestmentYearsInputs):
        raise TypeError(f"compute_realism3_investment_years() expected Realism3InvestmentYearsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_investment_years


@publish(data.REALISM3_INVESTMENT_PATH_LABELS.schema, constants=_CONSTANTS_14, cells=data.REALISM3_INVESTMENT_PATH_LABELS.cells)
def compute_realism3_investment_path_labels(inputs: Realism3InvestmentPathLabelsInputs) -> data.Realism3InvestmentPathLabels:
    """Compute `realism3_investment_path_labels` using authored coordinate identities."""
    if not isinstance(inputs, Realism3InvestmentPathLabelsInputs):
        raise TypeError(f"compute_realism3_investment_path_labels() expected Realism3InvestmentPathLabelsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_investment_path_labels


@publish(data.REALISM3_PUBLIC_PRIVATE_INVESTMENT_PATHS.schema, constants=_CONSTANTS_15, cells=data.REALISM3_PUBLIC_PRIVATE_INVESTMENT_PATHS.cells)
def compute_realism3_public_private_investment_paths(inputs: Realism3PublicPrivateInvestmentPathsInputs) -> data.Realism3PublicPrivateInvestmentPaths:
    """Compute `realism3_public_private_investment_paths` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_input_3_macro_current_account`.
    """
    if not isinstance(inputs, Realism3PublicPrivateInvestmentPathsInputs):
        raise TypeError(f"compute_realism3_public_private_investment_paths() expected Realism3PublicPrivateInvestmentPathsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_public_private_investment_paths


@publish(data.REALISM3_GROWTH_ACCOUNTING_VINTAGES.schema, constants=_CONSTANTS_16, cells=data.REALISM3_GROWTH_ACCOUNTING_VINTAGES.cells)
def compute_realism3_growth_accounting_vintages(inputs: Realism3GrowthAccountingVintagesInputs) -> data.Realism3GrowthAccountingVintages:
    """Compute `realism3_growth_accounting_vintages` using authored coordinate identities."""
    if not isinstance(inputs, Realism3GrowthAccountingVintagesInputs):
        raise TypeError(f"compute_realism3_growth_accounting_vintages() expected Realism3GrowthAccountingVintagesInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_growth_accounting_vintages


@publish(data.REALISM3_GROWTH_ACCOUNTING_CONTRIBUTIONS.schema, constants=_CONSTANTS_17, cells=data.REALISM3_GROWTH_ACCOUNTING_CONTRIBUTIONS.cells)
def compute_realism3_growth_accounting_contributions(inputs: Realism3GrowthAccountingContributionsInputs) -> data.Realism3GrowthAccountingContributions:
    """Compute `realism3_growth_accounting_contributions` using authored coordinate identities."""
    if not isinstance(inputs, Realism3GrowthAccountingContributionsInputs):
        raise TypeError(f"compute_realism3_growth_accounting_contributions() expected Realism3GrowthAccountingContributionsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism3_growth_accounting_contributions


@publish(key=(), domain=None, constants=_CONSTANTS_18, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_LABEL_CELLS)
def compute_realism4_projected_3yr_adjustment_label(inputs: Realism4Projected3yrAdjustmentLabelInputs) -> str | int | float | bool:
    """Compute `realism4_projected_3yr_adjustment_label` using authored coordinate identities."""
    if not isinstance(inputs, Realism4Projected3yrAdjustmentLabelInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_label() expected Realism4Projected3yrAdjustmentLabelInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_label


@publish(key=(), domain=None, constants=_CONSTANTS_5, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_CELLS)
def compute_realism4_projected_3yr_adjustment(inputs: Realism4Projected3yrAdjustmentInputs) -> float | str:
    """Compute `realism4_projected_3yr_adjustment` using authored coordinate identities."""
    if not isinstance(inputs, Realism4Projected3yrAdjustmentInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment() expected Realism4Projected3yrAdjustmentInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment


@publish(key=(), domain=None, constants=_CONSTANTS_5, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_BIN_CELLS)
def compute_realism4_projected_3yr_adjustment_bin(inputs: Realism4Projected3yrAdjustmentBinInputs) -> float | str:
    """Compute `realism4_projected_3yr_adjustment_bin` using authored coordinate identities."""
    if not isinstance(inputs, Realism4Projected3yrAdjustmentBinInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_bin() expected Realism4Projected3yrAdjustmentBinInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_bin


@publish(key=(), domain=None, constants=_CONSTANTS_19, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_CATEGORY_CELLS)
def compute_realism4_projected_3yr_adjustment_category(inputs: Realism4Projected3yrAdjustmentCategoryInputs) -> float | str:
    """Compute `realism4_projected_3yr_adjustment_category` using authored coordinate identities."""
    if not isinstance(inputs, Realism4Projected3yrAdjustmentCategoryInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_category() expected Realism4Projected3yrAdjustmentCategoryInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_category


@publish(key=(), domain=None, constants=_CONSTANTS_19, cells=data.REALISM4_PROJECTED_3YR_ADJUSTMENT_SAMPLE_SHARE_CELLS)
def compute_realism4_projected_3yr_adjustment_sample_share(inputs: Realism4Projected3yrAdjustmentSampleShareInputs) -> float | str:
    """Compute `realism4_projected_3yr_adjustment_sample_share` using authored coordinate identities."""
    if not isinstance(inputs, Realism4Projected3yrAdjustmentSampleShareInputs):
        raise TypeError(f"compute_realism4_projected_3yr_adjustment_sample_share() expected Realism4Projected3yrAdjustmentSampleShareInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_projected_3yr_adjustment_sample_share


@publish(key=(), domain=None, constants=_CONSTANTS_20, cells=data.REALISM4_FISCAL_ADJUSTMENT_TOP_BIN_LABEL_CELLS)
def compute_realism4_fiscal_adjustment_top_bin_label(inputs: Realism4FiscalAdjustmentTopBinLabelInputs) -> str | int | float | bool:
    """Compute `realism4_fiscal_adjustment_top_bin_label` using authored coordinate identities."""
    if not isinstance(inputs, Realism4FiscalAdjustmentTopBinLabelInputs):
        raise TypeError(f"compute_realism4_fiscal_adjustment_top_bin_label() expected Realism4FiscalAdjustmentTopBinLabelInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_fiscal_adjustment_top_bin_label


@publish(data.REALISM4_FISCAL_ADJUSTMENT_SAMPLE_SHARE.schema, constants=_CONSTANTS_21, cells=data.REALISM4_FISCAL_ADJUSTMENT_SAMPLE_SHARE.cells)
def compute_realism4_fiscal_adjustment_sample_share(inputs: Realism4FiscalAdjustmentSampleShareInputs) -> data.Realism4FiscalAdjustmentSampleShare:
    """Compute `realism4_fiscal_adjustment_sample_share` using authored coordinate identities."""
    if not isinstance(inputs, Realism4FiscalAdjustmentSampleShareInputs):
        raise TypeError(f"compute_realism4_fiscal_adjustment_sample_share() expected Realism4FiscalAdjustmentSampleShareInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_fiscal_adjustment_sample_share


@publish(data.REALISM4_FISCAL_ADJUSTMENT_CUMULATIVE_SHARE.schema, constants=_CONSTANTS_21, cells=data.REALISM4_FISCAL_ADJUSTMENT_CUMULATIVE_SHARE.cells)
def compute_realism4_fiscal_adjustment_cumulative_share(inputs: Realism4FiscalAdjustmentCumulativeShareInputs) -> data.Realism4FiscalAdjustmentCumulativeShare:
    """Compute `realism4_fiscal_adjustment_cumulative_share` using authored coordinate identities."""
    if not isinstance(inputs, Realism4FiscalAdjustmentCumulativeShareInputs):
        raise TypeError(f"compute_realism4_fiscal_adjustment_cumulative_share() expected Realism4FiscalAdjustmentCumulativeShareInputs, got {type(inputs).__name__}")
    return model.Model(inputs).realism4_fiscal_adjustment_cumulative_share


@publish(data.PROBABILITY_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_22, cells=data.PROBABILITY_PV_DEBT_TO_GDP.cells)
def compute_probability_pv_debt_to_gdp(inputs: ProbabilityPvDebtToGdpInputs) -> data.ProbabilityPvDebtToGdp:
    """Compute `probability_pv_debt_to_gdp` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ProbabilityPvDebtToGdpInputs):
        raise TypeError(f"compute_probability_pv_debt_to_gdp() expected ProbabilityPvDebtToGdpInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_gdp


@publish(data.PROBABILITY_PV_DEBT_TO_EXPORTS.schema, constants=_CONSTANTS_23, cells=data.PROBABILITY_PV_DEBT_TO_EXPORTS.cells)
def compute_probability_pv_debt_to_exports(inputs: ProbabilityPvDebtToExportsInputs) -> data.ProbabilityPvDebtToExports:
    """Compute `probability_pv_debt_to_exports` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ProbabilityPvDebtToExportsInputs):
        raise TypeError(f"compute_probability_pv_debt_to_exports() expected ProbabilityPvDebtToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_exports


@publish(data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS.schema, constants=_CONSTANTS_24, cells=data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS.cells)
def compute_probability_debt_service_to_exports(inputs: ProbabilityDebtServiceToExportsInputs) -> data.ProbabilityDebtServiceToExports:
    """Compute `probability_debt_service_to_exports` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToExportsInputs):
        raise TypeError(f"compute_probability_debt_service_to_exports() expected ProbabilityDebtServiceToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_exports


@publish(data.PROBABILITY_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_25, cells=data.PROBABILITY_DEBT_SERVICE_TO_REVENUE.cells)
def compute_probability_debt_service_to_revenue(inputs: ProbabilityDebtServiceToRevenueInputs) -> data.ProbabilityDebtServiceToRevenue:
    """Compute `probability_debt_service_to_revenue` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToRevenueInputs):
        raise TypeError(f"compute_probability_debt_service_to_revenue() expected ProbabilityDebtServiceToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_revenue


@publish(data.PROBABILITY_PV_DEBT_TO_GDP_DISTRESS.schema, constants=_CONSTANTS_26, cells=data.PROBABILITY_PV_DEBT_TO_GDP_DISTRESS.cells)
def compute_probability_pv_debt_to_gdp_distress(inputs: ProbabilityPvDebtToGdpDistressInputs) -> data.ProbabilityPvDebtToGdpDistress:
    """Compute `probability_pv_debt_to_gdp_distress` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ProbabilityPvDebtToGdpDistressInputs):
        raise TypeError(f"compute_probability_pv_debt_to_gdp_distress() expected ProbabilityPvDebtToGdpDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_gdp_distress


@publish(data.PROBABILITY_PV_DEBT_TO_EXPORTS_DISTRESS.schema, constants=_CONSTANTS_27, cells=data.PROBABILITY_PV_DEBT_TO_EXPORTS_DISTRESS.cells)
def compute_probability_pv_debt_to_exports_distress(inputs: ProbabilityPvDebtToExportsDistressInputs) -> data.ProbabilityPvDebtToExportsDistress:
    """Compute `probability_pv_debt_to_exports_distress` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ProbabilityPvDebtToExportsDistressInputs):
        raise TypeError(f"compute_probability_pv_debt_to_exports_distress() expected ProbabilityPvDebtToExportsDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_pv_debt_to_exports_distress


@publish(data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS_DISTRESS.schema, constants=_CONSTANTS_28, cells=data.PROBABILITY_DEBT_SERVICE_TO_EXPORTS_DISTRESS.cells)
def compute_probability_debt_service_to_exports_distress(inputs: ProbabilityDebtServiceToExportsDistressInputs) -> data.ProbabilityDebtServiceToExportsDistress:
    """Compute `probability_debt_service_to_exports_distress` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToExportsDistressInputs):
        raise TypeError(f"compute_probability_debt_service_to_exports_distress() expected ProbabilityDebtServiceToExportsDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_exports_distress


@publish(data.PROBABILITY_DEBT_SERVICE_TO_REVENUE_DISTRESS.schema, constants=_CONSTANTS_29, cells=data.PROBABILITY_DEBT_SERVICE_TO_REVENUE_DISTRESS.cells)
def compute_probability_debt_service_to_revenue_distress(inputs: ProbabilityDebtServiceToRevenueDistressInputs) -> data.ProbabilityDebtServiceToRevenueDistress:
    """Compute `probability_debt_service_to_revenue_distress` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ProbabilityDebtServiceToRevenueDistressInputs):
        raise TypeError(f"compute_probability_debt_service_to_revenue_distress() expected ProbabilityDebtServiceToRevenueDistressInputs, got {type(inputs).__name__}")
    return model.Model(inputs).probability_debt_service_to_revenue_distress


@publish(key=(), domain=None, constants=_CONSTANTS_30, cells=data.EXTERNAL_DSA_RISK_RATING_SIGNAL_CELLS)
def compute_external_dsa_risk_rating_signal(inputs: ExternalDsaRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute `external_dsa_risk_rating_signal` using authored coordinate identities."""
    if not isinstance(inputs, ExternalDsaRiskRatingSignalInputs):
        raise TypeError(f"compute_external_dsa_risk_rating_signal() expected ExternalDsaRiskRatingSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_dsa_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_31, cells=data.EXTERNAL_DSA_RISK_RATING_NUMERIC_CELLS)
def compute_external_dsa_risk_rating_numeric(inputs: ExternalDsaRiskRatingNumericInputs) -> float | str:
    """Compute `external_dsa_risk_rating_numeric` using authored coordinate identities."""
    if not isinstance(inputs, ExternalDsaRiskRatingNumericInputs):
        raise TypeError(f"compute_external_dsa_risk_rating_numeric() expected ExternalDsaRiskRatingNumericInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_dsa_risk_rating_numeric


@publish(key=(), domain=None, constants=_CONSTANTS_31, cells=data.EXTERNAL_BASELINE_BREACH_CELLS)
def compute_external_baseline_breach(inputs: ExternalBaselineBreachInputs) -> float | str:
    """Compute `external_baseline_breach` using authored coordinate identities."""
    if not isinstance(inputs, ExternalBaselineBreachInputs):
        raise TypeError(f"compute_external_baseline_breach() expected ExternalBaselineBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_baseline_breach


@publish(key=(), domain=None, constants=_CONSTANTS_31, cells=data.EXTERNAL_SHOCK_BREACH_CELLS)
def compute_external_shock_breach(inputs: ExternalShockBreachInputs) -> float | str:
    """Compute `external_shock_breach` using authored coordinate identities."""
    if not isinstance(inputs, ExternalShockBreachInputs):
        raise TypeError(f"compute_external_shock_breach() expected ExternalShockBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_shock_breach


@publish(key=(), domain=None, constants=_CONSTANTS_32, cells=data.EXTERNAL_PV_DEBT_TO_GDP_MX_SHOCK_CELLS)
def compute_external_pv_debt_to_gdp_mx_shock(inputs: ExternalPvDebtToGdpMxShockInputs) -> str | int | float | bool:
    """Compute `external_pv_debt_to_gdp_mx_shock` using authored coordinate identities."""
    if not isinstance(inputs, ExternalPvDebtToGdpMxShockInputs):
        raise TypeError(f"compute_external_pv_debt_to_gdp_mx_shock() expected ExternalPvDebtToGdpMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_pv_debt_to_gdp_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_33, cells=data.EXTERNAL_PV_DEBT_TO_EXPORTS_MX_SHOCK_CELLS)
def compute_external_pv_debt_to_exports_mx_shock(inputs: ExternalPvDebtToExportsMxShockInputs) -> str | int | float | bool:
    """Compute `external_pv_debt_to_exports_mx_shock` using authored coordinate identities."""
    if not isinstance(inputs, ExternalPvDebtToExportsMxShockInputs):
        raise TypeError(f"compute_external_pv_debt_to_exports_mx_shock() expected ExternalPvDebtToExportsMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_pv_debt_to_exports_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_34, cells=data.EXTERNAL_DEBT_SERVICE_TO_EXPORTS_MX_SHOCK_CELLS)
def compute_external_debt_service_to_exports_mx_shock(inputs: ExternalDebtServiceToExportsMxShockInputs) -> str | int | float | bool:
    """Compute `external_debt_service_to_exports_mx_shock` using authored coordinate identities."""
    if not isinstance(inputs, ExternalDebtServiceToExportsMxShockInputs):
        raise TypeError(f"compute_external_debt_service_to_exports_mx_shock() expected ExternalDebtServiceToExportsMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_debt_service_to_exports_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_35, cells=data.EXTERNAL_DEBT_SERVICE_TO_REVENUE_MX_SHOCK_CELLS)
def compute_external_debt_service_to_revenue_mx_shock(inputs: ExternalDebtServiceToRevenueMxShockInputs) -> str | int | float | bool:
    """Compute `external_debt_service_to_revenue_mx_shock` using authored coordinate identities."""
    if not isinstance(inputs, ExternalDebtServiceToRevenueMxShockInputs):
        raise TypeError(f"compute_external_debt_service_to_revenue_mx_shock() expected ExternalDebtServiceToRevenueMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).external_debt_service_to_revenue_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_36, cells=data.FISCAL_RISK_RATING_SIGNAL_CELLS)
def compute_fiscal_risk_rating_signal(inputs: FiscalRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute `fiscal_risk_rating_signal` using authored coordinate identities."""
    if not isinstance(inputs, FiscalRiskRatingSignalInputs):
        raise TypeError(f"compute_fiscal_risk_rating_signal() expected FiscalRiskRatingSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_37, cells=data.FISCAL_RISK_RATING_NUMERIC_CELLS)
def compute_fiscal_risk_rating_numeric(inputs: FiscalRiskRatingNumericInputs) -> float | str:
    """Compute `fiscal_risk_rating_numeric` using authored coordinate identities."""
    if not isinstance(inputs, FiscalRiskRatingNumericInputs):
        raise TypeError(f"compute_fiscal_risk_rating_numeric() expected FiscalRiskRatingNumericInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_risk_rating_numeric


@publish(key=(), domain=None, constants=_CONSTANTS_37, cells=data.FISCAL_BASELINE_BREACH_CELLS)
def compute_fiscal_baseline_breach(inputs: FiscalBaselineBreachInputs) -> float | str:
    """Compute `fiscal_baseline_breach` using authored coordinate identities."""
    if not isinstance(inputs, FiscalBaselineBreachInputs):
        raise TypeError(f"compute_fiscal_baseline_breach() expected FiscalBaselineBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_baseline_breach


@publish(key=(), domain=None, constants=_CONSTANTS_37, cells=data.FISCAL_SHOCK_BREACH_CELLS)
def compute_fiscal_shock_breach(inputs: FiscalShockBreachInputs) -> float | str:
    """Compute `fiscal_shock_breach` using authored coordinate identities."""
    if not isinstance(inputs, FiscalShockBreachInputs):
        raise TypeError(f"compute_fiscal_shock_breach() expected FiscalShockBreachInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_shock_breach


@publish(key=(), domain=None, constants=_CONSTANTS_38, cells=data.FISCAL_PV_DEBT_TO_GDP_MX_SHOCK_CELLS)
def compute_fiscal_pv_debt_to_gdp_mx_shock(inputs: FiscalPvDebtToGdpMxShockInputs) -> str | int | float | bool:
    """Compute `fiscal_pv_debt_to_gdp_mx_shock` using authored coordinate identities."""
    if not isinstance(inputs, FiscalPvDebtToGdpMxShockInputs):
        raise TypeError(f"compute_fiscal_pv_debt_to_gdp_mx_shock() expected FiscalPvDebtToGdpMxShockInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_pv_debt_to_gdp_mx_shock


@publish(key=(), domain=None, constants=_CONSTANTS_39, cells=data.TAILORED_STRESS_NATURAL_DISASTER_APPLICABLE_CELLS)
def compute_tailored_stress_natural_disaster_applicable(inputs: TailoredStressNaturalDisasterApplicableInputs) -> float | str:
    """Compute `tailored_stress_natural_disaster_applicable` using authored coordinate identities."""
    if not isinstance(inputs, TailoredStressNaturalDisasterApplicableInputs):
        raise TypeError(f"compute_tailored_stress_natural_disaster_applicable() expected TailoredStressNaturalDisasterApplicableInputs, got {type(inputs).__name__}")
    return model.Model(inputs).tailored_stress_natural_disaster_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_40, cells=data.TAILORED_STRESS_COMMODITY_PRICE_APPLICABLE_CELLS)
def compute_tailored_stress_commodity_price_applicable(inputs: TailoredStressCommodityPriceApplicableInputs) -> float | str:
    """Compute `tailored_stress_commodity_price_applicable` using authored coordinate identities."""
    if not isinstance(inputs, TailoredStressCommodityPriceApplicableInputs):
        raise TypeError(f"compute_tailored_stress_commodity_price_applicable() expected TailoredStressCommodityPriceApplicableInputs, got {type(inputs).__name__}")
    return model.Model(inputs).tailored_stress_commodity_price_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_41, cells=data.TAILORED_STRESS_MARKET_FINANCING_APPLICABLE_CELLS)
def compute_tailored_stress_market_financing_applicable(inputs: TailoredStressMarketFinancingApplicableInputs) -> float | str:
    """Compute `tailored_stress_market_financing_applicable` using authored coordinate identities."""
    if not isinstance(inputs, TailoredStressMarketFinancingApplicableInputs):
        raise TypeError(f"compute_tailored_stress_market_financing_applicable() expected TailoredStressMarketFinancingApplicableInputs, got {type(inputs).__name__}")
    return model.Model(inputs).tailored_stress_market_financing_applicable


@publish(key=(), domain=None, constants=_CONSTANTS_42, cells=data.FISCAL_SPACE_MODERATE_RISK_SIGNAL_CELLS)
def compute_fiscal_space_moderate_risk_signal(inputs: FiscalSpaceModerateRiskSignalInputs) -> str | int | float | bool:
    """Compute `fiscal_space_moderate_risk_signal` using authored coordinate identities."""
    if not isinstance(inputs, FiscalSpaceModerateRiskSignalInputs):
        raise TypeError(f"compute_fiscal_space_moderate_risk_signal() expected FiscalSpaceModerateRiskSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).fiscal_space_moderate_risk_signal


@publish(key=(), domain=None, constants=_CONSTANTS_43, cells=data.OVERALL_RISK_RATING_SIGNAL_CELLS)
def compute_overall_risk_rating_signal(inputs: OverallRiskRatingSignalInputs) -> str | int | float | bool:
    """Compute `overall_risk_rating_signal` using authored coordinate identities."""
    if not isinstance(inputs, OverallRiskRatingSignalInputs):
        raise TypeError(f"compute_overall_risk_rating_signal() expected OverallRiskRatingSignalInputs, got {type(inputs).__name__}")
    return model.Model(inputs).overall_risk_rating_signal


@publish(key=(), domain=None, constants=_CONSTANTS_44, cells=data.OVERALL_RISK_RATING_NUMERIC_CELLS)
def compute_overall_risk_rating_numeric(inputs: OverallRiskRatingNumericInputs) -> float | str:
    """Compute `overall_risk_rating_numeric` using authored coordinate identities."""
    if not isinstance(inputs, OverallRiskRatingNumericInputs):
        raise TypeError(f"compute_overall_risk_rating_numeric() expected OverallRiskRatingNumericInputs, got {type(inputs).__name__}")
    return model.Model(inputs).overall_risk_rating_numeric


@publish(data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_GDP_RATIO_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_45, cells=data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_GDP_RATIO_PV_DEBT_TO_GDP.cells)
def compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp(inputs: ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs) -> data.ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdp:
    """Compute `chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs):
        raise TypeError(f"compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp() expected ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp


@publish(data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_REVENUE_RATIO_PV_DEBT_TO_REVENUE.schema, constants=_CONSTANTS_46, cells=data.CHART_OUTPUT_CHART_DATA_PV_OF_DEBT_TO_REVENUE_RATIO_PV_DEBT_TO_REVENUE.cells)
def compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue(inputs: ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs) -> data.ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenue:
    """Compute `chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs):
        raise TypeError(f"compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue() expected ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue


@publish(data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_REVENUE_RATIO_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_47, cells=data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_REVENUE_RATIO_DEBT_SERVICE_TO_REVENUE.cells)
def compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue(inputs: ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs) -> data.ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenue:
    """Compute `chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs):
        raise TypeError(f"compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue() expected ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue


@publish(data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_GDP_RATIO_DEBT_SERVICE_GDP_RATIO.schema, constants=_CONSTANTS_47, cells=data.CHART_OUTPUT_CHART_DATA_DEBT_SERVICE_TO_GDP_RATIO_DEBT_SERVICE_GDP_RATIO.cells)
def compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio(inputs: ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs) -> data.ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatio:
    """Compute `chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs):
        raise TypeError(f"compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio() expected ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio


@publish(data.CHART_PV_DEBT_GDP_RATIO_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_48, cells=data.CHART_PV_DEBT_GDP_RATIO_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_pv_debt_gdp_ratio_custom_alternative_scenario(inputs: ChartPvDebtGdpRatioCustomAlternativeScenarioInputs) -> data.ChartPvDebtGdpRatioCustomAlternativeScenario:
    """Compute `chart_pv_debt_gdp_ratio_custom_alternative_scenario` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartPvDebtGdpRatioCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_pv_debt_gdp_ratio_custom_alternative_scenario() expected ChartPvDebtGdpRatioCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_pv_debt_gdp_ratio_custom_alternative_scenario


@publish(data.CHART_OUTPUT_PV_DEBT_GDP_RATIO.schema, constants=_CONSTANTS_49, cells=data.CHART_OUTPUT_PV_DEBT_GDP_RATIO.cells)
def compute_chart_output_pv_debt_gdp_ratio(inputs: ChartOutputPvDebtGdpRatioInputs) -> data.ChartOutputPvDebtGdpRatio:
    """Compute `chart_output_pv_debt_gdp_ratio` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartOutputPvDebtGdpRatioInputs):
        raise TypeError(f"compute_chart_output_pv_debt_gdp_ratio() expected ChartOutputPvDebtGdpRatioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_pv_debt_gdp_ratio


@publish(data.CHART_PV_DEBT_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_48, cells=data.CHART_PV_DEBT_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_pv_debt_to_exports_custom_alternative_scenario(inputs: ChartPvDebtToExportsCustomAlternativeScenarioInputs) -> data.ChartPvDebtToExportsCustomAlternativeScenario:
    """Compute `chart_pv_debt_to_exports_custom_alternative_scenario` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartPvDebtToExportsCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_pv_debt_to_exports_custom_alternative_scenario() expected ChartPvDebtToExportsCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_pv_debt_to_exports_custom_alternative_scenario


@publish(data.CHART_OUTPUT_PV_DEBT_TO_EXPORTS.schema, constants=_CONSTANTS_50, cells=data.CHART_OUTPUT_PV_DEBT_TO_EXPORTS.cells)
def compute_chart_output_pv_debt_to_exports(inputs: ChartOutputPvDebtToExportsInputs) -> data.ChartOutputPvDebtToExports:
    """Compute `chart_output_pv_debt_to_exports` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartOutputPvDebtToExportsInputs):
        raise TypeError(f"compute_chart_output_pv_debt_to_exports() expected ChartOutputPvDebtToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_pv_debt_to_exports


@publish(data.CHART_DEBT_SERVICE_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_51, cells=data.CHART_DEBT_SERVICE_TO_EXPORTS_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_debt_service_to_exports_custom_alternative_scenario(inputs: ChartDebtServiceToExportsCustomAlternativeScenarioInputs) -> data.ChartDebtServiceToExportsCustomAlternativeScenario:
    """Compute `chart_debt_service_to_exports_custom_alternative_scenario` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartDebtServiceToExportsCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_debt_service_to_exports_custom_alternative_scenario() expected ChartDebtServiceToExportsCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_debt_service_to_exports_custom_alternative_scenario


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_EXPORTS.schema, constants=_CONSTANTS_52, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_EXPORTS.cells)
def compute_chart_output_debt_service_to_exports(inputs: ChartOutputDebtServiceToExportsInputs) -> data.ChartOutputDebtServiceToExports:
    """Compute `chart_output_debt_service_to_exports` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartOutputDebtServiceToExportsInputs):
        raise TypeError(f"compute_chart_output_debt_service_to_exports() expected ChartOutputDebtServiceToExportsInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_debt_service_to_exports


@publish(data.CHART_DEBT_SERVICE_TO_REVENUE_CUSTOM_ALTERNATIVE_SCENARIO.schema, constants=_CONSTANTS_51, cells=data.CHART_DEBT_SERVICE_TO_REVENUE_CUSTOM_ALTERNATIVE_SCENARIO.cells)
def compute_chart_debt_service_to_revenue_custom_alternative_scenario(inputs: ChartDebtServiceToRevenueCustomAlternativeScenarioInputs) -> data.ChartDebtServiceToRevenueCustomAlternativeScenario:
    """Compute `chart_debt_service_to_revenue_custom_alternative_scenario` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartDebtServiceToRevenueCustomAlternativeScenarioInputs):
        raise TypeError(f"compute_chart_debt_service_to_revenue_custom_alternative_scenario() expected ChartDebtServiceToRevenueCustomAlternativeScenarioInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_debt_service_to_revenue_custom_alternative_scenario


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE.schema, constants=_CONSTANTS_53, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE.cells)
def compute_chart_output_debt_service_to_revenue(inputs: ChartOutputDebtServiceToRevenueInputs) -> data.ChartOutputDebtServiceToRevenue:
    """Compute `chart_output_debt_service_to_revenue` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartOutputDebtServiceToRevenueInputs):
        raise TypeError(f"compute_chart_output_debt_service_to_revenue() expected ChartOutputDebtServiceToRevenueInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_debt_service_to_revenue


@publish(data.CHART_OUTPUT_PV_DEBT_TO_GDP.schema, constants=_CONSTANTS_45, cells=data.CHART_OUTPUT_PV_DEBT_TO_GDP.cells)
def compute_chart_output_pv_debt_to_gdp(inputs: ChartOutputPvDebtToGdpInputs) -> data.ChartOutputPvDebtToGdp:
    """Compute `chart_output_pv_debt_to_gdp` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartOutputPvDebtToGdpInputs):
        raise TypeError(f"compute_chart_output_pv_debt_to_gdp() expected ChartOutputPvDebtToGdpInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_output_pv_debt_to_gdp


@publish(data.CHART_PV_DEBT_TO_REVENUE_MX_SHOCK_STANDARD_TAILORED.schema, constants=_CONSTANTS_46, cells=data.CHART_PV_DEBT_TO_REVENUE_MX_SHOCK_STANDARD_TAILORED.cells)
def compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored(inputs: ChartPvDebtToRevenueMxShockStandardTailoredInputs) -> data.ChartPvDebtToRevenueMxShockStandardTailored:
    """Compute `chart_pv_debt_to_revenue_mx_shock_standard_tailored` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
    """
    if not isinstance(inputs, ChartPvDebtToRevenueMxShockStandardTailoredInputs):
        raise TypeError(f"compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored() expected ChartPvDebtToRevenueMxShockStandardTailoredInputs, got {type(inputs).__name__}")
    return model.Model(inputs).chart_pv_debt_to_revenue_mx_shock_standard_tailored


@publish(data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE_FISCAL.schema, constants=_CONSTANTS_47, cells=data.CHART_OUTPUT_DEBT_SERVICE_TO_REVENUE_FISCAL.cells)
def compute_chart_output_debt_service_to_revenue_fiscal(inputs: ChartOutputDebtServiceToRevenueFiscalInputs) -> data.ChartOutputDebtServiceToRevenueFiscal:
    """Compute `chart_output_debt_service_to_revenue_fiscal` using authored coordinate identities.

    Keys along `TIME_PERIOD` are determined by `input3_old_debt_service`.
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
