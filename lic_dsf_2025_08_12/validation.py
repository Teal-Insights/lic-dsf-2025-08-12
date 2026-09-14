"""Input schema, domain, and value-map checks for bound Model arguments."""

from __future__ import annotations

from . import data
from .excel import require_input_domain


def _check_input4_interest_rate(
    input4_interest_rate: data.Input4InterestRate,
) -> data.Input4InterestRate:
    """Validate `input4_interest_rate` before the model reads it."""
    data.INPUT4_INTEREST_RATE_SCHEMA.validate(input4_interest_rate)
    return input4_interest_rate


def _check_input4_grace_period(
    input4_grace_period: data.Input4GracePeriod,
) -> data.Input4GracePeriod:
    """Validate `input4_grace_period` before the model reads it."""
    data.INPUT4_GRACE_PERIOD_SCHEMA.validate(input4_grace_period)
    for coordinate in data.INPUT4_GRACE_PERIOD_REQUIRED:
        require_input_domain(input4_grace_period[coordinate], {"between": {"min": 0, "max": 50}}, series_id="input4_grace_period" + repr(coordinate))
    return input4_grace_period


def _check_input4_loan_maturity(
    input4_loan_maturity: data.Input4LoanMaturity,
) -> data.Input4LoanMaturity:
    """Validate `input4_loan_maturity` before the model reads it."""
    data.INPUT4_LOAN_MATURITY_SCHEMA.validate(input4_loan_maturity)
    for coordinate in data.INPUT4_LOAN_MATURITY_REQUIRED:
        require_input_domain(input4_loan_maturity[coordinate], {"between": {"min": 0, "max": 80}}, series_id="input4_loan_maturity" + repr(coordinate))
    return input4_loan_maturity


def _check_input4_disbursements(
    input4_disbursements: data.Input4Disbursements,
) -> data.Input4Disbursements:
    """Validate `input4_disbursements` before the model reads it."""
    data.INPUT4_DISBURSEMENTS_SCHEMA.validate(input4_disbursements)
    return input4_disbursements


def _check_input4_instrument_names(
    input4_instrument_names: data.Input4InstrumentNames,
) -> data.Input4InstrumentNames:
    """Validate `input4_instrument_names` before the model reads it."""
    data.INPUT4_INSTRUMENT_NAMES_SCHEMA.validate(input4_instrument_names)
    return input4_instrument_names


def _check_input4_blend_scale_key(
    input4_blend_scale_key: data.Input4BlendScaleKey,
) -> data.Input4BlendScaleKey:
    """Validate `input4_blend_scale_key` before the model reads it."""
    data.INPUT4_BLEND_SCALE_KEY_SCHEMA.validate(input4_blend_scale_key)
    return input4_blend_scale_key


def _check_input5_grace_period(
    input5_grace_period: data.Input5GracePeriod,
) -> data.Input5GracePeriod:
    """Validate `input5_grace_period` before the model reads it."""
    data.INPUT5_GRACE_PERIOD_SCHEMA.validate(input5_grace_period)
    for coordinate in data.INPUT5_GRACE_PERIOD_REQUIRED:
        require_input_domain(input5_grace_period[coordinate], {"between": {"min": 0, "max": 50}}, series_id="input5_grace_period" + repr(coordinate))
    return input5_grace_period


def _check_input5_interest_rate_on_domestic_debt(
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt,
) -> data.Input5InterestRateOnDomesticDebt:
    """Validate `input5_interest_rate_on_domestic_debt` before the model reads it."""
    data.INPUT5_INTEREST_RATE_ON_DOMESTIC_DEBT_SCHEMA.validate(input5_interest_rate_on_domestic_debt)
    return input5_interest_rate_on_domestic_debt


def _check_input5_maturity(input5_maturity: data.Input5Maturity) -> data.Input5Maturity:
    """Validate `input5_maturity` before the model reads it."""
    data.INPUT5_MATURITY_SCHEMA.validate(input5_maturity)
    return input5_maturity


def _check_input5_public_gfns_other_adjustment(
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment,
) -> data.Input5PublicGfnsOtherAdjustment:
    """Validate `input5_public_gfns_other_adjustment` before the model reads it."""
    data.INPUT5_PUBLIC_GFNS_OTHER_ADJUSTMENT_SCHEMA.validate(input5_public_gfns_other_adjustment)
    return input5_public_gfns_other_adjustment


