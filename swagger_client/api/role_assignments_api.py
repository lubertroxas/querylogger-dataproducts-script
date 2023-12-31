# coding: utf-8

"""
    Starburst Enterprise API documentation

    Documentation with details about endpoints and entities.  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class RoleAssignmentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_role_assignments(self, role_id, **kwargs):  # noqa: E501
        """List assignments of a Starburst built-in access control role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_assignments(role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int role_id: (required)
        :param str page_token: Page token
        :param str page_size: Page size
        :param str page_sort: Sorting order
        :return: PaginatedResultRoleAssignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_role_assignments_with_http_info(role_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_role_assignments_with_http_info(role_id, **kwargs)  # noqa: E501
            return data

    def list_role_assignments_with_http_info(self, role_id, **kwargs):  # noqa: E501
        """List assignments of a Starburst built-in access control role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_role_assignments_with_http_info(role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int role_id: (required)
        :param str page_token: Page token
        :param str page_size: Page size
        :param str page_sort: Sorting order
        :return: PaginatedResultRoleAssignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_id', 'page_token', 'page_size', 'page_sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_role_assignments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_id' is set
        if ('role_id' not in params or
                params['role_id'] is None):
            raise ValueError("Missing the required parameter `role_id` when calling `list_role_assignments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'role_id' in params:
            path_params['roleId'] = params['role_id']  # noqa: E501

        query_params = []
        if 'page_token' in params:
            query_params.append(('pageToken', params['page_token']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page_sort' in params:
            query_params.append(('pageSort', params['page_sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/biac/roles/{roleId}/assignments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedResultRoleAssignmentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
