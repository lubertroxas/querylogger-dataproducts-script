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

class DataProductWorkflowState(object):
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
        'workflow_type': 'str',
        'status': 'str',
        'errors': 'list[Error]',
        'is_final_status': 'bool'
    }

    attribute_map = {
        'workflow_type': 'workflowType',
        'status': 'status',
        'errors': 'errors',
        'is_final_status': 'isFinalStatus'
    }

    def __init__(self, workflow_type=None, status=None, errors=None, is_final_status=None):  # noqa: E501
        """DataProductWorkflowState - a model defined in Swagger"""  # noqa: E501
        self._workflow_type = None
        self._status = None
        self._errors = None
        self._is_final_status = None
        self.discriminator = None
        if workflow_type is not None:
            self.workflow_type = workflow_type
        if status is not None:
            self.status = status
        if errors is not None:
            self.errors = errors
        if is_final_status is not None:
            self.is_final_status = is_final_status

    @property
    def workflow_type(self):
        """Gets the workflow_type of this DataProductWorkflowState.  # noqa: E501

        Type of the workflow being checked  # noqa: E501

        :return: The workflow_type of this DataProductWorkflowState.  # noqa: E501
        :rtype: str
        """
        return self._workflow_type

    @workflow_type.setter
    def workflow_type(self, workflow_type):
        """Sets the workflow_type of this DataProductWorkflowState.

        Type of the workflow being checked  # noqa: E501

        :param workflow_type: The workflow_type of this DataProductWorkflowState.  # noqa: E501
        :type: str
        """
        allowed_values = ["DELETE", "PUBLISH", "REFRESH_MATERIALIZED_VIEW"]  # noqa: E501
        if workflow_type not in allowed_values:
            raise ValueError(
                "Invalid value for `workflow_type` ({0}), must be one of {1}"  # noqa: E501
                .format(workflow_type, allowed_values)
            )

        self._workflow_type = workflow_type

    @property
    def status(self):
        """Gets the status of this DataProductWorkflowState.  # noqa: E501

        Current status of the workflow execution  # noqa: E501

        :return: The status of this DataProductWorkflowState.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataProductWorkflowState.

        Current status of the workflow execution  # noqa: E501

        :param status: The status of this DataProductWorkflowState.  # noqa: E501
        :type: str
        """
        allowed_values = ["SCHEDULED", "IN_PROGRESS", "COMPLETED", "ERROR"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def errors(self):
        """Gets the errors of this DataProductWorkflowState.  # noqa: E501

        List of errors, if any, related to the workflow execution  # noqa: E501

        :return: The errors of this DataProductWorkflowState.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this DataProductWorkflowState.

        List of errors, if any, related to the workflow execution  # noqa: E501

        :param errors: The errors of this DataProductWorkflowState.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def is_final_status(self):
        """Gets the is_final_status of this DataProductWorkflowState.  # noqa: E501

        Whether the workflow task reached a final status or not  # noqa: E501

        :return: The is_final_status of this DataProductWorkflowState.  # noqa: E501
        :rtype: bool
        """
        return self._is_final_status

    @is_final_status.setter
    def is_final_status(self, is_final_status):
        """Sets the is_final_status of this DataProductWorkflowState.

        Whether the workflow task reached a final status or not  # noqa: E501

        :param is_final_status: The is_final_status of this DataProductWorkflowState.  # noqa: E501
        :type: bool
        """

        self._is_final_status = is_final_status

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
        if issubclass(DataProductWorkflowState, dict):
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
        if not isinstance(other, DataProductWorkflowState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