def _check_input5_domestic_financing_source(
    input5_domestic_financing_source: int | str,
) -> int | str:
    """Validate `input5_domestic_financing_source` before the model reads it."""
    require_input_domain(input5_domestic_financing_source, {"enum": frozenset({0, 1})}, series_id="input5_domestic_financing_source")
    return input5_domestic_financing_source


def _check_input5_gfn_share(input5_gfn_share: data.Input5GfnShare) -> data.Input5GfnShare:
    """Validate `input5_gfn_share` before the model reads it."""
    data.INPUT5_GFN_SHARE_SCHEMA.validate(input5_gfn_share)
    for coordinate in data.INPUT5_GFN_SHARE_REQUIRED:
        require_input_domain(input5_gfn_share[coordinate], {"real_between": {"min": 0, "max": 1}}, series_id="input5_gfn_share" + repr(coordinate))
    return input5_gfn_share


def _check_country(country: str) -> str:
    """Validate `country` before the model reads it."""
    require_input_domain(country, {"enum": frozenset({"Cote d'Ivoire", "Afghanistan", "Bangladesh", "Benin", "Bhutan", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo, DR", "Congo, Republic of", "Djibouti", "Dominica", "Eritrea", "Ethiopia", "Gambia, The", "Ghana", "Grenada", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Kenya", "Kiribati", "Kyrgyz Republic", "Lao PDR", "Lesotho", "Liberia", "Madagascar", "Malawi", "Maldives", "Mali", "Marshall Islands", "Mauritania", "Micronesia", "Moldova", "Mozambique", "Myanmar", "Nepal", "Nicaragua", "Niger", "Papua New Guinea", "Rwanda", "Samoa", "Sao Tome & Principe", "Senegal", "Sierra Leone", "Solomon Islands", "Somalia", "South Sudan", "St. Lucia", "St. Vincent & the Grenadines", "Sudan", "Tajikistan", "Tanzania", "Timor-Leste", "Togo", "Tonga", "Tuvalu", "Uganda", "Uzbekistan", "Vanuatu", "Yemen, Republic of", "Zambia", "Zimbabwe"})}, series_id="country")
    return country


def _check_first_projection_year(first_projection_year: int | str) -> int | str:
    """Validate `first_projection_year` before the model reads it."""
    require_input_domain(first_projection_year, {"between": {"min": 1990, "max": 2100}}, series_id="first_projection_year")
    return first_projection_year


def _check_discount_rate(discount_rate: float | str) -> float | str:
    """Validate `discount_rate` before the model reads it."""
    require_input_domain(discount_rate, {"real_between": {"min": 0, "max": 1}}, series_id="discount_rate")
    return discount_rate


def _check_external_domestic_debt_definition(external_domestic_debt_definition: str) -> str:
    """Validate `external_domestic_debt_definition` before the model reads it."""
    require_input_domain(external_domestic_debt_definition, {"enum": frozenset({"Currency-based", "Residency-based"})}, series_id="external_domestic_debt_definition")
    return external_domestic_debt_definition


def _check_fiscal_space_moderate_assessment_flag(
    fiscal_space_moderate_assessment_flag: int | str,
) -> int | str:
    """Validate `fiscal_space_moderate_assessment_flag` before the model reads it."""
    require_input_domain(fiscal_space_moderate_assessment_flag, {"between": {"min": 0, "max": 1}}, series_id="fiscal_space_moderate_assessment_flag")
    return fiscal_space_moderate_assessment_flag


def _check_fiscal_space_stock_band(
    fiscal_space_stock_band: data.FiscalSpaceStockBand,
) -> data.FiscalSpaceStockBand:
    """Validate `fiscal_space_stock_band` before the model reads it."""
    data.FISCAL_SPACE_STOCK_BAND_SCHEMA.validate(fiscal_space_stock_band)
    for coordinate in data.FISCAL_SPACE_STOCK_BAND_REQUIRED:
        require_input_domain(fiscal_space_stock_band[coordinate], {"real_between": {"min": 0, "max": 100}}, series_id="fiscal_space_stock_band" + repr(coordinate))
    return fiscal_space_stock_band


