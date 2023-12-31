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

class SubjectRoleAssignmentResponse(object):
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
        'role_id': 'int',
        'role_admin': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'role_id': 'roleId',
        'role_admin': 'roleAdmin'
    }

    def __init__(self, id=None, role_id=None, role_admin=None):  # noqa: E501
        """SubjectRoleAssignmentResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._role_id = None
        self._role_admin = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if role_id is not None:
            self.role_id = role_id
        if role_admin is not None:
            self.role_admin = role_admin

    @property
    def id(self):
        """Gets the id of this SubjectRoleAssignmentResponse.  # noqa: E501

        ID of the role assignment  # noqa: E501

        :return: The id of this SubjectRoleAssignmentResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubjectRoleAssignmentResponse.

        ID of the role assignment  # noqa: E501

        :param id: The id of this SubjectRoleAssignmentResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def role_id(self):
        """Gets the role_id of this SubjectRoleAssignmentResponse.  # noqa: E501

        ID of the role assigned to the subject  # noqa: E501

        :return: The role_id of this SubjectRoleAssignmentResponse.  # noqa: E501
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this SubjectRoleAssignmentResponse.

        ID of the role assigned to the subject  # noqa: E501

        :param role_id: The role_id of this SubjectRoleAssignmentResponse.  # noqa: E501
        :type: int
        """

        self._role_id = role_id

    @property
    def role_admin(self):
        """Gets the role_admin of this SubjectRoleAssignmentResponse.  # noqa: E501

        If true the subject has an admin option for the assigned role  # noqa: E501

        :return: The role_admin of this SubjectRoleAssignmentResponse.  # noqa: E501
        :rtype: bool
        """
        return self._role_admin

    @role_admin.setter
    def role_admin(self, role_admin):
        """Sets the role_admin of this SubjectRoleAssignmentResponse.

        If true the subject has an admin option for the assigned role  # noqa: E501

        :param role_admin: The role_admin of this SubjectRoleAssignmentResponse.  # noqa: E501
        :type: bool
        """

        self._role_admin = role_admin

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
        if issubclass(SubjectRoleAssignmentResponse, dict):
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
        if not isinstance(other, SubjectRoleAssignmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
