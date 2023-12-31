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

class ExpressionPayload(object):
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
        'name': 'str',
        'expression': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'expression': 'expression',
        'description': 'description'
    }

    def __init__(self, name=None, expression=None, description=None):  # noqa: E501
        """ExpressionPayload - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._expression = None
        self._description = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if expression is not None:
            self.expression = expression
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this ExpressionPayload.  # noqa: E501

        Expression name  # noqa: E501

        :return: The name of this ExpressionPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExpressionPayload.

        Expression name  # noqa: E501

        :param name: The name of this ExpressionPayload.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def expression(self):
        """Gets the expression of this ExpressionPayload.  # noqa: E501

        Expression definition in SQL  # noqa: E501

        :return: The expression of this ExpressionPayload.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this ExpressionPayload.

        Expression definition in SQL  # noqa: E501

        :param expression: The expression of this ExpressionPayload.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def description(self):
        """Gets the description of this ExpressionPayload.  # noqa: E501

        Optional expression description  # noqa: E501

        :return: The description of this ExpressionPayload.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExpressionPayload.

        Optional expression description  # noqa: E501

        :param description: The description of this ExpressionPayload.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(ExpressionPayload, dict):
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
        if not isinstance(other, ExpressionPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
