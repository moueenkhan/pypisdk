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
from verizon.models.diagnostics_subscription import DiagnosticsSubscription
from verizon.exceptions.device_diagnostics_result_exception import DeviceDiagnosticsResultException


class DiagnosticsSubscriptionsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(DiagnosticsSubscriptionsController, self).__init__(config)

    def get_diagnostics_subscription(self,
                                     account_name):
        """Does a GET request to /subscriptions.

        This endpoint retrieves a diagnostics subscription by account

        Args:
            account_name (string): Account identifier

        Returns:
            DiagnosticsSubscription: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT8)
            .path('/subscriptions')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('accountName')
                         .value(account_name))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DiagnosticsSubscription.from_dictionary)
        ).execute()
