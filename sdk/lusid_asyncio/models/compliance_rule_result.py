# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3639
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


class ComplianceRuleResult(object):
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
        'rule_id': 'str',
        'portfolio': 'ResourceId',
        'passed': 'bool'
    }

    attribute_map = {
        'rule_id': 'ruleId',
        'portfolio': 'portfolio',
        'passed': 'passed'
    }

    required_map = {
        'rule_id': 'required',
        'portfolio': 'required',
        'passed': 'required'
    }

    def __init__(self, rule_id=None, portfolio=None, passed=None, local_vars_configuration=None):  # noqa: E501
        """ComplianceRuleResult - a model defined in OpenAPI"
        
        :param rule_id:  The unique identifierof a compliance rule (required)
        :type rule_id: str
        :param portfolio:  (required)
        :type portfolio: lusid_asyncio.ResourceId
        :param passed:  The result of an individual compliance run, true if passed (required)
        :type passed: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._rule_id = None
        self._portfolio = None
        self._passed = None
        self.discriminator = None

        self.rule_id = rule_id
        self.portfolio = portfolio
        self.passed = passed

    @property
    def rule_id(self):
        """Gets the rule_id of this ComplianceRuleResult.  # noqa: E501

        The unique identifierof a compliance rule  # noqa: E501

        :return: The rule_id of this ComplianceRuleResult.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ComplianceRuleResult.

        The unique identifierof a compliance rule  # noqa: E501

        :param rule_id: The rule_id of this ComplianceRuleResult.  # noqa: E501
        :type rule_id: str
        """
        if self.local_vars_configuration.client_side_validation and rule_id is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_id`, must not be `None`")  # noqa: E501

        self._rule_id = rule_id

    @property
    def portfolio(self):
        """Gets the portfolio of this ComplianceRuleResult.  # noqa: E501


        :return: The portfolio of this ComplianceRuleResult.  # noqa: E501
        :rtype: lusid_asyncio.ResourceId
        """
        return self._portfolio

    @portfolio.setter
    def portfolio(self, portfolio):
        """Sets the portfolio of this ComplianceRuleResult.


        :param portfolio: The portfolio of this ComplianceRuleResult.  # noqa: E501
        :type portfolio: lusid_asyncio.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and portfolio is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio`, must not be `None`")  # noqa: E501

        self._portfolio = portfolio

    @property
    def passed(self):
        """Gets the passed of this ComplianceRuleResult.  # noqa: E501

        The result of an individual compliance run, true if passed  # noqa: E501

        :return: The passed of this ComplianceRuleResult.  # noqa: E501
        :rtype: bool
        """
        return self._passed

    @passed.setter
    def passed(self, passed):
        """Sets the passed of this ComplianceRuleResult.

        The result of an individual compliance run, true if passed  # noqa: E501

        :param passed: The passed of this ComplianceRuleResult.  # noqa: E501
        :type passed: bool
        """
        if self.local_vars_configuration.client_side_validation and passed is None:  # noqa: E501
            raise ValueError("Invalid value for `passed`, must not be `None`")  # noqa: E501

        self._passed = passed

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
        if not isinstance(other, ComplianceRuleResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceRuleResult):
            return True

        return self.to_dict() != other.to_dict()
