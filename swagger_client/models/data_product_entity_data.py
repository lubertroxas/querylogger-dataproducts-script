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
from swagger_client.models.entity_model import EntityModel  # noqa: F401,E501

class DataProductEntityData(EntityModel):
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
        'domain_name': 'str',
        'data_product_name': 'str'
    }
    if hasattr(EntityModel, "swagger_types"):
        swagger_types.update(EntityModel.swagger_types)

    attribute_map = {
        'domain_name': 'domainName',
        'data_product_name': 'dataProductName'
    }
    if hasattr(EntityModel, "attribute_map"):
        attribute_map.update(EntityModel.attribute_map)

    def __init__(self, domain_name=None, data_product_name=None, *args, **kwargs):  # noqa: E501
        """DataProductEntityData - a model defined in Swagger"""  # noqa: E501
        self._domain_name = None
        self._data_product_name = None
        self.discriminator = None
        if domain_name is not None:
            self.domain_name = domain_name
        if data_product_name is not None:
            self.data_product_name = data_product_name
        EntityModel.__init__(self, *args, **kwargs)

    @property
    def domain_name(self):
        """Gets the domain_name of this DataProductEntityData.  # noqa: E501

        If empty it applies to all domains  # noqa: E501

        :return: The domain_name of this DataProductEntityData.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DataProductEntityData.

        If empty it applies to all domains  # noqa: E501

        :param domain_name: The domain_name of this DataProductEntityData.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def data_product_name(self):
        """Gets the data_product_name of this DataProductEntityData.  # noqa: E501

        If empty it applies to all data products in the entity's domain  # noqa: E501

        :return: The data_product_name of this DataProductEntityData.  # noqa: E501
        :rtype: str
        """
        return self._data_product_name

    @data_product_name.setter
    def data_product_name(self, data_product_name):
        """Sets the data_product_name of this DataProductEntityData.

        If empty it applies to all data products in the entity's domain  # noqa: E501

        :param data_product_name: The data_product_name of this DataProductEntityData.  # noqa: E501
        :type: str
        """

        self._data_product_name = data_product_name

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
        if issubclass(DataProductEntityData, dict):
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
        if not isinstance(other, DataProductEntityData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