def _check_fiscal_space_flow_band(
    fiscal_space_flow_band: data.FiscalSpaceFlowBand,
) -> data.FiscalSpaceFlowBand:
    """Validate `fiscal_space_flow_band` before the model reads it."""
    data.FISCAL_SPACE_FLOW_BAND_SCHEMA.validate(fiscal_space_flow_band)
    for coordinate in data.FISCAL_SPACE_FLOW_BAND_REQUIRED:
        require_input_domain(fiscal_space_flow_band[coordinate], {"real_between": {"min": 0, "max": 100}}, series_id="fiscal_space_flow_band" + repr(coordinate))
    return fiscal_space_flow_band


def _check_customized_public_delta(
    customized_public_delta: data.CustomizedPublicDelta,
) -> data.CustomizedPublicDelta:
    """Validate `customized_public_delta` before the model reads it."""
    data.CUSTOMIZED_PUBLIC_DELTA_SCHEMA.validate(customized_public_delta)
    return customized_public_delta


def _check_blend_ida_new_floating_currency(blend_ida_new_floating_currency: str) -> str:
    """Validate `blend_ida_new_floating_currency` before the model reads it."""
    require_input_domain(blend_ida_new_floating_currency, {"enum": frozenset({"EUR", "GBP", "JPY", "USD"})}, series_id="blend_ida_new_floating_currency")
    return blend_ida_new_floating_currency


def _check_input_1_rer_overvaluation(input_1_rer_overvaluation: float | str) -> float | str:
    """Validate `input_1_rer_overvaluation` before the model reads it."""
    require_input_domain(input_1_rer_overvaluation, {"real_between": {"min": -100, "max": 100}}, series_id="input_1_rer_overvaluation")
    return input_1_rer_overvaluation


def _check_customized_public_include_scenario(customized_public_include_scenario: str) -> str:
    """Validate `customized_public_include_scenario` before the model reads it."""
    require_input_domain(customized_public_include_scenario, {"enum": frozenset({"No", "Yes"})}, series_id="customized_public_include_scenario")
    return customized_public_include_scenario


def _check_input6_commodity_group_relevant(
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant,
) -> data.Input6CommodityGroupRelevant:
    """Validate `input6_commodity_group_relevant` before the model reads it."""
    data.INPUT6_COMMODITY_GROUP_RELEVANT_SCHEMA.validate(input6_commodity_group_relevant)
    for coordinate in data.INPUT6_COMMODITY_GROUP_RELEVANT_REQUIRED:
        require_input_domain(input6_commodity_group_relevant[coordinate], {"enum": frozenset({"No", "Yes"})}, series_id="input6_commodity_group_relevant" + repr(coordinate))
    return input6_commodity_group_relevant


def _check_input8_sdr_interest_rate(
    input8_sdr_interest_rate: data.Input8SdrInterestRate,
) -> data.Input8SdrInterestRate:
    """Validate `input8_sdr_interest_rate` before the model reads it."""
    data.INPUT8_SDR_INTEREST_RATE_SCHEMA.validate(input8_sdr_interest_rate)
    return input8_sdr_interest_rate


def _check_input6_tailored_tests_enabled(input6_tailored_tests_enabled: str) -> str:
    """Validate `input6_tailored_tests_enabled` before the model reads it."""
    require_input_domain(input6_tailored_tests_enabled, {"enum": frozenset({"Off", "On"})}, series_id="input6_tailored_tests_enabled")
    return input6_tailored_tests_enabled


def _check_input6_standard_interactions(input6_standard_interactions: str) -> str:
    """Validate `input6_standard_interactions` before the model reads it."""
    require_input_domain(input6_standard_interactions, {"enum": frozenset({"Off", "On"})}, series_id="input6_standard_interactions")
    return input6_standard_interactions


def _check_input6_standard_user_defined_threshold(
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold,
) -> data.Input6StandardUserDefinedThreshold:
    """Validate `input6_standard_user_defined_threshold` before the model reads it."""
    data.INPUT6_STANDARD_USER_DEFINED_THRESHOLD_SCHEMA.validate(input6_standard_user_defined_threshold)
    for coordinate in data.INPUT6_STANDARD_USER_DEFINED_THRESHOLD_REQUIRED:
        require_input_domain(input6_standard_user_defined_threshold[coordinate], {"enum": frozenset({"Baseline projection only", "Historical average only", "Whichever is lower"})}, series_id="input6_standard_user_defined_threshold" + repr(coordinate))
    return input6_standard_user_defined_threshold


