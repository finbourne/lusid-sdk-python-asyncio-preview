# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3836
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


class ReconciliationLeftRightAddressKeyPair(object):
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
        'left': 'str',
        'right': 'str'
    }

    attribute_map = {
        'left': 'left',
        'right': 'right'
    }

    required_map = {
        'left': 'required',
        'right': 'required'
    }

    def __init__(self, left=None, right=None, local_vars_configuration=None):  # noqa: E501
        """ReconciliationLeftRightAddressKeyPair - a model defined in OpenAPI"
        
        :param left:  Address key defined by the lhs aggregation (required)
        :type left: str
        :param right:  Address key defined by the rhs aggregation (required)
        :type right: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._left = None
        self._right = None
        self.discriminator = None

        self.left = left
        self.right = right

    @property
    def left(self):
        """Gets the left of this ReconciliationLeftRightAddressKeyPair.  # noqa: E501

        Address key defined by the lhs aggregation  # noqa: E501

        :return: The left of this ReconciliationLeftRightAddressKeyPair.  # noqa: E501
        :rtype: str
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this ReconciliationLeftRightAddressKeyPair.

        Address key defined by the lhs aggregation  # noqa: E501

        :param left: The left of this ReconciliationLeftRightAddressKeyPair.  # noqa: E501
        :type left: str
        """
        if self.local_vars_configuration.client_side_validation and left is None:  # noqa: E501
            raise ValueError("Invalid value for `left`, must not be `None`")  # noqa: E501

        self._left = left

    @property
    def right(self):
        """Gets the right of this ReconciliationLeftRightAddressKeyPair.  # noqa: E501

        Address key defined by the rhs aggregation  # noqa: E501

        :return: The right of this ReconciliationLeftRightAddressKeyPair.  # noqa: E501
        :rtype: str
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this ReconciliationLeftRightAddressKeyPair.

        Address key defined by the rhs aggregation  # noqa: E501

        :param right: The right of this ReconciliationLeftRightAddressKeyPair.  # noqa: E501
        :type right: str
        """
        if self.local_vars_configuration.client_side_validation and right is None:  # noqa: E501
            raise ValueError("Invalid value for `right`, must not be `None`")  # noqa: E501

        self._right = right

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
        if not isinstance(other, ReconciliationLeftRightAddressKeyPair):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconciliationLeftRightAddressKeyPair):
            return True

        return self.to_dict() != other.to_dict()
