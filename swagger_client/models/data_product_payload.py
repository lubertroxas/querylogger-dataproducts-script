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

class DataProductPayload(object):
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
        'catalog_name': 'str',
        'data_domain_id': 'str',
        'summary': 'str',
        'description': 'str',
        'views': 'list[ViewDatasetPayload]',
        'materialized_views': 'list[MaterializedViewDatasetPayload]',
        'owners': 'list[DataProductOwner]',
        'relevant_links': 'list[RelevantLink]'
    }

    attribute_map = {
        'name': 'name',
        'catalog_name': 'catalogName',
        'data_domain_id': 'dataDomainId',
        'summary': 'summary',
        'description': 'description',
        'views': 'views',
        'materialized_views': 'materializedViews',
        'owners': 'owners',
        'relevant_links': 'relevantLinks'
    }

    def __init__(self, name=None, catalog_name=None, data_domain_id=None, summary=None, description=None, views=None, materialized_views=None, owners=None, relevant_links=None):  # noqa: E501
        """DataProductPayload - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._catalog_name = None
        self._data_domain_id = None
        self._summary = None
        self._description = None
        self._views = None
        self._materialized_views = None
        self._owners = None
        self._relevant_links = None
        self.discriminator = None
        self.name = name
        self.catalog_name = catalog_name
        self.data_domain_id = data_domain_id
        self.summary = summary
        if description is not None:
            self.description = description
        if views is not None:
            self.views = views
        if materialized_views is not None:
            self.materialized_views = materialized_views
        if owners is not None:
            self.owners = owners
        if relevant_links is not None:
            self.relevant_links = relevant_links

    @property
    def name(self):
        """Gets the name of this DataProductPayload.  # noqa: E501

        Data product name.  # noqa: E501

        :return: The name of this DataProductPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataProductPayload.

        Data product name.  # noqa: E501

        :param name: The name of this DataProductPayload.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def catalog_name(self):
        """Gets the catalog_name of this DataProductPayload.  # noqa: E501

        Catalog for this data product.  # noqa: E501

        :return: The catalog_name of this DataProductPayload.  # noqa: E501
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this DataProductPayload.

        Catalog for this data product.  # noqa: E501

        :param catalog_name: The catalog_name of this DataProductPayload.  # noqa: E501
        :type: str
        """
        if catalog_name is None:
            raise ValueError("Invalid value for `catalog_name`, must not be `None`")  # noqa: E501

        self._catalog_name = catalog_name

    @property
    def data_domain_id(self):
        """Gets the data_domain_id of this DataProductPayload.  # noqa: E501

        UUID of the domain that this data product belongs to.  # noqa: E501

        :return: The data_domain_id of this DataProductPayload.  # noqa: E501
        :rtype: str
        """
        return self._data_domain_id

    @data_domain_id.setter
    def data_domain_id(self, data_domain_id):
        """Sets the data_domain_id of this DataProductPayload.

        UUID of the domain that this data product belongs to.  # noqa: E501

        :param data_domain_id: The data_domain_id of this DataProductPayload.  # noqa: E501
        :type: str
        """
        if data_domain_id is None:
            raise ValueError("Invalid value for `data_domain_id`, must not be `None`")  # noqa: E501

        self._data_domain_id = data_domain_id

    @property
    def summary(self):
        """Gets the summary of this DataProductPayload.  # noqa: E501

        Summary description for this data product.  # noqa: E501

        :return: The summary of this DataProductPayload.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this DataProductPayload.

        Summary description for this data product.  # noqa: E501

        :param summary: The summary of this DataProductPayload.  # noqa: E501
        :type: str
        """
        if summary is None:
            raise ValueError("Invalid value for `summary`, must not be `None`")  # noqa: E501

        self._summary = summary

    @property
    def description(self):
        """Gets the description of this DataProductPayload.  # noqa: E501

        Detailed description for this data product.  # noqa: E501

        :return: The description of this DataProductPayload.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataProductPayload.

        Detailed description for this data product.  # noqa: E501

        :param description: The description of this DataProductPayload.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def views(self):
        """Gets the views of this DataProductPayload.  # noqa: E501

        List of view datasets  # noqa: E501

        :return: The views of this DataProductPayload.  # noqa: E501
        :rtype: list[ViewDatasetPayload]
        """
        return self._views

    @views.setter
    def views(self, views):
        """Sets the views of this DataProductPayload.

        List of view datasets  # noqa: E501

        :param views: The views of this DataProductPayload.  # noqa: E501
        :type: list[ViewDatasetPayload]
        """

        self._views = views

    @property
    def materialized_views(self):
        """Gets the materialized_views of this DataProductPayload.  # noqa: E501

        List of materialized view datasets  # noqa: E501

        :return: The materialized_views of this DataProductPayload.  # noqa: E501
        :rtype: list[MaterializedViewDatasetPayload]
        """
        return self._materialized_views

    @materialized_views.setter
    def materialized_views(self, materialized_views):
        """Sets the materialized_views of this DataProductPayload.

        List of materialized view datasets  # noqa: E501

        :param materialized_views: The materialized_views of this DataProductPayload.  # noqa: E501
        :type: list[MaterializedViewDatasetPayload]
        """

        self._materialized_views = materialized_views

    @property
    def owners(self):
        """Gets the owners of this DataProductPayload.  # noqa: E501

        User-supplied list of owners.  Used to indicate who is maintaining this data product.  # noqa: E501

        :return: The owners of this DataProductPayload.  # noqa: E501
        :rtype: list[DataProductOwner]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this DataProductPayload.

        User-supplied list of owners.  Used to indicate who is maintaining this data product.  # noqa: E501

        :param owners: The owners of this DataProductPayload.  # noqa: E501
        :type: list[DataProductOwner]
        """

        self._owners = owners

    @property
    def relevant_links(self):
        """Gets the relevant_links of this DataProductPayload.  # noqa: E501

        Relevant links for this data product.  # noqa: E501

        :return: The relevant_links of this DataProductPayload.  # noqa: E501
        :rtype: list[RelevantLink]
        """
        return self._relevant_links

    @relevant_links.setter
    def relevant_links(self, relevant_links):
        """Sets the relevant_links of this DataProductPayload.

        Relevant links for this data product.  # noqa: E501

        :param relevant_links: The relevant_links of this DataProductPayload.  # noqa: E501
        :type: list[RelevantLink]
        """

        self._relevant_links = relevant_links

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
        if issubclass(DataProductPayload, dict):
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
        if not isinstance(other, DataProductPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