def _check_input3_input_3_macro_gross_domestic_product_us_dollars(
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars,
) -> data.Input3Input3MacroGrossDomesticProductUsDollars:
    """Validate `input3_input_3_macro_gross_domestic_product_us_dollars` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_GROSS_DOMESTIC_PRODUCT_US_DOLLARS_SCHEMA.validate(input3_input_3_macro_gross_domestic_product_us_dollars)
    return input3_input_3_macro_gross_domestic_product_us_dollars


def _check_input3_input_3_macro_real_gross_domestic_product(
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct,
) -> data.Input3Input3MacroRealGrossDomesticProduct:
    """Validate `input3_input_3_macro_real_gross_domestic_product` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_REAL_GROSS_DOMESTIC_PRODUCT_SCHEMA.validate(input3_input_3_macro_real_gross_domestic_product)
    return input3_input_3_macro_real_gross_domestic_product


def _check_input3_input_3_macro_u_s_deflator(
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator,
) -> data.Input3Input3MacroUSDeflator:
    """Validate `input3_input_3_macro_u_s_deflator` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_U_S_DEFLATOR_SCHEMA.validate(input3_input_3_macro_u_s_deflator)
    return input3_input_3_macro_u_s_deflator


def _check_input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p(
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP,
) -> data.Input3Input3MacroNationalCurrencyPerUSDollarEOP:
    """Validate `input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_NATIONAL_CURRENCY_PER_U_S_DOLLAR_E_O_P_SCHEMA.validate(input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p)
    return input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p


def _check_input3_input_3_macro_national_currency_per_u_s_dollar_p_a(
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA,
) -> data.Input3Input3MacroNationalCurrencyPerUSDollarPA:
    """Validate `input3_input_3_macro_national_currency_per_u_s_dollar_p_a` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_NATIONAL_CURRENCY_PER_U_S_DOLLAR_P_A_SCHEMA.validate(input3_input_3_macro_national_currency_per_u_s_dollar_p_a)
    return input3_input_3_macro_national_currency_per_u_s_dollar_p_a


def _check_input3_input_3_macro_government_revenue_and_grants(
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants,
) -> data.Input3Input3MacroGovernmentRevenueAndGrants:
    """Validate `input3_input_3_macro_government_revenue_and_grants` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_GOVERNMENT_REVENUE_AND_GRANTS_SCHEMA.validate(input3_input_3_macro_government_revenue_and_grants)
    return input3_input_3_macro_government_revenue_and_grants


def _check_input3_input_3_macro_government_grants(
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants,
) -> data.Input3Input3MacroGovernmentGrants:
    """Validate `input3_input_3_macro_government_grants` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_GOVERNMENT_GRANTS_SCHEMA.validate(input3_input_3_macro_government_grants)
    return input3_input_3_macro_government_grants


def _check_in3_macro_government_primary_expenditures_this_used_be(
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe,
) -> data.In3MacroGovernmentPrimaryExpendituresThisUsedBe:
    """Validate `in3_macro_government_primary_expenditures_this_used_be` before the model reads it."""
    data.IN3_MACRO_GOVERNMENT_PRIMARY_EXPENDITURES_THIS_USED_BE_SCHEMA.validate(in3_macro_government_primary_expenditures_this_used_be)
    return in3_macro_government_primary_expenditures_this_used_be


def _check_in3_macro_public_sector_liquid_assets_stock_e_g_cash(
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash,
) -> data.In3MacroPublicSectorLiquidAssetsStockEGCash:
    """Validate `in3_macro_public_sector_liquid_assets_stock_e_g_cash` before the model reads it."""
    data.IN3_MACRO_PUBLIC_SECTOR_LIQUID_ASSETS_STOCK_E_G_CASH_SCHEMA.validate(in3_macro_public_sector_liquid_assets_stock_e_g_cash)
    return in3_macro_public_sector_liquid_assets_stock_e_g_cash


def _check_in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g(
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG,
) -> data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG:
    """Validate `in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g` before the model reads it."""
    data.IN3_MACRO_LIQUID_FINANCIAL_ASSETS_USED_MEET_GFNS_FLOW_E_G_SCHEMA.validate(in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g)
    return in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g


def _check_input3_input_3_macro_privatization_proceeds(
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds,
) -> data.Input3Input3MacroPrivatizationProceeds:
    """Validate `input3_input_3_macro_privatization_proceeds` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_PRIVATIZATION_PROCEEDS_SCHEMA.validate(input3_input_3_macro_privatization_proceeds)
    return input3_input_3_macro_privatization_proceeds


def _check_in3_macro_recognition_of_contingent_liab_e_g_bank(
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank,
) -> data.In3MacroRecognitionOfContingentLiabEGBank:
    """Validate `in3_macro_recognition_of_contingent_liab_e_g_bank` before the model reads it."""
    data.IN3_MACRO_RECOGNITION_OF_CONTINGENT_LIAB_E_G_BANK_SCHEMA.validate(in3_macro_recognition_of_contingent_liab_e_g_bank)
    return in3_macro_recognition_of_contingent_liab_e_g_bank


def _check_input3_input_3_macro_debt_relief_non_multilateral_hipc(
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc,
) -> data.Input3Input3MacroDebtReliefNonMultilateralHipc:
    """Validate `input3_input_3_macro_debt_relief_non_multilateral_hipc` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_DEBT_RELIEF_NON_MULTILATERAL_HIPC_SCHEMA.validate(input3_input_3_macro_debt_relief_non_multilateral_hipc)
    return input3_input_3_macro_debt_relief_non_multilateral_hipc


def _check_input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify(
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify,
) -> data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify:
    """Validate `input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_OTHER_DEBT_CREATING_OR_REDUCING_FLOW_PLEASE_SPECIFY_SCHEMA.validate(input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify)
    return input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify


