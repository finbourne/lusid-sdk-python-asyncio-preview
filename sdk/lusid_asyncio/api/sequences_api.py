# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3704
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid_asyncio.api_client import ApiClient
from lusid_asyncio.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SequencesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_sequence(self, scope, create_sequence_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] CreateSequence: Create a new sequence  # noqa: E501

        Create a new sequence  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_sequence(scope, create_sequence_request, async_req=True)
        >>> result = thread.get()

        :param scope: Scope of the sequence. (required)
        :type scope: str
        :param create_sequence_request: Request to create sequence (required)
        :type create_sequence_request: CreateSequenceRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SequenceDefinition
        """
        kwargs['_return_http_data_only'] = True
        return self.create_sequence_with_http_info(scope, create_sequence_request, **kwargs)  # noqa: E501

    def create_sequence_with_http_info(self, scope, create_sequence_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] CreateSequence: Create a new sequence  # noqa: E501

        Create a new sequence  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_sequence_with_http_info(scope, create_sequence_request, async_req=True)
        >>> result = thread.get()

        :param scope: Scope of the sequence. (required)
        :type scope: str
        :param create_sequence_request: Request to create sequence (required)
        :type create_sequence_request: CreateSequenceRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SequenceDefinition, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'scope',
            'create_sequence_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_sequence" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_sequence_request' is set
        if self.api_client.client_side_validation and ('create_sequence_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_sequence_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_sequence_request` when calling `create_sequence`")  # noqa: E501

        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `create_sequence`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `create_sequence`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `create_sequence`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_sequence_request' in local_var_params:
            body_params = local_var_params['create_sequence_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3704'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501
        
        response_types_map = {
            201: "SequenceDefinition",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/sequences/{scope}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_sequence(self, scope, code, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetSequence: Get a specified sequence  # noqa: E501

        Return the details of a specified sequence  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_sequence(scope, code, async_req=True)
        >>> result = thread.get()

        :param scope: Scope of the sequence. (required)
        :type scope: str
        :param code: Code of the sequence. This together with stated scope uniquely              identifies the sequence. (required)
        :type code: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SequenceDefinition
        """
        kwargs['_return_http_data_only'] = True
        return self.get_sequence_with_http_info(scope, code, **kwargs)  # noqa: E501

    def get_sequence_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetSequence: Get a specified sequence  # noqa: E501

        Return the details of a specified sequence  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_sequence_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param scope: Scope of the sequence. (required)
        :type scope: str
        :param code: Code of the sequence. This together with stated scope uniquely              identifies the sequence. (required)
        :type code: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SequenceDefinition, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'scope',
            'code'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sequence" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_sequence`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_sequence`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_sequence`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('code' in local_var_params and  # noqa: E501
                                                        len(local_var_params['code']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_sequence`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('code' in local_var_params and  # noqa: E501
                                                        len(local_var_params['code']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_sequence`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_sequence`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501
        
        response_types_map = {
            200: "SequenceDefinition",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/sequences/{scope}/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def next(self, scope, code, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Next: Get next values from sequence  # noqa: E501

        Get the next set of values from a specified sequence  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.next(scope, code, async_req=True)
        >>> result = thread.get()

        :param scope: Scope of the sequence. (required)
        :type scope: str
        :param code: Code of the sequence. This together with stated scope uniquely              identifies the sequence. (required)
        :type code: str
        :param batch: Number of sequences items to return for the specified sequence. Default to 1 if not specified.
        :type batch: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NextValueInSequenceResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.next_with_http_info(scope, code, **kwargs)  # noqa: E501

    def next_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Next: Get next values from sequence  # noqa: E501

        Get the next set of values from a specified sequence  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.next_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param scope: Scope of the sequence. (required)
        :type scope: str
        :param code: Code of the sequence. This together with stated scope uniquely              identifies the sequence. (required)
        :type code: str
        :param batch: Number of sequences items to return for the specified sequence. Default to 1 if not specified.
        :type batch: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NextValueInSequenceResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'scope',
            'code',
            'batch'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method next" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `next`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `next`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `next`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('code' in local_var_params and  # noqa: E501
                                                        len(local_var_params['code']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `next`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('code' in local_var_params and  # noqa: E501
                                                        len(local_var_params['code']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `next`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `next`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and 'batch' in local_var_params and local_var_params['batch'] > 5000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `batch` when calling `next`, must be a value less than or equal to `5000`")  # noqa: E501
        if self.api_client.client_side_validation and 'batch' in local_var_params and local_var_params['batch'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `batch` when calling `next`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'batch' in local_var_params and local_var_params['batch'] is not None:  # noqa: E501
            query_params.append(('batch', local_var_params['batch']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501
        
        response_types_map = {
            200: "NextValueInSequenceResponse",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/sequences/{scope}/{code}/next', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
