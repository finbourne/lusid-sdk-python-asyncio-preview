# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3758
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


class UpsertQuotesResponse(object):
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
        'href': 'str',
        'values': 'dict(str, Quote)',
        'failed': 'dict(str, ErrorDetail)',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'values': 'values',
        'failed': 'failed',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'values': 'optional',
        'failed': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, values=None, failed=None, links=None, local_vars_configuration=None):  # noqa: E501
        """UpsertQuotesResponse - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param values:  The quotes which have been successfully updated or inserted.
        :type values: dict[str, lusid_asyncio.Quote]
        :param failed:  The quotes that could not be updated or inserted along with a reason for their failure.
        :type failed: dict[str, lusid_asyncio.ErrorDetail]
        :param links:  Collection of links.
        :type links: list[lusid_asyncio.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._values = None
        self._failed = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.values = values
        self.failed = failed
        self.links = links

    @property
    def href(self):
        """Gets the href of this UpsertQuotesResponse.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this UpsertQuotesResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this UpsertQuotesResponse.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this UpsertQuotesResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def values(self):
        """Gets the values of this UpsertQuotesResponse.  # noqa: E501

        The quotes which have been successfully updated or inserted.  # noqa: E501

        :return: The values of this UpsertQuotesResponse.  # noqa: E501
        :rtype: dict[str, lusid_asyncio.Quote]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this UpsertQuotesResponse.

        The quotes which have been successfully updated or inserted.  # noqa: E501

        :param values: The values of this UpsertQuotesResponse.  # noqa: E501
        :type values: dict[str, lusid_asyncio.Quote]
        """

        self._values = values

    @property
    def failed(self):
        """Gets the failed of this UpsertQuotesResponse.  # noqa: E501

        The quotes that could not be updated or inserted along with a reason for their failure.  # noqa: E501

        :return: The failed of this UpsertQuotesResponse.  # noqa: E501
        :rtype: dict[str, lusid_asyncio.ErrorDetail]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this UpsertQuotesResponse.

        The quotes that could not be updated or inserted along with a reason for their failure.  # noqa: E501

        :param failed: The failed of this UpsertQuotesResponse.  # noqa: E501
        :type failed: dict[str, lusid_asyncio.ErrorDetail]
        """

        self._failed = failed

    @property
    def links(self):
        """Gets the links of this UpsertQuotesResponse.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this UpsertQuotesResponse.  # noqa: E501
        :rtype: list[lusid_asyncio.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UpsertQuotesResponse.

        Collection of links.  # noqa: E501

        :param links: The links of this UpsertQuotesResponse.  # noqa: E501
        :type links: list[lusid_asyncio.Link]
        """

        self._links = links

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
        if not isinstance(other, UpsertQuotesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpsertQuotesResponse):
            return True

        return self.to_dict() != other.to_dict()
