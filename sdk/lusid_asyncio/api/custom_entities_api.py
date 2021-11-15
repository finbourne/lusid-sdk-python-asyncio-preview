# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3720
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


class CustomEntitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_custom_entity(self, entity_type, identifier_type, identifier_value, identifier_scope, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetCustomEntity: Get CustomEntity  # noqa: E501

        Retrieve a CustomEntity by a specific Id at a point in AsAt time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_custom_entity(entity_type, identifier_type, identifier_value, identifier_scope, async_req=True)
        >>> result = thread.get()

        :param entity_type: The type of entity to retrieve. This is included in the response from M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.CreateCustomEntityDefinition(Finbourne.WebApi.Interface.Dto.CustomEntityDefinitions.CustomEntityDefinitionRequest). (required)
        :type entity_type: str
        :param identifier_type: An identifier type attached to the CustomEntity. (required)
        :type identifier_type: str
        :param identifier_value: The identifier value. (required)
        :type identifier_value: str
        :param identifier_scope: The identifier scope. (required)
        :type identifier_scope: str
        :param as_at: The AsAt at which to retrieve the CustomEntity.
        :type as_at: datetime
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
        :rtype: CustomEntityResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_custom_entity_with_http_info(entity_type, identifier_type, identifier_value, identifier_scope, **kwargs)  # noqa: E501

    def get_custom_entity_with_http_info(self, entity_type, identifier_type, identifier_value, identifier_scope, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetCustomEntity: Get CustomEntity  # noqa: E501

        Retrieve a CustomEntity by a specific Id at a point in AsAt time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_custom_entity_with_http_info(entity_type, identifier_type, identifier_value, identifier_scope, async_req=True)
        >>> result = thread.get()

        :param entity_type: The type of entity to retrieve. This is included in the response from M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.CreateCustomEntityDefinition(Finbourne.WebApi.Interface.Dto.CustomEntityDefinitions.CustomEntityDefinitionRequest). (required)
        :type entity_type: str
        :param identifier_type: An identifier type attached to the CustomEntity. (required)
        :type identifier_type: str
        :param identifier_value: The identifier value. (required)
        :type identifier_value: str
        :param identifier_scope: The identifier scope. (required)
        :type identifier_scope: str
        :param as_at: The AsAt at which to retrieve the CustomEntity.
        :type as_at: datetime
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
        :rtype: tuple(CustomEntityResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'entity_type',
            'identifier_type',
            'identifier_value',
            'identifier_scope',
            'as_at'
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
                    " to method get_custom_entity" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'entity_type' is set
        if self.api_client.client_side_validation and ('entity_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['entity_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `entity_type` when calling `get_custom_entity`")  # noqa: E501
        # verify the required parameter 'identifier_type' is set
        if self.api_client.client_side_validation and ('identifier_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['identifier_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `identifier_type` when calling `get_custom_entity`")  # noqa: E501
        # verify the required parameter 'identifier_value' is set
        if self.api_client.client_side_validation and ('identifier_value' not in local_var_params or  # noqa: E501
                                                        local_var_params['identifier_value'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `identifier_value` when calling `get_custom_entity`")  # noqa: E501
        # verify the required parameter 'identifier_scope' is set
        if self.api_client.client_side_validation and ('identifier_scope' not in local_var_params or  # noqa: E501
                                                        local_var_params['identifier_scope'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `identifier_scope` when calling `get_custom_entity`")  # noqa: E501

        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `get_custom_entity`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `get_custom_entity`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('identifier_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['identifier_type']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `identifier_type` when calling `get_custom_entity`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('identifier_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['identifier_type']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `identifier_type` when calling `get_custom_entity`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'identifier_type' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['identifier_type']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `identifier_type` when calling `get_custom_entity`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('identifier_value' in local_var_params and  # noqa: E501
                                                        len(local_var_params['identifier_value']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `identifier_value` when calling `get_custom_entity`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('identifier_value' in local_var_params and  # noqa: E501
                                                        len(local_var_params['identifier_value']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `identifier_value` when calling `get_custom_entity`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'identifier_value' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['identifier_value']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `identifier_value` when calling `get_custom_entity`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('identifier_scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['identifier_scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `identifier_scope` when calling `get_custom_entity`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('identifier_scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['identifier_scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `identifier_scope` when calling `get_custom_entity`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'identifier_scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['identifier_scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `identifier_scope` when calling `get_custom_entity`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'entity_type' in local_var_params:
            path_params['entityType'] = local_var_params['entity_type']  # noqa: E501
        if 'identifier_type' in local_var_params:
            path_params['identifierType'] = local_var_params['identifier_type']  # noqa: E501
        if 'identifier_value' in local_var_params:
            path_params['identifierValue'] = local_var_params['identifier_value']  # noqa: E501

        query_params = []
        if 'identifier_scope' in local_var_params and local_var_params['identifier_scope'] is not None:  # noqa: E501
            query_params.append(('identifierScope', local_var_params['identifier_scope']))  # noqa: E501
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

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
            200: "CustomEntityResponse",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/customentities/{entityType}/{identifierType}/{identifierValue}', 'GET',
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

    def list_custom_entities(self, entity_type, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListCustomEntities: List Custom Entities  # noqa: E501

        List all the Custom Entities matching particular criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_custom_entities(entity_type, async_req=True)
        >>> result = thread.get()

        :param entity_type: The type of entity to list. (required)
        :type entity_type: str
        :param effective_at: The effective datetime or cut label at which to list the entities. Defaults to the current LUSID              system datetime if not specified.
        :type effective_at: str
        :param as_at: The asAt datetime at which to list the entities. Defaults to returning the latest version              of each portfolio if not specified.
        :type as_at: datetime
        :param limit: When paginating, limit the results to this number. Defaults to 100 if not specified.
        :type limit: int
        :param filter: Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914.
        :type filter: str
        :param page: The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request.
        :type page: str
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
        :rtype: PagedResourceListOfCustomEntityResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.list_custom_entities_with_http_info(entity_type, **kwargs)  # noqa: E501

    def list_custom_entities_with_http_info(self, entity_type, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListCustomEntities: List Custom Entities  # noqa: E501

        List all the Custom Entities matching particular criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_custom_entities_with_http_info(entity_type, async_req=True)
        >>> result = thread.get()

        :param entity_type: The type of entity to list. (required)
        :type entity_type: str
        :param effective_at: The effective datetime or cut label at which to list the entities. Defaults to the current LUSID              system datetime if not specified.
        :type effective_at: str
        :param as_at: The asAt datetime at which to list the entities. Defaults to returning the latest version              of each portfolio if not specified.
        :type as_at: datetime
        :param limit: When paginating, limit the results to this number. Defaults to 100 if not specified.
        :type limit: int
        :param filter: Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914.
        :type filter: str
        :param page: The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request.
        :type page: str
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
        :rtype: tuple(PagedResourceListOfCustomEntityResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'entity_type',
            'effective_at',
            'as_at',
            'limit',
            'filter',
            'page'
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
                    " to method list_custom_entities" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'entity_type' is set
        if self.api_client.client_side_validation and ('entity_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['entity_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `entity_type` when calling `list_custom_entities`")  # noqa: E501

        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `list_custom_entities`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `list_custom_entities`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 5000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_custom_entities`, must be a value less than or equal to `5000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_custom_entities`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'entity_type' in local_var_params:
            path_params['entityType'] = local_var_params['entity_type']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params and local_var_params['effective_at'] is not None:  # noqa: E501
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

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
            200: "PagedResourceListOfCustomEntityResponse",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/customentities/{entityType}', 'GET',
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

    def upsert_custom_entity(self, entity_type, custom_entity_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] UpsertCustomEntity: Upsert a new CustomEntity  # noqa: E501

        Insert the custom entity if it does not exist or update the custom entity with the supplied state if it does exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upsert_custom_entity(entity_type, custom_entity_request, async_req=True)
        >>> result = thread.get()

        :param entity_type: The type of the CustomEntity to be created. An entityType can be created using the M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.GetDefinition(System.String,System.Nullable{System.DateTimeOffset}) endpoint. (required)
        :type entity_type: str
        :param custom_entity_request: The CustomEntity to be created. (required)
        :type custom_entity_request: CustomEntityRequest
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
        :rtype: CustomEntityResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.upsert_custom_entity_with_http_info(entity_type, custom_entity_request, **kwargs)  # noqa: E501

    def upsert_custom_entity_with_http_info(self, entity_type, custom_entity_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] UpsertCustomEntity: Upsert a new CustomEntity  # noqa: E501

        Insert the custom entity if it does not exist or update the custom entity with the supplied state if it does exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upsert_custom_entity_with_http_info(entity_type, custom_entity_request, async_req=True)
        >>> result = thread.get()

        :param entity_type: The type of the CustomEntity to be created. An entityType can be created using the M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.GetDefinition(System.String,System.Nullable{System.DateTimeOffset}) endpoint. (required)
        :type entity_type: str
        :param custom_entity_request: The CustomEntity to be created. (required)
        :type custom_entity_request: CustomEntityRequest
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
        :rtype: tuple(CustomEntityResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'entity_type',
            'custom_entity_request'
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
                    " to method upsert_custom_entity" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'entity_type' is set
        if self.api_client.client_side_validation and ('entity_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['entity_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `entity_type` when calling `upsert_custom_entity`")  # noqa: E501
        # verify the required parameter 'custom_entity_request' is set
        if self.api_client.client_side_validation and ('custom_entity_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['custom_entity_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `custom_entity_request` when calling `upsert_custom_entity`")  # noqa: E501

        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `upsert_custom_entity`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `upsert_custom_entity`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'entity_type' in local_var_params:
            path_params['entityType'] = local_var_params['entity_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'custom_entity_request' in local_var_params:
            body_params = local_var_params['custom_entity_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3720'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501
        
        response_types_map = {
            200: "CustomEntityResponse",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/customentities/{entityType}', 'POST',
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
