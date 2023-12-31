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

class DataProductSummary(object):
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
        'id': 'str',
        'name': 'str',
        'catalog_name': 'str',
        'schema_name': 'str',
        'data_domain_id': 'str',
        'summary': 'str',
        'description': 'str',
        'created_by': 'str',
        'status': 'DataProductStatus',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'published_at': 'datetime',
        'published_by': 'str',
        'last_queried_at': 'datetime',
        'last_queried_by': 'str',
        'ratings_average': 'float',
        'ratings_count': 'int',
        'user_data': 'DataProductUserData'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'catalog_name': 'catalogName',
        'schema_name': 'schemaName',
        'data_domain_id': 'dataDomainId',
        'summary': 'summary',
        'description': 'description',
        'created_by': 'createdBy',
        'status': 'status',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'published_at': 'publishedAt',
        'published_by': 'publishedBy',
        'last_queried_at': 'lastQueriedAt',
        'last_queried_by': 'lastQueriedBy',
        'ratings_average': 'ratingsAverage',
        'ratings_count': 'ratingsCount',
        'user_data': 'userData'
    }

    def __init__(self, id=None, name=None, catalog_name=None, schema_name=None, data_domain_id=None, summary=None, description=None, created_by=None, status=None, created_at=None, updated_at=None, published_at=None, published_by=None, last_queried_at=None, last_queried_by=None, ratings_average=None, ratings_count=None, user_data=None):  # noqa: E501
        """DataProductSummary - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._catalog_name = None
        self._schema_name = None
        self._data_domain_id = None
        self._summary = None
        self._description = None
        self._created_by = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._published_at = None
        self._published_by = None
        self._last_queried_at = None
        self._last_queried_by = None
        self._ratings_average = None
        self._ratings_count = None
        self._user_data = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if catalog_name is not None:
            self.catalog_name = catalog_name
        if schema_name is not None:
            self.schema_name = schema_name
        if data_domain_id is not None:
            self.data_domain_id = data_domain_id
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if created_by is not None:
            self.created_by = created_by
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if published_at is not None:
            self.published_at = published_at
        if published_by is not None:
            self.published_by = published_by
        if last_queried_at is not None:
            self.last_queried_at = last_queried_at
        if last_queried_by is not None:
            self.last_queried_by = last_queried_by
        if ratings_average is not None:
            self.ratings_average = ratings_average
        if ratings_count is not None:
            self.ratings_count = ratings_count
        if user_data is not None:
            self.user_data = user_data

    @property
    def id(self):
        """Gets the id of this DataProductSummary.  # noqa: E501

        Data product ID  # noqa: E501

        :return: The id of this DataProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataProductSummary.

        Data product ID  # noqa: E501

        :param id: The id of this DataProductSummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DataProductSummary.  # noqa: E501

        Data product name.  # noqa: E501

        :return: The name of this DataProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataProductSummary.

        Data product name.  # noqa: E501

        :param name: The name of this DataProductSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def catalog_name(self):
        """Gets the catalog_name of this DataProductSummary.  # noqa: E501

        Catalog for this data product.  # noqa: E501

        :return: The catalog_name of this DataProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this DataProductSummary.

        Catalog for this data product.  # noqa: E501

        :param catalog_name: The catalog_name of this DataProductSummary.  # noqa: E501
        :type: str
        """

        self._catalog_name = catalog_name

    @property
    def schema_name(self):
        """Gets the schema_name of this DataProductSummary.  # noqa: E501

        Trino schema name that will be generated for this data product.  # noqa: E501

        :return: The schema_name of this DataProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this DataProductSummary.

        Trino schema name that will be generated for this data product.  # noqa: E501

        :param schema_name: The schema_name of this DataProductSummary.  # noqa: E501
        :type: str
        """

        self._schema_name = schema_name

    @property
    def data_domain_id(self):
        """Gets the data_domain_id of this DataProductSummary.  # noqa: E501

        ID of the domain that this data product belongs to.  # noqa: E501

        :return: The data_domain_id of this DataProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._data_domain_id

    @data_domain_id.setter
    def data_domain_id(self, data_domain_id):
        """Sets the data_domain_id of this DataProductSummary.

        ID of the domain that this data product belongs to.  # noqa: E501

        :param data_domain_id: The data_domain_id of this DataProductSummary.  # noqa: E501
        :type: str
        """

        self._data_domain_id = data_domain_id

    @property
    def summary(self):
        """Gets the summary of this DataProductSummary.  # noqa: E501

        Summary description for this data product.  # noqa: E501

        :return: The summary of this DataProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this DataProductSummary.

        Summary description for this data product.  # noqa: E501

        :param summary: The summary of this DataProductSummary.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def description(self):
        """Gets the description of this DataProductSummary.  # noqa: E501

        Description for this data product.  # noqa: E501

        :return: The description of this DataProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataProductSummary.

        Description for this data product.  # noqa: E501

        :param description: The description of this DataProductSummary.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_by(self):
        """Gets the created_by of this DataProductSummary.  # noqa: E501

        User who created this data product.  # noqa: E501

        :return: The created_by of this DataProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this DataProductSummary.

        User who created this data product.  # noqa: E501

        :param created_by: The created_by of this DataProductSummary.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def status(self):
        """Gets the status of this DataProductSummary.  # noqa: E501


        :return: The status of this DataProductSummary.  # noqa: E501
        :rtype: DataProductStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataProductSummary.


        :param status: The status of this DataProductSummary.  # noqa: E501
        :type: DataProductStatus
        """

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this DataProductSummary.  # noqa: E501

        Timestamp of when this data product was created.  # noqa: E501

        :return: The created_at of this DataProductSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DataProductSummary.

        Timestamp of when this data product was created.  # noqa: E501

        :param created_at: The created_at of this DataProductSummary.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DataProductSummary.  # noqa: E501

        Timestamp of when this data product was last updated.  Will be initialized to createdAt timestamp.  # noqa: E501

        :return: The updated_at of this DataProductSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DataProductSummary.

        Timestamp of when this data product was last updated.  Will be initialized to createdAt timestamp.  # noqa: E501

        :param updated_at: The updated_at of this DataProductSummary.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def published_at(self):
        """Gets the published_at of this DataProductSummary.  # noqa: E501

        Timestamp of when this data product was last published.  # noqa: E501

        :return: The published_at of this DataProductSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this DataProductSummary.

        Timestamp of when this data product was last published.  # noqa: E501

        :param published_at: The published_at of this DataProductSummary.  # noqa: E501
        :type: datetime
        """

        self._published_at = published_at

    @property
    def published_by(self):
        """Gets the published_by of this DataProductSummary.  # noqa: E501

        User who published this data product.  # noqa: E501

        :return: The published_by of this DataProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._published_by

    @published_by.setter
    def published_by(self, published_by):
        """Sets the published_by of this DataProductSummary.

        User who published this data product.  # noqa: E501

        :param published_by: The published_by of this DataProductSummary.  # noqa: E501
        :type: str
        """

        self._published_by = published_by

    @property
    def last_queried_at(self):
        """Gets the last_queried_at of this DataProductSummary.  # noqa: E501

        Timestamp of when this data product was last queried.  # noqa: E501

        :return: The last_queried_at of this DataProductSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._last_queried_at

    @last_queried_at.setter
    def last_queried_at(self, last_queried_at):
        """Sets the last_queried_at of this DataProductSummary.

        Timestamp of when this data product was last queried.  # noqa: E501

        :param last_queried_at: The last_queried_at of this DataProductSummary.  # noqa: E501
        :type: datetime
        """

        self._last_queried_at = last_queried_at

    @property
    def last_queried_by(self):
        """Gets the last_queried_by of this DataProductSummary.  # noqa: E501

        Last user who used this data product.  # noqa: E501

        :return: The last_queried_by of this DataProductSummary.  # noqa: E501
        :rtype: str
        """
        return self._last_queried_by

    @last_queried_by.setter
    def last_queried_by(self, last_queried_by):
        """Sets the last_queried_by of this DataProductSummary.

        Last user who used this data product.  # noqa: E501

        :param last_queried_by: The last_queried_by of this DataProductSummary.  # noqa: E501
        :type: str
        """

        self._last_queried_by = last_queried_by

    @property
    def ratings_average(self):
        """Gets the ratings_average of this DataProductSummary.  # noqa: E501

        Average user rating of this data product.  If empty then this data product has not been rated yet.  # noqa: E501

        :return: The ratings_average of this DataProductSummary.  # noqa: E501
        :rtype: float
        """
        return self._ratings_average

    @ratings_average.setter
    def ratings_average(self, ratings_average):
        """Sets the ratings_average of this DataProductSummary.

        Average user rating of this data product.  If empty then this data product has not been rated yet.  # noqa: E501

        :param ratings_average: The ratings_average of this DataProductSummary.  # noqa: E501
        :type: float
        """

        self._ratings_average = ratings_average

    @property
    def ratings_count(self):
        """Gets the ratings_count of this DataProductSummary.  # noqa: E501

        Number of user ratings of this data product.  # noqa: E501

        :return: The ratings_count of this DataProductSummary.  # noqa: E501
        :rtype: int
        """
        return self._ratings_count

    @ratings_count.setter
    def ratings_count(self, ratings_count):
        """Sets the ratings_count of this DataProductSummary.

        Number of user ratings of this data product.  # noqa: E501

        :param ratings_count: The ratings_count of this DataProductSummary.  # noqa: E501
        :type: int
        """

        self._ratings_count = ratings_count

    @property
    def user_data(self):
        """Gets the user_data of this DataProductSummary.  # noqa: E501


        :return: The user_data of this DataProductSummary.  # noqa: E501
        :rtype: DataProductUserData
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this DataProductSummary.


        :param user_data: The user_data of this DataProductSummary.  # noqa: E501
        :type: DataProductUserData
        """

        self._user_data = user_data

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
        if issubclass(DataProductSummary, dict):
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
        if not isinstance(other, DataProductSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
