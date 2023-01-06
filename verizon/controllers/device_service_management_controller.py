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
from verizon.models.bullseye_service_result import BullseyeServiceResult
from verizon.exceptions.hyper_precise_location_result_exception import HyperPreciseLocationResultException


class DeviceServiceManagementController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(DeviceServiceManagementController, self).__init__(config)

    def get_device_hyper_precise_status(self,
                                        imei,
                                        account_number):
        """Does a GET request to /devices/services.

        Gets the list of a status for hyper-precise location devices

        Args:
            imei (string): A unique identifier for a `Device`.
            account_number (string): A unique identifier for a `Account`.

        Returns:
            BullseyeServiceResult: Response from the API. Returns the status
                of Hyper Precise Location on the device.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT10)
            .path('/devices/services')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('imei')
                         .value(imei))
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
            .deserialize_into(BullseyeServiceResult.from_dictionary)
            .local_error('400', 'Bad request.', HyperPreciseLocationResultException)
            .local_error('401', 'Unauthorized request. Access token is missing or invalid.', HyperPreciseLocationResultException)
            .local_error('403', 'Forbidden request.', HyperPreciseLocationResultException)
            .local_error('404', 'Bad request. Not found.', HyperPreciseLocationResultException)
            .local_error('409', 'Bad request. Conflict state.', HyperPreciseLocationResultException)
            .local_error('500', 'Internal Server Error.', HyperPreciseLocationResultException)
        ).execute()

    def update_device_hyper_precise_status(self,
                                           imei,
                                           bullseye_enable,
                                           body=None):
        """Does a PUT request to /devices/services.

        Enable/disable hyper-precise service for a device.

        Args:
            imei (string): International Mobile Equipment Identifier. The
                unique ID of a device.
            bullseye_enable (bool): Set to Enable (true) or Disable (false)
            body (BullseyeServiceRequest, optional): List of devices and
                hyper-precise required statuses.

        Returns:
            BullseyeServiceResult: Response from the API. Successful
                response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT10)
            .path('/devices/services')
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                          .key('imei')
                          .value(imei))
            .header_param(Parameter()
                          .key('BullseyeEnable')
                          .value(bullseye_enable))
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
            .deserialize_into(BullseyeServiceResult.from_dictionary)
            .local_error('400', 'Bad request.', HyperPreciseLocationResultException)
            .local_error('401', 'Unauthorized request. Access token is missing or invalid.', HyperPreciseLocationResultException)
            .local_error('403', 'Forbidden request.', HyperPreciseLocationResultException)
            .local_error('404', 'Bad request. Not found.', HyperPreciseLocationResultException)
            .local_error('409', 'Bad request. Conflict state.', HyperPreciseLocationResultException)
            .local_error('500', 'Internal Server Error.', HyperPreciseLocationResultException)
        ).execute()
