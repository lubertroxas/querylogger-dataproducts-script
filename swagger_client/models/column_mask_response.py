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

class ColumnMaskResponse(object):
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
        'entity': 'EntityModel',
        'expression_id': 'int',
        'force_none': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'entity': 'entity',
        'expression_id': 'expressionId',
        'force_none': 'forceNone'
    }

    def __init__(self, id=None, entity=None, expression_id=None, force_none=None):  # noqa: E501
        """ColumnMaskResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._entity = None
        self._expression_id = None
        self._force_none = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if entity is not None:
            self.entity = entity
        if expression_id is not None:
            self.expression_id = expression_id
        if force_none is not None:
            self.force_none = force_none

    @property
    def id(self):
        """Gets the id of this ColumnMaskResponse.  # noqa: E501

        Id of the column mask applied to a role.  # noqa: E501

        :return: The id of this ColumnMaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ColumnMaskResponse.

        Id of the column mask applied to a role.  # noqa: E501

        :param id: The id of this ColumnMaskResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def entity(self):
        """Gets the entity of this ColumnMaskResponse.  # noqa: E501


        :return: The entity of this ColumnMaskResponse.  # noqa: E501
        :rtype: EntityModel
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this ColumnMaskResponse.


        :param entity: The entity of this ColumnMaskResponse.  # noqa: E501
        :type: EntityModel
        """

        self._entity = entity

    @property
    def expression_id(self):
        """Gets the expression_id of this ColumnMaskResponse.  # noqa: E501

        Id of the columm mask expression.  # noqa: E501

        :return: The expression_id of this ColumnMaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._expression_id

    @expression_id.setter
    def expression_id(self, expression_id):
        """Sets the expression_id of this ColumnMaskResponse.

        Id of the columm mask expression.  # noqa: E501

        :param expression_id: The expression_id of this ColumnMaskResponse.  # noqa: E501
        :type: int
        """

        self._expression_id = expression_id

    @property
    def force_none(self):
        """Gets the force_none of this ColumnMaskResponse.  # noqa: E501

        If true, forces not masking column values for the given entity, even if the subject is assigned to other roles with column masks to the same entity.  # noqa: E501

        :return: The force_none of this ColumnMaskResponse.  # noqa: E501
        :rtype: bool
        """
        return self._force_none

    @force_none.setter
    def force_none(self, force_none):
        """Sets the force_none of this ColumnMaskResponse.

        If true, forces not masking column values for the given entity, even if the subject is assigned to other roles with column masks to the same entity.  # noqa: E501

        :param force_none: The force_none of this ColumnMaskResponse.  # noqa: E501
        :type: bool
        """

        self._force_none = force_none

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
        if issubclass(ColumnMaskResponse, dict):
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
        if not isinstance(other, ColumnMaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
