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


class TagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_all_unused_tags(self, **kwargs):  # noqa: E501
        """Delete all unused tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_unused_tags(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_all_unused_tags_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_unused_tags_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_all_unused_tags_with_http_info(self, **kwargs):  # noqa: E501
        """Delete all unused tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_unused_tags_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_unused_tags" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/dataProduct/tags/unused', 'DELETE',
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

    def delete_data_product_tag(self, tag_id, data_product_id, **kwargs):  # noqa: E501
        """Delete a tag from a specific data product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_data_product_tag(tag_id, data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_id: (required)
        :param str data_product_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_data_product_tag_with_http_info(tag_id, data_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_data_product_tag_with_http_info(tag_id, data_product_id, **kwargs)  # noqa: E501
            return data

    def delete_data_product_tag_with_http_info(self, tag_id, data_product_id, **kwargs):  # noqa: E501
        """Delete a tag from a specific data product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_data_product_tag_with_http_info(tag_id, data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_id: (required)
        :param str data_product_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id', 'data_product_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_data_product_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params or
                params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `delete_data_product_tag`")  # noqa: E501
        # verify the required parameter 'data_product_id' is set
        if ('data_product_id' not in params or
                params['data_product_id'] is None):
            raise ValueError("Missing the required parameter `data_product_id` when calling `delete_data_product_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501
        if 'data_product_id' in params:
            path_params['dataProductId'] = params['data_product_id']  # noqa: E501

        query_params = []

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
            '/api/v1/dataProduct/tags/{tagId}/products/{dataProductId}', 'DELETE',
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

    def delete_tag(self, tag_id, **kwargs):  # noqa: E501
        """Delete an unused tag with a specific identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tag(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_tag_with_http_info(tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_tag_with_http_info(tag_id, **kwargs)  # noqa: E501
            return data

    def delete_tag_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """Delete an unused tag with a specific identifier  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tag_with_http_info(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params or
                params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `delete_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501

        query_params = []

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
            '/api/v1/dataProduct/tags/{tagId}', 'DELETE',
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

    def get_data_product_tags(self, data_product_id, **kwargs):  # noqa: E501
        """List all tags associated with a specific data product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_data_product_tags(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :return: list[DataProductTag]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_data_product_tags_with_http_info(data_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_data_product_tags_with_http_info(data_product_id, **kwargs)  # noqa: E501
            return data

    def get_data_product_tags_with_http_info(self, data_product_id, **kwargs):  # noqa: E501
        """List all tags associated with a specific data product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_data_product_tags_with_http_info(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :return: list[DataProductTag]
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
                    " to method get_data_product_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_product_id' is set
        if ('data_product_id' not in params or
                params['data_product_id'] is None):
            raise ValueError("Missing the required parameter `data_product_id` when calling `get_data_product_tags`")  # noqa: E501

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
            '/api/v1/dataProduct/tags/products/{dataProductId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DataProductTag]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_tags(self, **kwargs):  # noqa: E501
        """List all available tags for all data products  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_tags(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DataProductTag]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_tags_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_tags_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_tags_with_http_info(self, **kwargs):  # noqa: E501
        """List all available tags for all data products  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_tags_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DataProductTag]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_tags" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/dataProduct/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DataProductTag]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_data_product_tags(self, data_product_id, **kwargs):  # noqa: E501
        """Replace all tags for a specific data product with the supplied list of new tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_data_product_tags(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :param list[DataProductTagValue] body:
        :return: list[DataProductTag]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_data_product_tags_with_http_info(data_product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_data_product_tags_with_http_info(data_product_id, **kwargs)  # noqa: E501
            return data

    def update_data_product_tags_with_http_info(self, data_product_id, **kwargs):  # noqa: E501
        """Replace all tags for a specific data product with the supplied list of new tags  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_data_product_tags_with_http_info(data_product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_product_id: (required)
        :param list[DataProductTagValue] body:
        :return: list[DataProductTag]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_product_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_data_product_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_product_id' is set
        if ('data_product_id' not in params or
                params['data_product_id'] is None):
            raise ValueError("Missing the required parameter `data_product_id` when calling `update_data_product_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_product_id' in params:
            path_params['dataProductId'] = params['data_product_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/dataProduct/tags/products/{dataProductId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DataProductTag]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_tag(self, tag_id, **kwargs):  # noqa: E501
        """Update a specific tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tag(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_id: (required)
        :param DataProductTagValue body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_tag_with_http_info(tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_tag_with_http_info(tag_id, **kwargs)  # noqa: E501
            return data

    def update_tag_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """Update a specific tag  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tag_with_http_info(tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tag_id: (required)
        :param DataProductTagValue body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params or
                params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `update_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/dataProduct/tags/{tagId}', 'PUT',
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
