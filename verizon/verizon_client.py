# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from verizon.configuration import Configuration
from verizon.controllers.base_controller import BaseController
from verizon.configuration import Environment
from verizon.http.auth.oauth_2 import Oauth2
from verizon.controllers.m_5g_edge_platforms_controller\
    import M5gEdgePlatformsController
from verizon.controllers.service_profiles_controller\
    import ServiceProfilesController
from verizon.controllers.device_management_controller\
    import DeviceManagementController
from verizon.controllers.accounts_controller import AccountsController
from verizon.controllers.service_endpoints_controller\
    import ServiceEndpointsController
from verizon.controllers.device_groups_controller import DeviceGroupsController
from verizon.controllers.sms_controller import SMSController
from verizon.controllers.session_management_controller\
    import SessionManagementController
from verizon.controllers.connectivity_callbacks_controller\
    import ConnectivityCallbacksController
from verizon.controllers.service_plans_controller import ServicePlansController
from verizon.controllers.devices_locations_controller\
    import DevicesLocationsController
from verizon.controllers.device_location_callbacks_controller\
    import DeviceLocationCallbacksController
from verizon.controllers.software_management_subscriptions_v1_controller\
    import SoftwareManagementSubscriptionsV1Controller
from verizon.controllers.firmware_v1_controller import FirmwareV1Controller
from verizon.controllers.software_management_licenses_v1_controller\
    import SoftwareManagementLicensesV1Controller
from verizon.controllers.software_management_callbacks_v1_controller\
    import SoftwareManagementCallbacksV1Controller
from verizon.controllers.software_management_reports_v1_controller\
    import SoftwareManagementReportsV1Controller
from verizon.controllers.exclusions_controller import ExclusionsController
from verizon.controllers.account_requests_controller\
    import AccountRequestsController
from verizon.controllers.devices_location_subscriptions_controller\
    import DevicesLocationSubscriptionsController
from verizon.controllers.software_management_licenses_v2_controller\
    import SoftwareManagementLicensesV2Controller
from verizon.controllers.campaigns_v2_controller import CampaignsV2Controller
from verizon.controllers.software_management_callbacks_v2_controller\
    import SoftwareManagementCallbacksV2Controller
from verizon.controllers.software_management_reports_v2_controller\
    import SoftwareManagementReportsV2Controller
from verizon.controllers.client_logging_controller\
    import ClientLoggingController
from verizon.controllers.software_management_reports_v3_controller\
    import SoftwareManagementReportsV3Controller
from verizon.controllers.account_devices_controller\
    import AccountDevicesController
from verizon.controllers.software_management_callbacks_v3_controller\
    import SoftwareManagementCallbacksV3Controller
from verizon.controllers.sim_secure_for_io_t_licenses_controller\
    import SIMSecureForIoTLicensesController
from verizon.controllers.diagnostics_observations_controller\
    import DiagnosticsObservationsController
from verizon.controllers.diagnostics_settings_controller\
    import DiagnosticsSettingsController
from verizon.controllers.targets_controller import TargetsController
from verizon.controllers.cloud_connector_subscriptions_controller\
    import CloudConnectorSubscriptionsController
from verizon.controllers.device_reports_controller\
    import DeviceReportsController
from verizon.controllers.mec_sites_controller import MECSitesController
from verizon.controllers.service_launch_requests_controller\
    import ServiceLaunchRequestsController
from verizon.controllers.service_instances_controller\
    import ServiceInstancesController
from verizon.controllers.software_management_licenses_v3_controller\
    import SoftwareManagementLicensesV3Controller
from verizon.controllers.campaigns_v3_controller import CampaignsV3Controller
from verizon.controllers.firmware_v3_controller import FirmwareV3Controller
from verizon.controllers.account_subscriptions_controller\
    import AccountSubscriptionsController
from verizon.controllers.diagnostics_subscriptions_controller\
    import DiagnosticsSubscriptionsController
from verizon.controllers.diagnostics_callbacks_controller\
    import DiagnosticsCallbacksController
from verizon.controllers.device_service_management_controller\
    import DeviceServiceManagementController
from verizon.controllers.hyper_precise_location_callbacks_controller\
    import HyperPreciseLocationCallbacksController
from verizon.controllers.anomaly_settings_controller\
    import AnomalySettingsController
from verizon.controllers.anomaly_triggers_controller\
    import AnomalyTriggersController
from verizon.controllers.service_launch_profiles_controller\
    import ServiceLaunchProfilesController
from verizon.controllers.service_onboarding_controller\
    import ServiceOnboardingController
