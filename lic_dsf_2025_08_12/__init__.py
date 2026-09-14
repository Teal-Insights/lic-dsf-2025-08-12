"""Inverted-tree mechanical extraction."""

from __future__ import annotations

from . import data
from .runtime import as_records

from .api import compute_external_dsa_risk_rating_signal, compute_external_dsa_risk_rating_numeric, compute_external_baseline_breach, compute_external_shock_breach, compute_external_pv_debt_to_gdp_mx_shock, compute_external_pv_debt_to_exports_mx_shock, compute_external_debt_service_to_exports_mx_shock, compute_external_debt_service_to_revenue_mx_shock, compute_fiscal_risk_rating_signal, compute_fiscal_risk_rating_numeric, compute_fiscal_baseline_breach, compute_fiscal_shock_breach, compute_fiscal_pv_debt_to_gdp_mx_shock, compute_tailored_stress_natural_disaster_applicable, compute_tailored_stress_commodity_price_applicable, compute_tailored_stress_market_financing_applicable, compute_fiscal_space_moderate_risk_signal, compute_overall_risk_rating_signal, compute_overall_risk_rating_numeric, compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp, compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue, compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue, compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio, compute_chart_pv_debt_gdp_ratio_a2_alternative_scenario_customize_enter, compute_chart_output_chart_data_figure_r61_pv_debt_gdp_ratio, compute_chart_pv_debt_to_exports_a2_alternative_scenario_customize_enter, compute_chart_output_chart_data_figure_r103_pv_debt_to_exports, compute_chart_debt_service_to_exports_a2_alternative_scenario_customize_enter, compute_chart_output_chart_data_figure_r145_debt_service_to_exports, compute_chart_debt_service_to_revenue_a2_alternative_scenario_customize_enter, compute_chart_output_chart_data_figure_r187_debt_service_to_revenue, compute_chart_output_chart_data_figure_r263_pv_debt_to_gdp, compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored, compute_chart_output_chart_data_figure_r341_debt_service_to_revenue

__all__ = [
    'as_records',
    'data',
    'compute_external_dsa_risk_rating_signal',
    'compute_external_dsa_risk_rating_numeric',
    'compute_external_baseline_breach',
    'compute_external_shock_breach',
    'compute_external_pv_debt_to_gdp_mx_shock',
    'compute_external_pv_debt_to_exports_mx_shock',
    'compute_external_debt_service_to_exports_mx_shock',
    'compute_external_debt_service_to_revenue_mx_shock',
    'compute_fiscal_risk_rating_signal',
    'compute_fiscal_risk_rating_numeric',
    'compute_fiscal_baseline_breach',
    'compute_fiscal_shock_breach',
    'compute_fiscal_pv_debt_to_gdp_mx_shock',
    'compute_tailored_stress_natural_disaster_applicable',
    'compute_tailored_stress_commodity_price_applicable',
    'compute_tailored_stress_market_financing_applicable',
    'compute_fiscal_space_moderate_risk_signal',
    'compute_overall_risk_rating_signal',
    'compute_overall_risk_rating_numeric',
    'compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp',
    'compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue',
    'compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue',
    'compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio',
    'compute_chart_pv_debt_gdp_ratio_a2_alternative_scenario_customize_enter',
    'compute_chart_output_chart_data_figure_r61_pv_debt_gdp_ratio',
    'compute_chart_pv_debt_to_exports_a2_alternative_scenario_customize_enter',
    'compute_chart_output_chart_data_figure_r103_pv_debt_to_exports',
    'compute_chart_debt_service_to_exports_a2_alternative_scenario_customize_enter',
    'compute_chart_output_chart_data_figure_r145_debt_service_to_exports',
    'compute_chart_debt_service_to_revenue_a2_alternative_scenario_customize_enter',
    'compute_chart_output_chart_data_figure_r187_debt_service_to_revenue',
    'compute_chart_output_chart_data_figure_r263_pv_debt_to_gdp',
    'compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored',
    'compute_chart_output_chart_data_figure_r341_debt_service_to_revenue',
]

from .tensor import Axis, Domain, Tensor, TensorSchema
__all__ += ['Axis', 'Domain', 'Tensor', 'TensorSchema']
