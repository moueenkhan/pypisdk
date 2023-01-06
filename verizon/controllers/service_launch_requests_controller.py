# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from verizon.api_helper import APIHelper
from verizon.configuration import Server
from verizon.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from verizon.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from verizon.models.service_launch_request_result import ServiceLaunchRequestResult
from verizon.models.get_service_launch_request import GetServiceLaunchRequest
from verizon.exceptions.edge_service_launch_result_exception import EdgeServiceLaunchResultException


class ServiceLaunchRequestsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(ServiceLaunchRequestsController, self).__init__(config)

    def create_service_launch_request(self,
                                      account_name,
                                      user_name,
                                      correlation_id=None,
                                      body=None):
        """Does a POST request to /v1/service/launch/request.

        Create servicelaunch request

        Args:
            account_name (string): User account name.
            user_name (string): TODO: type description here.
            correlation_id (string, optional): TODO: type description here.
            body (CreateServiceLaunchRequest, optional): TODO: type
                description here.

        Returns:
            ServiceLaunchRequestResult: Response from the API. Service request
                created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT11)
            .path('/v1/service/launch/request')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .header_param(Parameter()
                          .key('userName')
                          .value(user_name))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceLaunchRequestResult.from_dictionary)
            .local_error('400', 'HTTP 400 Bad Request', EdgeServiceLaunchResultException)
            .local_error('401', 'HTTP 401 Unauthorized', EdgeServiceLaunchResultException)
            .local_error('404', 'HTTP 404 Not found', EdgeServiceLaunchResultException)
            .local_error('500', 'Internal Server Error', EdgeServiceLaunchResultException)
        ).execute()

    def get_service_launch_request(self,
                                   account_name,
                                   user_name,
                                   id=None,
                                   correlation_id=None,
                                   name=None,
                                   offset=None,
                                   limit=None):
        """Does a GET request to /v1/service/launch/request.

        Get service launch request

        Args:
            account_name (string): User account name.
            user_name (string): TODO: type description here.
            id (uuid|string, optional): Service Launch Request Id.
            correlation_id (string, optional): TODO: type description here.
            name (string, optional): Service request name.
            offset (long|int, optional): TODO: type description here.
            limit (long|int, optional): TODO: type description here.

        Returns:
            GetServiceLaunchRequest: Response from the API. Get service launch
                request

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT11)
            .path('/v1/service/launch/request')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .header_param(Parameter()
                          .key('userName')
                          .value(user_name))
            .query_param(Parameter()
                         .key('id')
                         .value(id))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .query_param(Parameter()
                         .key('offset')
                         .value(offset))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetServiceLaunchRequest.from_dictionary)
            .local_error('400', 'Bad Request', EdgeServiceLaunchResultException)
            .local_error('401', 'Unauthorized', EdgeServiceLaunchResultException)
            .local_error('403', 'Forbidden', EdgeServiceLaunchResultException)
            .local_error('404', 'Not found', EdgeServiceLaunchResultException)
            .local_error('415', 'Unsupported media type', EdgeServiceLaunchResultException)
            .local_error('429', 'Too many requests', EdgeServiceLaunchResultException)
            .local_error('500', 'Internal Server Error', EdgeServiceLaunchResultException)
        ).execute()

    def submit_service_launch_request(self,
                                      id,
                                      account_name,
                                      user_name,
                                      correlation_id=None):
        """Does a PUT request to /v1/service/launch/request/{id}/submit.

        This endpoint allows the user to submit a service request that
        describes the resource requirements of a service. This API submit an
        object of the service request and moves it to STATE from “DRAFT”  to
        “INSTANTIATED” and triggers the launch flow.

        Args:
            id (uuid|string): A unique Id assigned to the request by system
                calling API.
            account_name (string): User account name.
            user_name (string): TODO: type description here.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            ServiceLaunchRequestResult: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT11)
            .path('/v1/service/launch/request/{id}/submit')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .header_param(Parameter()
                          .key('userName')
                          .value(user_name))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceLaunchRequestResult.from_dictionary)
            .local_error('400', 'HTTP 400 Bad Request', EdgeServiceLaunchResultException)
            .local_error('401', 'HTTP 401 Unauthorized', EdgeServiceLaunchResultException)
            .local_error('412', 'Precondition Failed', EdgeServiceLaunchResultException)
            .local_error('500', 'Internal Server Error', EdgeServiceLaunchResultException)
        ).execute()