def _check_input3_input_3_macro_current_account(
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount,
) -> data.Input3Input3MacroCurrentAccount:
    """Validate `input3_input_3_macro_current_account` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_CURRENT_ACCOUNT_SCHEMA.validate(input3_input_3_macro_current_account)
    return input3_input_3_macro_current_account


def _check_input3_input_3_macro_exports_of_goods_and_services(
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices,
) -> data.Input3Input3MacroExportsOfGoodsAndServices:
    """Validate `input3_input_3_macro_exports_of_goods_and_services` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_EXPORTS_OF_GOODS_AND_SERVICES_SCHEMA.validate(input3_input_3_macro_exports_of_goods_and_services)
    return input3_input_3_macro_exports_of_goods_and_services


def _check_input3_input_3_macro_exports_commodity_fuel(
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel,
) -> data.Input3Input3MacroExportsCommodityFuel:
    """Validate `input3_input_3_macro_exports_commodity_fuel` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_EXPORTS_COMMODITY_FUEL_SCHEMA.validate(input3_input_3_macro_exports_commodity_fuel)
    return input3_input_3_macro_exports_commodity_fuel


def _check_input3_input_3_macro_exports_commodity_non_fuel(
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel,
) -> data.Input3Input3MacroExportsCommodityNonFuel:
    """Validate `input3_input_3_macro_exports_commodity_non_fuel` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_EXPORTS_COMMODITY_NON_FUEL_SCHEMA.validate(input3_input_3_macro_exports_commodity_non_fuel)
    return input3_input_3_macro_exports_commodity_non_fuel


def _check_input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number(
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber,
) -> data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber:
    """Validate `input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_IMPORTS_OF_GOODS_AND_SERVICES_ENTER_AS_A_POSITIVE_NUMBER_SCHEMA.validate(input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number)
    return input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number


def _check_input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number(
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber,
) -> data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber:
    """Validate `input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_IMPORTS_COMMODITY_FUEL_ENTER_AS_A_POSITIVE_NUMBER_SCHEMA.validate(input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number)
    return input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number


def _check_input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number(
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber,
) -> data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber:
    """Validate `input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_IMPORTS_COMMODITY_NON_FUEL_ENTER_AS_A_POSITIVE_NUMBER_SCHEMA.validate(input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number)
    return input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number


