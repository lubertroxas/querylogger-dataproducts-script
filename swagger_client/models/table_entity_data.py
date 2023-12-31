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

class TableEntityData(EntityModel):
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
        'catalog': 'str',
        'schema': 'str',
        'table': 'str',
        'columns': 'list[str]'
    }
    if hasattr(EntityModel, "swagger_types"):
        swagger_types.update(EntityModel.swagger_types)

    attribute_map = {
        'catalog': 'catalog',
        'schema': 'schema',
        'table': 'table',
        'columns': 'columns'
    }
    if hasattr(EntityModel, "attribute_map"):
        attribute_map.update(EntityModel.attribute_map)

    def __init__(self, catalog=None, schema=None, table=None, columns=None, *args, **kwargs):  # noqa: E501
        """TableEntityData - a model defined in Swagger"""  # noqa: E501
        self._catalog = None
        self._schema = None
        self._table = None
        self._columns = None
        self.discriminator = None
        if catalog is not None:
            self.catalog = catalog
        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table
        if columns is not None:
            self.columns = columns
        EntityModel.__init__(self, *args, **kwargs)

    @property
    def catalog(self):
        """Gets the catalog of this TableEntityData.  # noqa: E501

        If empty it applies to all catalogs  # noqa: E501

        :return: The catalog of this TableEntityData.  # noqa: E501
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this TableEntityData.

        If empty it applies to all catalogs  # noqa: E501

        :param catalog: The catalog of this TableEntityData.  # noqa: E501
        :type: str
        """

        self._catalog = catalog

    @property
    def schema(self):
        """Gets the schema of this TableEntityData.  # noqa: E501

        If empty it applies to all schemas of the entity's catalog  # noqa: E501

        :return: The schema of this TableEntityData.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this TableEntityData.

        If empty it applies to all schemas of the entity's catalog  # noqa: E501

        :param schema: The schema of this TableEntityData.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def table(self):
        """Gets the table of this TableEntityData.  # noqa: E501

        If empty it applies to all tables of the entity's schema  # noqa: E501

        :return: The table of this TableEntityData.  # noqa: E501
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this TableEntityData.

        If empty it applies to all tables of the entity's schema  # noqa: E501

        :param table: The table of this TableEntityData.  # noqa: E501
        :type: str
        """

        self._table = table

    @property
    def columns(self):
        """Gets the columns of this TableEntityData.  # noqa: E501

        If empty it applies to all columns of the entity's table  # noqa: E501

        :return: The columns of this TableEntityData.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this TableEntityData.

        If empty it applies to all columns of the entity's table  # noqa: E501

        :param columns: The columns of this TableEntityData.  # noqa: E501
        :type: list[str]
        """

        self._columns = columns

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
        if issubclass(TableEntityData, dict):
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
        if not isinstance(other, TableEntityData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