from verizon.controllers.software_management_subscriptions_v2_controller\
    import SoftwareManagementSubscriptionsV2Controller
from verizon.controllers.software_management_subscriptions_v3_controller\
    import SoftwareManagementSubscriptionsV3Controller
from verizon.controllers.diagnostics_history_controller\
    import DiagnosticsHistoryController
from verizon.controllers.server_logging_controller\
    import ServerLoggingController
from verizon.controllers.performance_metrics_controller\
    import PerformanceMetricsController
from verizon.controllers.service_metadata_controller\
    import ServiceMetadataController
from verizon.controllers.csp_profiles_controller import CSPProfilesController
from verizon.controllers.service_claims_controller\
    import ServiceClaimsController
from verizon.controllers.repositories_controller import RepositoriesController
from verizon.controllers.token_controller import TokenController
from verizon.controllers.oauth_authorization_controller\
    import OauthAuthorizationController


class VerizonClient(object):

    @LazyProperty
    def m_5g_edge_platforms(self):
        return M5gEdgePlatformsController(self.global_configuration)

    @LazyProperty
    def service_profiles(self):
        return ServiceProfilesController(self.global_configuration)

    @LazyProperty
    def device_management(self):
        return DeviceManagementController(self.global_configuration)

    @LazyProperty
    def accounts(self):
        return AccountsController(self.global_configuration)

    @LazyProperty
    def service_endpoints(self):
        return ServiceEndpointsController(self.global_configuration)

    @LazyProperty
    def device_groups(self):
        return DeviceGroupsController(self.global_configuration)

    @LazyProperty
    def sms(self):
        return SMSController(self.global_configuration)

    @LazyProperty
    def session_management(self):
        return SessionManagementController(self.global_configuration)

    @LazyProperty
    def connectivity_callbacks(self):
        return ConnectivityCallbacksController(self.global_configuration)

    @LazyProperty
    def service_plans(self):
        return ServicePlansController(self.global_configuration)

    @LazyProperty
    def devices_locations(self):
        return DevicesLocationsController(self.global_configuration)

    @LazyProperty
    def device_location_callbacks(self):
        return DeviceLocationCallbacksController(self.global_configuration)

    @LazyProperty
    def software_management_subscriptions_v1(self):
        return SoftwareManagementSubscriptionsV1Controller(self.global_configuration)

    @LazyProperty
    def firmware_v1(self):
        return FirmwareV1Controller(self.global_configuration)

    @LazyProperty
    def software_management_licenses_v1(self):
        return SoftwareManagementLicensesV1Controller(self.global_configuration)

    @LazyProperty
    def software_management_callbacks_v1(self):
        return SoftwareManagementCallbacksV1Controller(self.global_configuration)

    @LazyProperty
    def software_management_reports_v1(self):
        return SoftwareManagementReportsV1Controller(self.global_configuration)

    @LazyProperty
    def exclusions(self):
        return ExclusionsController(self.global_configuration)

    @LazyProperty
    def account_requests(self):
        return AccountRequestsController(self.global_configuration)

    @LazyProperty
    def devices_location_subscriptions(self):
        return DevicesLocationSubscriptionsController(self.global_configuration)

    @LazyProperty
    def software_management_licenses_v2(self):
        return SoftwareManagementLicensesV2Controller(self.global_configuration)

    @LazyProperty
    def campaigns_v2(self):
        return CampaignsV2Controller(self.global_configuration)

    @LazyProperty
    def software_management_callbacks_v2(self):
        return SoftwareManagementCallbacksV2Controller(self.global_configuration)

    @LazyProperty
    def software_management_reports_v2(self):
        return SoftwareManagementReportsV2Controller(self.global_configuration)

    @LazyProperty
    def client_logging(self):
        return ClientLoggingController(self.global_configuration)

    @LazyProperty
    def software_management_reports_v3(self):
        return SoftwareManagementReportsV3Controller(self.global_configuration)

    @LazyProperty
    def account_devices(self):
        return AccountDevicesController(self.global_configuration)

    @LazyProperty
    def software_management_callbacks_v3(self):
        return SoftwareManagementCallbacksV3Controller(self.global_configuration)

    @LazyProperty
    def sim_secure_for_io_t_licenses(self):
        return SIMSecureForIoTLicensesController(self.global_configuration)

    @LazyProperty
    def diagnostics_observations(self):
        return DiagnosticsObservationsController(self.global_configuration)

    @LazyProperty
    def diagnostics_settings(self):
        return DiagnosticsSettingsController(self.global_configuration)

    @LazyProperty
    def targets(self):
        return TargetsController(self.global_configuration)

    @LazyProperty
    def cloud_connector_subscriptions(self):
        return CloudConnectorSubscriptionsController(self.global_configuration)

    @LazyProperty
    def device_reports(self):
        return DeviceReportsController(self.global_configuration)

    @LazyProperty
    def mec_sites(self):
        return MECSitesController(self.global_configuration)

    @LazyProperty
    def service_launch_requests(self):
        return ServiceLaunchRequestsController(self.global_configuration)

    @LazyProperty
    def service_instances(self):
        return ServiceInstancesController(self.global_configuration)

    @LazyProperty
    def software_management_licenses_v3(self):
        return SoftwareManagementLicensesV3Controller(self.global_configuration)

    @LazyProperty
    def campaigns_v3(self):
        return CampaignsV3Controller(self.global_configuration)

    @LazyProperty
    def firmware_v3(self):
        return FirmwareV3Controller(self.global_configuration)

    @LazyProperty
    def account_subscriptions(self):
        return AccountSubscriptionsController(self.global_configuration)

    @LazyProperty
    def diagnostics_subscriptions(self):
        return DiagnosticsSubscriptionsController(self.global_configuration)

    @LazyProperty
    def diagnostics_callbacks(self):
        return DiagnosticsCallbacksController(self.global_configuration)

    @LazyProperty
    def device_service_management(self):
        return DeviceServiceManagementController(self.global_configuration)

    @LazyProperty
    def hyper_precise_location_callbacks(self):
        return HyperPreciseLocationCallbacksController(self.global_configuration)

    @LazyProperty
    def anomaly_settings(self):
        return AnomalySettingsController(self.global_configuration)

    @LazyProperty
    def anomaly_triggers(self):
        return AnomalyTriggersController(self.global_configuration)

    @LazyProperty
    def service_launch_profiles(self):
        return ServiceLaunchProfilesController(self.global_configuration)

    @LazyProperty
    def service_onboarding(self):
        return ServiceOnboardingController(self.global_configuration)

    @LazyProperty
    def software_management_subscriptions_v2(self):
        return SoftwareManagementSubscriptionsV2Controller(self.global_configuration)

    @LazyProperty
    def software_management_subscriptions_v3(self):
        return SoftwareManagementSubscriptionsV3Controller(self.global_configuration)

    @LazyProperty
    def diagnostics_history(self):
        return DiagnosticsHistoryController(self.global_configuration)

    @LazyProperty
    def server_logging(self):
        return ServerLoggingController(self.global_configuration)

    @LazyProperty
    def performance_metrics(self):
        return PerformanceMetricsController(self.global_configuration)

    @LazyProperty
    def service_metadata(self):
        return ServiceMetadataController(self.global_configuration)

    @LazyProperty
    def csp_profiles(self):
        return CSPProfilesController(self.global_configuration)

    @LazyProperty
    def service_claims(self):
        return ServiceClaimsController(self.global_configuration)

    @LazyProperty
    def repositories(self):
        return RepositoriesController(self.global_configuration)

    @LazyProperty
    def token(self):
        return TokenController(self.global_configuration)

    @LazyProperty
    def oauth_authorization(self):
        return OauthAuthorizationController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT', 'GET', 'PUT'],
                 environment=Environment.PRODUCTION,
                 oauth_client_id='TODO: Replace',
                 oauth_client_secret='TODO: Replace', oauth_token=None,
                 oauth_scopes=None, vz_m2m_token='TODO: Replace', config=None):
        if config is None:
            self.config = Configuration(
                                         http_client_instance=http_client_instance,
                                         override_http_client_configuration=override_http_client_configuration,
                                         http_call_back=http_call_back,
                                         timeout=timeout,
                                         max_retries=max_retries,
                                         backoff_factor=backoff_factor,
                                         retry_statuses=retry_statuses,
                                         retry_methods=retry_methods,
                                         environment=environment,
                                         oauth_client_id=oauth_client_id,
                                         oauth_client_secret=oauth_client_secret,
                                         oauth_token=oauth_token,
                                         oauth_scopes=oauth_scopes,
                                         vz_m2m_token=vz_m2m_token)
        else:
            self.config = config

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())\
            .global_header('VZ-M2M-Token', self.config.vz_m2m_token)

        self.initialize_auth_managers(self.global_configuration)

        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

    def initialize_auth_managers(self, global_config):
        http_client_config = global_config.get_http_client_configuration()
        self.auth_managers = { key: None for key in ['global']}
        self.auth_managers['global'] = Oauth2(http_client_config.oauth_client_id, http_client_config.oauth_client_secret, http_client_config.oauth_token, global_config, http_client_config.oauth_scopes)
        return self.auth_managers
