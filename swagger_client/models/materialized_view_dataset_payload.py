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

class MaterializedViewDatasetPayload(object):
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
        'description': 'str',
        'definition_query': 'str',
        'definition_properties': 'dict(str, object)',
        'columns': 'list[ColumnDocumentation]',
        'marked_for_deletion': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'definition_query': 'definitionQuery',
        'definition_properties': 'definitionProperties',
        'columns': 'columns',
        'marked_for_deletion': 'markedForDeletion'
    }

    def __init__(self, name=None, description=None, definition_query=None, definition_properties=None, columns=None, marked_for_deletion=None):  # noqa: E501
        """MaterializedViewDatasetPayload - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._definition_query = None
        self._definition_properties = None
        self._columns = None
        self._marked_for_deletion = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        if definition_query is not None:
            self.definition_query = definition_query
        if definition_properties is not None:
            self.definition_properties = definition_properties
        if columns is not None:
            self.columns = columns
        if marked_for_deletion is not None:
            self.marked_for_deletion = marked_for_deletion

    @property
    def name(self):
        """Gets the name of this MaterializedViewDatasetPayload.  # noqa: E501

        Name of the dataset.  Must be a valid SQL name with lowercase letters.  # noqa: E501

        :return: The name of this MaterializedViewDatasetPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MaterializedViewDatasetPayload.

        Name of the dataset.  Must be a valid SQL name with lowercase letters.  # noqa: E501

        :param name: The name of this MaterializedViewDatasetPayload.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this MaterializedViewDatasetPayload.  # noqa: E501

        Description of the dataset.  # noqa: E501

        :return: The description of this MaterializedViewDatasetPayload.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MaterializedViewDatasetPayload.

        Description of the dataset.  # noqa: E501

        :param description: The description of this MaterializedViewDatasetPayload.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def definition_query(self):
        """Gets the definition_query of this MaterializedViewDatasetPayload.  # noqa: E501

        Definition query for the materialized view.  # noqa: E501

        :return: The definition_query of this MaterializedViewDatasetPayload.  # noqa: E501
        :rtype: str
        """
        return self._definition_query

    @definition_query.setter
    def definition_query(self, definition_query):
        """Sets the definition_query of this MaterializedViewDatasetPayload.

        Definition query for the materialized view.  # noqa: E501

        :param definition_query: The definition_query of this MaterializedViewDatasetPayload.  # noqa: E501
        :type: str
        """

        self._definition_query = definition_query

    @property
    def definition_properties(self):
        """Gets the definition_properties of this MaterializedViewDatasetPayload.  # noqa: E501

        Map of definition properties for the materialized view. Valid keys are **refresh_interval** and **incremental_column**.  # noqa: E501

        :return: The definition_properties of this MaterializedViewDatasetPayload.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._definition_properties

    @definition_properties.setter
    def definition_properties(self, definition_properties):
        """Sets the definition_properties of this MaterializedViewDatasetPayload.

        Map of definition properties for the materialized view. Valid keys are **refresh_interval** and **incremental_column**.  # noqa: E501

        :param definition_properties: The definition_properties of this MaterializedViewDatasetPayload.  # noqa: E501
        :type: dict(str, object)
        """

        self._definition_properties = definition_properties

    @property
    def columns(self):
        """Gets the columns of this MaterializedViewDatasetPayload.  # noqa: E501

        List of column definitions for the dataset.  # noqa: E501

        :return: The columns of this MaterializedViewDatasetPayload.  # noqa: E501
        :rtype: list[ColumnDocumentation]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this MaterializedViewDatasetPayload.

        List of column definitions for the dataset.  # noqa: E501

        :param columns: The columns of this MaterializedViewDatasetPayload.  # noqa: E501
        :type: list[ColumnDocumentation]
        """

        self._columns = columns

    @property
    def marked_for_deletion(self):
        """Gets the marked_for_deletion of this MaterializedViewDatasetPayload.  # noqa: E501

        Whether this dataset is marked to be deleted in the next publishing workflow  # noqa: E501

        :return: The marked_for_deletion of this MaterializedViewDatasetPayload.  # noqa: E501
        :rtype: bool
        """
        return self._marked_for_deletion

    @marked_for_deletion.setter
    def marked_for_deletion(self, marked_for_deletion):
        """Sets the marked_for_deletion of this MaterializedViewDatasetPayload.

        Whether this dataset is marked to be deleted in the next publishing workflow  # noqa: E501

        :param marked_for_deletion: The marked_for_deletion of this MaterializedViewDatasetPayload.  # noqa: E501
        :type: bool
        """

        self._marked_for_deletion = marked_for_deletion

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
        if issubclass(MaterializedViewDatasetPayload, dict):
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
        if not isinstance(other, MaterializedViewDatasetPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other