def _check_input3_input_3_macro_current_transfers_net(
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet,
) -> data.Input3Input3MacroCurrentTransfersNet:
    """Validate `input3_input_3_macro_current_transfers_net` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_CURRENT_TRANSFERS_NET_SCHEMA.validate(input3_input_3_macro_current_transfers_net)
    return input3_input_3_macro_current_transfers_net


def _check_input3_input_3_macro_foreign_direct_investment(
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment,
) -> data.Input3Input3MacroForeignDirectInvestment:
    """Validate `input3_input_3_macro_foreign_direct_investment` before the model reads it."""
    data.INPUT3_INPUT_3_MACRO_FOREIGN_DIRECT_INVESTMENT_SCHEMA.validate(input3_input_3_macro_foreign_direct_investment)
    return input3_input_3_macro_foreign_direct_investment


def _check_input3_input_3_external_debt_ppg_mlt_external_debt_outstanding(
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding,
) -> data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding:
    """Validate `input3_input_3_external_debt_ppg_mlt_external_debt_outstanding` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_MLT_EXTERNAL_DEBT_OUTSTANDING_SCHEMA.validate(input3_input_3_external_debt_ppg_mlt_external_debt_outstanding)
    return input3_input_3_external_debt_ppg_mlt_external_debt_outstanding


def _check_input3_input_3_external_debt_ppg_st_external_debt_outstanding(
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding,
) -> data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding:
    """Validate `input3_input_3_external_debt_ppg_st_external_debt_outstanding` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_ST_EXTERNAL_DEBT_OUTSTANDING_SCHEMA.validate(input3_input_3_external_debt_ppg_st_external_debt_outstanding)
    return input3_input_3_external_debt_ppg_st_external_debt_outstanding


def _check_input3_input_3_external_debt_ppg_external_debt_interest_due(
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue,
) -> data.Input3Input3ExternalDebtPpgExternalDebtInterestDue:
    """Validate `input3_input_3_external_debt_ppg_external_debt_interest_due` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_EXTERNAL_DEBT_INTEREST_DUE_SCHEMA.validate(input3_input_3_external_debt_ppg_external_debt_interest_due)
    return input3_input_3_external_debt_ppg_external_debt_interest_due


