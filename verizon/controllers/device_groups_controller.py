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
from verizon.models.connectivity_management_success_result import ConnectivityManagementSuccessResult
from verizon.models.device_group import DeviceGroup
from verizon.models.device_group_devices_data import DeviceGroupDevicesData
from verizon.exceptions.connectivity_management_result_exception import ConnectivityManagementResultException


class DeviceGroupsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(DeviceGroupsController, self).__init__(config)

    def create_device_group(self,
                            body):
        """Does a POST request to /groups.

        Create a new device group and optionally add devices to the group.
        Device groups can make it easier to manage similar devices and to get
        reports on their usage.

        Args:
            body (CreateDevGroupRequest): Request

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
            .path('/groups')
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
            .deserialize_into(ConnectivityManagementSuccessResult.from_dictionary)
            .local_error('400', 'Error Response', ConnectivityManagementResultException)
        ).execute()

    def list_device_groups(self,
                           aname):
        """Does a GET request to /groups/{aname}.

        Returns a list of all device groups in a specified account.

        Args:
            aname (string): Account name

        Returns:
            list of DeviceGroup: Response from the API. The list of device
                groups in the account.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT1)
            .path('/groups/{aname}')
            .http_method(HttpMethodEnum.GET)
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
            .deserialize_into(DeviceGroup.from_dictionary)
            .local_error('400', 'Error Response', ConnectivityManagementResultException)
        ).execute()

    def delete_device_group(self,
                            aname,
                            gname):
        """Does a DELETE request to /groups/{aname}/name/{gname}.

        Deletes a device group from the account. Devices in the group are
        moved to the default device group and are not deleted from the
        account.

        Args:
            aname (string): Account name
            gname (string): Group name

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
            .path('/groups/{aname}/name/{gname}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('aname')
                            .value(aname)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('gname')
                            .value(gname)
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

    def get_device_group_information(self,
                                     aname,
                                     gname,
                                     next=None):
        """Does a GET request to /groups/{aname}/name/{gname}.

        When HTTP status is 202, a URL will be returned in the Location header
        of the form /groups/{aname}/name/{gname}/?next={token}. This URL can
        be used to request the next set of groups.

        Args:
            aname (string): Account name
            gname (string): Group name
            next (long|int, optional): Continue the previous query from the
                pageUrl pagetoken

        Returns:
            DeviceGroupDevicesData: Response from the API. Successful
                response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT1)
            .path('/groups/{aname}/name/{gname}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('aname')
                            .value(aname)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('gname')
                            .value(gname)
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
            .deserialize_into(DeviceGroupDevicesData.from_dictionary)
            .local_error('400', 'Error Response', ConnectivityManagementResultException)
        ).execute()

    def update_device_group(self,
                            aname,
                            gname,
                            body):
        """Does a PUT request to /groups/{aname}/name/{gname}.

        Make changes to a device group, including changing the name and
        description, and adding or removing devices.

        Args:
            aname (string): Account name
            gname (string): Group name
            body (GroupUpdateRequest): Request

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
            .path('/groups/{aname}/name/{gname}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('aname')
                            .value(aname)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('gname')
                            .value(gname)
                            .should_encode(True))
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
            .deserialize_into(ConnectivityManagementSuccessResult.from_dictionary)
            .local_error('400', 'Error Response', ConnectivityManagementResultException)
        ).execute()
