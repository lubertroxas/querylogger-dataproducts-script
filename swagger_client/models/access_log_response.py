# coding: utf-8

"""
    Starburst Enterprise API documentation

    Documentation with details about endpoints and entities.  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccessLogResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'query_id': 'str',
        'action': 'str',
        'entity_category': 'str',
        'entity': 'str',
        'entity_specified': 'bool',
        'grant_option': 'bool',
        'access_result': 'AuditAccessResult',
        'user': 'str',
        'enabled_roles': 'list[str]',
        'at_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'query_id': 'queryId',
        'action': 'action',
        'entity_category': 'entityCategory',
        'entity': 'entity',
        'entity_specified': 'entitySpecified',
        'grant_option': 'grantOption',
        'access_result': 'accessResult',
        'user': 'user',
        'enabled_roles': 'enabledRoles',
        'at_time': 'atTime'
    }

    def __init__(self, id=None, query_id=None, action=None, entity_category=None, entity=None, entity_specified=None, grant_option=None, access_result=None, user=None, enabled_roles=None, at_time=None):  # noqa: E501
        """AccessLogResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._query_id = None
        self._action = None
        self._entity_category = None
        self._entity = None
        self._entity_specified = None
        self._grant_option = None
        self._access_result = None
        self._user = None
        self._enabled_roles = None
        self._at_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if query_id is not None:
            self.query_id = query_id
        if action is not None:
            self.action = action
        if entity_category is not None:
            self.entity_category = entity_category
        if entity is not None:
            self.entity = entity
        if entity_specified is not None:
            self.entity_specified = entity_specified
        if grant_option is not None:
            self.grant_option = grant_option
        if access_result is not None:
            self.access_result = access_result
        if user is not None:
            self.user = user
        if enabled_roles is not None:
            self.enabled_roles = enabled_roles
        if at_time is not None:
            self.at_time = at_time

    @property
    def id(self):
        """Gets the id of this AccessLogResponse.  # noqa: E501


        :return: The id of this AccessLogResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessLogResponse.


        :param id: The id of this AccessLogResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def query_id(self):
        """Gets the query_id of this AccessLogResponse.  # noqa: E501

        ID of the query that generated this access log  # noqa: E501

        :return: The query_id of this AccessLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this AccessLogResponse.

        ID of the query that generated this access log  # noqa: E501

        :param query_id: The query_id of this AccessLogResponse.  # noqa: E501
        :type: str
        """

        self._query_id = query_id

    @property
    def action(self):
        """Gets the action of this AccessLogResponse.  # noqa: E501

        The action for which access was requested, or (ANY) if action was not specified  # noqa: E501

        :return: The action of this AccessLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AccessLogResponse.

        The action for which access was requested, or (ANY) if action was not specified  # noqa: E501

        :param action: The action of this AccessLogResponse.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def entity_category(self):
        """Gets the entity_category of this AccessLogResponse.  # noqa: E501

        Category of the entity to which access was requested  # noqa: E501

        :return: The entity_category of this AccessLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity_category

    @entity_category.setter
    def entity_category(self, entity_category):
        """Sets the entity_category of this AccessLogResponse.

        Category of the entity to which access was requested  # noqa: E501

        :param entity_category: The entity_category of this AccessLogResponse.  # noqa: E501
        :type: str
        """

        self._entity_category = entity_category

    @property
    def entity(self):
        """Gets the entity of this AccessLogResponse.  # noqa: E501

        Entity to which access was requested  # noqa: E501

        :return: The entity of this AccessLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this AccessLogResponse.

        Entity to which access was requested  # noqa: E501

        :param entity: The entity of this AccessLogResponse.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def entity_specified(self):
        """Gets the entity_specified of this AccessLogResponse.  # noqa: E501

        If true, access was requested to a specific entity, otherwise access was requested to all entities of a given category  # noqa: E501

        :return: The entity_specified of this AccessLogResponse.  # noqa: E501
        :rtype: bool
        """
        return self._entity_specified

    @entity_specified.setter
    def entity_specified(self, entity_specified):
        """Sets the entity_specified of this AccessLogResponse.

        If true, access was requested to a specific entity, otherwise access was requested to all entities of a given category  # noqa: E501

        :param entity_specified: The entity_specified of this AccessLogResponse.  # noqa: E501
        :type: bool
        """

        self._entity_specified = entity_specified

    @property
    def grant_option(self):
        """Gets the grant_option of this AccessLogResponse.  # noqa: E501

        If true, the requester has WITH GRANT OPTION grant for the given entity  # noqa: E501

        :return: The grant_option of this AccessLogResponse.  # noqa: E501
        :rtype: bool
        """
        return self._grant_option

    @grant_option.setter
    def grant_option(self, grant_option):
        """Sets the grant_option of this AccessLogResponse.

        If true, the requester has WITH GRANT OPTION grant for the given entity  # noqa: E501

        :param grant_option: The grant_option of this AccessLogResponse.  # noqa: E501
        :type: bool
        """

        self._grant_option = grant_option

    @property
    def access_result(self):
        """Gets the access_result of this AccessLogResponse.  # noqa: E501


        :return: The access_result of this AccessLogResponse.  # noqa: E501
        :rtype: AuditAccessResult
        """
        return self._access_result

    @access_result.setter
    def access_result(self, access_result):
        """Sets the access_result of this AccessLogResponse.


        :param access_result: The access_result of this AccessLogResponse.  # noqa: E501
        :type: AuditAccessResult
        """

        self._access_result = access_result

    @property
    def user(self):
        """Gets the user of this AccessLogResponse.  # noqa: E501

        Session User  # noqa: E501

        :return: The user of this AccessLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AccessLogResponse.

        Session User  # noqa: E501

        :param user: The user of this AccessLogResponse.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def enabled_roles(self):
        """Gets the enabled_roles of this AccessLogResponse.  # noqa: E501

        Roles enabled on the session  # noqa: E501

        :return: The enabled_roles of this AccessLogResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._enabled_roles

    @enabled_roles.setter
    def enabled_roles(self, enabled_roles):
        """Sets the enabled_roles of this AccessLogResponse.

        Roles enabled on the session  # noqa: E501

        :param enabled_roles: The enabled_roles of this AccessLogResponse.  # noqa: E501
        :type: list[str]
        """

        self._enabled_roles = enabled_roles

    @property
    def at_time(self):
        """Gets the at_time of this AccessLogResponse.  # noqa: E501

        When access was requested  # noqa: E501

        :return: The at_time of this AccessLogResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._at_time

    @at_time.setter
    def at_time(self, at_time):
        """Sets the at_time of this AccessLogResponse.

        When access was requested  # noqa: E501

        :param at_time: The at_time of this AccessLogResponse.  # noqa: E501
        :type: datetime
        """

        self._at_time = at_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AccessLogResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccessLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
