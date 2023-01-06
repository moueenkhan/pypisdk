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
from verizon.models.request_result import RequestResult
from verizon.models.sms_messages_query_result import SmsMessagesQueryResult
from verizon.models.connectivity_management_success_result import ConnectivityManagementSuccessResult
from verizon.exceptions.connectivity_management_result_exception import ConnectivityManagementResultException


class SMSController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(SMSController, self).__init__(config)

    def send_sms_to_device(self,
                           body):
        """Does a POST request to /sms.

        The messages are queued on the ThingSpace Platform and sent as soon as
        possible, but they may be delayed due to traffic and routing
        considerations.

        Args:
            body (SMSSendRequest): SMS Request

        Returns:
            RequestResult: Response from the API. Request ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT1)
            .path('/sms')
            .http_method(HttpMethodEnum.POST)
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
            .deserialize_into(RequestResult.from_dictionary)
            .local_error('400', 'Error Response', ConnectivityManagementResultException)
        ).execute()

    def list_devices_sms_messages(self,
                                  aname,
                                  next=None):
        """Does a GET request to /sms/{aname}/history.

        When HTTP status is 202, a URL will be returned in the Location header
        of the form /sms/{aname}/history?next={token}. This URL can be used to
        request the next set of messages.

        Args:
            aname (string): Account name
            next (long|int, optional): Continue the previous query from the
                URL in Location Header

        Returns:
            SmsMessagesQueryResult: Response from the API. Successful
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT1)
            .path('/sms/{aname}/history')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('aname')
                            .value(aname)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('next')
                         .value(next))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SmsMessagesQueryResult.from_dictionary)
            .local_error('400', 'Error Response', ConnectivityManagementResultException)
        ).execute()

    def start_queued_sms_delivery(self,
                                  aname):
        """Does a PUT request to /sms/{aname}/startCallbacks.

        Tells the ThingSpace Platform to start sending mobile-originated SMS
        messages through the EnhancedConnectivityService callback service. SMS
        messages from devices are queued until they are retrieved by your
        application, either by callback or synchronously with GET
        /sms/{accountName}/history.

        Args:
            aname (string): Account name

        Returns:
            ConnectivityManagementSuccessResult: Response from the API.
                Request Success Message

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT1)
            .path('/sms/{aname}/startCallbacks')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('aname')
                            .value(aname)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ConnectivityManagementSuccessResult.from_dictionary)
            .local_error('400', 'Error Response', ConnectivityManagementResultException)
        ).execute()
