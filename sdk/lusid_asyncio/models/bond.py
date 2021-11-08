# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3698
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_asyncio.configuration import Configuration


class Bond(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'start_date': 'datetime',
        'maturity_date': 'datetime',
        'dom_ccy': 'str',
        'flow_conventions': 'FlowConventions',
        'principal': 'float',
        'coupon_rate': 'float',
        'identifiers': 'dict(str, str)',
        'ex_dividend_days': 'int',
        'initial_coupon_date': 'datetime',
        'first_coupon_pay_date': 'datetime',
        'calculation_type': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'dom_ccy': 'domCcy',
        'flow_conventions': 'flowConventions',
        'principal': 'principal',
        'coupon_rate': 'couponRate',
        'identifiers': 'identifiers',
        'ex_dividend_days': 'exDividendDays',
        'initial_coupon_date': 'initialCouponDate',
        'first_coupon_pay_date': 'firstCouponPayDate',
        'calculation_type': 'calculationType',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'dom_ccy': 'required',
        'flow_conventions': 'required',
        'principal': 'required',
        'coupon_rate': 'required',
        'identifiers': 'optional',
        'ex_dividend_days': 'optional',
        'initial_coupon_date': 'optional',
        'first_coupon_pay_date': 'optional',
        'calculation_type': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, dom_ccy=None, flow_conventions=None, principal=None, coupon_rate=None, identifiers=None, ex_dividend_days=None, initial_coupon_date=None, first_coupon_pay_date=None, calculation_type=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """Bond - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.              For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as              Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date (required)
        :type maturity_date: datetime
        :param dom_ccy:  The domestic currency of the instrument. (required)
        :type dom_ccy: str
        :param flow_conventions:  (required)
        :type flow_conventions: lusid_asyncio.FlowConventions
        :param principal:  The face-value or principal for the bond at outset.              This might be reduced through its lifetime in the event of amortization or similar. (required)
        :type principal: float
        :param coupon_rate:  simple coupon rate. (required)
        :type coupon_rate: float
        :param identifiers:  external market codes and identifiers for the bond, e.g. ISIN.
        :type identifiers: dict(str, str)
        :param ex_dividend_days:  The number of days before the next coupon payment for which the bond goes ex-dividend.
        :type ex_dividend_days: int
        :param initial_coupon_date:  The initial coupon date which specifies the accrual start period for a fixed coupon bond with ex dividend schedule
        :type initial_coupon_date: datetime
        :param first_coupon_pay_date:  The date that the first coupon of the bond is paid. This is required for bonds that have a long first coupon or short first coupon. The first coupon pay date is used  as an anchor to compare with the start date and determine if this is a long/short coupon period.
        :type first_coupon_pay_date: datetime
        :param calculation_type:  The calculation type applied to the bond coupon amount. This is required for bonds that have a particular type of computing the period coupon, such as simple compounding,  irregular coupons etc.  Supported string (enumeration) values are: [Standard, NoCalculationFloater, BrazilFixedCoupon].
        :type calculation_type: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._dom_ccy = None
        self._flow_conventions = None
        self._principal = None
        self._coupon_rate = None
        self._identifiers = None
        self._ex_dividend_days = None
        self._initial_coupon_date = None
        self._first_coupon_pay_date = None
        self._calculation_type = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        self.dom_ccy = dom_ccy
        self.flow_conventions = flow_conventions
        self.principal = principal
        self.coupon_rate = coupon_rate
        self.identifiers = identifiers
        self.ex_dividend_days = ex_dividend_days
        self.initial_coupon_date = initial_coupon_date
        self.first_coupon_pay_date = first_coupon_pay_date
        self.calculation_type = calculation_type
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this Bond.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this Bond.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Bond.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this Bond.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this Bond.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.              For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as              Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date  # noqa: E501

        :return: The maturity_date of this Bond.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this Bond.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.              For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as              Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date  # noqa: E501

        :param maturity_date: The maturity_date of this Bond.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this Bond.  # noqa: E501

        The domestic currency of the instrument.  # noqa: E501

        :return: The dom_ccy of this Bond.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this Bond.

        The domestic currency of the instrument.  # noqa: E501

        :param dom_ccy: The dom_ccy of this Bond.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def flow_conventions(self):
        """Gets the flow_conventions of this Bond.  # noqa: E501


        :return: The flow_conventions of this Bond.  # noqa: E501
        :rtype: lusid_asyncio.FlowConventions
        """
        return self._flow_conventions

    @flow_conventions.setter
    def flow_conventions(self, flow_conventions):
        """Sets the flow_conventions of this Bond.


        :param flow_conventions: The flow_conventions of this Bond.  # noqa: E501
        :type flow_conventions: lusid_asyncio.FlowConventions
        """
        if self.local_vars_configuration.client_side_validation and flow_conventions is None:  # noqa: E501
            raise ValueError("Invalid value for `flow_conventions`, must not be `None`")  # noqa: E501

        self._flow_conventions = flow_conventions

    @property
    def principal(self):
        """Gets the principal of this Bond.  # noqa: E501

        The face-value or principal for the bond at outset.              This might be reduced through its lifetime in the event of amortization or similar.  # noqa: E501

        :return: The principal of this Bond.  # noqa: E501
        :rtype: float
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this Bond.

        The face-value or principal for the bond at outset.              This might be reduced through its lifetime in the event of amortization or similar.  # noqa: E501

        :param principal: The principal of this Bond.  # noqa: E501
        :type principal: float
        """
        if self.local_vars_configuration.client_side_validation and principal is None:  # noqa: E501
            raise ValueError("Invalid value for `principal`, must not be `None`")  # noqa: E501

        self._principal = principal

    @property
    def coupon_rate(self):
        """Gets the coupon_rate of this Bond.  # noqa: E501

        simple coupon rate.  # noqa: E501

        :return: The coupon_rate of this Bond.  # noqa: E501
        :rtype: float
        """
        return self._coupon_rate

    @coupon_rate.setter
    def coupon_rate(self, coupon_rate):
        """Sets the coupon_rate of this Bond.

        simple coupon rate.  # noqa: E501

        :param coupon_rate: The coupon_rate of this Bond.  # noqa: E501
        :type coupon_rate: float
        """
        if self.local_vars_configuration.client_side_validation and coupon_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon_rate`, must not be `None`")  # noqa: E501

        self._coupon_rate = coupon_rate

    @property
    def identifiers(self):
        """Gets the identifiers of this Bond.  # noqa: E501

        external market codes and identifiers for the bond, e.g. ISIN.  # noqa: E501

        :return: The identifiers of this Bond.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this Bond.

        external market codes and identifiers for the bond, e.g. ISIN.  # noqa: E501

        :param identifiers: The identifiers of this Bond.  # noqa: E501
        :type identifiers: dict(str, str)
        """

        self._identifiers = identifiers

    @property
    def ex_dividend_days(self):
        """Gets the ex_dividend_days of this Bond.  # noqa: E501

        The number of days before the next coupon payment for which the bond goes ex-dividend.  # noqa: E501

        :return: The ex_dividend_days of this Bond.  # noqa: E501
        :rtype: int
        """
        return self._ex_dividend_days

    @ex_dividend_days.setter
    def ex_dividend_days(self, ex_dividend_days):
        """Sets the ex_dividend_days of this Bond.

        The number of days before the next coupon payment for which the bond goes ex-dividend.  # noqa: E501

        :param ex_dividend_days: The ex_dividend_days of this Bond.  # noqa: E501
        :type ex_dividend_days: int
        """

        self._ex_dividend_days = ex_dividend_days

    @property
    def initial_coupon_date(self):
        """Gets the initial_coupon_date of this Bond.  # noqa: E501

        The initial coupon date which specifies the accrual start period for a fixed coupon bond with ex dividend schedule  # noqa: E501

        :return: The initial_coupon_date of this Bond.  # noqa: E501
        :rtype: datetime
        """
        return self._initial_coupon_date

    @initial_coupon_date.setter
    def initial_coupon_date(self, initial_coupon_date):
        """Sets the initial_coupon_date of this Bond.

        The initial coupon date which specifies the accrual start period for a fixed coupon bond with ex dividend schedule  # noqa: E501

        :param initial_coupon_date: The initial_coupon_date of this Bond.  # noqa: E501
        :type initial_coupon_date: datetime
        """

        self._initial_coupon_date = initial_coupon_date

    @property
    def first_coupon_pay_date(self):
        """Gets the first_coupon_pay_date of this Bond.  # noqa: E501

        The date that the first coupon of the bond is paid. This is required for bonds that have a long first coupon or short first coupon. The first coupon pay date is used  as an anchor to compare with the start date and determine if this is a long/short coupon period.  # noqa: E501

        :return: The first_coupon_pay_date of this Bond.  # noqa: E501
        :rtype: datetime
        """
        return self._first_coupon_pay_date

    @first_coupon_pay_date.setter
    def first_coupon_pay_date(self, first_coupon_pay_date):
        """Sets the first_coupon_pay_date of this Bond.

        The date that the first coupon of the bond is paid. This is required for bonds that have a long first coupon or short first coupon. The first coupon pay date is used  as an anchor to compare with the start date and determine if this is a long/short coupon period.  # noqa: E501

        :param first_coupon_pay_date: The first_coupon_pay_date of this Bond.  # noqa: E501
        :type first_coupon_pay_date: datetime
        """

        self._first_coupon_pay_date = first_coupon_pay_date

    @property
    def calculation_type(self):
        """Gets the calculation_type of this Bond.  # noqa: E501

        The calculation type applied to the bond coupon amount. This is required for bonds that have a particular type of computing the period coupon, such as simple compounding,  irregular coupons etc.  Supported string (enumeration) values are: [Standard, NoCalculationFloater, BrazilFixedCoupon].  # noqa: E501

        :return: The calculation_type of this Bond.  # noqa: E501
        :rtype: str
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this Bond.

        The calculation type applied to the bond coupon amount. This is required for bonds that have a particular type of computing the period coupon, such as simple compounding,  irregular coupons etc.  Supported string (enumeration) values are: [Standard, NoCalculationFloater, BrazilFixedCoupon].  # noqa: E501

        :param calculation_type: The calculation_type of this Bond.  # noqa: E501
        :type calculation_type: str
        """

        self._calculation_type = calculation_type

    @property
    def instrument_type(self):
        """Gets the instrument_type of this Bond.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption  # noqa: E501

        :return: The instrument_type of this Bond.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this Bond.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, CrossCurrencySwap, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption  # noqa: E501

        :param instrument_type: The instrument_type of this Bond.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "CrossCurrencySwap", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Bond):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Bond):
            return True

        return self.to_dict() != other.to_dict()
