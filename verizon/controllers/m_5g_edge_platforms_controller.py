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
from verizon.models.list_mec_platforms_result import ListMECPlatformsResult
from verizon.models.list_regions_result import ListRegionsResult
from verizon.exceptions.edge_discovery_result_exception import EdgeDiscoveryResultException


class M5gEdgePlatformsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(M5gEdgePlatformsController, self).__init__(config)

    def list_mec_platforms(self,
                           region=None,
                           service_profile_id=None,
                           subscriber_density=None,
                           ue_identity_type=None,
                           ue_identity=None):
        """Does a GET request to /mecplatforms.

        Returns a list of optimal MEC Platforms where you can register your
        deployed application. **Note:** If a query is sent with all of the
        parameters, it will fail with a "400" error. You can search based on
        the following parameter combinations - region plus Service Profile ID
        and subscriber density (density is optional but recommended), region
        plus UEIdentity(Including UEIdentity Type) or Service Profile ID plus
        UEIdentity(Including UEIdentity Type).

        Args:
            region (string, optional): MEC region name. Current valid values
                are US_WEST_2 and US_EAST_1.
            service_profile_id (string, optional): service profile identifier
            subscriber_density (int, optional): Minimum number of 4G/5G
                subscribers per square kilometer.
            ue_identity_type (UserEquipmentIdentityTypeEnum, optional): Type
                of User Equipment identifier used in `UEIdentity`.
            ue_identity (string, optional): The identifier value for User
                Equipment. The type of identifier is defined by the
                'UEIdentityType' parameter. The`IPAddress`format can be IPv4
                or IPv6.

        Returns:
            ListMECPlatformsResult: Response from the API. MEC platforms
                matching query parameters

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/mecplatforms')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('region')
                         .value(region))
            .query_param(Parameter()
                         .key('serviceProfileId')
                         .value(service_profile_id))
            .query_param(Parameter()
                         .key('subscriberDensity')
                         .value(subscriber_density))
            .query_param(Parameter()
                         .key('UEIdentityType')
                         .value(ue_identity_type))
            .query_param(Parameter()
                         .key('UEIdentity')
                         .value(ue_identity))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListMECPlatformsResult.from_dictionary)
            .local_error('400', 'HTTP 400 Bad Request', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized', EdgeDiscoveryResultException)
        ).execute()

    def list_regions(self):
        """Does a GET request to /regions.

        List the geographical regions available, based on the user's bearer
        token. **Note:** Country code, Metropolitan area, Area and Zone are
        future functionality and will currently return a "null" value.

        Returns:
            ListRegionsResult: Response from the API. List of geographical
                regions

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/regions')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListRegionsResult.from_dictionary)
            .local_error('400', 'HTTP 400 Bad Request', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized', EdgeDiscoveryResultException)
        ).execute()
