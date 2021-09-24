# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3534
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


class RelationshipDefinition(object):
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
        'version': 'Version',
        'relationship_definition_id': 'ResourceId',
        'source_entity_type': 'str',
        'target_entity_type': 'str',
        'display_name': 'str',
        'outward_description': 'str',
        'inward_description': 'str',
        'life_time': 'str',
        'relationship_cardinality': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'version': 'version',
        'relationship_definition_id': 'relationshipDefinitionId',
        'source_entity_type': 'sourceEntityType',
        'target_entity_type': 'targetEntityType',
        'display_name': 'displayName',
        'outward_description': 'outwardDescription',
        'inward_description': 'inwardDescription',
        'life_time': 'lifeTime',
        'relationship_cardinality': 'relationshipCardinality',
        'links': 'links'
    }

    required_map = {
        'version': 'optional',
        'relationship_definition_id': 'required',
        'source_entity_type': 'required',
        'target_entity_type': 'required',
        'display_name': 'required',
        'outward_description': 'required',
        'inward_description': 'required',
        'life_time': 'required',
        'relationship_cardinality': 'required',
        'links': 'optional'
    }

    def __init__(self, version=None, relationship_definition_id=None, source_entity_type=None, target_entity_type=None, display_name=None, outward_description=None, inward_description=None, life_time=None, relationship_cardinality=None, links=None, local_vars_configuration=None):  # noqa: E501
        """RelationshipDefinition - a model defined in OpenAPI"
        
        :param version: 
        :type version: lusid_asyncio.Version
        :param relationship_definition_id:  (required)
        :type relationship_definition_id: lusid_asyncio.ResourceId
        :param source_entity_type:  The entity type of the source entity object. (required)
        :type source_entity_type: str
        :param target_entity_type:  The entity type of the target entity object. (required)
        :type target_entity_type: str
        :param display_name:  The display name of the relationship. (required)
        :type display_name: str
        :param outward_description:  The description to relate source entity object and target entity object (required)
        :type outward_description: str
        :param inward_description:  The description to relate target entity object and source entity object (required)
        :type inward_description: str
        :param life_time:  Describes how the relationships can change over time. (required)
        :type life_time: str
        :param relationship_cardinality:  Describes the cardinality of the relationship between source entity and target entity. (required)
        :type relationship_cardinality: str
        :param links:  Collection of links.
        :type links: list[lusid_asyncio.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._relationship_definition_id = None
        self._source_entity_type = None
        self._target_entity_type = None
        self._display_name = None
        self._outward_description = None
        self._inward_description = None
        self._life_time = None
        self._relationship_cardinality = None
        self._links = None
        self.discriminator = None

        if version is not None:
            self.version = version
        self.relationship_definition_id = relationship_definition_id
        self.source_entity_type = source_entity_type
        self.target_entity_type = target_entity_type
        self.display_name = display_name
        self.outward_description = outward_description
        self.inward_description = inward_description
        self.life_time = life_time
        self.relationship_cardinality = relationship_cardinality
        self.links = links

    @property
    def version(self):
        """Gets the version of this RelationshipDefinition.  # noqa: E501


        :return: The version of this RelationshipDefinition.  # noqa: E501
        :rtype: lusid_asyncio.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RelationshipDefinition.


        :param version: The version of this RelationshipDefinition.  # noqa: E501
        :type version: lusid_asyncio.Version
        """

        self._version = version

    @property
    def relationship_definition_id(self):
        """Gets the relationship_definition_id of this RelationshipDefinition.  # noqa: E501


        :return: The relationship_definition_id of this RelationshipDefinition.  # noqa: E501
        :rtype: lusid_asyncio.ResourceId
        """
        return self._relationship_definition_id

    @relationship_definition_id.setter
    def relationship_definition_id(self, relationship_definition_id):
        """Sets the relationship_definition_id of this RelationshipDefinition.


        :param relationship_definition_id: The relationship_definition_id of this RelationshipDefinition.  # noqa: E501
        :type relationship_definition_id: lusid_asyncio.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and relationship_definition_id is None:  # noqa: E501
            raise ValueError("Invalid value for `relationship_definition_id`, must not be `None`")  # noqa: E501

        self._relationship_definition_id = relationship_definition_id

    @property
    def source_entity_type(self):
        """Gets the source_entity_type of this RelationshipDefinition.  # noqa: E501

        The entity type of the source entity object.  # noqa: E501

        :return: The source_entity_type of this RelationshipDefinition.  # noqa: E501
        :rtype: str
        """
        return self._source_entity_type

    @source_entity_type.setter
    def source_entity_type(self, source_entity_type):
        """Sets the source_entity_type of this RelationshipDefinition.

        The entity type of the source entity object.  # noqa: E501

        :param source_entity_type: The source_entity_type of this RelationshipDefinition.  # noqa: E501
        :type source_entity_type: str
        """
        if self.local_vars_configuration.client_side_validation and source_entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `source_entity_type`, must not be `None`")  # noqa: E501

        self._source_entity_type = source_entity_type

    @property
    def target_entity_type(self):
        """Gets the target_entity_type of this RelationshipDefinition.  # noqa: E501

        The entity type of the target entity object.  # noqa: E501

        :return: The target_entity_type of this RelationshipDefinition.  # noqa: E501
        :rtype: str
        """
        return self._target_entity_type

    @target_entity_type.setter
    def target_entity_type(self, target_entity_type):
        """Sets the target_entity_type of this RelationshipDefinition.

        The entity type of the target entity object.  # noqa: E501

        :param target_entity_type: The target_entity_type of this RelationshipDefinition.  # noqa: E501
        :type target_entity_type: str
        """
        if self.local_vars_configuration.client_side_validation and target_entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `target_entity_type`, must not be `None`")  # noqa: E501

        self._target_entity_type = target_entity_type

    @property
    def display_name(self):
        """Gets the display_name of this RelationshipDefinition.  # noqa: E501

        The display name of the relationship.  # noqa: E501

        :return: The display_name of this RelationshipDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this RelationshipDefinition.

        The display name of the relationship.  # noqa: E501

        :param display_name: The display_name of this RelationshipDefinition.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 512):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not re.search(r'^[\s\S]*$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._display_name = display_name

    @property
    def outward_description(self):
        """Gets the outward_description of this RelationshipDefinition.  # noqa: E501

        The description to relate source entity object and target entity object  # noqa: E501

        :return: The outward_description of this RelationshipDefinition.  # noqa: E501
        :rtype: str
        """
        return self._outward_description

    @outward_description.setter
    def outward_description(self, outward_description):
        """Sets the outward_description of this RelationshipDefinition.

        The description to relate source entity object and target entity object  # noqa: E501

        :param outward_description: The outward_description of this RelationshipDefinition.  # noqa: E501
        :type outward_description: str
        """
        if self.local_vars_configuration.client_side_validation and outward_description is None:  # noqa: E501
            raise ValueError("Invalid value for `outward_description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                outward_description is not None and len(outward_description) > 512):
            raise ValueError("Invalid value for `outward_description`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                outward_description is not None and len(outward_description) < 1):
            raise ValueError("Invalid value for `outward_description`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                outward_description is not None and not re.search(r'^[\s\S]*$', outward_description)):  # noqa: E501
            raise ValueError(r"Invalid value for `outward_description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._outward_description = outward_description

    @property
    def inward_description(self):
        """Gets the inward_description of this RelationshipDefinition.  # noqa: E501

        The description to relate target entity object and source entity object  # noqa: E501

        :return: The inward_description of this RelationshipDefinition.  # noqa: E501
        :rtype: str
        """
        return self._inward_description

    @inward_description.setter
    def inward_description(self, inward_description):
        """Sets the inward_description of this RelationshipDefinition.

        The description to relate target entity object and source entity object  # noqa: E501

        :param inward_description: The inward_description of this RelationshipDefinition.  # noqa: E501
        :type inward_description: str
        """
        if self.local_vars_configuration.client_side_validation and inward_description is None:  # noqa: E501
            raise ValueError("Invalid value for `inward_description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inward_description is not None and len(inward_description) > 512):
            raise ValueError("Invalid value for `inward_description`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inward_description is not None and len(inward_description) < 1):
            raise ValueError("Invalid value for `inward_description`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                inward_description is not None and not re.search(r'^[\s\S]*$', inward_description)):  # noqa: E501
            raise ValueError(r"Invalid value for `inward_description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._inward_description = inward_description

    @property
    def life_time(self):
        """Gets the life_time of this RelationshipDefinition.  # noqa: E501

        Describes how the relationships can change over time.  # noqa: E501

        :return: The life_time of this RelationshipDefinition.  # noqa: E501
        :rtype: str
        """
        return self._life_time

    @life_time.setter
    def life_time(self, life_time):
        """Sets the life_time of this RelationshipDefinition.

        Describes how the relationships can change over time.  # noqa: E501

        :param life_time: The life_time of this RelationshipDefinition.  # noqa: E501
        :type life_time: str
        """
        if self.local_vars_configuration.client_side_validation and life_time is None:  # noqa: E501
            raise ValueError("Invalid value for `life_time`, must not be `None`")  # noqa: E501

        self._life_time = life_time

    @property
    def relationship_cardinality(self):
        """Gets the relationship_cardinality of this RelationshipDefinition.  # noqa: E501

        Describes the cardinality of the relationship between source entity and target entity.  # noqa: E501

        :return: The relationship_cardinality of this RelationshipDefinition.  # noqa: E501
        :rtype: str
        """
        return self._relationship_cardinality

    @relationship_cardinality.setter
    def relationship_cardinality(self, relationship_cardinality):
        """Sets the relationship_cardinality of this RelationshipDefinition.

        Describes the cardinality of the relationship between source entity and target entity.  # noqa: E501

        :param relationship_cardinality: The relationship_cardinality of this RelationshipDefinition.  # noqa: E501
        :type relationship_cardinality: str
        """
        if self.local_vars_configuration.client_side_validation and relationship_cardinality is None:  # noqa: E501
            raise ValueError("Invalid value for `relationship_cardinality`, must not be `None`")  # noqa: E501

        self._relationship_cardinality = relationship_cardinality

    @property
    def links(self):
        """Gets the links of this RelationshipDefinition.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this RelationshipDefinition.  # noqa: E501
        :rtype: list[lusid_asyncio.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RelationshipDefinition.

        Collection of links.  # noqa: E501

        :param links: The links of this RelationshipDefinition.  # noqa: E501
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
        if not isinstance(other, RelationshipDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelationshipDefinition):
            return True

        return self.to_dict() != other.to_dict()