def _check_input3_input_3_external_debt_ppg_external_arrears(
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears,
) -> data.Input3Input3ExternalDebtPpgExternalArrears:
    """Validate `input3_input_3_external_debt_ppg_external_arrears` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_EXTERNAL_ARREARS_SCHEMA.validate(input3_input_3_external_debt_ppg_external_arrears)
    return input3_input_3_external_debt_ppg_external_arrears


def _check_input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding(
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding,
) -> data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding:
    """Validate `input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_SECTOR_MLT_EXTERNAL_DEBT_OUTSTANDING_SCHEMA.validate(input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding)
    return input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding


def _check_input3_input_3_external_debt_private_sector_st_external_debt_outstanding(
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding,
) -> data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding:
    """Validate `input3_input_3_external_debt_private_sector_st_external_debt_outstanding` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_SECTOR_ST_EXTERNAL_DEBT_OUTSTANDING_SCHEMA.validate(input3_input_3_external_debt_private_sector_st_external_debt_outstanding)
    return input3_input_3_external_debt_private_sector_st_external_debt_outstanding


def _check_input3_input_3_external_debt_private_external_debt_interest_due(
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue,
) -> data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue:
    """Validate `input3_input_3_external_debt_private_external_debt_interest_due` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_EXTERNAL_DEBT_INTEREST_DUE_SCHEMA.validate(input3_input_3_external_debt_private_external_debt_interest_due)
    return input3_input_3_external_debt_private_external_debt_interest_due


def _check_input3_input_3_external_debt_private_mlt_external_debt_amortization_due(
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue,
) -> data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue:
    """Validate `input3_input_3_external_debt_private_mlt_external_debt_amortization_due` before the model reads it."""
    data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_MLT_EXTERNAL_DEBT_AMORTIZATION_DUE_SCHEMA.validate(input3_input_3_external_debt_private_mlt_external_debt_amortization_due)
    return input3_input_3_external_debt_private_mlt_external_debt_amortization_due


def _check_input3_input_3_old_debt_service_total_principal_payment(
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment,
) -> data.Input3Input3OldDebtServiceTotalPrincipalPayment:
    """Validate `input3_input_3_old_debt_service_total_principal_payment` before the model reads it."""
    data.INPUT3_INPUT_3_OLD_DEBT_SERVICE_TOTAL_PRINCIPAL_PAYMENT_SCHEMA.validate(input3_input_3_old_debt_service_total_principal_payment)
    return input3_input_3_old_debt_service_total_principal_payment


def _check_customized_public_new_forex_borrowing_cumulative_overflow(
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow,
) -> data.CustomizedPublicNewForexBorrowingCumulativeOverflow:
    """Validate `customized_public_new_forex_borrowing_cumulative_overflow` before the model reads it."""
    data.CUSTOMIZED_PUBLIC_NEW_FOREX_BORROWING_CUMULATIVE_OVERFLOW_SCHEMA.validate(customized_public_new_forex_borrowing_cumulative_overflow)
    return customized_public_new_forex_borrowing_cumulative_overflow


def _check_customized_public_new_domestic_mlt_cumulative_overflow(
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow,
) -> data.CustomizedPublicNewDomesticMltCumulativeOverflow:
    """Validate `customized_public_new_domestic_mlt_cumulative_overflow` before the model reads it."""
    data.CUSTOMIZED_PUBLIC_NEW_DOMESTIC_MLT_CUMULATIVE_OVERFLOW_SCHEMA.validate(customized_public_new_domestic_mlt_cumulative_overflow)
    return customized_public_new_domestic_mlt_cumulative_overflow


def _check_customized_public_residual_overflow(
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow,
) -> data.CustomizedPublicResidualOverflow:
    """Validate `customized_public_residual_overflow` before the model reads it."""
    data.CUSTOMIZED_PUBLIC_RESIDUAL_OVERFLOW_SCHEMA.validate(customized_public_residual_overflow)
    return customized_public_residual_overflow


def _check_customized_external_new_forex_borrowing_cumulative_overflow(
    customized_external_new_forex_borrowing_cumulative_overflow: data.CustomizedExternalNewForexBorrowingCumulativeOverflow,
) -> data.CustomizedExternalNewForexBorrowingCumulativeOverflow:
    """Validate `customized_external_new_forex_borrowing_cumulative_overflow` before the model reads it."""
    data.CUSTOMIZED_EXTERNAL_NEW_FOREX_BORROWING_CUMULATIVE_OVERFLOW_SCHEMA.validate(customized_external_new_forex_borrowing_cumulative_overflow)
    return customized_external_new_forex_borrowing_cumulative_overflow


def _check_input8_sdr_stock(input8_sdr_stock: data.Input8SdrStock) -> data.Input8SdrStock:
    """Validate `input8_sdr_stock` before the model reads it."""
    data.INPUT8_SDR_STOCK_SCHEMA.validate(input8_sdr_stock)
    return input8_sdr_stock


def _check_input3_old_debt_service(
    input3_old_debt_service: data.Input3OldDebtService,
) -> data.Input3OldDebtService:
    """Validate `input3_old_debt_service` before the model reads it."""
    data.INPUT3_OLD_DEBT_SERVICE_SCHEMA.validate(input3_old_debt_service)
    return input3_old_debt_service


def _check_input3_new_disbursements(
    input3_new_disbursements: data.Input3NewDisbursements,
) -> data.Input3NewDisbursements:
    """Validate `input3_new_disbursements` before the model reads it."""
    data.INPUT3_NEW_DISBURSEMENTS_SCHEMA.validate(input3_new_disbursements)
    return input3_new_disbursements


def _check_input3_domestic_outstanding_of_existing_debt(
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt,
) -> data.Input3DomesticOutstandingOfExistingDebt:
    """Validate `input3_domestic_outstanding_of_existing_debt` before the model reads it."""
    data.INPUT3_DOMESTIC_OUTSTANDING_OF_EXISTING_DEBT_SCHEMA.validate(input3_domestic_outstanding_of_existing_debt)
    return input3_domestic_outstanding_of_existing_debt


def _check_input3_domestic_o_w_st(
    input3_domestic_o_w_st: data.Input3DomesticOWSt,
) -> data.Input3DomesticOWSt:
    """Validate `input3_domestic_o_w_st` before the model reads it."""
    data.INPUT3_DOMESTIC_O_W_ST_SCHEMA.validate(input3_domestic_o_w_st)
    return input3_domestic_o_w_st


def _check_input3_domestic_interest_payment_from_existing_debt(
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt,
) -> data.Input3DomesticInterestPaymentFromExistingDebt:
    """Validate `input3_domestic_interest_payment_from_existing_debt` before the model reads it."""
    data.INPUT3_DOMESTIC_INTEREST_PAYMENT_FROM_EXISTING_DEBT_SCHEMA.validate(input3_domestic_interest_payment_from_existing_debt)
    return input3_domestic_interest_payment_from_existing_debt


def _check_input3_domestic_principal_payment_from_existing_debt(
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt,
) -> data.Input3DomesticPrincipalPaymentFromExistingDebt:
    """Validate `input3_domestic_principal_payment_from_existing_debt` before the model reads it."""
    data.INPUT3_DOMESTIC_PRINCIPAL_PAYMENT_FROM_EXISTING_DEBT_SCHEMA.validate(input3_domestic_principal_payment_from_existing_debt)
    return input3_domestic_principal_payment_from_existing_debt


def _check_input3_domestic_new_gross_disbursement(
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement,
) -> data.Input3DomesticNewGrossDisbursement:
    """Validate `input3_domestic_new_gross_disbursement` before the model reads it."""
    data.INPUT3_DOMESTIC_NEW_GROSS_DISBURSEMENT_SCHEMA.validate(input3_domestic_new_gross_disbursement)
    return input3_domestic_new_gross_disbursement


def _check_pv_base_input_output_cumulative(
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative,
) -> data.PvBaseInputOutputCumulative:
    """Validate `pv_base_input_output_cumulative` before the model reads it."""
    data.PV_BASE_INPUT_OUTPUT_CUMULATIVE_SCHEMA.validate(pv_base_input_output_cumulative)
    return pv_base_input_output_cumulative


CHECKS = {
    "input4_interest_rate": _check_input4_interest_rate,
    "input4_grace_period": _check_input4_grace_period,
    "input4_loan_maturity": _check_input4_loan_maturity,
    "input4_disbursements": _check_input4_disbursements,
    "input4_instrument_names": _check_input4_instrument_names,
    "input4_blend_scale_key": _check_input4_blend_scale_key,
    "input5_grace_period": _check_input5_grace_period,
    "input5_interest_rate_on_domestic_debt": _check_input5_interest_rate_on_domestic_debt,
    "input5_maturity": _check_input5_maturity,
    "input5_public_gfns_other_adjustment": _check_input5_public_gfns_other_adjustment,
    "input5_domestic_financing_source": _check_input5_domestic_financing_source,
    "input5_gfn_share": _check_input5_gfn_share,
    "country": _check_country,
    "first_projection_year": _check_first_projection_year,
    "discount_rate": _check_discount_rate,
    "external_domestic_debt_definition": _check_external_domestic_debt_definition,
    "fiscal_space_moderate_assessment_flag": _check_fiscal_space_moderate_assessment_flag,
    "fiscal_space_stock_band": _check_fiscal_space_stock_band,
    "fiscal_space_flow_band": _check_fiscal_space_flow_band,
    "customized_public_delta": _check_customized_public_delta,
    "blend_ida_new_floating_currency": _check_blend_ida_new_floating_currency,
    "input_1_rer_overvaluation": _check_input_1_rer_overvaluation,
    "customized_public_include_scenario": _check_customized_public_include_scenario,
    "input6_commodity_group_relevant": _check_input6_commodity_group_relevant,
    "input8_sdr_interest_rate": _check_input8_sdr_interest_rate,
    "input6_tailored_tests_enabled": _check_input6_tailored_tests_enabled,
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
    "customized_public_new_forex_borrowing_cumulative_overflow": _check_customized_public_new_forex_borrowing_cumulative_overflow,
    "customized_public_new_domestic_mlt_cumulative_overflow": _check_customized_public_new_domestic_mlt_cumulative_overflow,
    "customized_public_residual_overflow": _check_customized_public_residual_overflow,
    "customized_external_new_forex_borrowing_cumulative_overflow": _check_customized_external_new_forex_borrowing_cumulative_overflow,
    "input8_sdr_stock": _check_input8_sdr_stock,
    "input3_old_debt_service": _check_input3_old_debt_service,
    "input3_new_disbursements": _check_input3_new_disbursements,
    "input3_domestic_outstanding_of_existing_debt": _check_input3_domestic_outstanding_of_existing_debt,
    "input3_domestic_o_w_st": _check_input3_domestic_o_w_st,
    "input3_domestic_interest_payment_from_existing_debt": _check_input3_domestic_interest_payment_from_existing_debt,
    "input3_domestic_principal_payment_from_existing_debt": _check_input3_domestic_principal_payment_from_existing_debt,
    "input3_domestic_new_gross_disbursement": _check_input3_domestic_new_gross_disbursement,
    "pv_base_input_output_cumulative": _check_pv_base_input_output_cumulative,
}
