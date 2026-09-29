"""Input schema, domain, and value-map checks for bound Model arguments."""

from __future__ import annotations

from typing import Literal

from . import data
from .excel import coerce_input_measure, require_input_domain
from .runtime import require_annotated_domain


def _check_input4_interest_rate(
    input4_interest_rate: data.Input4InterestRate,
) -> data.Input4InterestRate:
    """Validate `input4_interest_rate` before the model reads it."""
    data.INPUT4_INTEREST_RATE.schema.validate(input4_interest_rate)
    input4_interest_rate = coerce_input_measure(input4_interest_rate, dtype="float", series_id="input4_interest_rate")
    for coordinate in data.INPUT4_INTEREST_RATE.required:
        require_input_domain(input4_interest_rate[coordinate], {"real_between": {"min": 0, "max": 1}}, series_id="input4_interest_rate" + repr(coordinate))
    return input4_interest_rate


def _check_input4_grace_period(
    input4_grace_period: data.Input4GracePeriod,
) -> data.Input4GracePeriod:
    """Validate `input4_grace_period` before the model reads it."""
    data.INPUT4_GRACE_PERIOD.schema.validate(input4_grace_period)
    input4_grace_period = coerce_input_measure(input4_grace_period, dtype="int", series_id="input4_grace_period")
    for coordinate in data.INPUT4_GRACE_PERIOD.required:
        require_input_domain(input4_grace_period[coordinate], {"between": {"min": 0, "max": 50}}, series_id="input4_grace_period" + repr(coordinate))
    return input4_grace_period


def _check_input4_loan_maturity(
    input4_loan_maturity: data.Input4LoanMaturity,
) -> data.Input4LoanMaturity:
    """Validate `input4_loan_maturity` before the model reads it."""
    data.INPUT4_LOAN_MATURITY.schema.validate(input4_loan_maturity)
    input4_loan_maturity = coerce_input_measure(input4_loan_maturity, dtype="int", series_id="input4_loan_maturity")
    for coordinate in data.INPUT4_LOAN_MATURITY.required:
        require_input_domain(input4_loan_maturity[coordinate], {"between": {"min": 0, "max": 80}}, series_id="input4_loan_maturity" + repr(coordinate))
    return input4_loan_maturity


