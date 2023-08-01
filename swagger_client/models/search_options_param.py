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

class SearchOptionsParam(object):
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
        'value': 'SearchOptions',
        'original_param': 'str'
    }

    attribute_map = {
        'value': 'value',
        'original_param': 'originalParam'
    }

    def __init__(self, value=None, original_param=None):  # noqa: E501
        """SearchOptionsParam - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._original_param = None
        self.discriminator = None
        self.value = value
        if original_param is not None:
            self.original_param = original_param

    @property
    def value(self):
        """Gets the value of this SearchOptionsParam.  # noqa: E501


        :return: The value of this SearchOptionsParam.  # noqa: E501
        :rtype: SearchOptions
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SearchOptionsParam.


        :param value: The value of this SearchOptionsParam.  # noqa: E501
        :type: SearchOptions
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def original_param(self):
        """Gets the original_param of this SearchOptionsParam.  # noqa: E501


        :return: The original_param of this SearchOptionsParam.  # noqa: E501
        :rtype: str
        """
        return self._original_param

    @original_param.setter
    def original_param(self, original_param):
        """Sets the original_param of this SearchOptionsParam.


        :param original_param: The original_param of this SearchOptionsParam.  # noqa: E501
        :type: str
        """

        self._original_param = original_param

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
        if issubclass(SearchOptionsParam, dict):
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
        if not isinstance(other, SearchOptionsParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
