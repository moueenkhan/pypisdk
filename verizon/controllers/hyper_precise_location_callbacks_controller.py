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
from verizon.models.api_response_code import ApiResponseCode
from verizon.models.call_back_created import CallBackCreated
from verizon.exceptions.hyper_precise_location_result_exception import HyperPreciseLocationResultException


class HyperPreciseLocationCallbacksController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(HyperPreciseLocationCallbacksController, self).__init__(config)

    def deregister_callback(self,
                            account_number,
                            name):
        """Does a DELETE request to /callbacks.

        Stops ThingSpace from sending callback messages for the specified
        account and listener name.

        Args:
            account_number (string): A unique identifier for a `Account`.
            name (string): The name of the callback service that will be
                deleted

        Returns:
            ApiResponseCode: Response from the API. Successful response (no
                content).

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT10)
            .path('/callbacks')
            .http_method(HttpMethodEnum.DELETE)
            .query_param(Parameter()
                         .key('accountNumber')
                         .value(account_number))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ApiResponseCode.from_dictionary)
            .local_error('400', 'Bad request.', HyperPreciseLocationResultException)
            .local_error('401', 'Unauthorized request. Access token is missing or invalid.', HyperPreciseLocationResultException)
            .local_error('403', 'Forbidden request.', HyperPreciseLocationResultException)
            .local_error('404', 'Bad request. Not found.', HyperPreciseLocationResultException)
            .local_error('409', 'Bad request. Conflict state.', HyperPreciseLocationResultException)
            .local_error('500', 'Internal Server Error.', HyperPreciseLocationResultException)
        ).execute()

    def list_registered_callbacks(self,
                                  account_number):
        """Does a GET request to /callbacks.

        Find registered callback listener for account by account number.

        Args:
            account_number (string): A unique identifier for an account.

        Returns:
            list of CallBackCreated: Response from the API. A successful
                response will display the billing account number (`aname`),
                the name of the callback service (`name`) and the address of
                the callback listening service (`url`).

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT10)
            .path('/callbacks')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('accountNumber')
                         .value(account_number))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CallBackCreated.from_dictionary)
            .local_error('400', 'Bad request.', HyperPreciseLocationResultException)
            .local_error('401', 'Unauthorized request. Access token is missing or invalid.', HyperPreciseLocationResultException)
            .local_error('403', 'Forbidden request.', HyperPreciseLocationResultException)
            .local_error('404', 'Bad request. Not found.', HyperPreciseLocationResultException)
            .local_error('409', 'Bad request. Conflict state.', HyperPreciseLocationResultException)
            .local_error('500', 'Internal Server Error.', HyperPreciseLocationResultException)
        ).execute()

    def register_callback(self,
                          account_number,
                          name,
                          url,
                          body):
        """Does a POST request to /callbacks.

        Registers a URL at which an account receives asynchronous responses
        and other messages from a ThingSpace Platform callback service. The
        messages are REST messages. You are responsible for creating and
        running a listening process on your server at that URL to receive and
        parse the messages.

        Args:
            account_number (string): A unique identifier for an account.
            name (string): The name to be assigned to the lister service
            url (string): The address of the listerner service
            body (HyperPreciseLocationCallback): TODO: type description here.

        Returns:
            CallBackCreated: Response from the API. A successful response will
                display the billing account number (`aname`), the name of the
                callback service (`name`) and the address of the callback
                listening service (`url`).

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT10)
            .path('/callbacks')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('accountNumber')
                         .value(account_number))
            .header_param(Parameter()
                          .key('name')
                          .value(name))
            .header_param(Parameter()
                          .key('url')
                          .value(url))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
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
            .deserialize_into(CallBackCreated.from_dictionary)
            .local_error('400', 'Bad request.', HyperPreciseLocationResultException)
            .local_error('401', 'Unauthorized request. Access token is missing or invalid.', HyperPreciseLocationResultException)
            .local_error('403', 'Forbidden request.', HyperPreciseLocationResultException)
            .local_error('404', 'Bad request. Not found.', HyperPreciseLocationResultException)
            .local_error('409', 'Bad request. Conflict state.', HyperPreciseLocationResultException)
            .local_error('500', 'Internal Server Error.', HyperPreciseLocationResultException)
        ).execute()
