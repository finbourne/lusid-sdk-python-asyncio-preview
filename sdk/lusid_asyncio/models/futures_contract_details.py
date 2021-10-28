# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3659
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


class FuturesContractDetails(object):
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
        'dom_ccy': 'str',
        'contract_code': 'str',
        'contract_month': 'str',
        'contract_size': 'float',
        'convention': 'str',
        'country': 'str',
        'description': 'str',
        'exchange_code': 'str',
        'exchange_name': 'str',
        'ticker_step': 'float',
        'unit_value': 'float'
    }

    attribute_map = {
        'dom_ccy': 'domCcy',
        'contract_code': 'contractCode',
        'contract_month': 'contractMonth',
        'contract_size': 'contractSize',
        'convention': 'convention',
        'country': 'country',
        'description': 'description',
        'exchange_code': 'exchangeCode',
        'exchange_name': 'exchangeName',
        'ticker_step': 'tickerStep',
        'unit_value': 'unitValue'
    }

    required_map = {
        'dom_ccy': 'required',
        'contract_code': 'required',
        'contract_month': 'required',
        'contract_size': 'required',
        'convention': 'required',
        'country': 'required',
        'description': 'required',
        'exchange_code': 'required',
        'exchange_name': 'required',
        'ticker_step': 'required',
        'unit_value': 'required'
    }

    def __init__(self, dom_ccy=None, contract_code=None, contract_month=None, contract_size=None, convention=None, country=None, description=None, exchange_code=None, exchange_name=None, ticker_step=None, unit_value=None, local_vars_configuration=None):  # noqa: E501
        """FuturesContractDetails - a model defined in OpenAPI"
        
        :param dom_ccy:  currency in which the contract is paid. (required)
        :type dom_ccy: str
        :param contract_code:  The two letter contract code abbreviation. e.g. CL => Crude Oil. (required)
        :type contract_code: str
        :param contract_month:  which month does the contract trade for.  Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z]. (required)
        :type contract_month: str
        :param contract_size:  Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such. (required)
        :type contract_size: float
        :param convention:  If appropriate, the day count convention method used in pricing (rates futures) (required)
        :type convention: str
        :param country:  Country (code) for the exchange. (required)
        :type country: str
        :param description:  Description of contract (required)
        :type description: str
        :param exchange_code:  Exchange code for contract  Supported string (enumeration) values are: [ASX, CBOT, CBF, CME, CMX, EOP, HKG, KFE, MFM, OSE, SGX, NYBOT, KCBT, MGE, MATIF, SFE, NYFE, NYM, LIFFE, EUREX, ICE, MSE]. (required)
        :type exchange_code: str
        :param exchange_name:  Exchange name (for when code is not automatically recognized) (required)
        :type exchange_name: str
        :param ticker_step:  Minimal step size change in ticker (required)
        :type ticker_step: float
        :param unit_value:  The value in the currency of a 1 unit change in the contract price (required)
        :type unit_value: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dom_ccy = None
        self._contract_code = None
        self._contract_month = None
        self._contract_size = None
        self._convention = None
        self._country = None
        self._description = None
        self._exchange_code = None
        self._exchange_name = None
        self._ticker_step = None
        self._unit_value = None
        self.discriminator = None

        self.dom_ccy = dom_ccy
        self.contract_code = contract_code
        self.contract_month = contract_month
        self.contract_size = contract_size
        self.convention = convention
        self.country = country
        self.description = description
        self.exchange_code = exchange_code
        self.exchange_name = exchange_name
        self.ticker_step = ticker_step
        self.unit_value = unit_value

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this FuturesContractDetails.  # noqa: E501

        currency in which the contract is paid.  # noqa: E501

        :return: The dom_ccy of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this FuturesContractDetails.

        currency in which the contract is paid.  # noqa: E501

        :param dom_ccy: The dom_ccy of this FuturesContractDetails.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def contract_code(self):
        """Gets the contract_code of this FuturesContractDetails.  # noqa: E501

        The two letter contract code abbreviation. e.g. CL => Crude Oil.  # noqa: E501

        :return: The contract_code of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._contract_code

    @contract_code.setter
    def contract_code(self, contract_code):
        """Sets the contract_code of this FuturesContractDetails.

        The two letter contract code abbreviation. e.g. CL => Crude Oil.  # noqa: E501

        :param contract_code: The contract_code of this FuturesContractDetails.  # noqa: E501
        :type contract_code: str
        """
        if self.local_vars_configuration.client_side_validation and contract_code is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_code`, must not be `None`")  # noqa: E501

        self._contract_code = contract_code

    @property
    def contract_month(self):
        """Gets the contract_month of this FuturesContractDetails.  # noqa: E501

        which month does the contract trade for.  Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z].  # noqa: E501

        :return: The contract_month of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._contract_month

    @contract_month.setter
    def contract_month(self, contract_month):
        """Sets the contract_month of this FuturesContractDetails.

        which month does the contract trade for.  Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z].  # noqa: E501

        :param contract_month: The contract_month of this FuturesContractDetails.  # noqa: E501
        :type contract_month: str
        """
        if self.local_vars_configuration.client_side_validation and contract_month is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_month`, must not be `None`")  # noqa: E501

        self._contract_month = contract_month

    @property
    def contract_size(self):
        """Gets the contract_size of this FuturesContractDetails.  # noqa: E501

        Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such.  # noqa: E501

        :return: The contract_size of this FuturesContractDetails.  # noqa: E501
        :rtype: float
        """
        return self._contract_size

    @contract_size.setter
    def contract_size(self, contract_size):
        """Sets the contract_size of this FuturesContractDetails.

        Size of a single contract. By default this should be set to 1000 if otherwise unknown and is defaulted to such.  # noqa: E501

        :param contract_size: The contract_size of this FuturesContractDetails.  # noqa: E501
        :type contract_size: float
        """
        if self.local_vars_configuration.client_side_validation and contract_size is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_size`, must not be `None`")  # noqa: E501

        self._contract_size = contract_size

    @property
    def convention(self):
        """Gets the convention of this FuturesContractDetails.  # noqa: E501

        If appropriate, the day count convention method used in pricing (rates futures)  # noqa: E501

        :return: The convention of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._convention

    @convention.setter
    def convention(self, convention):
        """Sets the convention of this FuturesContractDetails.

        If appropriate, the day count convention method used in pricing (rates futures)  # noqa: E501

        :param convention: The convention of this FuturesContractDetails.  # noqa: E501
        :type convention: str
        """
        if self.local_vars_configuration.client_side_validation and convention is None:  # noqa: E501
            raise ValueError("Invalid value for `convention`, must not be `None`")  # noqa: E501

        self._convention = convention

    @property
    def country(self):
        """Gets the country of this FuturesContractDetails.  # noqa: E501

        Country (code) for the exchange.  # noqa: E501

        :return: The country of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this FuturesContractDetails.

        Country (code) for the exchange.  # noqa: E501

        :param country: The country of this FuturesContractDetails.  # noqa: E501
        :type country: str
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def description(self):
        """Gets the description of this FuturesContractDetails.  # noqa: E501

        Description of contract  # noqa: E501

        :return: The description of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FuturesContractDetails.

        Description of contract  # noqa: E501

        :param description: The description of this FuturesContractDetails.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def exchange_code(self):
        """Gets the exchange_code of this FuturesContractDetails.  # noqa: E501

        Exchange code for contract  Supported string (enumeration) values are: [ASX, CBOT, CBF, CME, CMX, EOP, HKG, KFE, MFM, OSE, SGX, NYBOT, KCBT, MGE, MATIF, SFE, NYFE, NYM, LIFFE, EUREX, ICE, MSE].  # noqa: E501

        :return: The exchange_code of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._exchange_code

    @exchange_code.setter
    def exchange_code(self, exchange_code):
        """Sets the exchange_code of this FuturesContractDetails.

        Exchange code for contract  Supported string (enumeration) values are: [ASX, CBOT, CBF, CME, CMX, EOP, HKG, KFE, MFM, OSE, SGX, NYBOT, KCBT, MGE, MATIF, SFE, NYFE, NYM, LIFFE, EUREX, ICE, MSE].  # noqa: E501

        :param exchange_code: The exchange_code of this FuturesContractDetails.  # noqa: E501
        :type exchange_code: str
        """
        if self.local_vars_configuration.client_side_validation and exchange_code is None:  # noqa: E501
            raise ValueError("Invalid value for `exchange_code`, must not be `None`")  # noqa: E501

        self._exchange_code = exchange_code

    @property
    def exchange_name(self):
        """Gets the exchange_name of this FuturesContractDetails.  # noqa: E501

        Exchange name (for when code is not automatically recognized)  # noqa: E501

        :return: The exchange_name of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this FuturesContractDetails.

        Exchange name (for when code is not automatically recognized)  # noqa: E501

        :param exchange_name: The exchange_name of this FuturesContractDetails.  # noqa: E501
        :type exchange_name: str
        """
        if self.local_vars_configuration.client_side_validation and exchange_name is None:  # noqa: E501
            raise ValueError("Invalid value for `exchange_name`, must not be `None`")  # noqa: E501

        self._exchange_name = exchange_name

    @property
    def ticker_step(self):
        """Gets the ticker_step of this FuturesContractDetails.  # noqa: E501

        Minimal step size change in ticker  # noqa: E501

        :return: The ticker_step of this FuturesContractDetails.  # noqa: E501
        :rtype: float
        """
        return self._ticker_step

    @ticker_step.setter
    def ticker_step(self, ticker_step):
        """Sets the ticker_step of this FuturesContractDetails.

        Minimal step size change in ticker  # noqa: E501

        :param ticker_step: The ticker_step of this FuturesContractDetails.  # noqa: E501
        :type ticker_step: float
        """
        if self.local_vars_configuration.client_side_validation and ticker_step is None:  # noqa: E501
            raise ValueError("Invalid value for `ticker_step`, must not be `None`")  # noqa: E501

        self._ticker_step = ticker_step

    @property
    def unit_value(self):
        """Gets the unit_value of this FuturesContractDetails.  # noqa: E501

        The value in the currency of a 1 unit change in the contract price  # noqa: E501

        :return: The unit_value of this FuturesContractDetails.  # noqa: E501
        :rtype: float
        """
        return self._unit_value

    @unit_value.setter
    def unit_value(self, unit_value):
        """Sets the unit_value of this FuturesContractDetails.

        The value in the currency of a 1 unit change in the contract price  # noqa: E501

        :param unit_value: The unit_value of this FuturesContractDetails.  # noqa: E501
        :type unit_value: float
        """
        if self.local_vars_configuration.client_side_validation and unit_value is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_value`, must not be `None`")  # noqa: E501

        self._unit_value = unit_value

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
        if not isinstance(other, FuturesContractDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FuturesContractDetails):
            return True

        return self.to_dict() != other.to_dict()
