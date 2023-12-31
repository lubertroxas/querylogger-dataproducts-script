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


class WorkflowsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_data_product(self, data_product_id, **kwargs):  # noqa: E501
        """Initiate an asynchronous task to delete the data product.  # noqa: E501

        This workflow attempts to delete the data product's schema and its views, or materialized views, from the underlying storage system. If the deletion succeeds the data product metadata is also deleted. This endpoint returns a success response if the async task is accepted by the server. Clients must poll the endpoint returned in the location header in order to follow the status of the async operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_data_product(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :param bool skip_trino_delete: If true, just delete from the data product DB, don't delete any tables or schemas from Trino
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_data_product_with_http_info(data_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_data_product_with_http_info(data_product_id, **kwargs)  # noqa: E501
            return data

    def delete_data_product_with_http_info(self, data_product_id, **kwargs):  # noqa: E501
        """Initiate an asynchronous task to delete the data product.  # noqa: E501

        This workflow attempts to delete the data product's schema and its views, or materialized views, from the underlying storage system. If the deletion succeeds the data product metadata is also deleted. This endpoint returns a success response if the async task is accepted by the server. Clients must poll the endpoint returned in the location header in order to follow the status of the async operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_data_product_with_http_info(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :param bool skip_trino_delete: If true, just delete from the data product DB, don't delete any tables or schemas from Trino
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_product_id', 'skip_trino_delete']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_data_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_product_id' is set
        if ('data_product_id' not in params or
                params['data_product_id'] is None):
            raise ValueError("Missing the required parameter `data_product_id` when calling `delete_data_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_product_id' in params:
            path_params['dataProductId'] = params['data_product_id']  # noqa: E501

        query_params = []
        if 'skip_trino_delete' in params:
            query_params.append(('skipTrinoDelete', params['skip_trino_delete']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/dataProduct/products/{dataProductId}/workflows/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_delete_data_product_status(self, data_product_id, **kwargs):  # noqa: E501
        """Get the status of the async task to delete a data product.  # noqa: E501

        Clients must poll this endpoint until the attribute isFinalStatus in the response body is true.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delete_data_product_status(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :return: DataProductWorkflowState
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_delete_data_product_status_with_http_info(data_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_delete_data_product_status_with_http_info(data_product_id, **kwargs)  # noqa: E501
            return data

    def get_delete_data_product_status_with_http_info(self, data_product_id, **kwargs):  # noqa: E501
        """Get the status of the async task to delete a data product.  # noqa: E501

        Clients must poll this endpoint until the attribute isFinalStatus in the response body is true.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_delete_data_product_status_with_http_info(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :return: DataProductWorkflowState
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_delete_data_product_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_product_id' is set
        if ('data_product_id' not in params or
                params['data_product_id'] is None):
            raise ValueError("Missing the required parameter `data_product_id` when calling `get_delete_data_product_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_product_id' in params:
            path_params['dataProductId'] = params['data_product_id']  # noqa: E501

        query_params = []

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
            '/api/v1/dataProduct/products/{dataProductId}/workflows/delete', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataProductWorkflowState',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_publish_data_product_status(self, data_product_id, **kwargs):  # noqa: E501
        """Get the status of the async task that publishes a data product.  # noqa: E501

        Clients must poll this endpoint until the attribute isFinalStatus in the response body is true.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_publish_data_product_status(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :return: DataProductWorkflowState
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_publish_data_product_status_with_http_info(data_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_publish_data_product_status_with_http_info(data_product_id, **kwargs)  # noqa: E501
            return data

    def get_publish_data_product_status_with_http_info(self, data_product_id, **kwargs):  # noqa: E501
        """Get the status of the async task that publishes a data product.  # noqa: E501

        Clients must poll this endpoint until the attribute isFinalStatus in the response body is true.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_publish_data_product_status_with_http_info(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :return: DataProductWorkflowState
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_publish_data_product_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_product_id' is set
        if ('data_product_id' not in params or
                params['data_product_id'] is None):
            raise ValueError("Missing the required parameter `data_product_id` when calling `get_publish_data_product_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_product_id' in params:
            path_params['dataProductId'] = params['data_product_id']  # noqa: E501

        query_params = []

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
            '/api/v1/dataProduct/products/{dataProductId}/workflows/publish', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataProductWorkflowState',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def publish_data_product(self, data_product_id, **kwargs):  # noqa: E501
        """Publish the data product by initiating an asynchronous task to populate the views, or materialized views, in the schema.  # noqa: E501

        The publish workflow creates the data product as a schema in the data product's catalog using the domain schema location if provided, or the catalog's default schema location. The datasets are created as views or materialized views in that schema, according to their types. If completed successfully, the data product status transitions to PUBLISHED. This endpoint returns a success response if the async task is accepted by the server. Clients must poll the endpoint returned in the location header in order to follow the status of the async operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_data_product(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :param bool force: If true the data product will be republished, even if it is already published, and all its datasets will be recreated
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.publish_data_product_with_http_info(data_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.publish_data_product_with_http_info(data_product_id, **kwargs)  # noqa: E501
            return data

    def publish_data_product_with_http_info(self, data_product_id, **kwargs):  # noqa: E501
        """Publish the data product by initiating an asynchronous task to populate the views, or materialized views, in the schema.  # noqa: E501

        The publish workflow creates the data product as a schema in the data product's catalog using the domain schema location if provided, or the catalog's default schema location. The datasets are created as views or materialized views in that schema, according to their types. If completed successfully, the data product status transitions to PUBLISHED. This endpoint returns a success response if the async task is accepted by the server. Clients must poll the endpoint returned in the location header in order to follow the status of the async operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_data_product_with_http_info(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :param bool force: If true the data product will be republished, even if it is already published, and all its datasets will be recreated
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_product_id', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method publish_data_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_product_id' is set
        if ('data_product_id' not in params or
                params['data_product_id'] is None):
            raise ValueError("Missing the required parameter `data_product_id` when calling `publish_data_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_product_id' in params:
            path_params['dataProductId'] = params['data_product_id']  # noqa: E501

        query_params = []
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/dataProduct/products/{dataProductId}/workflows/publish', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
