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

class SearchOptions(object):
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
        'search_string': 'str',
        'sort_key': 'SortKey',
        'sort_direction': 'str',
        'limit': 'SearchOptionsLimit',
        'only_bookmarked': 'bool',
        'data_domain_ids': 'list[str]',
        'tag_ids': 'list[str]'
    }

    attribute_map = {
        'search_string': 'searchString',
        'sort_key': 'sortKey',
        'sort_direction': 'sortDirection',
        'limit': 'limit',
        'only_bookmarked': 'onlyBookmarked',
        'data_domain_ids': 'dataDomainIds',
        'tag_ids': 'tagIds'
    }

    def __init__(self, search_string=None, sort_key=None, sort_direction=None, limit=None, only_bookmarked=None, data_domain_ids=None, tag_ids=None):  # noqa: E501
        """SearchOptions - a model defined in Swagger"""  # noqa: E501
        self._search_string = None
        self._sort_key = None
        self._sort_direction = None
        self._limit = None
        self._only_bookmarked = None
        self._data_domain_ids = None
        self._tag_ids = None
        self.discriminator = None
        if search_string is not None:
            self.search_string = search_string
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_direction is not None:
            self.sort_direction = sort_direction
        if limit is not None:
            self.limit = limit
        if only_bookmarked is not None:
            self.only_bookmarked = only_bookmarked
        if data_domain_ids is not None:
            self.data_domain_ids = data_domain_ids
        if tag_ids is not None:
            self.tag_ids = tag_ids

    @property
    def search_string(self):
        """Gets the search_string of this SearchOptions.  # noqa: E501

        Returns all data products containing this string.  The following fields are searched: Data Product: name, description, creator Data sets: name, description Column Descriptions: name, description, dataset name.  # noqa: E501

        :return: The search_string of this SearchOptions.  # noqa: E501
        :rtype: str
        """
        return self._search_string

    @search_string.setter
    def search_string(self, search_string):
        """Sets the search_string of this SearchOptions.

        Returns all data products containing this string.  The following fields are searched: Data Product: name, description, creator Data sets: name, description Column Descriptions: name, description, dataset name.  # noqa: E501

        :param search_string: The search_string of this SearchOptions.  # noqa: E501
        :type: str
        """

        self._search_string = search_string

    @property
    def sort_key(self):
        """Gets the sort_key of this SearchOptions.  # noqa: E501


        :return: The sort_key of this SearchOptions.  # noqa: E501
        :rtype: SortKey
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this SearchOptions.


        :param sort_key: The sort_key of this SearchOptions.  # noqa: E501
        :type: SortKey
        """

        self._sort_key = sort_key

    @property
    def sort_direction(self):
        """Gets the sort_direction of this SearchOptions.  # noqa: E501

        Specifies if sorting is ascending or descending.  # noqa: E501

        :return: The sort_direction of this SearchOptions.  # noqa: E501
        :rtype: str
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        """Sets the sort_direction of this SearchOptions.

        Specifies if sorting is ascending or descending.  # noqa: E501

        :param sort_direction: The sort_direction of this SearchOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASC", "DESC"]  # noqa: E501
        if sort_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_direction, allowed_values)
            )

        self._sort_direction = sort_direction

    @property
    def limit(self):
        """Gets the limit of this SearchOptions.  # noqa: E501


        :return: The limit of this SearchOptions.  # noqa: E501
        :rtype: SearchOptionsLimit
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchOptions.


        :param limit: The limit of this SearchOptions.  # noqa: E501
        :type: SearchOptionsLimit
        """

        self._limit = limit

    @property
    def only_bookmarked(self):
        """Gets the only_bookmarked of this SearchOptions.  # noqa: E501

        If true return only data products bookmarked by the authorized user.  # noqa: E501

        :return: The only_bookmarked of this SearchOptions.  # noqa: E501
        :rtype: bool
        """
        return self._only_bookmarked

    @only_bookmarked.setter
    def only_bookmarked(self, only_bookmarked):
        """Sets the only_bookmarked of this SearchOptions.

        If true return only data products bookmarked by the authorized user.  # noqa: E501

        :param only_bookmarked: The only_bookmarked of this SearchOptions.  # noqa: E501
        :type: bool
        """

        self._only_bookmarked = only_bookmarked

    @property
    def data_domain_ids(self):
        """Gets the data_domain_ids of this SearchOptions.  # noqa: E501

        Restrict data products to those contained in specified domains.  # noqa: E501

        :return: The data_domain_ids of this SearchOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_domain_ids

    @data_domain_ids.setter
    def data_domain_ids(self, data_domain_ids):
        """Sets the data_domain_ids of this SearchOptions.

        Restrict data products to those contained in specified domains.  # noqa: E501

        :param data_domain_ids: The data_domain_ids of this SearchOptions.  # noqa: E501
        :type: list[str]
        """

        self._data_domain_ids = data_domain_ids

    @property
    def tag_ids(self):
        """Gets the tag_ids of this SearchOptions.  # noqa: E501

        Restrict data products to those with specified tags.  # noqa: E501

        :return: The tag_ids of this SearchOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this SearchOptions.

        Restrict data products to those with specified tags.  # noqa: E501

        :param tag_ids: The tag_ids of this SearchOptions.  # noqa: E501
        :type: list[str]
        """

        self._tag_ids = tag_ids

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
        if issubclass(SearchOptions, dict):
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
        if not isinstance(other, SearchOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