def _check_input4_disbursements(
    input4_disbursements: data.Input4Disbursements,
) -> data.Input4Disbursements:
    """Validate `input4_disbursements` before the model reads it."""
    data.INPUT4_DISBURSEMENTS.schema.validate(input4_disbursements)
    input4_disbursements = coerce_input_measure(input4_disbursements, dtype="float", series_id="input4_disbursements")
    for coordinate in data.INPUT4_DISBURSEMENTS.required:
        require_input_domain(input4_disbursements[coordinate], {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="input4_disbursements" + repr(coordinate))
    return input4_disbursements


def _check_input4_instrument_names(
    input4_instrument_names: data.Input4InstrumentNames,
) -> data.Input4InstrumentNames:
    """Validate `input4_instrument_names` before the model reads it."""
    data.INPUT4_INSTRUMENT_NAMES.schema.validate(input4_instrument_names)
    input4_instrument_names = coerce_input_measure(input4_instrument_names, dtype="string", series_id="input4_instrument_names")
    return input4_instrument_names


def _check_input4_blend_variant(input4_blend_variant: str) -> str:
    """Validate `input4_blend_variant` before the model reads it."""
    input4_blend_variant = coerce_input_measure(input4_blend_variant, dtype="string", series_id="input4_blend_variant")
    require_input_domain(input4_blend_variant, {"enum": frozenset({"IDA NEW Blend floating"})}, series_id="input4_blend_variant")
    return input4_blend_variant


def _check_input4_blend_scale_key(
    input4_blend_scale_key: data.Input4BlendScaleKey,
) -> data.Input4BlendScaleKey:
    """Validate `input4_blend_scale_key` before the model reads it."""
    data.INPUT4_BLEND_SCALE_KEY.schema.validate(input4_blend_scale_key)
    input4_blend_scale_key = coerce_input_measure(input4_blend_scale_key, dtype="string", series_id="input4_blend_scale_key")
    for coordinate in data.INPUT4_BLEND_SCALE_KEY.required:
        require_input_domain(input4_blend_scale_key[coordinate], {"enum": frozenset({"IDA - 50Y loans", "IDA - SML", "IDA - blend", "IDA - regular", "IDA - small economy", "IDA NEW 40-year credits", "IDA NEW 60-year credits", "IDA NEW Blend (also enter) -->", "IDA NEW Regular"})}, series_id="input4_blend_scale_key" + repr(coordinate))
    return input4_blend_scale_key


def _check_input5_grace_period(
    input5_grace_period: data.Input5GracePeriod,
) -> data.Input5GracePeriod:
    """Validate `input5_grace_period` before the model reads it."""
    data.INPUT5_GRACE_PERIOD.schema.validate(input5_grace_period)
    input5_grace_period = coerce_input_measure(input5_grace_period, dtype="int", series_id="input5_grace_period")
    for coordinate in data.INPUT5_GRACE_PERIOD.required:
        require_input_domain(input5_grace_period[coordinate], {"between": {"min": 0, "max": 50}}, series_id="input5_grace_period" + repr(coordinate))
    return input5_grace_period


def _check_input5_interest_rate_on_domestic_debt(
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt,
) -> data.Input5InterestRateOnDomesticDebt:
    """Validate `input5_interest_rate_on_domestic_debt` before the model reads it."""
    data.INPUT5_INTEREST_RATE_ON_DOMESTIC_DEBT.schema.validate(input5_interest_rate_on_domestic_debt)
    input5_interest_rate_on_domestic_debt = coerce_input_measure(input5_interest_rate_on_domestic_debt, dtype="float", series_id="input5_interest_rate_on_domestic_debt")
    for coordinate in data.INPUT5_INTEREST_RATE_ON_DOMESTIC_DEBT.required:
        require_input_domain(input5_interest_rate_on_domestic_debt[coordinate], {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="input5_interest_rate_on_domestic_debt" + repr(coordinate))
    return input5_interest_rate_on_domestic_debt


def _check_input5_interest_rate_on_domestic_debt_fx_long(
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong,
) -> data.Input5InterestRateOnDomesticDebtFxLong:
    """Validate `input5_interest_rate_on_domestic_debt_fx_long` before the model reads it."""
    data.INPUT5_INTEREST_RATE_ON_DOMESTIC_DEBT_FX_LONG.schema.validate(input5_interest_rate_on_domestic_debt_fx_long)
    input5_interest_rate_on_domestic_debt_fx_long = coerce_input_measure(input5_interest_rate_on_domestic_debt_fx_long, dtype="float", series_id="input5_interest_rate_on_domestic_debt_fx_long")
    for coordinate in data.INPUT5_INTEREST_RATE_ON_DOMESTIC_DEBT_FX_LONG.required:
        require_input_domain(input5_interest_rate_on_domestic_debt_fx_long[coordinate], {"real_between": {"min": 0, "max": 1}}, series_id="input5_interest_rate_on_domestic_debt_fx_long" + repr(coordinate))
    return input5_interest_rate_on_domestic_debt_fx_long


def _check_input5_maturity(input5_maturity: data.Input5Maturity) -> data.Input5Maturity:
    """Validate `input5_maturity` before the model reads it."""
    data.INPUT5_MATURITY.schema.validate(input5_maturity)
    input5_maturity = coerce_input_measure(input5_maturity, dtype="int", series_id="input5_maturity")
    for coordinate in data.INPUT5_MATURITY.required:
        require_input_domain(input5_maturity[coordinate], {"between": {"min": 1, "max": 100}}, series_id="input5_maturity" + repr(coordinate))
    return input5_maturity


def _check_input5_maturity_central_bank(input5_maturity_central_bank: int | str) -> int | str:
    """Validate `input5_maturity_central_bank` before the model reads it."""
    input5_maturity_central_bank = coerce_input_measure(input5_maturity_central_bank, dtype="int", series_id="input5_maturity_central_bank")
    require_input_domain(input5_maturity_central_bank, {"between": {"min": 1, "max": 5}}, series_id="input5_maturity_central_bank")
    return input5_maturity_central_bank


def _check_input5_public_gfns_other_adjustment(
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment,
) -> data.Input5PublicGfnsOtherAdjustment:
    """Validate `input5_public_gfns_other_adjustment` before the model reads it."""
    data.INPUT5_PUBLIC_GFNS_OTHER_ADJUSTMENT.schema.validate(input5_public_gfns_other_adjustment)
    input5_public_gfns_other_adjustment = coerce_input_measure(input5_public_gfns_other_adjustment, dtype="float", series_id="input5_public_gfns_other_adjustment")
    for coordinate in data.INPUT5_PUBLIC_GFNS_OTHER_ADJUSTMENT.required:
        require_input_domain(input5_public_gfns_other_adjustment[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input5_public_gfns_other_adjustment" + repr(coordinate))
    return input5_public_gfns_other_adjustment


def _check_input5_domestic_financing_source(
    input5_domestic_financing_source: int | str,
) -> int | str:
    """Validate `input5_domestic_financing_source` before the model reads it."""
    input5_domestic_financing_source = coerce_input_measure(input5_domestic_financing_source, dtype="int", series_id="input5_domestic_financing_source")
    require_input_domain(input5_domestic_financing_source, {"enum": frozenset({0, 1})}, series_id="input5_domestic_financing_source")
    return input5_domestic_financing_source


def _check_input5_gfn_share(input5_gfn_share: data.Input5GfnShare) -> data.Input5GfnShare:
    """Validate `input5_gfn_share` before the model reads it."""
    data.INPUT5_GFN_SHARE.schema.validate(input5_gfn_share)
    input5_gfn_share = coerce_input_measure(input5_gfn_share, dtype="float", series_id="input5_gfn_share")
    for coordinate in data.INPUT5_GFN_SHARE.required:
        require_input_domain(input5_gfn_share[coordinate], {"real_between": {"min": 0, "max": 1}}, series_id="input5_gfn_share" + repr(coordinate))
    return input5_gfn_share


def _check_start_working_language(
    start_working_language: Literal["English", "Espa\u00f1ol", "Fran\u00e7ais", "Portugues"],
) -> Literal["English", "Espa\u00f1ol", "Fran\u00e7ais", "Portugues"]:
    """Validate `start_working_language` before the model reads it."""
    start_working_language = coerce_input_measure(start_working_language, dtype="string", series_id="start_working_language")
    require_annotated_domain(
        start_working_language,
        Literal["English", "Espa\u00f1ol", "Fran\u00e7ais", "Portugues"],
        series_id="start_working_language",
    )
    return start_working_language


def _check_country(country: str) -> str:
    """Validate `country` before the model reads it."""
    country = coerce_input_measure(country, dtype="string", series_id="country")
    require_input_domain(country, {"enum": frozenset({"Cote d'Ivoire", "Afghanistan", "Bangladesh", "Benin", "Bhutan", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, DR", "Congo, Republic of", "Djibouti", "Dominica", "Eritrea", "Ethiopia", "Gambia, The", "Ghana", "Grenada", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Kenya", "Kiribati", "Kyrgyz Republic", "Lao PDR", "Lesotho", "Liberia", "Madagascar", "Malawi", "Maldives", "Mali", "Marshall Islands", "Mauritania", "Micronesia", "Moldova", "Mozambique", "Myanmar", "Nepal", "Nicaragua", "Niger", "Papua New Guinea", "Rwanda", "Samoa", "Sao Tome & Principe", "Senegal", "Sierra Leone", "Solomon Islands", "Somalia", "South Sudan", "St. Lucia", "St. Vincent & the Grenadines", "Sudan", "Tajikistan", "Tanzania", "Timor-Leste", "Togo", "Tonga", "Tuvalu", "Uganda", "Uzbekistan", "Vanuatu", "Yemen, Republic of", "Zambia", "Zimbabwe"})}, series_id="country")
    return country


def _check_first_projection_year(first_projection_year: int | str) -> int | str:
    """Validate `first_projection_year` before the model reads it."""
    first_projection_year = coerce_input_measure(first_projection_year, dtype="int", series_id="first_projection_year")
    require_input_domain(first_projection_year, {"between": {"min": 1990, "max": 2100}}, series_id="first_projection_year")
    return first_projection_year


def _check_discount_rate(discount_rate: float | str) -> float | str:
    """Validate `discount_rate` before the model reads it."""
    discount_rate = coerce_input_measure(discount_rate, dtype="float", series_id="discount_rate")
    require_input_domain(discount_rate, {"real_between": {"min": 0, "max": 1}}, series_id="discount_rate")
    return discount_rate


def _check_external_domestic_debt_definition(external_domestic_debt_definition: str) -> str:
    """Validate `external_domestic_debt_definition` before the model reads it."""
    external_domestic_debt_definition = coerce_input_measure(external_domestic_debt_definition, dtype="string", series_id="external_domestic_debt_definition")
    require_input_domain(external_domestic_debt_definition, {"enum": frozenset({"Currency-based", "Residency-based"})}, series_id="external_domestic_debt_definition")
    return external_domestic_debt_definition


def _check_fiscal_space_moderate_assessment_flag(
    fiscal_space_moderate_assessment_flag: int | str,
) -> int | str:
    """Validate `fiscal_space_moderate_assessment_flag` before the model reads it."""
    fiscal_space_moderate_assessment_flag = coerce_input_measure(fiscal_space_moderate_assessment_flag, dtype="int", series_id="fiscal_space_moderate_assessment_flag")
    require_input_domain(fiscal_space_moderate_assessment_flag, {"between": {"min": 0, "max": 1}}, series_id="fiscal_space_moderate_assessment_flag")
    return fiscal_space_moderate_assessment_flag


def _check_fiscal_space_stock_band(
    fiscal_space_stock_band: data.FiscalSpaceStockBand,
) -> data.FiscalSpaceStockBand:
    """Validate `fiscal_space_stock_band` before the model reads it."""
    data.FISCAL_SPACE_STOCK_BAND.schema.validate(fiscal_space_stock_band)
    fiscal_space_stock_band = coerce_input_measure(fiscal_space_stock_band, dtype="float", series_id="fiscal_space_stock_band")
    for coordinate in data.FISCAL_SPACE_STOCK_BAND.required:
        require_input_domain(fiscal_space_stock_band[coordinate], {"real_between": {"min": 0, "max": 100}}, series_id="fiscal_space_stock_band" + repr(coordinate))
    return fiscal_space_stock_band


def _check_fiscal_space_flow_band(
    fiscal_space_flow_band: data.FiscalSpaceFlowBand,
) -> data.FiscalSpaceFlowBand:
    """Validate `fiscal_space_flow_band` before the model reads it."""
    data.FISCAL_SPACE_FLOW_BAND.schema.validate(fiscal_space_flow_band)
    fiscal_space_flow_band = coerce_input_measure(fiscal_space_flow_band, dtype="float", series_id="fiscal_space_flow_band")
    for coordinate in data.FISCAL_SPACE_FLOW_BAND.required:
        require_input_domain(fiscal_space_flow_band[coordinate], {"real_between": {"min": 0, "max": 100}}, series_id="fiscal_space_flow_band" + repr(coordinate))
    return fiscal_space_flow_band


def _check_contingent_liability_other_elements_pct_gdp(
    contingent_liability_other_elements_pct_gdp: float | str,
) -> float | str:
    """Validate `contingent_liability_other_elements_pct_gdp` before the model reads it."""
    contingent_liability_other_elements_pct_gdp = coerce_input_measure(contingent_liability_other_elements_pct_gdp, dtype="float", series_id="contingent_liability_other_elements_pct_gdp")
    require_input_domain(contingent_liability_other_elements_pct_gdp, {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="contingent_liability_other_elements_pct_gdp")
    return contingent_liability_other_elements_pct_gdp


def _check_contingent_liability_soe_debt_pct_gdp(
    contingent_liability_soe_debt_pct_gdp: float | str,
) -> float | str:
    """Validate `contingent_liability_soe_debt_pct_gdp` before the model reads it."""
    contingent_liability_soe_debt_pct_gdp = coerce_input_measure(contingent_liability_soe_debt_pct_gdp, dtype="float", series_id="contingent_liability_soe_debt_pct_gdp")
    require_input_domain(contingent_liability_soe_debt_pct_gdp, {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="contingent_liability_soe_debt_pct_gdp")
    return contingent_liability_soe_debt_pct_gdp


def _check_contingent_liability_financial_market_pct_gdp(
    contingent_liability_financial_market_pct_gdp: float | str,
) -> float | str:
    """Validate `contingent_liability_financial_market_pct_gdp` before the model reads it."""
    contingent_liability_financial_market_pct_gdp = coerce_input_measure(contingent_liability_financial_market_pct_gdp, dtype="float", series_id="contingent_liability_financial_market_pct_gdp")
    require_input_domain(contingent_liability_financial_market_pct_gdp, {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="contingent_liability_financial_market_pct_gdp")
    return contingent_liability_financial_market_pct_gdp


def _check_ppp_capital_stock_shock_pct(ppp_capital_stock_shock_pct: float | str) -> float | str:
    """Validate `ppp_capital_stock_shock_pct` before the model reads it."""
    ppp_capital_stock_shock_pct = coerce_input_measure(ppp_capital_stock_shock_pct, dtype="float", series_id="ppp_capital_stock_shock_pct")
    require_input_domain(ppp_capital_stock_shock_pct, {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="ppp_capital_stock_shock_pct")
    return ppp_capital_stock_shock_pct


def _check_customized_public_delta(
    customized_public_delta: data.CustomizedPublicDelta,
) -> data.CustomizedPublicDelta:
    """Validate `customized_public_delta` before the model reads it."""
    data.CUSTOMIZED_PUBLIC_DELTA.schema.validate(customized_public_delta)
    customized_public_delta = coerce_input_measure(customized_public_delta, dtype="float", series_id="customized_public_delta")
    for coordinate in data.CUSTOMIZED_PUBLIC_DELTA.required:
        require_input_domain(customized_public_delta[coordinate], {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_public_delta" + repr(coordinate))
    return customized_public_delta


def _check_blend_ida_new_floating_currency(blend_ida_new_floating_currency: str) -> str:
    """Validate `blend_ida_new_floating_currency` before the model reads it."""
    blend_ida_new_floating_currency = coerce_input_measure(blend_ida_new_floating_currency, dtype="string", series_id="blend_ida_new_floating_currency")
    require_input_domain(blend_ida_new_floating_currency, {"enum": frozenset({"EUR", "GBP", "JPY", "USD"})}, series_id="blend_ida_new_floating_currency")
    return blend_ida_new_floating_currency


def _check_input_1_rer_overvaluation(input_1_rer_overvaluation: float | str) -> float | str:
    """Validate `input_1_rer_overvaluation` before the model reads it."""
    input_1_rer_overvaluation = coerce_input_measure(input_1_rer_overvaluation, dtype="float", series_id="input_1_rer_overvaluation")
    require_input_domain(input_1_rer_overvaluation, {"real_between": {"min": -100, "max": 100}}, series_id="input_1_rer_overvaluation")
    return input_1_rer_overvaluation


def _check_customized_public_include_scenario(customized_public_include_scenario: str) -> str:
    """Validate `customized_public_include_scenario` before the model reads it."""
    customized_public_include_scenario = coerce_input_measure(customized_public_include_scenario, dtype="string", series_id="customized_public_include_scenario")
    require_input_domain(customized_public_include_scenario, {"enum": frozenset({"No", "Yes"})}, series_id="customized_public_include_scenario")
    return customized_public_include_scenario


def _check_input6_commodity_group_relevant(
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant,
) -> data.Input6CommodityGroupRelevant:
    """Validate `input6_commodity_group_relevant` before the model reads it."""
    data.INPUT6_COMMODITY_GROUP_RELEVANT.schema.validate(input6_commodity_group_relevant)
    input6_commodity_group_relevant = coerce_input_measure(input6_commodity_group_relevant, dtype="string", series_id="input6_commodity_group_relevant")
    for coordinate in data.INPUT6_COMMODITY_GROUP_RELEVANT.required:
        require_input_domain(input6_commodity_group_relevant[coordinate], {"enum": frozenset({"No", "Yes"})}, series_id="input6_commodity_group_relevant" + repr(coordinate))
    return input6_commodity_group_relevant


def _check_input8_sdr_interest_historical(
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical,
) -> data.Input8SdrInterestHistorical:
    """Validate `input8_sdr_interest_historical` before the model reads it."""
    data.INPUT8_SDR_INTEREST_HISTORICAL.schema.validate(input8_sdr_interest_historical)
    input8_sdr_interest_historical = coerce_input_measure(input8_sdr_interest_historical, dtype="float", series_id="input8_sdr_interest_historical")
    for coordinate in data.INPUT8_SDR_INTEREST_HISTORICAL.required:
        require_input_domain(input8_sdr_interest_historical[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input8_sdr_interest_historical" + repr(coordinate))
    return input8_sdr_interest_historical


def _check_input8_sdr_interest(
    input8_sdr_interest: data.Input8SdrInterest,
) -> data.Input8SdrInterest:
    """Validate `input8_sdr_interest` before the model reads it."""
    data.INPUT8_SDR_INTEREST.schema.validate(input8_sdr_interest)
    input8_sdr_interest = coerce_input_measure(input8_sdr_interest, dtype="float", series_id="input8_sdr_interest")
    for coordinate in data.INPUT8_SDR_INTEREST.required:
        require_input_domain(input8_sdr_interest[coordinate], {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="input8_sdr_interest" + repr(coordinate))
    return input8_sdr_interest


def _check_input8_sdr_interest_rate(input8_sdr_interest_rate: float | str) -> float | str:
    """Validate `input8_sdr_interest_rate` before the model reads it."""
    input8_sdr_interest_rate = coerce_input_measure(input8_sdr_interest_rate, dtype="float", series_id="input8_sdr_interest_rate")
    require_input_domain(input8_sdr_interest_rate, {"real_between": {"min": 0, "max": 1}}, series_id="input8_sdr_interest_rate")
    return input8_sdr_interest_rate


def _check_input6_tailored_tests_enabled(
    input6_tailored_tests_enabled: Literal["Off", "On"],
) -> Literal["Off", "On"]:
    """Validate `input6_tailored_tests_enabled` before the model reads it."""
    input6_tailored_tests_enabled = coerce_input_measure(input6_tailored_tests_enabled, dtype="string", series_id="input6_tailored_tests_enabled")
    require_annotated_domain(
        input6_tailored_tests_enabled,
        Literal["Off", "On"],
        series_id="input6_tailored_tests_enabled",
    )
    return input6_tailored_tests_enabled


def _check_input6_standard_size_threshold_mode(
    input6_standard_size_threshold_mode: Literal["New", "Old"],
) -> Literal["New", "Old"]:
    """Validate `input6_standard_size_threshold_mode` before the model reads it."""
    input6_standard_size_threshold_mode = coerce_input_measure(input6_standard_size_threshold_mode, dtype="string", series_id="input6_standard_size_threshold_mode")
    require_annotated_domain(
        input6_standard_size_threshold_mode,
        Literal["New", "Old"],
        series_id="input6_standard_size_threshold_mode",
    )
    return input6_standard_size_threshold_mode


def _check_input6_standard_interactions(input6_standard_interactions: str) -> str:
    """Validate `input6_standard_interactions` before the model reads it."""
    input6_standard_interactions = coerce_input_measure(input6_standard_interactions, dtype="string", series_id="input6_standard_interactions")
    require_input_domain(input6_standard_interactions, {"enum": frozenset({"Off", "On"})}, series_id="input6_standard_interactions")
    return input6_standard_interactions


def _check_input6_standard_user_defined_threshold(
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold,
) -> data.Input6StandardUserDefinedThreshold:
    """Validate `input6_standard_user_defined_threshold` before the model reads it."""
    data.INPUT6_STANDARD_USER_DEFINED_THRESHOLD.schema.validate(input6_standard_user_defined_threshold)
    input6_standard_user_defined_threshold = coerce_input_measure(input6_standard_user_defined_threshold, dtype="string", series_id="input6_standard_user_defined_threshold")
    for coordinate in data.INPUT6_STANDARD_USER_DEFINED_THRESHOLD.required:
        require_input_domain(input6_standard_user_defined_threshold[coordinate], {"enum": frozenset({"Baseline projection only", "Historical average only", "Whichever is lower"})}, series_id="input6_standard_user_defined_threshold" + repr(coordinate))
    return input6_standard_user_defined_threshold


def _check_input3_input_3_macro_gross_domestic_product_us_dollars(
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars,
) -> data.Input3Input3MacroGrossDomesticProductUsDollars:
    """Validate `input3_input_3_macro_gross_domestic_product_us_dollars` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_GROSS_DOMESTIC_PRODUCT_US_DOLLARS.schema.validate(input3_input_3_macro_gross_domestic_product_us_dollars)
    input3_input_3_macro_gross_domestic_product_us_dollars = coerce_input_measure(input3_input_3_macro_gross_domestic_product_us_dollars, dtype="float", series_id="input3_input_3_macro_gross_domestic_product_us_dollars")
    for coordinate in data.INPUT3_INPUT_3_MACRO_GROSS_DOMESTIC_PRODUCT_US_DOLLARS.required:
        require_input_domain(input3_input_3_macro_gross_domestic_product_us_dollars[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_gross_domestic_product_us_dollars" + repr(coordinate))
    return input3_input_3_macro_gross_domestic_product_us_dollars


def _check_input3_input_3_macro_real_gross_domestic_product(
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct,
) -> data.Input3Input3MacroRealGrossDomesticProduct:
    """Validate `input3_input_3_macro_real_gross_domestic_product` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_REAL_GROSS_DOMESTIC_PRODUCT.schema.validate(input3_input_3_macro_real_gross_domestic_product)
    input3_input_3_macro_real_gross_domestic_product = coerce_input_measure(input3_input_3_macro_real_gross_domestic_product, dtype="float", series_id="input3_input_3_macro_real_gross_domestic_product")
    for coordinate in data.INPUT3_INPUT_3_MACRO_REAL_GROSS_DOMESTIC_PRODUCT.required:
        require_input_domain(input3_input_3_macro_real_gross_domestic_product[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_real_gross_domestic_product" + repr(coordinate))
    return input3_input_3_macro_real_gross_domestic_product


def _check_input3_input_3_macro_u_s_deflator(
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator,
) -> data.Input3Input3MacroUSDeflator:
    """Validate `input3_input_3_macro_u_s_deflator` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_U_S_DEFLATOR.schema.validate(input3_input_3_macro_u_s_deflator)
    input3_input_3_macro_u_s_deflator = coerce_input_measure(input3_input_3_macro_u_s_deflator, dtype="float", series_id="input3_input_3_macro_u_s_deflator")
    for coordinate in data.INPUT3_INPUT_3_MACRO_U_S_DEFLATOR.required:
        require_input_domain(input3_input_3_macro_u_s_deflator[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_u_s_deflator" + repr(coordinate))
    return input3_input_3_macro_u_s_deflator


def _check_input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p(
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP,
) -> data.Input3Input3MacroNationalCurrencyPerUSDollarEOP:
    """Validate `input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_NATIONAL_CURRENCY_PER_U_S_DOLLAR_E_O_P.schema.validate(input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p)
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p = coerce_input_measure(input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p, dtype="float", series_id="input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p")
    for coordinate in data.INPUT3_INPUT_3_MACRO_NATIONAL_CURRENCY_PER_U_S_DOLLAR_E_O_P.required:
        require_input_domain(input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p" + repr(coordinate))
    return input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p


def _check_input3_input_3_macro_national_currency_per_u_s_dollar_p_a(
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA,
) -> data.Input3Input3MacroNationalCurrencyPerUSDollarPA:
    """Validate `input3_input_3_macro_national_currency_per_u_s_dollar_p_a` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_NATIONAL_CURRENCY_PER_U_S_DOLLAR_P_A.schema.validate(input3_input_3_macro_national_currency_per_u_s_dollar_p_a)
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a = coerce_input_measure(input3_input_3_macro_national_currency_per_u_s_dollar_p_a, dtype="float", series_id="input3_input_3_macro_national_currency_per_u_s_dollar_p_a")
    for coordinate in data.INPUT3_INPUT_3_MACRO_NATIONAL_CURRENCY_PER_U_S_DOLLAR_P_A.required:
        require_input_domain(input3_input_3_macro_national_currency_per_u_s_dollar_p_a[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_national_currency_per_u_s_dollar_p_a" + repr(coordinate))
    return input3_input_3_macro_national_currency_per_u_s_dollar_p_a


def _check_input3_input_3_macro_government_revenue_and_grants(
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants,
) -> data.Input3Input3MacroGovernmentRevenueAndGrants:
    """Validate `input3_input_3_macro_government_revenue_and_grants` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_GOVERNMENT_REVENUE_AND_GRANTS.schema.validate(input3_input_3_macro_government_revenue_and_grants)
    input3_input_3_macro_government_revenue_and_grants = coerce_input_measure(input3_input_3_macro_government_revenue_and_grants, dtype="float", series_id="input3_input_3_macro_government_revenue_and_grants")
    for coordinate in data.INPUT3_INPUT_3_MACRO_GOVERNMENT_REVENUE_AND_GRANTS.required:
        require_input_domain(input3_input_3_macro_government_revenue_and_grants[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_government_revenue_and_grants" + repr(coordinate))
    return input3_input_3_macro_government_revenue_and_grants


def _check_input3_input_3_macro_government_grants(
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants,
) -> data.Input3Input3MacroGovernmentGrants:
    """Validate `input3_input_3_macro_government_grants` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_GOVERNMENT_GRANTS.schema.validate(input3_input_3_macro_government_grants)
    input3_input_3_macro_government_grants = coerce_input_measure(input3_input_3_macro_government_grants, dtype="float", series_id="input3_input_3_macro_government_grants")
    for coordinate in data.INPUT3_INPUT_3_MACRO_GOVERNMENT_GRANTS.required:
        require_input_domain(input3_input_3_macro_government_grants[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_government_grants" + repr(coordinate))
    return input3_input_3_macro_government_grants


def _check_in3_macro_government_primary_expenditures_this_used_be(
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe,
) -> data.In3MacroGovernmentPrimaryExpendituresThisUsedBe:
    """Validate `in3_macro_government_primary_expenditures_this_used_be` before the model reads it."""
    data.IN3_MACRO_GOVERNMENT_PRIMARY_EXPENDITURES_THIS_USED_BE.schema.validate(in3_macro_government_primary_expenditures_this_used_be)
    in3_macro_government_primary_expenditures_this_used_be = coerce_input_measure(in3_macro_government_primary_expenditures_this_used_be, dtype="float", series_id="in3_macro_government_primary_expenditures_this_used_be")
    for coordinate in data.IN3_MACRO_GOVERNMENT_PRIMARY_EXPENDITURES_THIS_USED_BE.required:
        require_input_domain(in3_macro_government_primary_expenditures_this_used_be[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="in3_macro_government_primary_expenditures_this_used_be" + repr(coordinate))
    return in3_macro_government_primary_expenditures_this_used_be


def _check_in3_macro_public_sector_liquid_assets_stock_e_g_cash(
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash,
) -> data.In3MacroPublicSectorLiquidAssetsStockEGCash:
    """Validate `in3_macro_public_sector_liquid_assets_stock_e_g_cash` before the model reads it."""
    data.IN3_MACRO_PUBLIC_SECTOR_LIQUID_ASSETS_STOCK_E_G_CASH.schema.validate(in3_macro_public_sector_liquid_assets_stock_e_g_cash)
    in3_macro_public_sector_liquid_assets_stock_e_g_cash = coerce_input_measure(
        in3_macro_public_sector_liquid_assets_stock_e_g_cash,
        dtype="float",
        series_id="in3_macro_public_sector_liquid_assets_stock_e_g_cash",
        enum=frozenset({"n.a."}),
    )
    for coordinate in data.IN3_MACRO_PUBLIC_SECTOR_LIQUID_ASSETS_STOCK_E_G_CASH.required:
        require_input_domain(in3_macro_public_sector_liquid_assets_stock_e_g_cash[coordinate], {"enum": frozenset({"n.a."}), "real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="in3_macro_public_sector_liquid_assets_stock_e_g_cash" + repr(coordinate))
    return in3_macro_public_sector_liquid_assets_stock_e_g_cash


def _check_in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g(
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG,
) -> data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG:
    """Validate `in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g` before the model reads it."""
    data.IN3_MACRO_LIQUID_FINANCIAL_ASSETS_USED_MEET_GFNS_FLOW_E_G.schema.validate(in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g)
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g = coerce_input_measure(in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g, dtype="float", series_id="in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g")
    for coordinate in data.IN3_MACRO_LIQUID_FINANCIAL_ASSETS_USED_MEET_GFNS_FLOW_E_G.required:
        require_input_domain(in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g" + repr(coordinate))
    return in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g


def _check_input3_input_3_macro_privatization_proceeds(
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds,
) -> data.Input3Input3MacroPrivatizationProceeds:
    """Validate `input3_input_3_macro_privatization_proceeds` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_PRIVATIZATION_PROCEEDS.schema.validate(input3_input_3_macro_privatization_proceeds)
    input3_input_3_macro_privatization_proceeds = coerce_input_measure(input3_input_3_macro_privatization_proceeds, dtype="float", series_id="input3_input_3_macro_privatization_proceeds")
    for coordinate in data.INPUT3_INPUT_3_MACRO_PRIVATIZATION_PROCEEDS.required:
        require_input_domain(input3_input_3_macro_privatization_proceeds[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_privatization_proceeds" + repr(coordinate))
    return input3_input_3_macro_privatization_proceeds


def _check_in3_macro_recognition_of_contingent_liab_e_g_bank(
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank,
) -> data.In3MacroRecognitionOfContingentLiabEGBank:
    """Validate `in3_macro_recognition_of_contingent_liab_e_g_bank` before the model reads it."""
    data.IN3_MACRO_RECOGNITION_OF_CONTINGENT_LIAB_E_G_BANK.schema.validate(in3_macro_recognition_of_contingent_liab_e_g_bank)
    in3_macro_recognition_of_contingent_liab_e_g_bank = coerce_input_measure(in3_macro_recognition_of_contingent_liab_e_g_bank, dtype="float", series_id="in3_macro_recognition_of_contingent_liab_e_g_bank")
    for coordinate in data.IN3_MACRO_RECOGNITION_OF_CONTINGENT_LIAB_E_G_BANK.required:
        require_input_domain(in3_macro_recognition_of_contingent_liab_e_g_bank[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="in3_macro_recognition_of_contingent_liab_e_g_bank" + repr(coordinate))
    return in3_macro_recognition_of_contingent_liab_e_g_bank


def _check_input3_input_3_macro_debt_relief_non_multilateral_hipc(
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc,
) -> data.Input3Input3MacroDebtReliefNonMultilateralHipc:
    """Validate `input3_input_3_macro_debt_relief_non_multilateral_hipc` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_DEBT_RELIEF_NON_MULTILATERAL_HIPC.schema.validate(input3_input_3_macro_debt_relief_non_multilateral_hipc)
    input3_input_3_macro_debt_relief_non_multilateral_hipc = coerce_input_measure(input3_input_3_macro_debt_relief_non_multilateral_hipc, dtype="float", series_id="input3_input_3_macro_debt_relief_non_multilateral_hipc")
    for coordinate in data.INPUT3_INPUT_3_MACRO_DEBT_RELIEF_NON_MULTILATERAL_HIPC.required:
        require_input_domain(input3_input_3_macro_debt_relief_non_multilateral_hipc[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_debt_relief_non_multilateral_hipc" + repr(coordinate))
    return input3_input_3_macro_debt_relief_non_multilateral_hipc


def _check_input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify(
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify,
) -> data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify:
    """Validate `input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_OTHER_DEBT_CREATING_OR_REDUCING_FLOW_PLEASE_SPECIFY.schema.validate(input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify)
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify = coerce_input_measure(input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify, dtype="float", series_id="input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify")
    for coordinate in data.INPUT3_INPUT_3_MACRO_OTHER_DEBT_CREATING_OR_REDUCING_FLOW_PLEASE_SPECIFY.required:
        require_input_domain(input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify" + repr(coordinate))
    return input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify


def _check_input3_input_3_macro_current_account(
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount,
) -> data.Input3Input3MacroCurrentAccount:
    """Validate `input3_input_3_macro_current_account` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_CURRENT_ACCOUNT.schema.validate(input3_input_3_macro_current_account)
    input3_input_3_macro_current_account = coerce_input_measure(input3_input_3_macro_current_account, dtype="float", series_id="input3_input_3_macro_current_account")
    for coordinate in data.INPUT3_INPUT_3_MACRO_CURRENT_ACCOUNT.required:
        require_input_domain(input3_input_3_macro_current_account[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_current_account" + repr(coordinate))
    return input3_input_3_macro_current_account


def _check_input3_input_3_macro_exports_of_goods_and_services(
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices,
) -> data.Input3Input3MacroExportsOfGoodsAndServices:
    """Validate `input3_input_3_macro_exports_of_goods_and_services` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_EXPORTS_OF_GOODS_AND_SERVICES.schema.validate(input3_input_3_macro_exports_of_goods_and_services)
    input3_input_3_macro_exports_of_goods_and_services = coerce_input_measure(input3_input_3_macro_exports_of_goods_and_services, dtype="float", series_id="input3_input_3_macro_exports_of_goods_and_services")
    for coordinate in data.INPUT3_INPUT_3_MACRO_EXPORTS_OF_GOODS_AND_SERVICES.required:
        require_input_domain(input3_input_3_macro_exports_of_goods_and_services[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_exports_of_goods_and_services" + repr(coordinate))
    return input3_input_3_macro_exports_of_goods_and_services


def _check_input3_input_3_macro_exports_commodity_fuel(
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel,
) -> data.Input3Input3MacroExportsCommodityFuel:
    """Validate `input3_input_3_macro_exports_commodity_fuel` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_EXPORTS_COMMODITY_FUEL.schema.validate(input3_input_3_macro_exports_commodity_fuel)
    input3_input_3_macro_exports_commodity_fuel = coerce_input_measure(input3_input_3_macro_exports_commodity_fuel, dtype="float", series_id="input3_input_3_macro_exports_commodity_fuel")
    for coordinate in data.INPUT3_INPUT_3_MACRO_EXPORTS_COMMODITY_FUEL.required:
        require_input_domain(input3_input_3_macro_exports_commodity_fuel[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_exports_commodity_fuel" + repr(coordinate))
    return input3_input_3_macro_exports_commodity_fuel


def _check_input3_input_3_macro_exports_commodity_non_fuel(
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel,
) -> data.Input3Input3MacroExportsCommodityNonFuel:
    """Validate `input3_input_3_macro_exports_commodity_non_fuel` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_EXPORTS_COMMODITY_NON_FUEL.schema.validate(input3_input_3_macro_exports_commodity_non_fuel)
    input3_input_3_macro_exports_commodity_non_fuel = coerce_input_measure(input3_input_3_macro_exports_commodity_non_fuel, dtype="float", series_id="input3_input_3_macro_exports_commodity_non_fuel")
    for coordinate in data.INPUT3_INPUT_3_MACRO_EXPORTS_COMMODITY_NON_FUEL.required:
        require_input_domain(input3_input_3_macro_exports_commodity_non_fuel[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_exports_commodity_non_fuel" + repr(coordinate))
    return input3_input_3_macro_exports_commodity_non_fuel


def _check_input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number(
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber,
) -> data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber:
    """Validate `input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_IMPORTS_OF_GOODS_AND_SERVICES_ENTER_AS_A_POSITIVE_NUMBER.schema.validate(input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number)
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number = coerce_input_measure(input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number, dtype="float", series_id="input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number")
    for coordinate in data.INPUT3_INPUT_3_MACRO_IMPORTS_OF_GOODS_AND_SERVICES_ENTER_AS_A_POSITIVE_NUMBER.required:
        require_input_domain(input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number" + repr(coordinate))
    return input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number


def _check_input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number(
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber,
) -> data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber:
    """Validate `input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_IMPORTS_COMMODITY_FUEL_ENTER_AS_A_POSITIVE_NUMBER.schema.validate(input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number)
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number = coerce_input_measure(input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number, dtype="float", series_id="input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number")
    for coordinate in data.INPUT3_INPUT_3_MACRO_IMPORTS_COMMODITY_FUEL_ENTER_AS_A_POSITIVE_NUMBER.required:
        require_input_domain(input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number" + repr(coordinate))
    return input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number


def _check_input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number(
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber,
) -> data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber:
    """Validate `input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_IMPORTS_COMMODITY_NON_FUEL_ENTER_AS_A_POSITIVE_NUMBER.schema.validate(input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number)
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number = coerce_input_measure(input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number, dtype="float", series_id="input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number")
    for coordinate in data.INPUT3_INPUT_3_MACRO_IMPORTS_COMMODITY_NON_FUEL_ENTER_AS_A_POSITIVE_NUMBER.required:
        require_input_domain(input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number" + repr(coordinate))
    return input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number


def _check_input3_input_3_macro_current_transfers_net(
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet,
) -> data.Input3Input3MacroCurrentTransfersNet:
    """Validate `input3_input_3_macro_current_transfers_net` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_CURRENT_TRANSFERS_NET.schema.validate(input3_input_3_macro_current_transfers_net)
    input3_input_3_macro_current_transfers_net = coerce_input_measure(input3_input_3_macro_current_transfers_net, dtype="float", series_id="input3_input_3_macro_current_transfers_net")
    for coordinate in data.INPUT3_INPUT_3_MACRO_CURRENT_TRANSFERS_NET.required:
        require_input_domain(input3_input_3_macro_current_transfers_net[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_current_transfers_net" + repr(coordinate))
    return input3_input_3_macro_current_transfers_net


def _check_input3_input_3_macro_foreign_direct_investment(
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment,
) -> data.Input3Input3MacroForeignDirectInvestment:
    """Validate `input3_input_3_macro_foreign_direct_investment` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_FOREIGN_DIRECT_INVESTMENT.schema.validate(input3_input_3_macro_foreign_direct_investment)
    input3_input_3_macro_foreign_direct_investment = coerce_input_measure(input3_input_3_macro_foreign_direct_investment, dtype="float", series_id="input3_input_3_macro_foreign_direct_investment")
    for coordinate in data.INPUT3_INPUT_3_MACRO_FOREIGN_DIRECT_INVESTMENT.required:
        require_input_domain(input3_input_3_macro_foreign_direct_investment[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_macro_foreign_direct_investment" + repr(coordinate))
    return input3_input_3_macro_foreign_direct_investment


def _check_input3_input_3_external_debt_ppg_mlt_external_debt_outstanding(
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding,
) -> data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding:
    """Validate `input3_input_3_external_debt_ppg_mlt_external_debt_outstanding` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_MLT_EXTERNAL_DEBT_OUTSTANDING.schema.validate(input3_input_3_external_debt_ppg_mlt_external_debt_outstanding)
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding = coerce_input_measure(input3_input_3_external_debt_ppg_mlt_external_debt_outstanding, dtype="float", series_id="input3_input_3_external_debt_ppg_mlt_external_debt_outstanding")
    for coordinate in data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_MLT_EXTERNAL_DEBT_OUTSTANDING.required:
        require_input_domain(input3_input_3_external_debt_ppg_mlt_external_debt_outstanding[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_external_debt_ppg_mlt_external_debt_outstanding" + repr(coordinate))
    return input3_input_3_external_debt_ppg_mlt_external_debt_outstanding


def _check_input3_input_3_external_debt_ppg_st_external_debt_outstanding(
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding,
) -> data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding:
    """Validate `input3_input_3_external_debt_ppg_st_external_debt_outstanding` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_ST_EXTERNAL_DEBT_OUTSTANDING.schema.validate(input3_input_3_external_debt_ppg_st_external_debt_outstanding)
    input3_input_3_external_debt_ppg_st_external_debt_outstanding = coerce_input_measure(input3_input_3_external_debt_ppg_st_external_debt_outstanding, dtype="float", series_id="input3_input_3_external_debt_ppg_st_external_debt_outstanding")
    for coordinate in data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_ST_EXTERNAL_DEBT_OUTSTANDING.required:
        require_input_domain(input3_input_3_external_debt_ppg_st_external_debt_outstanding[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_external_debt_ppg_st_external_debt_outstanding" + repr(coordinate))
    return input3_input_3_external_debt_ppg_st_external_debt_outstanding


def _check_input3_input_3_external_debt_ppg_external_debt_interest_due(
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue,
) -> data.Input3Input3ExternalDebtPpgExternalDebtInterestDue:
    """Validate `input3_input_3_external_debt_ppg_external_debt_interest_due` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_EXTERNAL_DEBT_INTEREST_DUE.schema.validate(input3_input_3_external_debt_ppg_external_debt_interest_due)
    input3_input_3_external_debt_ppg_external_debt_interest_due = coerce_input_measure(input3_input_3_external_debt_ppg_external_debt_interest_due, dtype="float", series_id="input3_input_3_external_debt_ppg_external_debt_interest_due")
    for coordinate in data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_EXTERNAL_DEBT_INTEREST_DUE.required:
        require_input_domain(input3_input_3_external_debt_ppg_external_debt_interest_due[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_external_debt_ppg_external_debt_interest_due" + repr(coordinate))
    return input3_input_3_external_debt_ppg_external_debt_interest_due


def _check_input3_input_3_external_debt_ppg_external_arrears(
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears,
) -> data.Input3Input3ExternalDebtPpgExternalArrears:
    """Validate `input3_input_3_external_debt_ppg_external_arrears` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_EXTERNAL_ARREARS.schema.validate(input3_input_3_external_debt_ppg_external_arrears)
    input3_input_3_external_debt_ppg_external_arrears = coerce_input_measure(
        input3_input_3_external_debt_ppg_external_arrears,
        dtype="float",
        series_id="input3_input_3_external_debt_ppg_external_arrears",
        enum=frozenset({"n.a."}),
    )
    for coordinate in data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_EXTERNAL_ARREARS.required:
        require_input_domain(input3_input_3_external_debt_ppg_external_arrears[coordinate], {"enum": frozenset({"n.a."}), "real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_external_debt_ppg_external_arrears" + repr(coordinate))
    return input3_input_3_external_debt_ppg_external_arrears


def _check_input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding(
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding,
) -> data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding:
    """Validate `input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_SECTOR_MLT_EXTERNAL_DEBT_OUTSTANDING.schema.validate(input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding)
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding = coerce_input_measure(input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding, dtype="float", series_id="input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding")
    for coordinate in data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_SECTOR_MLT_EXTERNAL_DEBT_OUTSTANDING.required:
        require_input_domain(input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding" + repr(coordinate))
    return input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding


def _check_input3_input_3_external_debt_private_sector_st_external_debt_outstanding(
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding,
) -> data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding:
    """Validate `input3_input_3_external_debt_private_sector_st_external_debt_outstanding` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_SECTOR_ST_EXTERNAL_DEBT_OUTSTANDING.schema.validate(input3_input_3_external_debt_private_sector_st_external_debt_outstanding)
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding = coerce_input_measure(input3_input_3_external_debt_private_sector_st_external_debt_outstanding, dtype="float", series_id="input3_input_3_external_debt_private_sector_st_external_debt_outstanding")
    for coordinate in data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_SECTOR_ST_EXTERNAL_DEBT_OUTSTANDING.required:
        require_input_domain(input3_input_3_external_debt_private_sector_st_external_debt_outstanding[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_external_debt_private_sector_st_external_debt_outstanding" + repr(coordinate))
    return input3_input_3_external_debt_private_sector_st_external_debt_outstanding


def _check_input3_input_3_external_debt_private_external_debt_interest_due(
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue,
) -> data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue:
    """Validate `input3_input_3_external_debt_private_external_debt_interest_due` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_EXTERNAL_DEBT_INTEREST_DUE.schema.validate(input3_input_3_external_debt_private_external_debt_interest_due)
    input3_input_3_external_debt_private_external_debt_interest_due = coerce_input_measure(input3_input_3_external_debt_private_external_debt_interest_due, dtype="float", series_id="input3_input_3_external_debt_private_external_debt_interest_due")
    for coordinate in data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_EXTERNAL_DEBT_INTEREST_DUE.required:
        require_input_domain(input3_input_3_external_debt_private_external_debt_interest_due[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_external_debt_private_external_debt_interest_due" + repr(coordinate))
    return input3_input_3_external_debt_private_external_debt_interest_due


def _check_input3_input_3_external_debt_private_mlt_external_debt_amortization_due(
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue,
) -> data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue:
    """Validate `input3_input_3_external_debt_private_mlt_external_debt_amortization_due` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_MLT_EXTERNAL_DEBT_AMORTIZATION_DUE.schema.validate(input3_input_3_external_debt_private_mlt_external_debt_amortization_due)
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due = coerce_input_measure(input3_input_3_external_debt_private_mlt_external_debt_amortization_due, dtype="float", series_id="input3_input_3_external_debt_private_mlt_external_debt_amortization_due")
    for coordinate in data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_MLT_EXTERNAL_DEBT_AMORTIZATION_DUE.required:
        require_input_domain(input3_input_3_external_debt_private_mlt_external_debt_amortization_due[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_external_debt_private_mlt_external_debt_amortization_due" + repr(coordinate))
    return input3_input_3_external_debt_private_mlt_external_debt_amortization_due


def _check_input3_input_3_old_debt_service_total_principal_payment(
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment,
) -> data.Input3Input3OldDebtServiceTotalPrincipalPayment:
    """Validate `input3_input_3_old_debt_service_total_principal_payment` before the model reads it."""
    data.INPUT3_INPUT_3_OLD_DEBT_SERVICE_TOTAL_PRINCIPAL_PAYMENT.schema.validate(input3_input_3_old_debt_service_total_principal_payment)
    input3_input_3_old_debt_service_total_principal_payment = coerce_input_measure(input3_input_3_old_debt_service_total_principal_payment, dtype="float", series_id="input3_input_3_old_debt_service_total_principal_payment")
    for coordinate in data.INPUT3_INPUT_3_OLD_DEBT_SERVICE_TOTAL_PRINCIPAL_PAYMENT.required:
        require_input_domain(input3_input_3_old_debt_service_total_principal_payment[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_input_3_old_debt_service_total_principal_payment" + repr(coordinate))
    return input3_input_3_old_debt_service_total_principal_payment


def _check_customized_public_template_anchor(
    customized_public_template_anchor: float | str,
) -> float | str:
    """Validate `customized_public_template_anchor` before the model reads it."""
    customized_public_template_anchor = coerce_input_measure(customized_public_template_anchor, dtype="float", series_id="customized_public_template_anchor")
    require_input_domain(customized_public_template_anchor, {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_public_template_anchor")
    return customized_public_template_anchor


def _check_customized_public_natural_disaster_year(
    customized_public_natural_disaster_year: int | str,
) -> int | str:
    """Validate `customized_public_natural_disaster_year` before the model reads it."""
    customized_public_natural_disaster_year = coerce_input_measure(customized_public_natural_disaster_year, dtype="int", series_id="customized_public_natural_disaster_year")
    require_input_domain(customized_public_natural_disaster_year, {"between": {"min": 0, "max": 50}}, series_id="customized_public_natural_disaster_year")
    return customized_public_natural_disaster_year


def _check_customized_public_external_mlt_disbursement_profile(
    customized_public_external_mlt_disbursement_profile: float | str,
) -> float | str:
    """Validate `customized_public_external_mlt_disbursement_profile` before the model reads it."""
    customized_public_external_mlt_disbursement_profile = coerce_input_measure(customized_public_external_mlt_disbursement_profile, dtype="float", series_id="customized_public_external_mlt_disbursement_profile")
    require_input_domain(customized_public_external_mlt_disbursement_profile, {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_public_external_mlt_disbursement_profile")
    return customized_public_external_mlt_disbursement_profile


def _check_customized_public_new_forex_borrowing_cumulative_overflow(
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow,
) -> data.CustomizedPublicNewForexBorrowingCumulativeOverflow:
    """Validate `customized_public_new_forex_borrowing_cumulative_overflow` before the model reads it."""
    data.CUSTOMIZED_PUBLIC_NEW_FOREX_BORROWING_CUMULATIVE_OVERFLOW.schema.validate(customized_public_new_forex_borrowing_cumulative_overflow)
    customized_public_new_forex_borrowing_cumulative_overflow = coerce_input_measure(customized_public_new_forex_borrowing_cumulative_overflow, dtype="float", series_id="customized_public_new_forex_borrowing_cumulative_overflow")
    for coordinate in data.CUSTOMIZED_PUBLIC_NEW_FOREX_BORROWING_CUMULATIVE_OVERFLOW.required:
        require_input_domain(customized_public_new_forex_borrowing_cumulative_overflow[coordinate], {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_public_new_forex_borrowing_cumulative_overflow" + repr(coordinate))
    return customized_public_new_forex_borrowing_cumulative_overflow


def _check_customized_public_new_domestic_mlt_cumulative_overflow(
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow,
) -> data.CustomizedPublicNewDomesticMltCumulativeOverflow:
    """Validate `customized_public_new_domestic_mlt_cumulative_overflow` before the model reads it."""
    data.CUSTOMIZED_PUBLIC_NEW_DOMESTIC_MLT_CUMULATIVE_OVERFLOW.schema.validate(customized_public_new_domestic_mlt_cumulative_overflow)
    customized_public_new_domestic_mlt_cumulative_overflow = coerce_input_measure(customized_public_new_domestic_mlt_cumulative_overflow, dtype="float", series_id="customized_public_new_domestic_mlt_cumulative_overflow")
    for coordinate in data.CUSTOMIZED_PUBLIC_NEW_DOMESTIC_MLT_CUMULATIVE_OVERFLOW.required:
        require_input_domain(customized_public_new_domestic_mlt_cumulative_overflow[coordinate], {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_public_new_domestic_mlt_cumulative_overflow" + repr(coordinate))
    return customized_public_new_domestic_mlt_cumulative_overflow


def _check_customized_public_residual_overflow(
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow,
) -> data.CustomizedPublicResidualOverflow:
    """Validate `customized_public_residual_overflow` before the model reads it."""
    data.CUSTOMIZED_PUBLIC_RESIDUAL_OVERFLOW.schema.validate(customized_public_residual_overflow)
    customized_public_residual_overflow = coerce_input_measure(customized_public_residual_overflow, dtype="float", series_id="customized_public_residual_overflow")
    for coordinate in data.CUSTOMIZED_PUBLIC_RESIDUAL_OVERFLOW.required:
        require_input_domain(customized_public_residual_overflow[coordinate], {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_public_residual_overflow" + repr(coordinate))
    return customized_public_residual_overflow


def _check_customized_public_new_forex_debt_stock_initial(
    customized_public_new_forex_debt_stock_initial: float | str | None,
) -> float | str | None:
    """Validate `customized_public_new_forex_debt_stock_initial` before the model reads it."""
    customized_public_new_forex_debt_stock_initial = coerce_input_measure(customized_public_new_forex_debt_stock_initial, dtype="float", series_id="customized_public_new_forex_debt_stock_initial")
    require_input_domain(customized_public_new_forex_debt_stock_initial, {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_public_new_forex_debt_stock_initial")
    return customized_public_new_forex_debt_stock_initial


def _check_customized_public_domestic_mlt_interest_initial(
    customized_public_domestic_mlt_interest_initial: float | str,
) -> float | str:
    """Validate `customized_public_domestic_mlt_interest_initial` before the model reads it."""
    customized_public_domestic_mlt_interest_initial = coerce_input_measure(customized_public_domestic_mlt_interest_initial, dtype="float", series_id="customized_public_domestic_mlt_interest_initial")
    require_input_domain(customized_public_domestic_mlt_interest_initial, {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_public_domestic_mlt_interest_initial")
    return customized_public_domestic_mlt_interest_initial


def _check_customized_public_domestic_st_interest_initial(
    customized_public_domestic_st_interest_initial: float | str | None,
) -> float | str | None:
    """Validate `customized_public_domestic_st_interest_initial` before the model reads it."""
    customized_public_domestic_st_interest_initial = coerce_input_measure(customized_public_domestic_st_interest_initial, dtype="float", series_id="customized_public_domestic_st_interest_initial")
    require_input_domain(customized_public_domestic_st_interest_initial, {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_public_domestic_st_interest_initial")
    return customized_public_domestic_st_interest_initial


def _check_customized_external_debt_profile_period(
    customized_external_debt_profile_period: int | str,
) -> int | str:
    """Validate `customized_external_debt_profile_period` before the model reads it."""
    customized_external_debt_profile_period = coerce_input_measure(customized_external_debt_profile_period, dtype="int", series_id="customized_external_debt_profile_period")
    require_input_domain(customized_external_debt_profile_period, {"between": {"min": 0, "max": 50}}, series_id="customized_external_debt_profile_period")
    return customized_external_debt_profile_period


def _check_customized_external_debt_profile_disbursement(
    customized_external_debt_profile_disbursement: float | str,
) -> float | str:
    """Validate `customized_external_debt_profile_disbursement` before the model reads it."""
    customized_external_debt_profile_disbursement = coerce_input_measure(customized_external_debt_profile_disbursement, dtype="float", series_id="customized_external_debt_profile_disbursement")
    require_input_domain(customized_external_debt_profile_disbursement, {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_external_debt_profile_disbursement")
    return customized_external_debt_profile_disbursement


def _check_customized_external_new_forex_borrowing_cumulative_overflow(
    customized_external_new_forex_borrowing_cumulative_overflow: data.CustomizedExternalNewForexBorrowingCumulativeOverflow,
) -> data.CustomizedExternalNewForexBorrowingCumulativeOverflow:
    """Validate `customized_external_new_forex_borrowing_cumulative_overflow` before the model reads it."""
    data.CUSTOMIZED_EXTERNAL_NEW_FOREX_BORROWING_CUMULATIVE_OVERFLOW.schema.validate(customized_external_new_forex_borrowing_cumulative_overflow)
    customized_external_new_forex_borrowing_cumulative_overflow = coerce_input_measure(customized_external_new_forex_borrowing_cumulative_overflow, dtype="float", series_id="customized_external_new_forex_borrowing_cumulative_overflow")
    for coordinate in data.CUSTOMIZED_EXTERNAL_NEW_FOREX_BORROWING_CUMULATIVE_OVERFLOW.required:
        require_input_domain(customized_external_new_forex_borrowing_cumulative_overflow[coordinate], {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="customized_external_new_forex_borrowing_cumulative_overflow" + repr(coordinate))
    return customized_external_new_forex_borrowing_cumulative_overflow


def _check_input8_sdr_stock(input8_sdr_stock: data.Input8SdrStock) -> data.Input8SdrStock:
    """Validate `input8_sdr_stock` before the model reads it."""
    data.INPUT8_SDR_STOCK.schema.validate(input8_sdr_stock)
    input8_sdr_stock = coerce_input_measure(input8_sdr_stock, dtype="float", series_id="input8_sdr_stock")
    for coordinate in data.INPUT8_SDR_STOCK.required:
        require_input_domain(input8_sdr_stock[coordinate], {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="input8_sdr_stock" + repr(coordinate))
    return input8_sdr_stock


def _check_input3_old_debt_service(
    input3_old_debt_service: data.Input3OldDebtService,
) -> data.Input3OldDebtService:
    """Validate `input3_old_debt_service` before the model reads it."""
    data.INPUT3_OLD_DEBT_SERVICE.schema.validate(input3_old_debt_service)
    input3_old_debt_service = coerce_input_measure(input3_old_debt_service, dtype="float", series_id="input3_old_debt_service")
    for coordinate in data.INPUT3_OLD_DEBT_SERVICE.required:
        require_input_domain(input3_old_debt_service[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_old_debt_service" + repr(coordinate))
    return input3_old_debt_service


def _check_input3_new_disbursements(
    input3_new_disbursements: data.Input3NewDisbursements,
) -> data.Input3NewDisbursements:
    """Validate `input3_new_disbursements` before the model reads it."""
    data.INPUT3_NEW_DISBURSEMENTS.schema.validate(input3_new_disbursements)
    input3_new_disbursements = coerce_input_measure(input3_new_disbursements, dtype="float", series_id="input3_new_disbursements")
    for coordinate in data.INPUT3_NEW_DISBURSEMENTS.required:
        require_input_domain(input3_new_disbursements[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_new_disbursements" + repr(coordinate))
    return input3_new_disbursements


def _check_input3_domestic_outstanding_of_existing_debt(
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt,
) -> data.Input3DomesticOutstandingOfExistingDebt:
    """Validate `input3_domestic_outstanding_of_existing_debt` before the model reads it."""
    data.INPUT3_DOMESTIC_OUTSTANDING_OF_EXISTING_DEBT.schema.validate(input3_domestic_outstanding_of_existing_debt)
    input3_domestic_outstanding_of_existing_debt = coerce_input_measure(input3_domestic_outstanding_of_existing_debt, dtype="float", series_id="input3_domestic_outstanding_of_existing_debt")
    for coordinate in data.INPUT3_DOMESTIC_OUTSTANDING_OF_EXISTING_DEBT.required:
        require_input_domain(input3_domestic_outstanding_of_existing_debt[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_domestic_outstanding_of_existing_debt" + repr(coordinate))
    return input3_domestic_outstanding_of_existing_debt


def _check_input3_domestic_o_w_st(
    input3_domestic_o_w_st: data.Input3DomesticOWSt,
) -> data.Input3DomesticOWSt:
    """Validate `input3_domestic_o_w_st` before the model reads it."""
    data.INPUT3_DOMESTIC_O_W_ST.schema.validate(input3_domestic_o_w_st)
    input3_domestic_o_w_st = coerce_input_measure(input3_domestic_o_w_st, dtype="float", series_id="input3_domestic_o_w_st")
    for coordinate in data.INPUT3_DOMESTIC_O_W_ST.required:
        require_input_domain(input3_domestic_o_w_st[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_domestic_o_w_st" + repr(coordinate))
    return input3_domestic_o_w_st


def _check_input3_domestic_interest_payment_from_existing_debt(
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt,
) -> data.Input3DomesticInterestPaymentFromExistingDebt:
    """Validate `input3_domestic_interest_payment_from_existing_debt` before the model reads it."""
    data.INPUT3_DOMESTIC_INTEREST_PAYMENT_FROM_EXISTING_DEBT.schema.validate(input3_domestic_interest_payment_from_existing_debt)
    input3_domestic_interest_payment_from_existing_debt = coerce_input_measure(input3_domestic_interest_payment_from_existing_debt, dtype="float", series_id="input3_domestic_interest_payment_from_existing_debt")
    for coordinate in data.INPUT3_DOMESTIC_INTEREST_PAYMENT_FROM_EXISTING_DEBT.required:
        require_input_domain(input3_domestic_interest_payment_from_existing_debt[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_domestic_interest_payment_from_existing_debt" + repr(coordinate))
    return input3_domestic_interest_payment_from_existing_debt


def _check_input3_domestic_principal_payment_from_existing_debt(
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt,
) -> data.Input3DomesticPrincipalPaymentFromExistingDebt:
    """Validate `input3_domestic_principal_payment_from_existing_debt` before the model reads it."""
    data.INPUT3_DOMESTIC_PRINCIPAL_PAYMENT_FROM_EXISTING_DEBT.schema.validate(input3_domestic_principal_payment_from_existing_debt)
    input3_domestic_principal_payment_from_existing_debt = coerce_input_measure(input3_domestic_principal_payment_from_existing_debt, dtype="float", series_id="input3_domestic_principal_payment_from_existing_debt")
    for coordinate in data.INPUT3_DOMESTIC_PRINCIPAL_PAYMENT_FROM_EXISTING_DEBT.required:
        require_input_domain(input3_domestic_principal_payment_from_existing_debt[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_domestic_principal_payment_from_existing_debt" + repr(coordinate))
    return input3_domestic_principal_payment_from_existing_debt


def _check_input3_domestic_new_gross_disbursement(
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement,
) -> data.Input3DomesticNewGrossDisbursement:
    """Validate `input3_domestic_new_gross_disbursement` before the model reads it."""
    data.INPUT3_DOMESTIC_NEW_GROSS_DISBURSEMENT.schema.validate(input3_domestic_new_gross_disbursement)
    input3_domestic_new_gross_disbursement = coerce_input_measure(input3_domestic_new_gross_disbursement, dtype="float", series_id="input3_domestic_new_gross_disbursement")
    for coordinate in data.INPUT3_DOMESTIC_NEW_GROSS_DISBURSEMENT.required:
        require_input_domain(input3_domestic_new_gross_disbursement[coordinate], {"real_between": {"min": -1000000000000000.0, "max": 1000000000000000.0}}, series_id="input3_domestic_new_gross_disbursement" + repr(coordinate))
    return input3_domestic_new_gross_disbursement


def _check_current_year(current_year: int | str) -> int | str:
    """Validate `current_year` before the model reads it."""
    current_year = coerce_input_measure(current_year, dtype="int", series_id="current_year")
    require_input_domain(current_year, {"between": {"min": 1990, "max": 2100}}, series_id="current_year")
    return current_year


def _check_pv_base_input_output_cumulative(
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative,
) -> data.PvBaseInputOutputCumulative:
    """Validate `pv_base_input_output_cumulative` before the model reads it."""
    data.PV_BASE_INPUT_OUTPUT_CUMULATIVE.schema.validate(pv_base_input_output_cumulative)
    pv_base_input_output_cumulative = coerce_input_measure(pv_base_input_output_cumulative, dtype="float", series_id="pv_base_input_output_cumulative")
    for coordinate in data.PV_BASE_INPUT_OUTPUT_CUMULATIVE.required:
        require_input_domain(pv_base_input_output_cumulative[coordinate], {"real_between": {"min": 0, "max": 1000000000000000.0}}, series_id="pv_base_input_output_cumulative" + repr(coordinate))
    return pv_base_input_output_cumulative


CHECKS = {
    "input4_interest_rate": _check_input4_interest_rate,
    "input4_grace_period": _check_input4_grace_period,
    "input4_loan_maturity": _check_input4_loan_maturity,
    "input4_disbursements": _check_input4_disbursements,
    "input4_instrument_names": _check_input4_instrument_names,
    "input4_blend_variant": _check_input4_blend_variant,
    "input4_blend_scale_key": _check_input4_blend_scale_key,
    "input5_grace_period": _check_input5_grace_period,
    "input5_interest_rate_on_domestic_debt": _check_input5_interest_rate_on_domestic_debt,
    "input5_interest_rate_on_domestic_debt_fx_long": _check_input5_interest_rate_on_domestic_debt_fx_long,
    "input5_maturity": _check_input5_maturity,
    "input5_maturity_central_bank": _check_input5_maturity_central_bank,
    "input5_public_gfns_other_adjustment": _check_input5_public_gfns_other_adjustment,
    "input5_domestic_financing_source": _check_input5_domestic_financing_source,
    "input5_gfn_share": _check_input5_gfn_share,
    "start_working_language": _check_start_working_language,
    "country": _check_country,
    "first_projection_year": _check_first_projection_year,
    "discount_rate": _check_discount_rate,
    "external_domestic_debt_definition": _check_external_domestic_debt_definition,
    "fiscal_space_moderate_assessment_flag": _check_fiscal_space_moderate_assessment_flag,
    "fiscal_space_stock_band": _check_fiscal_space_stock_band,
    "fiscal_space_flow_band": _check_fiscal_space_flow_band,
    "contingent_liability_other_elements_pct_gdp": _check_contingent_liability_other_elements_pct_gdp,
    "contingent_liability_soe_debt_pct_gdp": _check_contingent_liability_soe_debt_pct_gdp,
    "contingent_liability_financial_market_pct_gdp": _check_contingent_liability_financial_market_pct_gdp,
    "ppp_capital_stock_shock_pct": _check_ppp_capital_stock_shock_pct,
    "customized_public_delta": _check_customized_public_delta,
    "blend_ida_new_floating_currency": _check_blend_ida_new_floating_currency,
    "input_1_rer_overvaluation": _check_input_1_rer_overvaluation,
    "customized_public_include_scenario": _check_customized_public_include_scenario,
    "input6_commodity_group_relevant": _check_input6_commodity_group_relevant,
    "input8_sdr_interest_historical": _check_input8_sdr_interest_historical,
    "input8_sdr_interest": _check_input8_sdr_interest,
    "input8_sdr_interest_rate": _check_input8_sdr_interest_rate,
    "input6_tailored_tests_enabled": _check_input6_tailored_tests_enabled,
    "input6_standard_size_threshold_mode": _check_input6_standard_size_threshold_mode,
    "input6_standard_interactions": _check_input6_standard_interactions,
    "input6_standard_user_defined_threshold": _check_input6_standard_user_defined_threshold,
    "input3_input_3_macro_gross_domestic_product_us_dollars": _check_input3_input_3_macro_gross_domestic_product_us_dollars,
    "input3_input_3_macro_real_gross_domestic_product": _check_input3_input_3_macro_real_gross_domestic_product,
    "input3_input_3_macro_u_s_deflator": _check_input3_input_3_macro_u_s_deflator,
    "input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p": _check_input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p,
    "input3_input_3_macro_national_currency_per_u_s_dollar_p_a": _check_input3_input_3_macro_national_currency_per_u_s_dollar_p_a,
    "input3_input_3_macro_government_revenue_and_grants": _check_input3_input_3_macro_government_revenue_and_grants,
    "input3_input_3_macro_government_grants": _check_input3_input_3_macro_government_grants,
    "in3_macro_government_primary_expenditures_this_used_be": _check_in3_macro_government_primary_expenditures_this_used_be,
    "in3_macro_public_sector_liquid_assets_stock_e_g_cash": _check_in3_macro_public_sector_liquid_assets_stock_e_g_cash,
    "in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g": _check_in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g,
    "input3_input_3_macro_privatization_proceeds": _check_input3_input_3_macro_privatization_proceeds,
    "in3_macro_recognition_of_contingent_liab_e_g_bank": _check_in3_macro_recognition_of_contingent_liab_e_g_bank,
    "input3_input_3_macro_debt_relief_non_multilateral_hipc": _check_input3_input_3_macro_debt_relief_non_multilateral_hipc,
    "input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify": _check_input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify,
    "input3_input_3_macro_current_account": _check_input3_input_3_macro_current_account,
    "input3_input_3_macro_exports_of_goods_and_services": _check_input3_input_3_macro_exports_of_goods_and_services,
    "input3_input_3_macro_exports_commodity_fuel": _check_input3_input_3_macro_exports_commodity_fuel,
    "input3_input_3_macro_exports_commodity_non_fuel": _check_input3_input_3_macro_exports_commodity_non_fuel,
    "input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number": _check_input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number,
    "input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number": _check_input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number,
    "input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number": _check_input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number,
    "input3_input_3_macro_current_transfers_net": _check_input3_input_3_macro_current_transfers_net,
    "input3_input_3_macro_foreign_direct_investment": _check_input3_input_3_macro_foreign_direct_investment,
    "input3_input_3_external_debt_ppg_mlt_external_debt_outstanding": _check_input3_input_3_external_debt_ppg_mlt_external_debt_outstanding,
    "input3_input_3_external_debt_ppg_st_external_debt_outstanding": _check_input3_input_3_external_debt_ppg_st_external_debt_outstanding,
    "input3_input_3_external_debt_ppg_external_debt_interest_due": _check_input3_input_3_external_debt_ppg_external_debt_interest_due,
    "input3_input_3_external_debt_ppg_external_arrears": _check_input3_input_3_external_debt_ppg_external_arrears,
    "input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding": _check_input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding,
    "input3_input_3_external_debt_private_sector_st_external_debt_outstanding": _check_input3_input_3_external_debt_private_sector_st_external_debt_outstanding,
    "input3_input_3_external_debt_private_external_debt_interest_due": _check_input3_input_3_external_debt_private_external_debt_interest_due,
    "input3_input_3_external_debt_private_mlt_external_debt_amortization_due": _check_input3_input_3_external_debt_private_mlt_external_debt_amortization_due,
    "input3_input_3_old_debt_service_total_principal_payment": _check_input3_input_3_old_debt_service_total_principal_payment,
    "customized_public_template_anchor": _check_customized_public_template_anchor,
    "customized_public_natural_disaster_year": _check_customized_public_natural_disaster_year,
    "customized_public_external_mlt_disbursement_profile": _check_customized_public_external_mlt_disbursement_profile,
    "customized_public_new_forex_borrowing_cumulative_overflow": _check_customized_public_new_forex_borrowing_cumulative_overflow,
    "customized_public_new_domestic_mlt_cumulative_overflow": _check_customized_public_new_domestic_mlt_cumulative_overflow,
    "customized_public_residual_overflow": _check_customized_public_residual_overflow,
    "customized_public_new_forex_debt_stock_initial": _check_customized_public_new_forex_debt_stock_initial,
    "customized_public_domestic_mlt_interest_initial": _check_customized_public_domestic_mlt_interest_initial,
    "customized_public_domestic_st_interest_initial": _check_customized_public_domestic_st_interest_initial,
    "customized_external_debt_profile_period": _check_customized_external_debt_profile_period,
    "customized_external_debt_profile_disbursement": _check_customized_external_debt_profile_disbursement,
    "customized_external_new_forex_borrowing_cumulative_overflow": _check_customized_external_new_forex_borrowing_cumulative_overflow,
    "input8_sdr_stock": _check_input8_sdr_stock,
    "input3_old_debt_service": _check_input3_old_debt_service,
    "input3_new_disbursements": _check_input3_new_disbursements,
    "input3_domestic_outstanding_of_existing_debt": _check_input3_domestic_outstanding_of_existing_debt,
    "input3_domestic_o_w_st": _check_input3_domestic_o_w_st,
    "input3_domestic_interest_payment_from_existing_debt": _check_input3_domestic_interest_payment_from_existing_debt,
    "input3_domestic_principal_payment_from_existing_debt": _check_input3_domestic_principal_payment_from_existing_debt,
    "input3_domestic_new_gross_disbursement": _check_input3_domestic_new_gross_disbursement,
    "current_year": _check_current_year,
    "pv_base_input_output_cumulative": _check_pv_base_input_output_cumulative,
}
