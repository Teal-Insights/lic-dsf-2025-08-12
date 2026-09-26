"""Memoized evaluator and per-output input bundles."""

from __future__ import annotations

from dataclasses import Field, dataclass, fields
from functools import cached_property
from pathlib import Path
from typing import Any, ClassVar, Self

from . import data, internals, validation
from .workbook import read_bound_inputs


def _bind_inputs(target: object, inputs: dict[str, Any], *, validate: bool = True) -> None:
    if not validate:
        for name, value in inputs.items():
            setattr(target, name, value)
        return
    for name, value in inputs.items():
        check = validation.CHECKS.get(name)
        setattr(target, name, value if check is None else check(value))


class _BoundInputs:
    """Shared workbook bind and CHECKS validation for Model and input bundles."""

    __dataclass_fields__: ClassVar[dict[str, Field[Any]]]
    _INPUT_IDS: tuple[str, ...] = ()

    @classmethod
    def from_workbook(cls, workbook: Path | str, **overrides: object) -> Self:
        """Bind input leaves from a populated workbook of this vintage."""
        declared = getattr(cls, "__dataclass_fields__", None)
        names = tuple(declared) if declared else cls._INPUT_IDS
        unknown = overrides.keys() - set(names)
        if unknown:
            raise TypeError(f"unknown inputs: {sorted(unknown)}")
        values = read_bound_inputs(Path(workbook), names, data)
        values.update(overrides)
        return cls(**values)

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        holder = Model.__new__(Model)
        names = {field.name for field in fields(self)}
        values = {name: getattr(self, name) for name in names}
        _bind_inputs(holder, values)
        for name in names:
            object.__setattr__(self, name, getattr(holder, name))


class _SnapshotInputs(_BoundInputs):
    """Per-output bundle factory over `data.*_DEFAULT` leaves."""

    @classmethod
    def from_defaults(cls, **overrides: object) -> Self:
        names = {field.name for field in fields(cls)}
        unexpected = overrides.keys() - names
        if unexpected:
            listed = ", ".join(sorted(unexpected))
            raise TypeError(f"{cls.__name__}.from_defaults() got unknown argument(s): {listed}")
        values = {
            name: (
                overrides[name] if name in overrides else getattr(data, f"{name.upper()}_DEFAULT")
            )
            for name in names
        }
        return cls(**values)


class Model(_BoundInputs):
    """Formula series of the workbook, evaluated on demand from bound inputs.

    Each attribute evaluates its named formula once per model. Only the
    inputs bound at construction are available, so a public function
    supplies exactly the leaves of its output. Unknown constructor
    names fail closed. `from_defaults` binds every input from
    `data.*_DEFAULT`. `from_workbook` reads those input cells from a
    populated workbook of this vintage.
    """

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    fiscal_space_moderate_assessment_flag: int | str
    fiscal_space_stock_band: data.FiscalSpaceStockBand
    fiscal_space_flow_band: data.FiscalSpaceFlowBand
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    customized_external_debt_profile_period: int | str
    customized_external_debt_profile_disbursement: float | str
    customized_external_new_forex_borrowing_cumulative_overflow: data.CustomizedExternalNewForexBorrowingCumulativeOverflow
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    current_year: int | str
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative
    _INPUT_IDS: tuple[str, ...] = ("input4_interest_rate", "input4_grace_period", "input4_loan_maturity", "input4_disbursements", "input4_instrument_names", "input4_blend_variant", "input4_blend_scale_key", "input5_grace_period", "input5_interest_rate_on_domestic_debt", "input5_interest_rate_on_domestic_debt_fx_long", "input5_maturity", "input5_maturity_central_bank", "input5_public_gfns_other_adjustment", "input5_domestic_financing_source", "input5_gfn_share", "start_working_language", "country", "first_projection_year", "discount_rate", "external_domestic_debt_definition", "fiscal_space_moderate_assessment_flag", "fiscal_space_stock_band", "fiscal_space_flow_band", "contingent_liability_other_elements_pct_gdp", "contingent_liability_soe_debt_pct_gdp", "contingent_liability_financial_market_pct_gdp", "ppp_capital_stock_shock_pct", "customized_public_delta", "blend_ida_new_floating_currency", "input_1_rer_overvaluation", "customized_public_include_scenario", "input6_commodity_group_relevant", "input8_sdr_interest_historical", "input8_sdr_interest", "input8_sdr_interest_rate", "input6_tailored_tests_enabled", "input6_standard_size_threshold_mode", "input6_standard_interactions", "input6_standard_user_defined_threshold", "input3_input_3_macro_gross_domestic_product_us_dollars", "input3_input_3_macro_real_gross_domestic_product", "input3_input_3_macro_u_s_deflator", "input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p", "input3_input_3_macro_national_currency_per_u_s_dollar_p_a", "input3_input_3_macro_government_revenue_and_grants", "input3_input_3_macro_government_grants", "in3_macro_government_primary_expenditures_this_used_be", "in3_macro_public_sector_liquid_assets_stock_e_g_cash", "in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g", "input3_input_3_macro_privatization_proceeds", "in3_macro_recognition_of_contingent_liab_e_g_bank", "input3_input_3_macro_debt_relief_non_multilateral_hipc", "input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify", "input3_input_3_macro_current_account", "input3_input_3_macro_exports_of_goods_and_services", "input3_input_3_macro_exports_commodity_fuel", "input3_input_3_macro_exports_commodity_non_fuel", "input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number", "input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number", "input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number", "input3_input_3_macro_current_transfers_net", "input3_input_3_macro_foreign_direct_investment", "input3_input_3_external_debt_ppg_mlt_external_debt_outstanding", "input3_input_3_external_debt_ppg_st_external_debt_outstanding", "input3_input_3_external_debt_ppg_external_debt_interest_due", "input3_input_3_external_debt_ppg_external_arrears", "input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding", "input3_input_3_external_debt_private_sector_st_external_debt_outstanding", "input3_input_3_external_debt_private_external_debt_interest_due", "input3_input_3_external_debt_private_mlt_external_debt_amortization_due", "input3_input_3_old_debt_service_total_principal_payment", "customized_public_template_anchor", "customized_public_natural_disaster_year", "customized_public_external_mlt_disbursement_profile", "customized_public_new_forex_borrowing_cumulative_overflow", "customized_public_new_domestic_mlt_cumulative_overflow", "customized_public_residual_overflow", "customized_public_new_forex_debt_stock_initial", "customized_public_domestic_mlt_interest_initial", "customized_public_domestic_st_interest_initial", "customized_external_debt_profile_period", "customized_external_debt_profile_disbursement", "customized_external_new_forex_borrowing_cumulative_overflow", "input8_sdr_stock", "input3_old_debt_service", "input3_new_disbursements", "input3_domestic_outstanding_of_existing_debt", "input3_domestic_o_w_st", "input3_domestic_interest_payment_from_existing_debt", "input3_domestic_principal_payment_from_existing_debt", "input3_domestic_new_gross_disbursement", "current_year", "pv_base_input_output_cumulative")

    def __init__(self, bundle: _BoundInputs | None = None, /, **inputs: Any) -> None:
        if bundle is not None:
            if not isinstance(bundle, _BoundInputs):
                raise TypeError(
                    f"Model() bundle must be a bound inputs instance, not {type(bundle).__name__}"
                )
            if inputs:
                raise TypeError("Model() does not accept keyword inputs with a bound bundle")
            values = {field.name: getattr(bundle, field.name) for field in fields(bundle)}
            _bind_inputs(self, values, validate=False)
            return
        unknown = inputs.keys() - {"input4_interest_rate", "input4_grace_period", "input4_loan_maturity", "input4_disbursements", "input4_instrument_names", "input4_blend_variant", "input4_blend_scale_key", "input5_grace_period", "input5_interest_rate_on_domestic_debt", "input5_interest_rate_on_domestic_debt_fx_long", "input5_maturity", "input5_maturity_central_bank", "input5_public_gfns_other_adjustment", "input5_domestic_financing_source", "input5_gfn_share", "start_working_language", "country", "first_projection_year", "discount_rate", "external_domestic_debt_definition", "fiscal_space_moderate_assessment_flag", "fiscal_space_stock_band", "fiscal_space_flow_band", "contingent_liability_other_elements_pct_gdp", "contingent_liability_soe_debt_pct_gdp", "contingent_liability_financial_market_pct_gdp", "ppp_capital_stock_shock_pct", "customized_public_delta", "blend_ida_new_floating_currency", "input_1_rer_overvaluation", "customized_public_include_scenario", "input6_commodity_group_relevant", "input8_sdr_interest_historical", "input8_sdr_interest", "input8_sdr_interest_rate", "input6_tailored_tests_enabled", "input6_standard_size_threshold_mode", "input6_standard_interactions", "input6_standard_user_defined_threshold", "input3_input_3_macro_gross_domestic_product_us_dollars", "input3_input_3_macro_real_gross_domestic_product", "input3_input_3_macro_u_s_deflator", "input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p", "input3_input_3_macro_national_currency_per_u_s_dollar_p_a", "input3_input_3_macro_government_revenue_and_grants", "input3_input_3_macro_government_grants", "in3_macro_government_primary_expenditures_this_used_be", "in3_macro_public_sector_liquid_assets_stock_e_g_cash", "in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g", "input3_input_3_macro_privatization_proceeds", "in3_macro_recognition_of_contingent_liab_e_g_bank", "input3_input_3_macro_debt_relief_non_multilateral_hipc", "input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify", "input3_input_3_macro_current_account", "input3_input_3_macro_exports_of_goods_and_services", "input3_input_3_macro_exports_commodity_fuel", "input3_input_3_macro_exports_commodity_non_fuel", "input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number", "input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number", "input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number", "input3_input_3_macro_current_transfers_net", "input3_input_3_macro_foreign_direct_investment", "input3_input_3_external_debt_ppg_mlt_external_debt_outstanding", "input3_input_3_external_debt_ppg_st_external_debt_outstanding", "input3_input_3_external_debt_ppg_external_debt_interest_due", "input3_input_3_external_debt_ppg_external_arrears", "input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding", "input3_input_3_external_debt_private_sector_st_external_debt_outstanding", "input3_input_3_external_debt_private_external_debt_interest_due", "input3_input_3_external_debt_private_mlt_external_debt_amortization_due", "input3_input_3_old_debt_service_total_principal_payment", "customized_public_template_anchor", "customized_public_natural_disaster_year", "customized_public_external_mlt_disbursement_profile", "customized_public_new_forex_borrowing_cumulative_overflow", "customized_public_new_domestic_mlt_cumulative_overflow", "customized_public_residual_overflow", "customized_public_new_forex_debt_stock_initial", "customized_public_domestic_mlt_interest_initial", "customized_public_domestic_st_interest_initial", "customized_external_debt_profile_period", "customized_external_debt_profile_disbursement", "customized_external_new_forex_borrowing_cumulative_overflow", "input8_sdr_stock", "input3_old_debt_service", "input3_new_disbursements", "input3_domestic_outstanding_of_existing_debt", "input3_domestic_o_w_st", "input3_domestic_interest_payment_from_existing_debt", "input3_domestic_principal_payment_from_existing_debt", "input3_domestic_new_gross_disbursement", "current_year", "pv_base_input_output_cumulative"}
        if unknown:
            raise TypeError(f"unknown inputs: {sorted(unknown)}")
        _bind_inputs(self, inputs)

    @classmethod
    def from_defaults(
        cls,
        *,
        input4_interest_rate: data.Input4InterestRate = data.INPUT4_INTEREST_RATE_DEFAULT,
        input4_grace_period: data.Input4GracePeriod = data.INPUT4_GRACE_PERIOD_DEFAULT,
        input4_loan_maturity: data.Input4LoanMaturity = data.INPUT4_LOAN_MATURITY_DEFAULT,
        input4_disbursements: data.Input4Disbursements = data.INPUT4_DISBURSEMENTS_DEFAULT,
        input4_instrument_names: data.Input4InstrumentNames = data.INPUT4_INSTRUMENT_NAMES_DEFAULT,
        input4_blend_variant: str = data.INPUT4_BLEND_VARIANT_DEFAULT,
        input4_blend_scale_key: data.Input4BlendScaleKey = data.INPUT4_BLEND_SCALE_KEY_DEFAULT,
        input5_grace_period: data.Input5GracePeriod = data.INPUT5_GRACE_PERIOD_DEFAULT,
        input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt = data.INPUT5_INTEREST_RATE_ON_DOMESTIC_DEBT_DEFAULT,
        input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong = data.INPUT5_INTEREST_RATE_ON_DOMESTIC_DEBT_FX_LONG_DEFAULT,
        input5_maturity: data.Input5Maturity = data.INPUT5_MATURITY_DEFAULT,
        input5_maturity_central_bank: int | str = data.INPUT5_MATURITY_CENTRAL_BANK_DEFAULT,
        input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment = data.INPUT5_PUBLIC_GFNS_OTHER_ADJUSTMENT_DEFAULT,
        input5_domestic_financing_source: int | str = data.INPUT5_DOMESTIC_FINANCING_SOURCE_DEFAULT,
        input5_gfn_share: data.Input5GfnShare = data.INPUT5_GFN_SHARE_DEFAULT,
        start_working_language: str = data.START_WORKING_LANGUAGE_DEFAULT,
        country: str = data.COUNTRY_DEFAULT,
        first_projection_year: int | str = data.FIRST_PROJECTION_YEAR_DEFAULT,
        discount_rate: float | str = data.DISCOUNT_RATE_DEFAULT,
        external_domestic_debt_definition: str = data.EXTERNAL_DOMESTIC_DEBT_DEFINITION_DEFAULT,
        fiscal_space_moderate_assessment_flag: int | str = data.FISCAL_SPACE_MODERATE_ASSESSMENT_FLAG_DEFAULT,
        fiscal_space_stock_band: data.FiscalSpaceStockBand = data.FISCAL_SPACE_STOCK_BAND_DEFAULT,
        fiscal_space_flow_band: data.FiscalSpaceFlowBand = data.FISCAL_SPACE_FLOW_BAND_DEFAULT,
        contingent_liability_other_elements_pct_gdp: float | str = data.CONTINGENT_LIABILITY_OTHER_ELEMENTS_PCT_GDP_DEFAULT,
        contingent_liability_soe_debt_pct_gdp: float | str = data.CONTINGENT_LIABILITY_SOE_DEBT_PCT_GDP_DEFAULT,
        contingent_liability_financial_market_pct_gdp: float | str = data.CONTINGENT_LIABILITY_FINANCIAL_MARKET_PCT_GDP_DEFAULT,
        ppp_capital_stock_shock_pct: float | str = data.PPP_CAPITAL_STOCK_SHOCK_PCT_DEFAULT,
        customized_public_delta: data.CustomizedPublicDelta = data.CUSTOMIZED_PUBLIC_DELTA_DEFAULT,
        blend_ida_new_floating_currency: str = data.BLEND_IDA_NEW_FLOATING_CURRENCY_DEFAULT,
        input_1_rer_overvaluation: float | str = data.INPUT_1_RER_OVERVALUATION_DEFAULT,
        customized_public_include_scenario: str = data.CUSTOMIZED_PUBLIC_INCLUDE_SCENARIO_DEFAULT,
        input6_commodity_group_relevant: data.Input6CommodityGroupRelevant = data.INPUT6_COMMODITY_GROUP_RELEVANT_DEFAULT,
        input8_sdr_interest_historical: data.Input8SdrInterestHistorical = data.INPUT8_SDR_INTEREST_HISTORICAL_DEFAULT,
        input8_sdr_interest: data.Input8SdrInterest = data.INPUT8_SDR_INTEREST_DEFAULT,
        input8_sdr_interest_rate: float | str = data.INPUT8_SDR_INTEREST_RATE_DEFAULT,
        input6_tailored_tests_enabled: str = data.INPUT6_TAILORED_TESTS_ENABLED_DEFAULT,
        input6_standard_size_threshold_mode: str = data.INPUT6_STANDARD_SIZE_THRESHOLD_MODE_DEFAULT,
        input6_standard_interactions: str = data.INPUT6_STANDARD_INTERACTIONS_DEFAULT,
        input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold = data.INPUT6_STANDARD_USER_DEFINED_THRESHOLD_DEFAULT,
        input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars = data.INPUT3_INPUT_3_MACRO_GROSS_DOMESTIC_PRODUCT_US_DOLLARS_DEFAULT,
        input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct = data.INPUT3_INPUT_3_MACRO_REAL_GROSS_DOMESTIC_PRODUCT_DEFAULT,
        input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator = data.INPUT3_INPUT_3_MACRO_U_S_DEFLATOR_DEFAULT,
        input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP = data.INPUT3_INPUT_3_MACRO_NATIONAL_CURRENCY_PER_U_S_DOLLAR_E_O_P_DEFAULT,
        input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA = data.INPUT3_INPUT_3_MACRO_NATIONAL_CURRENCY_PER_U_S_DOLLAR_P_A_DEFAULT,
        input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants = data.INPUT3_INPUT_3_MACRO_GOVERNMENT_REVENUE_AND_GRANTS_DEFAULT,
        input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants = data.INPUT3_INPUT_3_MACRO_GOVERNMENT_GRANTS_DEFAULT,
        in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe = data.IN3_MACRO_GOVERNMENT_PRIMARY_EXPENDITURES_THIS_USED_BE_DEFAULT,
        in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash = data.IN3_MACRO_PUBLIC_SECTOR_LIQUID_ASSETS_STOCK_E_G_CASH_DEFAULT,
        in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG = data.IN3_MACRO_LIQUID_FINANCIAL_ASSETS_USED_MEET_GFNS_FLOW_E_G_DEFAULT,
        input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds = data.INPUT3_INPUT_3_MACRO_PRIVATIZATION_PROCEEDS_DEFAULT,
        in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank = data.IN3_MACRO_RECOGNITION_OF_CONTINGENT_LIAB_E_G_BANK_DEFAULT,
        input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc = data.INPUT3_INPUT_3_MACRO_DEBT_RELIEF_NON_MULTILATERAL_HIPC_DEFAULT,
        input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify = data.INPUT3_INPUT_3_MACRO_OTHER_DEBT_CREATING_OR_REDUCING_FLOW_PLEASE_SPECIFY_DEFAULT,
        input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount = data.INPUT3_INPUT_3_MACRO_CURRENT_ACCOUNT_DEFAULT,
        input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices = data.INPUT3_INPUT_3_MACRO_EXPORTS_OF_GOODS_AND_SERVICES_DEFAULT,
        input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel = data.INPUT3_INPUT_3_MACRO_EXPORTS_COMMODITY_FUEL_DEFAULT,
        input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel = data.INPUT3_INPUT_3_MACRO_EXPORTS_COMMODITY_NON_FUEL_DEFAULT,
        input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber = data.INPUT3_INPUT_3_MACRO_IMPORTS_OF_GOODS_AND_SERVICES_ENTER_AS_A_POSITIVE_NUMBER_DEFAULT,
        input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber = data.INPUT3_INPUT_3_MACRO_IMPORTS_COMMODITY_FUEL_ENTER_AS_A_POSITIVE_NUMBER_DEFAULT,
        input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber = data.INPUT3_INPUT_3_MACRO_IMPORTS_COMMODITY_NON_FUEL_ENTER_AS_A_POSITIVE_NUMBER_DEFAULT,
        input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet = data.INPUT3_INPUT_3_MACRO_CURRENT_TRANSFERS_NET_DEFAULT,
        input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment = data.INPUT3_INPUT_3_MACRO_FOREIGN_DIRECT_INVESTMENT_DEFAULT,
        input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding = data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_MLT_EXTERNAL_DEBT_OUTSTANDING_DEFAULT,
        input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding = data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_ST_EXTERNAL_DEBT_OUTSTANDING_DEFAULT,
        input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue = data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_EXTERNAL_DEBT_INTEREST_DUE_DEFAULT,
        input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears = data.INPUT3_INPUT_3_EXTERNAL_DEBT_PPG_EXTERNAL_ARREARS_DEFAULT,
        input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding = data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_SECTOR_MLT_EXTERNAL_DEBT_OUTSTANDING_DEFAULT,
        input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding = data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_SECTOR_ST_EXTERNAL_DEBT_OUTSTANDING_DEFAULT,
        input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue = data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_EXTERNAL_DEBT_INTEREST_DUE_DEFAULT,
        input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue = data.INPUT3_INPUT_3_EXTERNAL_DEBT_PRIVATE_MLT_EXTERNAL_DEBT_AMORTIZATION_DUE_DEFAULT,
        input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment = data.INPUT3_INPUT_3_OLD_DEBT_SERVICE_TOTAL_PRINCIPAL_PAYMENT_DEFAULT,
        customized_public_template_anchor: float | str = data.CUSTOMIZED_PUBLIC_TEMPLATE_ANCHOR_DEFAULT,
        customized_public_natural_disaster_year: int | str = data.CUSTOMIZED_PUBLIC_NATURAL_DISASTER_YEAR_DEFAULT,
        customized_public_external_mlt_disbursement_profile: float | str = data.CUSTOMIZED_PUBLIC_EXTERNAL_MLT_DISBURSEMENT_PROFILE_DEFAULT,
        customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow = data.CUSTOMIZED_PUBLIC_NEW_FOREX_BORROWING_CUMULATIVE_OVERFLOW_DEFAULT,
        customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow = data.CUSTOMIZED_PUBLIC_NEW_DOMESTIC_MLT_CUMULATIVE_OVERFLOW_DEFAULT,
        customized_public_residual_overflow: data.CustomizedPublicResidualOverflow = data.CUSTOMIZED_PUBLIC_RESIDUAL_OVERFLOW_DEFAULT,
        customized_public_new_forex_debt_stock_initial: float | str = data.CUSTOMIZED_PUBLIC_NEW_FOREX_DEBT_STOCK_INITIAL_DEFAULT,
        customized_public_domestic_mlt_interest_initial: float | str = data.CUSTOMIZED_PUBLIC_DOMESTIC_MLT_INTEREST_INITIAL_DEFAULT,
        customized_public_domestic_st_interest_initial: float | str = data.CUSTOMIZED_PUBLIC_DOMESTIC_ST_INTEREST_INITIAL_DEFAULT,
        customized_external_debt_profile_period: int | str = data.CUSTOMIZED_EXTERNAL_DEBT_PROFILE_PERIOD_DEFAULT,
        customized_external_debt_profile_disbursement: float | str = data.CUSTOMIZED_EXTERNAL_DEBT_PROFILE_DISBURSEMENT_DEFAULT,
        customized_external_new_forex_borrowing_cumulative_overflow: data.CustomizedExternalNewForexBorrowingCumulativeOverflow = data.CUSTOMIZED_EXTERNAL_NEW_FOREX_BORROWING_CUMULATIVE_OVERFLOW_DEFAULT,
        input8_sdr_stock: data.Input8SdrStock = data.INPUT8_SDR_STOCK_DEFAULT,
        input3_old_debt_service: data.Input3OldDebtService = data.INPUT3_OLD_DEBT_SERVICE_DEFAULT,
        input3_new_disbursements: data.Input3NewDisbursements = data.INPUT3_NEW_DISBURSEMENTS_DEFAULT,
        input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt = data.INPUT3_DOMESTIC_OUTSTANDING_OF_EXISTING_DEBT_DEFAULT,
        input3_domestic_o_w_st: data.Input3DomesticOWSt = data.INPUT3_DOMESTIC_O_W_ST_DEFAULT,
        input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt = data.INPUT3_DOMESTIC_INTEREST_PAYMENT_FROM_EXISTING_DEBT_DEFAULT,
        input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt = data.INPUT3_DOMESTIC_PRINCIPAL_PAYMENT_FROM_EXISTING_DEBT_DEFAULT,
        input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement = data.INPUT3_DOMESTIC_NEW_GROSS_DISBURSEMENT_DEFAULT,
        current_year: int | str = data.CURRENT_YEAR_DEFAULT,
        pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative = data.PV_BASE_INPUT_OUTPUT_CUMULATIVE_DEFAULT,
    ) -> Model:
        """Bind every input from `data.*_DEFAULT`, then apply overrides."""
        return cls(
            input4_interest_rate=input4_interest_rate,
            input4_grace_period=input4_grace_period,
            input4_loan_maturity=input4_loan_maturity,
            input4_disbursements=input4_disbursements,
            input4_instrument_names=input4_instrument_names,
            input4_blend_variant=input4_blend_variant,
            input4_blend_scale_key=input4_blend_scale_key,
            input5_grace_period=input5_grace_period,
            input5_interest_rate_on_domestic_debt=input5_interest_rate_on_domestic_debt,
            input5_interest_rate_on_domestic_debt_fx_long=input5_interest_rate_on_domestic_debt_fx_long,
            input5_maturity=input5_maturity,
            input5_maturity_central_bank=input5_maturity_central_bank,
            input5_public_gfns_other_adjustment=input5_public_gfns_other_adjustment,
            input5_domestic_financing_source=input5_domestic_financing_source,
            input5_gfn_share=input5_gfn_share,
            start_working_language=start_working_language,
            country=country,
            first_projection_year=first_projection_year,
            discount_rate=discount_rate,
            external_domestic_debt_definition=external_domestic_debt_definition,
            fiscal_space_moderate_assessment_flag=fiscal_space_moderate_assessment_flag,
            fiscal_space_stock_band=fiscal_space_stock_band,
            fiscal_space_flow_band=fiscal_space_flow_band,
            contingent_liability_other_elements_pct_gdp=contingent_liability_other_elements_pct_gdp,
            contingent_liability_soe_debt_pct_gdp=contingent_liability_soe_debt_pct_gdp,
            contingent_liability_financial_market_pct_gdp=contingent_liability_financial_market_pct_gdp,
            ppp_capital_stock_shock_pct=ppp_capital_stock_shock_pct,
            customized_public_delta=customized_public_delta,
            blend_ida_new_floating_currency=blend_ida_new_floating_currency,
            input_1_rer_overvaluation=input_1_rer_overvaluation,
            customized_public_include_scenario=customized_public_include_scenario,
            input6_commodity_group_relevant=input6_commodity_group_relevant,
            input8_sdr_interest_historical=input8_sdr_interest_historical,
            input8_sdr_interest=input8_sdr_interest,
            input8_sdr_interest_rate=input8_sdr_interest_rate,
            input6_tailored_tests_enabled=input6_tailored_tests_enabled,
            input6_standard_size_threshold_mode=input6_standard_size_threshold_mode,
            input6_standard_interactions=input6_standard_interactions,
            input6_standard_user_defined_threshold=input6_standard_user_defined_threshold,
            input3_input_3_macro_gross_domestic_product_us_dollars=input3_input_3_macro_gross_domestic_product_us_dollars,
            input3_input_3_macro_real_gross_domestic_product=input3_input_3_macro_real_gross_domestic_product,
            input3_input_3_macro_u_s_deflator=input3_input_3_macro_u_s_deflator,
            input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p=input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p,
            input3_input_3_macro_national_currency_per_u_s_dollar_p_a=input3_input_3_macro_national_currency_per_u_s_dollar_p_a,
            input3_input_3_macro_government_revenue_and_grants=input3_input_3_macro_government_revenue_and_grants,
            input3_input_3_macro_government_grants=input3_input_3_macro_government_grants,
            in3_macro_government_primary_expenditures_this_used_be=in3_macro_government_primary_expenditures_this_used_be,
            in3_macro_public_sector_liquid_assets_stock_e_g_cash=in3_macro_public_sector_liquid_assets_stock_e_g_cash,
            in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g=in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g,
            input3_input_3_macro_privatization_proceeds=input3_input_3_macro_privatization_proceeds,
            in3_macro_recognition_of_contingent_liab_e_g_bank=in3_macro_recognition_of_contingent_liab_e_g_bank,
            input3_input_3_macro_debt_relief_non_multilateral_hipc=input3_input_3_macro_debt_relief_non_multilateral_hipc,
            input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify=input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify,
            input3_input_3_macro_current_account=input3_input_3_macro_current_account,
            input3_input_3_macro_exports_of_goods_and_services=input3_input_3_macro_exports_of_goods_and_services,
            input3_input_3_macro_exports_commodity_fuel=input3_input_3_macro_exports_commodity_fuel,
            input3_input_3_macro_exports_commodity_non_fuel=input3_input_3_macro_exports_commodity_non_fuel,
            input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number=input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number,
            input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number=input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number,
            input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number=input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number,
            input3_input_3_macro_current_transfers_net=input3_input_3_macro_current_transfers_net,
            input3_input_3_macro_foreign_direct_investment=input3_input_3_macro_foreign_direct_investment,
            input3_input_3_external_debt_ppg_mlt_external_debt_outstanding=input3_input_3_external_debt_ppg_mlt_external_debt_outstanding,
            input3_input_3_external_debt_ppg_st_external_debt_outstanding=input3_input_3_external_debt_ppg_st_external_debt_outstanding,
            input3_input_3_external_debt_ppg_external_debt_interest_due=input3_input_3_external_debt_ppg_external_debt_interest_due,
            input3_input_3_external_debt_ppg_external_arrears=input3_input_3_external_debt_ppg_external_arrears,
            input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding=input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding,
            input3_input_3_external_debt_private_sector_st_external_debt_outstanding=input3_input_3_external_debt_private_sector_st_external_debt_outstanding,
            input3_input_3_external_debt_private_external_debt_interest_due=input3_input_3_external_debt_private_external_debt_interest_due,
            input3_input_3_external_debt_private_mlt_external_debt_amortization_due=input3_input_3_external_debt_private_mlt_external_debt_amortization_due,
            input3_input_3_old_debt_service_total_principal_payment=input3_input_3_old_debt_service_total_principal_payment,
            customized_public_template_anchor=customized_public_template_anchor,
            customized_public_natural_disaster_year=customized_public_natural_disaster_year,
            customized_public_external_mlt_disbursement_profile=customized_public_external_mlt_disbursement_profile,
            customized_public_new_forex_borrowing_cumulative_overflow=customized_public_new_forex_borrowing_cumulative_overflow,
            customized_public_new_domestic_mlt_cumulative_overflow=customized_public_new_domestic_mlt_cumulative_overflow,
            customized_public_residual_overflow=customized_public_residual_overflow,
            customized_public_new_forex_debt_stock_initial=customized_public_new_forex_debt_stock_initial,
            customized_public_domestic_mlt_interest_initial=customized_public_domestic_mlt_interest_initial,
            customized_public_domestic_st_interest_initial=customized_public_domestic_st_interest_initial,
            customized_external_debt_profile_period=customized_external_debt_profile_period,
            customized_external_debt_profile_disbursement=customized_external_debt_profile_disbursement,
            customized_external_new_forex_borrowing_cumulative_overflow=customized_external_new_forex_borrowing_cumulative_overflow,
            input8_sdr_stock=input8_sdr_stock,
            input3_old_debt_service=input3_old_debt_service,
            input3_new_disbursements=input3_new_disbursements,
            input3_domestic_outstanding_of_existing_debt=input3_domestic_outstanding_of_existing_debt,
            input3_domestic_o_w_st=input3_domestic_o_w_st,
            input3_domestic_interest_payment_from_existing_debt=input3_domestic_interest_payment_from_existing_debt,
            input3_domestic_principal_payment_from_existing_debt=input3_domestic_principal_payment_from_existing_debt,
            input3_domestic_new_gross_disbursement=input3_domestic_new_gross_disbursement,
            current_year=current_year,
            pv_base_input_output_cumulative=pv_base_input_output_cumulative,
        )

    @cached_property
    def imported_prev_dsa_match_keys(self) -> data.Series[str | int | float | bool | None]:
        return internals.imported_prev_dsa_match_keys(imported_prev_dsa_investment_weo_codes=data.IMPORTED_PREV_DSA_INVESTMENT_WEO_CODES, imported_country_code=self.imported_country_code, imported_prev_dsa_weo_codes=self.imported_prev_dsa_weo_codes, imported_selected_vintage_dates=self.imported_selected_vintage_dates)

    @cached_property
    def imported_prev_dsa_history_year_headers(self) -> data.Series[int | str | None]:
        return internals.imported_prev_dsa_history_year_headers(realism1_external_year_headers=self.realism1_external_year_headers)

    @cached_property
    def imported_prev_dsa_investment_year_headers(self) -> data.Series[int | str | None]:
        return internals.imported_prev_dsa_investment_year_headers(realism3_contribution_years=self.realism3_contribution_years)

    @cached_property
    def _scan_dsa_ext_external_debt_nominal_1(self) -> internals.ScanDsaExtExternalDebtNominal1Result:
        return internals.scan_dsa_ext_external_debt_nominal_1(dsa_ext_non_interest_current_account_deficit=self.dsa_ext_non_interest_current_account_deficit, dsa_ext_net_fdi_negative_inflow=self.dsa_ext_net_fdi_negative_inflow, dsa_ext_denominator_1_g_g=self.dsa_ext_denominator_1_g_g, dsa_ext_nominal_gdp_million_of_us_dollars=self.dsa_ext_nominal_gdp_million_of_us_dollars, dsa_ext_real_gdp_growth_in_percent=self.dsa_ext_real_gdp_growth_in_percent, dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent=self.dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent, dsa_ext_share_of_local_currency_denominated_external_debt_to_total_external_debt=self.dsa_ext_share_of_local_currency_denominated_external_debt_to_total_external_debt, dsa_ext_share_of_local_currency_denominated_external_debt_to_total_external_debt_baseline=self.dsa_ext_share_of_local_currency_denominated_external_debt_to_total_external_debt_baseline, dsa_ext_depreciation_of_nc_depreciation=self.dsa_ext_depreciation_of_nc_depreciation, dsa_ext_o_w_interest_baseline=self.dsa_ext_o_w_interest_baseline, dsa_ext_o_w_interest_additional_borrowing=self.dsa_ext_o_w_interest_additional_borrowing, dsa_ext_of_which_public_and_publicly_guaranteed_ppg=self.dsa_ext_of_which_public_and_publicly_guaranteed_ppg, dsa_ext_of_which_private=self.dsa_ext_of_which_private, c4_mkt_fin_gfn_increase=self.c4_mkt_fin_gfn_increase, macro_debt_total_ext_debt_interest_due_include_interest=self.macro_debt_total_ext_debt_interest_due_include_interest, pv_stress_bounds_t_g_0=self.pv_stress_bounds_t_g_0, pv_stress_bounds_t_m_condition=self.pv_stress_bounds_t_m_condition, pv_stress_average_interest_rate_new_debt=self.pv_stress_average_interest_rate_new_debt, pv_stress_average_maturity_of_new_debt=self.pv_stress_average_maturity_of_new_debt, pv_stress_average_grace_period_new_debt=self.pv_stress_average_grace_period_new_debt, pv_stress_t_g_0=self.pv_stress_t_g_0, pv_stress_t_m_condition=self.pv_stress_t_m_condition)

    @cached_property
    def dsa_ext_external_debt_nominal_1(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_external_debt_nominal_1

    @cached_property
    def dsa_ext_change_in_external_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_change_in_external_debt

    @cached_property
    def dsa_ext_identified_net_debt_creating_flows(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_identified_net_debt_creating_flows

    @cached_property
    def dsa_ext_endogenous_debt_dynamics_2(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_endogenous_debt_dynamics_2

    @cached_property
    def dsa_ext_contribution_from_nominal_interest_rate(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_contribution_from_nominal_interest_rate

    @cached_property
    def dsa_ext_contribution_from_real_gdp_growth(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_contribution_from_real_gdp_growth

    @cached_property
    def dsa_ext_contribution_from_price_and_exchange_rate_changes(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_contribution_from_price_and_exchange_rate_changes

    @cached_property
    def dsa_ext_residual_3(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_residual_3

    @cached_property
    def dsa_ext_effective_interest_rate_percent_4(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_effective_interest_rate_percent_4

    @cached_property
    def dsa_ext_nominal_debt_baseline(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_nominal_debt_baseline

    @cached_property
    def dsa_ext_increase_baseline(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_increase_baseline

    @cached_property
    def dsa_ext_nominal_debt_stress(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_nominal_debt_stress

    @cached_property
    def dsa_ext_increase_stress(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_increase_stress

    @cached_property
    def dsa_ext_residual_gross_borrowing(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_residual_gross_borrowing

    @cached_property
    def dsa_ext_o_w_interest_stress(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_o_w_interest_stress

    @cached_property
    def dsa_ext_new_interest_payments(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_new_interest_payments

    @cached_property
    def dsa_ext_effective_rate(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.dsa_ext_effective_rate

    @cached_property
    def pv_stress_bounds_new_forex_borrowing_gross_usd(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_bounds_new_forex_borrowing_gross_usd

    @cached_property
    def pv_stress_bounds_cumulative(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_bounds_cumulative

    @cached_property
    def pv_stress_bounds_stock_of_new_forex_debt_in_usd(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_bounds_stock_of_new_forex_debt_in_usd

    @cached_property
    def pv_stress_bounds_interest(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_bounds_interest

    @cached_property
    def pv_stress_bounds_amortization(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_bounds_amortization

    @cached_property
    def pv_stress_bounds_cumulative_selected_by_t_g_0(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_bounds_cumulative_selected_by_t_g_0

    @cached_property
    def pv_stress_bounds_cumulative_selected_by_t_m_condition(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_bounds_cumulative_selected_by_t_m_condition

    @cached_property
    def pv_stress_new_forex_borrowing_gross_usd(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_new_forex_borrowing_gross_usd

    @cached_property
    def pv_stress_cumulative(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_cumulative

    @cached_property
    def pv_stress_stock_of_new_forex_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_stock_of_new_forex_debt

    @cached_property
    def pv_stress_interest(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_interest

    @cached_property
    def pv_stress_amortization(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_amortization

    @cached_property
    def pv_stress_cumulative_selected_t_g_0(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_cumulative_selected_t_g_0

    @cached_property
    def pv_stress_cumulative_selected_t_m_condition(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_external_debt_nominal_1.pv_stress_cumulative_selected_t_m_condition

    @cached_property
    def _scan_dsa_ext_non_interest_current_account_deficit(self) -> internals.ScanDsaExtNonInterestCurrentAccountDeficitResult:
        return internals.scan_dsa_ext_non_interest_current_account_deficit(lookup_ida_terms_old=data.LOOKUP_IDA_TERMS_OLD, input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, dsa_ext_depreciation_of_nc_depreciation=self.dsa_ext_depreciation_of_nc_depreciation, dsa_ext_standard_test_gdp_growth_rule_primary=self.dsa_ext_standard_test_gdp_growth_rule_primary, dsa_ext_standard_test_export_growth_rule=self.dsa_ext_standard_test_export_growth_rule, dsa_ext_standard_test_current_transfers_rule=self.dsa_ext_standard_test_current_transfers_rule, dsa_ext_standard_test_current_transfers_rule_b6_mkt=self.dsa_ext_standard_test_current_transfers_rule_b6_mkt, dsa_ext_standard_test_current_transfers_rule_b6_nonmkt=self.dsa_ext_standard_test_current_transfers_rule_b6_nonmkt, dsa_ext_standard_test_fdi_rule=self.dsa_ext_standard_test_fdi_rule, dsa_ext_standard_test_fdi_rule_b6_mkt=self.dsa_ext_standard_test_fdi_rule_b6_mkt, dsa_ext_standard_test_fdi_rule_b6_nonmkt=self.dsa_ext_standard_test_fdi_rule_b6_nonmkt, dsa_ext_standard_test_gdp_growth_rule=self.dsa_ext_standard_test_gdp_growth_rule, dsa_ext_standard_test_exports_rule=self.dsa_ext_standard_test_exports_rule, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, macro_debt_total_ext_debt_interest_due_include_interest=self.macro_debt_total_ext_debt_interest_due_include_interest, macro_debt_us_dollars_k=self.macro_debt_us_dollars_k, macro_debt_us_dollars_v=self.macro_debt_us_dollars_v, macro_debt_exports_of_goods_services=self.macro_debt_exports_of_goods_services, macro_debt_imports_of_goods_services_use_positive_values=self.macro_debt_imports_of_goods_services_use_positive_values, macro_debt_us_dollars_by_year_k=self.macro_debt_us_dollars_by_year_k, macro_debt_us_dollars_by_year_v=self.macro_debt_us_dollars_by_year_v, macro_debt_main_assumptions_us_dollars_k=self.macro_debt_main_assumptions_us_dollars_k, macro_debt_main_assumptions_us_dollars_v=self.macro_debt_main_assumptions_us_dollars_v, macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_gdp_constant_prices=self.macro_debt_gdp_constant_prices, macro_debt_change_in_gdp_deflator_factor=self.macro_debt_change_in_gdp_deflator_factor, macro_debt_change_in_gdp_deflator_factor_by_year=self.macro_debt_change_in_gdp_deflator_factor_by_year, macro_debt_us_gdp_deflator_percent_change=self.macro_debt_us_gdp_deflator_percent_change, leftover_us_gdp_deflator=self.leftover_us_gdp_deflator, leftover_export_growth_usd=self.leftover_export_growth_usd, leftover_fdi_gdp=self.leftover_fdi_gdp, b1_gdp_ext_ii_key_macroeconomic_assumptions=self.b1_gdp_ext_ii_key_macroeconomic_assumptions, b3_exports_ext_iii_averages_standard_deviations=self.b3_exports_ext_iii_averages_standard_deviations, b4_otherflows_ext_ii_key_macroeconomic_assumptions=self.b4_otherflows_ext_ii_key_macroeconomic_assumptions, b6_combo_mkt_ext_ii_key_macroeconomic_assumptions=self.b6_combo_mkt_ext_ii_key_macroeconomic_assumptions, b6_combo_mkt_ext_y1_includes_both_public_nominal_debt_baseline=self.b6_combo_mkt_ext_y1_includes_both_public_nominal_debt_baseline, b6_combo_mkt_ext_y1_includes_both_public_nominal_debt_stress=self.b6_combo_mkt_ext_y1_includes_both_public_nominal_debt_stress, b6_combo_mkt_ext_y1_includes_both_public_private_sector_ext_debt=self.b6_combo_mkt_ext_y1_includes_both_public_private_sector_ext_debt, b6_combo_mkt_ext_y1_includes_both_public_pv_total=self.b6_combo_mkt_ext_y1_includes_both_public_pv_total, b6_combo_nonmkt_ext_ii_key_macroeconomic_assumptions=self.b6_combo_nonmkt_ext_ii_key_macroeconomic_assumptions, b6_combo_nonmkt_ext_increase=self.b6_combo_nonmkt_ext_increase, b6_combo_nonmkt_ext_y7_long_run_constant_balance_that_stabilizes=self.b6_combo_nonmkt_ext_y7_long_run_constant_balance_that_stabilizes, b6_combo_nonmkt_ext_y7_long_run_constant_private_debt_pv=self.b6_combo_nonmkt_ext_y7_long_run_constant_private_debt_pv, b6_combo_nonmkt_ext_y7_long_run_constant_pv_total=self.b6_combo_nonmkt_ext_y7_long_run_constant_pv_total, c3_commodity_ext_ii_key_macroeconomic_assumptions=self.c3_commodity_ext_ii_key_macroeconomic_assumptions, c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions=self.c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions, c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_2=self.c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_2, c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_3=self.c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_3, c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_4=self.c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_4, c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_5=self.c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_5, leftover_official_transfers_gdp=self.leftover_official_transfers_gdp, leftover_real_gdp_growth_2=self.leftover_real_gdp_growth_2, leftover_us_gdp_deflator_2=self.leftover_us_gdp_deflator_2)

    @cached_property
    def dsa_ext_non_interest_current_account_deficit(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_non_interest_current_account_deficit

    @cached_property
    def dsa_ext_exports(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_exports

    @cached_property
    def dsa_ext_net_fdi_negative_inflow(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_net_fdi_negative_inflow

    @cached_property
    def dsa_ext_nominal_gdp_million_of_us_dollars(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_nominal_gdp_million_of_us_dollars

    @cached_property
    def dsa_ext_real_gdp_growth_in_percent(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_real_gdp_growth_in_percent

    @cached_property
    def dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent

    @cached_property
    def dsa_ext_exports_usd_millions(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_exports_usd_millions

    @cached_property
    def dsa_ext_reference_historical_statistics(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_reference_historical_statistics

    @cached_property
    def dsa_ext_historical_statistics(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_historical_statistics

    @cached_property
    def dsa_ext_historical_statistics_baseline(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_historical_statistics_baseline

    @cached_property
    def dsa_ext_deficit_in_balance_of_goods_and_services(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_deficit_in_balance_of_goods_and_services

    @cached_property
    def dsa_ext_imports(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_imports

    @cached_property
    def dsa_ext_net_current_transfers_negative_inflow(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_net_current_transfers_negative_inflow

    @cached_property
    def dsa_ext_other_current_account_flows_negative_net_inflow(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_other_current_account_flows_negative_net_inflow

    @cached_property
    def dsa_ext_growth_of_exports_of_g_s_us_dollar_terms_in_percent(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_growth_of_exports_of_g_s_us_dollar_terms_in_percent

    @cached_property
    def dsa_ext_export_shock_sign_flags(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_export_shock_sign_flags

    @cached_property
    def dsa_ext_real_depreciation_identity(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_non_interest_current_account_deficit.dsa_ext_real_depreciation_identity

    @cached_property
    def dsa_ext_denominator_1_g_g(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_denominator_1_g_g(dsa_ext_real_gdp_growth_in_percent=self.dsa_ext_real_gdp_growth_in_percent, dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent=self.dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent)

    @cached_property
    def dsa_ext_pv_of_ppg_external_debt_to_gdp_ratio(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_pv_of_ppg_external_debt_to_gdp_ratio(dsa_ext_nominal_gdp_million_of_us_dollars=self.dsa_ext_nominal_gdp_million_of_us_dollars, dsa_ext_pv_ppg_stress=self.dsa_ext_pv_ppg_stress, ext_debt_total_pv_of_debt=self.ext_debt_total_pv_of_debt)

    @cached_property
    def dsa_ext_pv_of_ppg_external_debt_to_exports_ratio(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_pv_of_ppg_external_debt_to_exports_ratio(dsa_ext_exports=self.dsa_ext_exports, dsa_ext_pv_of_ppg_external_debt_to_gdp_ratio=self.dsa_ext_pv_of_ppg_external_debt_to_gdp_ratio)

    @cached_property
    def dsa_ext_ppg_debt_service_to_exports_ratio(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_ppg_debt_service_to_exports_ratio(dsa_ext_ppg_debt_service_stress=self.dsa_ext_ppg_debt_service_stress, dsa_ext_exports_usd_millions=self.dsa_ext_exports_usd_millions, dsa_ext_total_external_debt_service_to_exports_ratio=self.dsa_ext_total_external_debt_service_to_exports_ratio, macro_debt_private_debt_service_pct_exports=self.macro_debt_private_debt_service_pct_exports)

    @cached_property
    def dsa_ext_ppg_debt_service_to_revenue_ratio(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_ppg_debt_service_to_revenue_ratio(dsa_ext_ppg_debt_service_to_exports_ratio=self.dsa_ext_ppg_debt_service_to_exports_ratio, dsa_ext_ppg_debt_service_stress=self.dsa_ext_ppg_debt_service_stress, dsa_ext_revenue=self.dsa_ext_revenue, macro_debt_exports_of_goods_services=self.macro_debt_exports_of_goods_services, macro_debt_national_currency_us_dollars=self.macro_debt_national_currency_us_dollars)

    @cached_property
    def dsa_ext_share_of_local_currency_denominated_external_debt_to_total_external_debt(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_share_of_local_currency_denominated_external_debt_to_total_external_debt(dsa_ext_share_of_local_currency_denominated_external_debt_to_total_external_debt_baseline=self.dsa_ext_share_of_local_currency_denominated_external_debt_to_total_external_debt_baseline)

    @cached_property
    def dsa_ext_share_of_local_currency_denominated_external_debt_to_total_external_debt_baseline(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_share_of_local_currency_denominated_external_debt_to_total_external_debt_baseline(macro_debt_share_of_local_currency_denominated_external=self.macro_debt_share_of_local_currency_denominated_external)

    @cached_property
    def _scan_dsa_ext_depreciation_of_nc_depreciation(self) -> internals.ScanDsaExtDepreciationOfNcDepreciationResult:
        return internals.scan_dsa_ext_depreciation_of_nc_depreciation(lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, in6opt_standard_nominal_depreciation_close_real_overvaluation=self.in6opt_standard_nominal_depreciation_close_real_overvaluation, macro_debt_depreciation_of_nc_depreciation=self.macro_debt_depreciation_of_nc_depreciation)

    @cached_property
    def dsa_ext_depreciation_of_nc_depreciation(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_depreciation_of_nc_depreciation.dsa_ext_depreciation_of_nc_depreciation

    @cached_property
    def dsa_ext_standard_test_fx_depreciation(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_depreciation_of_nc_depreciation.dsa_ext_standard_test_fx_depreciation

    @cached_property
    def in6opt_standard_size_of_fx_depreciation_shock(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_depreciation_of_nc_depreciation.in6opt_standard_size_of_fx_depreciation_shock

    @cached_property
    def in6opt_standard_b6_combination_size_of_fx_depreciation_shock(self) -> data.Series[float | str | None]:
        return self._scan_dsa_ext_depreciation_of_nc_depreciation.in6opt_standard_b6_combination_size_of_fx_depreciation_shock

    @cached_property
    def dsa_ext_pv_ppg_baseline(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_pv_ppg_baseline(ext_debt_total_pv_of_debt=self.ext_debt_total_pv_of_debt)

    @cached_property
    def dsa_ext_pv_of_additional_borrowing(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_pv_of_additional_borrowing(pv_stress_bounds_pv_of_new_forex_debt_in_usd=self.pv_stress_bounds_pv_of_new_forex_debt_in_usd, pv_stress_pv_of_new_forex_debt=self.pv_stress_pv_of_new_forex_debt)

    @cached_property
    def dsa_ext_pv_ppg_stress(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_pv_ppg_stress(dsa_ext_pv_ppg_baseline=self.dsa_ext_pv_ppg_baseline, dsa_ext_pv_of_additional_borrowing=self.dsa_ext_pv_of_additional_borrowing)

    @cached_property
    def dsa_ext_o_w_interest_baseline(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_o_w_interest_baseline(macro_debt_total_ext_debt_interest_due_include_interest=self.macro_debt_total_ext_debt_interest_due_include_interest)

    @cached_property
    def dsa_ext_debt_service_ppg_baseline(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_debt_service_ppg_baseline(ext_debt_total_public_debt_service=self.ext_debt_total_public_debt_service)

    @cached_property
    def dsa_ext_additional_debt_service_stress(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_additional_debt_service_stress(dsa_ext_debt_services_associated_with_new_external_borrowing=self.dsa_ext_debt_services_associated_with_new_external_borrowing, pv_stress_bounds_total_debt_service_in_usd=self.pv_stress_bounds_total_debt_service_in_usd, pv_stress_total_debt_service=self.pv_stress_total_debt_service)

    @cached_property
    def dsa_ext_ppg_debt_service_stress(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_ppg_debt_service_stress(dsa_ext_debt_service_ppg_baseline=self.dsa_ext_debt_service_ppg_baseline, dsa_ext_additional_debt_service_stress=self.dsa_ext_additional_debt_service_stress)

    @cached_property
    def dsa_ext_revenue(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_revenue(dsa_ext_nominal_gdp_million_of_us_dollars=self.dsa_ext_nominal_gdp_million_of_us_dollars, dsa_ext_revenue_gdp_stress_stress=self.dsa_ext_revenue_gdp_stress_stress, dsa_ext_government_revenues_excluding_grants_in_percent_of_gdp=self.dsa_ext_government_revenues_excluding_grants_in_percent_of_gdp)

    @cached_property
    def dsa_ext_standard_test_gdp_growth_rule_primary(self) -> str | int | float | bool:
        return internals.dsa_ext_standard_test_gdp_growth_rule_primary(in6opt_standard_historical_average_baseline_projection=self.in6opt_standard_historical_average_baseline_projection, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_ext_standard_test_export_growth_rule(self) -> str | int | float | bool:
        return internals.dsa_ext_standard_test_export_growth_rule(in6opt_standard_b3_exports_historical_average_baseline_projection=self.in6opt_standard_b3_exports_historical_average_baseline_projection, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_ext_standard_test_current_transfers_rule(self) -> str | int | float | bool:
        return internals.dsa_ext_standard_test_current_transfers_rule(in6opt_standard_historical_average_baseline_projection_current_transfers_b4_other_non_debt_creating_flows=self.in6opt_standard_historical_average_baseline_projection_current_transfers_b4_other_non_debt_creating_flows, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_ext_standard_test_current_transfers_rule_b6_mkt(self) -> str | int | float | bool:
        return internals.dsa_ext_standard_test_current_transfers_rule_b6_mkt(in6opt_standard_historical_average_baseline_projection_current_transfers_b6_combination=self.in6opt_standard_historical_average_baseline_projection_current_transfers_b6_combination, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_ext_standard_test_current_transfers_rule_b6_nonmkt(self) -> str | int | float | bool:
        return internals.dsa_ext_standard_test_current_transfers_rule_b6_nonmkt(in6opt_standard_historical_average_baseline_projection_current_transfers_b6_combination=self.in6opt_standard_historical_average_baseline_projection_current_transfers_b6_combination, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_ext_standard_test_fdi_rule(self) -> str | int | float | bool:
        return internals.dsa_ext_standard_test_fdi_rule(in6opt_standard_historical_average_baseline_projection_fdi_b4_other_non_debt_creating_flows=self.in6opt_standard_historical_average_baseline_projection_fdi_b4_other_non_debt_creating_flows, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_ext_standard_test_fdi_rule_b6_mkt(self) -> str | int | float | bool:
        return internals.dsa_ext_standard_test_fdi_rule_b6_mkt(in6opt_standard_historical_average_baseline_projection_fdi_b6_combination=self.in6opt_standard_historical_average_baseline_projection_fdi_b6_combination, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_ext_standard_test_fdi_rule_b6_nonmkt(self) -> str | int | float | bool:
        return internals.dsa_ext_standard_test_fdi_rule_b6_nonmkt(in6opt_standard_historical_average_baseline_projection_fdi_b6_combination=self.in6opt_standard_historical_average_baseline_projection_fdi_b6_combination, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_ext_debt_services_associated_with_new_external_borrowing(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_debt_services_associated_with_new_external_borrowing(pv_base_add_cost_mkt_shock_addition_nominal_interest_payments_on_external_debt=self.pv_base_add_cost_mkt_shock_addition_nominal_interest_payments_on_external_debt)

    @cached_property
    def dsa_ext_o_w_interest_additional_borrowing(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_o_w_interest_additional_borrowing(pv_base_add_cost_mkt_shock_addition_nominal_interest_payments_on_external_debt=self.pv_base_add_cost_mkt_shock_addition_nominal_interest_payments_on_external_debt)

    @cached_property
    def dsa_ext_standard_test_gdp_growth_rule(self) -> data.Series[str | int | float | bool | None]:
        return internals.dsa_ext_standard_test_gdp_growth_rule(in6opt_standard_historical_average_baseline_projection_real_gdp_b6_combination=self.in6opt_standard_historical_average_baseline_projection_real_gdp_b6_combination, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_ext_standard_test_exports_rule(self) -> data.Series[str | int | float | bool | None]:
        return internals.dsa_ext_standard_test_exports_rule(in6opt_standard_historical_average_baseline_projection_exports_b6_combination=self.in6opt_standard_historical_average_baseline_projection_exports_b6_combination, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_ext_revenue_gdp_stress_stress(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_revenue_gdp_stress_stress(dsa_ext_government_revenues_excluding_grants_in_percent_of_gdp=self.dsa_ext_government_revenues_excluding_grants_in_percent_of_gdp, leftover_us_gdp_deflator=self.leftover_us_gdp_deflator, c3_commodity_ext_ii_key_macroeconomic_assumptions=self.c3_commodity_ext_ii_key_macroeconomic_assumptions)

    @cached_property
    def dsa_ext_of_which_public_and_publicly_guaranteed_ppg(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_of_which_public_and_publicly_guaranteed_ppg(macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc, macro_debt_total_public_ext_debt=self.macro_debt_total_public_ext_debt)

    @cached_property
    def dsa_ext_of_which_private(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_of_which_private(macro_debt_private_debt_pct_gdp=self.macro_debt_private_debt_pct_gdp)

    @cached_property
    def dsa_ext_total_external_debt_service_to_exports_ratio(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_total_external_debt_service_to_exports_ratio(macro_debt_private_sector_short_term=self.macro_debt_private_sector_short_term, macro_debt_total_ext_debt_interest_due_include_interest=self.macro_debt_total_ext_debt_interest_due_include_interest, macro_debt_total_external_amortization_due_include=self.macro_debt_total_external_amortization_due_include, macro_debt_exports_of_goods_services=self.macro_debt_exports_of_goods_services)

    @cached_property
    def dsa_ext_government_revenues_excluding_grants_in_percent_of_gdp(self) -> data.Series[float | str | None]:
        return internals.dsa_ext_government_revenues_excluding_grants_in_percent_of_gdp(macro_debt_revenues_pct_gdp=self.macro_debt_revenues_pct_gdp)

    @cached_property
    def _scan_dsa_pub_public_sector_debt_1(self) -> internals.ScanDsaPubPublicSectorDebt1Result:
        return internals.scan_dsa_pub_public_sector_debt_1(dsa_pub_of_which_external_debt=self.dsa_pub_of_which_external_debt, dsa_pub_primary_deficit=self.dsa_pub_primary_deficit, dsa_pub_contribution_from_real_exchange_rate_depreciation=self.dsa_pub_contribution_from_real_exchange_rate_depreciation, dsa_pub_denominator_1_g=self.dsa_pub_denominator_1_g, dsa_pub_other_identified_debt_creating_flows=self.dsa_pub_other_identified_debt_creating_flows, dsa_pub_residual=self.dsa_pub_residual, dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, dsa_pub_real_gdp_growth_in_percent=self.dsa_pub_real_gdp_growth_in_percent, dsa_pub_average_real_interest_rate_on_external_debt_in_percent=self.dsa_pub_average_real_interest_rate_on_external_debt_in_percent, dsa_pub_inflation_rate_gdp_deflator_in_percent=self.dsa_pub_inflation_rate_gdp_deflator_in_percent, dsa_pub_total_public_external_debt=self.dsa_pub_total_public_external_debt, dsa_pub_domestic_debt=self.dsa_pub_domestic_debt, macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc, macro_debt_total_public_debt_outstanding_year_end=self.macro_debt_total_public_debt_outstanding_year_end, pv_resfin_pub_assumptions_average_interest_rate_on_domestic_debt=self.pv_resfin_pub_assumptions_average_interest_rate_on_domestic_debt)

    @cached_property
    def dsa_pub_public_sector_debt_1(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_public_sector_debt_1

    @cached_property
    def dsa_pub_change_in_public_sector_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_change_in_public_sector_debt

    @cached_property
    def dsa_pub_identified_debt_creating_flows(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_identified_debt_creating_flows

    @cached_property
    def dsa_pub_automatic_debt_dynamics(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_automatic_debt_dynamics

    @cached_property
    def dsa_pub_contribution_from_interest_rate_growth_differential(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_contribution_from_interest_rate_growth_differential

    @cached_property
    def dsa_pub_of_which_contribution_from_average_real_interest_rate(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_of_which_contribution_from_average_real_interest_rate

    @cached_property
    def dsa_pub_of_which_contribution_from_real_gdp_growth(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_of_which_contribution_from_real_gdp_growth

    @cached_property
    def dsa_pub_average_nominal_interest_rate_on_domestic_debt_in_percent(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_average_nominal_interest_rate_on_domestic_debt_in_percent

    @cached_property
    def dsa_pub_average_real_interest_rate_in_percent(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_average_real_interest_rate_in_percent

    @cached_property
    def dsa_pub_average_real_interest_rate_on_domestic_debt_in_percent(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_average_real_interest_rate_on_domestic_debt_in_percent

    @cached_property
    def dsa_pub_nominal_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_nominal_debt

    @cached_property
    def dsa_pub_total_public_domestic_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_public_sector_debt_1.dsa_pub_total_public_domestic_debt

    @cached_property
    def dsa_pub_of_which_external_debt(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_of_which_external_debt(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, dsa_pub_total_public_external_debt=self.dsa_pub_total_public_external_debt)

    @cached_property
    def dsa_pub_pv_of_total_public_debt(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_pv_of_total_public_debt(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, dsa_pub_total_public_domestic_debt=self.dsa_pub_total_public_domestic_debt, dsa_pub_pv_of_public_sector_external_debt_end_of_period=self.dsa_pub_pv_of_public_sector_external_debt_end_of_period)

    @cached_property
    def dsa_pub_primary_deficit(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_primary_deficit(b6_combo_non_mkt_pub_gdp_shock_label=data.B6_COMBO_NON_MKT_PUB_GDP_SHOCK_LABEL, input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, dsa_pub_revenue_and_grants=self.dsa_pub_revenue_and_grants, dsa_pub_primary_noninterest_expenditure=self.dsa_pub_primary_noninterest_expenditure, dsa_pub_standard_test_parameter=self.dsa_pub_standard_test_parameter, dsa_pub_b2_pb_non_mkt_pub_standard_test_parameter=self.dsa_pub_b2_pb_non_mkt_pub_standard_test_parameter, dsa_pub_standard_test_pb_rule=self.dsa_pub_standard_test_pb_rule, dsa_pub_b6_combo_non_mkt_pub_standard_test_pb_rule=self.dsa_pub_b6_combo_non_mkt_pub_standard_test_pb_rule, a1_hist_pub_historical_statistics=self.a1_hist_pub_historical_statistics, baseline_pub_primary_deficit=self.baseline_pub_primary_deficit, leftover_primary_deficit=self.leftover_primary_deficit, leftover_revenue_gdp=self.leftover_revenue_gdp, b2_pb_mkt_pub_i_baseline_medium_term_projections=self.b2_pb_mkt_pub_i_baseline_medium_term_projections, b2_pb_nonmkt_pub_i_baseline_medium_term_projections=self.b2_pb_nonmkt_pub_i_baseline_medium_term_projections)

    @cached_property
    def dsa_pub_revenue_and_grants(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_revenue_and_grants(dsa_pub_of_which_grants=self.dsa_pub_of_which_grants, dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, baseline_pub_revenue_grants=self.baseline_pub_revenue_grants, baseline_pub_of_which_grants=self.baseline_pub_of_which_grants, macro_debt_public_sector_revenues_including_grants=self.macro_debt_public_sector_revenues_including_grants, leftover_real_interest_rate=self.leftover_real_interest_rate, c3_commodity_pub_historical_statistics_key_variables_past_10=self.c3_commodity_pub_historical_statistics_key_variables_past_10)

    @cached_property
    def dsa_pub_of_which_grants(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_of_which_grants(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, macro_debt_public_sector_grants=self.macro_debt_public_sector_grants)

    @cached_property
    def dsa_pub_primary_noninterest_expenditure(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_primary_noninterest_expenditure(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, baseline_pub_primary_noninterest_expenditure=self.baseline_pub_primary_noninterest_expenditure, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc)

    @cached_property
    def dsa_pub_contribution_from_real_exchange_rate_depreciation(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_contribution_from_real_exchange_rate_depreciation(dsa_pub_of_which_external_debt=self.dsa_pub_of_which_external_debt, dsa_pub_denominator_1_g=self.dsa_pub_denominator_1_g, dsa_pub_average_real_interest_rate_on_external_debt_in_percent=self.dsa_pub_average_real_interest_rate_on_external_debt_in_percent, dsa_pub_real_exchange_rate_depreciation_in_percent_indicates_depreciation=self.dsa_pub_real_exchange_rate_depreciation_in_percent_indicates_depreciation)

    @cached_property
    def dsa_pub_denominator_1_g(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_denominator_1_g(dsa_pub_real_gdp_growth_in_percent=self.dsa_pub_real_gdp_growth_in_percent)

    @cached_property
    def dsa_pub_other_identified_debt_creating_flows(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_other_identified_debt_creating_flows(dsa_pub_privatization_receipts_negative=self.dsa_pub_privatization_receipts_negative, dsa_pub_recognition_of_contingent_liabilities_e_g_bank_recapitalization=self.dsa_pub_recognition_of_contingent_liabilities_e_g_bank_recapitalization, dsa_pub_debt_relief_hipc_and_other=self.dsa_pub_debt_relief_hipc_and_other, dsa_pub_other_debt_creating_or_reducing_flow_please_specify=self.dsa_pub_other_debt_creating_or_reducing_flow_please_specify)

    @cached_property
    def dsa_pub_privatization_receipts_negative(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_privatization_receipts_negative(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, baseline_pub_privatization_receipts_negative=self.baseline_pub_privatization_receipts_negative, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc)

    @cached_property
    def dsa_pub_recognition_of_contingent_liabilities_e_g_bank_recapitalization(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_recognition_of_contingent_liabilities_e_g_bank_recapitalization(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, baseline_pub_recognition_of_contingent_liab_e_g_bank=self.baseline_pub_recognition_of_contingent_liab_e_g_bank, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc)

    @cached_property
    def dsa_pub_debt_relief_hipc_and_other(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_debt_relief_hipc_and_other(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, baseline_pub_debt_relief_hipc_other=self.baseline_pub_debt_relief_hipc_other, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc)

    @cached_property
    def dsa_pub_other_debt_creating_or_reducing_flow_please_specify(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_other_debt_creating_or_reducing_flow_please_specify(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, dsa_pub_old_new_scenario_total=self.dsa_pub_old_new_scenario_total, baseline_pub_other_debt_creating_reducing_flow_please_specify=self.baseline_pub_other_debt_creating_reducing_flow_please_specify, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, c2_natdisaster_historical_statistics_key_variables_past_10=self.c2_natdisaster_historical_statistics_key_variables_past_10)

    @cached_property
    def dsa_pub_residual(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_residual(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, baseline_pub_residual=self.baseline_pub_residual, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc)

    @cached_property
    def dsa_pub_nominal_gdp_local_currency(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_nominal_gdp_local_currency(dsa_pub_real_gdp_growth_in_percent=self.dsa_pub_real_gdp_growth_in_percent, dsa_pub_inflation_rate_gdp_deflator_in_percent=self.dsa_pub_inflation_rate_gdp_deflator_in_percent, macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def dsa_pub_real_gdp_growth_in_percent(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_real_gdp_growth_in_percent(a1_hist_pub_historical_statistics=self.a1_hist_pub_historical_statistics, input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, dsa_ext_real_gdp_growth_in_percent=self.dsa_ext_real_gdp_growth_in_percent, dsa_pub_standard_test_parameter=self.dsa_pub_standard_test_parameter, dsa_pub_standard_test_gdp_growth_rule=self.dsa_pub_standard_test_gdp_growth_rule, dsa_pub_b6_combo_non_mkt_pub_standard_test_gdp_growth_rule=self.dsa_pub_b6_combo_non_mkt_pub_standard_test_gdp_growth_rule, baseline_pub_real_gdp_growth=self.baseline_pub_real_gdp_growth, leftover_real_gdp_growth=self.leftover_real_gdp_growth, b1_gdp_pub_key_macroeconomic_fiscal_assumptions=self.b1_gdp_pub_key_macroeconomic_fiscal_assumptions, b6_combo_mkt_pub_i_baseline_medium_term_projections=self.b6_combo_mkt_pub_i_baseline_medium_term_projections, b6_combo_nonmkt_pub_i_baseline_medium_term_projections=self.b6_combo_nonmkt_pub_i_baseline_medium_term_projections, leftover_nominal_interest_rate=self.leftover_nominal_interest_rate)

    @cached_property
    def dsa_pub_average_nominal_interest_rate_on_external_debt_in_percent(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_average_nominal_interest_rate_on_external_debt_in_percent(dsa_pub_total_public_external_debt=self.dsa_pub_total_public_external_debt, dsa_pub_external_debt=self.dsa_pub_external_debt, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def dsa_pub_average_real_interest_rate_on_external_debt_in_percent(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_average_real_interest_rate_on_external_debt_in_percent(dsa_pub_average_nominal_interest_rate_on_external_debt_in_percent=self.dsa_pub_average_nominal_interest_rate_on_external_debt_in_percent, dsa_pub_us_inflation_rate_gdp_deflator_in_percent=self.dsa_pub_us_inflation_rate_gdp_deflator_in_percent)

    @cached_property
    def _scan_dsa_pub_exchange_rate_lc_per_us_dollar(self) -> internals.ScanDsaPubExchangeRateLcPerUsDollarResult:
        return internals.scan_dsa_pub_exchange_rate_lc_per_us_dollar(dsa_pub_b5_depreciation_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent=self.dsa_pub_b5_depreciation_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent, baseline_pub_exchange_rate_lc_per_us_dollar=self.baseline_pub_exchange_rate_lc_per_us_dollar, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar)

    @cached_property
    def dsa_pub_exchange_rate_lc_per_us_dollar(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_exchange_rate_lc_per_us_dollar.dsa_pub_exchange_rate_lc_per_us_dollar

    @cached_property
    def dsa_pub_b5_depreciation_pub_exchange_rate_us_dollar_per_lc(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_exchange_rate_lc_per_us_dollar.dsa_pub_b5_depreciation_pub_exchange_rate_us_dollar_per_lc

    @cached_property
    def dsa_pub_nominal_depreciation_of_local_currency_percentage_change_in_lc_per_dollar(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_nominal_depreciation_of_local_currency_percentage_change_in_lc_per_dollar(dsa_pub_exchange_rate_lc_per_us_dollar=self.dsa_pub_exchange_rate_lc_per_us_dollar)

    @cached_property
    def dsa_pub_real_exchange_rate_depreciation_in_percent_indicates_depreciation(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_real_exchange_rate_depreciation_in_percent_indicates_depreciation(dsa_pub_nominal_depreciation_of_local_currency_percentage_change_in_lc_per_dollar=self.dsa_pub_nominal_depreciation_of_local_currency_percentage_change_in_lc_per_dollar, dsa_pub_inflation_rate_gdp_deflator_in_percent=self.dsa_pub_inflation_rate_gdp_deflator_in_percent, dsa_pub_us_inflation_rate_gdp_deflator_in_percent=self.dsa_pub_us_inflation_rate_gdp_deflator_in_percent)

    @cached_property
    def dsa_pub_inflation_rate_gdp_deflator_in_percent(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_inflation_rate_gdp_deflator_in_percent(a1_hist_pub_historical_statistics=self.a1_hist_pub_historical_statistics, dsa_ext_exports=self.dsa_ext_exports, dsa_pub_real_gdp_growth_in_percent=self.dsa_pub_real_gdp_growth_in_percent, dsa_pub_b5_depreciation_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent=self.dsa_pub_b5_depreciation_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent, dsa_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent=self.dsa_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent, dsa_pub_b6_combo_non_mkt_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent=self.dsa_pub_b6_combo_non_mkt_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent, dsa_pub_c3_commodity_prices_pub_decline_in_gdp_deflator=self.dsa_pub_c3_commodity_prices_pub_decline_in_gdp_deflator, baseline_pub_real_gdp_growth=self.baseline_pub_real_gdp_growth, baseline_pub_inflation_rate_gdp_deflator_pct=self.baseline_pub_inflation_rate_gdp_deflator_pct, leftover_real_interest_rate=self.leftover_real_interest_rate, b6_combo_mkt_pub_i_baseline_medium_term_nominal_debt=self.b6_combo_mkt_pub_i_baseline_medium_term_nominal_debt, b6_combo_nonmkt_pub_in_billions_of_lc=self.b6_combo_nonmkt_pub_in_billions_of_lc, c3_commodity_pub_historical_statistics_key_variables_past_10=self.c3_commodity_pub_historical_statistics_key_variables_past_10)

    @cached_property
    def dsa_pub_us_inflation_rate_gdp_deflator_in_percent(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_us_inflation_rate_gdp_deflator_in_percent(macro_debt_us_gdp_deflator_percent_change=self.macro_debt_us_gdp_deflator_percent_change, baseline_pub_us_inflation_rate_gdp_deflator_pct=self.baseline_pub_us_inflation_rate_gdp_deflator_pct)

    @cached_property
    def _scan_dsa_pub_of_which_short_term(self) -> internals.ScanDsaPubOfWhichShortTermResult:
        return internals.scan_dsa_pub_of_which_short_term(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, dsa_pub_exchange_rate_lc_per_us_dollar=self.dsa_pub_exchange_rate_lc_per_us_dollar, dsa_pub_primary_deficit_local_currency=self.dsa_pub_primary_deficit_local_currency, dsa_pub_other_debt_creating_flows=self.dsa_pub_other_debt_creating_flows, dsa_pub_old_new_scenario_total=self.dsa_pub_old_new_scenario_total, baseline_pub_gross_financing_need_by_year=self.baseline_pub_gross_financing_need_by_year, macro_debt_short_term=self.macro_debt_short_term, macro_debt_public_domestic_st=self.macro_debt_public_domestic_st, macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_total_public_domestic_debt_interest_due=self.macro_debt_total_public_domestic_debt_interest_due, macro_debt_total_mlt_public_domestic_debt_amortization_debt=self.macro_debt_total_mlt_public_domestic_debt_amortization_debt, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6, c2_natdisaster_historical_statistics_key_variables_past_10=self.c2_natdisaster_historical_statistics_key_variables_past_10, pv_resfin_pub_assumptions_share_of_marginal_debt=self.pv_resfin_pub_assumptions_share_of_marginal_debt, pv_resfin_pub_assumptions_avg_nominal_interest_rate_on_new_borrowing_in_usd=self.pv_resfin_pub_assumptions_avg_nominal_interest_rate_on_new_borrowing_in_usd, pv_resfin_pub_assumptions_avg_maturity_incl_grace_period=self.pv_resfin_pub_assumptions_avg_maturity_incl_grace_period, pv_resfin_pub_assumptions_avg_grace_period=self.pv_resfin_pub_assumptions_avg_grace_period, pv_resfin_pub_assumptions_domestic_mlt_debt=self.pv_resfin_pub_assumptions_domestic_mlt_debt, pv_resfin_pub_assumptions_avg_interest_rate=self.pv_resfin_pub_assumptions_avg_interest_rate, pv_resfin_pub_assumptions_exchange_rate_pa=self.pv_resfin_pub_assumptions_exchange_rate_pa, pv_resfin_pub_output_new_borrowing_under_the_external_dsa_in_usd=self.pv_resfin_pub_output_new_borrowing_under_the_external_dsa_in_usd, pv_resfin_pub_output_t_g_0=self.pv_resfin_pub_output_t_g_0, pv_resfin_pub_output_t_m_condition=self.pv_resfin_pub_output_t_m_condition, pv_resfin_add_assumptions_share_of_marginal_debt=self.pv_resfin_add_assumptions_share_of_marginal_debt, pv_resfin_add_assumptions_avg_maturity_incl_grace_period=self.pv_resfin_add_assumptions_avg_maturity_incl_grace_period, pv_resfin_add_assumptions_avg_grace_period=self.pv_resfin_add_assumptions_avg_grace_period, pv_resfin_add_opening_percent_of_face=data.PV_RESFIN_ADD_OPENING_PERCENT_OF_FACE, pv_resfin_add_output_t_g_0=self.pv_resfin_add_output_t_g_0, pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_two_year_average=self.pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_two_year_average, pv_resfin_add_output_t_m_condition=self.pv_resfin_add_output_t_m_condition, pv_resfin_add_int_cost_mkt_additional_domestic_interest_rate_two_year_average=self.pv_resfin_add_int_cost_mkt_additional_domestic_interest_rate_two_year_average)

    @cached_property
    def dsa_pub_of_which_short_term(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.dsa_pub_of_which_short_term

    @cached_property
    def dsa_pub_amortization_excluding_st_domestic_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.dsa_pub_amortization_excluding_st_domestic_debt

    @cached_property
    def dsa_pub_interest_expenditure(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.dsa_pub_interest_expenditure

    @cached_property
    def dsa_pub_domestic_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.dsa_pub_domestic_debt

    @cached_property
    def dsa_pub_external_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.dsa_pub_external_debt

    @cached_property
    def dsa_pub_gross_financing_need_in_local_currency(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.dsa_pub_gross_financing_need_in_local_currency

    @cached_property
    def pv_resfin_pub_output_new_borrowing_gross_in_lcu(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_new_borrowing_gross_in_lcu

    @cached_property
    def pv_resfin_pub_output_modality_of_residual_financing_1_external_2_public(self) -> data.Series[int | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_modality_of_residual_financing_1_external_2_public

    @cached_property
    def pv_resfin_pub_output_new_forex_borrowing_gross_usd(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_new_forex_borrowing_gross_usd

    @cached_property
    def pv_resfin_pub_output_cumulative(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_cumulative

    @cached_property
    def pv_resfin_pub_output_stock_of_new_forex_debt_in_usd(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_stock_of_new_forex_debt_in_usd

    @cached_property
    def pv_resfin_pub_output_interest(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_interest

    @cached_property
    def pv_resfin_pub_output_amortization(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_amortization

    @cached_property
    def pv_resfin_pub_output_cumulative_selected_by_t_g_0(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_cumulative_selected_by_t_g_0

    @cached_property
    def pv_resfin_pub_output_cumulative_selected_by_t_m_condition(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_cumulative_selected_by_t_m_condition

    @cached_property
    def pv_resfin_pub_output_new_domestic_mlt_borrowing_gross(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_new_domestic_mlt_borrowing_gross

    @cached_property
    def pv_resfin_pub_output_stock_of_new_domestic_mlt_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_stock_of_new_domestic_mlt_debt

    @cached_property
    def pv_resfin_pub_output_new_domestic_short_term_borrowing_gross_also_stock_of_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_pub_output_new_domestic_short_term_borrowing_gross_also_stock_of_debt

    @cached_property
    def pv_resfin_add_output_new_forex_borrowing_gross_usd(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_output_new_forex_borrowing_gross_usd

    @cached_property
    def pv_resfin_add_output_cumulative(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_output_cumulative

    @cached_property
    def pv_resfin_add_int_cost_mkt_cumulative_beyond_projection_window(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_int_cost_mkt_cumulative_beyond_projection_window

    @cached_property
    def pv_resfin_add_output_stock_of_new_forex_debt_in_usd(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_output_stock_of_new_forex_debt_in_usd

    @cached_property
    def pv_resfin_add_output_interest(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_output_interest

    @cached_property
    def pv_resfin_add_output_amortization(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_output_amortization

    @cached_property
    def pv_resfin_add_output_cumulative_selected_by_t_g_0(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_output_cumulative_selected_by_t_g_0

    @cached_property
    def pv_resfin_add_output_cumulative_selected_by_t_m_condition(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_output_cumulative_selected_by_t_m_condition

    @cached_property
    def pv_resfin_add_output_new_domestic_mlt_borrowing_gross(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_output_new_domestic_mlt_borrowing_gross

    @cached_property
    def pv_resfin_add_output_stock_of_new_domestic_mlt_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_output_stock_of_new_domestic_mlt_debt

    @cached_property
    def pv_resfin_add_output_new_domestic_short_term_borrowing_gross_also_stock_of_debt(self) -> data.Series[float | str | None]:
        return self._scan_dsa_pub_of_which_short_term.pv_resfin_add_output_new_domestic_short_term_borrowing_gross_also_stock_of_debt

    @cached_property
    def dsa_pub_total_public_external_debt(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_total_public_external_debt(dsa_pub_exchange_rate_lc_per_us_dollar=self.dsa_pub_exchange_rate_lc_per_us_dollar, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar, macro_debt_total_public_ext_debt=self.macro_debt_total_public_ext_debt, pv_resfin_pub_output_stock_of_new_forex_debt_in_usd=self.pv_resfin_pub_output_stock_of_new_forex_debt_in_usd)

    @cached_property
    def dsa_pub_primary_deficit_local_currency(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_primary_deficit_local_currency(dsa_pub_primary_deficit=self.dsa_pub_primary_deficit, dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency)

    @cached_property
    def dsa_pub_other_debt_creating_flows(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_other_debt_creating_flows(baseline_pub_other_identified_debt_creating_flows=self.baseline_pub_other_identified_debt_creating_flows, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc)

    @cached_property
    def dsa_pub_pv_of_public_sector_external_debt_end_of_period(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_pv_of_public_sector_external_debt_end_of_period(dsa_pub_exchange_rate_lc_per_us_dollar=self.dsa_pub_exchange_rate_lc_per_us_dollar, baseline_pub_exchange_rate_lc_per_us_dollar=self.baseline_pub_exchange_rate_lc_per_us_dollar, macro_debt_pv_of_public_sector_ext_debt_end_of_period=self.macro_debt_pv_of_public_sector_ext_debt_end_of_period, pv_resfin_pub_output_new_forex_borrowing_gross_usd=self.pv_resfin_pub_output_new_forex_borrowing_gross_usd, pv_resfin_pub_output_pv_of_new_forex_debt_in_usd=self.pv_resfin_pub_output_pv_of_new_forex_debt_in_usd, pv_resfin_add_output_pv_of_new_forex_debt_in_usd=self.pv_resfin_add_output_pv_of_new_forex_debt_in_usd)

    @cached_property
    def dsa_pub_debt_service_to_revenue_and_grants_ratio_in_percent(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_debt_service_to_revenue_and_grants_ratio_in_percent(dsa_pub_revenue_and_grants=self.dsa_pub_revenue_and_grants, dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, dsa_pub_of_which_short_term=self.dsa_pub_of_which_short_term, dsa_pub_amortization_excluding_st_domestic_debt=self.dsa_pub_amortization_excluding_st_domestic_debt, dsa_pub_interest_expenditure=self.dsa_pub_interest_expenditure)

    @cached_property
    def dsa_pub_debt_service_to_gdp_ratio_in_percent(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_debt_service_to_gdp_ratio_in_percent(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, dsa_pub_of_which_short_term=self.dsa_pub_of_which_short_term, dsa_pub_amortization_excluding_st_domestic_debt=self.dsa_pub_amortization_excluding_st_domestic_debt, dsa_pub_interest_expenditure=self.dsa_pub_interest_expenditure)

    @cached_property
    def dsa_pub_pv_of_public_debt_to_revenue_and_grants_ratio(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_pv_of_public_debt_to_revenue_and_grants_ratio(dsa_pub_pv_of_total_public_debt=self.dsa_pub_pv_of_total_public_debt, dsa_pub_revenue_and_grants=self.dsa_pub_revenue_and_grants)

    @cached_property
    def dsa_pub_standard_test_parameter(self) -> data.Series[str | int | float | bool | None]:
        return internals.dsa_pub_standard_test_parameter(in6opt_standard_historical_average_baseline_projection=self.in6opt_standard_historical_average_baseline_projection, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold, in6opt_standard_b1_real_gdp_growth_historical_average_baseline_projection=self.in6opt_standard_b1_real_gdp_growth_historical_average_baseline_projection)

    @cached_property
    def dsa_pub_pv_of_debt_gdp(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_pv_of_debt_gdp(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, dsa_pub_exchange_rate_lc_per_us_dollar=self.dsa_pub_exchange_rate_lc_per_us_dollar, dsa_pub_pv_of_public_sector_external_debt_end_of_period=self.dsa_pub_pv_of_public_sector_external_debt_end_of_period, leftover_exchange_rate_pa=self.leftover_exchange_rate_pa)

    @cached_property
    def dsa_pub_pv_of_debt_exports(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_pv_of_debt_exports(dsa_pub_exchange_rate_lc_per_us_dollar=self.dsa_pub_exchange_rate_lc_per_us_dollar, dsa_pub_pv_of_public_sector_external_debt_end_of_period=self.dsa_pub_pv_of_public_sector_external_debt_end_of_period, dsa_pub_exports_us_baseline=self.dsa_pub_exports_us_baseline)

    @cached_property
    def dsa_pub_debt_service_exports(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_debt_service_exports(dsa_pub_exports_us_baseline=self.dsa_pub_exports_us_baseline, macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6, pv_resfin_pub_output_total_debt_service_in_usd=self.pv_resfin_pub_output_total_debt_service_in_usd, pv_resfin_add_output_interest=self.pv_resfin_add_output_interest)

    @cached_property
    def dsa_pub_debt_service_revenue_excl_grants(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_debt_service_revenue_excl_grants(dsa_pub_revenue=self.dsa_pub_revenue, macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_national_currency_us_dollars=self.macro_debt_national_currency_us_dollars, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6, pv_resfin_pub_output_total_debt_service_in_usd=self.pv_resfin_pub_output_total_debt_service_in_usd, pv_resfin_add_output_interest=self.pv_resfin_add_output_interest)

    @cached_property
    def dsa_pub_exports_us_baseline(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_exports_us_baseline(macro_debt_exports_of_goods_services=self.macro_debt_exports_of_goods_services)

    @cached_property
    def dsa_pub_revenue(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_revenue(dsa_pub_revenue_and_grants=self.dsa_pub_revenue_and_grants, dsa_pub_of_which_grants=self.dsa_pub_of_which_grants, dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, leftover_exchange_rate_pa=self.leftover_exchange_rate_pa)

    @cached_property
    def dsa_pub_b2_pb_non_mkt_pub_pv_of_debt_gdp(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_b2_pb_non_mkt_pub_pv_of_debt_gdp(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, dsa_pub_exchange_rate_lc_per_us_dollar=self.dsa_pub_exchange_rate_lc_per_us_dollar, dsa_pub_pv_of_public_sector_external_debt_end_of_period=self.dsa_pub_pv_of_public_sector_external_debt_end_of_period, leftover_exchange_rate_pa=self.leftover_exchange_rate_pa)

    @cached_property
    def dsa_pub_b2_pb_non_mkt_pub_pv_of_debt_exports(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_b2_pb_non_mkt_pub_pv_of_debt_exports(dsa_pub_exchange_rate_lc_per_us_dollar=self.dsa_pub_exchange_rate_lc_per_us_dollar, dsa_pub_pv_of_public_sector_external_debt_end_of_period=self.dsa_pub_pv_of_public_sector_external_debt_end_of_period, dsa_pub_b2_pb_non_mkt_pub_exports_us_baseline=self.dsa_pub_b2_pb_non_mkt_pub_exports_us_baseline)

    @cached_property
    def dsa_pub_b2_pb_non_mkt_pub_debt_service_exports(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_b2_pb_non_mkt_pub_debt_service_exports(dsa_pub_b2_pb_non_mkt_pub_exports_us_baseline=self.dsa_pub_b2_pb_non_mkt_pub_exports_us_baseline, macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6, pv_resfin_pub_output_total_debt_service_in_usd=self.pv_resfin_pub_output_total_debt_service_in_usd)

    @cached_property
    def dsa_pub_b2_pb_non_mkt_pub_debt_service_revenue_excl_grants(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_b2_pb_non_mkt_pub_debt_service_revenue_excl_grants(dsa_pub_b2_pb_non_mkt_pub_revenue=self.dsa_pub_b2_pb_non_mkt_pub_revenue, macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6, pv_resfin_pub_output_total_debt_service_in_usd=self.pv_resfin_pub_output_total_debt_service_in_usd)

    @cached_property
    def dsa_pub_b2_pb_non_mkt_pub_exports_us_baseline(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_b2_pb_non_mkt_pub_exports_us_baseline(macro_debt_exports_of_goods_services=self.macro_debt_exports_of_goods_services)

    @cached_property
    def dsa_pub_b2_pb_non_mkt_pub_revenue(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_b2_pb_non_mkt_pub_revenue(dsa_pub_revenue_and_grants=self.dsa_pub_revenue_and_grants, dsa_pub_of_which_grants=self.dsa_pub_of_which_grants, dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, leftover_exchange_rate_pa=self.leftover_exchange_rate_pa)

    @cached_property
    def dsa_pub_b2_pb_non_mkt_pub_standard_test_parameter(self) -> str | int | float | bool:
        return internals.dsa_pub_b2_pb_non_mkt_pub_standard_test_parameter(in6opt_standard_b1_real_gdp_growth_historical_average_baseline_projection=self.in6opt_standard_b1_real_gdp_growth_historical_average_baseline_projection, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_pub_b5_depreciation_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_b5_depreciation_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent(dsa_pub_b5_depreciation_pub_standard_test_fx_depreciation=self.dsa_pub_b5_depreciation_pub_standard_test_fx_depreciation, baseline_pub_nominal_appreciation_increase_in_us_dollar=self.baseline_pub_nominal_appreciation_increase_in_us_dollar)

    @cached_property
    def dsa_pub_b5_depreciation_pub_standard_test_fx_depreciation(self) -> float | str:
        return internals.dsa_pub_b5_depreciation_pub_standard_test_fx_depreciation(lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, in6opt_standard_size_of_fx_depreciation_shock=self.in6opt_standard_size_of_fx_depreciation_shock)

    @cached_property
    def dsa_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent(dsa_pub_standard_test_fx_depreciation=self.dsa_pub_standard_test_fx_depreciation)

    @cached_property
    def dsa_pub_standard_test_gdp_growth_rule(self) -> str | int | float | bool:
        return internals.dsa_pub_standard_test_gdp_growth_rule(in6opt_standard_historical_average_baseline_projection_real_gdp_b6_combination=self.in6opt_standard_historical_average_baseline_projection_real_gdp_b6_combination, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_pub_standard_test_pb_rule(self) -> str | int | float | bool:
        return internals.dsa_pub_standard_test_pb_rule(in6opt_standard_historical_average_baseline_projection_primary_balance_b6_combination=self.in6opt_standard_historical_average_baseline_projection_primary_balance_b6_combination, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_pub_standard_test_fx_depreciation(self) -> float | str:
        return internals.dsa_pub_standard_test_fx_depreciation(lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, in6opt_standard_b6_combination_size_of_fx_depreciation_shock=self.in6opt_standard_b6_combination_size_of_fx_depreciation_shock)

    @cached_property
    def dsa_pub_b6_combo_non_mkt_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_b6_combo_non_mkt_pub_nominal_appreciation_increase_in_us_dollar_value_of_local_currency_in_percent(dsa_pub_b6_combo_non_mkt_pub_standard_test_fx_depreciation=self.dsa_pub_b6_combo_non_mkt_pub_standard_test_fx_depreciation)

    @cached_property
    def dsa_pub_b6_combo_non_mkt_pub_standard_test_gdp_growth_rule(self) -> str | int | float | bool:
        return internals.dsa_pub_b6_combo_non_mkt_pub_standard_test_gdp_growth_rule(in6opt_standard_historical_average_baseline_projection_real_gdp_b6_combination=self.in6opt_standard_historical_average_baseline_projection_real_gdp_b6_combination, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_pub_b6_combo_non_mkt_pub_standard_test_pb_rule(self) -> str | int | float | bool:
        return internals.dsa_pub_b6_combo_non_mkt_pub_standard_test_pb_rule(in6opt_standard_historical_average_baseline_projection_primary_balance_b6_combination=self.in6opt_standard_historical_average_baseline_projection_primary_balance_b6_combination, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def dsa_pub_b6_combo_non_mkt_pub_standard_test_fx_depreciation(self) -> float | str:
        return internals.dsa_pub_b6_combo_non_mkt_pub_standard_test_fx_depreciation(lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, in6opt_standard_b6_combination_size_of_fx_depreciation_shock=self.in6opt_standard_b6_combination_size_of_fx_depreciation_shock)

    @cached_property
    def dsa_pub_old_new_scenario_total(self) -> float | str:
        return internals.dsa_pub_old_new_scenario_total(dsa_pub_input2_coverage=self.dsa_pub_input2_coverage, in6opt_standard_scenario=self.in6opt_standard_scenario)

    @cached_property
    def dsa_pub_input2_coverage(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_input2_coverage(contingent_liability_financial_market_pct_gdp=self.contingent_liability_financial_market_pct_gdp, in2_coverage_ppp=self.in2_coverage_ppp, in2_coverage_other_elements_of_govt_not_captured_in_1=self.in2_coverage_other_elements_of_govt_not_captured_in_1, in2_coverage_soe_s_debt_guaranteed_not_guaranteed_government=self.in2_coverage_soe_s_debt_guaranteed_not_guaranteed_government)

    @cached_property
    def dsa_pub_c2_natural_disaster_pv_of_debt_gdp(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_c2_natural_disaster_pv_of_debt_gdp(dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, dsa_pub_exchange_rate_lc_per_us_dollar=self.dsa_pub_exchange_rate_lc_per_us_dollar, dsa_pub_pv_of_public_sector_external_debt_end_of_period=self.dsa_pub_pv_of_public_sector_external_debt_end_of_period, leftover_exchange_rate_pa=self.leftover_exchange_rate_pa)

    @cached_property
    def dsa_pub_c2_natural_disaster_pv_of_debt_exports(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_c2_natural_disaster_pv_of_debt_exports(dsa_pub_exchange_rate_lc_per_us_dollar=self.dsa_pub_exchange_rate_lc_per_us_dollar, dsa_pub_pv_of_public_sector_external_debt_end_of_period=self.dsa_pub_pv_of_public_sector_external_debt_end_of_period, dsa_pub_c2_natural_disaster_exports_us_baseline=self.dsa_pub_c2_natural_disaster_exports_us_baseline)

    @cached_property
    def dsa_pub_c2_natural_disaster_debt_service_exports(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_c2_natural_disaster_debt_service_exports(dsa_pub_c2_natural_disaster_exports_us_baseline=self.dsa_pub_c2_natural_disaster_exports_us_baseline, macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6, pv_resfin_pub_output_total_debt_service_in_usd=self.pv_resfin_pub_output_total_debt_service_in_usd)

    @cached_property
    def dsa_pub_c2_natural_disaster_debt_service_revenue_excl_grants(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_c2_natural_disaster_debt_service_revenue_excl_grants(dsa_pub_c2_natural_disaster_revenue=self.dsa_pub_c2_natural_disaster_revenue, macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6, pv_resfin_pub_output_total_debt_service_in_usd=self.pv_resfin_pub_output_total_debt_service_in_usd)

    @cached_property
    def dsa_pub_c2_natural_disaster_exports_us_baseline(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_c2_natural_disaster_exports_us_baseline(macro_debt_exports_of_goods_services=self.macro_debt_exports_of_goods_services, dsa_pub_c2_natural_disaster_exports_growth_rate=self.dsa_pub_c2_natural_disaster_exports_growth_rate)

    @cached_property
    def dsa_pub_c2_natural_disaster_exports_growth_rate(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_c2_natural_disaster_exports_growth_rate(dsa_ext_growth_of_exports_of_g_s_us_dollar_terms_in_percent=self.dsa_ext_growth_of_exports_of_g_s_us_dollar_terms_in_percent, leftover_real_interest_rate=self.leftover_real_interest_rate)

    @cached_property
    def dsa_pub_c2_natural_disaster_revenue(self) -> data.Series[float | str | None]:
        return internals.dsa_pub_c2_natural_disaster_revenue(dsa_pub_revenue_and_grants=self.dsa_pub_revenue_and_grants, dsa_pub_of_which_grants=self.dsa_pub_of_which_grants, dsa_pub_nominal_gdp_local_currency=self.dsa_pub_nominal_gdp_local_currency, leftover_exchange_rate_pa=self.leftover_exchange_rate_pa)

    @cached_property
    def dsa_pub_c3_commodity_prices_pub_decline_in_gdp_deflator(self) -> float | str:
        return internals.dsa_pub_c3_commodity_prices_pub_decline_in_gdp_deflator(c3_commodity_pub_historical_statistics_key_historical_statistics_key_variables_past_10=self.c3_commodity_pub_historical_statistics_key_historical_statistics_key_variables_past_10, c3_commodity_pub_historical_statistics_key_historical_statistics_key_variables_past_10_2=self.c3_commodity_pub_historical_statistics_key_historical_statistics_key_variables_past_10_2)

    @cached_property
    def input4_discount_rate(self) -> data.Series[float | str | None]:
        return internals.input4_discount_rate(discount_rate=self.discount_rate)

    @cached_property
    def input4_discount_rate_bonds_fx_non_residents(self) -> data.Series[float | str | None]:
        return internals.input4_discount_rate_bonds_fx_non_residents(input4_discount_rate=self.input4_discount_rate)

    @cached_property
    def input4_discount_rate_bonds_fx_residents(self) -> data.Series[float | str | None]:
        return internals.input4_discount_rate_bonds_fx_residents(input4_discount_rate=self.input4_discount_rate)

    @cached_property
    def input4_terms_ida_regular(self) -> data.Series[float | str | None]:
        return internals.input4_terms_ida_regular(input4_instrument_names=self.input4_instrument_names, input4_ida_scale_name=data.INPUT4_IDA_SCALE_NAME, input4_ida_scale_service_fee=data.INPUT4_IDA_SCALE_SERVICE_FEE, input4_ida_scale_grace=data.INPUT4_IDA_SCALE_GRACE, input4_ida_scale_maturity=data.INPUT4_IDA_SCALE_MATURITY, input4_ida_scale_blend_fixed=data.INPUT4_IDA_SCALE_BLEND_FIXED, input4_ida_regular_translated_name=self.input4_ida_regular_translated_name, input4_ida_scale_blend_fixed_interest=self.input4_ida_scale_blend_fixed_interest)

    @cached_property
    def input4_terms_ida_and_lc(self) -> data.Series[float | str | None]:
        return internals.input4_terms_ida_and_lc(input5_internal_grace_period=self.input5_internal_grace_period, blend_ida_new_fixed_interest_rate=data.BLEND_IDA_NEW_FIXED_INTEREST_RATE, blend_ida_new_fixed_name=data.BLEND_IDA_NEW_FIXED_NAME, blend_ida_new_floating_name=data.BLEND_IDA_NEW_FLOATING_NAME, input4_instrument_names=self.input4_instrument_names, input4_blend_variant=self.input4_blend_variant, input4_blend_scale_key=self.input4_blend_scale_key, input4_ida_scale_name=data.INPUT4_IDA_SCALE_NAME, input4_ida_scale_service_fee=data.INPUT4_IDA_SCALE_SERVICE_FEE, input4_ida_scale_grace=data.INPUT4_IDA_SCALE_GRACE, input4_ida_scale_maturity=data.INPUT4_IDA_SCALE_MATURITY, input4_ida_scale_blend_fixed=data.INPUT4_IDA_SCALE_BLEND_FIXED, input4_ida_scale_blend_fixed_interest=self.input4_ida_scale_blend_fixed_interest, input5_internal_interest_rate_on_domestic_debt=self.input5_internal_interest_rate_on_domestic_debt, input5_internal_maturity=self.input5_internal_maturity, blend_ida_new_floating_currency=self.blend_ida_new_floating_currency, blend_ida_new_floating_interest_rate=self.blend_ida_new_floating_interest_rate)

    @cached_property
    def input4_terms_bonds_fx_non_residents(self) -> data.Series[float | str | None]:
        return internals.input4_terms_bonds_fx_non_residents(input5_internal_grace_period=self.input5_internal_grace_period, input5_internal_interest_rate_on_domestic_debt=self.input5_internal_interest_rate_on_domestic_debt, input5_internal_maturity=self.input5_internal_maturity)

    @cached_property
    def input4_terms_bonds_fx_residents(self) -> data.Series[float | str | None]:
        return internals.input4_terms_bonds_fx_residents(input5_grace_period=self.input5_grace_period, input5_interest_rate_on_domestic_debt=self.input5_interest_rate_on_domestic_debt, input5_interest_rate_on_domestic_debt_fx_long=self.input5_interest_rate_on_domestic_debt_fx_long, input5_internal_interest_rate_on_domestic_debt=self.input5_internal_interest_rate_on_domestic_debt, input5_maturity=self.input5_maturity)

    @cached_property
    def input4_disbursements_internal(self) -> data.Series[float | str | None]:
        return internals.input4_disbursements_internal(input3_new_disbursements=self.input3_new_disbursements)

    @cached_property
    def input4_ida_scale_principal_internal(self) -> data.Series[float | str | None]:
        return internals.input4_ida_scale_principal_internal(input4_ida_scale_principal=data.INPUT4_IDA_SCALE_PRINCIPAL)

    @cached_property
    def input4_ida_scale_principal_share_internal(self) -> data.Series[float | str | None]:
        return internals.input4_ida_scale_principal_share_internal()

    @cached_property
    def input4_disbursement_totals(self) -> data.Series[float | str | None]:
        return internals.input4_disbursement_totals(input4_disbursements=self.input4_disbursements, input4_disbursements_internal=self.input4_disbursements_internal)

    @cached_property
    def input4_grace_period_column_header(self) -> str | int | float | bool:
        return internals.input4_grace_period_column_header(start_debt_sustainability_analysis=self.start_debt_sustainability_analysis, translation_input_4_external_fin_terms_grace_period=data.TRANSLATION_INPUT_4_EXTERNAL_FIN_TERMS_GRACE_PERIOD)

    @cached_property
    def input4_ida_regular_translated_name(self) -> str | int | float | bool:
        return internals.input4_ida_regular_translated_name(translation_input_4_external_fin_terms_ida_information=data.TRANSLATION_INPUT_4_EXTERNAL_FIN_TERMS_IDA_INFORMATION, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def input4_ida_scale_blend_fixed_interest(self) -> str | int | float | bool:
        return internals.input4_ida_scale_blend_fixed_interest(input4_ida_scale_blend_fixed=data.INPUT4_IDA_SCALE_BLEND_FIXED)

    @cached_property
    def input5_blue_cells_note(self) -> str | int | float | bool:
        return internals.input5_blue_cells_note(in1_basics_autofill_note=self.in1_basics_autofill_note)

    @cached_property
    def input5_projection_years(self) -> data.Series[int | str | None]:
        return internals.input5_projection_years(macro_debt_data=self.macro_debt_data)

    @cached_property
    def input5_instrument_terms_assumptions_on_domestic_financial_instruments_header(self) -> str | int | float | bool:
        return internals.input5_instrument_terms_assumptions_on_domestic_financial_instruments_header(translation_input_5_domestic_financing_assumptions_on_domestic_financial_instruments=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_ASSUMPTIONS_ON_DOMESTIC_FINANCIAL_INSTRUMENTS, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def input5_instrument_terms_grace_period_header(self) -> str | int | float | bool:
        return internals.input5_instrument_terms_grace_period_header(input4_grace_period_column_header=self.input4_grace_period_column_header)

    @cached_property
    def input5_instrument_terms_interest_rate_on_domestic_debt_header(self) -> str | int | float | bool:
        return internals.input5_instrument_terms_interest_rate_on_domestic_debt_header(start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m, translation_interest_rate_domestic_debt=self.translation_interest_rate_domestic_debt)

    @cached_property
    def input5_instrument_terms_maturity_header(self) -> str | int | float | bool:
        return internals.input5_instrument_terms_maturity_header(translation_input_5_domestic_financing_maturity=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_MATURITY, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def input5_instrument_terms_instrument_label(self) -> data.Series[str | int | float | bool | None]:
        return internals.input5_instrument_terms_instrument_label(translation_input_5_domestic_financing_locally_issued_debt=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_LOCALLY_ISSUED_DEBT, translation_input_5_domestic_financing_central_bank_financing=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_CENTRAL_BANK_FINANCING, translation_input_5_domestic_financing_t_bills_denominated_in_local_currency=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_T_BILLS_DENOMINATED_IN_LOCAL_CURRENCY, translation_input_5_domestic_financing_t_bills_denominated_in_foreign_currency=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_T_BILLS_DENOMINATED_IN_FOREIGN_CURRENCY, translation_input_5_domestic_financing_mlt_debt=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_MLT_DEBT, translation_input_5_domestic_financing_denominated_in_local_currency_lc=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_DENOMINATED_IN_LOCAL_CURRENCY_LC, translation_input_5_domestic_financing_bonds_1_to_3_years_lc=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_BONDS_1_TO_3_YEARS_LC, translation_input_5_domestic_financing_bonds_4_to_7_years_lc=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_BONDS_4_TO_7_YEARS_LC, translation_input_5_domestic_financing_bonds_beyond_7_years_lc=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_BONDS_BEYOND_7_YEARS_LC, translation_input_5_domestic_financing_bonds_1_to_3_years_fx=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_BONDS_1_TO_3_YEARS_FX, translation_input_5_domestic_financing_bonds_4_to_7_years_fx=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_BONDS_4_TO_7_YEARS_FX, translation_input_5_domestic_financing_bonds_beyond_7_years_fx=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_BONDS_BEYOND_7_YEARS_FX, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, external_domestic_debt_definition=self.external_domestic_debt_definition, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m, lookup_afg_ap=self.lookup_afg_ap, lookup_hti=self.lookup_hti, lookup_hnd=self.lookup_hnd, translation_st_debt=self.translation_st_debt, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_internal_interest_rate_on_domestic_debt(self) -> data.Series[float | str | None]:
        return internals.input5_internal_interest_rate_on_domestic_debt(input5_interest_rate_on_domestic_debt=self.input5_interest_rate_on_domestic_debt, input5_interest_rate_on_domestic_debt_fx_long=self.input5_interest_rate_on_domestic_debt_fx_long)

    @cached_property
    def input5_internal_grace_period(self) -> data.Series[float | str | None]:
        return internals.input5_internal_grace_period(input5_grace_period=self.input5_grace_period)

    @cached_property
    def input5_internal_maturity(self) -> data.Series[float | str | None]:
        return internals.input5_internal_maturity(input5_maturity=self.input5_maturity)

    @cached_property
    def input5_public_gfns_1_primary_deficit(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_1_primary_deficit(macro_debt_public_sector_revenues_including_grants=self.macro_debt_public_sector_revenues_including_grants, macro_debt_public_sector_primary_expenditure=self.macro_debt_public_sector_primary_expenditure)

    @cached_property
    def input5_public_gfns_2_debt_services_from_existing_debt(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_2_debt_services_from_existing_debt(input5_public_gfns_2_debt_services_from_existing_debt_domestic_including_st_debt_from_previous_year=self.input5_public_gfns_2_debt_services_from_existing_debt_domestic_including_st_debt_from_previous_year, input5_public_gfns_2_debt_services_from_existing_debt_external_debt_mlt=self.input5_public_gfns_2_debt_services_from_existing_debt_external_debt_mlt)

    @cached_property
    def input5_public_gfns_2_debt_services_from_existing_debt_domestic_including_st_debt_from_previous_year(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_2_debt_services_from_existing_debt_domestic_including_st_debt_from_previous_year(input5_old_debt_debt_service_from_old_debt_residency_based=self.input5_old_debt_debt_service_from_old_debt_residency_based)

    @cached_property
    def input5_public_gfns_2_debt_services_from_existing_debt_external_debt_mlt(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_2_debt_services_from_existing_debt_external_debt_mlt(input5_macro_nominal_exchange_rate_average_lcu_usd=self.input5_macro_nominal_exchange_rate_average_lcu_usd, ext_debt_total_including_locally_issued=self.ext_debt_total_including_locally_issued)

    @cached_property
    def input5_public_gfns_2_debt_services_from_existing_debt_ow_imf(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_2_debt_services_from_existing_debt_ow_imf(ext_debt_old_mlt_debt_service=self.ext_debt_old_mlt_debt_service, input5_macro_nominal_exchange_rate_average_lcu_usd=self.input5_macro_nominal_exchange_rate_average_lcu_usd)

    @cached_property
    def _scan_input5_public_gfns_3_debt_services_from_new_debt(self) -> internals.ScanInput5PublicGfns3DebtServicesFromNewDebtResult:
        return internals.scan_input5_public_gfns_3_debt_services_from_new_debt(ext_debt_st_principal_first_year=data.EXT_DEBT_ST_PRINCIPAL_FIRST_YEAR, ext_debt_st_interest_first_year=data.EXT_DEBT_ST_INTEREST_FIRST_YEAR, input5_public_gfns_1_primary_deficit=self.input5_public_gfns_1_primary_deficit, input5_public_gfns_2_debt_services_from_existing_debt=self.input5_public_gfns_2_debt_services_from_existing_debt, input5_public_gfns_5_other_debt_creating_or_reducing_flows=self.input5_public_gfns_5_other_debt_creating_or_reducing_flows, input5_public_gfns_7_external_financing_mlt_excluding_locally_issued_debt=self.input5_public_gfns_7_external_financing_mlt_excluding_locally_issued_debt, input5_public_gfns_8_external_financing_st_excluding_locally_issued_debt=self.input5_public_gfns_8_external_financing_st_excluding_locally_issued_debt, input5_public_gfns_9_changes_in_liquid_assets=self.input5_public_gfns_9_changes_in_liquid_assets, input5_public_gfns_10_drawdown_of_reserves_to_repay_the_imf=self.input5_public_gfns_10_drawdown_of_reserves_to_repay_the_imf, input5_public_gfns_other_adjustment=self.input5_public_gfns_other_adjustment, input5_domestic_financing_source=self.input5_domestic_financing_source, input5_gfn_share=self.input5_gfn_share, input5_new_issuance_financing_strategy_share=self.input5_new_issuance_financing_strategy_share, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, input5_macro_nominal_exchange_rate_average_lcu_usd=self.input5_macro_nominal_exchange_rate_average_lcu_usd, input5_vintage_projection_years_interest=self.input5_vintage_projection_years_interest, input5_vintage_projection_years_principal=self.input5_vintage_projection_years_principal, input5_vintage_issuance_year=self.input5_vintage_issuance_year, input5_vintage_terms=self.input5_vintage_terms, input3_domestic_new_gross_disbursement=self.input3_domestic_new_gross_disbursement, ext_debt_definition_external_domestic=self.ext_debt_definition_external_domestic, ext_debt_new_interest_external=self.ext_debt_new_interest_external, ext_debt_new_amortization_external=self.ext_debt_new_amortization_external, ext_debt_st_external_nominal=self.ext_debt_st_external_nominal, ext_debt_st_external_interest=self.ext_debt_st_external_interest, ext_debt_exchange_rate_period_average=self.ext_debt_exchange_rate_period_average, lookup_afg=self.lookup_afg, pv_base_block_grace_fx=self.pv_base_block_grace_fx, pv_base_block_maturity_fx=self.pv_base_block_maturity_fx, pv_base_block_interest_fx=self.pv_base_block_interest_fx, pv_base_discount_t_g_0_fx=self.pv_base_discount_t_g_0_fx, pv_base_discount_t_m_condition_fx=self.pv_base_discount_t_m_condition_fx, pv_lc_nr1_terms_projection_year=self.pv_lc_nr1_terms_projection_year, pv_lc_nr1_terms_fx_pa=self.pv_lc_nr1_terms_fx_pa, pv_lc_nr1_terms_fx_eop=self.pv_lc_nr1_terms_fx_eop, pv_lc_terms_interest_rate_local_currency=self.pv_lc_terms_interest_rate_local_currency, pv_lc_output_issuance_year=self.pv_lc_output_issuance_year, pv_lc_output_projection_year=self.pv_lc_output_projection_year, pv_lc_labels_stock_of_debt_in_lc=data.PV_LC_LABELS_STOCK_OF_DEBT_IN_LC, pv_lc_output_grace=self.pv_lc_output_grace, pv_lc_output_maturity=self.pv_lc_output_maturity, pv_lc_output_t_g_0=self.pv_lc_output_t_g_0, pv_lc_output_t_m_condition=self.pv_lc_output_t_m_condition, pv_lc_terms_projection_year=self.pv_lc_terms_projection_year, pv_lc_terms_fx_pa=self.pv_lc_terms_fx_pa, pv_lc_terms_fx_eop=self.pv_lc_terms_fx_eop)

    @cached_property
    def input5_public_gfns_3_debt_services_from_new_debt(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_public_gfns_3_debt_services_from_new_debt

    @cached_property
    def input5_public_gfns_3_debt_services_from_new_debt_domestic_including_st_debt_from_previous_year(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_public_gfns_3_debt_services_from_new_debt_domestic_including_st_debt_from_previous_year

    @cached_property
    def input5_public_gfns_3_debt_services_from_new_debt_external_debt_mlt(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_public_gfns_3_debt_services_from_new_debt_external_debt_mlt

    @cached_property
    def input5_public_gfns_4_debt_services_from_st_external_debt(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_public_gfns_4_debt_services_from_st_external_debt

    @cached_property
    def input5_public_gfns_6_public_gfns(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_public_gfns_6_public_gfns

    @cached_property
    def input5_public_gfns_12_domestic_financing(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_public_gfns_12_domestic_financing

    @cached_property
    def input5_new_issuance_gfns_to_be_financed_with_domestic_debt(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_issuance_gfns_to_be_financed_with_domestic_debt

    @cached_property
    def input5_new_issuance_new_issuance_of_locally_issued_debt(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_issuance_new_issuance_of_locally_issued_debt

    @cached_property
    def input5_new_issuance_locally_issued_debt(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_issuance_locally_issued_debt

    @cached_property
    def input5_new_issuance(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_issuance

    @cached_property
    def input5_new_issuance_short_term_debt(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_issuance_short_term_debt

    @cached_property
    def input5_new_issuance_mlt_debt(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_issuance_mlt_debt

    @cached_property
    def input5_new_issuance_denominated_in_local_currency_lc(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_issuance_denominated_in_local_currency_lc

    @cached_property
    def input5_new_issuance_denominated_in_foreign_currency_fx(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_issuance_denominated_in_foreign_currency_fx

    @cached_property
    def input5_new_issuance_domestic_residual_financing_to_close_gap(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_issuance_domestic_residual_financing_to_close_gap

    @cached_property
    def input5_new_debt_debt_services_from_new_debt_residency_based(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_debt_services_from_new_debt_residency_based

    @cached_property
    def input5_new_debt_interest_payment_on_new_debt_residency_based(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_interest_payment_on_new_debt_residency_based

    @cached_property
    def input5_new_debt_interest_payment_on_new_debt_denominated_in_local_currency(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_interest_payment_on_new_debt_denominated_in_local_currency

    @cached_property
    def input5_new_debt_interest_payment_on_new_debt_denominated_in_foreign_currency(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_interest_payment_on_new_debt_denominated_in_foreign_currency

    @cached_property
    def input5_new_debt_interest_payment_on_new_debt_denominated_in_foreign_currency_ow_short_term(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_interest_payment_on_new_debt_denominated_in_foreign_currency_ow_short_term

    @cached_property
    def input5_new_debt_interest_payment_on_new_debt_denominated_in_local_currency_ow_short_term(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_interest_payment_on_new_debt_denominated_in_local_currency_ow_short_term

    @cached_property
    def input5_new_debt_principal_payment_on_new_debt_residency_based(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_principal_payment_on_new_debt_residency_based

    @cached_property
    def input5_new_debt_principal_payments_on_new_debt_denominated_in_local_currency(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_principal_payments_on_new_debt_denominated_in_local_currency

    @cached_property
    def input5_new_debt_principal_payments_on_new_debt_denominated_in_foreign_currency(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_principal_payments_on_new_debt_denominated_in_foreign_currency

    @cached_property
    def input5_new_debt_principal_payments_on_new_debt_denominated_in_foreign_currency_ow_short_term(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_principal_payments_on_new_debt_denominated_in_foreign_currency_ow_short_term

    @cached_property
    def input5_new_debt_principal_payments_on_new_debt_denominated_in_local_currency_ow_short_term(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_new_debt_principal_payments_on_new_debt_denominated_in_local_currency_ow_short_term

    @cached_property
    def input5_vintage_interest(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_vintage_interest

    @cached_property
    def input5_vintage_principal(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_vintage_principal

    @cached_property
    def input5_vintage_stock(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.input5_vintage_stock

    @cached_property
    def ext_debt_new_disbursements_non_residents(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_new_disbursements_non_residents

    @cached_property
    def ext_debt_new_disbursements_residents(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_new_disbursements_residents

    @cached_property
    def ext_debt_new_debt_service_total(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_new_debt_service_total

    @cached_property
    def ext_debt_new_interest_total(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_new_interest_total

    @cached_property
    def ext_debt_new_interest_non_residents(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_new_interest_non_residents

    @cached_property
    def ext_debt_new_interest_residents(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_new_interest_residents

    @cached_property
    def ext_debt_new_amortization_total(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_new_amortization_total

    @cached_property
    def ext_debt_new_amortization_non_residents(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_new_amortization_non_residents

    @cached_property
    def ext_debt_new_amortization_residents(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_new_amortization_residents

    @cached_property
    def ext_debt_st_locally_issued_principal(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_st_locally_issued_principal

    @cached_property
    def ext_debt_st_locally_issued_interest(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_st_locally_issued_interest

    @cached_property
    def ext_debt_st_total_principal(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_st_total_principal

    @cached_property
    def ext_debt_st_total_interest(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.ext_debt_st_total_interest

    @cached_property
    def pv_base_discount_post_grace_cumulative_fx(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_base_discount_post_grace_cumulative_fx

    @cached_property
    def pv_base_discount_post_maturity_cumulative_fx(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_base_discount_post_maturity_cumulative_fx

    @cached_property
    def pv_base_output_new_forex_borrowing_gross_usd_fx(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_base_output_new_forex_borrowing_gross_usd_fx

    @cached_property
    def pv_base_output_cumulative_fx(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_base_output_cumulative_fx

    @cached_property
    def pv_base_output_stock_of_new_forex_debt_in_usd_fx(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_base_output_stock_of_new_forex_debt_in_usd_fx

    @cached_property
    def pv_base_output_interest_fx(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_base_output_interest_fx

    @cached_property
    def pv_base_output_amortization_fx(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_base_output_amortization_fx

    @cached_property
    def pv_lc_terms_gross_financing_in_lc(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_terms_gross_financing_in_lc

    @cached_property
    def pv_lc_summary_interest_in_usd(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_summary_interest_in_usd

    @cached_property
    def pv_lc_summary_amortization_in_usd(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_summary_amortization_in_usd

    @cached_property
    def pv_lc_output_new_borrowing_gross_in_local_currency(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_output_new_borrowing_gross_in_local_currency

    @cached_property
    def pv_lc_output_cumulative(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_output_cumulative

    @cached_property
    def pv_lc_output_stock_of_debt_in_lc(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_output_stock_of_debt_in_lc

    @cached_property
    def pv_lc_output_interest_in_usd(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_output_interest_in_usd

    @cached_property
    def pv_lc_output_amortization_in_usd(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_output_amortization_in_usd

    @cached_property
    def pv_lc_output_interest_rate_local_currency(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_output_interest_rate_local_currency

    @cached_property
    def pv_lc_output_amortization_in_lc(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_output_amortization_in_lc

    @cached_property
    def pv_lc_output_grace_end_cumulative(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_output_grace_end_cumulative

    @cached_property
    def pv_lc_output_maturity_end_cumulative(self) -> data.Series[float | str | None]:
        return self._scan_input5_public_gfns_3_debt_services_from_new_debt.pv_lc_output_maturity_end_cumulative

    @cached_property
    def input5_public_gfns_3_debt_services_from_new_debt_ow_imf(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_3_debt_services_from_new_debt_ow_imf(input5_macro_nominal_exchange_rate_average_lcu_usd=self.input5_macro_nominal_exchange_rate_average_lcu_usd, ext_debt_new_interest_external=self.ext_debt_new_interest_external, ext_debt_new_amortization_external=self.ext_debt_new_amortization_external)

    @cached_property
    def input5_public_gfns_5_other_debt_creating_or_reducing_flows(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_5_other_debt_creating_or_reducing_flows(baseline_pub_other_identified_debt_creating_flows=self.baseline_pub_other_identified_debt_creating_flows, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc)

    @cached_property
    def input5_public_gfns_7_external_financing_mlt_excluding_locally_issued_debt(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_7_external_financing_mlt_excluding_locally_issued_debt(input4_disbursement_totals=self.input4_disbursement_totals, input5_macro_nominal_exchange_rate_average_lcu_usd=self.input5_macro_nominal_exchange_rate_average_lcu_usd)

    @cached_property
    def input5_public_gfns_7_external_financing_mlt_ow_imf(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_7_external_financing_mlt_ow_imf(ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external, input5_macro_nominal_exchange_rate_average_lcu_usd=self.input5_macro_nominal_exchange_rate_average_lcu_usd)

    @cached_property
    def input5_public_gfns_8_external_financing_st_excluding_locally_issued_debt(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_8_external_financing_st_excluding_locally_issued_debt(input5_macro_nominal_exchange_rate_average_lcu_usd=self.input5_macro_nominal_exchange_rate_average_lcu_usd, ext_debt_st_external_nominal=self.ext_debt_st_external_nominal)

    @cached_property
    def input5_public_gfns_9_changes_in_liquid_assets(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_9_changes_in_liquid_assets(in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g=self.in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g)

    @cached_property
    def input5_public_gfns_10_drawdown_of_reserves_to_repay_the_imf(self) -> data.Series[float | str | None]:
        return internals.input5_public_gfns_10_drawdown_of_reserves_to_repay_the_imf(input5_public_gfns_2_debt_services_from_existing_debt_ow_imf=self.input5_public_gfns_2_debt_services_from_existing_debt_ow_imf, input5_public_gfns_3_debt_services_from_new_debt_ow_imf=self.input5_public_gfns_3_debt_services_from_new_debt_ow_imf, input5_public_gfns_7_external_financing_mlt_ow_imf=self.input5_public_gfns_7_external_financing_mlt_ow_imf)

    @cached_property
    def input5_new_issuance_financing_strategy_share(self) -> data.Series[float | str | None]:
        return internals.input5_new_issuance_financing_strategy_share(input5_gfn_share=self.input5_gfn_share, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_definition_of_external_domestic_debt(self) -> str | int | float | bool:
        return internals.input5_definition_of_external_domestic_debt(external_domestic_debt_definition=self.external_domestic_debt_definition)

    @cached_property
    def input5_disbursements_public_domestic_st_disbursements_residency_based(self) -> data.Series[float | str | None]:
        return internals.input5_disbursements_public_domestic_st_disbursements_residency_based(input5_maturity_central_bank=self.input5_maturity_central_bank, input5_new_issuance=self.input5_new_issuance, input5_new_issuance_short_term_debt=self.input5_new_issuance_short_term_debt, input5_new_issuance_domestic_residual_financing_to_close_gap=self.input5_new_issuance_domestic_residual_financing_to_close_gap, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_disbursements_public_domestic_mlt_disbursements_residency_based(self) -> data.Series[float | str | None]:
        return internals.input5_disbursements_public_domestic_mlt_disbursements_residency_based(input5_maturity_central_bank=self.input5_maturity_central_bank, input5_new_issuance=self.input5_new_issuance, input5_new_issuance_mlt_debt=self.input5_new_issuance_mlt_debt, input5_new_issuance_denominated_in_local_currency_lc=self.input5_new_issuance_denominated_in_local_currency_lc, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_disbursements_total_public_new_domestic_disbursements_residency_based(self) -> data.Series[float | str | None]:
        return internals.input5_disbursements_total_public_new_domestic_disbursements_residency_based(input5_new_issuance_locally_issued_debt=self.input5_new_issuance_locally_issued_debt, input5_new_issuance=self.input5_new_issuance, input5_new_issuance_denominated_in_local_currency_lc=self.input5_new_issuance_denominated_in_local_currency_lc, input5_new_issuance_domestic_residual_financing_to_close_gap=self.input5_new_issuance_domestic_residual_financing_to_close_gap, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_residual_terms_average_nominal_interest_rate_on_new_debt(self) -> data.Series[float | str | None]:
        return internals.input5_residual_terms_average_nominal_interest_rate_on_new_debt(input5_interest_rate_on_domestic_debt=self.input5_interest_rate_on_domestic_debt, input5_interest_rate_on_domestic_debt_fx_long=self.input5_interest_rate_on_domestic_debt_fx_long, input5_internal_interest_rate_on_domestic_debt=self.input5_internal_interest_rate_on_domestic_debt, input5_maturity_central_bank=self.input5_maturity_central_bank, input5_new_issuance=self.input5_new_issuance, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, input5_disbursements_public_domestic_st_disbursements_residency_based=self.input5_disbursements_public_domestic_st_disbursements_residency_based, input5_disbursements_public_domestic_mlt_disbursements_residency_based=self.input5_disbursements_public_domestic_mlt_disbursements_residency_based, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_residual_terms_gdp_deflator(self) -> data.Series[float | str | None]:
        return internals.input5_residual_terms_gdp_deflator(macro_debt_change_in_gdp_deflator_factor=self.macro_debt_change_in_gdp_deflator_factor)

    @cached_property
    def input5_residual_terms_average_real_interest_rate_on_new_debt(self) -> data.Series[float | str | None]:
        return internals.input5_residual_terms_average_real_interest_rate_on_new_debt(input5_residual_terms_average_nominal_interest_rate_on_new_debt=self.input5_residual_terms_average_nominal_interest_rate_on_new_debt, input5_residual_terms_gdp_deflator=self.input5_residual_terms_gdp_deflator)

    @cached_property
    def input5_residual_terms_average_real_interest_rate_on_new_debt_average(self) -> data.Series[float | str | None]:
        return internals.input5_residual_terms_average_real_interest_rate_on_new_debt_average(input5_residual_terms_average_real_interest_rate_on_new_debt=self.input5_residual_terms_average_real_interest_rate_on_new_debt)

    @cached_property
    def input5_residual_terms_average_real_interest_rate_on_new_debt_rounded_average(self) -> data.Series[float | str | None]:
        return internals.input5_residual_terms_average_real_interest_rate_on_new_debt_rounded_average(input5_residual_terms_average_real_interest_rate_on_new_debt_average=self.input5_residual_terms_average_real_interest_rate_on_new_debt_average)

    @cached_property
    def input5_residual_terms_average_grace_period_on_new_debt(self) -> data.Series[float | str | None]:
        return internals.input5_residual_terms_average_grace_period_on_new_debt(input5_grace_period=self.input5_grace_period, input5_maturity_central_bank=self.input5_maturity_central_bank, input5_new_issuance=self.input5_new_issuance, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, input5_disbursements_public_domestic_mlt_disbursements_residency_based=self.input5_disbursements_public_domestic_mlt_disbursements_residency_based, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_residual_terms_average_grace_period_on_new_debt_average(self) -> float | str:
        return internals.input5_residual_terms_average_grace_period_on_new_debt_average(input5_residual_terms_average_grace_period_on_new_debt=self.input5_residual_terms_average_grace_period_on_new_debt)

    @cached_property
    def input5_residual_terms_average_grace_period_on_new_debt_rounded_average(self) -> int | str:
        return internals.input5_residual_terms_average_grace_period_on_new_debt_rounded_average(input5_residual_terms_average_grace_period_on_new_debt_average=self.input5_residual_terms_average_grace_period_on_new_debt_average)

    @cached_property
    def input5_residual_terms_average_maturity_of_new_debt(self) -> data.Series[float | str | None]:
        return internals.input5_residual_terms_average_maturity_of_new_debt(input5_maturity=self.input5_maturity, input5_maturity_central_bank=self.input5_maturity_central_bank, input5_new_issuance=self.input5_new_issuance, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, input5_disbursements_public_domestic_mlt_disbursements_residency_based=self.input5_disbursements_public_domestic_mlt_disbursements_residency_based, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_residual_terms_average_maturity_of_new_debt_average(self) -> float | str:
        return internals.input5_residual_terms_average_maturity_of_new_debt_average(input5_residual_terms_average_maturity_of_new_debt=self.input5_residual_terms_average_maturity_of_new_debt)

    @cached_property
    def input5_residual_terms_average_maturity_of_new_debt_rounded_average(self) -> int | str:
        return internals.input5_residual_terms_average_maturity_of_new_debt_rounded_average(input5_residual_terms_average_grace_period_on_new_debt_rounded_average=self.input5_residual_terms_average_grace_period_on_new_debt_rounded_average, input5_residual_terms_average_maturity_of_new_debt_average=self.input5_residual_terms_average_maturity_of_new_debt_average)

    @cached_property
    def input5_old_debt_debt_service_from_old_debt_residency_based(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_debt_service_from_old_debt_residency_based(input5_old_debt_interest_payment_on_old_debt_residency_based=self.input5_old_debt_interest_payment_on_old_debt_residency_based, input5_old_debt_principal_payment_on_old_debt_residency_based=self.input5_old_debt_principal_payment_on_old_debt_residency_based)

    @cached_property
    def input5_old_debt_interest_payment_on_old_debt_residency_based(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_interest_payment_on_old_debt_residency_based(input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, input5_old_debt_interest_payment_on_old_debt_denominated_in_local_currency=self.input5_old_debt_interest_payment_on_old_debt_denominated_in_local_currency, input5_old_debt_interest_payment_on_old_debt_denominated_in_foreign_currency=self.input5_old_debt_interest_payment_on_old_debt_denominated_in_foreign_currency, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_old_debt_interest_payment_on_old_debt_denominated_in_local_currency(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_interest_payment_on_old_debt_denominated_in_local_currency(input3_domestic_interest_payment_from_existing_debt=self.input3_domestic_interest_payment_from_existing_debt)

    @cached_property
    def input5_old_debt_interest_payment_on_old_debt_denominated_in_foreign_currency(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_interest_payment_on_old_debt_denominated_in_foreign_currency(input5_macro_nominal_exchange_rate_average_lcu_usd=self.input5_macro_nominal_exchange_rate_average_lcu_usd, input3_domestic_interest_payment_from_existing_debt=self.input3_domestic_interest_payment_from_existing_debt)

    @cached_property
    def input5_old_debt_principal_payment_on_old_debt_residency_based(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_principal_payment_on_old_debt_residency_based(input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, input5_old_debt_principal_payments_on_old_debt_denominated_in_local_currency=self.input5_old_debt_principal_payments_on_old_debt_denominated_in_local_currency, input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency=self.input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_old_debt_principal_payments_on_old_debt_denominated_in_local_currency(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_principal_payments_on_old_debt_denominated_in_local_currency(input3_domestic_principal_payment_from_existing_debt=self.input3_domestic_principal_payment_from_existing_debt)

    @cached_property
    def input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency(input5_macro_nominal_exchange_rate_average_lcu_usd=self.input5_macro_nominal_exchange_rate_average_lcu_usd, input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency_usd=self.input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency_usd)

    @cached_property
    def input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency_usd(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency_usd(input3_domestic_principal_payment_from_existing_debt=self.input3_domestic_principal_payment_from_existing_debt)

    @cached_property
    def input5_old_debt_outstanding_of_old_debt_residency_based(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_outstanding_of_old_debt_residency_based(input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, input5_old_debt_outstanding_from_old_debt_in_local_currency=self.input5_old_debt_outstanding_from_old_debt_in_local_currency, input5_old_debt_outstanding_from_old_debt_in_foreign_currency=self.input5_old_debt_outstanding_from_old_debt_in_foreign_currency, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_old_debt_outstanding_from_old_debt_in_local_currency(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_outstanding_from_old_debt_in_local_currency(input5_old_debt_principal_payments_on_old_debt_denominated_in_local_currency=self.input5_old_debt_principal_payments_on_old_debt_denominated_in_local_currency, input3_domestic_outstanding_of_existing_debt=self.input3_domestic_outstanding_of_existing_debt)

    @cached_property
    def input5_old_debt_outstanding_from_old_debt_in_foreign_currency(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_outstanding_from_old_debt_in_foreign_currency(input5_macro_nominal_exchange_rate_end_of_period_lcu_usd=self.input5_macro_nominal_exchange_rate_end_of_period_lcu_usd, input5_old_debt_outstanding_from_old_debt_in_foreign_currency_usd=self.input5_old_debt_outstanding_from_old_debt_in_foreign_currency_usd)

    @cached_property
    def input5_old_debt_outstanding_from_old_debt_in_foreign_currency_usd(self) -> data.Series[float | str | None]:
        return internals.input5_old_debt_outstanding_from_old_debt_in_foreign_currency_usd(input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency_usd=self.input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency_usd, input3_domestic_outstanding_of_existing_debt=self.input3_domestic_outstanding_of_existing_debt)

    @cached_property
    def input5_new_debt_outstanding_of_new_debt_residency_based(self) -> data.Series[float | str | None]:
        return internals.input5_new_debt_outstanding_of_new_debt_residency_based(input5_new_debt_debt_stock_on_new_debt_denominated_in_foreign_currency=self.input5_new_debt_debt_stock_on_new_debt_denominated_in_foreign_currency, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, input5_new_debt_debt_stock_on_new_debt_denominated_in_local_currency=self.input5_new_debt_debt_stock_on_new_debt_denominated_in_local_currency, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_new_debt_debt_stock_on_new_debt_denominated_in_local_currency(self) -> data.Series[float | str | None]:
        return internals.input5_new_debt_debt_stock_on_new_debt_denominated_in_local_currency(input5_vintage_stock=self.input5_vintage_stock)

    @cached_property
    def input5_new_debt_debt_stock_on_new_debt_denominated_in_foreign_currency(self) -> data.Series[float | str | None]:
        return internals.input5_new_debt_debt_stock_on_new_debt_denominated_in_foreign_currency(input5_macro_nominal_exchange_rate_end_of_period_lcu_usd=self.input5_macro_nominal_exchange_rate_end_of_period_lcu_usd, input5_vintage_stock=self.input5_vintage_stock)

    @cached_property
    def input5_summary_outstanding_stock(self) -> data.Series[float | str | None]:
        return internals.input5_summary_outstanding_stock(input5_old_debt_outstanding_of_old_debt_residency_based=self.input5_old_debt_outstanding_of_old_debt_residency_based, input5_new_debt_outstanding_of_new_debt_residency_based=self.input5_new_debt_outstanding_of_new_debt_residency_based)

    @cached_property
    def input5_summary_mlt(self) -> data.Series[float | str | None]:
        return internals.input5_summary_mlt(input5_summary_outstanding_stock=self.input5_summary_outstanding_stock, input5_summary_short_term=self.input5_summary_short_term)

    @cached_property
    def input5_summary_short_term(self) -> data.Series[float | str | None]:
        return internals.input5_summary_short_term(input5_maturity_central_bank=self.input5_maturity_central_bank, input5_new_issuance=self.input5_new_issuance, input5_new_issuance_short_term_debt=self.input5_new_issuance_short_term_debt, input5_new_issuance_domestic_residual_financing_to_close_gap=self.input5_new_issuance_domestic_residual_financing_to_close_gap, input5_definition_of_external_domestic_debt=self.input5_definition_of_external_domestic_debt, lookup_afg=self.lookup_afg)

    @cached_property
    def input5_summary_interest_payment(self) -> data.Series[float | str | None]:
        return internals.input5_summary_interest_payment(input5_old_debt_interest_payment_on_old_debt_residency_based=self.input5_old_debt_interest_payment_on_old_debt_residency_based, input5_new_debt_interest_payment_on_new_debt_residency_based=self.input5_new_debt_interest_payment_on_new_debt_residency_based)

    @cached_property
    def input5_summary_principal_payment(self) -> data.Series[float | str | None]:
        return internals.input5_summary_principal_payment(input5_old_debt_principal_payment_on_old_debt_residency_based=self.input5_old_debt_principal_payment_on_old_debt_residency_based, input5_new_debt_principal_payment_on_new_debt_residency_based=self.input5_new_debt_principal_payment_on_new_debt_residency_based)

    @cached_property
    def input5_macro_nominal_exchange_rate_average_lcu_usd(self) -> data.Series[float | str | None]:
        return internals.input5_macro_nominal_exchange_rate_average_lcu_usd(macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def input5_macro_nominal_exchange_rate_end_of_period_lcu_usd(self) -> data.Series[float | str | None]:
        return internals.input5_macro_nominal_exchange_rate_end_of_period_lcu_usd(macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar)

    @cached_property
    def input5_vintage_projection_years_stock(self) -> data.Series[int | str | None]:
        return internals.input5_vintage_projection_years_stock(input5_projection_years=self.input5_projection_years)

    @cached_property
    def input5_vintage_projection_years_interest(self) -> data.Series[int | str | None]:
        return internals.input5_vintage_projection_years_interest(input5_vintage_projection_years_principal=self.input5_vintage_projection_years_principal)

    @cached_property
    def input5_vintage_projection_years_principal(self) -> data.Series[int | str | None]:
        return internals.input5_vintage_projection_years_principal(input5_vintage_projection_years_stock=self.input5_vintage_projection_years_stock)

    @cached_property
    def input5_vintage_instrument_title(self) -> data.Series[str | int | float | bool | None]:
        return internals.input5_vintage_instrument_title(input5_instrument_titles=self.input5_instrument_titles, input5_instrument_terms_instrument_label=self.input5_instrument_terms_instrument_label)

    @cached_property
    def input5_vintage_issuance_year(self) -> data.Series[int | str | None]:
        return internals.input5_vintage_issuance_year(input5_projection_years=self.input5_projection_years)

    @cached_property
    def input5_vintage_terms(self) -> data.Series[float | str | None]:
        return internals.input5_vintage_terms(input5_grace_period=self.input5_grace_period, input5_blue_cells_note=self.input5_blue_cells_note, input5_projection_years=self.input5_projection_years, input5_instrument_terms_assumptions_on_domestic_financial_instruments_header=self.input5_instrument_terms_assumptions_on_domestic_financial_instruments_header, input5_instrument_terms_grace_period_header=self.input5_instrument_terms_grace_period_header, input5_instrument_terms_interest_rate_on_domestic_debt_header=self.input5_instrument_terms_interest_rate_on_domestic_debt_header, input5_instrument_terms_maturity_header=self.input5_instrument_terms_maturity_header, input5_instrument_terms_instrument_label=self.input5_instrument_terms_instrument_label, input5_interest_rate_on_domestic_debt=self.input5_interest_rate_on_domestic_debt, input5_interest_rate_on_domestic_debt_fx_long=self.input5_interest_rate_on_domestic_debt_fx_long, input5_internal_interest_rate_on_domestic_debt=self.input5_internal_interest_rate_on_domestic_debt, input5_maturity=self.input5_maturity, input5_maturity_central_bank=self.input5_maturity_central_bank, input5_constant_grace_period=data.INPUT5_CONSTANT_GRACE_PERIOD, input5_constant_maturity=data.INPUT5_CONSTANT_MATURITY, input5_internal_grace_period=self.input5_internal_grace_period, input5_internal_maturity=self.input5_internal_maturity, input5_vintage_instrument_title=self.input5_vintage_instrument_title, input5_vintage_issuance_year=self.input5_vintage_issuance_year, input5_vintage_instrument_label=self.input5_vintage_instrument_label)

    @cached_property
    def input5_vintage_instrument_label(self) -> data.Series[str | int | float | bool | None]:
        return internals.input5_vintage_instrument_label(input5_instrument_titles=self.input5_instrument_titles)

    @cached_property
    def a1_hist_pub_historical_statistics(self) -> data.Series[float | str | None]:
        return internals.a1_hist_pub_historical_statistics(baseline_pub_inflation_rate_gdp_deflator_pct_al=self.baseline_pub_inflation_rate_gdp_deflator_pct_al, baseline_pub_primary_deficit_by_indicator=self.baseline_pub_primary_deficit_by_indicator, baseline_pub_real_gdp_growth_by_indicator=self.baseline_pub_real_gdp_growth_by_indicator)

    @cached_property
    def blend_calculated_blend_rate(self) -> float | str:
        return internals.blend_calculated_blend_rate(blend_ibrd_group_a_pricing=data.BLEND_IBRD_GROUP_A_PRICING, blend_sofr_selected_by_maturity=self.blend_sofr_selected_by_maturity)

    @cached_property
    def blend_sofr_selected_by_maturity(self) -> float | str:
        return internals.blend_sofr_selected_by_maturity(blend_ida_new_floating_maturity=data.BLEND_IDA_NEW_FLOATING_MATURITY, blend_interpolation_index=data.BLEND_INTERPOLATION_INDEX, blend_sofr_interpolated_rate=self.blend_sofr_interpolated_rate)

    @cached_property
    def blend_ida_new_floating_interest_rate(self) -> float | str:
        return internals.blend_ida_new_floating_interest_rate(blend_calculated_blend_rate=self.blend_calculated_blend_rate)

    @cached_property
    def blend_selected_base_rate(self) -> str | int | float | bool:
        return internals.blend_selected_base_rate(blend_ida_new_floating_currency=self.blend_ida_new_floating_currency, blend_reference_rate_currency=data.BLEND_REFERENCE_RATE_CURRENCY, blend_reference_rate_name=data.BLEND_REFERENCE_RATE_NAME)

    @cached_property
    def blend_quoted_rate_column_header(self) -> str | int | float | bool:
        return internals.blend_quoted_rate_column_header(blend_selected_base_rate=self.blend_selected_base_rate)

    @cached_property
    def blend_published_tenor_years(self) -> data.Series[int | str | None]:
        return internals.blend_published_tenor_years(blend_sofr_tenor_labels=data.BLEND_SOFR_TENOR_LABELS)

    @cached_property
    def blend_sofr_quoted_rate(self) -> data.Series[float | str | None]:
        return internals.blend_sofr_quoted_rate(blend_interpolation_index=data.BLEND_INTERPOLATION_INDEX, blend_sofr_swap_curve=data.BLEND_SOFR_SWAP_CURVE, blend_published_tenor_years=self.blend_published_tenor_years)

    @cached_property
    def blend_sofr_interpolated_rate(self) -> data.Series[float | str | None]:
        return internals.blend_sofr_interpolated_rate(blend_linear_interpolation_header=data.BLEND_LINEAR_INTERPOLATION_HEADER, blend_year_header=data.BLEND_YEAR_HEADER, blend_interpolation_index=data.BLEND_INTERPOLATION_INDEX, blend_quoted_rate_column_header=self.blend_quoted_rate_column_header, blend_sofr_quoted_rate=self.blend_sofr_quoted_rate)

    @cached_property
    def chart_chart_data_scenario_labels_pv_debt_to_gdp(self) -> data.Series[str | int | float | bool | None]:
        return internals.chart_chart_data_scenario_labels_pv_debt_to_gdp(translation_chart_data_exports=data.TRANSLATION_CHART_DATA_EXPORTS, translation_chart_data_primary_balance=data.TRANSLATION_CHART_DATA_PRIMARY_BALANCE, chart_tailored_test_names=data.CHART_TAILORED_TEST_NAMES, start_debt_sustainability_analysis=self.start_debt_sustainability_analysis)

    @cached_property
    def chart_chart_data_scenario_labels_pv_debt_to_exports(self) -> data.Series[str | int | float | bool | None]:
        return internals.chart_chart_data_scenario_labels_pv_debt_to_exports(chart_chart_data_scenario_labels_pv_debt_to_gdp=self.chart_chart_data_scenario_labels_pv_debt_to_gdp)

    @cached_property
    def chart_chart_data_scenario_labels_debt_service_to_exports(self) -> data.Series[str | int | float | bool | None]:
        return internals.chart_chart_data_scenario_labels_debt_service_to_exports(chart_chart_data_scenario_labels_pv_debt_to_gdp=self.chart_chart_data_scenario_labels_pv_debt_to_gdp)

    @cached_property
    def chart_chart_data_scenario_labels_debt_service_to_revenue(self) -> data.Series[str | int | float | bool | None]:
        return internals.chart_chart_data_scenario_labels_debt_service_to_revenue(chart_chart_data_scenario_labels_pv_debt_to_gdp=self.chart_chart_data_scenario_labels_pv_debt_to_gdp)

    @cached_property
    def chart_chart_data_scenario_labels_pv_of_debt_to_gdp_ratio(self) -> data.Series[str | int | float | bool | None]:
        return internals.chart_chart_data_scenario_labels_pv_of_debt_to_gdp_ratio(chart_chart_data_scenario_labels_pv_debt_to_gdp=self.chart_chart_data_scenario_labels_pv_debt_to_gdp)

    @cached_property
    def chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic(self) -> int | str:
        return internals.chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic(chart_tailored_test_names=data.CHART_TAILORED_TEST_NAMES, chart_chart_data_scenario_labels_pv_debt_to_gdp=self.chart_chart_data_scenario_labels_pv_debt_to_gdp, tailored_stress_natural_disaster_applicable=self.tailored_stress_natural_disaster_applicable, tailored_stress_commodity_price_applicable=self.tailored_stress_commodity_price_applicable, tailored_stress_market_financing_applicable=self.tailored_stress_market_financing_applicable)

    @cached_property
    def chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica(self) -> int | str:
        return internals.chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica(chart_tailored_test_names=data.CHART_TAILORED_TEST_NAMES, chart_chart_data_scenario_labels_pv_debt_to_gdp=self.chart_chart_data_scenario_labels_pv_debt_to_gdp, tailored_stress_natural_disaster_applicable=self.tailored_stress_natural_disaster_applicable, tailored_stress_commodity_price_applicable=self.tailored_stress_commodity_price_applicable, tailored_stress_market_financing_applicable=self.tailored_stress_market_financing_applicable)

    @cached_property
    def chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic(self) -> int | str:
        return internals.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic(chart_tailored_test_names=data.CHART_TAILORED_TEST_NAMES, chart_chart_data_scenario_labels_pv_debt_to_gdp=self.chart_chart_data_scenario_labels_pv_debt_to_gdp, tailored_stress_natural_disaster_applicable=self.tailored_stress_natural_disaster_applicable, tailored_stress_commodity_price_applicable=self.tailored_stress_commodity_price_applicable, tailored_stress_market_financing_applicable=self.tailored_stress_market_financing_applicable)

    @cached_property
    def chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market(self) -> int | str:
        return internals.chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market(chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic)

    @cached_property
    def chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress(self) -> int | str:
        return internals.chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress(chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic)

    @cached_property
    def chart_chart_data_pv_debt_to_gdp_most_extreme_shock(self) -> str | int | float | bool:
        return internals.chart_chart_data_pv_debt_to_gdp_most_extreme_shock(chart_combined_contingent_liabilities_label=data.CHART_COMBINED_CONTINGENT_LIABILITIES_LABEL, chart_chart_data_scenario_labels_pv_debt_to_gdp=self.chart_chart_data_scenario_labels_pv_debt_to_gdp, chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio=self.chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio)

    @cached_property
    def chart_chart_data_pv_debt_to_gdp_baseline_breach_count(self) -> int | str:
        return internals.chart_chart_data_pv_debt_to_gdp_baseline_breach_count(chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_figure=self.chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_figure)

    @cached_property
    def chart_chart_data_pv_debt_to_gdp_shock_breach_count(self) -> int | str:
        return internals.chart_chart_data_pv_debt_to_gdp_shock_breach_count(chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_figure=self.chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_figure)

    @cached_property
    def chart_chart_data_pv_debt_to_exports_c2_natural_disaster_stress_path_ap(self) -> int | str:
        return internals.chart_chart_data_pv_debt_to_exports_c2_natural_disaster_stress_path_ap(chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic)

    @cached_property
    def chart_chart_data_pv_debt_to_exports_c3_commodity_price_stress_path_app(self) -> int | str:
        return internals.chart_chart_data_pv_debt_to_exports_c3_commodity_price_stress_path_app(chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica=self.chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica)

    @cached_property
    def chart_chart_data_pv_debt_to_exports_c4_market_financing_stress_path_ap(self) -> int | str:
        return internals.chart_chart_data_pv_debt_to_exports_c4_market_financing_stress_path_ap(chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic)

    @cached_property
    def chart_pv_debt_to_exports_applicable_flag_b2_1_primary_balance_market(self) -> int | str:
        return internals.chart_pv_debt_to_exports_applicable_flag_b2_1_primary_balance_market(chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market=self.chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market)

    @cached_property
    def chart_pv_debt_to_exports_applicable_flag_combined_market_financing_stress(self) -> int | str:
        return internals.chart_pv_debt_to_exports_applicable_flag_combined_market_financing_stress(chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress=self.chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress)

    @cached_property
    def chart_chart_data_pv_debt_to_exports_most_extreme_shock(self) -> str | int | float | bool:
        return internals.chart_chart_data_pv_debt_to_exports_most_extreme_shock(chart_chart_data_scenario_labels_pv_debt_to_exports=self.chart_chart_data_scenario_labels_pv_debt_to_exports, chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports=self.chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports)

    @cached_property
    def chart_chart_data_pv_debt_to_exports_baseline_breach_count(self) -> int | str:
        return internals.chart_chart_data_pv_debt_to_exports_baseline_breach_count(chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_figure=self.chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_figure)

    @cached_property
    def chart_chart_data_pv_debt_to_exports_shock_breach_count(self) -> int | str:
        return internals.chart_chart_data_pv_debt_to_exports_shock_breach_count(chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_figure=self.chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_figure)

    @cached_property
    def chart_debt_service_to_exports_applicable_flag_c2_natdisaster(self) -> int | str:
        return internals.chart_debt_service_to_exports_applicable_flag_c2_natdisaster(chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic)

    @cached_property
    def chart_debt_service_to_exports_applicable_flag_c3_commodity_price(self) -> int | str:
        return internals.chart_debt_service_to_exports_applicable_flag_c3_commodity_price(chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica=self.chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica)

    @cached_property
    def chart_debt_service_to_exports_applicable_flag_c4_mkt_financing(self) -> int | str:
        return internals.chart_debt_service_to_exports_applicable_flag_c4_mkt_financing(chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic)

    @cached_property
    def chart_debt_service_to_exports_applicable_flag_b2_1_primary_balance_market(self) -> int | str:
        return internals.chart_debt_service_to_exports_applicable_flag_b2_1_primary_balance_market(chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market=self.chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market)

    @cached_property
    def chart_debt_service_to_exports_applicable_flag_combined_market_financing_stress(self) -> int | str:
        return internals.chart_debt_service_to_exports_applicable_flag_combined_market_financing_stress(chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress=self.chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress)

    @cached_property
    def chart_chart_data_debt_service_to_exports_most_extreme_shock(self) -> str | int | float | bool:
        return internals.chart_chart_data_debt_service_to_exports_most_extreme_shock(chart_chart_data_scenario_labels_debt_service_to_exports=self.chart_chart_data_scenario_labels_debt_service_to_exports, chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports=self.chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports)

    @cached_property
    def chart_chart_data_debt_service_to_exports_baseline_breach_count(self) -> int | str:
        return internals.chart_chart_data_debt_service_to_exports_baseline_breach_count(chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_figure=self.chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_figure)

    @cached_property
    def chart_chart_data_debt_service_to_exports_shock_breach_count(self) -> int | str:
        return internals.chart_chart_data_debt_service_to_exports_shock_breach_count(chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_figure=self.chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_figure)

    @cached_property
    def chart_debt_service_to_revenue_applicable_flag_c2_natdisaster(self) -> int | str:
        return internals.chart_debt_service_to_revenue_applicable_flag_c2_natdisaster(chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic)

    @cached_property
    def chart_debt_service_to_revenue_applicable_flag_c3_commodity_price(self) -> int | str:
        return internals.chart_debt_service_to_revenue_applicable_flag_c3_commodity_price(chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica=self.chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica)

    @cached_property
    def chart_debt_service_to_revenue_applicable_flag_c4_mkt_financing(self) -> int | str:
        return internals.chart_debt_service_to_revenue_applicable_flag_c4_mkt_financing(chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic)

    @cached_property
    def chart_debt_service_to_revenue_applicable_flag_b2_1_primary_balance_market(self) -> int | str:
        return internals.chart_debt_service_to_revenue_applicable_flag_b2_1_primary_balance_market(chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market=self.chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market)

    @cached_property
    def chart_debt_service_to_revenue_applicable_flag_combined_market_financing_stress(self) -> int | str:
        return internals.chart_debt_service_to_revenue_applicable_flag_combined_market_financing_stress(chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress=self.chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress)

    @cached_property
    def chart_chart_data_debt_service_to_revenue_most_extreme_shock(self) -> str | int | float | bool:
        return internals.chart_chart_data_debt_service_to_revenue_most_extreme_shock(chart_chart_data_scenario_labels_debt_service_to_revenue=self.chart_chart_data_scenario_labels_debt_service_to_revenue, chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue=self.chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue)

    @cached_property
    def chart_chart_data_debt_service_to_revenue_baseline_breach_count(self) -> int | str:
        return internals.chart_chart_data_debt_service_to_revenue_baseline_breach_count(chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_figure=self.chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_figure)

    @cached_property
    def chart_chart_data_debt_service_to_revenue_shock_breach_count(self) -> int | str:
        return internals.chart_chart_data_debt_service_to_revenue_shock_breach_count(chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_figure=self.chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_figure)

    @cached_property
    def chart_chart_data_pv_of_debt_to_gdp_ratio_c2_natural_disaster_stress_pa(self) -> int | str:
        return internals.chart_chart_data_pv_of_debt_to_gdp_ratio_c2_natural_disaster_stress_pa(chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic)

    @cached_property
    def chart_chart_data_pv_of_debt_to_gdp_ratio_c3_commodity_price_stress_pat(self) -> int | str:
        return internals.chart_chart_data_pv_of_debt_to_gdp_ratio_c3_commodity_price_stress_pat(chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica=self.chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica)

    @cached_property
    def chart_chart_data_pv_of_debt_to_gdp_ratio_c4_market_financing_stress_pa(self) -> int | str:
        return internals.chart_chart_data_pv_of_debt_to_gdp_ratio_c4_market_financing_stress_pa(chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic)

    @cached_property
    def chart_pv_of_debt_to_gdp_ratio_applicable_flag_b2_1_primary_balance_market(self) -> int | str:
        return internals.chart_pv_of_debt_to_gdp_ratio_applicable_flag_b2_1_primary_balance_market(chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market=self.chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market)

    @cached_property
    def chart_pv_of_debt_to_gdp_ratio_applicable_flag_combined_market_financing_stress(self) -> int | str:
        return internals.chart_pv_of_debt_to_gdp_ratio_applicable_flag_combined_market_financing_stress(chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress=self.chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress)

    @cached_property
    def chart_chart_data_pv_of_debt_to_gdp_ratio_most_extreme_shock(self) -> str | int | float | bool:
        return internals.chart_chart_data_pv_of_debt_to_gdp_ratio_most_extreme_shock(chart_chart_data_scenario_labels_pv_of_debt_to_gdp_ratio=self.chart_chart_data_scenario_labels_pv_of_debt_to_gdp_ratio, chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp=self.chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp)

    @cached_property
    def chart_chart_data_pv_of_debt_to_gdp_ratio_baseline_breach_count(self) -> int | str:
        return internals.chart_chart_data_pv_of_debt_to_gdp_ratio_baseline_breach_count(chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp_figure=self.chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp_figure)

    @cached_property
    def chart_chart_data_pv_of_debt_to_gdp_ratio_shock_breach_count(self) -> int | str:
        return internals.chart_chart_data_pv_of_debt_to_gdp_ratio_shock_breach_count(chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp_figure=self.chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp_figure)

    @cached_property
    def chart_chart_data_pv_of_debt_to_revenue_ratio_c2_natural_disaster_stres(self) -> int | str:
        return internals.chart_chart_data_pv_of_debt_to_revenue_ratio_c2_natural_disaster_stres(chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic)

    @cached_property
    def chart_chart_data_pv_of_debt_to_revenue_ratio_c3_commodity_price_stress(self) -> int | str:
        return internals.chart_chart_data_pv_of_debt_to_revenue_ratio_c3_commodity_price_stress(chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica=self.chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica)

    @cached_property
    def chart_chart_data_pv_of_debt_to_revenue_ratio_c4_market_financing_stres(self) -> int | str:
        return internals.chart_chart_data_pv_of_debt_to_revenue_ratio_c4_market_financing_stres(chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic)

    @cached_property
    def chart_pv_of_debt_to_revenue_ratio_applicable_flag_b2_1_primary_balance_market(self) -> int | str:
        return internals.chart_pv_of_debt_to_revenue_ratio_applicable_flag_b2_1_primary_balance_market(chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market=self.chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market)

    @cached_property
    def chart_pv_of_debt_to_revenue_ratio_applicable_flag_combined_market_financing_stress(self) -> int | str:
        return internals.chart_pv_of_debt_to_revenue_ratio_applicable_flag_combined_market_financing_stress(chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress=self.chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress)

    @cached_property
    def chart_chart_data_debt_service_to_revenue_ratio_c2_natural_disaster_str(self) -> int | str:
        return internals.chart_chart_data_debt_service_to_revenue_ratio_c2_natural_disaster_str(chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic)

    @cached_property
    def chart_chart_data_debt_service_to_revenue_ratio_c3_commodity_price_stre(self) -> int | str:
        return internals.chart_chart_data_debt_service_to_revenue_ratio_c3_commodity_price_stre(chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica=self.chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica)

    @cached_property
    def chart_chart_data_debt_service_to_revenue_ratio_c4_market_financing_str(self) -> int | str:
        return internals.chart_chart_data_debt_service_to_revenue_ratio_c4_market_financing_str(chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic)

    @cached_property
    def chart_applicable_flag_b2_1_primary_balance_market(self) -> int | str:
        return internals.chart_applicable_flag_b2_1_primary_balance_market(chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market=self.chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market)

    @cached_property
    def chart_applicable_flag_combined_market_financing_stress(self) -> int | str:
        return internals.chart_applicable_flag_combined_market_financing_stress(chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress=self.chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress)

    @cached_property
    def chart_chart_data_debt_service_to_gdp_ratio_c2_natural_disaster_stress_(self) -> int | str:
        return internals.chart_chart_data_debt_service_to_gdp_ratio_c2_natural_disaster_stress_(chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic)

    @cached_property
    def chart_chart_data_debt_service_to_gdp_ratio_c3_commodity_price_stress_p(self) -> int | str:
        return internals.chart_chart_data_debt_service_to_gdp_ratio_c3_commodity_price_stress_p(chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica=self.chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica)

    @cached_property
    def chart_chart_data_debt_service_to_gdp_ratio_c4_market_financing_stress_(self) -> int | str:
        return internals.chart_chart_data_debt_service_to_gdp_ratio_c4_market_financing_stress_(chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic)

    @cached_property
    def chart_debt_service_to_gdp_ratio_applicable_flag_b2_1_primary_balance_market(self) -> int | str:
        return internals.chart_debt_service_to_gdp_ratio_applicable_flag_b2_1_primary_balance_market(chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market=self.chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market)

    @cached_property
    def chart_debt_service_to_gdp_ratio_applicable_flag_combined_market_financing_stress(self) -> int | str:
        return internals.chart_debt_service_to_gdp_ratio_applicable_flag_combined_market_financing_stress(chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress=self.chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress)

    @cached_property
    def chart_fiscal_space_pv_of_debt_to_gdp_max_baseline_breach(self) -> int | str:
        return internals.chart_fiscal_space_pv_of_debt_to_gdp_max_baseline_breach(chart_internal_chart_data_fiscal_space_pv_debt_gdp_moderate_space=self.chart_internal_chart_data_fiscal_space_pv_debt_gdp_moderate_space)

    @cached_property
    def chart_fiscal_space_pv_of_debt_to_exports_max_baseline_breach(self) -> int | str:
        return internals.chart_fiscal_space_pv_of_debt_to_exports_max_baseline_breach(chart_internal_chart_data_fiscal_space_pv_debt_exports_moderate_space=self.chart_internal_chart_data_fiscal_space_pv_debt_exports_moderate_space)

    @cached_property
    def chart_fiscal_space_debt_service_to_exports_max_baseline_breach(self) -> int | str:
        return internals.chart_fiscal_space_debt_service_to_exports_max_baseline_breach(chart_internal_chart_data_fiscal_space_debt_service_exports_moderate_space=self.chart_internal_chart_data_fiscal_space_debt_service_exports_moderate_space)

    @cached_property
    def chart_fiscal_space_debt_service_to_revenue_max_baseline_breach(self) -> int | str:
        return internals.chart_fiscal_space_debt_service_to_revenue_max_baseline_breach(chart_internal_chart_data_fiscal_space_debt_service_revenue_moderate_space=self.chart_internal_chart_data_fiscal_space_debt_service_revenue_moderate_space)

    @cached_property
    def chart_projection_years(self) -> data.Series[int | str | None]:
        return internals.chart_projection_years(macro_debt_main_assumptions_further_details=self.macro_debt_main_assumptions_further_details, macro_debt_further_details=self.macro_debt_further_details)

    @cached_property
    def _scan_chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_stress_path(self) -> internals.ScanChartInternalChartDataPvDebtToGdpPvDebtGdpRatioStressPathResult:
        return internals.scan_chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_stress_path(chart_tailored_test_marker=data.CHART_TAILORED_TEST_MARKER, dsa_ext_pv_of_ppg_external_debt_to_gdp_ratio=self.dsa_ext_pv_of_ppg_external_debt_to_gdp_ratio, dsa_pub_pv_of_debt_gdp=self.dsa_pub_pv_of_debt_gdp, dsa_pub_b2_pb_non_mkt_pub_pv_of_debt_gdp=self.dsa_pub_b2_pb_non_mkt_pub_pv_of_debt_gdp, dsa_pub_c2_natural_disaster_pv_of_debt_gdp=self.dsa_pub_c2_natural_disaster_pv_of_debt_gdp, chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c2_natural_disaster_stress_path_applic, chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica=self.chart_chart_data_pv_debt_to_gdp_c3_commodity_price_stress_path_applica, chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic=self.chart_chart_data_pv_debt_to_gdp_c4_market_financing_stress_path_applic, chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market=self.chart_pv_debt_to_gdp_applicable_flag_b2_1_primary_balance_market, chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress=self.chart_pv_debt_to_gdp_applicable_flag_combined_market_financing_stress, chart_projection_years=self.chart_projection_years, c4_mkt_fin_revised_pv_debt_pct_gdp=self.c4_mkt_fin_revised_pv_debt_pct_gdp, ci_summary_pv_gdp_applicable=self.ci_summary_pv_gdp_applicable, in6opt_standard_scenario=self.in6opt_standard_scenario)

    @cached_property
    def chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_stress_path(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_stress_path.chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_stress_path

    @cached_property
    def chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_stress_path.chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio

    @cached_property
    def chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_figure(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_stress_path.chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_figure

    @cached_property
    def chart_output_pv_debt_gdp_ratio(self) -> data.ChartOutputPvDebtGdpRatio:
        return self._scan_chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_stress_path.chart_output_pv_debt_gdp_ratio

    @cached_property
    def _scan_chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_stress_path(self) -> internals.ScanChartInternalChartDataPvDebtToExportsPvDebtToExportsStressPathResult:
        return internals.scan_chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_stress_path(chart_tailored_test_marker=data.CHART_TAILORED_TEST_MARKER, dsa_ext_pv_of_ppg_external_debt_to_exports_ratio=self.dsa_ext_pv_of_ppg_external_debt_to_exports_ratio, dsa_pub_pv_of_debt_exports=self.dsa_pub_pv_of_debt_exports, dsa_pub_b2_pb_non_mkt_pub_pv_of_debt_exports=self.dsa_pub_b2_pb_non_mkt_pub_pv_of_debt_exports, dsa_pub_c2_natural_disaster_pv_of_debt_exports=self.dsa_pub_c2_natural_disaster_pv_of_debt_exports, chart_chart_data_pv_debt_to_exports_c2_natural_disaster_stress_path_ap=self.chart_chart_data_pv_debt_to_exports_c2_natural_disaster_stress_path_ap, chart_chart_data_pv_debt_to_exports_c3_commodity_price_stress_path_app=self.chart_chart_data_pv_debt_to_exports_c3_commodity_price_stress_path_app, chart_chart_data_pv_debt_to_exports_c4_market_financing_stress_path_ap=self.chart_chart_data_pv_debt_to_exports_c4_market_financing_stress_path_ap, chart_pv_debt_to_exports_applicable_flag_b2_1_primary_balance_market=self.chart_pv_debt_to_exports_applicable_flag_b2_1_primary_balance_market, chart_pv_debt_to_exports_applicable_flag_combined_market_financing_stress=self.chart_pv_debt_to_exports_applicable_flag_combined_market_financing_stress, chart_projection_years=self.chart_projection_years, c4_mkt_fin_revised_pv_debt_to_exports=self.c4_mkt_fin_revised_pv_debt_to_exports, ci_summary_pv_exports_applicable=self.ci_summary_pv_exports_applicable, in6opt_standard_scenario=self.in6opt_standard_scenario, c4_market_path_revised_pv_debt_exports=self.c4_market_path_revised_pv_debt_exports)

    @cached_property
    def chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_stress_path(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_stress_path.chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_stress_path

    @cached_property
    def chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_stress_path.chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports

    @cached_property
    def chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_figure(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_stress_path.chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_figure

    @cached_property
    def chart_output_pv_debt_to_exports(self) -> data.ChartOutputPvDebtToExports:
        return self._scan_chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_stress_path.chart_output_pv_debt_to_exports

    @cached_property
    def _scan_chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_stress_path(self) -> internals.ScanChartInternalChartDataDebtServiceToExportsDebtServiceToExportsStressPathResult:
        return internals.scan_chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_stress_path(chart_tailored_test_marker=data.CHART_TAILORED_TEST_MARKER, dsa_ext_ppg_debt_service_to_exports_ratio=self.dsa_ext_ppg_debt_service_to_exports_ratio, dsa_pub_debt_service_exports=self.dsa_pub_debt_service_exports, dsa_pub_b2_pb_non_mkt_pub_debt_service_exports=self.dsa_pub_b2_pb_non_mkt_pub_debt_service_exports, dsa_pub_c2_natural_disaster_debt_service_exports=self.dsa_pub_c2_natural_disaster_debt_service_exports, chart_debt_service_to_exports_applicable_flag_c2_natdisaster=self.chart_debt_service_to_exports_applicable_flag_c2_natdisaster, chart_debt_service_to_exports_applicable_flag_c3_commodity_price=self.chart_debt_service_to_exports_applicable_flag_c3_commodity_price, chart_debt_service_to_exports_applicable_flag_c4_mkt_financing=self.chart_debt_service_to_exports_applicable_flag_c4_mkt_financing, chart_debt_service_to_exports_applicable_flag_b2_1_primary_balance_market=self.chart_debt_service_to_exports_applicable_flag_b2_1_primary_balance_market, chart_debt_service_to_exports_applicable_flag_combined_market_financing_stress=self.chart_debt_service_to_exports_applicable_flag_combined_market_financing_stress, chart_projection_years=self.chart_projection_years, c4_mkt_fin_dsr_exports_stress=self.c4_mkt_fin_dsr_exports_stress, ci_summary_ds_exports_applicable=self.ci_summary_ds_exports_applicable, in6opt_standard_scenario=self.in6opt_standard_scenario)

    @cached_property
    def chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_stress_path(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_stress_path.chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_stress_path

    @cached_property
    def chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_stress_path.chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports

    @cached_property
    def chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_figure(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_stress_path.chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_figure

    @cached_property
    def chart_output_debt_service_to_exports(self) -> data.ChartOutputDebtServiceToExports:
        return self._scan_chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_stress_path.chart_output_debt_service_to_exports

    @cached_property
    def _scan_chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_stress_path(self) -> internals.ScanChartInternalChartDataDebtServiceToRevenueDebtServiceToRevenueStressPathResult:
        return internals.scan_chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_stress_path(chart_tailored_test_marker=data.CHART_TAILORED_TEST_MARKER, dsa_ext_ppg_debt_service_to_revenue_ratio=self.dsa_ext_ppg_debt_service_to_revenue_ratio, dsa_pub_debt_service_revenue_excl_grants=self.dsa_pub_debt_service_revenue_excl_grants, dsa_pub_b2_pb_non_mkt_pub_debt_service_revenue_excl_grants=self.dsa_pub_b2_pb_non_mkt_pub_debt_service_revenue_excl_grants, dsa_pub_c2_natural_disaster_debt_service_revenue_excl_grants=self.dsa_pub_c2_natural_disaster_debt_service_revenue_excl_grants, chart_debt_service_to_revenue_applicable_flag_c2_natdisaster=self.chart_debt_service_to_revenue_applicable_flag_c2_natdisaster, chart_debt_service_to_revenue_applicable_flag_c3_commodity_price=self.chart_debt_service_to_revenue_applicable_flag_c3_commodity_price, chart_debt_service_to_revenue_applicable_flag_c4_mkt_financing=self.chart_debt_service_to_revenue_applicable_flag_c4_mkt_financing, chart_debt_service_to_revenue_applicable_flag_b2_1_primary_balance_market=self.chart_debt_service_to_revenue_applicable_flag_b2_1_primary_balance_market, chart_debt_service_to_revenue_applicable_flag_combined_market_financing_stress=self.chart_debt_service_to_revenue_applicable_flag_combined_market_financing_stress, chart_projection_years=self.chart_projection_years, c4_mkt_fin_dsr_revenue_stress=self.c4_mkt_fin_dsr_revenue_stress, ci_summary_ds_revenue_applicable=self.ci_summary_ds_revenue_applicable, in6opt_standard_scenario=self.in6opt_standard_scenario)

    @cached_property
    def chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_stress_path(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_stress_path.chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_stress_path

    @cached_property
    def chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_stress_path.chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue

    @cached_property
    def chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_figure(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_stress_path.chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_figure

    @cached_property
    def chart_output_debt_service_to_revenue(self) -> data.ChartOutputDebtServiceToRevenue:
        return self._scan_chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_stress_path.chart_output_debt_service_to_revenue

    @cached_property
    def _scan_chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp(self) -> internals.ScanChartInternalChartDataPvOfDebtToGdpRatioPvDebtToGdpResult:
        return internals.scan_chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp(chart_tailored_test_marker=data.CHART_TAILORED_TEST_MARKER, dsa_pub_pv_of_total_public_debt=self.dsa_pub_pv_of_total_public_debt, customized_public_include_scenario=self.customized_public_include_scenario, chart_chart_data_pv_of_debt_to_gdp_ratio_c2_natural_disaster_stress_pa=self.chart_chart_data_pv_of_debt_to_gdp_ratio_c2_natural_disaster_stress_pa, chart_chart_data_pv_of_debt_to_gdp_ratio_c3_commodity_price_stress_pat=self.chart_chart_data_pv_of_debt_to_gdp_ratio_c3_commodity_price_stress_pat, chart_chart_data_pv_of_debt_to_gdp_ratio_c4_market_financing_stress_pa=self.chart_chart_data_pv_of_debt_to_gdp_ratio_c4_market_financing_stress_pa, chart_pv_of_debt_to_gdp_ratio_applicable_flag_b2_1_primary_balance_market=self.chart_pv_of_debt_to_gdp_ratio_applicable_flag_b2_1_primary_balance_market, chart_pv_of_debt_to_gdp_ratio_applicable_flag_combined_market_financing_stress=self.chart_pv_of_debt_to_gdp_ratio_applicable_flag_combined_market_financing_stress, chart_projection_years=self.chart_projection_years, chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp_stress_path=self.chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp_stress_path, ci_summary_public_pv_medium_cutoff=self.ci_summary_public_pv_medium_cutoff, baseline_pub_pv_of_public_debt_gdp_ratio=self.baseline_pub_pv_of_public_debt_gdp_ratio, baseline_pub_pv_of_public_debt_gdp_ratio_b3_exports=self.baseline_pub_pv_of_public_debt_gdp_ratio_b3_exports, baseline_pub_pv_of_public_debt_gdp_ratio_b4_other_flows=self.baseline_pub_pv_of_public_debt_gdp_ratio_b4_other_flows, baseline_pub_pv_of_public_debt_gdp_ratio_c4_mkt_fin=self.baseline_pub_pv_of_public_debt_gdp_ratio_c4_mkt_fin, custom_pub_pv_of_public_debt_gdp_ratio=self.custom_pub_pv_of_public_debt_gdp_ratio, in6opt_standard_scenario=self.in6opt_standard_scenario)

    @cached_property
    def chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp.chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp

    @cached_property
    def chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp_figure(self) -> data.Series[float | str | None]:
        return self._scan_chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp.chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp_figure

    @cached_property
    def chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp(self) -> data.ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdp:
        return self._scan_chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp.chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp

    @cached_property
    def chart_output_pv_debt_to_gdp(self) -> data.ChartOutputPvDebtToGdp:
        return self._scan_chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp.chart_output_pv_debt_to_gdp

    @cached_property
    def chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp_stress_path(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp_stress_path(dsa_pub_pv_of_total_public_debt=self.dsa_pub_pv_of_total_public_debt)

    @cached_property
    def chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue(chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue=self.chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue)

    @cached_property
    def chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue_stress_path(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue_stress_path(dsa_pub_pv_of_public_debt_to_revenue_and_grants_ratio=self.dsa_pub_pv_of_public_debt_to_revenue_and_grants_ratio)

    @cached_property
    def chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue_figure(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue_figure(dsa_pub_pv_of_public_debt_to_revenue_and_grants_ratio=self.dsa_pub_pv_of_public_debt_to_revenue_and_grants_ratio, baseline_pub_pv_of_public_debt_revenue_grants_ratio_c4_mkt=self.baseline_pub_pv_of_public_debt_revenue_grants_ratio_c4_mkt)

    @cached_property
    def chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue(chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue=self.chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue)

    @cached_property
    def chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue_stress_path(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue_stress_path(dsa_pub_debt_service_to_revenue_and_grants_ratio_in_percent=self.dsa_pub_debt_service_to_revenue_and_grants_ratio_in_percent)

    @cached_property
    def chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue_figure(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue_figure(dsa_pub_debt_service_to_revenue_and_grants_ratio_in_percent=self.dsa_pub_debt_service_to_revenue_and_grants_ratio_in_percent, baseline_pub_debt_service_revenue_grants_ratio_c4_mkt_fin=self.baseline_pub_debt_service_revenue_grants_ratio_c4_mkt_fin)

    @cached_property
    def chart_internal_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio_stress_path(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio_stress_path(dsa_pub_debt_service_to_gdp_ratio_in_percent=self.dsa_pub_debt_service_to_gdp_ratio_in_percent)

    @cached_property
    def chart_internal_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio_figure(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio_figure(dsa_pub_debt_service_to_gdp_ratio_in_percent=self.dsa_pub_debt_service_to_gdp_ratio_in_percent, baseline_pub_debt_service_gdp_ratio_c4_mkt_fin=self.baseline_pub_debt_service_gdp_ratio_c4_mkt_fin)

    @cached_property
    def chart_internal_chart_data_fiscal_space_pv_debt_gdp_moderate_space(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_fiscal_space_pv_debt_gdp_moderate_space(fiscal_space_moderate_assessment_flag=self.fiscal_space_moderate_assessment_flag, fiscal_space_stock_band=self.fiscal_space_stock_band, chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_stress_path=self.chart_internal_chart_data_pv_debt_to_gdp_pv_debt_gdp_ratio_stress_path, chart_output_pv_debt_gdp_ratio=self.chart_output_pv_debt_gdp_ratio)

    @cached_property
    def chart_internal_chart_data_fiscal_space_pv_debt_exports_moderate_space(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_fiscal_space_pv_debt_exports_moderate_space(fiscal_space_moderate_assessment_flag=self.fiscal_space_moderate_assessment_flag, fiscal_space_stock_band=self.fiscal_space_stock_band, chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_stress_path=self.chart_internal_chart_data_pv_debt_to_exports_pv_debt_to_exports_stress_path, chart_output_pv_debt_to_exports=self.chart_output_pv_debt_to_exports)

    @cached_property
    def chart_internal_chart_data_fiscal_space_debt_service_exports_moderate_space(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_fiscal_space_debt_service_exports_moderate_space(fiscal_space_moderate_assessment_flag=self.fiscal_space_moderate_assessment_flag, fiscal_space_flow_band=self.fiscal_space_flow_band, chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_stress_path=self.chart_internal_chart_data_debt_service_to_exports_debt_service_to_exports_stress_path, chart_output_debt_service_to_exports=self.chart_output_debt_service_to_exports)

    @cached_property
    def chart_internal_chart_data_fiscal_space_debt_service_revenue_moderate_space(self) -> data.Series[float | str | None]:
        return internals.chart_internal_chart_data_fiscal_space_debt_service_revenue_moderate_space(fiscal_space_moderate_assessment_flag=self.fiscal_space_moderate_assessment_flag, fiscal_space_flow_band=self.fiscal_space_flow_band, chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_stress_path=self.chart_internal_chart_data_debt_service_to_revenue_debt_service_to_revenue_stress_path, chart_output_debt_service_to_revenue=self.chart_output_debt_service_to_revenue)

    @cached_property
    def ext_debt_old_mlt_debt_service(self) -> data.Series[float | str | None]:
        return internals.ext_debt_old_mlt_debt_service(input3_old_debt_service=self.input3_old_debt_service)

    @cached_property
    def ext_debt_old_mlt_total(self) -> data.Series[float | str | None]:
        return internals.ext_debt_old_mlt_total(ext_debt_old_mlt_debt_service=self.ext_debt_old_mlt_debt_service)

    @cached_property
    def ext_debt_old_mlt_principal(self) -> data.Series[float | str | None]:
        return internals.ext_debt_old_mlt_principal(input3_input_3_old_debt_service_total_principal_payment=self.input3_input_3_old_debt_service_total_principal_payment)

    @cached_property
    def ext_debt_old_mlt_evolution(self) -> data.Series[float | str | None]:
        return internals.ext_debt_old_mlt_evolution(input3_input_3_external_debt_ppg_mlt_external_debt_outstanding=self.input3_input_3_external_debt_ppg_mlt_external_debt_outstanding, ext_debt_old_mlt_principal=self.ext_debt_old_mlt_principal)

    @cached_property
    def ext_debt_locally_issued_service_non_residents(self) -> data.Series[float | str | None]:
        return internals.ext_debt_locally_issued_service_non_residents(input5_old_debt_interest_payment_on_old_debt_denominated_in_local_currency=self.input5_old_debt_interest_payment_on_old_debt_denominated_in_local_currency, input5_old_debt_interest_payment_on_old_debt_denominated_in_foreign_currency=self.input5_old_debt_interest_payment_on_old_debt_denominated_in_foreign_currency, input5_old_debt_principal_payments_on_old_debt_denominated_in_local_currency=self.input5_old_debt_principal_payments_on_old_debt_denominated_in_local_currency, input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency=self.input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency, ext_debt_definition_external_domestic=self.ext_debt_definition_external_domestic, ext_debt_exchange_rate_period_average=self.ext_debt_exchange_rate_period_average, lookup_afg=self.lookup_afg)

    @cached_property
    def ext_debt_locally_issued_service_residents(self) -> data.Series[float | str | None]:
        return internals.ext_debt_locally_issued_service_residents(input5_old_debt_interest_payment_on_old_debt_denominated_in_foreign_currency=self.input5_old_debt_interest_payment_on_old_debt_denominated_in_foreign_currency, input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency=self.input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency, ext_debt_definition_external_domestic=self.ext_debt_definition_external_domestic, ext_debt_exchange_rate_period_average=self.ext_debt_exchange_rate_period_average, lookup_afg=self.lookup_afg)

    @cached_property
    def ext_debt_locally_issued_service_total(self) -> data.Series[float | str | None]:
        return internals.ext_debt_locally_issued_service_total(ext_debt_locally_issued_service_non_residents=self.ext_debt_locally_issued_service_non_residents, ext_debt_locally_issued_service_residents=self.ext_debt_locally_issued_service_residents)

    @cached_property
    def ext_debt_locally_issued_principal(self) -> data.Series[float | str | None]:
        return internals.ext_debt_locally_issued_principal(input5_old_debt_principal_payments_on_old_debt_denominated_in_local_currency=self.input5_old_debt_principal_payments_on_old_debt_denominated_in_local_currency, input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency=self.input5_old_debt_principal_payments_on_old_debt_denominated_in_foreign_currency, ext_debt_definition_external_domestic=self.ext_debt_definition_external_domestic, ext_debt_exchange_rate_period_average=self.ext_debt_exchange_rate_period_average, lookup_afg=self.lookup_afg)

    @cached_property
    def ext_debt_locally_issued_evolution(self) -> data.Series[float | str | None]:
        return internals.ext_debt_locally_issued_evolution(input5_old_debt_outstanding_from_old_debt_in_local_currency=self.input5_old_debt_outstanding_from_old_debt_in_local_currency, input5_old_debt_outstanding_from_old_debt_in_foreign_currency=self.input5_old_debt_outstanding_from_old_debt_in_foreign_currency, ext_debt_definition_external_domestic=self.ext_debt_definition_external_domestic, ext_debt_exchange_rate_eop=self.ext_debt_exchange_rate_eop, lookup_afg=self.lookup_afg)

    @cached_property
    def ext_debt_total_including_locally_issued(self) -> data.Series[float | str | None]:
        return internals.ext_debt_total_including_locally_issued(ext_debt_old_mlt_total=self.ext_debt_old_mlt_total, ext_debt_locally_issued_service_total=self.ext_debt_locally_issued_service_total)

    @cached_property
    def ext_debt_total_principal(self) -> data.Series[float | str | None]:
        return internals.ext_debt_total_principal(ext_debt_old_mlt_principal=self.ext_debt_old_mlt_principal, ext_debt_locally_issued_principal=self.ext_debt_locally_issued_principal)

    @cached_property
    def ext_debt_total_interest(self) -> data.Series[float | str | None]:
        return internals.ext_debt_total_interest(ext_debt_total_including_locally_issued=self.ext_debt_total_including_locally_issued, ext_debt_total_principal=self.ext_debt_total_principal)

    @cached_property
    def ext_debt_stock_of_outstanding_arrears(self) -> data.Series[float | str | None]:
        return internals.ext_debt_stock_of_outstanding_arrears(input3_input_3_external_debt_ppg_external_arrears=self.input3_input_3_external_debt_ppg_external_arrears)

    @cached_property
    def _scan_ext_debt_old_mlt_stock_evolution(self) -> internals.ScanExtDebtOldMltStockEvolutionResult:
        return internals.scan_ext_debt_old_mlt_stock_evolution(input3_ppg_external_debt_stock=data.INPUT3_PPG_EXTERNAL_DEBT_STOCK, input3_input_3_external_debt_ppg_mlt_external_debt_outstanding=self.input3_input_3_external_debt_ppg_mlt_external_debt_outstanding, ext_debt_old_mlt_principal=self.ext_debt_old_mlt_principal, ext_debt_locally_issued_evolution=self.ext_debt_locally_issued_evolution, ext_debt_stock_of_outstanding_arrears=self.ext_debt_stock_of_outstanding_arrears, ext_debt_nominal_new_mlt_total=self.ext_debt_nominal_new_mlt_total, in3_macro_transition_formula_these_o_w_medium_long_term=self.in3_macro_transition_formula_these_o_w_medium_long_term, input3_local_currency_external_debt=self.input3_local_currency_external_debt)

    @cached_property
    def ext_debt_old_mlt_stock_evolution(self) -> data.Series[float | str | None]:
        return self._scan_ext_debt_old_mlt_stock_evolution.ext_debt_old_mlt_stock_evolution

    @cached_property
    def macro_debt_main_assumptions_us_dollars(self) -> data.Series[float | str | None]:
        return self._scan_ext_debt_old_mlt_stock_evolution.macro_debt_main_assumptions_us_dollars

    @cached_property
    def ext_debt_new_disbursements_external(self) -> data.Series[float | str | None]:
        return internals.ext_debt_new_disbursements_external(input4_disbursements=self.input4_disbursements, input4_disbursements_internal=self.input4_disbursements_internal)

    @cached_property
    def ext_debt_new_disbursements_external_total(self) -> data.Series[float | str | None]:
        return internals.ext_debt_new_disbursements_external_total(ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external, ext_debt_new_disbursements_non_residents=self.ext_debt_new_disbursements_non_residents, ext_debt_new_disbursements_residents=self.ext_debt_new_disbursements_residents)

    @cached_property
    def ext_debt_new_disbursements_public_total(self) -> data.Series[float | str | None]:
        return internals.ext_debt_new_disbursements_public_total(input5_disbursements_total_public_new_domestic_disbursements_residency_based=self.input5_disbursements_total_public_new_domestic_disbursements_residency_based, ext_debt_new_disbursements_external_total=self.ext_debt_new_disbursements_external_total, ext_debt_st_total=self.ext_debt_st_total, ext_debt_exchange_rate_period_average=self.ext_debt_exchange_rate_period_average)

    @cached_property
    def ext_debt_marginal_share_external_ppg_mlt(self) -> data.Series[float | str | None]:
        return internals.ext_debt_marginal_share_external_ppg_mlt(ext_debt_new_disbursements_external_total=self.ext_debt_new_disbursements_external_total, ext_debt_new_disbursements_public_total=self.ext_debt_new_disbursements_public_total)

    @cached_property
    def ext_debt_marginal_share_external_ppg_mlt_average(self) -> float | str:
        return internals.ext_debt_marginal_share_external_ppg_mlt_average(ext_debt_marginal_share_external_ppg_mlt=self.ext_debt_marginal_share_external_ppg_mlt)

    @cached_property
    def ext_debt_marginal_share_external_ppg_mlt_residual_financing(self) -> float | str:
        return internals.ext_debt_marginal_share_external_ppg_mlt_residual_financing(ext_debt_marginal_share_external_ppg_mlt_average=self.ext_debt_marginal_share_external_ppg_mlt_average)

    @cached_property
    def ext_debt_marginal_share_domestic_mlt(self) -> data.Series[float | str | None]:
        return internals.ext_debt_marginal_share_domestic_mlt(input5_disbursements_public_domestic_mlt_disbursements_residency_based=self.input5_disbursements_public_domestic_mlt_disbursements_residency_based, ext_debt_new_disbursements_public_total=self.ext_debt_new_disbursements_public_total, ext_debt_exchange_rate_period_average=self.ext_debt_exchange_rate_period_average)

    @cached_property
    def ext_debt_marginal_share_domestic_mlt_average(self) -> float | str:
        return internals.ext_debt_marginal_share_domestic_mlt_average(ext_debt_marginal_share_domestic_mlt=self.ext_debt_marginal_share_domestic_mlt)

    @cached_property
    def ext_debt_marginal_share_domestic_mlt_residual_financing(self) -> float | str:
        return internals.ext_debt_marginal_share_domestic_mlt_residual_financing(ext_debt_marginal_share_domestic_mlt_average=self.ext_debt_marginal_share_domestic_mlt_average)

    @cached_property
    def ext_debt_marginal_share_domestic_st(self) -> data.Series[float | str | None]:
        return internals.ext_debt_marginal_share_domestic_st(input5_disbursements_public_domestic_st_disbursements_residency_based=self.input5_disbursements_public_domestic_st_disbursements_residency_based, ext_debt_new_disbursements_public_total=self.ext_debt_new_disbursements_public_total, ext_debt_exchange_rate_period_average=self.ext_debt_exchange_rate_period_average)

    @cached_property
    def ext_debt_marginal_share_domestic_st_average(self) -> float | str:
        return internals.ext_debt_marginal_share_domestic_st_average(ext_debt_marginal_share_domestic_st=self.ext_debt_marginal_share_domestic_st)

    @cached_property
    def ext_debt_marginal_share_domestic_st_residual_financing(self) -> float | str:
        return internals.ext_debt_marginal_share_domestic_st_residual_financing(ext_debt_marginal_share_domestic_st_average=self.ext_debt_marginal_share_domestic_st_average)

    @cached_property
    def ext_debt_residual_interest_rate(self) -> data.Series[float | str | None]:
        return internals.ext_debt_residual_interest_rate(input4_interest_rate=self.input4_interest_rate, input4_terms_ida_regular=self.input4_terms_ida_regular, input4_terms_ida_and_lc=self.input4_terms_ida_and_lc, input4_terms_bonds_fx_non_residents=self.input4_terms_bonds_fx_non_residents, input4_terms_bonds_fx_residents=self.input4_terms_bonds_fx_residents, ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external, ext_debt_new_disbursements_non_residents=self.ext_debt_new_disbursements_non_residents, ext_debt_new_disbursements_residents=self.ext_debt_new_disbursements_residents, ext_debt_new_disbursements_external_total=self.ext_debt_new_disbursements_external_total)

    @cached_property
    def ext_debt_residual_interest_rate_summary(self) -> float | str:
        return internals.ext_debt_residual_interest_rate_summary(ext_debt_residual_interest_rate=self.ext_debt_residual_interest_rate)

    @cached_property
    def ext_debt_residual_grace_period(self) -> data.Series[float | str | None]:
        return internals.ext_debt_residual_grace_period(input4_grace_period=self.input4_grace_period, input4_terms_ida_regular=self.input4_terms_ida_regular, input4_terms_ida_and_lc=self.input4_terms_ida_and_lc, input4_terms_bonds_fx_non_residents=self.input4_terms_bonds_fx_non_residents, input4_terms_bonds_fx_residents=self.input4_terms_bonds_fx_residents, ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external, ext_debt_new_disbursements_non_residents=self.ext_debt_new_disbursements_non_residents, ext_debt_new_disbursements_residents=self.ext_debt_new_disbursements_residents, ext_debt_new_disbursements_external_total=self.ext_debt_new_disbursements_external_total)

    @cached_property
    def ext_debt_residual_grace_period_summary(self) -> float | str:
        return internals.ext_debt_residual_grace_period_summary(ext_debt_residual_grace_period=self.ext_debt_residual_grace_period)

    @cached_property
    def ext_debt_residual_maturity(self) -> data.Series[float | str | None]:
        return internals.ext_debt_residual_maturity(input4_loan_maturity=self.input4_loan_maturity, input4_terms_ida_regular=self.input4_terms_ida_regular, input4_terms_ida_and_lc=self.input4_terms_ida_and_lc, input4_terms_bonds_fx_non_residents=self.input4_terms_bonds_fx_non_residents, input4_terms_bonds_fx_residents=self.input4_terms_bonds_fx_residents, ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external, ext_debt_new_disbursements_non_residents=self.ext_debt_new_disbursements_non_residents, ext_debt_new_disbursements_residents=self.ext_debt_new_disbursements_residents, ext_debt_new_disbursements_external_total=self.ext_debt_new_disbursements_external_total)

    @cached_property
    def ext_debt_residual_maturity_summary(self) -> float | str:
        return internals.ext_debt_residual_maturity_summary(ext_debt_residual_maturity=self.ext_debt_residual_maturity)

    @cached_property
    def ext_debt_residual_grace_period_rounded_summary(self) -> float | str:
        return internals.ext_debt_residual_grace_period_rounded_summary(ext_debt_residual_grace_period_summary=self.ext_debt_residual_grace_period_summary)

    @cached_property
    def ext_debt_residual_maturity_rounded_summary(self) -> float | str:
        return internals.ext_debt_residual_maturity_rounded_summary(ext_debt_residual_maturity_summary=self.ext_debt_residual_maturity_summary)

    @cached_property
    def ext_debt_residual_interest_rate_residual_financing(self) -> float | str:
        return internals.ext_debt_residual_interest_rate_residual_financing(ext_debt_residual_interest_rate_summary=self.ext_debt_residual_interest_rate_summary)

    @cached_property
    def ext_debt_residual_grace_period_residual_financing(self) -> float | str:
        return internals.ext_debt_residual_grace_period_residual_financing(ext_debt_residual_grace_period_rounded_summary=self.ext_debt_residual_grace_period_rounded_summary)

    @cached_property
    def ext_debt_residual_maturity_residual_financing(self) -> float | str:
        return internals.ext_debt_residual_maturity_residual_financing(ext_debt_residual_maturity_rounded_summary=self.ext_debt_residual_maturity_rounded_summary)

    @cached_property
    def ext_debt_definition_external_domestic(self) -> str | int | float | bool:
        return internals.ext_debt_definition_external_domestic(external_domestic_debt_definition=self.external_domestic_debt_definition)

    @cached_property
    def ext_debt_new_interest_external(self) -> data.Series[float | str | None]:
        return internals.ext_debt_new_interest_external(pv_base_output_interest=self.pv_base_output_interest)

    @cached_property
    def ext_debt_new_amortization_external(self) -> data.Series[float | str | None]:
        return internals.ext_debt_new_amortization_external(pv_base_output_amortization=self.pv_base_output_amortization)

    @cached_property
    def ext_debt_pv_old_mlt_total(self) -> data.Series[float | str | None]:
        return internals.ext_debt_pv_old_mlt_total(ext_debt_pv_old_mlt_by_instrument=self.ext_debt_pv_old_mlt_by_instrument, ext_debt_pv_old_locally_issued=self.ext_debt_pv_old_locally_issued)

    @cached_property
    def ext_debt_pv_old_mlt_by_instrument(self) -> data.Series[float | str | None]:
        return internals.ext_debt_pv_old_mlt_by_instrument(input4_discount_rate=self.input4_discount_rate, ext_debt_old_mlt_debt_service=self.ext_debt_old_mlt_debt_service)

    @cached_property
    def ext_debt_pv_old_locally_issued(self) -> data.Series[float | str | None]:
        return internals.ext_debt_pv_old_locally_issued(ext_debt_locally_issued_evolution=self.ext_debt_locally_issued_evolution)

    @cached_property
    def ext_debt_pv_existing_arrears(self) -> data.Series[float | str | None]:
        return internals.ext_debt_pv_existing_arrears(ext_debt_stock_of_outstanding_arrears=self.ext_debt_stock_of_outstanding_arrears)

    @cached_property
    def ext_debt_pv_new_mlt_total(self) -> data.Series[float | str | None]:
        return internals.ext_debt_pv_new_mlt_total(ext_debt_pv_new_mlt_external=self.ext_debt_pv_new_mlt_external, ext_debt_pv_new_mlt_non_residents=self.ext_debt_pv_new_mlt_non_residents, ext_debt_pv_new_mlt_residents=self.ext_debt_pv_new_mlt_residents)

    @cached_property
    def ext_debt_pv_new_mlt_external(self) -> data.Series[float | str | None]:
        return internals.ext_debt_pv_new_mlt_external(pv_base_output_pv_of_debt=self.pv_base_output_pv_of_debt)

    @cached_property
    def ext_debt_pv_new_mlt_non_residents(self) -> data.Series[float | str | None]:
        return internals.ext_debt_pv_new_mlt_non_residents(pv_base_output_pv_of_debt_fx=self.pv_base_output_pv_of_debt_fx, pv_lc_summary_pv_of_debt_in_usd=self.pv_lc_summary_pv_of_debt_in_usd)

    @cached_property
    def ext_debt_pv_new_mlt_residents(self) -> data.Series[float | str | None]:
        return internals.ext_debt_pv_new_mlt_residents(pv_base_output_pv_of_debt_fx=self.pv_base_output_pv_of_debt_fx)

    @cached_property
    def ext_debt_nominal_new_mlt_total(self) -> data.Series[float | str | None]:
        return internals.ext_debt_nominal_new_mlt_total(ext_debt_nominal_new_mlt_external=self.ext_debt_nominal_new_mlt_external, ext_debt_nominal_new_mlt_non_residents=self.ext_debt_nominal_new_mlt_non_residents, ext_debt_nominal_new_mlt_residents=self.ext_debt_nominal_new_mlt_residents)

    @cached_property
    def ext_debt_nominal_new_mlt_external(self) -> data.Series[float | str | None]:
        return internals.ext_debt_nominal_new_mlt_external(pv_base_output_stock_of_new_forex_debt_in_usd=self.pv_base_output_stock_of_new_forex_debt_in_usd)

    @cached_property
    def ext_debt_nominal_new_mlt_non_residents(self) -> data.Series[float | str | None]:
        return internals.ext_debt_nominal_new_mlt_non_residents(pv_base_output_stock_of_new_forex_debt_in_usd_fx=self.pv_base_output_stock_of_new_forex_debt_in_usd_fx, pv_lc_summary_stock_of_debt_in_usd=self.pv_lc_summary_stock_of_debt_in_usd)

    @cached_property
    def ext_debt_nominal_new_mlt_residents(self) -> data.Series[float | str | None]:
        return internals.ext_debt_nominal_new_mlt_residents(pv_base_output_stock_of_new_forex_debt_in_usd_fx=self.pv_base_output_stock_of_new_forex_debt_in_usd_fx)

    @cached_property
    def ext_debt_st_external_nominal(self) -> data.Series[float | str | None]:
        return internals.ext_debt_st_external_nominal(input3_input_3_external_debt_ppg_st_external_debt_outstanding=self.input3_input_3_external_debt_ppg_st_external_debt_outstanding)

    @cached_property
    def ext_debt_st_external_interest(self) -> data.Series[float | str | None]:
        return internals.ext_debt_st_external_interest(input4_interest_rate=self.input4_interest_rate, ext_debt_st_external_nominal=self.ext_debt_st_external_nominal)

    @cached_property
    def ext_debt_st_locally_issued_nominal(self) -> data.Series[float | str | None]:
        return internals.ext_debt_st_locally_issued_nominal(input5_new_debt_principal_payments_on_new_debt_denominated_in_foreign_currency_ow_short_term=self.input5_new_debt_principal_payments_on_new_debt_denominated_in_foreign_currency_ow_short_term, input5_new_debt_principal_payments_on_new_debt_denominated_in_local_currency_ow_short_term=self.input5_new_debt_principal_payments_on_new_debt_denominated_in_local_currency_ow_short_term, ext_debt_definition_external_domestic=self.ext_debt_definition_external_domestic, ext_debt_exchange_rate_eop=self.ext_debt_exchange_rate_eop, lookup_afg=self.lookup_afg)

    @cached_property
    def ext_debt_st_total(self) -> data.Series[float | str | None]:
        return internals.ext_debt_st_total(ext_debt_st_external_nominal=self.ext_debt_st_external_nominal, ext_debt_st_locally_issued_nominal=self.ext_debt_st_locally_issued_nominal)

    @cached_property
    def ext_debt_pv_net_use_of_sdrs(self) -> data.Series[float | str | None]:
        return internals.ext_debt_pv_net_use_of_sdrs(in8_sdr_pv_of_interest_payments_in_million_of_usd=self.in8_sdr_pv_of_interest_payments_in_million_of_usd)

    @cached_property
    def ext_debt_total_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.ext_debt_total_pv_of_debt(ext_debt_pv_old_mlt_total=self.ext_debt_pv_old_mlt_total, ext_debt_pv_existing_arrears=self.ext_debt_pv_existing_arrears, ext_debt_pv_new_mlt_total=self.ext_debt_pv_new_mlt_total, ext_debt_st_total=self.ext_debt_st_total, ext_debt_pv_net_use_of_sdrs=self.ext_debt_pv_net_use_of_sdrs)

    @cached_property
    def ext_debt_total_public_debt_service(self) -> data.Series[float | str | None]:
        return internals.ext_debt_total_public_debt_service(ext_debt_public_debt_service_principal=self.ext_debt_public_debt_service_principal, ext_debt_public_debt_service_interest=self.ext_debt_public_debt_service_interest)

    @cached_property
    def ext_debt_public_debt_service_principal(self) -> data.Series[float | str | None]:
        return internals.ext_debt_public_debt_service_principal(ext_debt_total_principal=self.ext_debt_total_principal, ext_debt_new_amortization_total=self.ext_debt_new_amortization_total, ext_debt_st_total_principal=self.ext_debt_st_total_principal)

    @cached_property
    def ext_debt_public_debt_service_interest(self) -> data.Series[float | str | None]:
        return internals.ext_debt_public_debt_service_interest(ext_debt_total_interest=self.ext_debt_total_interest, ext_debt_new_interest_total=self.ext_debt_new_interest_total, ext_debt_st_total_interest=self.ext_debt_st_total_interest, in8_sdr_interest_payments_in_million_of_usd=self.in8_sdr_interest_payments_in_million_of_usd)

    @cached_property
    def ext_debt_external_debt_outstanding(self) -> data.Series[float | str | None]:
        return internals.ext_debt_external_debt_outstanding(ext_debt_stock_of_outstanding_arrears=self.ext_debt_stock_of_outstanding_arrears, ext_debt_old_mlt_stock_evolution=self.ext_debt_old_mlt_stock_evolution, ext_debt_nominal_new_mlt_total=self.ext_debt_nominal_new_mlt_total)

    @cached_property
    def ext_debt_fx_denominated_debt_outstanding(self) -> data.Series[float | str | None]:
        return internals.ext_debt_fx_denominated_debt_outstanding(input5_old_debt_outstanding_from_old_debt_in_foreign_currency_usd=self.input5_old_debt_outstanding_from_old_debt_in_foreign_currency_usd, input5_new_debt_debt_stock_on_new_debt_denominated_in_foreign_currency=self.input5_new_debt_debt_stock_on_new_debt_denominated_in_foreign_currency, ext_debt_old_mlt_evolution=self.ext_debt_old_mlt_evolution, ext_debt_stock_of_outstanding_arrears=self.ext_debt_stock_of_outstanding_arrears, ext_debt_definition_external_domestic=self.ext_debt_definition_external_domestic, ext_debt_nominal_new_mlt_external=self.ext_debt_nominal_new_mlt_external, ext_debt_nominal_new_mlt_non_residents=self.ext_debt_nominal_new_mlt_non_residents, ext_debt_st_external_nominal=self.ext_debt_st_external_nominal, ext_debt_external_debt_outstanding=self.ext_debt_external_debt_outstanding, ext_debt_exchange_rate_eop=self.ext_debt_exchange_rate_eop, lookup_afg=self.lookup_afg)

    @cached_property
    def ext_debt_exchange_rate_eop(self) -> data.Series[float | str | None]:
        return internals.ext_debt_exchange_rate_eop(macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar)

    @cached_property
    def ext_debt_exchange_rate_period_average(self) -> data.Series[float | str | None]:
        return internals.ext_debt_exchange_rate_period_average(macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def imported_country_code(self) -> int | str:
        return internals.imported_country_code(in1_basics_country_code=self.in1_basics_country_code)

    @cached_property
    def imported_classification_years(self) -> data.Series[int | str | None]:
        return internals.imported_classification_years(classification_cpia_reported_years=data.CLASSIFICATION_CPIA_REPORTED_YEARS)

    @cached_property
    def imported_classification_values(self) -> data.Series[float | str | None]:
        return internals.imported_classification_values(classification_cpia_reported_codes=data.CLASSIFICATION_CPIA_REPORTED_CODES, classification_cpia_reported_years=data.CLASSIFICATION_CPIA_REPORTED_YEARS, classification_cpia_reported_values=data.CLASSIFICATION_CPIA_REPORTED_VALUES, classification_growth_reported_codes=data.CLASSIFICATION_GROWTH_REPORTED_CODES, classification_growth_reported_years=data.CLASSIFICATION_GROWTH_REPORTED_YEARS, classification_growth_reported_values=data.CLASSIFICATION_GROWTH_REPORTED_VALUES, classification_growth_actual_codes=data.CLASSIFICATION_GROWTH_ACTUAL_CODES, classification_growth_actual_years=data.CLASSIFICATION_GROWTH_ACTUAL_YEARS, classification_growth_actual_values=data.CLASSIFICATION_GROWTH_ACTUAL_VALUES, classification_reserves_reported_codes=data.CLASSIFICATION_RESERVES_REPORTED_CODES, classification_reserves_reported_years=data.CLASSIFICATION_RESERVES_REPORTED_YEARS, classification_reserves_reported_values=data.CLASSIFICATION_RESERVES_REPORTED_VALUES, classification_reserves_actual_codes=data.CLASSIFICATION_RESERVES_ACTUAL_CODES, classification_reserves_actual_years=data.CLASSIFICATION_RESERVES_ACTUAL_YEARS, classification_reserves_actual_values=data.CLASSIFICATION_RESERVES_ACTUAL_VALUES, classification_remittances_reported_codes=data.CLASSIFICATION_REMITTANCES_REPORTED_CODES, classification_remittances_reported_years=data.CLASSIFICATION_REMITTANCES_REPORTED_YEARS, classification_remittances_reported_values=data.CLASSIFICATION_REMITTANCES_REPORTED_VALUES, classification_remittances_actual_codes=data.CLASSIFICATION_REMITTANCES_ACTUAL_CODES, classification_remittances_actual_years=data.CLASSIFICATION_REMITTANCES_ACTUAL_YEARS, classification_remittances_actual_values=data.CLASSIFICATION_REMITTANCES_ACTUAL_VALUES, classification_world_growth_reported_codes=data.CLASSIFICATION_WORLD_GROWTH_REPORTED_CODES, classification_world_growth_reported_years=data.CLASSIFICATION_WORLD_GROWTH_REPORTED_YEARS, classification_world_growth_reported_values=data.CLASSIFICATION_WORLD_GROWTH_REPORTED_VALUES, classification_lookup_year_id_note=data.CLASSIFICATION_LOOKUP_YEAR_ID_NOTE, classification_classification_prior_vintage_header=data.CLASSIFICATION_CLASSIFICATION_PRIOR_VINTAGE_HEADER, classification_classification_two_vintages_ago_header=data.CLASSIFICATION_CLASSIFICATION_TWO_VINTAGES_AGO_HEADER, classification_ci_score_prior_vintage_header=data.CLASSIFICATION_CI_SCORE_PRIOR_VINTAGE_HEADER, classification_ci_score_two_vintages_ago_column_header=data.CLASSIFICATION_CI_SCORE_TWO_VINTAGES_AGO_COLUMN_HEADER, classification_column_headers=data.CLASSIFICATION_COLUMN_HEADERS, classification_ifs_code=data.CLASSIFICATION_IFS_CODE, classification_iso_alpha3=data.CLASSIFICATION_ISO_ALPHA3, classification_country_name=data.CLASSIFICATION_COUNTRY_NAME, classification_classification_final=data.CLASSIFICATION_CLASSIFICATION_FINAL, classification_classification_current_vintage=data.CLASSIFICATION_CLASSIFICATION_CURRENT_VINTAGE, classification_classification_previous_vintage=data.CLASSIFICATION_CLASSIFICATION_PREVIOUS_VINTAGE, classification_classification_final_previous=data.CLASSIFICATION_CLASSIFICATION_FINAL_PREVIOUS, classification_current_ci_score_current_vintage=data.CLASSIFICATION_CURRENT_CI_SCORE_CURRENT_VINTAGE, classification_current_ci_score_previous_vintage=data.CLASSIFICATION_CURRENT_CI_SCORE_PREVIOUS_VINTAGE, classification_current_ci_score_2_vintages_ago=data.CLASSIFICATION_CURRENT_CI_SCORE_2_VINTAGES_AGO, classification_current_cpia=data.CLASSIFICATION_CURRENT_CPIA, classification_current_growth=data.CLASSIFICATION_CURRENT_GROWTH, classification_current_reserves=data.CLASSIFICATION_CURRENT_RESERVES, classification_current_remittances=data.CLASSIFICATION_CURRENT_REMITTANCES, classification_current_world_growth=data.CLASSIFICATION_CURRENT_WORLD_GROWTH, classification_growth_memo_primary=data.CLASSIFICATION_GROWTH_MEMO_PRIMARY, classification_growth_memo_secondary=data.CLASSIFICATION_GROWTH_MEMO_SECONDARY, classification_reserves_memo=data.CLASSIFICATION_RESERVES_MEMO, classification_remittances_memo=data.CLASSIFICATION_REMITTANCES_MEMO, classification_ci_score_2018_oct_header=data.CLASSIFICATION_CI_SCORE_2018_OCT_HEADER, classification_ci_class_2018_oct_header=data.CLASSIFICATION_CI_CLASS_2018_OCT_HEADER, classification_ci_score_2018_oct_label=data.CLASSIFICATION_CI_SCORE_2018_OCT_LABEL, classification_ci_class_2018_oct_label=data.CLASSIFICATION_CI_CLASS_2018_OCT_LABEL, classification_ci_score_2018_oct=data.CLASSIFICATION_CI_SCORE_2018_OCT, classification_ci_class_2018_oct=data.CLASSIFICATION_CI_CLASS_2018_OCT, classification_ci_components_share_headers=data.CLASSIFICATION_CI_COMPONENTS_SHARE_HEADERS, classification_ci_components_share=data.CLASSIFICATION_CI_COMPONENTS_SHARE, classification_ci_components_contribution_headers=data.CLASSIFICATION_CI_COMPONENTS_CONTRIBUTION_HEADERS, classification_ci_components_contribution=data.CLASSIFICATION_CI_COMPONENTS_CONTRIBUTION, data_rem_headers=data.DATA_REM_HEADERS, data_rem_notes_header=data.DATA_REM_NOTES_HEADER, data_rem_metadata=data.DATA_REM_METADATA, data_gdpusd_headers=data.DATA_GDPUSD_HEADERS, data_gdpusd_country_code_note=data.DATA_GDPUSD_COUNTRY_CODE_NOTE, data_gdpusd_metadata=data.DATA_GDPUSD_METADATA, data_gdpusd_ifs_code=data.DATA_GDPUSD_IFS_CODE, imported_country_code=self.imported_country_code, imported_classification_years=self.imported_classification_years, imported_classification_ids=self.imported_classification_ids)

    @cached_property
    def imported_classification_ids(self) -> data.Series[str | int | float | bool | None]:
        return internals.imported_classification_ids(imported_series_stub_cpia=data.IMPORTED_SERIES_STUB_CPIA, imported_series_stub_gr_a=data.IMPORTED_SERIES_STUB_GR_A, imported_series_stub_res_a=data.IMPORTED_SERIES_STUB_RES_A, imported_series_stub_wgr=data.IMPORTED_SERIES_STUB_WGR, imported_components=self.imported_components)

    @cached_property
    def imported_cpia_rating(self) -> data.Series[str | int | float | bool | None]:
        return internals.imported_cpia_rating(imported_classification_prior_vintage=data.IMPORTED_CLASSIFICATION_PRIOR_VINTAGE, imported_classification_two_vintages_ago=data.IMPORTED_CLASSIFICATION_TWO_VINTAGES_AGO, classification_cpia_reported_codes=data.CLASSIFICATION_CPIA_REPORTED_CODES, classification_cpia_reported_years=data.CLASSIFICATION_CPIA_REPORTED_YEARS, classification_cpia_reported_values=data.CLASSIFICATION_CPIA_REPORTED_VALUES, classification_growth_reported_codes=data.CLASSIFICATION_GROWTH_REPORTED_CODES, classification_growth_reported_years=data.CLASSIFICATION_GROWTH_REPORTED_YEARS, classification_growth_reported_values=data.CLASSIFICATION_GROWTH_REPORTED_VALUES, classification_growth_actual_codes=data.CLASSIFICATION_GROWTH_ACTUAL_CODES, classification_growth_actual_years=data.CLASSIFICATION_GROWTH_ACTUAL_YEARS, classification_growth_actual_values=data.CLASSIFICATION_GROWTH_ACTUAL_VALUES, classification_reserves_reported_codes=data.CLASSIFICATION_RESERVES_REPORTED_CODES, classification_reserves_reported_years=data.CLASSIFICATION_RESERVES_REPORTED_YEARS, classification_reserves_reported_values=data.CLASSIFICATION_RESERVES_REPORTED_VALUES, classification_reserves_actual_codes=data.CLASSIFICATION_RESERVES_ACTUAL_CODES, classification_reserves_actual_years=data.CLASSIFICATION_RESERVES_ACTUAL_YEARS, classification_reserves_actual_values=data.CLASSIFICATION_RESERVES_ACTUAL_VALUES, classification_remittances_reported_codes=data.CLASSIFICATION_REMITTANCES_REPORTED_CODES, classification_remittances_reported_years=data.CLASSIFICATION_REMITTANCES_REPORTED_YEARS, classification_remittances_reported_values=data.CLASSIFICATION_REMITTANCES_REPORTED_VALUES, classification_remittances_actual_codes=data.CLASSIFICATION_REMITTANCES_ACTUAL_CODES, classification_remittances_actual_years=data.CLASSIFICATION_REMITTANCES_ACTUAL_YEARS, classification_remittances_actual_values=data.CLASSIFICATION_REMITTANCES_ACTUAL_VALUES, classification_world_growth_reported_codes=data.CLASSIFICATION_WORLD_GROWTH_REPORTED_CODES, classification_world_growth_reported_years=data.CLASSIFICATION_WORLD_GROWTH_REPORTED_YEARS, classification_world_growth_reported_values=data.CLASSIFICATION_WORLD_GROWTH_REPORTED_VALUES, classification_lookup_year_id_note=data.CLASSIFICATION_LOOKUP_YEAR_ID_NOTE, classification_classification_prior_vintage_header=data.CLASSIFICATION_CLASSIFICATION_PRIOR_VINTAGE_HEADER, classification_classification_two_vintages_ago_header=data.CLASSIFICATION_CLASSIFICATION_TWO_VINTAGES_AGO_HEADER, classification_ci_score_prior_vintage_header=data.CLASSIFICATION_CI_SCORE_PRIOR_VINTAGE_HEADER, classification_ci_score_two_vintages_ago_column_header=data.CLASSIFICATION_CI_SCORE_TWO_VINTAGES_AGO_COLUMN_HEADER, classification_column_headers=data.CLASSIFICATION_COLUMN_HEADERS, classification_ifs_code=data.CLASSIFICATION_IFS_CODE, classification_iso_alpha3=data.CLASSIFICATION_ISO_ALPHA3, classification_country_name=data.CLASSIFICATION_COUNTRY_NAME, classification_classification_final=data.CLASSIFICATION_CLASSIFICATION_FINAL, classification_classification_current_vintage=data.CLASSIFICATION_CLASSIFICATION_CURRENT_VINTAGE, classification_classification_previous_vintage=data.CLASSIFICATION_CLASSIFICATION_PREVIOUS_VINTAGE, classification_classification_final_previous=data.CLASSIFICATION_CLASSIFICATION_FINAL_PREVIOUS, classification_current_ci_score_current_vintage=data.CLASSIFICATION_CURRENT_CI_SCORE_CURRENT_VINTAGE, classification_current_ci_score_previous_vintage=data.CLASSIFICATION_CURRENT_CI_SCORE_PREVIOUS_VINTAGE, classification_current_ci_score_2_vintages_ago=data.CLASSIFICATION_CURRENT_CI_SCORE_2_VINTAGES_AGO, classification_current_cpia=data.CLASSIFICATION_CURRENT_CPIA, classification_current_growth=data.CLASSIFICATION_CURRENT_GROWTH, classification_current_reserves=data.CLASSIFICATION_CURRENT_RESERVES, classification_current_remittances=data.CLASSIFICATION_CURRENT_REMITTANCES, classification_current_world_growth=data.CLASSIFICATION_CURRENT_WORLD_GROWTH, classification_growth_memo_primary=data.CLASSIFICATION_GROWTH_MEMO_PRIMARY, classification_growth_memo_secondary=data.CLASSIFICATION_GROWTH_MEMO_SECONDARY, classification_reserves_memo=data.CLASSIFICATION_RESERVES_MEMO, classification_remittances_memo=data.CLASSIFICATION_REMITTANCES_MEMO, classification_ci_score_2018_oct_header=data.CLASSIFICATION_CI_SCORE_2018_OCT_HEADER, classification_ci_class_2018_oct_header=data.CLASSIFICATION_CI_CLASS_2018_OCT_HEADER, classification_ci_score_2018_oct_label=data.CLASSIFICATION_CI_SCORE_2018_OCT_LABEL, classification_ci_class_2018_oct_label=data.CLASSIFICATION_CI_CLASS_2018_OCT_LABEL, classification_ci_score_2018_oct=data.CLASSIFICATION_CI_SCORE_2018_OCT, classification_ci_class_2018_oct=data.CLASSIFICATION_CI_CLASS_2018_OCT, classification_ci_components_share_headers=data.CLASSIFICATION_CI_COMPONENTS_SHARE_HEADERS, classification_ci_components_share=data.CLASSIFICATION_CI_COMPONENTS_SHARE, classification_ci_components_contribution_headers=data.CLASSIFICATION_CI_COMPONENTS_CONTRIBUTION_HEADERS, classification_ci_components_contribution=data.CLASSIFICATION_CI_COMPONENTS_CONTRIBUTION, imported_country_code=self.imported_country_code)

    @cached_property
    def imported_composite_indicator(self) -> data.Series[str | int | float | bool | None]:
        return internals.imported_composite_indicator(imported_class_code_weak=data.IMPORTED_CLASS_CODE_WEAK, imported_class_label_weak=data.IMPORTED_CLASS_LABEL_WEAK, imported_class_code_medium=data.IMPORTED_CLASS_CODE_MEDIUM, imported_class_label_medium=data.IMPORTED_CLASS_LABEL_MEDIUM, imported_class_code_strong=data.IMPORTED_CLASS_CODE_STRONG, imported_class_label_strong=data.IMPORTED_CLASS_LABEL_STRONG, imported_cpia_rating=self.imported_cpia_rating)

    @cached_property
    def imported_commodity_ids(self) -> data.Series[str | int | float | bool | None]:
        return internals.imported_commodity_ids(imported_commodity_names=data.IMPORTED_COMMODITY_NAMES, imported_of=self.imported_of)

    @cached_property
    def imported_commodity_prices(self) -> data.Series[float | str | None]:
        return internals.imported_commodity_prices(com_as_of_date=data.COM_AS_OF_DATE, com_prices=data.COM_PRICES, com_price_percent_change=data.COM_PRICE_PERCENT_CHANGE, com_price_column_headers=data.COM_PRICE_COLUMN_HEADERS, com_commodity_ids=data.COM_COMMODITY_IDS, com_commodity_names=data.COM_COMMODITY_NAMES, imported_com_latest_actual_header=data.IMPORTED_COM_LATEST_ACTUAL_HEADER, imported_com_p16_header=data.IMPORTED_COM_P16_HEADER, imported_commodity_ids=self.imported_commodity_ids)

    @cached_property
    def imported_eurobond_header(self) -> str | int | float | bool:
        return internals.imported_eurobond_header(trigger_right_headers=data.TRIGGER_RIGHT_HEADERS)

    @cached_property
    def imported_country_imf_codes(self) -> data.Series[int | str | None]:
        return internals.imported_country_imf_codes(lookup_imf_country_code=data.LOOKUP_IMF_COUNTRY_CODE)

    @cached_property
    def imported_country_market_access(self) -> data.Series[str | int | float | bool | None]:
        return internals.imported_country_market_access(country_information_headers=data.COUNTRY_INFORMATION_HEADERS, country_information_ifs_code=data.COUNTRY_INFORMATION_IFS_CODE, country_information_name=data.COUNTRY_INFORMATION_NAME, country_information_eurobond=data.COUNTRY_INFORMATION_EUROBOND, country_information_prgt=data.COUNTRY_INFORMATION_PRGT, imported_prgt_header=data.IMPORTED_PRGT_HEADER, imported_eurobond_header=self.imported_eurobond_header, imported_country_imf_codes=self.imported_country_imf_codes)

    @cached_property
    def imported_country_imf_codes_overflow(self) -> data.Series[int | str | None]:
        return internals.imported_country_imf_codes_overflow()

    @cached_property
    def imported_country_market_access_overflow(self) -> data.Series[str | int | float | bool | None]:
        return internals.imported_country_market_access_overflow(country_information_headers=data.COUNTRY_INFORMATION_HEADERS, country_information_ifs_code=data.COUNTRY_INFORMATION_IFS_CODE, country_information_name=data.COUNTRY_INFORMATION_NAME, country_information_eurobond=data.COUNTRY_INFORMATION_EUROBOND, country_information_prgt=data.COUNTRY_INFORMATION_PRGT, imported_prgt_header=data.IMPORTED_PRGT_HEADER, imported_eurobond_header=self.imported_eurobond_header, imported_country_imf_codes_overflow=self.imported_country_imf_codes_overflow)

    @cached_property
    def imported_prev_dsa_weo_codes(self) -> data.Series[str | int | float | bool | None]:
        return internals.imported_prev_dsa_weo_codes(realism1_prev_dsa_weo_codes=data.REALISM1_PREV_DSA_WEO_CODES, realism1_public_rebased_weo_codes=self.realism1_public_rebased_weo_codes)

    @cached_property
    def imported_prev_dsa_external_2019(self) -> data.Series[float | str | None]:
        return internals.imported_prev_dsa_external_2019(imported_prev_dsa_match_keys=self.imported_prev_dsa_match_keys, imported_prev_dsa_history_year_headers=self.imported_prev_dsa_history_year_headers, imported_prev_dsa_unit_scales=data.IMPORTED_PREV_DSA_UNIT_SCALES, data_all_prev_dsa_field_headers=data.DATA_ALL_PREV_DSA_FIELD_HEADERS, data_all_prev_dsa_year_headers=data.DATA_ALL_PREV_DSA_YEAR_HEADERS, data_all_prev_dsa_series_codes=data.DATA_ALL_PREV_DSA_SERIES_CODES, data_all_prev_dsa_text_attributes=data.DATA_ALL_PREV_DSA_TEXT_ATTRIBUTES, data_all_prev_dsa_imf_country_codes=data.DATA_ALL_PREV_DSA_IMF_COUNTRY_CODES, data_all_prev_dsa_issuance_dates=data.DATA_ALL_PREV_DSA_ISSUANCE_DATES, data_all_prev_dsa_first_projection_years=data.DATA_ALL_PREV_DSA_FIRST_PROJECTION_YEARS, data_all_prev_dsa_observations=data.DATA_ALL_PREV_DSA_OBSERVATIONS)

    @cached_property
    def imported_prev_dsa_external_2024(self) -> data.Series[float | str | None]:
        return internals.imported_prev_dsa_external_2024(imported_prev_dsa_match_keys=self.imported_prev_dsa_match_keys, imported_prev_dsa_history_year_headers=self.imported_prev_dsa_history_year_headers, imported_prev_dsa_unit_scales=data.IMPORTED_PREV_DSA_UNIT_SCALES, data_all_prev_dsa_field_headers=data.DATA_ALL_PREV_DSA_FIELD_HEADERS, data_all_prev_dsa_year_headers=data.DATA_ALL_PREV_DSA_YEAR_HEADERS, data_all_prev_dsa_series_codes=data.DATA_ALL_PREV_DSA_SERIES_CODES, data_all_prev_dsa_text_attributes=data.DATA_ALL_PREV_DSA_TEXT_ATTRIBUTES, data_all_prev_dsa_imf_country_codes=data.DATA_ALL_PREV_DSA_IMF_COUNTRY_CODES, data_all_prev_dsa_issuance_dates=data.DATA_ALL_PREV_DSA_ISSUANCE_DATES, data_all_prev_dsa_first_projection_years=data.DATA_ALL_PREV_DSA_FIRST_PROJECTION_YEARS, data_all_prev_dsa_observations=data.DATA_ALL_PREV_DSA_OBSERVATIONS)

    @cached_property
    def imported_prev_dsa_public_2019(self) -> data.Series[float | str | None]:
        return internals.imported_prev_dsa_public_2019(imported_prev_dsa_match_keys=self.imported_prev_dsa_match_keys, imported_prev_dsa_history_year_headers=self.imported_prev_dsa_history_year_headers, imported_prev_dsa_unit_scales=data.IMPORTED_PREV_DSA_UNIT_SCALES, data_all_prev_dsa_field_headers=data.DATA_ALL_PREV_DSA_FIELD_HEADERS, data_all_prev_dsa_year_headers=data.DATA_ALL_PREV_DSA_YEAR_HEADERS, data_all_prev_dsa_series_codes=data.DATA_ALL_PREV_DSA_SERIES_CODES, data_all_prev_dsa_text_attributes=data.DATA_ALL_PREV_DSA_TEXT_ATTRIBUTES, data_all_prev_dsa_imf_country_codes=data.DATA_ALL_PREV_DSA_IMF_COUNTRY_CODES, data_all_prev_dsa_issuance_dates=data.DATA_ALL_PREV_DSA_ISSUANCE_DATES, data_all_prev_dsa_first_projection_years=data.DATA_ALL_PREV_DSA_FIRST_PROJECTION_YEARS, data_all_prev_dsa_observations=data.DATA_ALL_PREV_DSA_OBSERVATIONS)

    @cached_property
    def imported_prev_dsa_public_2024(self) -> data.Series[float | str | None]:
        return internals.imported_prev_dsa_public_2024(imported_prev_dsa_match_keys=self.imported_prev_dsa_match_keys, imported_prev_dsa_history_year_headers=self.imported_prev_dsa_history_year_headers, imported_prev_dsa_unit_scales=data.IMPORTED_PREV_DSA_UNIT_SCALES, data_all_prev_dsa_field_headers=data.DATA_ALL_PREV_DSA_FIELD_HEADERS, data_all_prev_dsa_year_headers=data.DATA_ALL_PREV_DSA_YEAR_HEADERS, data_all_prev_dsa_series_codes=data.DATA_ALL_PREV_DSA_SERIES_CODES, data_all_prev_dsa_text_attributes=data.DATA_ALL_PREV_DSA_TEXT_ATTRIBUTES, data_all_prev_dsa_imf_country_codes=data.DATA_ALL_PREV_DSA_IMF_COUNTRY_CODES, data_all_prev_dsa_issuance_dates=data.DATA_ALL_PREV_DSA_ISSUANCE_DATES, data_all_prev_dsa_first_projection_years=data.DATA_ALL_PREV_DSA_FIRST_PROJECTION_YEARS, data_all_prev_dsa_observations=data.DATA_ALL_PREV_DSA_OBSERVATIONS)

    @cached_property
    def imported_investment_growth(self) -> data.Series[float | str | None]:
        return internals.imported_investment_growth(imported_fad_capital_stock_indicator=data.IMPORTED_FAD_CAPITAL_STOCK_INDICATOR, imported_prev_dsa_match_keys=self.imported_prev_dsa_match_keys, imported_prev_dsa_investment_year_headers=self.imported_prev_dsa_investment_year_headers, imported_prev_dsa_unit_scales=data.IMPORTED_PREV_DSA_UNIT_SCALES, data_all_prev_dsa_field_headers=data.DATA_ALL_PREV_DSA_FIELD_HEADERS, data_all_prev_dsa_year_headers=data.DATA_ALL_PREV_DSA_YEAR_HEADERS, data_all_prev_dsa_series_codes=data.DATA_ALL_PREV_DSA_SERIES_CODES, data_all_prev_dsa_text_attributes=data.DATA_ALL_PREV_DSA_TEXT_ATTRIBUTES, data_all_prev_dsa_imf_country_codes=data.DATA_ALL_PREV_DSA_IMF_COUNTRY_CODES, data_all_prev_dsa_issuance_dates=data.DATA_ALL_PREV_DSA_ISSUANCE_DATES, data_all_prev_dsa_first_projection_years=data.DATA_ALL_PREV_DSA_FIRST_PROJECTION_YEARS, data_all_prev_dsa_observations=data.DATA_ALL_PREV_DSA_OBSERVATIONS, fad_column_headers=data.FAD_COLUMN_HEADERS, fad_years=data.FAD_YEARS, fad_text_attributes=data.FAD_TEXT_ATTRIBUTES, fad_dsa_template_ids=data.FAD_DSA_TEMPLATE_IDS, fad_numeric_attributes=data.FAD_NUMERIC_ATTRIBUTES, imported_country_code=self.imported_country_code)

    @cached_property
    def imported_cpia_by_year(self) -> data.Series[float | str | None]:
        return internals.imported_cpia_by_year(cpia_column_headers=data.CPIA_COLUMN_HEADERS, cpia_record_fields=data.CPIA_RECORD_FIELDS, cpia_score_by_year=data.CPIA_SCORE_BY_YEAR, imported_country_code=self.imported_country_code, imported_cpia_year_headers=self.imported_cpia_year_headers)

    @cached_property
    def imported_selected_vintage_keys(self) -> data.Series[str | int | float | bool | None]:
        return internals.imported_selected_vintage_keys(imported_country_code=self.imported_country_code)

    @cached_property
    def imported_selected_vintage_dates(self) -> data.Series[str | int | float | bool | None]:
        return internals.imported_selected_vintage_dates(list_dsa_vintage_id=data.LIST_DSA_VINTAGE_ID, list_dsa_vintage_date=data.LIST_DSA_VINTAGE_DATE, list_dsa_field_headers=data.LIST_DSA_FIELD_HEADERS, imported_vintage_date_header=data.IMPORTED_VINTAGE_DATE_HEADER, imported_selected_vintage_keys=self.imported_selected_vintage_keys)

    @cached_property
    def imported_fad_capital_stock_note(self) -> str | int | float | bool:
        return internals.imported_fad_capital_stock_note(realism3_government_capital_actual_label=self.realism3_government_capital_actual_label)

    @cached_property
    def imported_cpia_year_headers(self) -> data.Series[int | str | None]:
        return internals.imported_cpia_year_headers(probability_scenario_years=self.probability_scenario_years)

    @cached_property
    def probability_debt_carrying_capacity_paths(self) -> data.Series[float | str | None]:
        return internals.probability_debt_carrying_capacity_paths(probability_background_macro=self.probability_background_macro)

    @cached_property
    def probability_background_macro(self) -> data.Series[float | str | None]:
        return internals.probability_background_macro(input3_imports=data.INPUT3_IMPORTS, input3_remittances=data.INPUT3_REMITTANCES, input3_world_growth_and_reserves=data.INPUT3_WORLD_GROWTH_AND_RESERVES, input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number=self.input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number, imported_cpia_by_year=self.imported_cpia_by_year, imported_cpia_year_headers=self.imported_cpia_year_headers, imported_cpia_row_label=data.IMPORTED_CPIA_ROW_LABEL, probability_background_years=self.probability_background_years, probability_background_cpia_label=data.PROBABILITY_BACKGROUND_CPIA_LABEL, macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_real_gdp_growth=self.macro_debt_real_gdp_growth)

    @cached_property
    def probability_scenario_years(self) -> data.Series[int | str | None]:
        return internals.probability_scenario_years(macro_debt_data=self.macro_debt_data)

    @cached_property
    def probability_carrying_capacity_years(self) -> data.Series[int | str | None]:
        return internals.probability_carrying_capacity_years(probability_scenario_years=self.probability_scenario_years)

    @cached_property
    def probability_background_years(self) -> data.Series[int | str | None]:
        return internals.probability_background_years(probability_carrying_capacity_years=self.probability_carrying_capacity_years)

    @cached_property
    def realism1_external_current_vintage_projection(self) -> data.Series[float | str | None]:
        return internals.realism1_external_current_vintage_projection(display_scale=data.DISPLAY_SCALE, dsa_ext_external_debt_nominal_1=self.dsa_ext_external_debt_nominal_1, dsa_ext_change_in_external_debt=self.dsa_ext_change_in_external_debt, dsa_ext_net_fdi_negative_inflow=self.dsa_ext_net_fdi_negative_inflow, dsa_ext_contribution_from_nominal_interest_rate=self.dsa_ext_contribution_from_nominal_interest_rate, dsa_ext_contribution_from_real_gdp_growth=self.dsa_ext_contribution_from_real_gdp_growth, dsa_ext_contribution_from_price_and_exchange_rate_changes=self.dsa_ext_contribution_from_price_and_exchange_rate_changes, dsa_ext_residual_3=self.dsa_ext_residual_3, dsa_ext_nominal_gdp_million_of_us_dollars=self.dsa_ext_nominal_gdp_million_of_us_dollars, dsa_ext_deficit_in_balance_of_goods_and_services=self.dsa_ext_deficit_in_balance_of_goods_and_services, dsa_ext_net_current_transfers_negative_inflow=self.dsa_ext_net_current_transfers_negative_inflow, dsa_ext_other_current_account_flows_negative_net_inflow=self.dsa_ext_other_current_account_flows_negative_net_inflow, dsa_ext_of_which_public_and_publicly_guaranteed_ppg=self.dsa_ext_of_which_public_and_publicly_guaranteed_ppg, baseline_ext_historical_indicators=self.baseline_ext_historical_indicators, baseline_ext_year_before_projection=self.baseline_ext_year_before_projection, lookup_country_scale_phrase=self.lookup_country_scale_phrase)

    @cached_property
    def realism1_external_five_years_ago_projection(self) -> data.Series[float | str | None]:
        return internals.realism1_external_five_years_ago_projection(imported_prev_dsa_external_2019=self.imported_prev_dsa_external_2019)

    @cached_property
    def _scan_realism1_external_five_years_ago_rebased_projection(self) -> internals.ScanRealism1ExternalFiveYearsAgoRebasedProjectionResult:
        return internals.scan_realism1_external_five_years_ago_rebased_projection(realism1_external_current_vintage_projection=self.realism1_external_current_vintage_projection, realism1_external_five_years_ago_projection=self.realism1_external_five_years_ago_projection)

    @cached_property
    def realism1_external_five_years_ago_rebased_projection(self) -> data.Series[float | str | None]:
        return self._scan_realism1_external_five_years_ago_rebased_projection.realism1_external_five_years_ago_rebased_projection

    @cached_property
    def realism1_external_usd_rebase_factors(self) -> data.Series[float | str | None]:
        return self._scan_realism1_external_five_years_ago_rebased_projection.realism1_external_usd_rebase_factors

    @cached_property
    def realism1_external_last_vintage_projection(self) -> data.Series[float | str | None]:
        return internals.realism1_external_last_vintage_projection(imported_prev_dsa_external_2024=self.imported_prev_dsa_external_2024)

    @cached_property
    def _scan_realism1_external_last_vintage_rebased_projection(self) -> internals.ScanRealism1ExternalLastVintageRebasedProjectionResult:
        return internals.scan_realism1_external_last_vintage_rebased_projection(realism1_external_current_vintage_projection=self.realism1_external_current_vintage_projection, realism1_external_last_vintage_projection=self.realism1_external_last_vintage_projection)

    @cached_property
    def realism1_external_last_vintage_rebased_projection(self) -> data.Series[float | str | None]:
        return self._scan_realism1_external_last_vintage_rebased_projection.realism1_external_last_vintage_rebased_projection

    @cached_property
    def realism1_external_last_vintage_usd_rebase_factors(self) -> data.Series[float | str | None]:
        return self._scan_realism1_external_last_vintage_rebased_projection.realism1_external_last_vintage_usd_rebase_factors

    @cached_property
    def realism1_public_current_vintage_projection(self) -> data.Series[float | str | None]:
        return internals.realism1_public_current_vintage_projection(display_scale=data.DISPLAY_SCALE, baseline_pub_historical_indicators=self.baseline_pub_historical_indicators, baseline_pub_year_before_projection=self.baseline_pub_year_before_projection, baseline_pub_public_sector_debt=self.baseline_pub_public_sector_debt, baseline_pub_change_in_public_sector_debt=self.baseline_pub_change_in_public_sector_debt, baseline_pub_primary_deficit=self.baseline_pub_primary_deficit, baseline_pub_of_which_contribution_from_average_real=self.baseline_pub_of_which_contribution_from_average_real, baseline_pub_of_which_contribution_from_real_gdp_growth=self.baseline_pub_of_which_contribution_from_real_gdp_growth, baseline_pub_contribution_from_real_exchange_rate=self.baseline_pub_contribution_from_real_exchange_rate, baseline_pub_other_identified_debt_creating_flows=self.baseline_pub_other_identified_debt_creating_flows, baseline_pub_residual=self.baseline_pub_residual, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, lookup_country_scale_phrase=self.lookup_country_scale_phrase)

    @cached_property
    def realism1_public_five_years_ago_projection(self) -> data.Series[float | str | None]:
        return internals.realism1_public_five_years_ago_projection(imported_prev_dsa_public_2019=self.imported_prev_dsa_public_2019)

    @cached_property
    def _scan_realism1_public_five_years_ago_rebased_projection(self) -> internals.ScanRealism1PublicFiveYearsAgoRebasedProjectionResult:
        return internals.scan_realism1_public_five_years_ago_rebased_projection(realism1_public_current_vintage_projection=self.realism1_public_current_vintage_projection, realism1_public_five_years_ago_projection=self.realism1_public_five_years_ago_projection)

    @cached_property
    def realism1_public_five_years_ago_rebased_projection(self) -> data.Series[float | str | None]:
        return self._scan_realism1_public_five_years_ago_rebased_projection.realism1_public_five_years_ago_rebased_projection

    @cached_property
    def realism1_public_lc_rebase_factors(self) -> data.Series[float | str | None]:
        return self._scan_realism1_public_five_years_ago_rebased_projection.realism1_public_lc_rebase_factors

    @cached_property
    def realism1_public_last_vintage_projection(self) -> data.Series[float | str | None]:
        return internals.realism1_public_last_vintage_projection(imported_prev_dsa_public_2024=self.imported_prev_dsa_public_2024)

    @cached_property
    def _scan_realism1_public_last_vintage_lc_rebase_factors(self) -> internals.ScanRealism1PublicLastVintageLcRebaseFactorsResult:
        return internals.scan_realism1_public_last_vintage_lc_rebase_factors(realism1_public_current_vintage_projection=self.realism1_public_current_vintage_projection, realism1_public_last_vintage_projection=self.realism1_public_last_vintage_projection)

    @cached_property
    def realism1_public_last_vintage_lc_rebase_factors(self) -> data.Series[float | str | None]:
        return self._scan_realism1_public_last_vintage_lc_rebase_factors.realism1_public_last_vintage_lc_rebase_factors

    @cached_property
    def realism1_public_last_vintage_stock_copies(self) -> data.Series[float | str | None]:
        return self._scan_realism1_public_last_vintage_lc_rebase_factors.realism1_public_last_vintage_stock_copies

    @cached_property
    def realism3_real_growth_by_vintage(self) -> data.Series[float | str | None]:
        return internals.realism3_real_growth_by_vintage(dsa_ext_real_gdp_growth_in_percent=self.dsa_ext_real_gdp_growth_in_percent, imported_investment_growth=self.imported_investment_growth)

    @cached_property
    def realism3_public_investment_ratio_by_vintage(self) -> data.Series[float | str | None]:
        return internals.realism3_public_investment_ratio_by_vintage(macro_debt_gdp_constant_prices=self.macro_debt_gdp_constant_prices, imported_investment_growth=self.imported_investment_growth, macro_debt_previous_vintage_investment=self.macro_debt_previous_vintage_investment)

    @cached_property
    def realism3_private_investment_ratio_by_vintage(self) -> data.Series[float | str | None]:
        return internals.realism3_private_investment_ratio_by_vintage(macro_debt_gdp_constant_prices=self.macro_debt_gdp_constant_prices, imported_investment_growth=self.imported_investment_growth, macro_debt_previous_vintage_investment=self.macro_debt_previous_vintage_investment)

    @cached_property
    def realism3_baseline_real_gdp_index_by_vintage(self) -> data.Series[float | str | None]:
        return internals.realism3_baseline_real_gdp_index_by_vintage(realism3_real_growth_by_vintage=self.realism3_real_growth_by_vintage)

    @cached_property
    def realism3_government_capital_actual(self) -> data.Series[float | str | None]:
        return internals.realism3_government_capital_actual(imported_prev_dsa_match_keys=self.imported_prev_dsa_match_keys, imported_prev_dsa_investment_year_headers=self.imported_prev_dsa_investment_year_headers, imported_investment_growth=self.imported_investment_growth, imported_fad_capital_stock_note=self.imported_fad_capital_stock_note, realism3_baseline_real_gdp_index_by_vintage=self.realism3_baseline_real_gdp_index_by_vintage, realism3_contribution_years=self.realism3_contribution_years, realism3_government_capital_actual_label=self.realism3_government_capital_actual_label)

    @cached_property
    def realism3_government_capital_projected_by_vintage(self) -> data.Series[float | str | None]:
        return internals.realism3_government_capital_projected_by_vintage(imported_fad_capital_stock_year=data.IMPORTED_FAD_CAPITAL_STOCK_YEAR, realism3_public_investment_ratio_by_vintage=self.realism3_public_investment_ratio_by_vintage, realism3_baseline_real_gdp_index_by_vintage=self.realism3_baseline_real_gdp_index_by_vintage, realism3_government_capital_actual=self.realism3_government_capital_actual, realism3_current_vintage_year=self.realism3_current_vintage_year, realism3_latest_vintage_year=self.realism3_latest_vintage_year, realism3_depreciation_rate=data.REALISM3_DEPRECIATION_RATE, realism3_efficiency_public=data.REALISM3_EFFICIENCY_PUBLIC, realism3_efficiency_private=data.REALISM3_EFFICIENCY_PRIVATE, realism3_contribution_years=self.realism3_contribution_years)

    @cached_property
    def baseline_pub_historical_indicators(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_historical_indicators(baseline_pub_primary_deficit=self.baseline_pub_primary_deficit, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, baseline_pub_real_gdp_growth=self.baseline_pub_real_gdp_growth, baseline_pub_inflation_rate_gdp_deflator_pct=self.baseline_pub_inflation_rate_gdp_deflator_pct, macro_debt_privatization_receipts=self.macro_debt_privatization_receipts, macro_debt_public_sector_interest_expenditure=self.macro_debt_public_sector_interest_expenditure, macro_debt_recognition_of_contingent_liab_e_g_bank=self.macro_debt_recognition_of_contingent_liab_e_g_bank, macro_debt_other_debt_creating_reducing_flow_please_specify=self.macro_debt_other_debt_creating_reducing_flow_please_specify, macro_debt_debt_relief=self.macro_debt_debt_relief, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar, macro_debt_total_public_debt_outstanding_year_end=self.macro_debt_total_public_debt_outstanding_year_end, macro_debt_fx_denominated_public_debt_end_of_period=self.macro_debt_fx_denominated_public_debt_end_of_period, macro_debt_interest_rate_ext_debt=self.macro_debt_interest_rate_ext_debt, macro_debt_interest_rate_domestic_debt=self.macro_debt_interest_rate_domestic_debt, macro_debt_us_gdp_deflator_percent_change=self.macro_debt_us_gdp_deflator_percent_change)

    @cached_property
    def baseline_ext_historical_indicators(self) -> data.Series[float | str | None]:
        return internals.baseline_ext_historical_indicators(dsa_ext_external_debt_nominal_1=self.dsa_ext_external_debt_nominal_1, dsa_ext_non_interest_current_account_deficit=self.dsa_ext_non_interest_current_account_deficit, dsa_ext_exports=self.dsa_ext_exports, dsa_ext_net_fdi_negative_inflow=self.dsa_ext_net_fdi_negative_inflow, dsa_ext_nominal_gdp_million_of_us_dollars=self.dsa_ext_nominal_gdp_million_of_us_dollars, dsa_ext_real_gdp_growth_in_percent=self.dsa_ext_real_gdp_growth_in_percent, dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent=self.dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent, dsa_ext_net_current_transfers_negative_inflow=self.dsa_ext_net_current_transfers_negative_inflow, macro_debt_total_ext_debt_interest_due_include_interest=self.macro_debt_total_ext_debt_interest_due_include_interest, macro_debt_exports_of_goods_services=self.macro_debt_exports_of_goods_services, macro_debt_imports_of_goods_services_use_positive_values=self.macro_debt_imports_of_goods_services_use_positive_values, macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc, macro_debt_private_debt_pct_gdp=self.macro_debt_private_debt_pct_gdp, macro_debt_total_public_ext_debt=self.macro_debt_total_public_ext_debt, macro_debt_share_of_local_currency_denominated_external=self.macro_debt_share_of_local_currency_denominated_external, macro_debt_depreciation_of_nc_depreciation=self.macro_debt_depreciation_of_nc_depreciation)

    @cached_property
    def baseline_pub_year_before_projection(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_year_before_projection(baseline_pub_historical_indicators=self.baseline_pub_historical_indicators, baseline_pub_public_sector_debt=self.baseline_pub_public_sector_debt, baseline_pub_primary_deficit=self.baseline_pub_primary_deficit, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, baseline_pub_real_gdp_growth=self.baseline_pub_real_gdp_growth, baseline_pub_exchange_rate_lc_per_us_dollar=self.baseline_pub_exchange_rate_lc_per_us_dollar, baseline_pub_inflation_rate_gdp_deflator_pct=self.baseline_pub_inflation_rate_gdp_deflator_pct, macro_debt_privatization_receipts=self.macro_debt_privatization_receipts, macro_debt_public_sector_interest_expenditure=self.macro_debt_public_sector_interest_expenditure, macro_debt_recognition_of_contingent_liab_e_g_bank=self.macro_debt_recognition_of_contingent_liab_e_g_bank, macro_debt_other_debt_creating_reducing_flow_please_specify=self.macro_debt_other_debt_creating_reducing_flow_please_specify, macro_debt_debt_relief=self.macro_debt_debt_relief, macro_debt_total_public_debt_outstanding_year_end=self.macro_debt_total_public_debt_outstanding_year_end, macro_debt_interest_rate_ext_debt=self.macro_debt_interest_rate_ext_debt, macro_debt_interest_rate_domestic_debt=self.macro_debt_interest_rate_domestic_debt, macro_debt_us_gdp_deflator_percent_change=self.macro_debt_us_gdp_deflator_percent_change)

    @cached_property
    def baseline_ext_year_before_projection(self) -> data.Series[float | str | None]:
        return internals.baseline_ext_year_before_projection(dsa_ext_external_debt_nominal_1=self.dsa_ext_external_debt_nominal_1, dsa_ext_non_interest_current_account_deficit=self.dsa_ext_non_interest_current_account_deficit, dsa_ext_exports=self.dsa_ext_exports, dsa_ext_net_fdi_negative_inflow=self.dsa_ext_net_fdi_negative_inflow, dsa_ext_nominal_gdp_million_of_us_dollars=self.dsa_ext_nominal_gdp_million_of_us_dollars, dsa_ext_real_gdp_growth_in_percent=self.dsa_ext_real_gdp_growth_in_percent, dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent=self.dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent, dsa_ext_net_current_transfers_negative_inflow=self.dsa_ext_net_current_transfers_negative_inflow, baseline_ext_historical_indicators=self.baseline_ext_historical_indicators, macro_debt_total_ext_debt_interest_due_include_interest=self.macro_debt_total_ext_debt_interest_due_include_interest, macro_debt_imports_of_goods_services_use_positive_values=self.macro_debt_imports_of_goods_services_use_positive_values, macro_debt_depreciation_of_nc_depreciation=self.macro_debt_depreciation_of_nc_depreciation)

    @cached_property
    def realism1_current_vintage_year(self) -> int | str:
        return internals.realism1_current_vintage_year(current_year=self.current_year)

    @cached_property
    def realism1_latest_vintage_year(self) -> int | str:
        return internals.realism1_latest_vintage_year(realism1_latest_vintage_date=self.realism1_latest_vintage_date)

    @cached_property
    def realism1_latest_vintage_date(self) -> str | int | float | bool:
        return internals.realism1_latest_vintage_date(imported_selected_vintage_dates=self.imported_selected_vintage_dates)

    @cached_property
    def realism1_external_year_headers(self) -> data.Series[int | str | None]:
        return internals.realism1_external_year_headers(output_submit_first_projection_year=self.output_submit_first_projection_year)

    @cached_property
    def realism1_public_year_headers(self) -> data.Series[int | str | None]:
        return internals.realism1_public_year_headers(realism1_current_vintage_year=self.realism1_current_vintage_year)

    @cached_property
    def realism1_public_rebased_weo_codes(self) -> data.Series[str | int | float | bool | None]:
        return internals.realism1_public_rebased_weo_codes(realism1_public_current_vintage_weo_codes=data.REALISM1_PUBLIC_CURRENT_VINTAGE_WEO_CODES)

    @cached_property
    def realism1_external_forecast_error_component_names(self) -> data.Series[str | int | float | bool | None]:
        return internals.realism1_external_forecast_error_component_names(realism1_external_debt_flow_components=self.realism1_external_debt_flow_components)

    @cached_property
    def realism1_external_five_year_flow_changes(self) -> data.Series[float | str | None]:
        return internals.realism1_external_five_year_flow_changes(realism1_external_five_years_ago_rebased_projection=self.realism1_external_five_years_ago_rebased_projection, realism1_external_private_debt_rebased_change=self.realism1_external_private_debt_rebased_change, realism1_external_debt_creating_flows=self.realism1_external_debt_creating_flows)

    @cached_property
    def realism1_public_forecast_error_component_names(self) -> data.Series[str | int | float | bool | None]:
        return internals.realism1_public_forecast_error_component_names(realism1_public_debt_flow_components=self.realism1_public_debt_flow_components)

    @cached_property
    def realism1_public_five_year_flow_changes(self) -> data.Series[float | str | None]:
        return internals.realism1_public_five_year_flow_changes(realism1_public_five_years_ago_rebased_projection=self.realism1_public_five_years_ago_rebased_projection, realism1_public_debt_creating_flows=self.realism1_public_debt_creating_flows)

    @cached_property
    def realism1_external_median_label(self) -> str | int | float | bool:
        return internals.realism1_external_median_label(translation_debt_change_phrases=data.TRANSLATION_DEBT_CHANGE_PHRASES, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def realism1_external_projected_change_callouts(self) -> data.Series[float | str | None]:
        return internals.realism1_external_projected_change_callouts(realism1_external_five_year_flow_changes=self.realism1_external_five_year_flow_changes)

    @cached_property
    def realism1_public_projected_change_callouts(self) -> data.Series[float | str | None]:
        return internals.realism1_public_projected_change_callouts(realism1_public_five_year_flow_changes=self.realism1_public_five_year_flow_changes)

    @cached_property
    def realism1_public_projected_change_callout_labels(self) -> data.Series[str | int | float | bool | None]:
        return internals.realism1_public_projected_change_callout_labels(realism1_public_forecast_error_component_names=self.realism1_public_forecast_error_component_names, realism1_external_median_label=self.realism1_external_median_label)

    @cached_property
    def realism1_external_private_debt_rebased_change(self) -> data.Series[float | str | None]:
        return internals.realism1_external_private_debt_rebased_change(realism1_external_five_years_ago_rebased_projection=self.realism1_external_five_years_ago_rebased_projection, realism1_external_last_vintage_usd_rebase_factors=self.realism1_external_last_vintage_usd_rebase_factors)

    @cached_property
    def realism2_history_years(self) -> data.Series[int | str | None]:
        return internals.realism2_history_years(input3_projection_year_header=self.input3_projection_year_header)

    @cached_property
    def realism2_primary_balance(self) -> data.Series[float | str | None]:
        return internals.realism2_primary_balance(macro_debt_public_sector_revenues_including_grants=self.macro_debt_public_sector_revenues_including_grants, macro_debt_public_sector_primary_expenditure=self.macro_debt_public_sector_primary_expenditure, macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def realism2_fiscal_adjustment(self) -> data.Series[float | str | None]:
        return internals.realism2_fiscal_adjustment(realism2_primary_balance=self.realism2_primary_balance)

    @cached_property
    def realism2_real_gdp_growth(self) -> data.Series[float | str | None]:
        return internals.realism2_real_gdp_growth(macro_debt_real_gdp_growth=self.macro_debt_real_gdp_growth)

    @cached_property
    def realism2_persistence_values(self) -> data.Series[float | str | None]:
        return internals.realism2_persistence_values()

    @cached_property
    def realism2_shock_year_index(self) -> data.Series[float | str | None]:
        return internals.realism2_shock_year_index()

    @cached_property
    def realism2_growth_shock(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_shock(realism2_multiplier_values=data.REALISM2_MULTIPLIER_VALUES, realism2_persistence_values=self.realism2_persistence_values, realism2_shock_year_index=self.realism2_shock_year_index)

    @cached_property
    def realism2_adjustment_size(self) -> data.Series[float | str | None]:
        return internals.realism2_adjustment_size(realism2_fiscal_adjustment=self.realism2_fiscal_adjustment)

    @cached_property
    def realism2_growth_impact_multiplier_0_2(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_impact_multiplier_0_2(realism2_growth_shock=self.realism2_growth_shock, realism2_adjustment_size=self.realism2_adjustment_size)

    @cached_property
    def realism2_growth_impact_multiplier_0_2_cumulative(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_impact_multiplier_0_2_cumulative(realism2_growth_impact_multiplier_0_2=self.realism2_growth_impact_multiplier_0_2)

    @cached_property
    def realism2_growth_impact_multiplier_0_4(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_impact_multiplier_0_4(realism2_growth_shock=self.realism2_growth_shock, realism2_adjustment_size=self.realism2_adjustment_size)

    @cached_property
    def realism2_growth_impact_multiplier_0_4_cumulative(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_impact_multiplier_0_4_cumulative(realism2_growth_impact_multiplier_0_4=self.realism2_growth_impact_multiplier_0_4)

    @cached_property
    def realism2_growth_impact_multiplier_0_6(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_impact_multiplier_0_6(realism2_growth_shock=self.realism2_growth_shock, realism2_adjustment_size=self.realism2_adjustment_size)

    @cached_property
    def realism2_growth_impact_multiplier_0_6_cumulative(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_impact_multiplier_0_6_cumulative(realism2_growth_impact_multiplier_0_6=self.realism2_growth_impact_multiplier_0_6)

    @cached_property
    def realism2_growth_impact_multiplier_0_8(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_impact_multiplier_0_8(realism2_growth_shock=self.realism2_growth_shock, realism2_adjustment_size=self.realism2_adjustment_size)

    @cached_property
    def realism2_growth_impact_multiplier_0_8_cumulative(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_impact_multiplier_0_8_cumulative(realism2_growth_impact_multiplier_0_8=self.realism2_growth_impact_multiplier_0_8)

    @cached_property
    def realism2_growth_impact_multiplier_1_0(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_impact_multiplier_1_0(realism2_growth_shock=self.realism2_growth_shock, realism2_adjustment_size=self.realism2_adjustment_size)

    @cached_property
    def realism2_growth_impact_multiplier_1_0_cumulative(self) -> data.Series[float | str | None]:
        return internals.realism2_growth_impact_multiplier_1_0_cumulative(realism2_growth_impact_multiplier_1_0=self.realism2_growth_impact_multiplier_1_0)

    @cached_property
    def realism3_current_vintage_year(self) -> int | str:
        return internals.realism3_current_vintage_year(realism1_current_vintage_year=self.realism1_current_vintage_year)

    @cached_property
    def realism3_latest_vintage_year(self) -> int | str:
        return internals.realism3_latest_vintage_year(realism1_latest_vintage_year=self.realism1_latest_vintage_year)

    @cached_property
    def realism3_first_projection_year(self) -> int | str:
        return internals.realism3_first_projection_year(output_submit_first_projection_year=self.output_submit_first_projection_year)

    @cached_property
    def realism3_contribution_years(self) -> data.Series[int | str | None]:
        return internals.realism3_contribution_years(realism3_first_projection_year=self.realism3_first_projection_year)

    @cached_property
    def realism3_growth_contributions(self) -> data.Series[float | str | None]:
        return internals.realism3_growth_contributions(realism3_capital_growth_contribution=self.realism3_capital_growth_contribution, realism3_growth_residual=self.realism3_growth_residual)

    @cached_property
    def realism3_government_capital_actual_label(self) -> str | int | float | bool:
        return internals.realism3_government_capital_actual_label(imported_fad_capital_stock_year=data.IMPORTED_FAD_CAPITAL_STOCK_YEAR)

    @cached_property
    def realism3_government_capital_growth(self) -> data.Series[float | str | None]:
        return internals.realism3_government_capital_growth(realism3_government_capital_projected_by_vintage=self.realism3_government_capital_projected_by_vintage)

    @cached_property
    def realism3_capital_growth_contribution(self) -> data.Series[float | str | None]:
        return internals.realism3_capital_growth_contribution(realism3_output_elasticity=data.REALISM3_OUTPUT_ELASTICITY, realism3_government_capital_growth=self.realism3_government_capital_growth)

    @cached_property
    def realism3_growth_residual(self) -> data.Series[float | str | None]:
        return internals.realism3_growth_residual(realism3_real_growth_by_vintage=self.realism3_real_growth_by_vintage, realism3_capital_growth_contribution=self.realism3_capital_growth_contribution)

    @cached_property
    def realism4_primary_deficit(self) -> data.Series[float | str | None]:
        return internals.realism4_primary_deficit(baseline_pub_primary_deficit=self.baseline_pub_primary_deficit)

    @cached_property
    def realism4_three_year_adjustment(self) -> data.Series[float | str | None]:
        return internals.realism4_three_year_adjustment(realism4_primary_deficit=self.realism4_primary_deficit)

    @cached_property
    def in8_sdr_sdr_interest(self) -> data.Series[int | str | None]:
        return internals.in8_sdr_sdr_interest(in8_sdr_sdr_allocation_holdings_in_million_of_usd=self.in8_sdr_sdr_allocation_holdings_in_million_of_usd, discount_rate=self.discount_rate, input8_sdr_interest_historical=self.input8_sdr_interest_historical, input8_sdr_interest=self.input8_sdr_interest, input8_sdr_interest_rate=self.input8_sdr_interest_rate)

    @cached_property
    def in8_sdr_of_end_2044(self) -> int | str:
        return internals.in8_sdr_of_end_2044(discount_rate=self.discount_rate, input8_sdr_interest_rate=self.input8_sdr_interest_rate, in8_sdr_sdr_allocation_holdings_in_million_of_usd=self.in8_sdr_sdr_allocation_holdings_in_million_of_usd)

    @cached_property
    def c4_mkt_fin_nominal_gdp(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_nominal_gdp(c4_market_path_nominal_gdp=self.c4_market_path_nominal_gdp, c4_mkt_fin_gdp_deflator=self.c4_mkt_fin_gdp_deflator, c4_market_path_real_gdp_growth=self.c4_market_path_real_gdp_growth)

    @cached_property
    def c4_mkt_fin_gdp_deflator(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_gdp_deflator(dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent=self.dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent, c4_mkt_fin_nc_depreciation=self.c4_mkt_fin_nc_depreciation, c4_mkt_fin_historical_flag=self.c4_mkt_fin_historical_flag, c4_market_path_non_interest_ca_pct_gdp=self.c4_market_path_non_interest_ca_pct_gdp)

    @cached_property
    def c4_mkt_fin_nc_depreciation(self) -> float | str:
        return internals.c4_mkt_fin_nc_depreciation(c4_mkt_fin_i_macro_indicators=self.c4_mkt_fin_i_macro_indicators, dsa_ext_depreciation_of_nc_depreciation=self.dsa_ext_depreciation_of_nc_depreciation)

    @cached_property
    def c4_mkt_fin_historical_flag(self) -> float | str:
        return internals.c4_mkt_fin_historical_flag(ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external)

    @cached_property
    def c4_mkt_fin_stressed_lending_terms(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_stressed_lending_terms(c4_market_instruments=self.c4_market_instruments, c4_mkt_fin_net_non_debt_creating_flows_fdi_gdp_ratio_by_row=self.c4_mkt_fin_net_non_debt_creating_flows_fdi_gdp_ratio_by_row)

    @cached_property
    def c4_mkt_fin_average_residual_terms(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_average_residual_terms(c4_mkt_fin_stressed_lending_terms=self.c4_mkt_fin_stressed_lending_terms, c4_mkt_fin_total_commercial_borrowing_total=self.c4_mkt_fin_total_commercial_borrowing_total, c4_mkt_fin_new_borrowing_total=self.c4_mkt_fin_new_borrowing_total)

    @cached_property
    def c4_mkt_fin_average_residual_interest(self) -> float | str:
        return internals.c4_mkt_fin_average_residual_interest(c4_mkt_fin_total_commercial_borrowing_total=self.c4_mkt_fin_total_commercial_borrowing_total, c4_mkt_fin_new_borrowing_total=self.c4_mkt_fin_new_borrowing_total, c4_market_instruments_k=self.c4_market_instruments_k)

    @cached_property
    def c4_mkt_fin_total_commercial_borrowing(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_total_commercial_borrowing(c4_mkt_fin_new_borrowing=self.c4_mkt_fin_new_borrowing)

    @cached_property
    def c4_mkt_fin_total_commercial_borrowing_total(self) -> float | str:
        return internals.c4_mkt_fin_total_commercial_borrowing_total(c4_mkt_fin_total_commercial_borrowing=self.c4_mkt_fin_total_commercial_borrowing)

    @cached_property
    def c4_mkt_fin_new_borrowing(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_new_borrowing(ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external)

    @cached_property
    def c4_mkt_fin_new_borrowing_total(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_new_borrowing_total(c4_mkt_fin_new_borrowing=self.c4_mkt_fin_new_borrowing)

    @cached_property
    def c4_mkt_fin_gfn_increase(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_gfn_increase(c4_market_path_total_debt_service=self.c4_market_path_total_debt_service, c4_market_path_total_debt_service_alt=self.c4_market_path_total_debt_service_alt)

    @cached_property
    def c4_mkt_fin_pv_residual_financing(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_pv_residual_financing(pv_stress_pv_of_new_forex_debt=self.pv_stress_pv_of_new_forex_debt)

    @cached_property
    def c4_mkt_fin_pv_debt_adjustments(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_pv_debt_adjustments(c4_mkt_fin_pv_residual_financing=self.c4_mkt_fin_pv_residual_financing, c4_market_path_pv_of_debt=self.c4_market_path_pv_of_debt, c4_market_path_pv_of_debt_alt=self.c4_market_path_pv_of_debt_alt)

    @cached_property
    def c4_mkt_fin_revised_pv_debt(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_revised_pv_debt(c4_market_path_baseline_pv_of_debt=self.c4_market_path_baseline_pv_of_debt, c4_mkt_fin_pv_debt_adjustments=self.c4_mkt_fin_pv_debt_adjustments)

    @cached_property
    def c4_mkt_fin_revised_pv_debt_pct_gdp(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_revised_pv_debt_pct_gdp(c4_market_path_nominal_gdp_stress=self.c4_market_path_nominal_gdp_stress, c4_mkt_fin_revised_pv_debt=self.c4_mkt_fin_revised_pv_debt)

    @cached_property
    def c4_mkt_fin_baseline_debt_service(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_baseline_debt_service(macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6)

    @cached_property
    def c4_mkt_fin_debt_service_adjustment(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_debt_service_adjustment(c4_market_path_total_debt_service=self.c4_market_path_total_debt_service, c4_market_path_total_debt_service_alt=self.c4_market_path_total_debt_service_alt, pv_stress_total_debt_service=self.pv_stress_total_debt_service)

    @cached_property
    def c4_mkt_fin_adjusted_debt_service(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_adjusted_debt_service(c4_mkt_fin_baseline_debt_service=self.c4_mkt_fin_baseline_debt_service, c4_mkt_fin_debt_service_adjustment=self.c4_mkt_fin_debt_service_adjustment)

    @cached_property
    def c4_mkt_fin_revenue_ex_grants(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_revenue_ex_grants(dsa_ext_nominal_gdp_million_of_us_dollars=self.dsa_ext_nominal_gdp_million_of_us_dollars, dsa_ext_government_revenues_excluding_grants_in_percent_of_gdp=self.dsa_ext_government_revenues_excluding_grants_in_percent_of_gdp)

    @cached_property
    def c4_mkt_fin_revised_pv_debt_to_exports(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_revised_pv_debt_to_exports(c4_mkt_fin_pv_debt_adjustments=self.c4_mkt_fin_pv_debt_adjustments, c4_market_path_baseline_pv_of_debt=self.c4_market_path_baseline_pv_of_debt, c4_market_path_exports=self.c4_market_path_exports)

    @cached_property
    def c4_mkt_fin_dsr_exports_stress(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_dsr_exports_stress(c4_market_path_exports=self.c4_market_path_exports, c4_mkt_fin_adjusted_debt_service=self.c4_mkt_fin_adjusted_debt_service)

    @cached_property
    def c4_mkt_fin_dsr_revenue_stress(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_dsr_revenue_stress(c4_mkt_fin_adjusted_debt_service=self.c4_mkt_fin_adjusted_debt_service, c4_mkt_fin_revenue_ex_grants=self.c4_mkt_fin_revenue_ex_grants)

    @cached_property
    def ci_summary_debt_carrying_capacity(self) -> str | int | float | bool:
        return internals.ci_summary_debt_carrying_capacity(lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, ci_summary_performance_policy=self.ci_summary_performance_policy, ci_summary_debt_carrying_capacity_vintage_reconciled=self.ci_summary_debt_carrying_capacity_vintage_reconciled)

    @cached_property
    def ci_summary_external_thresholds_heading(self) -> str | int | float | bool:
        return internals.ci_summary_external_thresholds_heading(start_debt_sustainability_analysis=self.start_debt_sustainability_analysis, translation_input_2_debt_coverage_external_debt_burden_thresholds=data.TRANSLATION_INPUT_2_DEBT_COVERAGE_EXTERNAL_DEBT_BURDEN_THRESHOLDS)

    @cached_property
    def ci_summary_public_benchmark_heading(self) -> str | int | float | bool:
        return internals.ci_summary_public_benchmark_heading(start_debt_sustainability_analysis=self.start_debt_sustainability_analysis, translation_input_2_debt_coverage_total_public_debt_benchmark=data.TRANSLATION_INPUT_2_DEBT_COVERAGE_TOTAL_PUBLIC_DEBT_BENCHMARK)

    @cached_property
    def ci_summary_pv_of_debt_heading(self) -> str | int | float | bool:
        return internals.ci_summary_pv_of_debt_heading(start_debt_sustainability_analysis=self.start_debt_sustainability_analysis, translation_input_2_debt_coverage_pv_of_debt_in_of=data.TRANSLATION_INPUT_2_DEBT_COVERAGE_PV_OF_DEBT_IN_OF)

    @cached_property
    def ci_summary_public_pv_heading(self) -> str | int | float | bool:
        return internals.ci_summary_public_pv_heading(start_debt_sustainability_analysis=self.start_debt_sustainability_analysis, translation_input_2_debt_coverage_pv_of_total_public_debt_in_percent_of_gdp=data.TRANSLATION_INPUT_2_DEBT_COVERAGE_PV_OF_TOTAL_PUBLIC_DEBT_IN_PERCENT_OF_GDP)

    @cached_property
    def ci_summary_pv_exports_heading(self) -> str | int | float | bool:
        return internals.ci_summary_pv_exports_heading(start_debt_sustainability_analysis=self.start_debt_sustainability_analysis, translation_input_2_debt_coverage_exports_pv_of_debt_in_of=data.TRANSLATION_INPUT_2_DEBT_COVERAGE_EXPORTS_PV_OF_DEBT_IN_OF)

    @cached_property
    def ci_summary_pv_gdp_heading(self) -> str | int | float | bool:
        return internals.ci_summary_pv_gdp_heading(start_debt_sustainability_analysis=self.start_debt_sustainability_analysis, translation_input_2_debt_coverage_gdp=data.TRANSLATION_INPUT_2_DEBT_COVERAGE_GDP)

    @cached_property
    def ci_summary_ds_exports_heading(self) -> str | int | float | bool:
        return internals.ci_summary_ds_exports_heading(start_debt_sustainability_analysis=self.start_debt_sustainability_analysis, translation_input_2_debt_coverage_exports_debt_service_in_of=data.TRANSLATION_INPUT_2_DEBT_COVERAGE_EXPORTS_DEBT_SERVICE_IN_OF)

    @cached_property
    def ci_summary_ds_revenue_heading(self) -> str | int | float | bool:
        return internals.ci_summary_ds_revenue_heading(start_debt_sustainability_analysis=self.start_debt_sustainability_analysis, translation_input_2_debt_coverage_revenue=data.TRANSLATION_INPUT_2_DEBT_COVERAGE_REVENUE)

    @cached_property
    def ci_summary_public_pv_medium_cutoff(self) -> float | str:
        return internals.ci_summary_public_pv_medium_cutoff(lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, ci_pub_pv_debt_gdp_new=data.CI_PUB_PV_DEBT_GDP_NEW, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, ci_summary_debt_carrying_capacity=self.ci_summary_debt_carrying_capacity, ci_summary_public_pv_heading=self.ci_summary_public_pv_heading, ci_summary_cpia_rating=self.ci_summary_cpia_rating, ci_summary_public_benchmark_grid_heading=self.ci_summary_public_benchmark_grid_heading, ci_summary_public_pv_grid_heading=self.ci_summary_public_pv_grid_heading, ci_summary_public_capacity_class_headers=self.ci_summary_public_capacity_class_headers)

    @cached_property
    def ci_summary_pv_exports_applicable(self) -> float | str:
        return internals.ci_summary_pv_exports_applicable(ci_summary_old_policy_exports_threshold=self.ci_summary_old_policy_exports_threshold, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, ci_class_labels_thresholds=data.CI_CLASS_LABELS_THRESHOLDS, ci_ext_pv_debt_exports=data.CI_EXT_PV_DEBT_EXPORTS, ci_ext_pv_debt_gdp=data.CI_EXT_PV_DEBT_GDP, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, ci_summary_debt_carrying_capacity=self.ci_summary_debt_carrying_capacity, ci_summary_pv_exports_heading=self.ci_summary_pv_exports_heading, ci_summary_external_thresholds_grid_heading=self.ci_summary_external_thresholds_grid_heading, ci_summary_pv_of_debt_grid_heading=self.ci_summary_pv_of_debt_grid_heading, ci_summary_pv_exports_grid_heading=self.ci_summary_pv_exports_grid_heading, ci_summary_pv_gdp_grid_heading=self.ci_summary_pv_gdp_grid_heading)

    @cached_property
    def ci_summary_pv_gdp_applicable(self) -> float | str:
        return internals.ci_summary_pv_gdp_applicable(ci_summary_old_framework_gdp_lookup=self.ci_summary_old_framework_gdp_lookup, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, ci_class_labels_thresholds=data.CI_CLASS_LABELS_THRESHOLDS, ci_ext_pv_debt_exports=data.CI_EXT_PV_DEBT_EXPORTS, ci_ext_pv_debt_gdp=data.CI_EXT_PV_DEBT_GDP, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, ci_summary_debt_carrying_capacity=self.ci_summary_debt_carrying_capacity, ci_summary_pv_gdp_heading=self.ci_summary_pv_gdp_heading, ci_summary_external_thresholds_grid_heading=self.ci_summary_external_thresholds_grid_heading, ci_summary_pv_of_debt_grid_heading=self.ci_summary_pv_of_debt_grid_heading, ci_summary_pv_exports_grid_heading=self.ci_summary_pv_exports_grid_heading, ci_summary_pv_gdp_grid_heading=self.ci_summary_pv_gdp_grid_heading)

    @cached_property
    def ci_summary_ds_exports_applicable(self) -> float | str:
        return internals.ci_summary_ds_exports_applicable(ci_summary_old_framework_ds_exports_lookup=self.ci_summary_old_framework_ds_exports_lookup, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, ci_class_labels_thresholds=data.CI_CLASS_LABELS_THRESHOLDS, ci_ext_debt_service_exports=data.CI_EXT_DEBT_SERVICE_EXPORTS, ci_ext_debt_service_revenue=data.CI_EXT_DEBT_SERVICE_REVENUE, ci_debt_service_in_percent_of=data.CI_DEBT_SERVICE_IN_PERCENT_OF, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, ci_summary_debt_carrying_capacity=self.ci_summary_debt_carrying_capacity, ci_summary_ds_exports_heading=self.ci_summary_ds_exports_heading, ci_summary_external_thresholds_grid_heading=self.ci_summary_external_thresholds_grid_heading, ci_summary_ds_exports_grid_heading=self.ci_summary_ds_exports_grid_heading, ci_summary_ds_revenue_grid_heading=self.ci_summary_ds_revenue_grid_heading)

    @cached_property
    def ci_summary_ds_revenue_applicable(self) -> float | str:
        return internals.ci_summary_ds_revenue_applicable(ci_summary_old_framework_ds_revenue_lookup=self.ci_summary_old_framework_ds_revenue_lookup, lookup_ida_terms_new=data.LOOKUP_IDA_TERMS_NEW, ci_class_labels_thresholds=data.CI_CLASS_LABELS_THRESHOLDS, ci_ext_debt_service_exports=data.CI_EXT_DEBT_SERVICE_EXPORTS, ci_ext_debt_service_revenue=data.CI_EXT_DEBT_SERVICE_REVENUE, ci_debt_service_in_percent_of=data.CI_DEBT_SERVICE_IN_PERCENT_OF, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, ci_summary_debt_carrying_capacity=self.ci_summary_debt_carrying_capacity, ci_summary_ds_revenue_heading=self.ci_summary_ds_revenue_heading, ci_summary_external_thresholds_grid_heading=self.ci_summary_external_thresholds_grid_heading, ci_summary_ds_exports_grid_heading=self.ci_summary_ds_exports_grid_heading, ci_summary_ds_revenue_grid_heading=self.ci_summary_ds_revenue_grid_heading)

    @cached_property
    def ci_summary_index_components(self) -> data.Series[float | str | None]:
        return internals.ci_summary_index_components(ci_probit_coefficients=data.CI_PROBIT_COEFFICIENTS, ci_summary_components_by_year=self.ci_summary_components_by_year)

    @cached_property
    def ci_summary_ci_score(self) -> float | str:
        return internals.ci_summary_ci_score(ci_summary_index_components=self.ci_summary_index_components)

    @cached_property
    def ci_summary_ci_rating(self) -> str | int | float | bool:
        return internals.ci_summary_ci_rating(ci_cutoff_weak=data.CI_CUTOFF_WEAK, ci_cutoff_strong=data.CI_CUTOFF_STRONG, ci_class_labels_cutoffs=data.CI_CLASS_LABELS_CUTOFFS, ci_summary_ci_score=self.ci_summary_ci_score)

    @cached_property
    def ci_summary_components_by_year(self) -> data.Series[float | str | None]:
        return internals.ci_summary_components_by_year(ci_remittances_higher_cutoff=data.CI_REMITTANCES_HIGHER_CUTOFF, imported_classification_values=self.imported_classification_values, ci_summary_gdp_us_dollars_billions=self.ci_summary_gdp_us_dollars_billions, ci_summary_remittances_gross_us_dollars_billions=self.ci_summary_remittances_gross_us_dollars_billions)

    @cached_property
    def ci_summary_cpia_rating(self) -> float | str:
        return internals.ci_summary_cpia_rating(ci_pub_pv_debt_gdp_old=data.CI_PUB_PV_DEBT_GDP_OLD, ci_public_pv_gdp_caption=data.CI_PUBLIC_PV_GDP_CAPTION, ci_summary_performance_policy=self.ci_summary_performance_policy, ci_summary_old_public_heading=self.ci_summary_old_public_heading, ci_summary_old_public_pv_heading=self.ci_summary_old_public_pv_heading, ci_summary_old_public_capacity_class_headers=self.ci_summary_old_public_capacity_class_headers)

    @cached_property
    def ci_summary_performance_policy(self) -> str | int | float | bool:
        return internals.ci_summary_performance_policy(imported_composite_indicator=self.imported_composite_indicator)

    @cached_property
    def ci_summary_old_policy_exports_threshold(self) -> float | str:
        return internals.ci_summary_old_policy_exports_threshold(ci_ref_pv_of_debt_in_of_exports=data.CI_REF_PV_OF_DEBT_IN_OF_EXPORTS, ci_pub_pv_debt_exports=data.CI_PUB_PV_DEBT_EXPORTS, ci_pub_pv_debt_gdp=data.CI_PUB_PV_DEBT_GDP, ci_pub_debt_service_exports=data.CI_PUB_DEBT_SERVICE_EXPORTS, ci_pub_debt_service_revenue=data.CI_PUB_DEBT_SERVICE_REVENUE, ci_summary_performance_policy=self.ci_summary_performance_policy, ci_summary_old_external_heading=self.ci_summary_old_external_heading, ci_summary_old_pv_heading=self.ci_summary_old_pv_heading, ci_summary_old_ds_heading=self.ci_summary_old_ds_heading, ci_summary_old_capacity_class_headers=self.ci_summary_old_capacity_class_headers, ci_summary_old_pv_exports_grid_heading=self.ci_summary_old_pv_exports_grid_heading, ci_summary_old_pv_gdp_grid_heading=self.ci_summary_old_pv_gdp_grid_heading, ci_summary_old_ds_exports_grid_heading=self.ci_summary_old_ds_exports_grid_heading, ci_summary_old_ds_revenue_grid_heading=self.ci_summary_old_ds_revenue_grid_heading)

    @cached_property
    def ci_summary_old_framework_gdp_lookup(self) -> float | str:
        return internals.ci_summary_old_framework_gdp_lookup(ci_ref_pv_of_debt_in_of_gdp=data.CI_REF_PV_OF_DEBT_IN_OF_GDP, ci_pub_pv_debt_exports=data.CI_PUB_PV_DEBT_EXPORTS, ci_pub_pv_debt_gdp=data.CI_PUB_PV_DEBT_GDP, ci_pub_debt_service_exports=data.CI_PUB_DEBT_SERVICE_EXPORTS, ci_pub_debt_service_revenue=data.CI_PUB_DEBT_SERVICE_REVENUE, ci_summary_performance_policy=self.ci_summary_performance_policy, ci_summary_old_external_heading=self.ci_summary_old_external_heading, ci_summary_old_pv_heading=self.ci_summary_old_pv_heading, ci_summary_old_ds_heading=self.ci_summary_old_ds_heading, ci_summary_old_capacity_class_headers=self.ci_summary_old_capacity_class_headers, ci_summary_old_pv_exports_grid_heading=self.ci_summary_old_pv_exports_grid_heading, ci_summary_old_pv_gdp_grid_heading=self.ci_summary_old_pv_gdp_grid_heading, ci_summary_old_ds_exports_grid_heading=self.ci_summary_old_ds_exports_grid_heading, ci_summary_old_ds_revenue_grid_heading=self.ci_summary_old_ds_revenue_grid_heading)

    @cached_property
    def ci_summary_old_framework_ds_exports_lookup(self) -> float | str:
        return internals.ci_summary_old_framework_ds_exports_lookup(ci_ref_debt_service_in_of_exports=data.CI_REF_DEBT_SERVICE_IN_OF_EXPORTS, ci_pub_debt_service_exports=data.CI_PUB_DEBT_SERVICE_EXPORTS, ci_pub_debt_service_revenue=data.CI_PUB_DEBT_SERVICE_REVENUE, ci_summary_performance_policy=self.ci_summary_performance_policy, ci_summary_old_external_heading=self.ci_summary_old_external_heading, ci_summary_old_ds_heading=self.ci_summary_old_ds_heading, ci_summary_old_capacity_class_headers=self.ci_summary_old_capacity_class_headers, ci_summary_old_ds_exports_grid_heading=self.ci_summary_old_ds_exports_grid_heading, ci_summary_old_ds_revenue_grid_heading=self.ci_summary_old_ds_revenue_grid_heading)

    @cached_property
    def ci_summary_old_framework_ds_revenue_lookup(self) -> float | str:
        return internals.ci_summary_old_framework_ds_revenue_lookup(ci_ref_debt_service_in_of_revenue=data.CI_REF_DEBT_SERVICE_IN_OF_REVENUE, ci_pub_debt_service_exports=data.CI_PUB_DEBT_SERVICE_EXPORTS, ci_pub_debt_service_revenue=data.CI_PUB_DEBT_SERVICE_REVENUE, ci_summary_performance_policy=self.ci_summary_performance_policy, ci_summary_old_external_heading=self.ci_summary_old_external_heading, ci_summary_old_ds_heading=self.ci_summary_old_ds_heading, ci_summary_old_capacity_class_headers=self.ci_summary_old_capacity_class_headers, ci_summary_old_ds_exports_grid_heading=self.ci_summary_old_ds_exports_grid_heading, ci_summary_old_ds_revenue_grid_heading=self.ci_summary_old_ds_revenue_grid_heading)

    @cached_property
    def ci_summary_old_external_heading(self) -> str | int | float | bool:
        return internals.ci_summary_old_external_heading(ci_summary_external_thresholds_grid_heading=self.ci_summary_external_thresholds_grid_heading)

    @cached_property
    def ci_summary_old_public_heading(self) -> str | int | float | bool:
        return internals.ci_summary_old_public_heading(ci_summary_public_benchmark_grid_heading=self.ci_summary_public_benchmark_grid_heading)

    @cached_property
    def ci_summary_old_pv_heading(self) -> str | int | float | bool:
        return internals.ci_summary_old_pv_heading(ci_summary_pv_of_debt_grid_heading=self.ci_summary_pv_of_debt_grid_heading)

    @cached_property
    def ci_summary_old_public_pv_heading(self) -> str | int | float | bool:
        return internals.ci_summary_old_public_pv_heading(ci_summary_public_pv_grid_heading=self.ci_summary_public_pv_grid_heading)

    @cached_property
    def ci_summary_old_ds_heading(self) -> str | int | float | bool:
        return internals.ci_summary_old_ds_heading(ci_debt_service_in_percent_of=data.CI_DEBT_SERVICE_IN_PERCENT_OF)

    @cached_property
    def ci_summary_debt_carrying_capacity_vintage_reconciled(self) -> str | int | float | bool:
        return internals.ci_summary_debt_carrying_capacity_vintage_reconciled(ci_summary_debt_carrying_capacity_current_vintage=self.ci_summary_debt_carrying_capacity_current_vintage, ci_summary_medium=self.ci_summary_medium)

    @cached_property
    def ci_summary_debt_carrying_capacity_current_vintage(self) -> str | int | float | bool:
        return internals.ci_summary_debt_carrying_capacity_current_vintage(input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, ci_summary_ci_rating=self.ci_summary_ci_rating, ci_summary_performance_policy=self.ci_summary_performance_policy)

    @cached_property
    def ci_summary_external_thresholds_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_external_thresholds_grid_heading(ci_summary_external_thresholds_heading=self.ci_summary_external_thresholds_heading)

    @cached_property
    def ci_summary_pv_of_debt_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_pv_of_debt_grid_heading(ci_summary_pv_of_debt_heading=self.ci_summary_pv_of_debt_heading)

    @cached_property
    def ci_summary_pv_exports_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_pv_exports_grid_heading(ci_summary_pv_exports_heading=self.ci_summary_pv_exports_heading)

    @cached_property
    def ci_summary_pv_gdp_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_pv_gdp_grid_heading(ci_summary_pv_gdp_heading=self.ci_summary_pv_gdp_heading)

    @cached_property
    def ci_summary_ds_exports_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_ds_exports_grid_heading(ci_summary_ds_exports_heading=self.ci_summary_ds_exports_heading)

    @cached_property
    def ci_summary_ds_revenue_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_ds_revenue_grid_heading(ci_summary_ds_revenue_heading=self.ci_summary_ds_revenue_heading)

    @cached_property
    def ci_summary_public_benchmark_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_public_benchmark_grid_heading(ci_summary_public_benchmark_heading=self.ci_summary_public_benchmark_heading)

    @cached_property
    def ci_summary_public_pv_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_public_pv_grid_heading(ci_summary_public_pv_heading=self.ci_summary_public_pv_heading)

    @cached_property
    def ci_summary_public_capacity_class_headers(self) -> data.Series[str | int | float | bool | None]:
        return internals.ci_summary_public_capacity_class_headers(ci_class_labels_thresholds=data.CI_CLASS_LABELS_THRESHOLDS)

    @cached_property
    def ci_summary_old_capacity_class_headers(self) -> data.Series[str | int | float | bool | None]:
        return internals.ci_summary_old_capacity_class_headers(ci_class_labels_thresholds=data.CI_CLASS_LABELS_THRESHOLDS)

    @cached_property
    def ci_summary_old_public_capacity_class_headers(self) -> data.Series[str | int | float | bool | None]:
        return internals.ci_summary_old_public_capacity_class_headers(ci_summary_public_capacity_class_headers=self.ci_summary_public_capacity_class_headers)

    @cached_property
    def ci_summary_old_pv_exports_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_old_pv_exports_grid_heading(ci_summary_pv_exports_grid_heading=self.ci_summary_pv_exports_grid_heading)

    @cached_property
    def ci_summary_old_pv_gdp_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_old_pv_gdp_grid_heading(ci_summary_pv_gdp_grid_heading=self.ci_summary_pv_gdp_grid_heading)

    @cached_property
    def ci_summary_old_ds_exports_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_old_ds_exports_grid_heading(ci_summary_ds_exports_grid_heading=self.ci_summary_ds_exports_grid_heading)

    @cached_property
    def ci_summary_old_ds_revenue_grid_heading(self) -> str | int | float | bool:
        return internals.ci_summary_old_ds_revenue_grid_heading(ci_summary_ds_revenue_grid_heading=self.ci_summary_ds_revenue_grid_heading)

    @cached_property
    def trigger_ifscode_header(self) -> str | int | float | bool:
        return internals.trigger_ifscode_header(lookup_country_table_headers=data.LOOKUP_COUNTRY_TABLE_HEADERS)

    @cached_property
    def trigger_country_header(self) -> str | int | float | bool:
        return internals.trigger_country_header(lookup_country_table_headers=data.LOOKUP_COUNTRY_TABLE_HEADERS)

    @cached_property
    def trigger_ifscode(self) -> data.Series[int | str | None]:
        return internals.trigger_ifscode(imported_ppp_ifs_code=data.IMPORTED_PPP_IFS_CODE)

    @cached_property
    def trigger_isocode(self) -> data.Series[str | int | float | bool | None]:
        return internals.trigger_isocode(lookup_imf_country_code=data.LOOKUP_IMF_COUNTRY_CODE, lookup_country_table_headers=data.LOOKUP_COUNTRY_TABLE_HEADERS, lookup_iso_alpha3=data.LOOKUP_ISO_ALPHA3, lookup_country_name=data.LOOKUP_COUNTRY_NAME, lookup_hipc_status=data.LOOKUP_HIPC_STATUS, trigger_ifscode_header=self.trigger_ifscode_header, trigger_ifscode=self.trigger_ifscode)

    @cached_property
    def trigger_country_name(self) -> data.Series[str | int | float | bool | None]:
        return internals.trigger_country_name(lookup_imf_country_code=data.LOOKUP_IMF_COUNTRY_CODE, lookup_country_table_headers=data.LOOKUP_COUNTRY_TABLE_HEADERS, lookup_iso_alpha3=data.LOOKUP_ISO_ALPHA3, lookup_country_name=data.LOOKUP_COUNTRY_NAME, lookup_hipc_status=data.LOOKUP_HIPC_STATUS, trigger_country_header=self.trigger_country_header, trigger_ifscode=self.trigger_ifscode)

    @cached_property
    def trigger_ppp_year(self) -> data.Series[int | str | None]:
        return internals.trigger_ppp_year(trigger_left_headers=data.TRIGGER_LEFT_HEADERS, imported_ppp_headers=data.IMPORTED_PPP_HEADERS, imported_ppp_ifs_code=data.IMPORTED_PPP_IFS_CODE, imported_ppp_country_name=data.IMPORTED_PPP_COUNTRY_NAME, imported_ppp_year=data.IMPORTED_PPP_YEAR, imported_ppp_incgr=data.IMPORTED_PPP_INCGR, imported_ppp_licdsf=data.IMPORTED_PPP_LICDSF, imported_ppp_kppp=data.IMPORTED_PPP_KPPP, imported_ppp_gdp=data.IMPORTED_PPP_GDP, imported_ppp_ratio=data.IMPORTED_PPP_RATIO)

    @cached_property
    def trigger_ppp_stocks(self) -> data.Series[float | str | None]:
        return internals.trigger_ppp_stocks(trigger_left_headers=data.TRIGGER_LEFT_HEADERS, imported_ppp_headers=data.IMPORTED_PPP_HEADERS, imported_ppp_ifs_code=data.IMPORTED_PPP_IFS_CODE, imported_ppp_country_name=data.IMPORTED_PPP_COUNTRY_NAME, imported_ppp_year=data.IMPORTED_PPP_YEAR, imported_ppp_incgr=data.IMPORTED_PPP_INCGR, imported_ppp_licdsf=data.IMPORTED_PPP_LICDSF, imported_ppp_kppp=data.IMPORTED_PPP_KPPP, imported_ppp_gdp=data.IMPORTED_PPP_GDP, imported_ppp_ratio=data.IMPORTED_PPP_RATIO)

    @cached_property
    def trigger_market_access_country_code(self) -> data.Series[int | str | None]:
        return internals.trigger_market_access_country_code(lookup_imf_country_code_index=data.LOOKUP_IMF_COUNTRY_CODE_INDEX, lookup_country_name=data.LOOKUP_COUNTRY_NAME, lookup_hipc_status=data.LOOKUP_HIPC_STATUS, lookup_mdri=data.LOOKUP_MDRI, trigger_country_names=data.TRIGGER_COUNTRY_NAMES)

    @cached_property
    def trigger_market_access(self) -> data.Series[str | int | float | bool | None]:
        return internals.trigger_market_access(trigger_right_headers=data.TRIGGER_RIGHT_HEADERS, imported_prgt_header=data.IMPORTED_PRGT_HEADER, imported_eurobond_header=self.imported_eurobond_header, imported_country_imf_codes=self.imported_country_imf_codes, imported_country_market_access=self.imported_country_market_access, imported_country_imf_codes_overflow=self.imported_country_imf_codes_overflow, imported_country_market_access_overflow=self.imported_country_market_access_overflow, trigger_market_access_country_code=self.trigger_market_access_country_code)

    @cached_property
    def baseline_pub_public_sector_debt(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_public_sector_debt(baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, macro_debt_total_public_debt_outstanding_year_end=self.macro_debt_total_public_debt_outstanding_year_end)

    @cached_property
    def baseline_pub_of_which_fx_denominated(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_of_which_fx_denominated(baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, macro_debt_fx_denominated_public_debt_end_of_period=self.macro_debt_fx_denominated_public_debt_end_of_period)

    @cached_property
    def baseline_pub_change_in_public_sector_debt(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_change_in_public_sector_debt(baseline_pub_public_sector_debt=self.baseline_pub_public_sector_debt)

    @cached_property
    def baseline_pub_identified_debt_creating_flows(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_identified_debt_creating_flows(baseline_pub_primary_deficit=self.baseline_pub_primary_deficit, baseline_pub_automatic_debt_dynamics=self.baseline_pub_automatic_debt_dynamics, baseline_pub_other_identified_debt_creating_flows=self.baseline_pub_other_identified_debt_creating_flows)

    @cached_property
    def baseline_pub_primary_deficit(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_primary_deficit(baseline_pub_revenue_grants=self.baseline_pub_revenue_grants, baseline_pub_primary_noninterest_expenditure=self.baseline_pub_primary_noninterest_expenditure)

    @cached_property
    def baseline_pub_primary_deficit_by_indicator(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_primary_deficit_by_indicator(baseline_pub_primary_deficit=self.baseline_pub_primary_deficit)

    @cached_property
    def baseline_pub_revenue_grants(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_revenue_grants(macro_debt_public_sector_revenues_including_grants=self.macro_debt_public_sector_revenues_including_grants, macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def baseline_pub_of_which_grants(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_of_which_grants(baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, macro_debt_public_sector_grants=self.macro_debt_public_sector_grants)

    @cached_property
    def baseline_pub_primary_noninterest_expenditure(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_primary_noninterest_expenditure(baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, macro_debt_public_sector_primary_expenditure=self.macro_debt_public_sector_primary_expenditure)

    @cached_property
    def baseline_pub_automatic_debt_dynamics(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_automatic_debt_dynamics(baseline_pub_contribution_from_interest_rate_growth=self.baseline_pub_contribution_from_interest_rate_growth, baseline_pub_contribution_from_real_exchange_rate=self.baseline_pub_contribution_from_real_exchange_rate)

    @cached_property
    def baseline_pub_contribution_from_interest_rate_growth(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_contribution_from_interest_rate_growth(baseline_pub_of_which_contribution_from_average_real=self.baseline_pub_of_which_contribution_from_average_real, baseline_pub_of_which_contribution_from_real_gdp_growth=self.baseline_pub_of_which_contribution_from_real_gdp_growth)

    @cached_property
    def baseline_pub_of_which_contribution_from_average_real(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_of_which_contribution_from_average_real(baseline_pub_public_sector_debt=self.baseline_pub_public_sector_debt, baseline_pub_hide=self.baseline_pub_hide, baseline_pub_average_real_interest_rate=self.baseline_pub_average_real_interest_rate)

    @cached_property
    def baseline_pub_of_which_contribution_from_real_gdp_growth(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_of_which_contribution_from_real_gdp_growth(baseline_pub_public_sector_debt=self.baseline_pub_public_sector_debt, baseline_pub_hide=self.baseline_pub_hide, baseline_pub_real_gdp_growth=self.baseline_pub_real_gdp_growth)

    @cached_property
    def baseline_pub_contribution_from_real_exchange_rate(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_contribution_from_real_exchange_rate(baseline_pub_of_which_fx_denominated=self.baseline_pub_of_which_fx_denominated, baseline_pub_hide=self.baseline_pub_hide, baseline_pub_average_real_interest_rate_ext_debt=self.baseline_pub_average_real_interest_rate_ext_debt, baseline_pub_real_exchange_rate_depreciation_pct_indicates=self.baseline_pub_real_exchange_rate_depreciation_pct_indicates)

    @cached_property
    def baseline_pub_hide(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_hide(baseline_pub_real_gdp_growth=self.baseline_pub_real_gdp_growth)

    @cached_property
    def baseline_pub_other_identified_debt_creating_flows(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_other_identified_debt_creating_flows(baseline_pub_privatization_receipts_negative=self.baseline_pub_privatization_receipts_negative, baseline_pub_recognition_of_contingent_liab_e_g_bank=self.baseline_pub_recognition_of_contingent_liab_e_g_bank, baseline_pub_debt_relief_hipc_other=self.baseline_pub_debt_relief_hipc_other, baseline_pub_other_debt_creating_reducing_flow_please_specify=self.baseline_pub_other_debt_creating_reducing_flow_please_specify)

    @cached_property
    def baseline_pub_privatization_receipts_negative(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_privatization_receipts_negative(baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, macro_debt_privatization_receipts=self.macro_debt_privatization_receipts)

    @cached_property
    def baseline_pub_recognition_of_contingent_liab_e_g_bank(self) -> data.Series[int | str | None]:
        return internals.baseline_pub_recognition_of_contingent_liab_e_g_bank(baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, macro_debt_recognition_of_contingent_liab_e_g_bank=self.macro_debt_recognition_of_contingent_liab_e_g_bank)

    @cached_property
    def baseline_pub_debt_relief_hipc_other(self) -> data.Series[int | str | None]:
        return internals.baseline_pub_debt_relief_hipc_other(baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, macro_debt_debt_relief=self.macro_debt_debt_relief)

    @cached_property
    def baseline_pub_other_debt_creating_reducing_flow_please_specify(self) -> data.Series[int | str | None]:
        return internals.baseline_pub_other_debt_creating_reducing_flow_please_specify(baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, macro_debt_other_debt_creating_reducing_flow_please_specify=self.macro_debt_other_debt_creating_reducing_flow_please_specify)

    @cached_property
    def baseline_pub_residual(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_residual(baseline_pub_change_in_public_sector_debt=self.baseline_pub_change_in_public_sector_debt, baseline_pub_identified_debt_creating_flows=self.baseline_pub_identified_debt_creating_flows)

    @cached_property
    def baseline_pub_pv_of_public_debt_gdp_ratio(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_pv_of_public_debt_gdp_ratio(baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, macro_debt_total_public_domestic_debt=self.macro_debt_total_public_domestic_debt, macro_debt_pv_of_public_sector_ext_debt_end_of_period=self.macro_debt_pv_of_public_sector_ext_debt_end_of_period)

    @cached_property
    def baseline_pub_pv_of_public_debt_revenue_grants_ratio(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_pv_of_public_debt_revenue_grants_ratio(baseline_pub_revenue_grants=self.baseline_pub_revenue_grants, baseline_pub_pv_of_public_debt_gdp_ratio=self.baseline_pub_pv_of_public_debt_gdp_ratio)

    @cached_property
    def baseline_pub_debt_service_revenue_grants_ratio(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_revenue_grants_ratio(macro_debt_public_domestic_st=self.macro_debt_public_domestic_st, macro_debt_total_mlt_public_domestic_debt_amortization_debt=self.macro_debt_total_mlt_public_domestic_debt_amortization_debt, macro_debt_public_sector_revenues_including_grants=self.macro_debt_public_sector_revenues_including_grants, macro_debt_public_sector_interest_expenditure=self.macro_debt_public_sector_interest_expenditure, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6)

    @cached_property
    def baseline_pub_gross_financing_need(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_gross_financing_need(baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, macro_debt_gross_financing_need=self.macro_debt_gross_financing_need)

    @cached_property
    def baseline_pub_nominal_gdp_lc(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_nominal_gdp_lc(macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def baseline_pub_real_gdp_growth(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_real_gdp_growth(macro_debt_real_gdp_growth=self.macro_debt_real_gdp_growth)

    @cached_property
    def baseline_pub_real_gdp_growth_by_indicator(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_real_gdp_growth_by_indicator(baseline_pub_real_gdp_growth=self.baseline_pub_real_gdp_growth)

    @cached_property
    def baseline_pub_average_nominal_interest_rate_public_debt(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_average_nominal_interest_rate_public_debt(macro_debt_public_sector_interest_expenditure=self.macro_debt_public_sector_interest_expenditure, macro_debt_total_public_debt_outstanding_year_end=self.macro_debt_total_public_debt_outstanding_year_end)

    @cached_property
    def baseline_pub_average_nominal_interest_rate_ext_debt(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_average_nominal_interest_rate_ext_debt(baseline_pub_average_nominal_interest_rate_public_debt=self.baseline_pub_average_nominal_interest_rate_public_debt, macro_debt_interest_rate_ext_debt=self.macro_debt_interest_rate_ext_debt)

    @cached_property
    def baseline_pub_average_nominal_interest_rate_domestic_debt(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_average_nominal_interest_rate_domestic_debt(baseline_pub_average_nominal_interest_rate_public_debt=self.baseline_pub_average_nominal_interest_rate_public_debt, macro_debt_interest_rate_domestic_debt=self.macro_debt_interest_rate_domestic_debt)

    @cached_property
    def baseline_pub_average_real_interest_rate(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_average_real_interest_rate(baseline_pub_public_sector_debt=self.baseline_pub_public_sector_debt, baseline_pub_of_which_fx_denominated=self.baseline_pub_of_which_fx_denominated, baseline_pub_average_real_interest_rate_domestic_debt=self.baseline_pub_average_real_interest_rate_domestic_debt, baseline_pub_average_real_interest_rate_ext_debt=self.baseline_pub_average_real_interest_rate_ext_debt)

    @cached_property
    def baseline_pub_average_real_interest_rate_domestic_debt(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_average_real_interest_rate_domestic_debt(baseline_pub_average_nominal_interest_rate_domestic_debt=self.baseline_pub_average_nominal_interest_rate_domestic_debt, baseline_pub_inflation_rate_gdp_deflator_pct=self.baseline_pub_inflation_rate_gdp_deflator_pct)

    @cached_property
    def baseline_pub_average_real_interest_rate_ext_debt(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_average_real_interest_rate_ext_debt(baseline_pub_average_nominal_interest_rate_ext_debt=self.baseline_pub_average_nominal_interest_rate_ext_debt, baseline_pub_us_inflation_rate_gdp_deflator_pct=self.baseline_pub_us_inflation_rate_gdp_deflator_pct)

    @cached_property
    def baseline_pub_exchange_rate_lc_per_us_dollar(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_exchange_rate_lc_per_us_dollar(macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar)

    @cached_property
    def baseline_pub_nominal_depreciation_of_lc_percentage_change_lc(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_nominal_depreciation_of_lc_percentage_change_lc(baseline_pub_exchange_rate_lc_per_us_dollar=self.baseline_pub_exchange_rate_lc_per_us_dollar)

    @cached_property
    def baseline_pub_exchange_rate_us_dollar_per_lc(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_exchange_rate_us_dollar_per_lc(baseline_pub_exchange_rate_lc_per_us_dollar=self.baseline_pub_exchange_rate_lc_per_us_dollar)

    @cached_property
    def baseline_pub_nominal_appreciation_increase_in_us_dollar(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_nominal_appreciation_increase_in_us_dollar(baseline_pub_exchange_rate_us_dollar_per_lc=self.baseline_pub_exchange_rate_us_dollar_per_lc)

    @cached_property
    def baseline_pub_real_exchange_rate_depreciation_pct_indicates(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_real_exchange_rate_depreciation_pct_indicates(baseline_pub_nominal_depreciation_of_lc_percentage_change_lc=self.baseline_pub_nominal_depreciation_of_lc_percentage_change_lc, baseline_pub_inflation_rate_gdp_deflator_pct=self.baseline_pub_inflation_rate_gdp_deflator_pct, baseline_pub_us_inflation_rate_gdp_deflator_pct=self.baseline_pub_us_inflation_rate_gdp_deflator_pct)

    @cached_property
    def baseline_pub_inflation_rate_gdp_deflator_pct(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_inflation_rate_gdp_deflator_pct(macro_debt_change_in_gdp_deflator_factor=self.macro_debt_change_in_gdp_deflator_factor)

    @cached_property
    def baseline_pub_inflation_rate_gdp_deflator_pct_al(self) -> float | str:
        return internals.baseline_pub_inflation_rate_gdp_deflator_pct_al(baseline_pub_inflation_rate_gdp_deflator_pct=self.baseline_pub_inflation_rate_gdp_deflator_pct)

    @cached_property
    def baseline_pub_us_inflation_rate_gdp_deflator_pct(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_us_inflation_rate_gdp_deflator_pct(macro_debt_us_gdp_deflator_percent_change=self.macro_debt_us_gdp_deflator_percent_change)

    @cached_property
    def baseline_pub_gross_financing_need_by_year(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_gross_financing_need_by_year(baseline_pub_gross_financing_need=self.baseline_pub_gross_financing_need, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc)

    @cached_property
    def baseline_pub_debt_service_in_lcu_baseline(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_in_lcu_baseline(macro_debt_public_domestic_st=self.macro_debt_public_domestic_st, macro_debt_total_mlt_public_domestic_debt_amortization_debt=self.macro_debt_total_mlt_public_domestic_debt_amortization_debt, macro_debt_public_sector_interest_expenditure=self.macro_debt_public_sector_interest_expenditure, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6)

    @cached_property
    def baseline_pub_pv_of_public_debt_level_in_lcu_baseline(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_pv_of_public_debt_level_in_lcu_baseline(baseline_pub_pv_of_public_debt_gdp_ratio=self.baseline_pub_pv_of_public_debt_gdp_ratio, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc)

    @cached_property
    def baseline_pub_pv_of_public_debt_gdp_ratio_b3_exports(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_pv_of_public_debt_gdp_ratio_b3_exports(dsa_ext_pv_of_additional_borrowing=self.dsa_ext_pv_of_additional_borrowing, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, baseline_pub_exchange_rate_lc_per_us_dollar=self.baseline_pub_exchange_rate_lc_per_us_dollar, baseline_pub_pv_of_public_debt_level_in_lcu_baseline=self.baseline_pub_pv_of_public_debt_level_in_lcu_baseline)

    @cached_property
    def baseline_pub_pv_of_public_debt_gdp_ratio_b4_other_flows(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_pv_of_public_debt_gdp_ratio_b4_other_flows(dsa_ext_pv_of_additional_borrowing=self.dsa_ext_pv_of_additional_borrowing, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, baseline_pub_exchange_rate_lc_per_us_dollar=self.baseline_pub_exchange_rate_lc_per_us_dollar, baseline_pub_pv_of_public_debt_level_in_lcu_baseline=self.baseline_pub_pv_of_public_debt_level_in_lcu_baseline)

    @cached_property
    def baseline_pub_pv_of_public_debt_gdp_ratio_c4_mkt_fin(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_pv_of_public_debt_gdp_ratio_c4_mkt_fin(c4_mkt_fin_pv_debt_adjustments=self.c4_mkt_fin_pv_debt_adjustments, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, baseline_pub_exchange_rate_lc_per_us_dollar=self.baseline_pub_exchange_rate_lc_per_us_dollar, baseline_pub_pv_of_public_debt_level_in_lcu_baseline=self.baseline_pub_pv_of_public_debt_level_in_lcu_baseline)

    @cached_property
    def baseline_pub_pv_of_public_debt_revenue_grants_ratio_exports_shock(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_pv_of_public_debt_revenue_grants_ratio_exports_shock(baseline_pub_revenue_grants=self.baseline_pub_revenue_grants, baseline_pub_pv_of_public_debt_gdp_ratio_b3_exports=self.baseline_pub_pv_of_public_debt_gdp_ratio_b3_exports)

    @cached_property
    def baseline_pub_pv_of_public_debt_revenue_grants_ratio_b4_other(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_pv_of_public_debt_revenue_grants_ratio_b4_other(baseline_pub_revenue_grants=self.baseline_pub_revenue_grants, baseline_pub_pv_of_public_debt_gdp_ratio_b4_other_flows=self.baseline_pub_pv_of_public_debt_gdp_ratio_b4_other_flows)

    @cached_property
    def baseline_pub_pv_of_public_debt_revenue_grants_ratio_c4_mkt(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_pv_of_public_debt_revenue_grants_ratio_c4_mkt(baseline_pub_revenue_grants=self.baseline_pub_revenue_grants, baseline_pub_pv_of_public_debt_gdp_ratio_c4_mkt_fin=self.baseline_pub_pv_of_public_debt_gdp_ratio_c4_mkt_fin)

    @cached_property
    def baseline_pub_debt_service_in_lcu_b3_export_stress_test(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_in_lcu_b3_export_stress_test(dsa_ext_additional_debt_service_stress=self.dsa_ext_additional_debt_service_stress, baseline_pub_debt_service_in_lcu_baseline=self.baseline_pub_debt_service_in_lcu_baseline, leftover_exchange_rate_pa=self.leftover_exchange_rate_pa)

    @cached_property
    def baseline_pub_debt_service_in_lcu_b4_other_flows_stress_test(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_in_lcu_b4_other_flows_stress_test(leftover_exchange_rate_pa=self.leftover_exchange_rate_pa, dsa_ext_additional_debt_service_stress=self.dsa_ext_additional_debt_service_stress, baseline_pub_debt_service_in_lcu_baseline=self.baseline_pub_debt_service_in_lcu_baseline)

    @cached_property
    def baseline_pub_debt_service_in_lcu_c4_market_stress_test(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_in_lcu_c4_market_stress_test(leftover_exchange_rate_pa=self.leftover_exchange_rate_pa, c4_mkt_fin_debt_service_adjustment=self.c4_mkt_fin_debt_service_adjustment, baseline_pub_debt_service_in_lcu_baseline=self.baseline_pub_debt_service_in_lcu_baseline)

    @cached_property
    def baseline_pub_debt_service_revenue_grants_ratio_bseline(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_revenue_grants_ratio_bseline(baseline_pub_debt_service_in_lcu_baseline=self.baseline_pub_debt_service_in_lcu_baseline, macro_debt_public_sector_revenues_including_grants=self.macro_debt_public_sector_revenues_including_grants)

    @cached_property
    def baseline_pub_debt_service_revenue_grants_ratio_b3_exports(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_revenue_grants_ratio_b3_exports(baseline_pub_debt_service_in_lcu_b3_export_stress_test=self.baseline_pub_debt_service_in_lcu_b3_export_stress_test, macro_debt_public_sector_revenues_including_grants=self.macro_debt_public_sector_revenues_including_grants)

    @cached_property
    def baseline_pub_debt_service_revenue_grants_ratio_b4_other_flows(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_revenue_grants_ratio_b4_other_flows(baseline_pub_debt_service_in_lcu_b4_other_flows_stress_test=self.baseline_pub_debt_service_in_lcu_b4_other_flows_stress_test, macro_debt_public_sector_revenues_including_grants=self.macro_debt_public_sector_revenues_including_grants)

    @cached_property
    def baseline_pub_debt_service_revenue_grants_ratio_c4_mkt_fin(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_revenue_grants_ratio_c4_mkt_fin(baseline_pub_debt_service_in_lcu_c4_market_stress_test=self.baseline_pub_debt_service_in_lcu_c4_market_stress_test, macro_debt_public_sector_revenues_including_grants=self.macro_debt_public_sector_revenues_including_grants)

    @cached_property
    def baseline_pub_debt_service_gdp_ratio_baseline(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_gdp_ratio_baseline(baseline_pub_revenue_grants=self.baseline_pub_revenue_grants, baseline_pub_debt_service_revenue_grants_ratio_bseline=self.baseline_pub_debt_service_revenue_grants_ratio_bseline)

    @cached_property
    def baseline_pub_debt_service_gdp_ratio_b3_exports(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_gdp_ratio_b3_exports(baseline_pub_revenue_grants=self.baseline_pub_revenue_grants, baseline_pub_debt_service_revenue_grants_ratio_b3_exports=self.baseline_pub_debt_service_revenue_grants_ratio_b3_exports)

    @cached_property
    def baseline_pub_debt_service_gdp_ratio_b4_other_flows(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_gdp_ratio_b4_other_flows(baseline_pub_revenue_grants=self.baseline_pub_revenue_grants, baseline_pub_debt_service_revenue_grants_ratio_b4_other_flows=self.baseline_pub_debt_service_revenue_grants_ratio_b4_other_flows)

    @cached_property
    def baseline_pub_debt_service_gdp_ratio_c4_mkt_fin(self) -> data.Series[float | str | None]:
        return internals.baseline_pub_debt_service_gdp_ratio_c4_mkt_fin(baseline_pub_revenue_grants=self.baseline_pub_revenue_grants, baseline_pub_debt_service_revenue_grants_ratio_c4_mkt_fin=self.baseline_pub_debt_service_revenue_grants_ratio_c4_mkt_fin)

    @cached_property
    def custom_pub_please_do_not_change_these_numbers(self) -> data.Series[int | str | None]:
        return internals.custom_pub_please_do_not_change_these_numbers(customized_public_template_anchor=self.customized_public_template_anchor)

    @cached_property
    def custom_pub_revenue_grants(self) -> data.Series[float | str | None]:
        return internals.custom_pub_revenue_grants(customized_public_delta=self.customized_public_delta, baseline_pub_revenue_grants=self.baseline_pub_revenue_grants)

    @cached_property
    def custom_pub_primary_noninterest_expenditure(self) -> data.Series[float | str | None]:
        return internals.custom_pub_primary_noninterest_expenditure(customized_public_delta=self.customized_public_delta, baseline_pub_primary_noninterest_expenditure=self.baseline_pub_primary_noninterest_expenditure)

    @cached_property
    def custom_pub_grants(self) -> data.Series[float | str | None]:
        return internals.custom_pub_grants(customized_public_delta=self.customized_public_delta, baseline_pub_of_which_grants=self.baseline_pub_of_which_grants)

    @cached_property
    def custom_pub_public_sector_assets_e_g_deposits(self) -> data.Series[float | str | None]:
        return internals.custom_pub_public_sector_assets_e_g_deposits(customized_public_delta=self.customized_public_delta, macro_debt_public_sector_assets_e_g_deposits=self.macro_debt_public_sector_assets_e_g_deposits)

    @cached_property
    def custom_pub_real_gdp_growth(self) -> data.Series[float | str | None]:
        return internals.custom_pub_real_gdp_growth(customized_public_delta=self.customized_public_delta, baseline_pub_real_gdp_growth=self.baseline_pub_real_gdp_growth)

    @cached_property
    def custom_pub_inflation_rate_gdp_deflator_pct(self) -> data.Series[float | str | None]:
        return internals.custom_pub_inflation_rate_gdp_deflator_pct(customized_public_delta=self.customized_public_delta, baseline_pub_inflation_rate_gdp_deflator_pct=self.baseline_pub_inflation_rate_gdp_deflator_pct)

    @cached_property
    def custom_pub_nominal_depreciation_of_lc_percentage_change_lc(self) -> data.Series[float | str | None]:
        return internals.custom_pub_nominal_depreciation_of_lc_percentage_change_lc(customized_public_delta=self.customized_public_delta, baseline_pub_nominal_depreciation_of_lc_percentage_change_lc=self.baseline_pub_nominal_depreciation_of_lc_percentage_change_lc)

    @cached_property
    def custom_pub_exports(self) -> data.Series[float | str | None]:
        return internals.custom_pub_exports(dsa_ext_exports=self.dsa_ext_exports, customized_public_delta=self.customized_public_delta)

    @cached_property
    def custom_pub_gdp_deflator_in_us_dollar_terms_change_pct(self) -> data.Series[float | str | None]:
        return internals.custom_pub_gdp_deflator_in_us_dollar_terms_change_pct(dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent=self.dsa_ext_gdp_deflator_in_us_dollar_terms_change_in_percent, customized_public_delta=self.customized_public_delta)

    @cached_property
    def custom_pub_usd_discount_rate_by_year(self) -> data.Series[int | str | None]:
        return internals.custom_pub_usd_discount_rate_by_year(customized_public_external_mlt_disbursement_profile=self.customized_public_external_mlt_disbursement_profile, custom_pub_avg_maturity_incl_grace_period_by_year=self.custom_pub_avg_maturity_incl_grace_period_by_year)

    @cached_property
    def custom_pub_avg_maturity_incl_grace_period_by_year(self) -> data.Series[int | str | None]:
        return internals.custom_pub_avg_maturity_incl_grace_period_by_year(customized_public_external_mlt_disbursement_profile=self.customized_public_external_mlt_disbursement_profile, custom_pub_period=self.custom_pub_period, custom_pub_avg_grace_period=self.custom_pub_avg_grace_period, custom_pub_avg_maturity_incl_grace_period=self.custom_pub_avg_maturity_incl_grace_period)

    @cached_property
    def custom_pub_avg_grace_period_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_pub_avg_grace_period_by_year(custom_pub_avg_nominal_interest_rate_new_borrowing_usd=self.custom_pub_avg_nominal_interest_rate_new_borrowing_usd, custom_pub_usd_discount_rate_by_year=self.custom_pub_usd_discount_rate_by_year)

    @cached_property
    def custom_pub_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.custom_pub_total_debt_service(custom_pub_avg_maturity_incl_grace_period_by_year=self.custom_pub_avg_maturity_incl_grace_period_by_year, custom_pub_avg_grace_period_by_year=self.custom_pub_avg_grace_period_by_year)

    @cached_property
    def custom_pub_pv_debt(self) -> float | str:
        return internals.custom_pub_pv_debt(custom_pub_usd_discount_rate_by_year=self.custom_pub_usd_discount_rate_by_year, custom_pub_total_debt_service=self.custom_pub_total_debt_service, custom_pub_avg_nominal_interest_rate_new_borrowing_usd=self.custom_pub_avg_nominal_interest_rate_new_borrowing_usd, custom_pub_usd_discount_rate=self.custom_pub_usd_discount_rate)

    @cached_property
    def custom_pub_domestic_mlt_debt(self) -> data.Series[float | str | None]:
        return internals.custom_pub_domestic_mlt_debt(custom_pub_inflation_gdp_deflator=self.custom_pub_inflation_gdp_deflator, custom_pub_avg_real_interest_rate_new_borrowing_by_year=self.custom_pub_avg_real_interest_rate_new_borrowing_by_year)

    @cached_property
    def custom_pub_avg_interest_rate(self) -> data.Series[float | str | None]:
        return internals.custom_pub_avg_interest_rate(custom_pub_inflation_gdp_deflator=self.custom_pub_inflation_gdp_deflator, custom_pub_avg_real_interest_rate_by_year=self.custom_pub_avg_real_interest_rate_by_year)

    @cached_property
    def custom_pub_inflation_gdp_deflator(self) -> data.Series[float | str | None]:
        return internals.custom_pub_inflation_gdp_deflator(custom_pub_inflation_rate_gdp_deflator_pct_by_year=self.custom_pub_inflation_rate_gdp_deflator_pct_by_year)

    @cached_property
    def _scan_custom_pub_new_borrowing_gross_in_lcu(self) -> internals.ScanCustomPubNewBorrowingGrossInLcuResult:
        return internals.scan_custom_pub_new_borrowing_gross_in_lcu(customized_public_template_anchor=self.customized_public_template_anchor, customized_public_natural_disaster_year=self.customized_public_natural_disaster_year, customized_public_new_forex_borrowing_cumulative_overflow=self.customized_public_new_forex_borrowing_cumulative_overflow, customized_public_new_domestic_mlt_cumulative_overflow=self.customized_public_new_domestic_mlt_cumulative_overflow, customized_public_residual_overflow=self.customized_public_residual_overflow, customized_public_new_forex_debt_stock_initial=self.customized_public_new_forex_debt_stock_initial, customized_public_domestic_mlt_interest_initial=self.customized_public_domestic_mlt_interest_initial, customized_public_domestic_st_interest_initial=self.customized_public_domestic_st_interest_initial, baseline_pub_gross_financing_need_by_year=self.baseline_pub_gross_financing_need_by_year, custom_pub_please_do_not_change_these_numbers=self.custom_pub_please_do_not_change_these_numbers, custom_pub_domestic_mlt_debt=self.custom_pub_domestic_mlt_debt, custom_pub_avg_interest_rate=self.custom_pub_avg_interest_rate, custom_pub_t_g_0=self.custom_pub_t_g_0, custom_pub_t_m_condition=self.custom_pub_t_m_condition, custom_pub_t_g_0_by_year=self.custom_pub_t_g_0_by_year, custom_pub_t_m_condition_by_year=self.custom_pub_t_m_condition_by_year, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc, custom_pub_exchange_rate_us_dollar_per_lc=self.custom_pub_exchange_rate_us_dollar_per_lc, custom_pub_primary_deficit_by_year=self.custom_pub_primary_deficit_by_year, custom_pub_other_debt_creating_flows=self.custom_pub_other_debt_creating_flows, macro_debt_public_domestic_st=self.macro_debt_public_domestic_st, macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_total_public_domestic_debt_interest_due=self.macro_debt_total_public_domestic_debt_interest_due, macro_debt_total_mlt_public_domestic_debt_amortization_debt=self.macro_debt_total_mlt_public_domestic_debt_amortization_debt, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6, customized_scenario_spec=self.customized_scenario_spec, custom_pub_avg_grace_period=self.custom_pub_avg_grace_period, custom_pub_avg_maturity_incl_grace_period=self.custom_pub_avg_maturity_incl_grace_period, custom_pub_avg_nominal_interest_rate_new_borrowing_usd=self.custom_pub_avg_nominal_interest_rate_new_borrowing_usd, custom_pub_domestic_mlt=self.custom_pub_domestic_mlt, custom_pub_domestic_st=self.custom_pub_domestic_st, custom_pub_external_ppg_mlt=self.custom_pub_external_ppg_mlt, custom_pub_in_billions_of_lc_of_which_short_term=self.custom_pub_in_billions_of_lc_of_which_short_term, custom_pub_shares_of_marginal_debt_avg_grace_period=self.custom_pub_shares_of_marginal_debt_avg_grace_period, custom_pub_shares_of_marginal_debt_avg_maturity_incl_grace_period=self.custom_pub_shares_of_marginal_debt_avg_maturity_incl_grace_period)

    @cached_property
    def custom_pub_new_borrowing_gross_in_lcu(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_new_borrowing_gross_in_lcu

    @cached_property
    def custom_pub_new_forex_borrowing_gross_usd(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_new_forex_borrowing_gross_usd

    @cached_property
    def custom_pub_cumulative(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_cumulative

    @cached_property
    def custom_pub_stock_of_new_forex_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_stock_of_new_forex_debt

    @cached_property
    def custom_pub_interest(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_interest

    @cached_property
    def custom_pub_amortization(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_amortization

    @cached_property
    def custom_pub_domestic_st_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_domestic_st_debt

    @cached_property
    def custom_pub_domestic_st_debt_t_m_condition(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_domestic_st_debt_t_m_condition

    @cached_property
    def custom_pub_new_domestic_mlt_borrowing_gross(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_new_domestic_mlt_borrowing_gross

    @cached_property
    def custom_pub_cumulative_by_year(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_cumulative_by_year

    @cached_property
    def custom_pub_stock_of_new_domestic_mlt_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_stock_of_new_domestic_mlt_debt

    @cached_property
    def custom_pub_interest_by_year(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_interest_by_year

    @cached_property
    def custom_pub_amortization_by_year(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_amortization_by_year

    @cached_property
    def custom_pub_domestic_st_debt_t_g_0(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_domestic_st_debt_t_g_0

    @cached_property
    def custom_pub_domestic_borrowing_domestic_st_debt_t_m_condition(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_domestic_borrowing_domestic_st_debt_t_m_condition

    @cached_property
    def custom_pub_new_domestic_st_borrowing_gross_also_stock_of(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_new_domestic_st_borrowing_gross_also_stock_of

    @cached_property
    def custom_pub_domestic_st_debt_interest(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_domestic_st_debt_interest

    @cached_property
    def custom_pub_of_which_short_term(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_of_which_short_term

    @cached_property
    def custom_pub_amortization_excluding_st_domestic_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_amortization_excluding_st_domestic_debt

    @cached_property
    def custom_pub_interest_expenditure(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_interest_expenditure

    @cached_property
    def custom_pub_domestic_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_domestic_debt

    @cached_property
    def custom_pub_ext_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_ext_debt

    @cached_property
    def custom_pub_gross_financing_need_in_lc(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_new_borrowing_gross_in_lcu.custom_pub_gross_financing_need_in_lc

    @cached_property
    def custom_pub_pv_of_new_forex_debt(self) -> data.Series[float | str | None]:
        return internals.custom_pub_pv_of_new_forex_debt(custom_pub_pv_debt=self.custom_pub_pv_debt, custom_pub_new_forex_borrowing_gross_usd=self.custom_pub_new_forex_borrowing_gross_usd, custom_pub_total_debt_service_by_year=self.custom_pub_total_debt_service_by_year, custom_pub_amortization=self.custom_pub_amortization, custom_pub_avg_nominal_interest_rate_new_borrowing_usd=self.custom_pub_avg_nominal_interest_rate_new_borrowing_usd, custom_pub_usd_discount_rate=self.custom_pub_usd_discount_rate)

    @cached_property
    def custom_pub_total_debt_service_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_pub_total_debt_service_by_year(custom_pub_interest=self.custom_pub_interest, custom_pub_amortization=self.custom_pub_amortization)

    @cached_property
    def custom_pub_t_g_0(self) -> data.Series[int | str | None]:
        return internals.custom_pub_t_g_0(custom_pub_avg_grace_period=self.custom_pub_avg_grace_period, custom_pub_period=self.custom_pub_period)

    @cached_property
    def custom_pub_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.custom_pub_t_m_condition(custom_pub_avg_maturity_incl_grace_period=self.custom_pub_avg_maturity_incl_grace_period, custom_pub_period=self.custom_pub_period)

    @cached_property
    def custom_pub_t_g_0_by_year(self) -> data.Series[int | str | None]:
        return internals.custom_pub_t_g_0_by_year(custom_pub_shares_of_marginal_debt_avg_grace_period=self.custom_pub_shares_of_marginal_debt_avg_grace_period, custom_pub_period=self.custom_pub_period)

    @cached_property
    def custom_pub_t_m_condition_by_year(self) -> data.Series[int | str | None]:
        return internals.custom_pub_t_m_condition_by_year(custom_pub_shares_of_marginal_debt_avg_maturity_incl_grace_period=self.custom_pub_shares_of_marginal_debt_avg_maturity_incl_grace_period, custom_pub_period=self.custom_pub_period)

    @cached_property
    def _scan_custom_pub_public_sector_debt(self) -> internals.ScanCustomPubPublicSectorDebtResult:
        return internals.scan_custom_pub_public_sector_debt(custom_pub_public_sector_assets_e_g_deposits=self.custom_pub_public_sector_assets_e_g_deposits, custom_pub_of_which_fx_denominated=self.custom_pub_of_which_fx_denominated, custom_pub_primary_deficit=self.custom_pub_primary_deficit, custom_pub_contribution_from_real_exchange_rate=self.custom_pub_contribution_from_real_exchange_rate, custom_pub_denominator_1_g=self.custom_pub_denominator_1_g, custom_pub_other_identified_debt_creating_flows=self.custom_pub_other_identified_debt_creating_flows, custom_pub_residual=self.custom_pub_residual, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc, custom_pub_real_gdp_growth_by_year=self.custom_pub_real_gdp_growth_by_year, custom_pub_average_real_interest_rate_ext_debt=self.custom_pub_average_real_interest_rate_ext_debt, custom_pub_total_public_ext_debt=self.custom_pub_total_public_ext_debt, custom_pub_domestic_debt=self.custom_pub_domestic_debt, macro_debt_public_sector_assets_e_g_deposits=self.macro_debt_public_sector_assets_e_g_deposits, macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc, macro_debt_total_public_debt_outstanding_year_end=self.macro_debt_total_public_debt_outstanding_year_end, custom_pub_inflation_rate_gdp_deflator_pct_by_year=self.custom_pub_inflation_rate_gdp_deflator_pct_by_year, custom_pub_variables_needed_public_public_sector_assets_e_g_deposits=self.custom_pub_variables_needed_public_public_sector_assets_e_g_deposits, pv_resfin_pub_assumptions_average_interest_rate_on_domestic_debt=self.pv_resfin_pub_assumptions_average_interest_rate_on_domestic_debt)

    @cached_property
    def custom_pub_public_sector_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_public_sector_debt

    @cached_property
    def custom_pub_change_in_public_sector_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_change_in_public_sector_debt

    @cached_property
    def custom_pub_identified_debt_creating_flows(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_identified_debt_creating_flows

    @cached_property
    def custom_pub_automatic_debt_dynamics(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_automatic_debt_dynamics

    @cached_property
    def custom_pub_contribution_from_interest_rate_growth(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_contribution_from_interest_rate_growth

    @cached_property
    def custom_pub_of_which_contribution_from_average_real(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_of_which_contribution_from_average_real

    @cached_property
    def custom_pub_of_which_contribution_from_real_gdp_growth(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_of_which_contribution_from_real_gdp_growth

    @cached_property
    def custom_pub_average_nominal_interest_rate_domestic_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_average_nominal_interest_rate_domestic_debt

    @cached_property
    def custom_pub_average_real_interest_rate(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_average_real_interest_rate

    @cached_property
    def custom_pub_average_real_interest_rate_domestic_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_average_real_interest_rate_domestic_debt

    @cached_property
    def custom_pub_nominal_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_nominal_debt

    @cached_property
    def custom_pub_total_public_domestic_debt(self) -> data.Series[float | str | None]:
        return self._scan_custom_pub_public_sector_debt.custom_pub_total_public_domestic_debt

    @cached_property
    def custom_pub_of_which_fx_denominated(self) -> data.Series[float | str | None]:
        return internals.custom_pub_of_which_fx_denominated(custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc, custom_pub_total_public_ext_debt=self.custom_pub_total_public_ext_debt)

    @cached_property
    def custom_pub_pv_of_public_debt_gdp_ratio(self) -> data.Series[float | str | None]:
        return internals.custom_pub_pv_of_public_debt_gdp_ratio(custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc, custom_pub_total_public_domestic_debt=self.custom_pub_total_public_domestic_debt, custom_pub_pv_of_public_sector_ext_debt_end_of_period=self.custom_pub_pv_of_public_sector_ext_debt_end_of_period)

    @cached_property
    def custom_pub_primary_deficit(self) -> data.Series[float | str | None]:
        return internals.custom_pub_primary_deficit(custom_pub_revenue_grants_by_year=self.custom_pub_revenue_grants_by_year, custom_pub_primary_noninterest_expenditure_by_year=self.custom_pub_primary_noninterest_expenditure_by_year)

    @cached_property
    def custom_pub_revenue_grants_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_pub_revenue_grants_by_year(custom_pub_revenue_grants=self.custom_pub_revenue_grants, custom_pub_grants=self.custom_pub_grants, custom_pub_of_which_grants=self.custom_pub_of_which_grants)

    @cached_property
    def custom_pub_of_which_grants(self) -> data.Series[float | str | None]:
        return internals.custom_pub_of_which_grants(custom_pub_grants=self.custom_pub_grants, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc, custom_pub_nominal_gdp_lc_custom=self.custom_pub_nominal_gdp_lc_custom)

    @cached_property
    def custom_pub_primary_noninterest_expenditure_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_pub_primary_noninterest_expenditure_by_year(custom_pub_primary_noninterest_expenditure=self.custom_pub_primary_noninterest_expenditure, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc, custom_pub_nominal_gdp_lc_custom=self.custom_pub_nominal_gdp_lc_custom)

    @cached_property
    def custom_pub_contribution_from_real_exchange_rate(self) -> data.Series[float | str | None]:
        return internals.custom_pub_contribution_from_real_exchange_rate(custom_pub_of_which_fx_denominated=self.custom_pub_of_which_fx_denominated, custom_pub_denominator_1_g=self.custom_pub_denominator_1_g, custom_pub_average_real_interest_rate_ext_debt=self.custom_pub_average_real_interest_rate_ext_debt, custom_pub_real_exchange_rate_depreciation_pct_indicates=self.custom_pub_real_exchange_rate_depreciation_pct_indicates)

    @cached_property
    def custom_pub_denominator_1_g(self) -> data.Series[float | str | None]:
        return internals.custom_pub_denominator_1_g(custom_pub_real_gdp_growth_by_year=self.custom_pub_real_gdp_growth_by_year)

    @cached_property
    def custom_pub_other_identified_debt_creating_flows(self) -> data.Series[float | str | None]:
        return internals.custom_pub_other_identified_debt_creating_flows(custom_pub_privatization_receipts_negative=self.custom_pub_privatization_receipts_negative, custom_pub_recognition_of_contingent_liab_e_g_bank=self.custom_pub_recognition_of_contingent_liab_e_g_bank, custom_pub_debt_relief_hipc_other=self.custom_pub_debt_relief_hipc_other, custom_pub_other_debt_creating_reducing_flow_please_specify=self.custom_pub_other_debt_creating_reducing_flow_please_specify)

    @cached_property
    def custom_pub_privatization_receipts_negative(self) -> data.Series[float | str | None]:
        return internals.custom_pub_privatization_receipts_negative(baseline_pub_privatization_receipts_negative=self.baseline_pub_privatization_receipts_negative, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc)

    @cached_property
    def custom_pub_recognition_of_contingent_liab_e_g_bank(self) -> data.Series[int | str | None]:
        return internals.custom_pub_recognition_of_contingent_liab_e_g_bank(baseline_pub_recognition_of_contingent_liab_e_g_bank=self.baseline_pub_recognition_of_contingent_liab_e_g_bank, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc)

    @cached_property
    def custom_pub_debt_relief_hipc_other(self) -> data.Series[int | str | None]:
        return internals.custom_pub_debt_relief_hipc_other(baseline_pub_debt_relief_hipc_other=self.baseline_pub_debt_relief_hipc_other, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc)

    @cached_property
    def custom_pub_other_debt_creating_reducing_flow_please_specify(self) -> data.Series[int | str | None]:
        return internals.custom_pub_other_debt_creating_reducing_flow_please_specify(customized_public_template_anchor=self.customized_public_template_anchor, customized_public_natural_disaster_year=self.customized_public_natural_disaster_year, baseline_pub_other_debt_creating_reducing_flow_please_specify=self.baseline_pub_other_debt_creating_reducing_flow_please_specify, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, custom_pub_please_do_not_change_these_numbers=self.custom_pub_please_do_not_change_these_numbers, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc, customized_scenario_spec=self.customized_scenario_spec)

    @cached_property
    def custom_pub_residual(self) -> data.Series[float | str | None]:
        return internals.custom_pub_residual(baseline_pub_residual=self.baseline_pub_residual, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc)

    @cached_property
    def custom_pub_nominal_gdp_lc(self) -> data.Series[float | str | None]:
        return internals.custom_pub_nominal_gdp_lc(custom_pub_real_gdp_growth_by_year=self.custom_pub_real_gdp_growth_by_year, macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc, custom_pub_inflation_rate_gdp_deflator_pct_by_year=self.custom_pub_inflation_rate_gdp_deflator_pct_by_year)

    @cached_property
    def custom_pub_real_gdp_growth_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_pub_real_gdp_growth_by_year(customized_public_template_anchor=self.customized_public_template_anchor, customized_public_natural_disaster_year=self.customized_public_natural_disaster_year, custom_pub_please_do_not_change_these_numbers=self.custom_pub_please_do_not_change_these_numbers, custom_pub_real_gdp_growth=self.custom_pub_real_gdp_growth, customized_scenario_spec=self.customized_scenario_spec)

    @cached_property
    def custom_pub_average_nominal_interest_rate_ext_debt(self) -> data.Series[float | str | None]:
        return internals.custom_pub_average_nominal_interest_rate_ext_debt(custom_pub_total_public_ext_debt=self.custom_pub_total_public_ext_debt, custom_pub_ext_debt=self.custom_pub_ext_debt, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def custom_pub_average_real_interest_rate_ext_debt(self) -> data.Series[float | str | None]:
        return internals.custom_pub_average_real_interest_rate_ext_debt(custom_pub_average_nominal_interest_rate_ext_debt=self.custom_pub_average_nominal_interest_rate_ext_debt, custom_pub_us_inflation_rate_gdp_deflator_pct=self.custom_pub_us_inflation_rate_gdp_deflator_pct)

    @cached_property
    def custom_pub_exchange_rate_lc_per_us_dollar(self) -> data.Series[float | str | None]:
        return internals.custom_pub_exchange_rate_lc_per_us_dollar(custom_pub_key_macroeconomic_fiscal_exchange_rate_lc_per_us_dollar=self.custom_pub_key_macroeconomic_fiscal_exchange_rate_lc_per_us_dollar, custom_pub_nominal_depreciation_of_lc_percentage_change_lc_by_year=self.custom_pub_nominal_depreciation_of_lc_percentage_change_lc_by_year)

    @cached_property
    def custom_pub_exchange_rate_us_dollar_per_lc(self) -> data.Series[float | str | None]:
        return internals.custom_pub_exchange_rate_us_dollar_per_lc(custom_pub_key_macroeconomic_fiscal_exchange_rate_lc_per_us_dollar=self.custom_pub_key_macroeconomic_fiscal_exchange_rate_lc_per_us_dollar, custom_pub_exchange_rate_lc_per_us_dollar=self.custom_pub_exchange_rate_lc_per_us_dollar)

    @cached_property
    def custom_pub_real_exchange_rate_depreciation_pct_indicates(self) -> data.Series[float | str | None]:
        return internals.custom_pub_real_exchange_rate_depreciation_pct_indicates(custom_pub_inflation_rate_gdp_deflator_pct_by_year=self.custom_pub_inflation_rate_gdp_deflator_pct_by_year, custom_pub_nominal_depreciation_of_lc_percentage_change_lc_by_year=self.custom_pub_nominal_depreciation_of_lc_percentage_change_lc_by_year, custom_pub_us_inflation_rate_gdp_deflator_pct=self.custom_pub_us_inflation_rate_gdp_deflator_pct)

    @cached_property
    def custom_pub_total_public_ext_debt(self) -> data.Series[float | str | None]:
        return internals.custom_pub_total_public_ext_debt(custom_pub_key_macroeconomic_fiscal_exchange_rate_lc_per_us_dollar=self.custom_pub_key_macroeconomic_fiscal_exchange_rate_lc_per_us_dollar, custom_pub_stock_of_new_forex_debt=self.custom_pub_stock_of_new_forex_debt, custom_pub_exchange_rate_lc_per_us_dollar=self.custom_pub_exchange_rate_lc_per_us_dollar, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar, macro_debt_total_public_ext_debt=self.macro_debt_total_public_ext_debt)

    @cached_property
    def custom_pub_primary_deficit_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_pub_primary_deficit_by_year(custom_pub_primary_deficit=self.custom_pub_primary_deficit, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc)

    @cached_property
    def custom_pub_pv_of_public_sector_ext_debt_end_of_period(self) -> data.Series[float | str | None]:
        return internals.custom_pub_pv_of_public_sector_ext_debt_end_of_period(baseline_pub_exchange_rate_lc_per_us_dollar=self.baseline_pub_exchange_rate_lc_per_us_dollar, custom_pub_pv_of_new_forex_debt=self.custom_pub_pv_of_new_forex_debt, custom_pub_exchange_rate_lc_per_us_dollar=self.custom_pub_exchange_rate_lc_per_us_dollar, macro_debt_pv_of_public_sector_ext_debt_end_of_period=self.macro_debt_pv_of_public_sector_ext_debt_end_of_period)

    @cached_property
    def custom_pub_other_debt_creating_flows(self) -> data.Series[float | str | None]:
        return internals.custom_pub_other_debt_creating_flows(baseline_pub_other_identified_debt_creating_flows=self.baseline_pub_other_identified_debt_creating_flows, baseline_pub_nominal_gdp_lc=self.baseline_pub_nominal_gdp_lc)

    @cached_property
    def custom_pub_debt_service_revenue_grants_ratio(self) -> data.Series[float | str | None]:
        return internals.custom_pub_debt_service_revenue_grants_ratio(custom_pub_in_billions_of_lc_of_which_short_term=self.custom_pub_in_billions_of_lc_of_which_short_term, custom_pub_revenue_grants_by_year=self.custom_pub_revenue_grants_by_year, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc, custom_pub_of_which_short_term=self.custom_pub_of_which_short_term, custom_pub_amortization_excluding_st_domestic_debt=self.custom_pub_amortization_excluding_st_domestic_debt, custom_pub_interest_expenditure=self.custom_pub_interest_expenditure)

    @cached_property
    def custom_pub_debt_service_gdp_ratio(self) -> data.Series[float | str | None]:
        return internals.custom_pub_debt_service_gdp_ratio(custom_pub_in_billions_of_lc_of_which_short_term=self.custom_pub_in_billions_of_lc_of_which_short_term, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc, custom_pub_of_which_short_term=self.custom_pub_of_which_short_term, custom_pub_amortization_excluding_st_domestic_debt=self.custom_pub_amortization_excluding_st_domestic_debt, custom_pub_interest_expenditure=self.custom_pub_interest_expenditure)

    @cached_property
    def custom_pub_pv_of_public_debt_revenue_grants_ratio(self) -> data.Series[float | str | None]:
        return internals.custom_pub_pv_of_public_debt_revenue_grants_ratio(custom_pub_pv_of_public_debt_gdp_ratio=self.custom_pub_pv_of_public_debt_gdp_ratio, custom_pub_revenue_grants_by_year=self.custom_pub_revenue_grants_by_year)

    @cached_property
    def custom_pub_nominal_gdp_lc_custom(self) -> data.Series[float | str | None]:
        return internals.custom_pub_nominal_gdp_lc_custom(custom_pub_real_gdp_growth=self.custom_pub_real_gdp_growth, custom_pub_nominal_gdp_lc=self.custom_pub_nominal_gdp_lc, custom_pub_inflation_rate_gdp_deflator_pct_by_year=self.custom_pub_inflation_rate_gdp_deflator_pct_by_year)

    @cached_property
    def custom_ext_period(self) -> data.Series[int | str | None]:
        return internals.custom_ext_period(customized_external_debt_profile_period=self.customized_external_debt_profile_period)

    @cached_property
    def custom_ext_debt_stock(self) -> data.Series[float | str | None]:
        return internals.custom_ext_debt_stock(customized_external_debt_profile_disbursement=self.customized_external_debt_profile_disbursement, custom_ext_amortization=self.custom_ext_amortization)

    @cached_property
    def custom_ext_amortization(self) -> data.Series[float | str | None]:
        return internals.custom_ext_amortization(customized_external_debt_profile_period=self.customized_external_debt_profile_period, customized_external_debt_profile_disbursement=self.customized_external_debt_profile_disbursement, custom_ext_period=self.custom_ext_period, custom_ext_average_interest_rate_new_debt_by_row=self.custom_ext_average_interest_rate_new_debt_by_row)

    @cached_property
    def custom_ext_interest(self) -> data.Series[float | str | None]:
        return internals.custom_ext_interest(custom_ext_average_interest_rate_new_debt_by_row=self.custom_ext_average_interest_rate_new_debt_by_row, custom_ext_debt_stock=self.custom_ext_debt_stock)

    @cached_property
    def custom_ext_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.custom_ext_total_debt_service(custom_ext_amortization=self.custom_ext_amortization, custom_ext_interest=self.custom_ext_interest)

    @cached_property
    def custom_ext_pv_debt(self) -> int | str:
        return internals.custom_ext_pv_debt(custom_ext_debt_stock=self.custom_ext_debt_stock, custom_ext_total_debt_service=self.custom_ext_total_debt_service, custom_ext_average_interest_rate_new_debt_by_row=self.custom_ext_average_interest_rate_new_debt_by_row)

    @cached_property
    def custom_ext_new_forex_borrowing_gross_usd(self) -> data.Series[float | str | None]:
        return internals.custom_ext_new_forex_borrowing_gross_usd(custom_pub_amortization=self.custom_pub_amortization, custom_ext_residual_gross_borrowing=self.custom_ext_residual_gross_borrowing)

    @cached_property
    def custom_ext_cumulative(self) -> data.Series[float | str | None]:
        return internals.custom_ext_cumulative(custom_ext_new_forex_borrowing_gross_usd=self.custom_ext_new_forex_borrowing_gross_usd)

    @cached_property
    def custom_ext_stock_of_new_forex_debt(self) -> data.Series[float | str | None]:
        return internals.custom_ext_stock_of_new_forex_debt(custom_ext_new_forex_borrowing_gross_usd=self.custom_ext_new_forex_borrowing_gross_usd, custom_ext_amortization_by_year=self.custom_ext_amortization_by_year)

    @cached_property
    def custom_ext_pv_of_new_forex_debt(self) -> data.Series[float | str | None]:
        return internals.custom_ext_pv_of_new_forex_debt(custom_ext_pv_debt=self.custom_ext_pv_debt, custom_ext_new_forex_borrowing_gross_usd=self.custom_ext_new_forex_borrowing_gross_usd, custom_ext_total_debt_service_by_year=self.custom_ext_total_debt_service_by_year, custom_ext_amortization_by_year=self.custom_ext_amortization_by_year, custom_ext_average_interest_rate_new_debt_by_row=self.custom_ext_average_interest_rate_new_debt_by_row)

    @cached_property
    def custom_ext_total_debt_service_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_ext_total_debt_service_by_year(custom_ext_interest_by_year=self.custom_ext_interest_by_year, custom_ext_amortization_by_year=self.custom_ext_amortization_by_year)

    @cached_property
    def custom_ext_interest_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_ext_interest_by_year(custom_ext_average_interest_rate_new_debt_by_row=self.custom_ext_average_interest_rate_new_debt_by_row, custom_ext_new_forex_borrowing_gross_usd=self.custom_ext_new_forex_borrowing_gross_usd, custom_ext_stock_of_new_forex_debt=self.custom_ext_stock_of_new_forex_debt)

    @cached_property
    def custom_ext_amortization_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_ext_amortization_by_year(custom_ext_short_name=self.custom_ext_short_name, custom_ext_short_name_by_year=self.custom_ext_short_name_by_year, custom_ext_average_interest_rate_new_debt_by_row=self.custom_ext_average_interest_rate_new_debt_by_row)

    @cached_property
    def custom_ext_t_g_0(self) -> data.Series[int | str | None]:
        return internals.custom_ext_t_g_0(customized_external_debt_profile_period=self.customized_external_debt_profile_period, custom_ext_period=self.custom_ext_period, custom_ext_average_interest_rate_new_debt_by_row=self.custom_ext_average_interest_rate_new_debt_by_row)

    @cached_property
    def custom_ext_short_name(self) -> data.Series[float | str | None]:
        return internals.custom_ext_short_name(custom_ext_short_name_cumulative=self.custom_ext_short_name_cumulative, customized_external_new_forex_borrowing_cumulative_overflow=self.customized_external_new_forex_borrowing_cumulative_overflow, custom_ext_cumulative=self.custom_ext_cumulative, custom_ext_t_g_0=self.custom_ext_t_g_0)

    @cached_property
    def custom_ext_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.custom_ext_t_m_condition(customized_external_debt_profile_period=self.customized_external_debt_profile_period, custom_ext_period=self.custom_ext_period, custom_ext_average_interest_rate_new_debt_by_row=self.custom_ext_average_interest_rate_new_debt_by_row)

    @cached_property
    def custom_ext_short_name_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_ext_short_name_by_year(custom_ext_short_name_cumulative=self.custom_ext_short_name_cumulative, custom_ext_cumulative=self.custom_ext_cumulative, custom_ext_t_m_condition=self.custom_ext_t_m_condition)

    @cached_property
    def custom_ext_pv_ppg_ext_debt_gdp_ratio(self) -> data.Series[float | str | None]:
        return internals.custom_ext_pv_ppg_ext_debt_gdp_ratio(custom_ext_nominal_gdp_million_of_us_dollars=self.custom_ext_nominal_gdp_million_of_us_dollars, custom_ext_pv_ppg_stress=self.custom_ext_pv_ppg_stress)

    @cached_property
    def custom_ext_pv_ppg_ext_debt_exports_ratio(self) -> data.Series[float | str | None]:
        return internals.custom_ext_pv_ppg_ext_debt_exports_ratio(custom_ext_pv_ppg_ext_debt_gdp_ratio=self.custom_ext_pv_ppg_ext_debt_gdp_ratio, custom_ext_exports_by_year=self.custom_ext_exports_by_year)

    @cached_property
    def custom_ext_ppg_debt_service_to_exports(self) -> data.Series[float | str | None]:
        return internals.custom_ext_ppg_debt_service_to_exports(custom_ext_ppg_debt_service_stress=self.custom_ext_ppg_debt_service_stress, custom_ext_y7_long_run_constant_exports=self.custom_ext_y7_long_run_constant_exports)

    @cached_property
    def custom_ext_ppg_debt_service_to_revenue(self) -> data.Series[float | str | None]:
        return internals.custom_ext_ppg_debt_service_to_revenue(custom_ext_ppg_debt_service_stress=self.custom_ext_ppg_debt_service_stress, custom_ext_revenue=self.custom_ext_revenue)

    @cached_property
    def custom_ext_nominal_gdp_million_of_us_dollars(self) -> data.Series[float | str | None]:
        return internals.custom_ext_nominal_gdp_million_of_us_dollars(custom_ext_ii_key_macroeconomic_nominal_gdp_million_of_us_dollars=self.custom_ext_ii_key_macroeconomic_nominal_gdp_million_of_us_dollars, custom_ext_real_gdp_growth_by_year=self.custom_ext_real_gdp_growth_by_year, custom_ext_gdp_deflator_in_us_dollar_terms_change_pct_by_year=self.custom_ext_gdp_deflator_in_us_dollar_terms_change_pct_by_year)

    @cached_property
    def custom_ext_real_gdp_growth_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_ext_real_gdp_growth_by_year(customized_public_template_anchor=self.customized_public_template_anchor, customized_public_natural_disaster_year=self.customized_public_natural_disaster_year, custom_pub_please_do_not_change_these_numbers=self.custom_pub_please_do_not_change_these_numbers, custom_ext_real_gdp_growth=self.custom_ext_real_gdp_growth, customized_scenario_spec=self.customized_scenario_spec)

    @cached_property
    def custom_ext_pv_ppg_stress(self) -> data.Series[float | str | None]:
        return internals.custom_ext_pv_ppg_stress(custom_ext_pv_of_additional_borrowing=self.custom_ext_pv_of_additional_borrowing, custom_ext_pv_ppg_baseline=self.custom_ext_pv_ppg_baseline)

    @cached_property
    def custom_ext_ppg_debt_service_stress(self) -> data.Series[float | str | None]:
        return internals.custom_ext_ppg_debt_service_stress(custom_ext_additional_debt_service_stress=self.custom_ext_additional_debt_service_stress, custom_ext_debt_service_ppg_baseline=self.custom_ext_debt_service_ppg_baseline)

    @cached_property
    def custom_ext_y7_long_run_constant_exports(self) -> data.Series[float | str | None]:
        return internals.custom_ext_y7_long_run_constant_exports(custom_ext_nominal_gdp_million_of_us_dollars=self.custom_ext_nominal_gdp_million_of_us_dollars, custom_ext_exports_by_year=self.custom_ext_exports_by_year)

    @cached_property
    def custom_ext_revenue(self) -> data.Series[float | str | None]:
        return internals.custom_ext_revenue(custom_pub_revenue_grants=self.custom_pub_revenue_grants, custom_pub_grants=self.custom_pub_grants, custom_ext_nominal_gdp_million_of_us_dollars=self.custom_ext_nominal_gdp_million_of_us_dollars)

    @cached_property
    def custom_ext_ppg_nominal_debt_baseline(self) -> data.Series[float | str | None]:
        return internals.custom_ext_ppg_nominal_debt_baseline(dsa_ext_nominal_gdp_million_of_us_dollars=self.dsa_ext_nominal_gdp_million_of_us_dollars, dsa_ext_of_which_public_and_publicly_guaranteed_ppg=self.dsa_ext_of_which_public_and_publicly_guaranteed_ppg)

    @cached_property
    def custom_ext_increase(self) -> data.Series[float | str | None]:
        return internals.custom_ext_increase(custom_ext_ppg_nominal_debt_baseline=self.custom_ext_ppg_nominal_debt_baseline)

    @cached_property
    def custom_ext_ppg_nominal_debt_stress(self) -> data.Series[float | str | None]:
        return internals.custom_ext_ppg_nominal_debt_stress(custom_ext_ii_key_macroeconomic_nominal_gdp_million_of_us_dollars=self.custom_ext_ii_key_macroeconomic_nominal_gdp_million_of_us_dollars, custom_ext_nominal_gdp_million_of_us_dollars=self.custom_ext_nominal_gdp_million_of_us_dollars, custom_ext_of_which_public_publicly_guaranteed_ppg=self.custom_ext_of_which_public_publicly_guaranteed_ppg)

    @cached_property
    def custom_ext_increase_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_ext_increase_by_year(custom_ext_ppg_nominal_debt_stress=self.custom_ext_ppg_nominal_debt_stress)

    @cached_property
    def custom_ext_residual_gross_borrowing(self) -> data.Series[float | str | None]:
        return internals.custom_ext_residual_gross_borrowing(custom_ext_increase=self.custom_ext_increase, custom_ext_increase_by_year=self.custom_ext_increase_by_year)

    @cached_property
    def _scan_custom_ext_exports_usd(self) -> internals.ScanCustomExtExportsUsdResult:
        return internals.scan_custom_ext_exports_usd(dsa_ext_exports=self.dsa_ext_exports, customized_public_template_anchor=self.customized_public_template_anchor, customized_public_natural_disaster_year=self.customized_public_natural_disaster_year, custom_pub_please_do_not_change_these_numbers=self.custom_pub_please_do_not_change_these_numbers, custom_ext_nominal_gdp_million_of_us_dollars=self.custom_ext_nominal_gdp_million_of_us_dollars, custom_ext_nominal_gdp_million_of_us_dollars_by_year=self.custom_ext_nominal_gdp_million_of_us_dollars_by_year, custom_ext_exports=self.custom_ext_exports, customized_scenario_spec=self.customized_scenario_spec, custom_ext_ii_key_macroeconomic_nominal_gdp_million_of_us_dollars=self.custom_ext_ii_key_macroeconomic_nominal_gdp_million_of_us_dollars)

    @cached_property
    def custom_ext_exports_usd(self) -> data.Series[float | str | None]:
        return self._scan_custom_ext_exports_usd.custom_ext_exports_usd

    @cached_property
    def custom_ext_exports_growth(self) -> data.Series[float | str | None]:
        return self._scan_custom_ext_exports_usd.custom_ext_exports_growth

    @cached_property
    def custom_ext_exports_usd_stress(self) -> data.Series[float | str | None]:
        return self._scan_custom_ext_exports_usd.custom_ext_exports_usd_stress

    @cached_property
    def custom_ext_exports_in_of_gdp_stress(self) -> data.Series[float | str | None]:
        return self._scan_custom_ext_exports_usd.custom_ext_exports_in_of_gdp_stress

    @cached_property
    def custom_ext_exports_by_year(self) -> data.Series[float | str | None]:
        return self._scan_custom_ext_exports_usd.custom_ext_exports_by_year

    @cached_property
    def custom_ext_nominal_gdp_million_of_us_dollars_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_ext_nominal_gdp_million_of_us_dollars_by_year(custom_ext_y7_long_run_constant_nominal_gdp_million_of_us_dollars=self.custom_ext_y7_long_run_constant_nominal_gdp_million_of_us_dollars, custom_ext_gdp_deflator_in_us_dollar_terms_change_pct_by_year=self.custom_ext_gdp_deflator_in_us_dollar_terms_change_pct_by_year, custom_ext_real_gdp_growth=self.custom_ext_real_gdp_growth)

    @cached_property
    def in1_basics_autofill_note(self) -> str | int | float | bool:
        return internals.in1_basics_autofill_note(translation_input_1_basics_blue_cells_are_populated_automatically=data.TRANSLATION_INPUT_1_BASICS_BLUE_CELLS_ARE_POPULATED_AUTOMATICALLY, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def in1_basics_country_code(self) -> int | str:
        return internals.in1_basics_country_code(country=self.country, lookup_imf_country_code_index=data.LOOKUP_IMF_COUNTRY_CODE_INDEX, lookup_country_name=data.LOOKUP_COUNTRY_NAME, lookup_hipc_status=data.LOOKUP_HIPC_STATUS, lookup_mdri=data.LOOKUP_MDRI)

    @cached_property
    def in2_coverage_ppp(self) -> float | str:
        return internals.in2_coverage_ppp(in2_coverage_y1_ppp_capital_stock_from_world_bank_s_ppp=self.in2_coverage_y1_ppp_capital_stock_from_world_bank_s_ppp, in2_coverage_y3_size_of_ppp_shock_pct_gdp_1_2=self.in2_coverage_y3_size_of_ppp_shock_pct_gdp_1_2)

    @cached_property
    def in2_coverage_y1_ppp_capital_stock_from_world_bank_s_ppp(self) -> float | str:
        return internals.in2_coverage_y1_ppp_capital_stock_from_world_bank_s_ppp(trigger_country_flags=data.TRIGGER_COUNTRY_FLAGS, trigger_left_headers=data.TRIGGER_LEFT_HEADERS, trigger_ifscode=self.trigger_ifscode, trigger_isocode=self.trigger_isocode, trigger_country_name=self.trigger_country_name, trigger_ppp_year=self.trigger_ppp_year, trigger_ppp_stocks=self.trigger_ppp_stocks, in1_basics_country_code=self.in1_basics_country_code)

    @cached_property
    def in2_coverage_y3_size_of_ppp_shock_pct_gdp_1_2(self) -> float | str:
        return internals.in2_coverage_y3_size_of_ppp_shock_pct_gdp_1_2(ppp_capital_stock_shock_pct=self.ppp_capital_stock_shock_pct, in2_coverage_y1_ppp_capital_stock_from_world_bank_s_ppp=self.in2_coverage_y1_ppp_capital_stock_from_world_bank_s_ppp)

    @cached_property
    def in3_macro_outstanding(self) -> float | str:
        return internals.in3_macro_outstanding(external_domestic_debt_definition=self.external_domestic_debt_definition, input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p=self.input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p, input3_domestic_outstanding_of_existing_debt=self.input3_domestic_outstanding_of_existing_debt, lookup_afg=self.lookup_afg)

    @cached_property
    def in3_macro_o_w_medium_long_term(self) -> float | str:
        return internals.in3_macro_o_w_medium_long_term(in3_macro_outstanding=self.in3_macro_outstanding, in3_macro_o_w_st=self.in3_macro_o_w_st)

    @cached_property
    def in3_macro_o_w_st(self) -> data.Series[float | str | None]:
        return internals.in3_macro_o_w_st(external_domestic_debt_definition=self.external_domestic_debt_definition, input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p=self.input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p, input3_domestic_o_w_st=self.input3_domestic_o_w_st, lookup_afg=self.lookup_afg)

    @cached_property
    def in3_macro_transition_formula_these_outstanding(self) -> float | str:
        return internals.in3_macro_transition_formula_these_outstanding(external_domestic_debt_definition=self.external_domestic_debt_definition, input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p=self.input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p, input3_domestic_outstanding_of_existing_debt=self.input3_domestic_outstanding_of_existing_debt, lookup_afg=self.lookup_afg)

    @cached_property
    def in3_macro_transition_formula_these_o_w_medium_long_term(self) -> float | str:
        return internals.in3_macro_transition_formula_these_o_w_medium_long_term(in3_macro_transition_formula_these_outstanding=self.in3_macro_transition_formula_these_outstanding, in3_macro_transition_formula_these_o_w_st=self.in3_macro_transition_formula_these_o_w_st)

    @cached_property
    def in3_macro_transition_formula_these_o_w_st(self) -> int | str:
        return internals.in3_macro_transition_formula_these_o_w_st(external_domestic_debt_definition=self.external_domestic_debt_definition, input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p=self.input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p, input3_domestic_o_w_st=self.input3_domestic_o_w_st, lookup_afg=self.lookup_afg)

    @cached_property
    def in3_macro_interest(self) -> data.Series[float | str | None]:
        return internals.in3_macro_interest(external_domestic_debt_definition=self.external_domestic_debt_definition, input3_input_3_macro_national_currency_per_u_s_dollar_p_a=self.input3_input_3_macro_national_currency_per_u_s_dollar_p_a, input3_domestic_interest_payment_from_existing_debt=self.input3_domestic_interest_payment_from_existing_debt, lookup_afg=self.lookup_afg)

    @cached_property
    def in3_macro_fx_denominated_debt_including_locally_issued(self) -> float | str:
        return internals.in3_macro_fx_denominated_debt_including_locally_issued(input3_input_3_external_debt_ppg_mlt_external_debt_outstanding=self.input3_input_3_external_debt_ppg_mlt_external_debt_outstanding, input3_input_3_external_debt_ppg_st_external_debt_outstanding=self.input3_input_3_external_debt_ppg_st_external_debt_outstanding, input3_domestic_outstanding_of_existing_debt=self.input3_domestic_outstanding_of_existing_debt)

    @cached_property
    def in6_tailored_natdisaster(self) -> str | int | float | bool:
        return internals.in6_tailored_natdisaster(trigger_natural_disaster_sample=data.TRIGGER_NATURAL_DISASTER_SAMPLE, country=self.country)

    @cached_property
    def in6_tailored_commodity_price(self) -> str | int | float | bool:
        return internals.in6_tailored_commodity_price(input6_tailored_tests_enabled=self.input6_tailored_tests_enabled, in6_tailored_share_of_commodities_in_total_exports_of_goods=self.in6_tailored_share_of_commodities_in_total_exports_of_goods)

    @cached_property
    def in6_tailored_mkt_financing(self) -> str | int | float | bool:
        return internals.in6_tailored_mkt_financing(trigger_right_headers=data.TRIGGER_RIGHT_HEADERS, input6_tailored_tests_enabled=self.input6_tailored_tests_enabled, trigger_market_access_country_code=self.trigger_market_access_country_code, trigger_market_access=self.trigger_market_access, in1_basics_country_code=self.in1_basics_country_code)

    @cached_property
    def in6_tailored_share_of_commodities_in_total_exports_of_goods(self) -> float | str:
        return internals.in6_tailored_share_of_commodities_in_total_exports_of_goods(input6_tailored_params_2=self.input6_tailored_params_2)

    @cached_property
    def in6_tailored_adjusted_share_of_commodities_in_total_exports(self) -> float | str:
        return internals.in6_tailored_adjusted_share_of_commodities_in_total_exports(in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s=self.in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s, in6_tailored_adjusted_share_of_non_fuel_in_exports_of_g_s=self.in6_tailored_adjusted_share_of_non_fuel_in_exports_of_g_s)

    @cached_property
    def _scan_in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s(self) -> internals.ScanIn6TailoredAdjustedShareOfFuelInExportsOfGSResult:
        return internals.scan_in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s(input6_tailored_tests_enabled=self.input6_tailored_tests_enabled, in6_tailored_price_shock_non_fuel=self.in6_tailored_price_shock_non_fuel, in6_tailored_natdisaster_shock_size_default=self.in6_tailored_natdisaster_shock_size_default, in6_tailored_commodity_close_gap_default=self.in6_tailored_commodity_close_gap_default, in6_tailored_share_of_fuel_in_exports_of_g_s_default=self.in6_tailored_share_of_fuel_in_exports_of_g_s_default, in6_tailored_share_of_non_fuel_in_exports_of_g_s_default=self.in6_tailored_share_of_non_fuel_in_exports_of_g_s_default, in6_tailored_mitigating_factor_fuel_default=self.in6_tailored_mitigating_factor_fuel_default, in6_tailored_mitigating_factor_non_fuel_default=self.in6_tailored_mitigating_factor_non_fuel_default, in6_tailored_mkt_fin_borrowing_cost_default=self.in6_tailored_mkt_fin_borrowing_cost_default, in6_tailored_mkt_fin_maturity_defaults=self.in6_tailored_mkt_fin_maturity_defaults, in6_tailored_mkt_fin_fx_depreciation_default=self.in6_tailored_mkt_fin_fx_depreciation_default, input6_tailored_params_fuel_label=self.input6_tailored_params_fuel_label)

    @cached_property
    def in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s(self) -> data.Series[float | str | None]:
        return self._scan_in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s.in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s

    @cached_property
    def in6_tailored_adjusted_share_of_non_fuel_in_exports_of_g_s(self) -> data.Series[float | str | None]:
        return self._scan_in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s.in6_tailored_adjusted_share_of_non_fuel_in_exports_of_g_s

    @cached_property
    def in6_tailored_average_of_prices_shock_default(self) -> float | str:
        return self._scan_in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s.in6_tailored_average_of_prices_shock_default

    @cached_property
    def input6_tailored_params_2(self) -> data.Series[float | str | None]:
        return self._scan_in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s.input6_tailored_params_2

    @cached_property
    def in6_tailored_price_shock_non_fuel(self) -> data.Series[float | str | None]:
        return internals.in6_tailored_price_shock_non_fuel(in6_tailored_commodity_group_price_shock=self.in6_tailored_commodity_group_price_shock)

    @cached_property
    def in6_tailored_commodity_group_price_shock(self) -> data.Series[float | str | None]:
        return internals.in6_tailored_commodity_group_price_shock(input6_commodity_group_relevant=self.input6_commodity_group_relevant, imported_commodity_prices=self.imported_commodity_prices)

    @cached_property
    def in6_tailored_natdisaster_shock_size_default(self) -> float | str:
        return internals.in6_tailored_natdisaster_shock_size_default(input6_tailored_tests_enabled=self.input6_tailored_tests_enabled)

    @cached_property
    def in6_tailored_natdisaster_interaction_defaults(self) -> data.Series[float | str | None]:
        return internals.in6_tailored_natdisaster_interaction_defaults(input6_tailored_tests_enabled=self.input6_tailored_tests_enabled)

    @cached_property
    def in6_tailored_commodity_close_gap_default(self) -> float | str:
        return internals.in6_tailored_commodity_close_gap_default(input6_tailored_tests_enabled=self.input6_tailored_tests_enabled)

    @cached_property
    def in6_tailored_commodity_interaction_defaults(self) -> data.Series[float | str | None]:
        return internals.in6_tailored_commodity_interaction_defaults(in6_tailored_average_of_prices_shock_default=self.in6_tailored_average_of_prices_shock_default, input6_tailored_tests_enabled=self.input6_tailored_tests_enabled)

    @cached_property
    def in6_tailored_share_of_fuel_in_exports_of_g_s_default(self) -> float | str:
        return internals.in6_tailored_share_of_fuel_in_exports_of_g_s_default(macro_debt_share_of_commodity_exports_fuel_of_exports_of_g=self.macro_debt_share_of_commodity_exports_fuel_of_exports_of_g)

    @cached_property
    def in6_tailored_share_of_non_fuel_in_exports_of_g_s_default(self) -> float | str:
        return internals.in6_tailored_share_of_non_fuel_in_exports_of_g_s_default(macro_debt_share_of_commodity_exports_non_fuel_of_exports=self.macro_debt_share_of_commodity_exports_non_fuel_of_exports)

    @cached_property
    def in6_tailored_mitigating_factor_fuel_default(self) -> float | str:
        return internals.in6_tailored_mitigating_factor_fuel_default(macro_debt_share_of_commodity_imports_fuel_of_exports_of_g=self.macro_debt_share_of_commodity_imports_fuel_of_exports_of_g)

    @cached_property
    def in6_tailored_mitigating_factor_non_fuel_default(self) -> float | str:
        return internals.in6_tailored_mitigating_factor_non_fuel_default(macro_debt_share_of_commodity_imports_non_fuel_of_exports=self.macro_debt_share_of_commodity_imports_non_fuel_of_exports)

    @cached_property
    def in6_tailored_mkt_fin_borrowing_cost_default(self) -> float | str:
        return internals.in6_tailored_mkt_fin_borrowing_cost_default(input6_tailored_tests_enabled=self.input6_tailored_tests_enabled)

    @cached_property
    def in6_tailored_mkt_fin_maturity_defaults(self) -> data.Series[float | str | None]:
        return internals.in6_tailored_mkt_fin_maturity_defaults(input6_tailored_tests_enabled=self.input6_tailored_tests_enabled)

    @cached_property
    def in6_tailored_mkt_fin_fx_depreciation_default(self) -> float | str:
        return internals.in6_tailored_mkt_fin_fx_depreciation_default(input6_tailored_tests_enabled=self.input6_tailored_tests_enabled)

    @cached_property
    def in6_tailored_mkt_fin_fx_passthrough_default(self) -> float | str:
        return internals.in6_tailored_mkt_fin_fx_passthrough_default(input6_tailored_tests_enabled=self.input6_tailored_tests_enabled)

    @cached_property
    def in6opt_standard_scenario(self) -> int | str:
        return internals.in6opt_standard_scenario(lookup_ida_terms_old=data.LOOKUP_IDA_TERMS_OLD, lookup_onoff_off=data.LOOKUP_ONOFF_OFF, input6_tailored_tests_enabled=self.input6_tailored_tests_enabled, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, input6_standard_interactions=self.input6_standard_interactions)

    @cached_property
    def in6opt_standard_historical_average_baseline_projection(self) -> str | int | float | bool:
        return internals.in6opt_standard_historical_average_baseline_projection(input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_b1_real_gdp_growth_historical_average_baseline_projection(self) -> str | int | float | bool:
        return internals.in6opt_standard_b1_real_gdp_growth_historical_average_baseline_projection(input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_b3_exports_historical_average_baseline_projection(self) -> str | int | float | bool:
        return internals.in6opt_standard_b3_exports_historical_average_baseline_projection(input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_historical_average_baseline_projection_current_transfers_b4_other_non_debt_creating_flows(self) -> str | int | float | bool:
        return internals.in6opt_standard_historical_average_baseline_projection_current_transfers_b4_other_non_debt_creating_flows(input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_historical_average_baseline_projection_fdi_b4_other_non_debt_creating_flows(self) -> str | int | float | bool:
        return internals.in6opt_standard_historical_average_baseline_projection_fdi_b4_other_non_debt_creating_flows(input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_one_time_30_percent_nominal_depreciation_of(self) -> int | str:
        return internals.in6opt_standard_one_time_30_percent_nominal_depreciation_of(input_1_rer_overvaluation=self.input_1_rer_overvaluation, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_nominal_depreciation_close_real_overvaluation(self) -> data.Series[float | str | None]:
        return internals.in6opt_standard_nominal_depreciation_close_real_overvaluation(input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode, baseline_pub_inflation_rate_gdp_deflator_pct=self.baseline_pub_inflation_rate_gdp_deflator_pct, in6opt_standard_one_time_30_percent_nominal_depreciation_of=self.in6opt_standard_one_time_30_percent_nominal_depreciation_of, in6opt_standard_us_inflation_default=self.in6opt_standard_us_inflation_default, input6_standard_params_2=self.input6_standard_params_2)

    @cached_property
    def in6opt_standard_apply_all_individual_shocks_b1_through_b5_half(self) -> float | str:
        return internals.in6opt_standard_apply_all_individual_shocks_b1_through_b5_half(input6_standard_params=self.input6_standard_params)

    @cached_property
    def in6opt_standard_historical_average_baseline_projection_real_gdp_b6_combination(self) -> str | int | float | bool:
        return internals.in6opt_standard_historical_average_baseline_projection_real_gdp_b6_combination(input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_size_of_exports_growth_shock_of_standard(self) -> float | str:
        return internals.in6opt_standard_size_of_exports_growth_shock_of_standard(input6_standard_params=self.input6_standard_params)

    @cached_property
    def in6opt_standard_historical_average_baseline_projection_exports_b6_combination(self) -> str | int | float | bool:
        return internals.in6opt_standard_historical_average_baseline_projection_exports_b6_combination(input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_size_of_pb_gdp_shock_of_standard_deviations(self) -> float | str:
        return internals.in6opt_standard_size_of_pb_gdp_shock_of_standard_deviations(input6_standard_params=self.input6_standard_params)

    @cached_property
    def in6opt_standard_historical_average_baseline_projection_primary_balance_b6_combination(self) -> str | int | float | bool:
        return internals.in6opt_standard_historical_average_baseline_projection_primary_balance_b6_combination(input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_other_flows_current_transfers_shock_of_standard(self) -> float | str:
        return internals.in6opt_standard_other_flows_current_transfers_shock_of_standard(input6_standard_params=self.input6_standard_params)

    @cached_property
    def in6opt_standard_historical_average_baseline_projection_current_transfers_b6_combination(self) -> str | int | float | bool:
        return internals.in6opt_standard_historical_average_baseline_projection_current_transfers_b6_combination(input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_b6_combination_other_flows_fdi_shock_of_standard_deviations(self) -> float | str:
        return internals.in6opt_standard_b6_combination_other_flows_fdi_shock_of_standard_deviations(input6_standard_params=self.input6_standard_params)

    @cached_property
    def in6opt_standard_historical_average_baseline_projection_fdi_b6_combination(self) -> str | int | float | bool:
        return internals.in6opt_standard_historical_average_baseline_projection_fdi_b6_combination(input6_standard_size_threshold_option_historical_average_only=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_HISTORICAL_AVERAGE_ONLY, input6_standard_size_threshold_option_whichever_is_lower=data.INPUT6_STANDARD_SIZE_THRESHOLD_OPTION_WHICHEVER_IS_LOWER, input6_standard_size_threshold_mode=self.input6_standard_size_threshold_mode)

    @cached_property
    def in6opt_standard_inflation_elasticity_default(self) -> float | str:
        return internals.in6opt_standard_inflation_elasticity_default(input6_standard_interactions=self.input6_standard_interactions)

    @cached_property
    def in6opt_standard_addl_borrowing_cost_default(self) -> float | str:
        return internals.in6opt_standard_addl_borrowing_cost_default(input6_standard_interactions=self.input6_standard_interactions)

    @cached_property
    def in6opt_standard_gdp_exports_elasticity_default(self) -> float | str:
        return internals.in6opt_standard_gdp_exports_elasticity_default(input6_standard_interactions=self.input6_standard_interactions)

    @cached_property
    def in6opt_standard_fx_passthrough_default(self) -> float | str:
        return internals.in6opt_standard_fx_passthrough_default(input6_standard_interactions=self.input6_standard_interactions)

    @cached_property
    def in6opt_standard_nx_elasticity_default(self) -> float | str:
        return internals.in6opt_standard_nx_elasticity_default(input6_standard_interactions=self.input6_standard_interactions)

    @cached_property
    def in6opt_standard_us_inflation_default(self) -> float | str:
        return internals.in6opt_standard_us_inflation_default(baseline_pub_us_inflation_rate_gdp_deflator_pct=self.baseline_pub_us_inflation_rate_gdp_deflator_pct, input6_standard_interactions=self.input6_standard_interactions)

    @cached_property
    def in7_resfin_domestic_st(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_domestic_st(in7_resfin_shares=self.in7_resfin_shares, input7_residual_params_sparse=self.input7_residual_params_sparse)

    @cached_property
    def in7_resfin_shares(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_shares(ext_debt_marginal_share_domestic_mlt_residual_financing=self.ext_debt_marginal_share_domestic_mlt_residual_financing, ext_debt_marginal_share_external_ppg_mlt_residual_financing=self.ext_debt_marginal_share_external_ppg_mlt_residual_financing)

    @cached_property
    def in7_resfin_shares_effective(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_shares_effective(in7_resfin_shares=self.in7_resfin_shares)

    @cached_property
    def in7_resfin_ext_mlt(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_ext_mlt(in7_resfin_ext_mlt_default=self.in7_resfin_ext_mlt_default)

    @cached_property
    def in7_resfin_ext_mlt_default(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_ext_mlt_default(ext_debt_residual_grace_period_residual_financing=self.ext_debt_residual_grace_period_residual_financing, discount_rate=self.discount_rate, ext_debt_residual_interest_rate_residual_financing=self.ext_debt_residual_interest_rate_residual_financing, ext_debt_residual_maturity_residual_financing=self.ext_debt_residual_maturity_residual_financing)

    @cached_property
    def in7_resfin_ext_mlt_override(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_ext_mlt_override(in7_resfin_ext_mlt_default=self.in7_resfin_ext_mlt_default, in7_resfin_avg_nominal_interest_rate_new_borrowing_usd_by_row=self.in7_resfin_avg_nominal_interest_rate_new_borrowing_usd_by_row)

    @cached_property
    def in7_resfin_ext_mlt_effective(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_ext_mlt_effective(in7_resfin_ext_mlt=self.in7_resfin_ext_mlt)

    @cached_property
    def in7_resfin_dom_mlt(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_dom_mlt(input5_residual_terms_average_grace_period_on_new_debt_rounded_average=self.input5_residual_terms_average_grace_period_on_new_debt_rounded_average, input5_residual_terms_average_real_interest_rate_on_new_debt_rounded_average=self.input5_residual_terms_average_real_interest_rate_on_new_debt_rounded_average, input5_residual_terms_average_maturity_of_new_debt_rounded_average=self.input5_residual_terms_average_maturity_of_new_debt_rounded_average)

    @cached_property
    def in7_resfin_dom_mlt_effective(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_dom_mlt_effective(in7_resfin_dom_mlt=self.in7_resfin_dom_mlt)

    @cached_property
    def in7_resfin_dom_st_interest(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_dom_st_interest(input5_residual_terms_average_real_interest_rate_on_new_debt_rounded_average=self.input5_residual_terms_average_real_interest_rate_on_new_debt_rounded_average)

    @cached_property
    def in7_resfin_dom_st_interest_effective(self) -> float | str:
        return internals.in7_resfin_dom_st_interest_effective(in7_resfin_dom_st_interest=self.in7_resfin_dom_st_interest)

    @cached_property
    def in8_sdr_sdr_allocation_holdings_in_million_of_usd(self) -> data.Series[int | str | None]:
        return internals.in8_sdr_sdr_allocation_holdings_in_million_of_usd(input8_sdr_stock=self.input8_sdr_stock)

    @cached_property
    def in8_sdr_interest_payments_in_million_of_usd(self) -> data.Series[int | str | None]:
        return internals.in8_sdr_interest_payments_in_million_of_usd(input8_sdr_interest_historical=self.input8_sdr_interest_historical, input8_sdr_interest=self.input8_sdr_interest, input8_sdr_interest_rate=self.input8_sdr_interest_rate, input8_sdr_stock=self.input8_sdr_stock, in8_sdr_sdr_allocation_holdings_in_million_of_usd=self.in8_sdr_sdr_allocation_holdings_in_million_of_usd)

    @cached_property
    def in8_sdr_pv_of_interest_payments_in_million_of_usd(self) -> data.Series[int | str | None]:
        return internals.in8_sdr_pv_of_interest_payments_in_million_of_usd(discount_rate=self.discount_rate, in8_sdr_sdr_interest=self.in8_sdr_sdr_interest, in8_sdr_of_end_2044=self.in8_sdr_of_end_2044)

    @cached_property
    def macro_debt_further_details(self) -> data.Series[int | str | None]:
        return internals.macro_debt_further_details(macro_debt_main_assumptions_further_details=self.macro_debt_main_assumptions_further_details)

    @cached_property
    def macro_debt_us_dollars(self) -> data.Series[float | str | None]:
        return internals.macro_debt_us_dollars(macro_debt_us_dollars_by_year=self.macro_debt_us_dollars_by_year, macro_debt_private_sector_ext_debt=self.macro_debt_private_sector_ext_debt)

    @cached_property
    def macro_debt_us_dollars_by_year(self) -> data.Series[float | str | None]:
        return internals.macro_debt_us_dollars_by_year(macro_debt_main_assumptions_us_dollars=self.macro_debt_main_assumptions_us_dollars, macro_debt_short_term=self.macro_debt_short_term)

    @cached_property
    def macro_debt_short_term(self) -> data.Series[float | str | None]:
        return internals.macro_debt_short_term(input3_ppg_external_debt_stock=data.INPUT3_PPG_EXTERNAL_DEBT_STOCK, input3_input_3_external_debt_ppg_st_external_debt_outstanding=self.input3_input_3_external_debt_ppg_st_external_debt_outstanding, ext_debt_st_total=self.ext_debt_st_total, in3_macro_transition_formula_these_o_w_st=self.in3_macro_transition_formula_these_o_w_st, input3_local_currency_external_debt=self.input3_local_currency_external_debt)

    @cached_property
    def macro_debt_private_sector_ext_debt(self) -> data.Series[float | str | None]:
        return internals.macro_debt_private_sector_ext_debt(macro_debt_private_sector_mlt_external=self.macro_debt_private_sector_mlt_external, macro_debt_private_sector_short_term=self.macro_debt_private_sector_short_term)

    @cached_property
    def macro_debt_private_sector_mlt_external(self) -> data.Series[float | str | None]:
        return internals.macro_debt_private_sector_mlt_external(input3_private_external_debt_stock=data.INPUT3_PRIVATE_EXTERNAL_DEBT_STOCK, input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding=self.input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding)

    @cached_property
    def macro_debt_private_sector_short_term(self) -> data.Series[float | str | None]:
        return internals.macro_debt_private_sector_short_term(input3_private_external_debt_stock=data.INPUT3_PRIVATE_EXTERNAL_DEBT_STOCK, input3_input_3_external_debt_private_sector_st_external_debt_outstanding=self.input3_input_3_external_debt_private_sector_st_external_debt_outstanding)

    @cached_property
    def macro_debt_national_currency(self) -> data.Series[float | str | None]:
        return internals.macro_debt_national_currency(macro_debt_public_domestic_mlt=self.macro_debt_public_domestic_mlt, macro_debt_public_domestic_st=self.macro_debt_public_domestic_st)

    @cached_property
    def macro_debt_public_domestic_mlt(self) -> data.Series[float | str | None]:
        return internals.macro_debt_public_domestic_mlt(input5_summary_mlt=self.input5_summary_mlt, in3_macro_o_w_medium_long_term=self.in3_macro_o_w_medium_long_term, input3_local_currency_domestic_debt=self.input3_local_currency_domestic_debt)

    @cached_property
    def macro_debt_public_domestic_st(self) -> data.Series[float | str | None]:
        return internals.macro_debt_public_domestic_st(input5_summary_short_term=self.input5_summary_short_term, in3_macro_o_w_st=self.in3_macro_o_w_st, input3_local_currency_domestic_debt=self.input3_local_currency_domestic_debt)

    @cached_property
    def macro_debt_total_ext_debt_interest_due_include_interest(self) -> data.Series[float | str | None]:
        return internals.macro_debt_total_ext_debt_interest_due_include_interest(macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_private_external_interest_due=self.macro_debt_private_external_interest_due)

    @cached_property
    def macro_debt_ppg_interest_due(self) -> data.Series[float | str | None]:
        return internals.macro_debt_ppg_interest_due(input3_input_3_external_debt_ppg_external_debt_interest_due=self.input3_input_3_external_debt_ppg_external_debt_interest_due, ext_debt_public_debt_service_interest=self.ext_debt_public_debt_service_interest, in3_macro_interest=self.in3_macro_interest)

    @cached_property
    def macro_debt_private_external_interest_due(self) -> data.Series[float | str | None]:
        return internals.macro_debt_private_external_interest_due(input3_input_3_external_debt_private_external_debt_interest_due=self.input3_input_3_external_debt_private_external_debt_interest_due)

    @cached_property
    def macro_debt_total_public_domestic_debt_interest_due(self) -> data.Series[float | str | None]:
        return internals.macro_debt_total_public_domestic_debt_interest_due(input5_summary_interest_payment=self.input5_summary_interest_payment, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc, input3_local_currency_domestic_debt=self.input3_local_currency_domestic_debt)

    @cached_property
    def macro_debt_total_external_amortization_due_include(self) -> data.Series[float | str | None]:
        return internals.macro_debt_total_external_amortization_due_include(macro_debt_mlt_private_ext_debt_amortization=self.macro_debt_mlt_private_ext_debt_amortization, macro_debt_main_assumptions_us_dollars_by_year_6=self.macro_debt_main_assumptions_us_dollars_by_year_6)

    @cached_property
    def macro_debt_mlt_private_ext_debt_amortization(self) -> data.Series[float | str | None]:
        return internals.macro_debt_mlt_private_ext_debt_amortization(input3_input_3_external_debt_private_mlt_external_debt_amortization_due=self.input3_input_3_external_debt_private_mlt_external_debt_amortization_due)

    @cached_property
    def macro_debt_total_mlt_public_domestic_debt_amortization_debt(self) -> data.Series[float | str | None]:
        return internals.macro_debt_total_mlt_public_domestic_debt_amortization_debt(input5_summary_principal_payment=self.input5_summary_principal_payment, macro_debt_public_domestic_st=self.macro_debt_public_domestic_st, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def macro_debt_us_dollars_k(self) -> data.Series[float | str | None]:
        return internals.macro_debt_us_dollars_k(input3_input_3_macro_current_account=self.input3_input_3_macro_current_account)

    @cached_property
    def macro_debt_us_dollars_v(self) -> data.Series[float | str | None]:
        return internals.macro_debt_us_dollars_v(input3_input_3_macro_current_account=self.input3_input_3_macro_current_account)

    @cached_property
    def macro_debt_exports_of_goods_services(self) -> data.Series[float | str | None]:
        return internals.macro_debt_exports_of_goods_services(input3_input_3_macro_exports_of_goods_and_services=self.input3_input_3_macro_exports_of_goods_and_services)

    @cached_property
    def macro_debt_imports_of_goods_services_use_positive_values(self) -> data.Series[float | str | None]:
        return internals.macro_debt_imports_of_goods_services_use_positive_values(input3_imports=data.INPUT3_IMPORTS, input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number=self.input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number)

    @cached_property
    def macro_debt_us_dollars_by_year_k(self) -> data.Series[float | str | None]:
        return internals.macro_debt_us_dollars_by_year_k(input3_input_3_macro_current_transfers_net=self.input3_input_3_macro_current_transfers_net)

    @cached_property
    def macro_debt_us_dollars_by_year_v(self) -> data.Series[float | str | None]:
        return internals.macro_debt_us_dollars_by_year_v(input3_input_3_macro_current_transfers_net=self.input3_input_3_macro_current_transfers_net)

    @cached_property
    def macro_debt_main_assumptions_us_dollars_k(self) -> data.Series[float | str | None]:
        return internals.macro_debt_main_assumptions_us_dollars_k(input3_input_3_macro_foreign_direct_investment=self.input3_input_3_macro_foreign_direct_investment)

    @cached_property
    def macro_debt_main_assumptions_us_dollars_v(self) -> data.Series[float | str | None]:
        return internals.macro_debt_main_assumptions_us_dollars_v(input3_input_3_macro_foreign_direct_investment=self.input3_input_3_macro_foreign_direct_investment)

    @cached_property
    def macro_debt_share_of_commodity_exports_fuel_of_exports_of_g(self) -> data.Series[float | str | None]:
        return internals.macro_debt_share_of_commodity_exports_fuel_of_exports_of_g(input3_input_3_macro_exports_of_goods_and_services=self.input3_input_3_macro_exports_of_goods_and_services, input3_input_3_macro_exports_commodity_fuel=self.input3_input_3_macro_exports_commodity_fuel)

    @cached_property
    def macro_debt_share_of_commodity_exports_non_fuel_of_exports(self) -> data.Series[float | str | None]:
        return internals.macro_debt_share_of_commodity_exports_non_fuel_of_exports(input3_input_3_macro_exports_of_goods_and_services=self.input3_input_3_macro_exports_of_goods_and_services, input3_input_3_macro_exports_commodity_non_fuel=self.input3_input_3_macro_exports_commodity_non_fuel)

    @cached_property
    def macro_debt_share_of_commodity_imports_fuel_of_exports_of_g(self) -> data.Series[float | str | None]:
        return internals.macro_debt_share_of_commodity_imports_fuel_of_exports_of_g(input3_input_3_macro_exports_of_goods_and_services=self.input3_input_3_macro_exports_of_goods_and_services, input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number=self.input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number)

    @cached_property
    def macro_debt_share_of_commodity_imports_non_fuel_of_exports(self) -> data.Series[int | str | None]:
        return internals.macro_debt_share_of_commodity_imports_non_fuel_of_exports(input3_input_3_macro_exports_of_goods_and_services=self.input3_input_3_macro_exports_of_goods_and_services, input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number=self.input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number)

    @cached_property
    def macro_debt_public_sector_revenues_including_grants(self) -> data.Series[float | str | None]:
        return internals.macro_debt_public_sector_revenues_including_grants(input3_input_3_macro_government_revenue_and_grants=self.input3_input_3_macro_government_revenue_and_grants)

    @cached_property
    def macro_debt_public_sector_grants(self) -> data.Series[float | str | None]:
        return internals.macro_debt_public_sector_grants(input3_input_3_macro_government_grants=self.input3_input_3_macro_government_grants)

    @cached_property
    def macro_debt_privatization_receipts(self) -> data.Series[float | str | None]:
        return internals.macro_debt_privatization_receipts(input3_other_debt_flows=data.INPUT3_OTHER_DEBT_FLOWS, input3_input_3_macro_privatization_proceeds=self.input3_input_3_macro_privatization_proceeds)

    @cached_property
    def macro_debt_public_sector_primary_expenditure(self) -> data.Series[float | str | None]:
        return internals.macro_debt_public_sector_primary_expenditure(in3_macro_government_primary_expenditures_this_used_be=self.in3_macro_government_primary_expenditures_this_used_be)

    @cached_property
    def macro_debt_public_sector_interest_expenditure(self) -> data.Series[float | str | None]:
        return internals.macro_debt_public_sector_interest_expenditure(macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due, macro_debt_total_public_domestic_debt_interest_due=self.macro_debt_total_public_domestic_debt_interest_due, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def macro_debt_public_sector_assets_e_g_deposits(self) -> data.Series[float | str | None]:
        return internals.macro_debt_public_sector_assets_e_g_deposits(in3_macro_public_sector_liquid_assets_stock_e_g_cash=self.in3_macro_public_sector_liquid_assets_stock_e_g_cash)

    @cached_property
    def macro_debt_recognition_of_contingent_liab_e_g_bank(self) -> data.Series[int | str | None]:
        return internals.macro_debt_recognition_of_contingent_liab_e_g_bank(input3_other_debt_flows=data.INPUT3_OTHER_DEBT_FLOWS, in3_macro_recognition_of_contingent_liab_e_g_bank=self.in3_macro_recognition_of_contingent_liab_e_g_bank)

    @cached_property
    def macro_debt_other_debt_creating_reducing_flow_please_specify(self) -> data.Series[int | str | None]:
        return internals.macro_debt_other_debt_creating_reducing_flow_please_specify(input3_other_debt_flows=data.INPUT3_OTHER_DEBT_FLOWS, input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify=self.input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify)

    @cached_property
    def macro_debt_debt_relief(self) -> data.Series[int | str | None]:
        return internals.macro_debt_debt_relief(input3_other_debt_flows=data.INPUT3_OTHER_DEBT_FLOWS, input3_input_3_macro_debt_relief_non_multilateral_hipc=self.input3_input_3_macro_debt_relief_non_multilateral_hipc)

    @cached_property
    def macro_debt_gdp_current_prices_u_s_dollars(self) -> data.Series[float | str | None]:
        return internals.macro_debt_gdp_current_prices_u_s_dollars(input3_input_3_macro_gross_domestic_product_us_dollars=self.input3_input_3_macro_gross_domestic_product_us_dollars)

    @cached_property
    def macro_debt_gdp_constant_prices(self) -> data.Series[float | str | None]:
        return internals.macro_debt_gdp_constant_prices(input3_input_3_macro_real_gross_domestic_product=self.input3_input_3_macro_real_gross_domestic_product)

    @cached_property
    def macro_debt_none(self) -> data.Series[float | str | None]:
        return internals.macro_debt_none(input3_us_deflator=data.INPUT3_US_DEFLATOR, input3_input_3_macro_u_s_deflator=self.input3_input_3_macro_u_s_deflator)

    @cached_property
    def macro_debt_exchange_rate_national_currency_per_u_s_dollar(self) -> data.Series[float | str | None]:
        return internals.macro_debt_exchange_rate_national_currency_per_u_s_dollar(input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p=self.input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p)

    @cached_property
    def macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc(self) -> data.Series[float | str | None]:
        return internals.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc(input3_input_3_macro_national_currency_per_u_s_dollar_p_a=self.input3_input_3_macro_national_currency_per_u_s_dollar_p_a)

    @cached_property
    def macro_debt_private_debt_pct_gdp(self) -> data.Series[float | str | None]:
        return internals.macro_debt_private_debt_pct_gdp(macro_debt_private_sector_ext_debt=self.macro_debt_private_sector_ext_debt, macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars)

    @cached_property
    def macro_debt_private_debt_service_pct_exports(self) -> data.Series[float | str | None]:
        return internals.macro_debt_private_debt_service_pct_exports(macro_debt_private_sector_short_term=self.macro_debt_private_sector_short_term, macro_debt_private_external_interest_due=self.macro_debt_private_external_interest_due, macro_debt_mlt_private_ext_debt_amortization=self.macro_debt_mlt_private_ext_debt_amortization, macro_debt_exports_of_goods_services=self.macro_debt_exports_of_goods_services)

    @cached_property
    def macro_debt_total_public_debt_outstanding_year_end(self) -> data.Series[float | str | None]:
        return internals.macro_debt_total_public_debt_outstanding_year_end(macro_debt_total_public_ext_debt=self.macro_debt_total_public_ext_debt, macro_debt_total_public_domestic_debt=self.macro_debt_total_public_domestic_debt)

    @cached_property
    def macro_debt_total_public_ext_debt(self) -> data.Series[float | str | None]:
        return internals.macro_debt_total_public_ext_debt(macro_debt_us_dollars_by_year=self.macro_debt_us_dollars_by_year, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar)

    @cached_property
    def macro_debt_total_public_domestic_debt(self) -> data.Series[float | str | None]:
        return internals.macro_debt_total_public_domestic_debt(macro_debt_national_currency=self.macro_debt_national_currency)

    @cached_property
    def macro_debt_fx_denominated_public_debt_end_of_period(self) -> data.Series[float | str | None]:
        return internals.macro_debt_fx_denominated_public_debt_end_of_period(input3_local_currency_external_debt=self.input3_local_currency_external_debt, ext_debt_fx_denominated_debt_outstanding=self.ext_debt_fx_denominated_debt_outstanding, in3_macro_fx_denominated_debt_including_locally_issued=self.in3_macro_fx_denominated_debt_including_locally_issued, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar)

    @cached_property
    def macro_debt_share_of_local_currency_denominated_external(self) -> data.Series[float | str | None]:
        return internals.macro_debt_share_of_local_currency_denominated_external(input3_local_currency_external_debt=self.input3_local_currency_external_debt, input5_old_debt_outstanding_from_old_debt_in_local_currency=self.input5_old_debt_outstanding_from_old_debt_in_local_currency, input5_new_debt_debt_stock_on_new_debt_denominated_in_local_currency=self.input5_new_debt_debt_stock_on_new_debt_denominated_in_local_currency, external_domestic_debt_definition=self.external_domestic_debt_definition, in3_macro_transition_formula_these_outstanding=self.in3_macro_transition_formula_these_outstanding, macro_debt_us_dollars=self.macro_debt_us_dollars, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar, lookup_afg=self.lookup_afg)

    @cached_property
    def macro_debt_interest_rate_ext_debt(self) -> data.Series[float | str | None]:
        return internals.macro_debt_interest_rate_ext_debt(macro_debt_us_dollars_by_year=self.macro_debt_us_dollars_by_year, macro_debt_ppg_interest_due=self.macro_debt_ppg_interest_due)

    @cached_property
    def macro_debt_interest_rate_domestic_debt(self) -> data.Series[float | str | None]:
        return internals.macro_debt_interest_rate_domestic_debt(macro_debt_national_currency=self.macro_debt_national_currency, macro_debt_total_public_domestic_debt_interest_due=self.macro_debt_total_public_domestic_debt_interest_due, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def macro_debt_pv_of_public_sector_ext_debt_end_of_period(self) -> data.Series[float | str | None]:
        return internals.macro_debt_pv_of_public_sector_ext_debt_end_of_period(ext_debt_total_pv_of_debt=self.ext_debt_total_pv_of_debt, macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar)

    @cached_property
    def macro_debt_national_currency_us_dollars(self) -> data.Series[float | str | None]:
        return internals.macro_debt_national_currency_us_dollars(macro_debt_public_sector_revenues_including_grants=self.macro_debt_public_sector_revenues_including_grants, macro_debt_public_sector_grants=self.macro_debt_public_sector_grants, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def macro_debt_revenues_pct_gdp(self) -> data.Series[float | str | None]:
        return internals.macro_debt_revenues_pct_gdp(macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_national_currency_us_dollars=self.macro_debt_national_currency_us_dollars)

    @cached_property
    def macro_debt_real_gdp_growth(self) -> data.Series[float | str | None]:
        return internals.macro_debt_real_gdp_growth(macro_debt_gdp_constant_prices=self.macro_debt_gdp_constant_prices)

    @cached_property
    def macro_debt_gdp_deflator_index_national_currency(self) -> data.Series[float | str | None]:
        return internals.macro_debt_gdp_deflator_index_national_currency(macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_gdp_constant_prices=self.macro_debt_gdp_constant_prices, macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def macro_debt_change_in_gdp_deflator_factor(self) -> data.Series[float | str | None]:
        return internals.macro_debt_change_in_gdp_deflator_factor(macro_debt_gdp_deflator_index_national_currency=self.macro_debt_gdp_deflator_index_national_currency)

    @cached_property
    def macro_debt_gdp_deflator_index_dollars(self) -> data.Series[float | str | None]:
        return internals.macro_debt_gdp_deflator_index_dollars(macro_debt_gdp_current_prices_u_s_dollars=self.macro_debt_gdp_current_prices_u_s_dollars, macro_debt_gdp_constant_prices=self.macro_debt_gdp_constant_prices)

    @cached_property
    def macro_debt_change_in_gdp_deflator_factor_by_year(self) -> data.Series[float | str | None]:
        return internals.macro_debt_change_in_gdp_deflator_factor_by_year(macro_debt_gdp_deflator_index_dollars=self.macro_debt_gdp_deflator_index_dollars)

    @cached_property
    def macro_debt_us_gdp_deflator_percent_change(self) -> data.Series[float | str | None]:
        return internals.macro_debt_us_gdp_deflator_percent_change(macro_debt_none=self.macro_debt_none)

    @cached_property
    def macro_debt_exchange_rate_dollar_nc(self) -> data.Series[float | str | None]:
        return internals.macro_debt_exchange_rate_dollar_nc(macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def macro_debt_depreciation_of_nc_depreciation(self) -> data.Series[float | str | None]:
        return internals.macro_debt_depreciation_of_nc_depreciation(macro_debt_exchange_rate_dollar_nc=self.macro_debt_exchange_rate_dollar_nc)

    @cached_property
    def start_debt_sustainability_analysis(self) -> str | int | float | bool:
        return internals.start_debt_sustainability_analysis(start_working_language=self.start_working_language, lookup_language_native_name=data.LOOKUP_LANGUAGE_NATIVE_NAME, lookup_language_english_name=data.LOOKUP_LANGUAGE_ENGLISH_NAME)

    @cached_property
    def start_debt_sustainability_analysis_m(self) -> int | str:
        return internals.start_debt_sustainability_analysis_m(start_debt_sustainability_analysis=self.start_debt_sustainability_analysis)

    @cached_property
    def lookup_afg_ap(self) -> str | int | float | bool:
        return internals.lookup_afg_ap(translation_input_3_macro_debt_data_dmx_held_by_residents=data.TRANSLATION_INPUT_3_MACRO_DEBT_DATA_DMX_HELD_BY_RESIDENTS, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def lookup_hti(self) -> str | int | float | bool:
        return internals.lookup_hti(translation_input_5_domestic_financing_denominated_in_foreign_currency_fx=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_DENOMINATED_IN_FOREIGN_CURRENCY_FX, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def lookup_hnd(self) -> str | int | float | bool:
        return internals.lookup_hnd(translation_input_5_domestic_financing_denominated_in_foreign_currency_fx_external_debt=data.TRANSLATION_INPUT_5_DOMESTIC_FINANCING_DENOMINATED_IN_FOREIGN_CURRENCY_FX_EXTERNAL_DEBT, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def translation_interest_rate_domestic_debt(self) -> data.Series[str | int | float | bool | None]:
        return internals.translation_interest_rate_domestic_debt(translation_input_3_macro_debt_data_dmx_interest_rate_on_domestic_debt=data.TRANSLATION_INPUT_3_MACRO_DEBT_DATA_DMX_INTEREST_RATE_ON_DOMESTIC_DEBT)

    @cached_property
    def translation_st_debt(self) -> data.Series[str | int | float | bool | None]:
        return internals.translation_st_debt(translation_labels_short_term_debt=data.TRANSLATION_LABELS_SHORT_TERM_DEBT)

    @cached_property
    def macro_debt_previous_vintage_investment(self) -> data.Series[float | str | None]:
        return internals.macro_debt_previous_vintage_investment(input3_investment=data.INPUT3_INVESTMENT)

    @cached_property
    def input3_projection_year_header(self) -> int | str:
        return internals.input3_projection_year_header(macro_debt_data=self.macro_debt_data)

    @cached_property
    def input3_local_currency_domestic_debt(self) -> data.Series[float | str | None]:
        return internals.input3_local_currency_domestic_debt(input3_domestic_local_currency_stock=data.INPUT3_DOMESTIC_LOCAL_CURRENCY_STOCK, input3_domestic_foreign_currency_stock=data.INPUT3_DOMESTIC_FOREIGN_CURRENCY_STOCK, input3_domestic_local_currency_interest=data.INPUT3_DOMESTIC_LOCAL_CURRENCY_INTEREST, external_domestic_debt_definition=self.external_domestic_debt_definition, input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p=self.input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p, input3_input_3_macro_national_currency_per_u_s_dollar_p_a=self.input3_input_3_macro_national_currency_per_u_s_dollar_p_a, input3_domestic_interest_payment_from_existing_debt=self.input3_domestic_interest_payment_from_existing_debt, in3_macro_o_w_st=self.in3_macro_o_w_st, lookup_afg=self.lookup_afg)

    @cached_property
    def input3_local_currency_external_debt(self) -> data.Series[float | str | None]:
        return internals.input3_local_currency_external_debt(input3_ppg_external_debt_stock=data.INPUT3_PPG_EXTERNAL_DEBT_STOCK, input3_domestic_foreign_currency_stock=data.INPUT3_DOMESTIC_FOREIGN_CURRENCY_STOCK, input3_nonresident_local_currency_stock=data.INPUT3_NONRESIDENT_LOCAL_CURRENCY_STOCK, input3_nonresident_foreign_currency_stock=data.INPUT3_NONRESIDENT_FOREIGN_CURRENCY_STOCK, external_domestic_debt_definition=self.external_domestic_debt_definition, input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p=self.input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p, input3_domestic_o_w_st=self.input3_domestic_o_w_st, lookup_afg=self.lookup_afg)

    @cached_property
    def output_submit_first_projection_year(self) -> int | str:
        return internals.output_submit_first_projection_year(macro_debt_data=self.macro_debt_data)

    @cached_property
    def lookup_country_scale_phrase(self) -> data.Series[str | int | float | bool | None]:
        return internals.lookup_country_scale_phrase(translation_scale_phrase=data.TRANSLATION_SCALE_PHRASE, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def leftover_exchange_rate_pa(self) -> data.Series[float | str | None]:
        return internals.leftover_exchange_rate_pa(macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def custom_pub_period(self) -> data.Series[int | str | None]:
        return internals.custom_pub_period(pv_resfin_pub_opening_stock_period=data.PV_RESFIN_PUB_OPENING_STOCK_PERIOD, pv_resfin_pub_discount_period=self.pv_resfin_pub_discount_period)

    @cached_property
    def custom_ext_of_which_public_publicly_guaranteed_ppg(self) -> data.Series[float | str | None]:
        return internals.custom_ext_of_which_public_publicly_guaranteed_ppg(custom_pub_of_which_fx_denominated=self.custom_pub_of_which_fx_denominated)

    @cached_property
    def c4_market_path_baseline_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.c4_market_path_baseline_pv_of_debt(ext_debt_total_pv_of_debt=self.ext_debt_total_pv_of_debt)

    @cached_property
    def c4_market_path_exports(self) -> data.Series[float | str | None]:
        return internals.c4_market_path_exports(macro_debt_exports_of_goods_services=self.macro_debt_exports_of_goods_services)

    @cached_property
    def c4_market_path_nominal_gdp_stress(self) -> data.Series[float | str | None]:
        return internals.c4_market_path_nominal_gdp_stress(c4_market_path_nominal_gdp=self.c4_market_path_nominal_gdp, c4_mkt_fin_nominal_gdp=self.c4_mkt_fin_nominal_gdp)

    @cached_property
    def custom_ext_additional_debt_service_stress(self) -> data.Series[float | str | None]:
        return internals.custom_ext_additional_debt_service_stress(custom_ext_total_debt_service_by_year=self.custom_ext_total_debt_service_by_year)

    @cached_property
    def custom_ext_debt_service_ppg_baseline(self) -> data.Series[float | str | None]:
        return internals.custom_ext_debt_service_ppg_baseline(ext_debt_total_public_debt_service=self.ext_debt_total_public_debt_service)

    @cached_property
    def custom_ext_exports(self) -> data.Series[float | str | None]:
        return internals.custom_ext_exports(custom_pub_exports=self.custom_pub_exports)

    @cached_property
    def custom_ext_gdp_deflator_in_us_dollar_terms_change_pct(self) -> data.Series[float | str | None]:
        return internals.custom_ext_gdp_deflator_in_us_dollar_terms_change_pct(custom_pub_gdp_deflator_in_us_dollar_terms_change_pct=self.custom_pub_gdp_deflator_in_us_dollar_terms_change_pct)

    @cached_property
    def custom_ext_gdp_deflator_in_us_dollar_terms_change_pct_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_ext_gdp_deflator_in_us_dollar_terms_change_pct_by_year(custom_ext_gdp_deflator_in_us_dollar_terms_change_pct=self.custom_ext_gdp_deflator_in_us_dollar_terms_change_pct)

    @cached_property
    def custom_ext_pv_of_additional_borrowing(self) -> data.Series[float | str | None]:
        return internals.custom_ext_pv_of_additional_borrowing(custom_ext_pv_of_new_forex_debt=self.custom_ext_pv_of_new_forex_debt)

    @cached_property
    def custom_ext_pv_ppg_baseline(self) -> data.Series[float | str | None]:
        return internals.custom_ext_pv_ppg_baseline(ext_debt_total_pv_of_debt=self.ext_debt_total_pv_of_debt)

    @cached_property
    def custom_ext_real_gdp_growth(self) -> data.Series[float | str | None]:
        return internals.custom_ext_real_gdp_growth(custom_pub_real_gdp_growth=self.custom_pub_real_gdp_growth)

    @cached_property
    def custom_pub_inflation_rate_gdp_deflator_pct_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_pub_inflation_rate_gdp_deflator_pct_by_year(custom_pub_inflation_rate_gdp_deflator_pct=self.custom_pub_inflation_rate_gdp_deflator_pct)

    @cached_property
    def custom_pub_nominal_depreciation_of_lc_percentage_change_lc_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_pub_nominal_depreciation_of_lc_percentage_change_lc_by_year(custom_pub_nominal_depreciation_of_lc_percentage_change_lc=self.custom_pub_nominal_depreciation_of_lc_percentage_change_lc)

    @cached_property
    def custom_pub_us_inflation_rate_gdp_deflator_pct(self) -> data.Series[float | str | None]:
        return internals.custom_pub_us_inflation_rate_gdp_deflator_pct(macro_debt_us_gdp_deflator_percent_change=self.macro_debt_us_gdp_deflator_percent_change)

    @cached_property
    def macro_debt_gross_financing_need(self) -> data.Series[float | str | None]:
        return internals.macro_debt_gross_financing_need(input5_public_gfns_6_public_gfns=self.input5_public_gfns_6_public_gfns)

    @cached_property
    def macro_debt_main_assumptions_us_dollars_by_year_6(self) -> data.Series[float | str | None]:
        return internals.macro_debt_main_assumptions_us_dollars_by_year_6(ext_debt_public_debt_service_principal=self.ext_debt_public_debt_service_principal)

    @cached_property
    def c4_market_path_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.c4_market_path_pv_of_debt(pv_baseline_com_pv_debt=self.pv_baseline_com_pv_debt)

    @cached_property
    def c4_market_path_pv_of_debt_alt(self) -> data.Series[float | str | None]:
        return internals.c4_market_path_pv_of_debt_alt(pv_stress_com_pv_debt=self.pv_stress_com_pv_debt)

    @cached_property
    def c4_market_path_real_gdp_growth(self) -> data.Series[float | str | None]:
        return internals.c4_market_path_real_gdp_growth(dsa_ext_real_gdp_growth_in_percent=self.dsa_ext_real_gdp_growth_in_percent)

    @cached_property
    def c4_market_path_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.c4_market_path_total_debt_service(pv_baseline_com_total_debt_service=self.pv_baseline_com_total_debt_service)

    @cached_property
    def c4_market_path_total_debt_service_alt(self) -> data.Series[float | str | None]:
        return internals.c4_market_path_total_debt_service_alt(pv_stress_com_total_debt_service=self.pv_stress_com_total_debt_service)

    @cached_property
    def custom_pub_avg_real_interest_rate_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_pub_avg_real_interest_rate_by_year(custom_pub_avg_real_interest_rate=self.custom_pub_avg_real_interest_rate)

    @cached_property
    def custom_pub_avg_real_interest_rate_new_borrowing_by_year(self) -> data.Series[float | str | None]:
        return internals.custom_pub_avg_real_interest_rate_new_borrowing_by_year(custom_pub_avg_real_interest_rate_new_borrowing=self.custom_pub_avg_real_interest_rate_new_borrowing)

    @cached_property
    def c4_market_instruments(self) -> data.Series[int | str | None]:
        return internals.c4_market_instruments(input4_grace_period=self.input4_grace_period, input4_loan_maturity=self.input4_loan_maturity)

    @cached_property
    def ci_summary_gdp_us_dollars_billions(self) -> data.Series[float | str | None]:
        return internals.ci_summary_gdp_us_dollars_billions(imported_classification_values=self.imported_classification_values)

    @cached_property
    def ci_summary_remittances_gross_us_dollars_billions(self) -> data.Series[float | str | None]:
        return internals.ci_summary_remittances_gross_us_dollars_billions(imported_classification_values=self.imported_classification_values)

    @cached_property
    def imported_components(self) -> data.Series[int | str | None]:
        return internals.imported_components(imported_classification_years=self.imported_classification_years)

    @cached_property
    def input5_instrument_titles(self) -> data.Series[str | int | float | bool | None]:
        return internals.input5_instrument_titles(input5_instrument_terms_instrument_label=self.input5_instrument_terms_instrument_label)

    @cached_property
    def input6_standard_params_2(self) -> data.Series[float | str | None]:
        return internals.input6_standard_params_2(in6opt_standard_inflation_elasticity_default=self.in6opt_standard_inflation_elasticity_default, in6opt_standard_addl_borrowing_cost_default=self.in6opt_standard_addl_borrowing_cost_default, in6opt_standard_gdp_exports_elasticity_default=self.in6opt_standard_gdp_exports_elasticity_default, in6opt_standard_fx_passthrough_default=self.in6opt_standard_fx_passthrough_default, in6opt_standard_nx_elasticity_default=self.in6opt_standard_nx_elasticity_default, in6opt_standard_us_inflation_default=self.in6opt_standard_us_inflation_default)

    @cached_property
    def leftover_primary_deficit(self) -> data.Series[float | str | None]:
        return internals.leftover_primary_deficit(a1_hist_pub_historical_statistics=self.a1_hist_pub_historical_statistics, baseline_pub_primary_deficit_by_indicator=self.baseline_pub_primary_deficit_by_indicator)

    @cached_property
    def customized_scenario_spec(self) -> data.Series[float | str | None]:
        return internals.customized_scenario_spec(input6_tailored_params_2=self.input6_tailored_params_2, input6_tailored_params_3=self.input6_tailored_params_3)

    @cached_property
    def leftover_real_gdp_growth(self) -> data.Series[float | str | None]:
        return internals.leftover_real_gdp_growth(a1_hist_pub_historical_statistics=self.a1_hist_pub_historical_statistics, baseline_pub_real_gdp_growth_by_indicator=self.baseline_pub_real_gdp_growth_by_indicator)

    @cached_property
    def c4_market_instruments_k(self) -> data.Series[float | str | None]:
        return internals.c4_market_instruments_k(pv_stress_com_discount_interest_rate=self.pv_stress_com_discount_interest_rate)

    @cached_property
    def input6_standard_params(self) -> data.Series[int | str | None]:
        return internals.input6_standard_params(input6_standard_b1_real_gdp_growth_size_of_real_gdp_growth_shock_of_standard_deviations=data.INPUT6_STANDARD_B1_REAL_GDP_GROWTH_SIZE_OF_REAL_GDP_GROWTH_SHOCK_OF_STANDARD_DEVIATIONS, input6_standard_b2_primary_balance_size_of_pb_gdp_shock_of_standard_deviations=data.INPUT6_STANDARD_B2_PRIMARY_BALANCE_SIZE_OF_PB_GDP_SHOCK_OF_STANDARD_DEVIATIONS, input6_standard_b3_exports_size_of_exports_growth_shock_of_standard_deviations=data.INPUT6_STANDARD_B3_EXPORTS_SIZE_OF_EXPORTS_GROWTH_SHOCK_OF_STANDARD_DEVIATIONS, input6_standard_b4_other_non_debt_creating_flows_other_flows_current_transfers_shock_of_standard_deviations=data.INPUT6_STANDARD_B4_OTHER_NON_DEBT_CREATING_FLOWS_OTHER_FLOWS_CURRENT_TRANSFERS_SHOCK_OF_STANDARD_DEVIATIONS, input6_standard_b4_other_non_debt_creating_flows_other_flows_fdi_shock_of_standard_deviations=data.INPUT6_STANDARD_B4_OTHER_NON_DEBT_CREATING_FLOWS_OTHER_FLOWS_FDI_SHOCK_OF_STANDARD_DEVIATIONS)

    @cached_property
    def input6_tailored_params_3(self) -> data.Series[float | str | None]:
        return internals.input6_tailored_params_3(in6_tailored_commodity_interaction_defaults=self.in6_tailored_commodity_interaction_defaults, in6_tailored_natdisaster_interaction_defaults=self.in6_tailored_natdisaster_interaction_defaults, in6_tailored_mkt_fin_fx_passthrough_default=self.in6_tailored_mkt_fin_fx_passthrough_default)

    @cached_property
    def leftover_us_gdp_deflator(self) -> data.Series[float | str | None]:
        return internals.leftover_us_gdp_deflator(input6_standard_params_2=self.input6_standard_params_2, input6_tailored_params_3=self.input6_tailored_params_3)

    @cached_property
    def custom_ext_average_interest_rate_new_debt_by_row(self) -> data.Series[float | str | None]:
        return internals.custom_ext_average_interest_rate_new_debt_by_row(in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def in7_resfin_avg_nominal_interest_rate_new_borrowing_usd_by_row(self) -> data.Series[float | str | None]:
        return internals.in7_resfin_avg_nominal_interest_rate_new_borrowing_usd_by_row(in7_resfin_ext_mlt_default=self.in7_resfin_ext_mlt_default)

    @cached_property
    def leftover_real_interest_rate(self) -> data.Series[float | str | None]:
        return internals.leftover_real_interest_rate(input6_standard_params_2=self.input6_standard_params_2, input6_tailored_params_3=self.input6_tailored_params_3)

    @cached_property
    def c4_mkt_fin_net_non_debt_creating_flows_fdi_gdp_ratio_by_row(self) -> data.Series[float | str | None]:
        return internals.c4_mkt_fin_net_non_debt_creating_flows_fdi_gdp_ratio_by_row(input6_tailored_params_2=self.input6_tailored_params_2)

    @cached_property
    def ci_summary_medium(self) -> data.Series[str | int | float | bool | None]:
        return internals.ci_summary_medium(imported_composite_indicator=self.imported_composite_indicator)

    @cached_property
    def leftover_export_growth_usd(self) -> data.Series[float | str | None]:
        return internals.leftover_export_growth_usd(input6_standard_params_2=self.input6_standard_params_2)

    @cached_property
    def leftover_fdi_gdp(self) -> data.Series[float | str | None]:
        return internals.leftover_fdi_gdp(in6opt_standard_size_of_exports_growth_shock_of_standard=self.in6opt_standard_size_of_exports_growth_shock_of_standard)

    @cached_property
    def leftover_revenue_gdp(self) -> data.Series[float | str | None]:
        return internals.leftover_revenue_gdp(in6opt_standard_size_of_pb_gdp_shock_of_standard_deviations=self.in6opt_standard_size_of_pb_gdp_shock_of_standard_deviations)

    @cached_property
    def b1_gdp_ext_ii_key_macroeconomic_assumptions(self) -> int | str:
        return internals.b1_gdp_ext_ii_key_macroeconomic_assumptions(input6_standard_params=self.input6_standard_params)

    @cached_property
    def b1_gdp_pub_key_macroeconomic_fiscal_assumptions(self) -> int | str:
        return internals.b1_gdp_pub_key_macroeconomic_fiscal_assumptions(input6_standard_params=self.input6_standard_params)

    @cached_property
    def b2_pb_mkt_pub_i_baseline_medium_term_projections(self) -> int | str:
        return internals.b2_pb_mkt_pub_i_baseline_medium_term_projections(input6_standard_params=self.input6_standard_params)

    @cached_property
    def b2_pb_nonmkt_pub_i_baseline_medium_term_projections(self) -> int | str:
        return internals.b2_pb_nonmkt_pub_i_baseline_medium_term_projections(input6_standard_params=self.input6_standard_params)

    @cached_property
    def b3_exports_ext_iii_averages_standard_deviations(self) -> int | str:
        return internals.b3_exports_ext_iii_averages_standard_deviations(input6_standard_params=self.input6_standard_params)

    @cached_property
    def b4_otherflows_ext_ii_key_macroeconomic_assumptions(self) -> int | str:
        return internals.b4_otherflows_ext_ii_key_macroeconomic_assumptions(input6_standard_params=self.input6_standard_params)

    @cached_property
    def b6_combo_mkt_ext_ii_key_macroeconomic_assumptions(self) -> float | str:
        return internals.b6_combo_mkt_ext_ii_key_macroeconomic_assumptions(in6opt_standard_apply_all_individual_shocks_b1_through_b5_half=self.in6opt_standard_apply_all_individual_shocks_b1_through_b5_half)

    @cached_property
    def b6_combo_mkt_ext_y1_includes_both_public_nominal_debt_baseline(self) -> float | str:
        return internals.b6_combo_mkt_ext_y1_includes_both_public_nominal_debt_baseline(in6opt_standard_other_flows_current_transfers_shock_of_standard=self.in6opt_standard_other_flows_current_transfers_shock_of_standard)

    @cached_property
    def b6_combo_mkt_ext_y1_includes_both_public_nominal_debt_stress(self) -> float | str:
        return internals.b6_combo_mkt_ext_y1_includes_both_public_nominal_debt_stress(in6opt_standard_b6_combination_other_flows_fdi_shock_of_standard_deviations=self.in6opt_standard_b6_combination_other_flows_fdi_shock_of_standard_deviations)

    @cached_property
    def b6_combo_mkt_ext_y1_includes_both_public_private_sector_ext_debt(self) -> float | str:
        return internals.b6_combo_mkt_ext_y1_includes_both_public_private_sector_ext_debt(input6_standard_params_2=self.input6_standard_params_2)

    @cached_property
    def b6_combo_mkt_ext_y1_includes_both_public_pv_total(self) -> float | str:
        return internals.b6_combo_mkt_ext_y1_includes_both_public_pv_total(input6_standard_params_2=self.input6_standard_params_2)

    @cached_property
    def b6_combo_mkt_pub_i_baseline_medium_term_nominal_debt(self) -> float | str:
        return internals.b6_combo_mkt_pub_i_baseline_medium_term_nominal_debt(input6_standard_params_2=self.input6_standard_params_2)

    @cached_property
    def b6_combo_mkt_pub_i_baseline_medium_term_projections(self) -> float | str:
        return internals.b6_combo_mkt_pub_i_baseline_medium_term_projections(in6opt_standard_apply_all_individual_shocks_b1_through_b5_half=self.in6opt_standard_apply_all_individual_shocks_b1_through_b5_half)

    @cached_property
    def b6_combo_nonmkt_ext_ii_key_macroeconomic_assumptions(self) -> float | str:
        return internals.b6_combo_nonmkt_ext_ii_key_macroeconomic_assumptions(in6opt_standard_apply_all_individual_shocks_b1_through_b5_half=self.in6opt_standard_apply_all_individual_shocks_b1_through_b5_half)

    @cached_property
    def b6_combo_nonmkt_ext_increase(self) -> float | str:
        return internals.b6_combo_nonmkt_ext_increase(in6opt_standard_b6_combination_other_flows_fdi_shock_of_standard_deviations=self.in6opt_standard_b6_combination_other_flows_fdi_shock_of_standard_deviations)

    @cached_property
    def b6_combo_nonmkt_ext_y7_long_run_constant_balance_that_stabilizes(self) -> float | str:
        return internals.b6_combo_nonmkt_ext_y7_long_run_constant_balance_that_stabilizes(in6opt_standard_other_flows_current_transfers_shock_of_standard=self.in6opt_standard_other_flows_current_transfers_shock_of_standard)

    @cached_property
    def b6_combo_nonmkt_ext_y7_long_run_constant_private_debt_pv(self) -> float | str:
        return internals.b6_combo_nonmkt_ext_y7_long_run_constant_private_debt_pv(input6_standard_params_2=self.input6_standard_params_2)

    @cached_property
    def b6_combo_nonmkt_ext_y7_long_run_constant_pv_total(self) -> float | str:
        return internals.b6_combo_nonmkt_ext_y7_long_run_constant_pv_total(input6_standard_params_2=self.input6_standard_params_2)

    @cached_property
    def b6_combo_nonmkt_pub_i_baseline_medium_term_projections(self) -> float | str:
        return internals.b6_combo_nonmkt_pub_i_baseline_medium_term_projections(in6opt_standard_apply_all_individual_shocks_b1_through_b5_half=self.in6opt_standard_apply_all_individual_shocks_b1_through_b5_half)

    @cached_property
    def b6_combo_nonmkt_pub_in_billions_of_lc(self) -> float | str:
        return internals.b6_combo_nonmkt_pub_in_billions_of_lc(input6_standard_params_2=self.input6_standard_params_2)

    @cached_property
    def c2_natdisaster_historical_statistics_key_variables_past_10(self) -> int | str:
        return internals.c2_natdisaster_historical_statistics_key_variables_past_10(input6_tailored_params_2=self.input6_tailored_params_2)

    @cached_property
    def c3_commodity_ext_ii_key_macroeconomic_assumptions(self) -> int | str:
        return internals.c3_commodity_ext_ii_key_macroeconomic_assumptions(input6_tailored_params_2=self.input6_tailored_params_2)

    @cached_property
    def c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions(self) -> float | str:
        return internals.c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions(input6_tailored_params=self.input6_tailored_params)

    @cached_property
    def c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_2(self) -> float | str:
        return internals.c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_2(in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s=self.in6_tailored_adjusted_share_of_fuel_in_exports_of_g_s)

    @cached_property
    def c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_3(self) -> float | str:
        return internals.c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_3(in6_tailored_price_shock_non_fuel=self.in6_tailored_price_shock_non_fuel)

    @cached_property
    def c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_4(self) -> float | str:
        return internals.c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_4(in6_tailored_adjusted_share_of_non_fuel_in_exports_of_g_s=self.in6_tailored_adjusted_share_of_non_fuel_in_exports_of_g_s)

    @cached_property
    def c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_5(self) -> float | str:
        return internals.c3_commodity_ext_ii_key_macroeconomic_ii_key_macroeconomic_assumptions_5(input6_tailored_params_2=self.input6_tailored_params_2)

    @cached_property
    def c3_commodity_pub_historical_statistics_key_historical_statistics_key_variables_past_10(self) -> float | str:
        return internals.c3_commodity_pub_historical_statistics_key_historical_statistics_key_variables_past_10(in6_tailored_adjusted_share_of_commodities_in_total_exports=self.in6_tailored_adjusted_share_of_commodities_in_total_exports)

    @cached_property
    def c3_commodity_pub_historical_statistics_key_historical_statistics_key_variables_past_10_2(self) -> float | str:
        return internals.c3_commodity_pub_historical_statistics_key_historical_statistics_key_variables_past_10_2(input6_tailored_params_2=self.input6_tailored_params_2)

    @cached_property
    def c3_commodity_pub_historical_statistics_key_variables_past_10(self) -> int | str:
        return internals.c3_commodity_pub_historical_statistics_key_variables_past_10(input6_tailored_params_2=self.input6_tailored_params_2)

    @cached_property
    def c4_market_path_nominal_gdp(self) -> float | str:
        return internals.c4_market_path_nominal_gdp(dsa_ext_nominal_gdp_million_of_us_dollars=self.dsa_ext_nominal_gdp_million_of_us_dollars)

    @cached_property
    def c4_market_path_non_interest_ca_pct_gdp(self) -> float | str:
        return internals.c4_market_path_non_interest_ca_pct_gdp(input6_tailored_params_3=self.input6_tailored_params_3)

    @cached_property
    def c4_market_path_revised_pv_debt_exports(self) -> float | str:
        return internals.c4_market_path_revised_pv_debt_exports(dsa_ext_pv_of_ppg_external_debt_to_exports_ratio=self.dsa_ext_pv_of_ppg_external_debt_to_exports_ratio)

    @cached_property
    def c4_market_path_us_gdp_deflator(self) -> int | str:
        return internals.c4_market_path_us_gdp_deflator(input6_tailored_params_2=self.input6_tailored_params_2)

    @cached_property
    def c4_mkt_fin_i_macro_indicators(self) -> int | str:
        return internals.c4_mkt_fin_i_macro_indicators(input6_tailored_params_2=self.input6_tailored_params_2)

    @cached_property
    def custom_ext_ii_key_macroeconomic_nominal_gdp_million_of_us_dollars(self) -> float | str:
        return internals.custom_ext_ii_key_macroeconomic_nominal_gdp_million_of_us_dollars(dsa_ext_nominal_gdp_million_of_us_dollars=self.dsa_ext_nominal_gdp_million_of_us_dollars)

    @cached_property
    def custom_ext_include_external_customized_scenario_in_charts(self) -> str | int | float | bool:
        return internals.custom_ext_include_external_customized_scenario_in_charts(customized_public_include_scenario=self.customized_public_include_scenario)

    @cached_property
    def custom_ext_short_name_cumulative(self) -> float | str:
        return internals.custom_ext_short_name_cumulative(custom_ext_new_forex_borrowing_gross_usd=self.custom_ext_new_forex_borrowing_gross_usd)

    @cached_property
    def custom_ext_y7_long_run_constant_nominal_gdp_million_of_us_dollars(self) -> float | str:
        return internals.custom_ext_y7_long_run_constant_nominal_gdp_million_of_us_dollars(custom_ext_ii_key_macroeconomic_nominal_gdp_million_of_us_dollars=self.custom_ext_ii_key_macroeconomic_nominal_gdp_million_of_us_dollars)

    @cached_property
    def custom_pub_avg_grace_period(self) -> int | str:
        return internals.custom_pub_avg_grace_period(in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def custom_pub_avg_maturity_incl_grace_period(self) -> int | str:
        return internals.custom_pub_avg_maturity_incl_grace_period(in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def custom_pub_avg_nominal_interest_rate_new_borrowing_usd(self) -> float | str:
        return internals.custom_pub_avg_nominal_interest_rate_new_borrowing_usd(in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def custom_pub_avg_real_interest_rate(self) -> float | str:
        return internals.custom_pub_avg_real_interest_rate(in7_resfin_dom_st_interest_effective=self.in7_resfin_dom_st_interest_effective)

    @cached_property
    def custom_pub_avg_real_interest_rate_new_borrowing(self) -> float | str:
        return internals.custom_pub_avg_real_interest_rate_new_borrowing(in7_resfin_dom_mlt_effective=self.in7_resfin_dom_mlt_effective)

    @cached_property
    def custom_pub_domestic_mlt(self) -> float | str:
        return internals.custom_pub_domestic_mlt(in7_resfin_shares_effective=self.in7_resfin_shares_effective)

    @cached_property
    def custom_pub_domestic_st(self) -> float | str:
        return internals.custom_pub_domestic_st(in7_resfin_domestic_st=self.in7_resfin_domestic_st)

    @cached_property
    def custom_pub_external_ppg_mlt(self) -> float | str:
        return internals.custom_pub_external_ppg_mlt(in7_resfin_shares_effective=self.in7_resfin_shares_effective)

    @cached_property
    def custom_pub_in_billions_of_lc_of_which_short_term(self) -> float | str:
        return internals.custom_pub_in_billions_of_lc_of_which_short_term(macro_debt_public_domestic_st=self.macro_debt_public_domestic_st)

    @cached_property
    def custom_pub_key_macroeconomic_fiscal_exchange_rate_lc_per_us_dollar(self) -> float | str:
        return internals.custom_pub_key_macroeconomic_fiscal_exchange_rate_lc_per_us_dollar(macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar)

    @cached_property
    def custom_pub_shares_of_marginal_debt_avg_grace_period(self) -> int | str:
        return internals.custom_pub_shares_of_marginal_debt_avg_grace_period(in7_resfin_dom_mlt_effective=self.in7_resfin_dom_mlt_effective)

    @cached_property
    def custom_pub_shares_of_marginal_debt_avg_maturity_incl_grace_period(self) -> int | str:
        return internals.custom_pub_shares_of_marginal_debt_avg_maturity_incl_grace_period(in7_resfin_dom_mlt_effective=self.in7_resfin_dom_mlt_effective)

    @cached_property
    def custom_pub_usd_discount_rate(self) -> float | str:
        return internals.custom_pub_usd_discount_rate(in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def custom_pub_variables_needed_public_public_sector_assets_e_g_deposits(self) -> float | str:
        return internals.custom_pub_variables_needed_public_public_sector_assets_e_g_deposits(macro_debt_public_sector_assets_e_g_deposits=self.macro_debt_public_sector_assets_e_g_deposits)

    @cached_property
    def imported_of(self) -> float | str:
        return internals.imported_of(com_id_as_of_date=data.COM_ID_AS_OF_DATE)

    @cached_property
    def in2_coverage_other_elements_of_govt_not_captured_in_1(self) -> int | str:
        return internals.in2_coverage_other_elements_of_govt_not_captured_in_1(contingent_liability_other_elements_pct_gdp=self.contingent_liability_other_elements_pct_gdp)

    @cached_property
    def in2_coverage_soe_s_debt_guaranteed_not_guaranteed_government(self) -> int | str:
        return internals.in2_coverage_soe_s_debt_guaranteed_not_guaranteed_government(contingent_liability_soe_debt_pct_gdp=self.contingent_liability_soe_debt_pct_gdp)

    @cached_property
    def input6_tailored_params(self) -> data.Series[float | str | None]:
        return internals.input6_tailored_params(input6_tailored_params_fuel_label=self.input6_tailored_params_fuel_label)

    @cached_property
    def input6_tailored_params_fuel_label(self) -> str | int | float | bool:
        return internals.input6_tailored_params_fuel_label(imported_commodity_prices=self.imported_commodity_prices)

    @cached_property
    def input7_residual_params_sparse(self) -> float | str:
        return internals.input7_residual_params_sparse(ext_debt_marginal_share_domestic_st_residual_financing=self.ext_debt_marginal_share_domestic_st_residual_financing)

    @cached_property
    def leftover_inflation_gdp_deflator(self) -> str | int | float | bool:
        return internals.leftover_inflation_gdp_deflator(input6_standard_user_defined_threshold=self.input6_standard_user_defined_threshold)

    @cached_property
    def leftover_nominal_interest_rate(self) -> float | str:
        return internals.leftover_nominal_interest_rate(input6_tailored_params_3=self.input6_tailored_params_3)

    @cached_property
    def leftover_official_transfers_gdp(self) -> float | str:
        return internals.leftover_official_transfers_gdp(in6_tailored_adjusted_share_of_commodities_in_total_exports=self.in6_tailored_adjusted_share_of_commodities_in_total_exports)

    @cached_property
    def leftover_real_gdp_growth_2(self) -> float | str:
        return internals.leftover_real_gdp_growth_2(input6_tailored_params_3=self.input6_tailored_params_3)

    @cached_property
    def leftover_us_gdp_deflator_2(self) -> int | str:
        return internals.leftover_us_gdp_deflator_2(input6_standard_params=self.input6_standard_params)

    @cached_property
    def lookup_afg(self) -> str | int | float | bool:
        return internals.lookup_afg(translation_input_1_basics_residency_based=data.TRANSLATION_INPUT_1_BASICS_RESIDENCY_BASED)

    @cached_property
    def macro_debt_data(self) -> int | str:
        return internals.macro_debt_data(first_projection_year=self.first_projection_year)

    @cached_property
    def macro_debt_main_assumptions_further_details(self) -> int | str:
        return internals.macro_debt_main_assumptions_further_details(macro_debt_data=self.macro_debt_data)

    @cached_property
    def realism1_external_debt_flow_components(self) -> data.Realism1ExternalDebtFlowComponents:
        return internals.realism1_external_debt_flow_components(translation_external_flow_phrases=data.TRANSLATION_EXTERNAL_FLOW_PHRASES, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def realism1_external_debt_creating_flows(self) -> data.Realism1ExternalDebtCreatingFlows:
        return internals.realism1_external_debt_creating_flows(realism1_external_current_vintage_projection=self.realism1_external_current_vintage_projection)

    @cached_property
    def realism1_external_forecast_error_component_labels(self) -> data.Realism1ExternalForecastErrorComponentLabels:
        return internals.realism1_external_forecast_error_component_labels(realism1_external_forecast_error_component_names=self.realism1_external_forecast_error_component_names)

    @cached_property
    def realism1_external_forecast_error_components(self) -> data.Realism1ExternalForecastErrorComponents:
        return internals.realism1_external_forecast_error_components(realism1_external_five_year_flow_changes=self.realism1_external_five_year_flow_changes)

    @cached_property
    def realism1_external_forecast_error_distribution_labels(self) -> data.Realism1ExternalForecastErrorDistributionLabels:
        return internals.realism1_external_forecast_error_distribution_labels(realism1_external_median_label=self.realism1_external_median_label, translation_debt_change_phrases=data.TRANSLATION_DEBT_CHANGE_PHRASES, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def realism1_external_forecast_error_distribution(self) -> data.Realism1ExternalForecastErrorDistribution:
        return internals.realism1_external_forecast_error_distribution(realism1_external_projected_change_callouts=self.realism1_external_projected_change_callouts)

    @cached_property
    def realism1_external_vintage_years(self) -> data.Realism1ExternalVintageYears:
        return internals.realism1_external_vintage_years(realism1_external_year_headers=self.realism1_external_year_headers)

    @cached_property
    def realism1_external_vintage_debt_paths(self) -> data.Realism1ExternalVintageDebtPaths:
        return internals.realism1_external_vintage_debt_paths(realism1_external_current_vintage_projection=self.realism1_external_current_vintage_projection, realism1_external_five_years_ago_rebased_projection=self.realism1_external_five_years_ago_rebased_projection, realism1_external_last_vintage_rebased_projection=self.realism1_external_last_vintage_rebased_projection)

    @cached_property
    def realism1_public_debt_flow_components(self) -> data.Realism1PublicDebtFlowComponents:
        return internals.realism1_public_debt_flow_components(translation_public_flow_phrases=data.TRANSLATION_PUBLIC_FLOW_PHRASES, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def realism1_public_debt_creating_flows(self) -> data.Realism1PublicDebtCreatingFlows:
        return internals.realism1_public_debt_creating_flows(realism1_public_current_vintage_projection=self.realism1_public_current_vintage_projection)

    @cached_property
    def realism1_public_forecast_error_component_labels(self) -> data.Realism1PublicForecastErrorComponentLabels:
        return internals.realism1_public_forecast_error_component_labels(realism1_public_forecast_error_component_names=self.realism1_public_forecast_error_component_names)

    @cached_property
    def realism1_public_forecast_error_components(self) -> data.Realism1PublicForecastErrorComponents:
        return internals.realism1_public_forecast_error_components(realism1_public_five_year_flow_changes=self.realism1_public_five_year_flow_changes)

    @cached_property
    def realism1_public_forecast_error_lower_quartile(self) -> float | str:
        return internals.realism1_public_forecast_error_lower_quartile(realism1_public_last_vintage_projected_change=data.REALISM1_PUBLIC_LAST_VINTAGE_PROJECTED_CHANGE)

    @cached_property
    def realism1_public_forecast_error_distribution_labels(self) -> data.Realism1PublicForecastErrorDistributionLabels:
        return internals.realism1_public_forecast_error_distribution_labels(realism1_public_projected_change_callout_labels=self.realism1_public_projected_change_callout_labels)

    @cached_property
    def realism1_public_forecast_error_distribution(self) -> data.Realism1PublicForecastErrorDistribution:
        return internals.realism1_public_forecast_error_distribution(realism1_public_projected_change_callouts=self.realism1_public_projected_change_callouts)

    @cached_property
    def realism1_public_vintage_years(self) -> data.Realism1PublicVintageYears:
        return internals.realism1_public_vintage_years(realism1_public_year_headers=self.realism1_public_year_headers)

    @cached_property
    def realism1_public_vintage_debt_paths(self) -> data.Realism1PublicVintageDebtPaths:
        return internals.realism1_public_vintage_debt_paths(realism1_public_current_vintage_projection=self.realism1_public_current_vintage_projection, realism1_public_five_years_ago_rebased_projection=self.realism1_public_five_years_ago_rebased_projection, realism1_public_last_vintage_stock_copies=self.realism1_public_last_vintage_stock_copies)

    @cached_property
    def realism2_fiscal_adjustment_multiplier_labels(self) -> data.Realism2FiscalAdjustmentMultiplierLabels:
        return internals.realism2_fiscal_adjustment_multiplier_labels(realism2_multiplier_values=data.REALISM2_MULTIPLIER_VALUES)

    @cached_property
    def realism2_underlying_growth_multiplier_labels(self) -> data.Realism2UnderlyingGrowthMultiplierLabels:
        return internals.realism2_underlying_growth_multiplier_labels(realism2_multiplier_values=data.REALISM2_MULTIPLIER_VALUES)

    @cached_property
    def realism2_fiscal_adjustment_years(self) -> data.Realism2FiscalAdjustmentYears:
        return internals.realism2_fiscal_adjustment_years(realism2_history_years=self.realism2_history_years)

    @cached_property
    def realism2_underlying_growth_years(self) -> data.Realism2UnderlyingGrowthYears:
        return internals.realism2_underlying_growth_years(realism2_fiscal_adjustment_years=self.realism2_fiscal_adjustment_years)

    @cached_property
    def realism2_baseline_growth(self) -> data.Realism2BaselineGrowth:
        return internals.realism2_baseline_growth(realism2_real_gdp_growth=self.realism2_real_gdp_growth)

    @cached_property
    def realism2_growth_t_minus_1(self) -> data.Realism2GrowthTMinus1:
        return internals.realism2_growth_t_minus_1(realism2_baseline_growth=self.realism2_baseline_growth)

    @cached_property
    def realism2_fiscal_adjustment_growth_impact(self) -> data.Realism2FiscalAdjustmentGrowthImpact:
        return internals.realism2_fiscal_adjustment_growth_impact(realism2_growth_impact_multiplier_0_2_cumulative=self.realism2_growth_impact_multiplier_0_2_cumulative, realism2_growth_impact_multiplier_0_4_cumulative=self.realism2_growth_impact_multiplier_0_4_cumulative, realism2_growth_impact_multiplier_0_6_cumulative=self.realism2_growth_impact_multiplier_0_6_cumulative, realism2_growth_impact_multiplier_0_8_cumulative=self.realism2_growth_impact_multiplier_0_8_cumulative, realism2_growth_impact_multiplier_1_0_cumulative=self.realism2_growth_impact_multiplier_1_0_cumulative)

    @cached_property
    def realism2_underlying_growth(self) -> data.Realism2UnderlyingGrowth:
        return internals.realism2_underlying_growth(realism2_growth_t_minus_1=self.realism2_growth_t_minus_1, realism2_fiscal_adjustment_growth_impact=self.realism2_fiscal_adjustment_growth_impact)

    @cached_property
    def realism3_investment_years(self) -> data.Realism3InvestmentYears:
        return internals.realism3_investment_years(realism3_first_projection_year=self.realism3_first_projection_year)

    @cached_property
    def realism3_investment_path_labels(self) -> data.Realism3InvestmentPathLabels:
        return internals.realism3_investment_path_labels(translation_investment_phrases=data.TRANSLATION_INVESTMENT_PHRASES, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def realism3_public_private_investment_paths(self) -> data.Realism3PublicPrivateInvestmentPaths:
        return internals.realism3_public_private_investment_paths(realism3_public_investment_ratio_by_vintage=self.realism3_public_investment_ratio_by_vintage, realism3_private_investment_ratio_by_vintage=self.realism3_private_investment_ratio_by_vintage)

    @cached_property
    def realism3_growth_accounting_vintages(self) -> data.Realism3GrowthAccountingVintages:
        return internals.realism3_growth_accounting_vintages(translation_projection_phrases=data.TRANSLATION_PROJECTION_PHRASES, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def realism3_growth_accounting_contributions(self) -> data.Realism3GrowthAccountingContributions:
        return internals.realism3_growth_accounting_contributions(realism3_growth_contributions=self.realism3_growth_contributions)

    @cached_property
    def realism4_projected_3yr_adjustment_label(self) -> str | int | float | bool:
        return internals.realism4_projected_3yr_adjustment_label(translation_adjustment_phrase=data.TRANSLATION_ADJUSTMENT_PHRASE, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def realism4_projected_3yr_adjustment(self) -> float | str:
        return internals.realism4_projected_3yr_adjustment(realism4_three_year_adjustment=self.realism4_three_year_adjustment)

    @cached_property
    def realism4_projected_3yr_adjustment_bin(self) -> float | str:
        return internals.realism4_projected_3yr_adjustment_bin(realism4_projected_3yr_adjustment=self.realism4_projected_3yr_adjustment)

    @cached_property
    def realism4_projected_3yr_adjustment_category(self) -> float | str:
        return internals.realism4_projected_3yr_adjustment_category(realism4_projected_3yr_adjustment_bin=self.realism4_projected_3yr_adjustment_bin, realism4_fiscal_adjustment_bin_edges=data.REALISM4_FISCAL_ADJUSTMENT_BIN_EDGES, realism4_fiscal_adjustment_bin_frequencies=data.REALISM4_FISCAL_ADJUSTMENT_BIN_FREQUENCIES, realism4_fiscal_adjustment_bin_categories=data.REALISM4_FISCAL_ADJUSTMENT_BIN_CATEGORIES)

    @cached_property
    def realism4_projected_3yr_adjustment_sample_share(self) -> float | str:
        return internals.realism4_projected_3yr_adjustment_sample_share(realism4_projected_3yr_adjustment_category=self.realism4_projected_3yr_adjustment_category, realism4_fiscal_adjustment_bin_categories=data.REALISM4_FISCAL_ADJUSTMENT_BIN_CATEGORIES, realism4_fiscal_adjustment_sample_share=self.realism4_fiscal_adjustment_sample_share)

    @cached_property
    def realism4_fiscal_adjustment_top_bin_label(self) -> str | int | float | bool:
        return internals.realism4_fiscal_adjustment_top_bin_label(translation_more_phrase=data.TRANSLATION_MORE_PHRASE, start_debt_sustainability_analysis_m=self.start_debt_sustainability_analysis_m)

    @cached_property
    def realism4_fiscal_adjustment_sample_share(self) -> data.Realism4FiscalAdjustmentSampleShare:
        return internals.realism4_fiscal_adjustment_sample_share(realism4_fiscal_adjustment_bin_frequencies=data.REALISM4_FISCAL_ADJUSTMENT_BIN_FREQUENCIES)

    @cached_property
    def realism4_fiscal_adjustment_cumulative_share(self) -> data.Realism4FiscalAdjustmentCumulativeShare:
        return internals.realism4_fiscal_adjustment_cumulative_share(realism4_fiscal_adjustment_sample_share=self.realism4_fiscal_adjustment_sample_share)

    @cached_property
    def probability_pv_debt_to_gdp(self) -> data.ProbabilityPvDebtToGdp:
        return internals.probability_pv_debt_to_gdp(probability_borderline_bandwidth=data.PROBABILITY_BORDERLINE_BANDWIDTH, chart_output_pv_debt_gdp_ratio=self.chart_output_pv_debt_gdp_ratio)

    @cached_property
    def probability_pv_debt_to_exports(self) -> data.ProbabilityPvDebtToExports:
        return internals.probability_pv_debt_to_exports(probability_borderline_bandwidth=data.PROBABILITY_BORDERLINE_BANDWIDTH, chart_output_pv_debt_to_exports=self.chart_output_pv_debt_to_exports)

    @cached_property
    def probability_debt_service_to_exports(self) -> data.ProbabilityDebtServiceToExports:
        return internals.probability_debt_service_to_exports(probability_borderline_bandwidth=data.PROBABILITY_BORDERLINE_BANDWIDTH, chart_output_debt_service_to_exports=self.chart_output_debt_service_to_exports)

    @cached_property
    def probability_debt_service_to_revenue(self) -> data.ProbabilityDebtServiceToRevenue:
        return internals.probability_debt_service_to_revenue(probability_borderline_bandwidth=data.PROBABILITY_BORDERLINE_BANDWIDTH, chart_output_debt_service_to_revenue=self.chart_output_debt_service_to_revenue)

    @cached_property
    def probability_pv_debt_to_gdp_distress(self) -> data.ProbabilityPvDebtToGdpDistress:
        return internals.probability_pv_debt_to_gdp_distress(probability_debt_carrying_capacity_paths=self.probability_debt_carrying_capacity_paths, probability_regression_diagonal=data.PROBABILITY_REGRESSION_DIAGONAL, probability_distress_thresholds=data.PROBABILITY_DISTRESS_THRESHOLDS, probability_regression_coefficients=data.PROBABILITY_REGRESSION_COEFFICIENTS, probability_pv_debt_to_gdp=self.probability_pv_debt_to_gdp)

    @cached_property
    def probability_pv_debt_to_exports_distress(self) -> data.ProbabilityPvDebtToExportsDistress:
        return internals.probability_pv_debt_to_exports_distress(probability_debt_carrying_capacity_paths=self.probability_debt_carrying_capacity_paths, probability_regression_diagonal=data.PROBABILITY_REGRESSION_DIAGONAL, probability_distress_thresholds=data.PROBABILITY_DISTRESS_THRESHOLDS, probability_regression_coefficients=data.PROBABILITY_REGRESSION_COEFFICIENTS, probability_pv_debt_to_exports=self.probability_pv_debt_to_exports)

    @cached_property
    def probability_debt_service_to_exports_distress(self) -> data.ProbabilityDebtServiceToExportsDistress:
        return internals.probability_debt_service_to_exports_distress(probability_debt_carrying_capacity_paths=self.probability_debt_carrying_capacity_paths, probability_regression_diagonal=data.PROBABILITY_REGRESSION_DIAGONAL, probability_distress_thresholds=data.PROBABILITY_DISTRESS_THRESHOLDS, probability_regression_coefficients=data.PROBABILITY_REGRESSION_COEFFICIENTS, probability_debt_service_to_exports=self.probability_debt_service_to_exports)

    @cached_property
    def probability_debt_service_to_revenue_distress(self) -> data.ProbabilityDebtServiceToRevenueDistress:
        return internals.probability_debt_service_to_revenue_distress(probability_debt_carrying_capacity_paths=self.probability_debt_carrying_capacity_paths, probability_regression_diagonal=data.PROBABILITY_REGRESSION_DIAGONAL, probability_distress_thresholds=data.PROBABILITY_DISTRESS_THRESHOLDS, probability_regression_coefficients=data.PROBABILITY_REGRESSION_COEFFICIENTS, probability_debt_service_to_revenue=self.probability_debt_service_to_revenue)

    @cached_property
    def external_dsa_risk_rating_signal(self) -> str | int | float | bool:
        return internals.external_dsa_risk_rating_signal(external_dsa_risk_rating_numeric=self.external_dsa_risk_rating_numeric, chart_numeric_risk_rating=data.CHART_NUMERIC_RISK_RATING, chart_numeric_risk_header=data.CHART_NUMERIC_RISK_HEADER, chart_label_risk_header=data.CHART_LABEL_RISK_HEADER, chart_risk_labels=data.CHART_RISK_LABELS)

    @cached_property
    def external_dsa_risk_rating_numeric(self) -> float | str:
        return internals.external_dsa_risk_rating_numeric(external_baseline_breach=self.external_baseline_breach, external_shock_breach=self.external_shock_breach)

    @cached_property
    def external_baseline_breach(self) -> float | str:
        return internals.external_baseline_breach(chart_years_of_breaches_to_exclude=data.CHART_YEARS_OF_BREACHES_TO_EXCLUDE, chart_chart_data_pv_debt_to_gdp_baseline_breach_count=self.chart_chart_data_pv_debt_to_gdp_baseline_breach_count, chart_chart_data_pv_debt_to_exports_baseline_breach_count=self.chart_chart_data_pv_debt_to_exports_baseline_breach_count, chart_chart_data_debt_service_to_exports_baseline_breach_count=self.chart_chart_data_debt_service_to_exports_baseline_breach_count, chart_chart_data_debt_service_to_revenue_baseline_breach_count=self.chart_chart_data_debt_service_to_revenue_baseline_breach_count)

    @cached_property
    def external_shock_breach(self) -> float | str:
        return internals.external_shock_breach(chart_years_of_breaches_to_exclude=data.CHART_YEARS_OF_BREACHES_TO_EXCLUDE, chart_chart_data_pv_debt_to_gdp_shock_breach_count=self.chart_chart_data_pv_debt_to_gdp_shock_breach_count, chart_chart_data_pv_debt_to_exports_shock_breach_count=self.chart_chart_data_pv_debt_to_exports_shock_breach_count, chart_chart_data_debt_service_to_exports_shock_breach_count=self.chart_chart_data_debt_service_to_exports_shock_breach_count, chart_chart_data_debt_service_to_revenue_shock_breach_count=self.chart_chart_data_debt_service_to_revenue_shock_breach_count)

    @cached_property
    def external_pv_debt_to_gdp_mx_shock(self) -> str | int | float | bool:
        return internals.external_pv_debt_to_gdp_mx_shock(chart_chart_data_pv_debt_to_gdp_most_extreme_shock=self.chart_chart_data_pv_debt_to_gdp_most_extreme_shock)

    @cached_property
    def external_pv_debt_to_exports_mx_shock(self) -> str | int | float | bool:
        return internals.external_pv_debt_to_exports_mx_shock(chart_chart_data_pv_debt_to_exports_most_extreme_shock=self.chart_chart_data_pv_debt_to_exports_most_extreme_shock)

    @cached_property
    def external_debt_service_to_exports_mx_shock(self) -> str | int | float | bool:
        return internals.external_debt_service_to_exports_mx_shock(chart_chart_data_debt_service_to_exports_most_extreme_shock=self.chart_chart_data_debt_service_to_exports_most_extreme_shock)

    @cached_property
    def external_debt_service_to_revenue_mx_shock(self) -> str | int | float | bool:
        return internals.external_debt_service_to_revenue_mx_shock(chart_chart_data_debt_service_to_revenue_most_extreme_shock=self.chart_chart_data_debt_service_to_revenue_most_extreme_shock)

    @cached_property
    def fiscal_risk_rating_signal(self) -> str | int | float | bool:
        return internals.fiscal_risk_rating_signal(fiscal_risk_rating_numeric=self.fiscal_risk_rating_numeric, chart_numeric_risk_rating=data.CHART_NUMERIC_RISK_RATING, chart_risk_labels=data.CHART_RISK_LABELS)

    @cached_property
    def fiscal_risk_rating_numeric(self) -> float | str:
        return internals.fiscal_risk_rating_numeric(fiscal_baseline_breach=self.fiscal_baseline_breach, fiscal_shock_breach=self.fiscal_shock_breach)

    @cached_property
    def fiscal_baseline_breach(self) -> float | str:
        return internals.fiscal_baseline_breach(chart_chart_data_pv_of_debt_to_gdp_ratio_baseline_breach_count=self.chart_chart_data_pv_of_debt_to_gdp_ratio_baseline_breach_count, chart_years_of_breaches_to_exclude=data.CHART_YEARS_OF_BREACHES_TO_EXCLUDE)

    @cached_property
    def fiscal_shock_breach(self) -> float | str:
        return internals.fiscal_shock_breach(chart_chart_data_pv_of_debt_to_gdp_ratio_shock_breach_count=self.chart_chart_data_pv_of_debt_to_gdp_ratio_shock_breach_count, chart_years_of_breaches_to_exclude=data.CHART_YEARS_OF_BREACHES_TO_EXCLUDE)

    @cached_property
    def fiscal_pv_debt_to_gdp_mx_shock(self) -> str | int | float | bool:
        return internals.fiscal_pv_debt_to_gdp_mx_shock(chart_chart_data_pv_of_debt_to_gdp_ratio_most_extreme_shock=self.chart_chart_data_pv_of_debt_to_gdp_ratio_most_extreme_shock)

    @cached_property
    def tailored_stress_natural_disaster_applicable(self) -> float | str:
        return internals.tailored_stress_natural_disaster_applicable(in6_tailored_natdisaster=self.in6_tailored_natdisaster)

    @cached_property
    def tailored_stress_commodity_price_applicable(self) -> float | str:
        return internals.tailored_stress_commodity_price_applicable(in6_tailored_commodity_price=self.in6_tailored_commodity_price)

    @cached_property
    def tailored_stress_market_financing_applicable(self) -> float | str:
        return internals.tailored_stress_market_financing_applicable(in6_tailored_mkt_financing=self.in6_tailored_mkt_financing)

    @cached_property
    def fiscal_space_moderate_risk_signal(self) -> str | int | float | bool:
        return internals.fiscal_space_moderate_risk_signal(fiscal_space_some_threshold=data.FISCAL_SPACE_SOME_THRESHOLD, fiscal_space_substantial_threshold=data.FISCAL_SPACE_SUBSTANTIAL_THRESHOLD, chart_fiscal_space_pv_of_debt_to_gdp_max_baseline_breach=self.chart_fiscal_space_pv_of_debt_to_gdp_max_baseline_breach, chart_fiscal_space_pv_of_debt_to_exports_max_baseline_breach=self.chart_fiscal_space_pv_of_debt_to_exports_max_baseline_breach, chart_fiscal_space_debt_service_to_exports_max_baseline_breach=self.chart_fiscal_space_debt_service_to_exports_max_baseline_breach, chart_fiscal_space_debt_service_to_revenue_max_baseline_breach=self.chart_fiscal_space_debt_service_to_revenue_max_baseline_breach)

    @cached_property
    def overall_risk_rating_signal(self) -> str | int | float | bool:
        return internals.overall_risk_rating_signal(overall_risk_rating_numeric=self.overall_risk_rating_numeric, chart_numeric_risk_rating=data.CHART_NUMERIC_RISK_RATING, chart_risk_labels=data.CHART_RISK_LABELS)

    @cached_property
    def overall_risk_rating_numeric(self) -> float | str:
        return internals.overall_risk_rating_numeric(external_dsa_risk_rating_numeric=self.external_dsa_risk_rating_numeric, fiscal_risk_rating_numeric=self.fiscal_risk_rating_numeric)

    @cached_property
    def chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue(self) -> data.ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenue:
        return internals.chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue(chart_tailored_test_marker=data.CHART_TAILORED_TEST_MARKER, dsa_pub_pv_of_public_debt_to_revenue_and_grants_ratio=self.dsa_pub_pv_of_public_debt_to_revenue_and_grants_ratio, customized_public_include_scenario=self.customized_public_include_scenario, chart_chart_data_pv_of_debt_to_revenue_ratio_c2_natural_disaster_stres=self.chart_chart_data_pv_of_debt_to_revenue_ratio_c2_natural_disaster_stres, chart_chart_data_pv_of_debt_to_revenue_ratio_c3_commodity_price_stress=self.chart_chart_data_pv_of_debt_to_revenue_ratio_c3_commodity_price_stress, chart_chart_data_pv_of_debt_to_revenue_ratio_c4_market_financing_stres=self.chart_chart_data_pv_of_debt_to_revenue_ratio_c4_market_financing_stres, chart_pv_of_debt_to_revenue_ratio_applicable_flag_b2_1_primary_balance_market=self.chart_pv_of_debt_to_revenue_ratio_applicable_flag_b2_1_primary_balance_market, chart_pv_of_debt_to_revenue_ratio_applicable_flag_combined_market_financing_stress=self.chart_pv_of_debt_to_revenue_ratio_applicable_flag_combined_market_financing_stress, chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue_stress_path=self.chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue_stress_path, chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue_figure=self.chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue_figure, baseline_pub_pv_of_public_debt_revenue_grants_ratio=self.baseline_pub_pv_of_public_debt_revenue_grants_ratio, baseline_pub_pv_of_public_debt_revenue_grants_ratio_exports_shock=self.baseline_pub_pv_of_public_debt_revenue_grants_ratio_exports_shock, baseline_pub_pv_of_public_debt_revenue_grants_ratio_b4_other=self.baseline_pub_pv_of_public_debt_revenue_grants_ratio_b4_other, custom_pub_pv_of_public_debt_revenue_grants_ratio=self.custom_pub_pv_of_public_debt_revenue_grants_ratio, in6opt_standard_scenario=self.in6opt_standard_scenario)

    @cached_property
    def chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue(self) -> data.ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenue:
        return internals.chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue(chart_tailored_test_marker=data.CHART_TAILORED_TEST_MARKER, dsa_pub_debt_service_to_revenue_and_grants_ratio_in_percent=self.dsa_pub_debt_service_to_revenue_and_grants_ratio_in_percent, customized_public_include_scenario=self.customized_public_include_scenario, chart_chart_data_debt_service_to_revenue_ratio_c2_natural_disaster_str=self.chart_chart_data_debt_service_to_revenue_ratio_c2_natural_disaster_str, chart_chart_data_debt_service_to_revenue_ratio_c3_commodity_price_stre=self.chart_chart_data_debt_service_to_revenue_ratio_c3_commodity_price_stre, chart_chart_data_debt_service_to_revenue_ratio_c4_market_financing_str=self.chart_chart_data_debt_service_to_revenue_ratio_c4_market_financing_str, chart_applicable_flag_b2_1_primary_balance_market=self.chart_applicable_flag_b2_1_primary_balance_market, chart_applicable_flag_combined_market_financing_stress=self.chart_applicable_flag_combined_market_financing_stress, chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue_stress_path=self.chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue_stress_path, chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue_figure=self.chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue_figure, baseline_pub_debt_service_revenue_grants_ratio=self.baseline_pub_debt_service_revenue_grants_ratio, baseline_pub_debt_service_revenue_grants_ratio_b3_exports=self.baseline_pub_debt_service_revenue_grants_ratio_b3_exports, baseline_pub_debt_service_revenue_grants_ratio_b4_other_flows=self.baseline_pub_debt_service_revenue_grants_ratio_b4_other_flows, custom_pub_debt_service_revenue_grants_ratio=self.custom_pub_debt_service_revenue_grants_ratio, in6opt_standard_scenario=self.in6opt_standard_scenario)

    @cached_property
    def chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio(self) -> data.ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatio:
        return internals.chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio(chart_tailored_test_marker=data.CHART_TAILORED_TEST_MARKER, dsa_pub_debt_service_to_gdp_ratio_in_percent=self.dsa_pub_debt_service_to_gdp_ratio_in_percent, customized_public_include_scenario=self.customized_public_include_scenario, chart_chart_data_debt_service_to_gdp_ratio_c2_natural_disaster_stress_=self.chart_chart_data_debt_service_to_gdp_ratio_c2_natural_disaster_stress_, chart_chart_data_debt_service_to_gdp_ratio_c3_commodity_price_stress_p=self.chart_chart_data_debt_service_to_gdp_ratio_c3_commodity_price_stress_p, chart_chart_data_debt_service_to_gdp_ratio_c4_market_financing_stress_=self.chart_chart_data_debt_service_to_gdp_ratio_c4_market_financing_stress_, chart_debt_service_to_gdp_ratio_applicable_flag_b2_1_primary_balance_market=self.chart_debt_service_to_gdp_ratio_applicable_flag_b2_1_primary_balance_market, chart_debt_service_to_gdp_ratio_applicable_flag_combined_market_financing_stress=self.chart_debt_service_to_gdp_ratio_applicable_flag_combined_market_financing_stress, chart_internal_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio_stress_path=self.chart_internal_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio_stress_path, chart_internal_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio_figure=self.chart_internal_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio_figure, baseline_pub_debt_service_gdp_ratio_baseline=self.baseline_pub_debt_service_gdp_ratio_baseline, baseline_pub_debt_service_gdp_ratio_b3_exports=self.baseline_pub_debt_service_gdp_ratio_b3_exports, baseline_pub_debt_service_gdp_ratio_b4_other_flows=self.baseline_pub_debt_service_gdp_ratio_b4_other_flows, custom_pub_debt_service_gdp_ratio=self.custom_pub_debt_service_gdp_ratio, in6opt_standard_scenario=self.in6opt_standard_scenario)

    @cached_property
    def chart_pv_debt_gdp_ratio_custom_alternative_scenario(self) -> data.ChartPvDebtGdpRatioCustomAlternativeScenario:
        return internals.chart_pv_debt_gdp_ratio_custom_alternative_scenario(custom_ext_pv_ppg_ext_debt_gdp_ratio=self.custom_ext_pv_ppg_ext_debt_gdp_ratio, custom_ext_include_external_customized_scenario_in_charts=self.custom_ext_include_external_customized_scenario_in_charts)

    @cached_property
    def chart_pv_debt_to_exports_custom_alternative_scenario(self) -> data.ChartPvDebtToExportsCustomAlternativeScenario:
        return internals.chart_pv_debt_to_exports_custom_alternative_scenario(custom_ext_pv_ppg_ext_debt_exports_ratio=self.custom_ext_pv_ppg_ext_debt_exports_ratio, custom_ext_include_external_customized_scenario_in_charts=self.custom_ext_include_external_customized_scenario_in_charts)

    @cached_property
    def chart_debt_service_to_exports_custom_alternative_scenario(self) -> data.ChartDebtServiceToExportsCustomAlternativeScenario:
        return internals.chart_debt_service_to_exports_custom_alternative_scenario(custom_ext_ppg_debt_service_to_exports=self.custom_ext_ppg_debt_service_to_exports, custom_ext_include_external_customized_scenario_in_charts=self.custom_ext_include_external_customized_scenario_in_charts)

    @cached_property
    def chart_debt_service_to_revenue_custom_alternative_scenario(self) -> data.ChartDebtServiceToRevenueCustomAlternativeScenario:
        return internals.chart_debt_service_to_revenue_custom_alternative_scenario(custom_ext_ppg_debt_service_to_revenue=self.custom_ext_ppg_debt_service_to_revenue, custom_ext_include_external_customized_scenario_in_charts=self.custom_ext_include_external_customized_scenario_in_charts)

    @cached_property
    def chart_pv_debt_to_revenue_mx_shock_standard_tailored(self) -> data.ChartPvDebtToRevenueMxShockStandardTailored:
        return internals.chart_pv_debt_to_revenue_mx_shock_standard_tailored(chart_projection_years=self.chart_projection_years, chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue=self.chart_internal_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue, chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue=self.chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue)

    @cached_property
    def chart_output_debt_service_to_revenue_fiscal(self) -> data.ChartOutputDebtServiceToRevenueFiscal:
        return internals.chart_output_debt_service_to_revenue_fiscal(chart_projection_years=self.chart_projection_years, chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue=self.chart_internal_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue, chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue=self.chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue)

    @cached_property
    def pv_base_multilaterals(self) -> data.Series[int | str | None]:
        return internals.pv_base_multilaterals(pv_base_constant_discount_schedule_period=data.PV_BASE_CONSTANT_DISCOUNT_SCHEDULE_PERIOD, pv_base_discount_schedule_period=self.pv_base_discount_schedule_period)

    @cached_property
    def _scan_pv_base_multilaterals_by_year(self) -> internals.ScanPvBaseMultilateralsByYearResult:
        return internals.scan_pv_base_multilaterals_by_year(macro_debt_data=self.macro_debt_data)

    @cached_property
    def pv_base_multilaterals_by_year(self) -> data.Series[int | str | None]:
        return self._scan_pv_base_multilaterals_by_year.pv_base_multilaterals_by_year

    @cached_property
    def pv_base_grace_ida_regular_by_year(self) -> data.Series[int | str | None]:
        return self._scan_pv_base_multilaterals_by_year.pv_base_grace_ida_regular_by_year

    @cached_property
    def pv_base_output_projection_year(self) -> data.Series[int | str | None]:
        return self._scan_pv_base_multilaterals_by_year.pv_base_output_projection_year

    @cached_property
    def pv_base_block_grace(self) -> data.Series[float | str | None]:
        return internals.pv_base_block_grace(input4_grace_period=self.input4_grace_period, input4_terms_ida_regular=self.input4_terms_ida_regular, input4_terms_ida_and_lc=self.input4_terms_ida_and_lc)

    @cached_property
    def pv_base_block_maturity(self) -> data.Series[float | str | None]:
        return internals.pv_base_block_maturity(input4_loan_maturity=self.input4_loan_maturity, input4_terms_ida_regular=self.input4_terms_ida_regular, input4_terms_ida_and_lc=self.input4_terms_ida_and_lc)

    @cached_property
    def pv_base_block_interest(self) -> data.Series[float | str | None]:
        return internals.pv_base_block_interest(input4_interest_rate=self.input4_interest_rate, input4_terms_ida_regular=self.input4_terms_ida_regular, input4_terms_ida_and_lc=self.input4_terms_ida_and_lc)

    @cached_property
    def pv_base_block_discount(self) -> data.Series[float | str | None]:
        return internals.pv_base_block_discount(input4_discount_rate=self.input4_discount_rate)

    @cached_property
    def pv_base_discount_debt_stock(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_debt_stock(pv_base_opening_percent_of_face=data.PV_BASE_OPENING_PERCENT_OF_FACE, pv_base_discount_amortization=self.pv_base_discount_amortization)

    @cached_property
    def pv_base_discount_amortization(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_amortization(pv_base_multilaterals=self.pv_base_multilaterals, pv_base_block_grace=self.pv_base_block_grace, pv_base_block_maturity=self.pv_base_block_maturity, pv_base_opening_percent_of_face=data.PV_BASE_OPENING_PERCENT_OF_FACE, pv_base_discount_repayment_schedule=self.pv_base_discount_repayment_schedule, pv_base_constant_discount_schedule_period=data.PV_BASE_CONSTANT_DISCOUNT_SCHEDULE_PERIOD, pv_base_discount_schedule_period=self.pv_base_discount_schedule_period, pv_base_block_index=self.pv_base_block_index)

    @cached_property
    def pv_base_discount_interest(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_interest(pv_base_multilaterals_by_year=self.pv_base_multilaterals_by_year, pv_base_block_interest=self.pv_base_block_interest, pv_base_discount_debt_stock=self.pv_base_discount_debt_stock)

    @cached_property
    def pv_base_discount_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_total_debt_service(pv_base_discount_amortization=self.pv_base_discount_amortization, pv_base_discount_interest=self.pv_base_discount_interest)

    @cached_property
    def pv_base_discount_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_pv_of_debt(pv_base_block_interest=self.pv_base_block_interest, pv_base_block_discount=self.pv_base_block_discount, pv_base_discount_debt_stock=self.pv_base_discount_debt_stock, pv_base_discount_total_debt_service=self.pv_base_discount_total_debt_service)

    @cached_property
    def pv_base_discount_t_g_0(self) -> data.Series[int | str | None]:
        return internals.pv_base_discount_t_g_0(pv_base_constant_discount_schedule_period=data.PV_BASE_CONSTANT_DISCOUNT_SCHEDULE_PERIOD, pv_base_block_grace=self.pv_base_block_grace, pv_base_discount_schedule_period=self.pv_base_discount_schedule_period, pv_base_block_index=self.pv_base_block_index)

    @cached_property
    def pv_base_discount_post_grace_cumulative(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_post_grace_cumulative(pv_base_discount_t_g_0=self.pv_base_discount_t_g_0, pv_base_output_cumulative=self.pv_base_output_cumulative, pv_base_input_output_cumulative=self.pv_base_input_output_cumulative)

    @cached_property
    def pv_base_discount_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.pv_base_discount_t_m_condition(pv_base_constant_discount_schedule_period=data.PV_BASE_CONSTANT_DISCOUNT_SCHEDULE_PERIOD, pv_base_block_maturity=self.pv_base_block_maturity, pv_base_discount_schedule_period=self.pv_base_discount_schedule_period, pv_base_block_index=self.pv_base_block_index)

    @cached_property
    def pv_base_discount_post_maturity_cumulative(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_post_maturity_cumulative(pv_base_discount_t_m_condition=self.pv_base_discount_t_m_condition, pv_base_output_cumulative=self.pv_base_output_cumulative, pv_base_input_output_cumulative=self.pv_base_input_output_cumulative)

    @cached_property
    def pv_base_output_new_forex_borrowing_gross_usd(self) -> data.Series[float | str | None]:
        return internals.pv_base_output_new_forex_borrowing_gross_usd(ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external)

    @cached_property
    def pv_base_output_cumulative(self) -> data.Series[float | str | None]:
        return internals.pv_base_output_cumulative(pv_base_output_new_forex_borrowing_gross_usd=self.pv_base_output_new_forex_borrowing_gross_usd)

    @cached_property
    def pv_base_output_stock_of_new_forex_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_base_output_stock_of_new_forex_debt_in_usd(pv_base_output_new_forex_borrowing_gross_usd=self.pv_base_output_new_forex_borrowing_gross_usd, pv_base_output_amortization=self.pv_base_output_amortization)

    @cached_property
    def pv_base_output_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.pv_base_output_pv_of_debt(pv_base_block_interest=self.pv_base_block_interest, pv_base_block_discount=self.pv_base_block_discount, pv_base_discount_pv_of_debt=self.pv_base_discount_pv_of_debt, pv_base_output_new_forex_borrowing_gross_usd=self.pv_base_output_new_forex_borrowing_gross_usd, pv_base_output_total_debt_service_in_usd=self.pv_base_output_total_debt_service_in_usd, pv_base_output_amortization=self.pv_base_output_amortization)

    @cached_property
    def pv_base_output_total_debt_service_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_base_output_total_debt_service_in_usd(pv_base_output_interest=self.pv_base_output_interest, pv_base_output_amortization=self.pv_base_output_amortization)

    @cached_property
    def pv_base_output_interest(self) -> data.Series[float | str | None]:
        return internals.pv_base_output_interest(pv_base_block_interest=self.pv_base_block_interest, pv_base_output_stock_of_new_forex_debt_in_usd=self.pv_base_output_stock_of_new_forex_debt_in_usd)

    @cached_property
    def pv_base_output_amortization(self) -> data.Series[float | str | None]:
        return internals.pv_base_output_amortization(pv_base_block_grace=self.pv_base_block_grace, pv_base_block_maturity=self.pv_base_block_maturity, pv_base_discount_post_grace_cumulative=self.pv_base_discount_post_grace_cumulative, pv_base_discount_post_maturity_cumulative=self.pv_base_discount_post_maturity_cumulative)

    @cached_property
    def pv_base_ida_terms_repayment_schedule(self) -> data.Series[float | str | None]:
        return internals.pv_base_ida_terms_repayment_schedule(input4_ida_scale_principal=data.INPUT4_IDA_SCALE_PRINCIPAL, input4_ida_scale_principal_internal=self.input4_ida_scale_principal_internal, input4_ida_scale_principal_share_internal=self.input4_ida_scale_principal_share_internal)

    @cached_property
    def pv_base_ida_terms_schedule_column_index(self) -> data.Series[int | str | None]:
        return internals.pv_base_ida_terms_schedule_column_index(pv_base_ida_scale_new_product_count=data.PV_BASE_IDA_SCALE_NEW_PRODUCT_COUNT)

    @cached_property
    def pv_base_discount_repayment_schedule(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_repayment_schedule(pv_base_ida_scale_name=data.PV_BASE_IDA_SCALE_NAME, pv_base_ida_scale_short_name=data.PV_BASE_IDA_SCALE_SHORT_NAME, pv_base_ida_terms_repayment_schedule=self.pv_base_ida_terms_repayment_schedule, pv_base_ida_scale_new_product_count=data.PV_BASE_IDA_SCALE_NEW_PRODUCT_COUNT, pv_base_ida_terms_schedule_column_index=self.pv_base_ida_terms_schedule_column_index, pv_base_instrument_title=self.pv_base_instrument_title, pv_base_discount_selected_instrument=self.pv_base_discount_selected_instrument)

    @cached_property
    def pv_base_instrument_title(self) -> data.Series[str | int | float | bool | None]:
        return internals.pv_base_instrument_title(input4_instrument_names=self.input4_instrument_names)

    @cached_property
    def pv_base_discount_schedule_period(self) -> data.Series[int | str | None]:
        return internals.pv_base_discount_schedule_period(pv_base_constant_discount_schedule_period=data.PV_BASE_CONSTANT_DISCOUNT_SCHEDULE_PERIOD)

    @cached_property
    def pv_base_discount_selected_instrument(self) -> data.Series[str | int | float | bool | None]:
        return internals.pv_base_discount_selected_instrument(input4_blend_scale_key=self.input4_blend_scale_key, input4_ida_scale_name=data.INPUT4_IDA_SCALE_NAME, pv_base_instrument_title=self.pv_base_instrument_title)

    @cached_property
    def pv_base_block_index(self) -> data.Series[int | str | None]:
        return internals.pv_base_block_index(pv_base_constant_discount_schedule_period=data.PV_BASE_CONSTANT_DISCOUNT_SCHEDULE_PERIOD, pv_base_discount_schedule_period=self.pv_base_discount_schedule_period)

    @cached_property
    def pv_base_block_index_fx(self) -> data.Series[int | str | None]:
        return internals.pv_base_block_index_fx(pv_base_constant_discount_schedule_period=data.PV_BASE_CONSTANT_DISCOUNT_SCHEDULE_PERIOD, pv_base_discount_schedule_period=self.pv_base_discount_schedule_period)

    @cached_property
    def pv_base_block_grace_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_block_grace_fx(input4_terms_bonds_fx_non_residents=self.input4_terms_bonds_fx_non_residents, input4_terms_bonds_fx_residents=self.input4_terms_bonds_fx_residents)

    @cached_property
    def pv_base_block_maturity_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_block_maturity_fx(input4_terms_bonds_fx_non_residents=self.input4_terms_bonds_fx_non_residents, input4_terms_bonds_fx_residents=self.input4_terms_bonds_fx_residents)

    @cached_property
    def pv_base_block_interest_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_block_interest_fx(input4_terms_bonds_fx_non_residents=self.input4_terms_bonds_fx_non_residents, input4_terms_bonds_fx_residents=self.input4_terms_bonds_fx_residents)

    @cached_property
    def pv_base_block_discount_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_block_discount_fx(input4_discount_rate_bonds_fx_non_residents=self.input4_discount_rate_bonds_fx_non_residents, input4_discount_rate_bonds_fx_residents=self.input4_discount_rate_bonds_fx_residents)

    @cached_property
    def pv_base_discount_debt_stock_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_debt_stock_fx(pv_base_opening_percent_of_face_fx=data.PV_BASE_OPENING_PERCENT_OF_FACE_FX, pv_base_discount_amortization_fx=self.pv_base_discount_amortization_fx)

    @cached_property
    def pv_base_discount_amortization_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_amortization_fx(pv_base_block_index_fx=self.pv_base_block_index_fx, pv_base_block_grace_fx=self.pv_base_block_grace_fx, pv_base_block_maturity_fx=self.pv_base_block_maturity_fx, pv_base_opening_percent_of_face_fx=data.PV_BASE_OPENING_PERCENT_OF_FACE_FX)

    @cached_property
    def pv_base_discount_interest_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_interest_fx(pv_base_block_interest_fx=self.pv_base_block_interest_fx, pv_base_discount_debt_stock_fx=self.pv_base_discount_debt_stock_fx)

    @cached_property
    def pv_base_discount_total_debt_service_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_total_debt_service_fx(pv_base_discount_amortization_fx=self.pv_base_discount_amortization_fx, pv_base_discount_interest_fx=self.pv_base_discount_interest_fx)

    @cached_property
    def pv_base_discount_pv_of_debt_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_discount_pv_of_debt_fx(pv_base_block_interest_fx=self.pv_base_block_interest_fx, pv_base_block_discount_fx=self.pv_base_block_discount_fx, pv_base_discount_debt_stock_fx=self.pv_base_discount_debt_stock_fx, pv_base_discount_total_debt_service_fx=self.pv_base_discount_total_debt_service_fx)

    @cached_property
    def pv_base_discount_t_g_0_fx(self) -> data.Series[int | str | None]:
        return internals.pv_base_discount_t_g_0_fx(pv_base_block_index_fx=self.pv_base_block_index_fx, pv_base_block_grace_fx=self.pv_base_block_grace_fx)

    @cached_property
    def pv_base_discount_t_m_condition_fx(self) -> data.Series[int | str | None]:
        return internals.pv_base_discount_t_m_condition_fx(pv_base_block_index_fx=self.pv_base_block_index_fx, pv_base_block_maturity_fx=self.pv_base_block_maturity_fx)

    @cached_property
    def pv_base_output_pv_of_debt_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_output_pv_of_debt_fx(pv_base_block_interest_fx=self.pv_base_block_interest_fx, pv_base_block_discount_fx=self.pv_base_block_discount_fx, pv_base_discount_pv_of_debt_fx=self.pv_base_discount_pv_of_debt_fx, pv_base_output_new_forex_borrowing_gross_usd_fx=self.pv_base_output_new_forex_borrowing_gross_usd_fx, pv_base_output_total_debt_service_in_usd_fx=self.pv_base_output_total_debt_service_in_usd_fx, pv_base_output_amortization_fx=self.pv_base_output_amortization_fx)

    @cached_property
    def pv_base_output_total_debt_service_in_usd_fx(self) -> data.Series[float | str | None]:
        return internals.pv_base_output_total_debt_service_in_usd_fx(pv_base_output_interest_fx=self.pv_base_output_interest_fx, pv_base_output_amortization_fx=self.pv_base_output_amortization_fx)

    @cached_property
    def pv_base_add_cost_mkt_shock_schedule_period(self) -> data.Series[int | str | None]:
        return internals.pv_base_add_cost_mkt_shock_schedule_period(pv_base_add_cost_mkt_opening_stock_percent_of_face=data.PV_BASE_ADD_COST_MKT_OPENING_STOCK_PERCENT_OF_FACE)

    @cached_property
    def pv_base_add_cost_mkt_whichever_lower(self) -> str | int | float | bool:
        return internals.pv_base_add_cost_mkt_whichever_lower(leftover_inflation_gdp_deflator=self.leftover_inflation_gdp_deflator)

    @cached_property
    def pv_base_add_cost_mkt_or(self) -> int | str:
        return internals.pv_base_add_cost_mkt_or(input6_tailored_params_2=self.input6_tailored_params_2)

    @cached_property
    def pv_base_add_cost_mkt_pb_baseline(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_pb_baseline(baseline_pub_primary_deficit=self.baseline_pub_primary_deficit)

    @cached_property
    def pv_base_add_cost_mkt_shock(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_shock(dsa_pub_primary_deficit=self.dsa_pub_primary_deficit)

    @cached_property
    def pv_base_add_cost_mkt_shock_deviation_from_baseline(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_shock_deviation_from_baseline(pv_base_add_cost_mkt_pb_baseline=self.pv_base_add_cost_mkt_pb_baseline, pv_base_add_cost_mkt_shock=self.pv_base_add_cost_mkt_shock)

    @cached_property
    def pv_base_add_cost_mkt_shock_increase_in_borrowing_costs(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_shock_increase_in_borrowing_costs(pv_base_add_cost_mkt_opening_percent_of_face=data.PV_BASE_ADD_COST_MKT_OPENING_PERCENT_OF_FACE, pv_base_add_cost_mkt_whichever_lower=self.pv_base_add_cost_mkt_whichever_lower, pv_base_add_cost_mkt_or=self.pv_base_add_cost_mkt_or, pv_base_add_cost_mkt_shock_deviation_from_baseline=self.pv_base_add_cost_mkt_shock_deviation_from_baseline)

    @cached_property
    def pv_base_add_cost_mkt_shock_average(self) -> float | str:
        return internals.pv_base_add_cost_mkt_shock_average(pv_base_add_cost_mkt_shock_increase_in_borrowing_costs=self.pv_base_add_cost_mkt_shock_increase_in_borrowing_costs)

    @cached_property
    def pv_base_add_cost_mkt_shock_addition_nominal_interest_payments_on_external_debt(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_shock_addition_nominal_interest_payments_on_external_debt(pv_base_add_cost_mkt_output_interest=self.pv_base_add_cost_mkt_output_interest)

    @cached_property
    def pv_base_add_cost_mkt_grace(self) -> data.Series[int | str | None]:
        return internals.pv_base_add_cost_mkt_grace(input4_grace_period=self.input4_grace_period)

    @cached_property
    def pv_base_add_cost_mkt_maturity(self) -> data.Series[int | str | None]:
        return internals.pv_base_add_cost_mkt_maturity(input4_loan_maturity=self.input4_loan_maturity)

    @cached_property
    def pv_base_add_cost_mkt_discount_interest_rate(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_discount_interest_rate(pv_base_add_cost_mkt_shock_average=self.pv_base_add_cost_mkt_shock_average)

    @cached_property
    def pv_base_add_cost_mkt_discount_t_g_0(self) -> data.Series[int | str | None]:
        return internals.pv_base_add_cost_mkt_discount_t_g_0(pv_base_add_cost_mkt_opening_stock_percent_of_face=data.PV_BASE_ADD_COST_MKT_OPENING_STOCK_PERCENT_OF_FACE, pv_base_add_cost_mkt_shock_schedule_period=self.pv_base_add_cost_mkt_shock_schedule_period, pv_base_add_cost_mkt_grace=self.pv_base_add_cost_mkt_grace)

    @cached_property
    def pv_base_add_cost_mkt_discount_post_grace_cumulative(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_discount_post_grace_cumulative(pv_base_add_cost_mkt_discount_t_g_0=self.pv_base_add_cost_mkt_discount_t_g_0, pv_base_add_cost_mkt_output_cumulative=self.pv_base_add_cost_mkt_output_cumulative)

    @cached_property
    def pv_base_add_cost_mkt_discount_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.pv_base_add_cost_mkt_discount_t_m_condition(pv_base_add_cost_mkt_opening_stock_percent_of_face=data.PV_BASE_ADD_COST_MKT_OPENING_STOCK_PERCENT_OF_FACE, pv_base_add_cost_mkt_shock_schedule_period=self.pv_base_add_cost_mkt_shock_schedule_period, pv_base_add_cost_mkt_maturity=self.pv_base_add_cost_mkt_maturity, pv_base_add_cost_mkt_discount_t_g_0=self.pv_base_add_cost_mkt_discount_t_g_0)

    @cached_property
    def pv_base_add_cost_mkt_discount_post_maturity_cumulative(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_discount_post_maturity_cumulative(pv_base_add_cost_mkt_discount_t_m_condition=self.pv_base_add_cost_mkt_discount_t_m_condition, pv_base_add_cost_mkt_output_cumulative=self.pv_base_add_cost_mkt_output_cumulative)

    @cached_property
    def pv_base_add_cost_mkt_output_new_forex_borrowing_gross_usd(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_output_new_forex_borrowing_gross_usd(ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external)

    @cached_property
    def pv_base_add_cost_mkt_output_cumulative(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_output_cumulative(pv_base_add_cost_mkt_output_new_forex_borrowing_gross_usd=self.pv_base_add_cost_mkt_output_new_forex_borrowing_gross_usd)

    @cached_property
    def pv_base_add_cost_mkt_output_stock_of_new_forex_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_output_stock_of_new_forex_debt_in_usd(pv_base_add_cost_mkt_output_new_forex_borrowing_gross_usd=self.pv_base_add_cost_mkt_output_new_forex_borrowing_gross_usd, pv_base_add_cost_mkt_output_amortization=self.pv_base_add_cost_mkt_output_amortization)

    @cached_property
    def pv_base_add_cost_mkt_output_interest(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_output_interest(pv_base_add_cost_mkt_discount_interest_rate=self.pv_base_add_cost_mkt_discount_interest_rate, pv_base_add_cost_mkt_output_stock_of_new_forex_debt_in_usd=self.pv_base_add_cost_mkt_output_stock_of_new_forex_debt_in_usd)

    @cached_property
    def pv_base_add_cost_mkt_output_amortization(self) -> data.Series[float | str | None]:
        return internals.pv_base_add_cost_mkt_output_amortization(pv_base_add_cost_mkt_grace=self.pv_base_add_cost_mkt_grace, pv_base_add_cost_mkt_maturity=self.pv_base_add_cost_mkt_maturity, pv_base_add_cost_mkt_discount_post_grace_cumulative=self.pv_base_add_cost_mkt_discount_post_grace_cumulative, pv_base_add_cost_mkt_discount_post_maturity_cumulative=self.pv_base_add_cost_mkt_discount_post_maturity_cumulative)

    @cached_property
    def _scan_pv_lc_nr1_terms_fx_pa_growth(self) -> internals.ScanPvLcNr1TermsFxPaGrowthResult:
        return internals.scan_pv_lc_nr1_terms_fx_pa_growth(macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar_nc)

    @cached_property
    def pv_lc_nr1_terms_fx_pa_growth(self) -> data.Series[float | str | None]:
        return self._scan_pv_lc_nr1_terms_fx_pa_growth.pv_lc_nr1_terms_fx_pa_growth

    @cached_property
    def pv_lc_nr1_terms_fx_pa_growth_avg(self) -> float | str:
        return self._scan_pv_lc_nr1_terms_fx_pa_growth.pv_lc_nr1_terms_fx_pa_growth_avg

    @cached_property
    def pv_lc_nr1_terms_fx_pa(self) -> data.Series[float | str | None]:
        return self._scan_pv_lc_nr1_terms_fx_pa_growth.pv_lc_nr1_terms_fx_pa

    @cached_property
    def pv_lc_nr1_terms_projection_year(self) -> data.Series[int | str | None]:
        return internals.pv_lc_nr1_terms_projection_year(macro_debt_data=self.macro_debt_data)

    @cached_property
    def pv_lc_nr1_terms_fx_eop(self) -> data.Series[float | str | None]:
        return internals.pv_lc_nr1_terms_fx_eop(macro_debt_exchange_rate_national_currency_per_u_s_dollar=self.macro_debt_exchange_rate_national_currency_per_u_s_dollar, pv_lc_nr1_terms_fx_pa_growth_avg=self.pv_lc_nr1_terms_fx_pa_growth_avg)

    @cached_property
    def pv_lc_terms_interest_rate_local_currency(self) -> data.Series[float | str | None]:
        return internals.pv_lc_terms_interest_rate_local_currency(input5_internal_interest_rate_on_domestic_debt=self.input5_internal_interest_rate_on_domestic_debt)

    @cached_property
    def pv_lc_summary_stock_of_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_lc_summary_stock_of_debt_in_usd(pv_lc_output_stock_of_debt_in_usd=self.pv_lc_output_stock_of_debt_in_usd)

    @cached_property
    def pv_lc_summary_pv_of_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_lc_summary_pv_of_debt_in_usd(pv_lc_output_pv_of_debt_in_usd=self.pv_lc_output_pv_of_debt_in_usd)

    @cached_property
    def pv_lc_terms_grace(self) -> data.Series[float | str | None]:
        return internals.pv_lc_terms_grace(input5_grace_period=self.input5_grace_period)

    @cached_property
    def pv_lc_terms_maturity(self) -> data.Series[float | str | None]:
        return internals.pv_lc_terms_maturity(input5_maturity=self.input5_maturity)

    @cached_property
    def pv_lc_terms_discount(self) -> data.Series[float | str | None]:
        return internals.pv_lc_terms_discount(discount_rate=self.discount_rate)

    @cached_property
    def pv_lc_output_issuance_year(self) -> data.Series[int | str | None]:
        return internals.pv_lc_output_issuance_year(pv_lc_nr1_terms_projection_year=self.pv_lc_nr1_terms_projection_year, pv_lc_terms_projection_year=self.pv_lc_terms_projection_year)

    @cached_property
    def pv_lc_output_period_index(self) -> data.Series[int | str | None]:
        return internals.pv_lc_output_period_index()

    @cached_property
    def pv_lc_output_projection_year(self) -> data.Series[int | str | None]:
        return internals.pv_lc_output_projection_year(pv_lc_nr1_terms_projection_year=self.pv_lc_nr1_terms_projection_year, pv_lc_terms_projection_year=self.pv_lc_terms_projection_year)

    @cached_property
    def pv_lc_output_stock_of_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_lc_output_stock_of_debt_in_usd(pv_lc_nr1_terms_fx_eop=self.pv_lc_nr1_terms_fx_eop, pv_lc_output_stock_of_debt_in_lc=self.pv_lc_output_stock_of_debt_in_lc, pv_lc_terms_fx_eop=self.pv_lc_terms_fx_eop)

    @cached_property
    def pv_lc_output_pv_of_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_lc_output_pv_of_debt_in_usd(pv_lc_output_issuance_year=self.pv_lc_output_issuance_year, pv_lc_output_projection_year=self.pv_lc_output_projection_year, pv_lc_output_stock_of_debt_in_usd=self.pv_lc_output_stock_of_debt_in_usd, pv_lc_output_total_debt_service_in_usd=self.pv_lc_output_total_debt_service_in_usd, pv_lc_output_discount=self.pv_lc_output_discount)

    @cached_property
    def pv_lc_output_grace(self) -> data.Series[float | str | None]:
        return internals.pv_lc_output_grace(pv_lc_terms_grace=self.pv_lc_terms_grace)

    @cached_property
    def pv_lc_output_total_debt_service_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_lc_output_total_debt_service_in_usd(pv_lc_output_interest_in_usd=self.pv_lc_output_interest_in_usd, pv_lc_output_amortization_in_usd=self.pv_lc_output_amortization_in_usd)

    @cached_property
    def pv_lc_output_maturity(self) -> data.Series[int | str | None]:
        return internals.pv_lc_output_maturity(pv_lc_terms_maturity=self.pv_lc_terms_maturity)

    @cached_property
    def pv_lc_output_discount(self) -> data.Series[float | str | None]:
        return internals.pv_lc_output_discount(pv_lc_terms_discount=self.pv_lc_terms_discount)

    @cached_property
    def pv_lc_output_t_g_0(self) -> data.Series[int | str | None]:
        return internals.pv_lc_output_t_g_0(pv_lc_output_period_index=self.pv_lc_output_period_index, pv_lc_output_grace=self.pv_lc_output_grace)

    @cached_property
    def pv_lc_output_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.pv_lc_output_t_m_condition(pv_lc_output_period_index=self.pv_lc_output_period_index, pv_lc_output_maturity=self.pv_lc_output_maturity)

    @cached_property
    def pv_lc_terms_projection_year(self) -> data.Series[int | str | None]:
        return internals.pv_lc_terms_projection_year(macro_debt_data=self.macro_debt_data)

    @cached_property
    def pv_lc_terms_fx_pa(self) -> data.Series[float | str | None]:
        return internals.pv_lc_terms_fx_pa(pv_lc_nr1_terms_fx_pa=self.pv_lc_nr1_terms_fx_pa)

    @cached_property
    def pv_lc_terms_fx_eop(self) -> data.Series[float | str | None]:
        return internals.pv_lc_terms_fx_eop(pv_lc_nr1_terms_fx_eop=self.pv_lc_nr1_terms_fx_eop)

    @cached_property
    def pv_stress_calendar_period(self) -> data.Series[int | str | None]:
        return internals.pv_stress_calendar_period(pv_base_constant_discount_schedule_period=data.PV_BASE_CONSTANT_DISCOUNT_SCHEDULE_PERIOD, pv_base_discount_schedule_period=self.pv_base_discount_schedule_period)

    @cached_property
    def pv_stress_discount_debt_stock(self) -> data.Series[float | str | None]:
        return internals.pv_stress_discount_debt_stock(pv_stress_discount_amortization=self.pv_stress_discount_amortization, pv_stress_historical_average_disbursement=data.PV_STRESS_HISTORICAL_AVERAGE_DISBURSEMENT)

    @cached_property
    def pv_stress_discount_amortization(self) -> data.Series[float | str | None]:
        return internals.pv_stress_discount_amortization(pv_stress_calendar_period=self.pv_stress_calendar_period, pv_stress_historical_average_disbursement=data.PV_STRESS_HISTORICAL_AVERAGE_DISBURSEMENT, pv_stress_average_maturity_of_new_debt=self.pv_stress_average_maturity_of_new_debt, pv_stress_average_grace_period_new_debt=self.pv_stress_average_grace_period_new_debt)

    @cached_property
    def pv_stress_discount_interest(self) -> data.Series[float | str | None]:
        return internals.pv_stress_discount_interest(pv_stress_average_interest_rate_new_debt=self.pv_stress_average_interest_rate_new_debt, pv_stress_discount_debt_stock=self.pv_stress_discount_debt_stock)

    @cached_property
    def pv_stress_discount_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.pv_stress_discount_total_debt_service(pv_stress_discount_amortization=self.pv_stress_discount_amortization, pv_stress_discount_interest=self.pv_stress_discount_interest)

    @cached_property
    def pv_stress_discount_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.pv_stress_discount_pv_of_debt(pv_stress_discount_debt_stock=self.pv_stress_discount_debt_stock, pv_stress_discount_total_debt_service=self.pv_stress_discount_total_debt_service, pv_stress_average_interest_rate_new_debt=self.pv_stress_average_interest_rate_new_debt, pv_stress_usd_discount_rate=self.pv_stress_usd_discount_rate)

    @cached_property
    def pv_stress_bounds_pv_of_new_forex_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_stress_bounds_pv_of_new_forex_debt_in_usd(pv_stress_discount_pv_of_debt=self.pv_stress_discount_pv_of_debt, pv_stress_bounds_new_forex_borrowing_gross_usd=self.pv_stress_bounds_new_forex_borrowing_gross_usd, pv_stress_bounds_total_debt_service_in_usd=self.pv_stress_bounds_total_debt_service_in_usd, pv_stress_bounds_amortization=self.pv_stress_bounds_amortization, pv_stress_average_interest_rate_new_debt=self.pv_stress_average_interest_rate_new_debt, pv_stress_usd_discount_rate=self.pv_stress_usd_discount_rate)

    @cached_property
    def pv_stress_bounds_total_debt_service_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_stress_bounds_total_debt_service_in_usd(pv_stress_opening_stock_percent_of_face=data.PV_STRESS_OPENING_STOCK_PERCENT_OF_FACE, pv_stress_bounds_interest=self.pv_stress_bounds_interest, pv_stress_bounds_amortization=self.pv_stress_bounds_amortization)

    @cached_property
    def pv_stress_bounds_t_g_0(self) -> data.Series[int | str | None]:
        return internals.pv_stress_bounds_t_g_0(pv_stress_calendar_period=self.pv_stress_calendar_period, pv_stress_average_grace_period_new_debt=self.pv_stress_average_grace_period_new_debt)

    @cached_property
    def pv_stress_bounds_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.pv_stress_bounds_t_m_condition(pv_stress_calendar_period=self.pv_stress_calendar_period, pv_stress_average_maturity_of_new_debt=self.pv_stress_average_maturity_of_new_debt)

    @cached_property
    def pv_resfin_pub_assumptions_share_of_marginal_debt(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_assumptions_share_of_marginal_debt(in7_resfin_domestic_st=self.in7_resfin_domestic_st, in7_resfin_shares_effective=self.in7_resfin_shares_effective)

    @cached_property
    def pv_resfin_pub_discount_period(self) -> data.Series[int | str | None]:
        return internals.pv_resfin_pub_discount_period(pv_resfin_pub_opening_stock_period=data.PV_RESFIN_PUB_OPENING_STOCK_PERIOD)

    @cached_property
    def pv_resfin_pub_assumptions_avg_nominal_interest_rate_on_new_borrowing_in_usd(self) -> float | str:
        return internals.pv_resfin_pub_assumptions_avg_nominal_interest_rate_on_new_borrowing_in_usd(in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def pv_resfin_pub_assumptions_usd_discount_rate(self) -> float | str:
        return internals.pv_resfin_pub_assumptions_usd_discount_rate(in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def pv_resfin_pub_discount_debt_stock(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_discount_debt_stock(pv_resfin_pub_opening_stock_disbursement=data.PV_RESFIN_PUB_OPENING_STOCK_DISBURSEMENT, pv_resfin_pub_discount_amortization=self.pv_resfin_pub_discount_amortization)

    @cached_property
    def pv_resfin_pub_assumptions_avg_maturity_incl_grace_period(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_assumptions_avg_maturity_incl_grace_period(in7_resfin_dom_mlt_effective=self.in7_resfin_dom_mlt_effective, in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def pv_resfin_pub_discount_amortization(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_discount_amortization(pv_resfin_pub_discount_period=self.pv_resfin_pub_discount_period, pv_resfin_pub_opening_stock_period=data.PV_RESFIN_PUB_OPENING_STOCK_PERIOD, pv_resfin_pub_opening_stock_disbursement=data.PV_RESFIN_PUB_OPENING_STOCK_DISBURSEMENT, pv_resfin_pub_assumptions_avg_maturity_incl_grace_period=self.pv_resfin_pub_assumptions_avg_maturity_incl_grace_period, pv_resfin_pub_assumptions_avg_grace_period=self.pv_resfin_pub_assumptions_avg_grace_period)

    @cached_property
    def pv_resfin_pub_assumptions_avg_grace_period(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_assumptions_avg_grace_period(in7_resfin_dom_mlt_effective=self.in7_resfin_dom_mlt_effective, in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def pv_resfin_pub_discount_interest(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_discount_interest(pv_resfin_pub_assumptions_avg_nominal_interest_rate_on_new_borrowing_in_usd=self.pv_resfin_pub_assumptions_avg_nominal_interest_rate_on_new_borrowing_in_usd, pv_resfin_pub_discount_debt_stock=self.pv_resfin_pub_discount_debt_stock)

    @cached_property
    def pv_resfin_pub_discount_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_discount_total_debt_service(pv_resfin_pub_discount_amortization=self.pv_resfin_pub_discount_amortization, pv_resfin_pub_discount_interest=self.pv_resfin_pub_discount_interest)

    @cached_property
    def pv_resfin_pub_discount_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_discount_pv_of_debt(pv_resfin_pub_assumptions_avg_nominal_interest_rate_on_new_borrowing_in_usd=self.pv_resfin_pub_assumptions_avg_nominal_interest_rate_on_new_borrowing_in_usd, pv_resfin_pub_assumptions_usd_discount_rate=self.pv_resfin_pub_assumptions_usd_discount_rate, pv_resfin_pub_discount_debt_stock=self.pv_resfin_pub_discount_debt_stock, pv_resfin_pub_discount_total_debt_service=self.pv_resfin_pub_discount_total_debt_service)

    @cached_property
    def pv_resfin_pub_assumptions_domestic_mlt_debt(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_assumptions_domestic_mlt_debt(pv_resfin_pub_assumptions_inflation_gdp_deflator=self.pv_resfin_pub_assumptions_inflation_gdp_deflator, pv_resfin_pub_avg_real_interest_rate_new_borrowing=self.pv_resfin_pub_avg_real_interest_rate_new_borrowing)

    @cached_property
    def pv_resfin_pub_assumptions_avg_real_interest_rate_on_new_borrowing(self) -> float | str:
        return internals.pv_resfin_pub_assumptions_avg_real_interest_rate_on_new_borrowing(in7_resfin_dom_mlt_effective=self.in7_resfin_dom_mlt_effective)

    @cached_property
    def pv_resfin_pub_avg_real_interest_rate_new_borrowing(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_avg_real_interest_rate_new_borrowing(pv_resfin_pub_assumptions_avg_real_interest_rate_on_new_borrowing=self.pv_resfin_pub_assumptions_avg_real_interest_rate_on_new_borrowing)

    @cached_property
    def pv_resfin_pub_assumptions_avg_interest_rate(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_assumptions_avg_interest_rate(pv_resfin_pub_assumptions_inflation_gdp_deflator=self.pv_resfin_pub_assumptions_inflation_gdp_deflator, pv_resfin_pub_avg_real_interest_rate=self.pv_resfin_pub_avg_real_interest_rate)

    @cached_property
    def pv_resfin_pub_assumptions_avg_real_interest_rate(self) -> float | str:
        return internals.pv_resfin_pub_assumptions_avg_real_interest_rate(in7_resfin_dom_st_interest_effective=self.in7_resfin_dom_st_interest_effective)

    @cached_property
    def pv_resfin_pub_avg_real_interest_rate(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_avg_real_interest_rate(pv_resfin_pub_assumptions_avg_real_interest_rate=self.pv_resfin_pub_assumptions_avg_real_interest_rate)

    @cached_property
    def pv_resfin_pub_assumptions_inflation_gdp_deflator(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_assumptions_inflation_gdp_deflator(macro_debt_change_in_gdp_deflator_factor=self.macro_debt_change_in_gdp_deflator_factor)

    @cached_property
    def pv_resfin_pub_assumptions_average_interest_rate_on_domestic_debt(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_assumptions_average_interest_rate_on_domestic_debt(pv_resfin_pub_assumptions_share_of_marginal_debt=self.pv_resfin_pub_assumptions_share_of_marginal_debt, pv_resfin_pub_assumptions_domestic_mlt_debt=self.pv_resfin_pub_assumptions_domestic_mlt_debt, pv_resfin_pub_assumptions_avg_interest_rate=self.pv_resfin_pub_assumptions_avg_interest_rate)

    @cached_property
    def pv_resfin_pub_assumptions_exchange_rate_pa(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_assumptions_exchange_rate_pa(input3_input_3_macro_national_currency_per_u_s_dollar_p_a=self.input3_input_3_macro_national_currency_per_u_s_dollar_p_a)

    @cached_property
    def pv_resfin_pub_output_new_borrowing_under_the_external_dsa_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_output_new_borrowing_under_the_external_dsa_in_usd(dsa_ext_residual_gross_borrowing=self.dsa_ext_residual_gross_borrowing)

    @cached_property
    def pv_resfin_pub_output_pv_of_new_forex_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_output_pv_of_new_forex_debt_in_usd(pv_resfin_pub_assumptions_avg_nominal_interest_rate_on_new_borrowing_in_usd=self.pv_resfin_pub_assumptions_avg_nominal_interest_rate_on_new_borrowing_in_usd, pv_resfin_pub_assumptions_usd_discount_rate=self.pv_resfin_pub_assumptions_usd_discount_rate, pv_resfin_pub_discount_pv_of_debt=self.pv_resfin_pub_discount_pv_of_debt, pv_resfin_pub_output_new_forex_borrowing_gross_usd=self.pv_resfin_pub_output_new_forex_borrowing_gross_usd, pv_resfin_pub_output_total_debt_service_in_usd=self.pv_resfin_pub_output_total_debt_service_in_usd, pv_resfin_pub_output_amortization=self.pv_resfin_pub_output_amortization)

    @cached_property
    def pv_resfin_pub_output_total_debt_service_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_pub_output_total_debt_service_in_usd(pv_resfin_pub_output_interest=self.pv_resfin_pub_output_interest, pv_resfin_pub_output_amortization=self.pv_resfin_pub_output_amortization)

    @cached_property
    def pv_resfin_pub_output_t_g_0(self) -> data.Series[int | str | None]:
        return internals.pv_resfin_pub_output_t_g_0(pv_resfin_pub_opening_stock_period=data.PV_RESFIN_PUB_OPENING_STOCK_PERIOD, pv_resfin_pub_discount_period=self.pv_resfin_pub_discount_period, pv_resfin_pub_assumptions_avg_grace_period=self.pv_resfin_pub_assumptions_avg_grace_period)

    @cached_property
    def pv_resfin_pub_output_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.pv_resfin_pub_output_t_m_condition(pv_resfin_pub_opening_stock_period=data.PV_RESFIN_PUB_OPENING_STOCK_PERIOD, pv_resfin_pub_discount_period=self.pv_resfin_pub_discount_period, pv_resfin_pub_assumptions_avg_maturity_incl_grace_period=self.pv_resfin_pub_assumptions_avg_maturity_incl_grace_period)

    @cached_property
    def pv_resfin_add_assumptions_additional_borrowing_costs_domestic(self) -> float | str:
        return internals.pv_resfin_add_assumptions_additional_borrowing_costs_domestic(input6_standard_params_2=self.input6_standard_params_2)

    @cached_property
    def pv_resfin_add_assumptions_share_of_marginal_debt(self) -> float | str:
        return internals.pv_resfin_add_assumptions_share_of_marginal_debt(in7_resfin_domestic_st=self.in7_resfin_domestic_st)

    @cached_property
    def pv_resfin_add_assumptions_usd_discount_rate(self) -> float | str:
        return internals.pv_resfin_add_assumptions_usd_discount_rate(discount_rate=self.discount_rate)

    @cached_property
    def pv_resfin_add_assumptions_avg_maturity_incl_grace_period(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_assumptions_avg_maturity_incl_grace_period(in7_resfin_dom_mlt_effective=self.in7_resfin_dom_mlt_effective, in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def pv_resfin_add_assumptions_avg_grace_period(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_assumptions_avg_grace_period(in7_resfin_dom_mlt_effective=self.in7_resfin_dom_mlt_effective, in7_resfin_ext_mlt_effective=self.in7_resfin_ext_mlt_effective)

    @cached_property
    def pv_resfin_add_projection_years_period_index(self) -> data.Series[int | str | None]:
        return internals.pv_resfin_add_projection_years_period_index(pv_resfin_add_opening_stock_period_seed=data.PV_RESFIN_ADD_OPENING_STOCK_PERIOD_SEED)

    @cached_property
    def pv_resfin_add_int_cost_mkt_stock_of_new_forex_debt_beyond_projection_window(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_stock_of_new_forex_debt_beyond_projection_window(pv_resfin_add_output_stock_of_new_forex_debt_in_usd=self.pv_resfin_add_output_stock_of_new_forex_debt_in_usd, pv_resfin_add_int_cost_mkt_amortization_beyond_projection_window=self.pv_resfin_add_int_cost_mkt_amortization_beyond_projection_window)

    @cached_property
    def pv_resfin_add_output_pv_of_new_forex_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_output_pv_of_new_forex_debt_in_usd(pv_resfin_add_assumptions_usd_discount_rate=self.pv_resfin_add_assumptions_usd_discount_rate, pv_resfin_add_output_interest=self.pv_resfin_add_output_interest, pv_resfin_add_int_cost_mkt_interest_beyond_projection_window=self.pv_resfin_add_int_cost_mkt_interest_beyond_projection_window, pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_two_year_average=self.pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_two_year_average)

    @cached_property
    def pv_resfin_add_int_cost_mkt_interest_beyond_projection_window(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_interest_beyond_projection_window(pv_resfin_add_output_stock_of_new_forex_debt_in_usd=self.pv_resfin_add_output_stock_of_new_forex_debt_in_usd, pv_resfin_add_int_cost_mkt_stock_of_new_forex_debt_beyond_projection_window=self.pv_resfin_add_int_cost_mkt_stock_of_new_forex_debt_beyond_projection_window, pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_two_year_average=self.pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_two_year_average)

    @cached_property
    def pv_resfin_add_assumptions_deviation_in_pb_ppt(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_assumptions_deviation_in_pb_ppt(dsa_pub_primary_deficit=self.dsa_pub_primary_deficit, baseline_pub_primary_deficit=self.baseline_pub_primary_deficit)

    @cached_property
    def pv_resfin_add_int_cost_mkt_amortization_beyond_projection_window(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_amortization_beyond_projection_window(pv_resfin_add_assumptions_avg_maturity_incl_grace_period=self.pv_resfin_add_assumptions_avg_maturity_incl_grace_period, pv_resfin_add_assumptions_avg_grace_period=self.pv_resfin_add_assumptions_avg_grace_period, pv_resfin_add_int_cost_mkt_cumulative_selected_t_g_0_beyond_projection_window=self.pv_resfin_add_int_cost_mkt_cumulative_selected_t_g_0_beyond_projection_window, pv_resfin_add_int_cost_mkt_cumulative_selected_t_m_condition_beyond_projection_window=self.pv_resfin_add_int_cost_mkt_cumulative_selected_t_m_condition_beyond_projection_window)

    @cached_property
    def pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_shock_years(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_shock_years(pv_resfin_add_assumptions_deviation_in_pb_ppt=self.pv_resfin_add_assumptions_deviation_in_pb_ppt, pv_resfin_add_assumptions_additional_borrowing_costs_external=data.PV_RESFIN_ADD_ASSUMPTIONS_ADDITIONAL_BORROWING_COSTS_EXTERNAL)

    @cached_property
    def pv_resfin_add_output_t_g_0(self) -> data.Series[int | str | None]:
        return internals.pv_resfin_add_output_t_g_0(pv_resfin_add_assumptions_avg_grace_period=self.pv_resfin_add_assumptions_avg_grace_period, pv_resfin_add_opening_stock_period_seed=data.PV_RESFIN_ADD_OPENING_STOCK_PERIOD_SEED, pv_resfin_add_projection_years_period_index=self.pv_resfin_add_projection_years_period_index)

    @cached_property
    def pv_resfin_add_int_cost_mkt_t_g_0_beyond_projection_window(self) -> data.Series[int | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_t_g_0_beyond_projection_window(pv_resfin_add_assumptions_avg_grace_period=self.pv_resfin_add_assumptions_avg_grace_period, pv_resfin_add_projection_years_period_index=self.pv_resfin_add_projection_years_period_index)

    @cached_property
    def pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_two_year_average(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_two_year_average(pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_shock_years=self.pv_resfin_add_int_cost_mkt_avg_nominal_interest_rate_new_borrowing_usd_shock_years)

    @cached_property
    def pv_resfin_add_int_cost_mkt_cumulative_selected_t_g_0_beyond_projection_window(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_cumulative_selected_t_g_0_beyond_projection_window(pv_resfin_add_output_cumulative=self.pv_resfin_add_output_cumulative, pv_resfin_add_int_cost_mkt_cumulative_beyond_projection_window=self.pv_resfin_add_int_cost_mkt_cumulative_beyond_projection_window, pv_resfin_add_int_cost_mkt_t_g_0_beyond_projection_window=self.pv_resfin_add_int_cost_mkt_t_g_0_beyond_projection_window)

    @cached_property
    def pv_resfin_add_int_cost_mkt_additional_domestic_interest_rate_shock_years(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_additional_domestic_interest_rate_shock_years(pv_resfin_add_assumptions_deviation_in_pb_ppt=self.pv_resfin_add_assumptions_deviation_in_pb_ppt, pv_resfin_add_assumptions_additional_borrowing_costs_domestic=self.pv_resfin_add_assumptions_additional_borrowing_costs_domestic)

    @cached_property
    def pv_resfin_add_output_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.pv_resfin_add_output_t_m_condition(pv_resfin_add_assumptions_avg_maturity_incl_grace_period=self.pv_resfin_add_assumptions_avg_maturity_incl_grace_period, pv_resfin_add_opening_stock_period_seed=data.PV_RESFIN_ADD_OPENING_STOCK_PERIOD_SEED, pv_resfin_add_projection_years_period_index=self.pv_resfin_add_projection_years_period_index)

    @cached_property
    def pv_resfin_add_int_cost_mkt_t_m_condition_beyond_projection_window(self) -> data.Series[int | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_t_m_condition_beyond_projection_window(pv_resfin_add_assumptions_avg_maturity_incl_grace_period=self.pv_resfin_add_assumptions_avg_maturity_incl_grace_period, pv_resfin_add_projection_years_period_index=self.pv_resfin_add_projection_years_period_index)

    @cached_property
    def pv_resfin_add_int_cost_mkt_additional_domestic_interest_rate_two_year_average(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_additional_domestic_interest_rate_two_year_average(pv_resfin_add_int_cost_mkt_additional_domestic_interest_rate_shock_years=self.pv_resfin_add_int_cost_mkt_additional_domestic_interest_rate_shock_years)

    @cached_property
    def pv_resfin_add_int_cost_mkt_cumulative_selected_t_m_condition_beyond_projection_window(self) -> data.Series[float | str | None]:
        return internals.pv_resfin_add_int_cost_mkt_cumulative_selected_t_m_condition_beyond_projection_window(pv_resfin_add_output_cumulative=self.pv_resfin_add_output_cumulative, pv_resfin_add_int_cost_mkt_cumulative_beyond_projection_window=self.pv_resfin_add_int_cost_mkt_cumulative_beyond_projection_window, pv_resfin_add_int_cost_mkt_t_m_condition_beyond_projection_window=self.pv_resfin_add_int_cost_mkt_t_m_condition_beyond_projection_window)

    @cached_property
    def pv_baseline_com_pv_debt(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_pv_debt(pv_baseline_com_output_pv_of_debt=self.pv_baseline_com_output_pv_of_debt)

    @cached_property
    def pv_baseline_com_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_total_debt_service(pv_baseline_com_output_total_debt_service_in_usd=self.pv_baseline_com_output_total_debt_service_in_usd)

    @cached_property
    def pv_baseline_com_discount_period(self) -> data.Series[int | str | None]:
        return internals.pv_baseline_com_discount_period(pv_baseline_com_discount_schedule_period=data.PV_BASELINE_COM_DISCOUNT_SCHEDULE_PERIOD)

    @cached_property
    def pv_baseline_com_grace(self) -> data.Series[int | str | None]:
        return internals.pv_baseline_com_grace(input4_grace_period=self.input4_grace_period)

    @cached_property
    def pv_baseline_com_maturity(self) -> data.Series[int | str | None]:
        return internals.pv_baseline_com_maturity(input4_loan_maturity=self.input4_loan_maturity)

    @cached_property
    def pv_baseline_com_discount_debt_stock(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_discount_debt_stock(pv_baseline_com_opening_percent_of_face=data.PV_BASELINE_COM_OPENING_PERCENT_OF_FACE, pv_baseline_com_discount_amortization=self.pv_baseline_com_discount_amortization)

    @cached_property
    def pv_baseline_com_discount_interest_rate(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_discount_interest_rate(input4_interest_rate=self.input4_interest_rate)

    @cached_property
    def pv_baseline_com_discount_amortization(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_discount_amortization(pv_baseline_com_discount_period=self.pv_baseline_com_discount_period, pv_baseline_com_grace=self.pv_baseline_com_grace, pv_baseline_com_maturity=self.pv_baseline_com_maturity, pv_baseline_com_opening_percent_of_face=data.PV_BASELINE_COM_OPENING_PERCENT_OF_FACE)

    @cached_property
    def pv_baseline_com_discount_discount_rate(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_discount_discount_rate(input4_discount_rate=self.input4_discount_rate)

    @cached_property
    def pv_baseline_com_discount_interest(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_discount_interest(pv_baseline_com_discount_debt_stock=self.pv_baseline_com_discount_debt_stock, pv_baseline_com_discount_interest_rate=self.pv_baseline_com_discount_interest_rate)

    @cached_property
    def pv_baseline_com_discount_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_discount_total_debt_service(pv_baseline_com_discount_amortization=self.pv_baseline_com_discount_amortization, pv_baseline_com_discount_interest=self.pv_baseline_com_discount_interest)

    @cached_property
    def pv_baseline_com_discount_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_discount_pv_of_debt(pv_baseline_com_discount_debt_stock=self.pv_baseline_com_discount_debt_stock, pv_baseline_com_discount_interest_rate=self.pv_baseline_com_discount_interest_rate, pv_baseline_com_discount_discount_rate=self.pv_baseline_com_discount_discount_rate, pv_baseline_com_discount_total_debt_service=self.pv_baseline_com_discount_total_debt_service)

    @cached_property
    def pv_baseline_com_discount_t_g_0(self) -> data.Series[int | str | None]:
        return internals.pv_baseline_com_discount_t_g_0(pv_baseline_com_discount_period=self.pv_baseline_com_discount_period, pv_baseline_com_grace=self.pv_baseline_com_grace)

    @cached_property
    def pv_baseline_com_discount_cumulative_selected_by_t_g_0(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_discount_cumulative_selected_by_t_g_0(pv_baseline_com_discount_t_g_0=self.pv_baseline_com_discount_t_g_0, pv_baseline_com_output_cumulative=self.pv_baseline_com_output_cumulative)

    @cached_property
    def pv_baseline_com_discount_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.pv_baseline_com_discount_t_m_condition(pv_baseline_com_discount_period=self.pv_baseline_com_discount_period, pv_baseline_com_maturity=self.pv_baseline_com_maturity)

    @cached_property
    def pv_baseline_com_discount_cumulative_selected_by_t_m_condition(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_discount_cumulative_selected_by_t_m_condition(pv_baseline_com_discount_t_m_condition=self.pv_baseline_com_discount_t_m_condition, pv_baseline_com_output_cumulative=self.pv_baseline_com_output_cumulative)

    @cached_property
    def pv_baseline_com_output_new_forex_borrowing_gross_usd(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_output_new_forex_borrowing_gross_usd(ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external)

    @cached_property
    def pv_baseline_com_output_cumulative(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_output_cumulative(pv_baseline_com_output_new_forex_borrowing_gross_usd=self.pv_baseline_com_output_new_forex_borrowing_gross_usd)

    @cached_property
    def pv_baseline_com_output_stock_of_new_forex_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_output_stock_of_new_forex_debt_in_usd(pv_baseline_com_output_new_forex_borrowing_gross_usd=self.pv_baseline_com_output_new_forex_borrowing_gross_usd, pv_baseline_com_output_amortization=self.pv_baseline_com_output_amortization)

    @cached_property
    def pv_baseline_com_output_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_output_pv_of_debt(pv_baseline_com_discount_interest_rate=self.pv_baseline_com_discount_interest_rate, pv_baseline_com_discount_discount_rate=self.pv_baseline_com_discount_discount_rate, pv_baseline_com_discount_pv_of_debt=self.pv_baseline_com_discount_pv_of_debt, pv_baseline_com_output_new_forex_borrowing_gross_usd=self.pv_baseline_com_output_new_forex_borrowing_gross_usd, pv_baseline_com_output_total_debt_service_in_usd=self.pv_baseline_com_output_total_debt_service_in_usd, pv_baseline_com_output_amortization=self.pv_baseline_com_output_amortization)

    @cached_property
    def pv_baseline_com_output_total_debt_service_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_output_total_debt_service_in_usd(pv_baseline_com_output_interest=self.pv_baseline_com_output_interest, pv_baseline_com_output_amortization=self.pv_baseline_com_output_amortization)

    @cached_property
    def pv_baseline_com_output_interest(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_output_interest(pv_baseline_com_discount_interest_rate=self.pv_baseline_com_discount_interest_rate, pv_baseline_com_output_stock_of_new_forex_debt_in_usd=self.pv_baseline_com_output_stock_of_new_forex_debt_in_usd)

    @cached_property
    def pv_baseline_com_output_amortization(self) -> data.Series[float | str | None]:
        return internals.pv_baseline_com_output_amortization(pv_baseline_com_grace=self.pv_baseline_com_grace, pv_baseline_com_maturity=self.pv_baseline_com_maturity, pv_baseline_com_discount_cumulative_selected_by_t_g_0=self.pv_baseline_com_discount_cumulative_selected_by_t_g_0, pv_baseline_com_discount_cumulative_selected_by_t_m_condition=self.pv_baseline_com_discount_cumulative_selected_by_t_m_condition)

    @cached_property
    def pv_stress_com_assumptions_increase_in_external_borrowing_costs(self) -> float | str:
        return internals.pv_stress_com_assumptions_increase_in_external_borrowing_costs(c4_market_path_us_gdp_deflator=self.c4_market_path_us_gdp_deflator)

    @cached_property
    def pv_stress_com_pv_debt(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_pv_debt(pv_stress_com_output_pv_of_debt=self.pv_stress_com_output_pv_of_debt)

    @cached_property
    def pv_stress_com_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_total_debt_service(pv_stress_com_output_total_debt_service_in_usd=self.pv_stress_com_output_total_debt_service_in_usd)

    @cached_property
    def pv_stress_com_discount_period(self) -> data.Series[int | str | None]:
        return internals.pv_stress_com_discount_period(pv_stress_com_opening_stock_percent_of_face=data.PV_STRESS_COM_OPENING_STOCK_PERCENT_OF_FACE)

    @cached_property
    def pv_stress_com_grace(self) -> data.Series[int | str | None]:
        return internals.pv_stress_com_grace(c4_mkt_fin_stressed_lending_terms=self.c4_mkt_fin_stressed_lending_terms)

    @cached_property
    def pv_stress_com_maturity(self) -> data.Series[int | str | None]:
        return internals.pv_stress_com_maturity(c4_mkt_fin_stressed_lending_terms=self.c4_mkt_fin_stressed_lending_terms)

    @cached_property
    def pv_stress_com_discount_debt_stock(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_discount_debt_stock(pv_stress_com_opening_percent_of_face=data.PV_STRESS_COM_OPENING_PERCENT_OF_FACE, pv_stress_com_discount_amortization=self.pv_stress_com_discount_amortization)

    @cached_property
    def pv_stress_com_discount_interest_rate(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_discount_interest_rate(input4_interest_rate=self.input4_interest_rate, pv_stress_com_assumptions_increase_in_external_borrowing_costs=self.pv_stress_com_assumptions_increase_in_external_borrowing_costs)

    @cached_property
    def pv_stress_com_discount_amortization(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_discount_amortization(pv_stress_com_opening_percent_of_face=data.PV_STRESS_COM_OPENING_PERCENT_OF_FACE, pv_stress_com_discount_period=self.pv_stress_com_discount_period, pv_stress_com_grace=self.pv_stress_com_grace, pv_stress_com_maturity=self.pv_stress_com_maturity)

    @cached_property
    def pv_stress_com_discount_discount_rate(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_discount_discount_rate(input4_discount_rate=self.input4_discount_rate)

    @cached_property
    def pv_stress_com_discount_interest(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_discount_interest(pv_stress_com_discount_debt_stock=self.pv_stress_com_discount_debt_stock, pv_stress_com_discount_interest_rate=self.pv_stress_com_discount_interest_rate)

    @cached_property
    def pv_stress_com_discount_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_discount_total_debt_service(pv_stress_com_discount_amortization=self.pv_stress_com_discount_amortization, pv_stress_com_discount_interest=self.pv_stress_com_discount_interest)

    @cached_property
    def pv_stress_com_discount_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_discount_pv_of_debt(pv_stress_com_discount_debt_stock=self.pv_stress_com_discount_debt_stock, pv_stress_com_discount_interest_rate=self.pv_stress_com_discount_interest_rate, pv_stress_com_discount_discount_rate=self.pv_stress_com_discount_discount_rate, pv_stress_com_discount_total_debt_service=self.pv_stress_com_discount_total_debt_service)

    @cached_property
    def pv_stress_com_discount_t_g_0(self) -> data.Series[int | str | None]:
        return internals.pv_stress_com_discount_t_g_0(pv_stress_com_discount_period=self.pv_stress_com_discount_period, pv_stress_com_grace=self.pv_stress_com_grace)

    @cached_property
    def pv_stress_com_discount_cumulative_selected_by_t_g_0(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_discount_cumulative_selected_by_t_g_0(pv_stress_com_discount_t_g_0=self.pv_stress_com_discount_t_g_0, pv_stress_com_output_cumulative=self.pv_stress_com_output_cumulative)

    @cached_property
    def pv_stress_com_discount_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.pv_stress_com_discount_t_m_condition(pv_stress_com_discount_period=self.pv_stress_com_discount_period, pv_stress_com_maturity=self.pv_stress_com_maturity)

    @cached_property
    def pv_stress_com_discount_cumulative_selected_by_t_m_condition(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_discount_cumulative_selected_by_t_m_condition(pv_stress_com_discount_t_m_condition=self.pv_stress_com_discount_t_m_condition, pv_stress_com_output_cumulative=self.pv_stress_com_output_cumulative)

    @cached_property
    def pv_stress_com_output_new_forex_borrowing_gross_usd(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_output_new_forex_borrowing_gross_usd(ext_debt_new_disbursements_external=self.ext_debt_new_disbursements_external)

    @cached_property
    def pv_stress_com_output_cumulative(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_output_cumulative(pv_stress_com_output_new_forex_borrowing_gross_usd=self.pv_stress_com_output_new_forex_borrowing_gross_usd)

    @cached_property
    def pv_stress_com_output_stock_of_new_forex_debt_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_output_stock_of_new_forex_debt_in_usd(pv_stress_com_output_new_forex_borrowing_gross_usd=self.pv_stress_com_output_new_forex_borrowing_gross_usd, pv_stress_com_output_amortization=self.pv_stress_com_output_amortization)

    @cached_property
    def pv_stress_com_output_pv_of_debt(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_output_pv_of_debt(pv_stress_com_discount_interest_rate=self.pv_stress_com_discount_interest_rate, pv_stress_com_discount_discount_rate=self.pv_stress_com_discount_discount_rate, pv_stress_com_discount_pv_of_debt=self.pv_stress_com_discount_pv_of_debt, pv_stress_com_output_new_forex_borrowing_gross_usd=self.pv_stress_com_output_new_forex_borrowing_gross_usd, pv_stress_com_output_total_debt_service_in_usd=self.pv_stress_com_output_total_debt_service_in_usd, pv_stress_com_output_amortization=self.pv_stress_com_output_amortization)

    @cached_property
    def pv_stress_com_output_total_debt_service_in_usd(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_output_total_debt_service_in_usd(pv_stress_com_output_interest=self.pv_stress_com_output_interest, pv_stress_com_output_amortization=self.pv_stress_com_output_amortization)

    @cached_property
    def pv_stress_com_output_interest(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_output_interest(pv_stress_com_discount_interest_rate=self.pv_stress_com_discount_interest_rate, pv_stress_com_output_stock_of_new_forex_debt_in_usd=self.pv_stress_com_output_stock_of_new_forex_debt_in_usd)

    @cached_property
    def pv_stress_com_output_amortization(self) -> data.Series[float | str | None]:
        return internals.pv_stress_com_output_amortization(pv_stress_com_grace=self.pv_stress_com_grace, pv_stress_com_maturity=self.pv_stress_com_maturity, pv_stress_com_discount_cumulative_selected_by_t_g_0=self.pv_stress_com_discount_cumulative_selected_by_t_g_0, pv_stress_com_discount_cumulative_selected_by_t_m_condition=self.pv_stress_com_discount_cumulative_selected_by_t_m_condition)

    @cached_property
    def pv_stress_average_interest_rate_new_debt(self) -> data.Series[float | str | None]:
        return internals.pv_stress_average_interest_rate_new_debt(in7_resfin_ext_mlt_override=self.in7_resfin_ext_mlt_override, c4_mkt_fin_average_residual_interest=self.c4_mkt_fin_average_residual_interest)

    @cached_property
    def pv_stress_usd_discount_rate(self) -> data.Series[float | str | None]:
        return internals.pv_stress_usd_discount_rate(in7_resfin_ext_mlt_override=self.in7_resfin_ext_mlt_override)

    @cached_property
    def pv_stress_average_maturity_of_new_debt(self) -> data.Series[float | str | None]:
        return internals.pv_stress_average_maturity_of_new_debt(in7_resfin_ext_mlt_override=self.in7_resfin_ext_mlt_override, c4_mkt_fin_average_residual_terms=self.c4_mkt_fin_average_residual_terms)

    @cached_property
    def pv_stress_average_grace_period_new_debt(self) -> data.Series[float | str | None]:
        return internals.pv_stress_average_grace_period_new_debt(in7_resfin_ext_mlt_override=self.in7_resfin_ext_mlt_override, c4_mkt_fin_average_residual_terms=self.c4_mkt_fin_average_residual_terms)

    @cached_property
    def pv_stress_pv_of_new_forex_debt(self) -> data.Series[float | str | None]:
        return internals.pv_stress_pv_of_new_forex_debt(pv_stress_discount_pv_of_debt=self.pv_stress_discount_pv_of_debt, pv_stress_average_interest_rate_new_debt=self.pv_stress_average_interest_rate_new_debt, pv_stress_usd_discount_rate=self.pv_stress_usd_discount_rate, pv_stress_new_forex_borrowing_gross_usd=self.pv_stress_new_forex_borrowing_gross_usd, pv_stress_total_debt_service=self.pv_stress_total_debt_service, pv_stress_amortization=self.pv_stress_amortization)

    @cached_property
    def pv_stress_total_debt_service(self) -> data.Series[float | str | None]:
        return internals.pv_stress_total_debt_service(pv_stress_interest=self.pv_stress_interest, pv_stress_amortization=self.pv_stress_amortization, pv_stress_interest_scenario=data.PV_STRESS_INTEREST_SCENARIO)

    @cached_property
    def pv_stress_t_g_0(self) -> data.Series[int | str | None]:
        return internals.pv_stress_t_g_0(pv_stress_calendar_period=self.pv_stress_calendar_period, pv_stress_average_grace_period_new_debt=self.pv_stress_average_grace_period_new_debt)

    @cached_property
    def pv_stress_t_m_condition(self) -> data.Series[int | str | None]:
        return internals.pv_stress_t_m_condition(pv_stress_calendar_period=self.pv_stress_calendar_period, pv_stress_average_maturity_of_new_debt=self.pv_stress_average_maturity_of_new_debt)


@dataclass(frozen=True, kw_only=True)
class Realism1ExternalDebtFlowComponentsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_external_debt_flow_components`."""

    start_working_language: str


@dataclass(frozen=True, kw_only=True)
class Realism1ExternalDebtCreatingFlowsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_external_debt_creating_flows`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class Realism1ExternalForecastErrorComponentLabelsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_external_forecast_error_component_labels`."""

    start_working_language: str


@dataclass(frozen=True, kw_only=True)
class Realism1ExternalForecastErrorComponentsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_external_forecast_error_components`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class Realism1ExternalForecastErrorDistributionLabelsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_external_forecast_error_distribution_labels`."""

    start_working_language: str


@dataclass(frozen=True, kw_only=True)
class Realism1ExternalForecastErrorDistributionInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_external_forecast_error_distribution`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class Realism1ExternalVintageYearsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_external_vintage_years`."""

    first_projection_year: int | str


@dataclass(frozen=True, kw_only=True)
class Realism1ExternalVintageDebtPathsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_external_vintage_debt_paths`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class Realism1PublicDebtFlowComponentsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_public_debt_flow_components`."""

    start_working_language: str


@dataclass(frozen=True, kw_only=True)
class Realism1PublicDebtCreatingFlowsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_public_debt_creating_flows`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    first_projection_year: int | str
    external_domestic_debt_definition: str
    blend_ida_new_floating_currency: str
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class Realism1PublicForecastErrorComponentLabelsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_public_forecast_error_component_labels`."""

    start_working_language: str


@dataclass(frozen=True, kw_only=True)
class Realism1PublicForecastErrorComponentsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_public_forecast_error_components`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    external_domestic_debt_definition: str
    blend_ida_new_floating_currency: str
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class Realism1PublicForecastErrorLowerQuartileInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_public_forecast_error_lower_quartile`."""



@dataclass(frozen=True, kw_only=True)
class Realism1PublicForecastErrorDistributionLabelsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_public_forecast_error_distribution_labels`."""

    start_working_language: str


@dataclass(frozen=True, kw_only=True)
class Realism1PublicForecastErrorDistributionInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_public_forecast_error_distribution`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    external_domestic_debt_definition: str
    blend_ida_new_floating_currency: str
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class Realism1PublicVintageYearsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_public_vintage_years`."""

    current_year: int | str


@dataclass(frozen=True, kw_only=True)
class Realism1PublicVintageDebtPathsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism1_public_vintage_debt_paths`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    external_domestic_debt_definition: str
    blend_ida_new_floating_currency: str
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class Realism2FiscalAdjustmentMultiplierLabelsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism2_fiscal_adjustment_multiplier_labels`."""



@dataclass(frozen=True, kw_only=True)
class Realism2UnderlyingGrowthMultiplierLabelsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism2_underlying_growth_multiplier_labels`."""



@dataclass(frozen=True, kw_only=True)
class Realism2FiscalAdjustmentYearsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism2_fiscal_adjustment_years`."""

    first_projection_year: int | str


@dataclass(frozen=True, kw_only=True)
class Realism2UnderlyingGrowthYearsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism2_underlying_growth_years`."""

    first_projection_year: int | str


@dataclass(frozen=True, kw_only=True)
class Realism2BaselineGrowthInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism2_baseline_growth`."""

    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct


@dataclass(frozen=True, kw_only=True)
class Realism2GrowthTMinus1Inputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism2_growth_t_minus_1`."""

    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct


@dataclass(frozen=True, kw_only=True)
class Realism2FiscalAdjustmentGrowthImpactInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism2_fiscal_adjustment_growth_impact`."""

    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe


@dataclass(frozen=True, kw_only=True)
class Realism2UnderlyingGrowthInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism2_underlying_growth`."""

    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe


@dataclass(frozen=True, kw_only=True)
class Realism3InvestmentYearsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism3_investment_years`."""

    first_projection_year: int | str


@dataclass(frozen=True, kw_only=True)
class Realism3InvestmentPathLabelsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism3_investment_path_labels`."""

    start_working_language: str


@dataclass(frozen=True, kw_only=True)
class Realism3PublicPrivateInvestmentPathsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism3_public_private_investment_paths`."""

    country: str
    first_projection_year: int | str
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct


@dataclass(frozen=True, kw_only=True)
class Realism3GrowthAccountingVintagesInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism3_growth_accounting_vintages`."""

    start_working_language: str


@dataclass(frozen=True, kw_only=True)
class Realism3GrowthAccountingContributionsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism3_growth_accounting_contributions`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    external_domestic_debt_definition: str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    current_year: int | str
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class Realism4Projected3yrAdjustmentLabelInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism4_projected_3yr_adjustment_label`."""

    start_working_language: str


@dataclass(frozen=True, kw_only=True)
class Realism4Projected3yrAdjustmentInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism4_projected_3yr_adjustment`."""

    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe


@dataclass(frozen=True, kw_only=True)
class Realism4Projected3yrAdjustmentBinInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism4_projected_3yr_adjustment_bin`."""

    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe


@dataclass(frozen=True, kw_only=True)
class Realism4Projected3yrAdjustmentCategoryInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism4_projected_3yr_adjustment_category`."""

    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe


@dataclass(frozen=True, kw_only=True)
class Realism4Projected3yrAdjustmentSampleShareInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism4_projected_3yr_adjustment_sample_share`."""

    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe


@dataclass(frozen=True, kw_only=True)
class Realism4FiscalAdjustmentTopBinLabelInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism4_fiscal_adjustment_top_bin_label`."""

    start_working_language: str


@dataclass(frozen=True, kw_only=True)
class Realism4FiscalAdjustmentSampleShareInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism4_fiscal_adjustment_sample_share`."""



@dataclass(frozen=True, kw_only=True)
class Realism4FiscalAdjustmentCumulativeShareInputs(_SnapshotInputs):
    """Bound input leaves for `compute_realism4_fiscal_adjustment_cumulative_share`."""



@dataclass(frozen=True, kw_only=True)
class ProbabilityPvDebtToGdpInputs(_SnapshotInputs):
    """Bound input leaves for `compute_probability_pv_debt_to_gdp`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ProbabilityPvDebtToExportsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_probability_pv_debt_to_exports`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ProbabilityDebtServiceToExportsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_probability_debt_service_to_exports`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ProbabilityDebtServiceToRevenueInputs(_SnapshotInputs):
    """Bound input leaves for `compute_probability_debt_service_to_revenue`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ProbabilityPvDebtToGdpDistressInputs(_SnapshotInputs):
    """Bound input leaves for `compute_probability_pv_debt_to_gdp_distress`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ProbabilityPvDebtToExportsDistressInputs(_SnapshotInputs):
    """Bound input leaves for `compute_probability_pv_debt_to_exports_distress`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ProbabilityDebtServiceToExportsDistressInputs(_SnapshotInputs):
    """Bound input leaves for `compute_probability_debt_service_to_exports_distress`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ProbabilityDebtServiceToRevenueDistressInputs(_SnapshotInputs):
    """Bound input leaves for `compute_probability_debt_service_to_revenue_distress`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ExternalDsaRiskRatingSignalInputs(_SnapshotInputs):
    """Bound input leaves for `compute_external_dsa_risk_rating_signal`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ExternalDsaRiskRatingNumericInputs(_SnapshotInputs):
    """Bound input leaves for `compute_external_dsa_risk_rating_numeric`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ExternalBaselineBreachInputs(_SnapshotInputs):
    """Bound input leaves for `compute_external_baseline_breach`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ExternalShockBreachInputs(_SnapshotInputs):
    """Bound input leaves for `compute_external_shock_breach`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ExternalPvDebtToGdpMxShockInputs(_SnapshotInputs):
    """Bound input leaves for `compute_external_pv_debt_to_gdp_mx_shock`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ExternalPvDebtToExportsMxShockInputs(_SnapshotInputs):
    """Bound input leaves for `compute_external_pv_debt_to_exports_mx_shock`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ExternalDebtServiceToExportsMxShockInputs(_SnapshotInputs):
    """Bound input leaves for `compute_external_debt_service_to_exports_mx_shock`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ExternalDebtServiceToRevenueMxShockInputs(_SnapshotInputs):
    """Bound input leaves for `compute_external_debt_service_to_revenue_mx_shock`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class FiscalRiskRatingSignalInputs(_SnapshotInputs):
    """Bound input leaves for `compute_fiscal_risk_rating_signal`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class FiscalRiskRatingNumericInputs(_SnapshotInputs):
    """Bound input leaves for `compute_fiscal_risk_rating_numeric`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class FiscalBaselineBreachInputs(_SnapshotInputs):
    """Bound input leaves for `compute_fiscal_baseline_breach`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class FiscalShockBreachInputs(_SnapshotInputs):
    """Bound input leaves for `compute_fiscal_shock_breach`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class FiscalPvDebtToGdpMxShockInputs(_SnapshotInputs):
    """Bound input leaves for `compute_fiscal_pv_debt_to_gdp_mx_shock`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class TailoredStressNaturalDisasterApplicableInputs(_SnapshotInputs):
    """Bound input leaves for `compute_tailored_stress_natural_disaster_applicable`."""

    country: str


@dataclass(frozen=True, kw_only=True)
class TailoredStressCommodityPriceApplicableInputs(_SnapshotInputs):
    """Bound input leaves for `compute_tailored_stress_commodity_price_applicable`."""

    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input6_tailored_tests_enabled: str
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber


@dataclass(frozen=True, kw_only=True)
class TailoredStressMarketFinancingApplicableInputs(_SnapshotInputs):
    """Bound input leaves for `compute_tailored_stress_market_financing_applicable`."""

    country: str
    input6_tailored_tests_enabled: str


@dataclass(frozen=True, kw_only=True)
class FiscalSpaceModerateRiskSignalInputs(_SnapshotInputs):
    """Bound input leaves for `compute_fiscal_space_moderate_risk_signal`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    fiscal_space_moderate_assessment_flag: int | str
    fiscal_space_stock_band: data.FiscalSpaceStockBand
    fiscal_space_flow_band: data.FiscalSpaceFlowBand
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class OverallRiskRatingSignalInputs(_SnapshotInputs):
    """Bound input leaves for `compute_overall_risk_rating_signal`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class OverallRiskRatingNumericInputs(_SnapshotInputs):
    """Bound input leaves for `compute_overall_risk_rating_numeric`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartOutputChartDataPvOfDebtToGdpRatioPvDebtToGdpInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_output_chart_data_pv_of_debt_to_gdp_ratio_pv_debt_to_gdp`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartOutputChartDataPvOfDebtToRevenueRatioPvDebtToRevenueInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_output_chart_data_pv_of_debt_to_revenue_ratio_pv_debt_to_revenue`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartOutputChartDataDebtServiceToRevenueRatioDebtServiceToRevenueInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_output_chart_data_debt_service_to_revenue_ratio_debt_service_to_revenue`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartOutputChartDataDebtServiceToGdpRatioDebtServiceGdpRatioInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_output_chart_data_debt_service_to_gdp_ratio_debt_service_gdp_ratio`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartPvDebtGdpRatioCustomAlternativeScenarioInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_pv_debt_gdp_ratio_custom_alternative_scenario`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    customized_external_debt_profile_period: int | str
    customized_external_debt_profile_disbursement: float | str
    customized_external_new_forex_borrowing_cumulative_overflow: data.CustomizedExternalNewForexBorrowingCumulativeOverflow
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartOutputPvDebtGdpRatioInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_output_pv_debt_gdp_ratio`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartPvDebtToExportsCustomAlternativeScenarioInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_pv_debt_to_exports_custom_alternative_scenario`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    customized_external_debt_profile_period: int | str
    customized_external_debt_profile_disbursement: float | str
    customized_external_new_forex_borrowing_cumulative_overflow: data.CustomizedExternalNewForexBorrowingCumulativeOverflow
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartOutputPvDebtToExportsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_output_pv_debt_to_exports`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartDebtServiceToExportsCustomAlternativeScenarioInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_debt_service_to_exports_custom_alternative_scenario`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    customized_external_debt_profile_period: int | str
    customized_external_new_forex_borrowing_cumulative_overflow: data.CustomizedExternalNewForexBorrowingCumulativeOverflow
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartOutputDebtServiceToExportsInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_output_debt_service_to_exports`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartDebtServiceToRevenueCustomAlternativeScenarioInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_debt_service_to_revenue_custom_alternative_scenario`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    customized_external_debt_profile_period: int | str
    customized_external_new_forex_borrowing_cumulative_overflow: data.CustomizedExternalNewForexBorrowingCumulativeOverflow
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartOutputDebtServiceToRevenueInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_output_debt_service_to_revenue`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_external_debt_private_mlt_external_debt_amortization_due: data.Input3Input3ExternalDebtPrivateMltExternalDebtAmortizationDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartOutputPvDebtToGdpInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_output_pv_debt_to_gdp`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartPvDebtToRevenueMxShockStandardTailoredInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_pv_debt_to_revenue_mx_shock_standard_tailored`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_public_sector_liquid_assets_stock_e_g_cash: data.In3MacroPublicSectorLiquidAssetsStockEGCash
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_external_mlt_disbursement_profile: float | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


@dataclass(frozen=True, kw_only=True)
class ChartOutputDebtServiceToRevenueFiscalInputs(_SnapshotInputs):
    """Bound input leaves for `compute_chart_output_debt_service_to_revenue_fiscal`."""

    input4_interest_rate: data.Input4InterestRate
    input4_grace_period: data.Input4GracePeriod
    input4_loan_maturity: data.Input4LoanMaturity
    input4_disbursements: data.Input4Disbursements
    input4_instrument_names: data.Input4InstrumentNames
    input4_blend_variant: str
    input4_blend_scale_key: data.Input4BlendScaleKey
    input5_grace_period: data.Input5GracePeriod
    input5_interest_rate_on_domestic_debt: data.Input5InterestRateOnDomesticDebt
    input5_interest_rate_on_domestic_debt_fx_long: data.Input5InterestRateOnDomesticDebtFxLong
    input5_maturity: data.Input5Maturity
    input5_maturity_central_bank: int | str
    input5_public_gfns_other_adjustment: data.Input5PublicGfnsOtherAdjustment
    input5_domestic_financing_source: int | str
    input5_gfn_share: data.Input5GfnShare
    start_working_language: str
    country: str
    first_projection_year: int | str
    discount_rate: float | str
    external_domestic_debt_definition: str
    contingent_liability_other_elements_pct_gdp: float | str
    contingent_liability_soe_debt_pct_gdp: float | str
    contingent_liability_financial_market_pct_gdp: float | str
    ppp_capital_stock_shock_pct: float | str
    customized_public_delta: data.CustomizedPublicDelta
    blend_ida_new_floating_currency: str
    input_1_rer_overvaluation: float | str
    customized_public_include_scenario: str
    input6_commodity_group_relevant: data.Input6CommodityGroupRelevant
    input8_sdr_interest_historical: data.Input8SdrInterestHistorical
    input8_sdr_interest: data.Input8SdrInterest
    input8_sdr_interest_rate: float | str
    input6_tailored_tests_enabled: str
    input6_standard_size_threshold_mode: str
    input6_standard_interactions: str
    input6_standard_user_defined_threshold: data.Input6StandardUserDefinedThreshold
    input3_input_3_macro_gross_domestic_product_us_dollars: data.Input3Input3MacroGrossDomesticProductUsDollars
    input3_input_3_macro_real_gross_domestic_product: data.Input3Input3MacroRealGrossDomesticProduct
    input3_input_3_macro_u_s_deflator: data.Input3Input3MacroUSDeflator
    input3_input_3_macro_national_currency_per_u_s_dollar_e_o_p: data.Input3Input3MacroNationalCurrencyPerUSDollarEOP
    input3_input_3_macro_national_currency_per_u_s_dollar_p_a: data.Input3Input3MacroNationalCurrencyPerUSDollarPA
    input3_input_3_macro_government_revenue_and_grants: data.Input3Input3MacroGovernmentRevenueAndGrants
    input3_input_3_macro_government_grants: data.Input3Input3MacroGovernmentGrants
    in3_macro_government_primary_expenditures_this_used_be: data.In3MacroGovernmentPrimaryExpendituresThisUsedBe
    in3_macro_liquid_financial_assets_used_meet_gfns_flow_e_g: data.In3MacroLiquidFinancialAssetsUsedMeetGfnsFlowEG
    input3_input_3_macro_privatization_proceeds: data.Input3Input3MacroPrivatizationProceeds
    in3_macro_recognition_of_contingent_liab_e_g_bank: data.In3MacroRecognitionOfContingentLiabEGBank
    input3_input_3_macro_debt_relief_non_multilateral_hipc: data.Input3Input3MacroDebtReliefNonMultilateralHipc
    input3_input_3_macro_other_debt_creating_or_reducing_flow_please_specify: data.Input3Input3MacroOtherDebtCreatingOrReducingFlowPleaseSpecify
    input3_input_3_macro_current_account: data.Input3Input3MacroCurrentAccount
    input3_input_3_macro_exports_of_goods_and_services: data.Input3Input3MacroExportsOfGoodsAndServices
    input3_input_3_macro_exports_commodity_fuel: data.Input3Input3MacroExportsCommodityFuel
    input3_input_3_macro_exports_commodity_non_fuel: data.Input3Input3MacroExportsCommodityNonFuel
    input3_input_3_macro_imports_of_goods_and_services_enter_as_a_positive_number: data.Input3Input3MacroImportsOfGoodsAndServicesEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityFuelEnterAsAPositiveNumber
    input3_input_3_macro_imports_commodity_non_fuel_enter_as_a_positive_number: data.Input3Input3MacroImportsCommodityNonFuelEnterAsAPositiveNumber
    input3_input_3_macro_current_transfers_net: data.Input3Input3MacroCurrentTransfersNet
    input3_input_3_macro_foreign_direct_investment: data.Input3Input3MacroForeignDirectInvestment
    input3_input_3_external_debt_ppg_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPpgMltExternalDebtOutstanding
    input3_input_3_external_debt_ppg_st_external_debt_outstanding: data.Input3Input3ExternalDebtPpgStExternalDebtOutstanding
    input3_input_3_external_debt_ppg_external_debt_interest_due: data.Input3Input3ExternalDebtPpgExternalDebtInterestDue
    input3_input_3_external_debt_ppg_external_arrears: data.Input3Input3ExternalDebtPpgExternalArrears
    input3_input_3_external_debt_private_sector_mlt_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorMltExternalDebtOutstanding
    input3_input_3_external_debt_private_sector_st_external_debt_outstanding: data.Input3Input3ExternalDebtPrivateSectorStExternalDebtOutstanding
    input3_input_3_external_debt_private_external_debt_interest_due: data.Input3Input3ExternalDebtPrivateExternalDebtInterestDue
    input3_input_3_old_debt_service_total_principal_payment: data.Input3Input3OldDebtServiceTotalPrincipalPayment
    customized_public_template_anchor: float | str
    customized_public_natural_disaster_year: int | str
    customized_public_new_forex_borrowing_cumulative_overflow: data.CustomizedPublicNewForexBorrowingCumulativeOverflow
    customized_public_new_domestic_mlt_cumulative_overflow: data.CustomizedPublicNewDomesticMltCumulativeOverflow
    customized_public_residual_overflow: data.CustomizedPublicResidualOverflow
    customized_public_new_forex_debt_stock_initial: float | str
    customized_public_domestic_mlt_interest_initial: float | str
    customized_public_domestic_st_interest_initial: float | str
    input8_sdr_stock: data.Input8SdrStock
    input3_old_debt_service: data.Input3OldDebtService
    input3_new_disbursements: data.Input3NewDisbursements
    input3_domestic_outstanding_of_existing_debt: data.Input3DomesticOutstandingOfExistingDebt
    input3_domestic_o_w_st: data.Input3DomesticOWSt
    input3_domestic_interest_payment_from_existing_debt: data.Input3DomesticInterestPaymentFromExistingDebt
    input3_domestic_principal_payment_from_existing_debt: data.Input3DomesticPrincipalPaymentFromExistingDebt
    input3_domestic_new_gross_disbursement: data.Input3DomesticNewGrossDisbursement
    pv_base_input_output_cumulative: data.PvBaseInputOutputCumulative


__all__ = [
    "Model",
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
]
