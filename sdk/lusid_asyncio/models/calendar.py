# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3680
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


class Calendar(object):
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
        'id': 'ResourceId',
        'type': 'str',
        'weekend_mask': 'WeekendMask',
        'source_provider': 'str',
        'properties': 'list[ModelProperty]'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'type': 'type',
        'weekend_mask': 'weekendMask',
        'source_provider': 'sourceProvider',
        'properties': 'properties'
    }

    required_map = {
        'href': 'optional',
        'id': 'required',
        'type': 'required',
        'weekend_mask': 'required',
        'source_provider': 'required',
        'properties': 'required'
    }

    def __init__(self, href=None, id=None, type=None, weekend_mask=None, source_provider=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """Calendar - a model defined in OpenAPI"
        
        :param href: 
        :type href: str
        :param id:  (required)
        :type id: lusid_asyncio.ResourceId
        :param type:  (required)
        :type type: str
        :param weekend_mask:  (required)
        :type weekend_mask: lusid_asyncio.WeekendMask
        :param source_provider:  (required)
        :type source_provider: str
        :param properties:  (required)
        :type properties: list[lusid_asyncio.ModelProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._id = None
        self._type = None
        self._weekend_mask = None
        self._source_provider = None
        self._properties = None
        self.discriminator = None

        self.href = href
        self.id = id
        self.type = type
        self.weekend_mask = weekend_mask
        self.source_provider = source_provider
        self.properties = properties

    @property
    def href(self):
        """Gets the href of this Calendar.  # noqa: E501


        :return: The href of this Calendar.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Calendar.


        :param href: The href of this Calendar.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Calendar.  # noqa: E501


        :return: The id of this Calendar.  # noqa: E501
        :rtype: lusid_asyncio.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Calendar.


        :param id: The id of this Calendar.  # noqa: E501
        :type id: lusid_asyncio.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this Calendar.  # noqa: E501


        :return: The type of this Calendar.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Calendar.


        :param type: The type of this Calendar.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def weekend_mask(self):
        """Gets the weekend_mask of this Calendar.  # noqa: E501


        :return: The weekend_mask of this Calendar.  # noqa: E501
        :rtype: lusid_asyncio.WeekendMask
        """
        return self._weekend_mask

    @weekend_mask.setter
    def weekend_mask(self, weekend_mask):
        """Sets the weekend_mask of this Calendar.


        :param weekend_mask: The weekend_mask of this Calendar.  # noqa: E501
        :type weekend_mask: lusid_asyncio.WeekendMask
        """
        if self.local_vars_configuration.client_side_validation and weekend_mask is None:  # noqa: E501
            raise ValueError("Invalid value for `weekend_mask`, must not be `None`")  # noqa: E501

        self._weekend_mask = weekend_mask

    @property
    def source_provider(self):
        """Gets the source_provider of this Calendar.  # noqa: E501


        :return: The source_provider of this Calendar.  # noqa: E501
        :rtype: str
        """
        return self._source_provider

    @source_provider.setter
    def source_provider(self, source_provider):
        """Sets the source_provider of this Calendar.


        :param source_provider: The source_provider of this Calendar.  # noqa: E501
        :type source_provider: str
        """
        if self.local_vars_configuration.client_side_validation and source_provider is None:  # noqa: E501
            raise ValueError("Invalid value for `source_provider`, must not be `None`")  # noqa: E501

        self._source_provider = source_provider

    @property
    def properties(self):
        """Gets the properties of this Calendar.  # noqa: E501


        :return: The properties of this Calendar.  # noqa: E501
        :rtype: list[lusid_asyncio.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Calendar.


        :param properties: The properties of this Calendar.  # noqa: E501
        :type properties: list[lusid_asyncio.ModelProperty]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if not isinstance(other, Calendar):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Calendar):
            return True

        return self.to_dict() != other.to_dict()
