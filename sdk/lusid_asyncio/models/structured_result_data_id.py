# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3765
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


class StructuredResultDataId(object):
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
        'source': 'str',
        'code': 'str',
        'effective_at': 'str',
        'result_type': 'str'
    }

    attribute_map = {
        'source': 'source',
        'code': 'code',
        'effective_at': 'effectiveAt',
        'result_type': 'resultType'
    }

    required_map = {
        'source': 'required',
        'code': 'optional',
        'effective_at': 'optional',
        'result_type': 'optional'
    }

    def __init__(self, source=None, code=None, effective_at=None, result_type=None, local_vars_configuration=None):  # noqa: E501
        """StructuredResultDataId - a model defined in OpenAPI"
        
        :param source:  The platform or vendor that provided the structured result data, e.g. 'client'. This is primarily of interest when data could have been sourced from multiple sources (required)
        :type source: str
        :param code:  The identifier for the entity that this id describes. It could be an index, instrument or other form of structured data
        :type code: str
        :param effective_at:  The effectiveAt or cut label that this item of structured result data is/was updated/inserted with.
        :type effective_at: str
        :param result_type:  An identifier that denotes the class of data that the id points to. This is not the same as the format, but a more generic identifier such as 'risk result', 'cashflow', 'index' or similar.
        :type result_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._code = None
        self._effective_at = None
        self._result_type = None
        self.discriminator = None

        self.source = source
        self.code = code
        self.effective_at = effective_at
        self.result_type = result_type

    @property
    def source(self):
        """Gets the source of this StructuredResultDataId.  # noqa: E501

        The platform or vendor that provided the structured result data, e.g. 'client'. This is primarily of interest when data could have been sourced from multiple sources  # noqa: E501

        :return: The source of this StructuredResultDataId.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this StructuredResultDataId.

        The platform or vendor that provided the structured result data, e.g. 'client'. This is primarily of interest when data could have been sourced from multiple sources  # noqa: E501

        :param source: The source of this StructuredResultDataId.  # noqa: E501
        :type source: str
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source is not None and len(source) > 256):
            raise ValueError("Invalid value for `source`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source is not None and len(source) < 1):
            raise ValueError("Invalid value for `source`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', source)):  # noqa: E501
            raise ValueError(r"Invalid value for `source`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._source = source

    @property
    def code(self):
        """Gets the code of this StructuredResultDataId.  # noqa: E501

        The identifier for the entity that this id describes. It could be an index, instrument or other form of structured data  # noqa: E501

        :return: The code of this StructuredResultDataId.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StructuredResultDataId.

        The identifier for the entity that this id describes. It could be an index, instrument or other form of structured data  # noqa: E501

        :param code: The code of this StructuredResultDataId.  # noqa: E501
        :type code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 256):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

    @property
    def effective_at(self):
        """Gets the effective_at of this StructuredResultDataId.  # noqa: E501

        The effectiveAt or cut label that this item of structured result data is/was updated/inserted with.  # noqa: E501

        :return: The effective_at of this StructuredResultDataId.  # noqa: E501
        :rtype: str
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this StructuredResultDataId.

        The effectiveAt or cut label that this item of structured result data is/was updated/inserted with.  # noqa: E501

        :param effective_at: The effective_at of this StructuredResultDataId.  # noqa: E501
        :type effective_at: str
        """

        self._effective_at = effective_at

    @property
    def result_type(self):
        """Gets the result_type of this StructuredResultDataId.  # noqa: E501

        An identifier that denotes the class of data that the id points to. This is not the same as the format, but a more generic identifier such as 'risk result', 'cashflow', 'index' or similar.  # noqa: E501

        :return: The result_type of this StructuredResultDataId.  # noqa: E501
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this StructuredResultDataId.

        An identifier that denotes the class of data that the id points to. This is not the same as the format, but a more generic identifier such as 'risk result', 'cashflow', 'index' or similar.  # noqa: E501

        :param result_type: The result_type of this StructuredResultDataId.  # noqa: E501
        :type result_type: str
        """

        self._result_type = result_type

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
        if not isinstance(other, StructuredResultDataId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StructuredResultDataId):
            return True

        return self.to_dict() != other.to_dict()
