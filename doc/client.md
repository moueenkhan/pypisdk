
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `vz_m2m_token` | `string` | M2M Session Token |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT', 'GET', 'PUT']** |
| `oauth_client_id` | `string` | OAuth 2 Client ID |
| `oauth_client_secret` | `string` | OAuth 2 Client Secret |
| `oauth_token` | `OauthToken` | Object for storing information about the OAuth token |
| `oauth_scopes` | `OauthScopeEnum` |  |

The API client can be initialized as follows:

```python
from verizon.verizon_client import VerizonClient
from verizon.configuration import Environment

client = VerizonClient(
    vz_m2m_token='VZ-M2M-Token',
    oauth_client_id='OAuthClientId',
    oauth_client_secret='OAuthClientSecret',
    oauth_scopes = [OauthScopeEnum.DISCOVERYREAD, OauthScopeEnum.SERVICEPROFILEREAD],
    environment=Environment.PRODUCTION,)
```

## Verizon Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| m_5g_edge_platforms | Gets M5gEdgePlatformsController |
| service_profiles | Gets ServiceProfilesController |
| device_management | Gets DeviceManagementController |
| accounts | Gets AccountsController |
| service_endpoints | Gets ServiceEndpointsController |
| device_groups | Gets DeviceGroupsController |
| sms | Gets SMSController |
| session_management | Gets SessionManagementController |
| connectivity_callbacks | Gets ConnectivityCallbacksController |
| service_plans | Gets ServicePlansController |
| devices_locations | Gets DevicesLocationsController |
| device_location_callbacks | Gets DeviceLocationCallbacksController |
| software_management_subscriptions_v1 | Gets SoftwareManagementSubscriptionsV1Controller |
| firmware_v1 | Gets FirmwareV1Controller |
| software_management_licenses_v1 | Gets SoftwareManagementLicensesV1Controller |
| software_management_callbacks_v1 | Gets SoftwareManagementCallbacksV1Controller |
| software_management_reports_v1 | Gets SoftwareManagementReportsV1Controller |
| exclusions | Gets ExclusionsController |
| account_requests | Gets AccountRequestsController |
| devices_location_subscriptions | Gets DevicesLocationSubscriptionsController |
| software_management_licenses_v2 | Gets SoftwareManagementLicensesV2Controller |
| campaigns_v2 | Gets CampaignsV2Controller |
| software_management_callbacks_v2 | Gets SoftwareManagementCallbacksV2Controller |
| software_management_reports_v2 | Gets SoftwareManagementReportsV2Controller |
| client_logging | Gets ClientLoggingController |
| software_management_reports_v3 | Gets SoftwareManagementReportsV3Controller |
| account_devices | Gets AccountDevicesController |
| software_management_callbacks_v3 | Gets SoftwareManagementCallbacksV3Controller |
| sim_secure_for_io_t_licenses | Gets SIMSecureForIoTLicensesController |
| diagnostics_observations | Gets DiagnosticsObservationsController |
| diagnostics_settings | Gets DiagnosticsSettingsController |
| targets | Gets TargetsController |
| cloud_connector_subscriptions | Gets CloudConnectorSubscriptionsController |
| device_reports | Gets DeviceReportsController |
| mec_sites | Gets MECSitesController |
| service_launch_requests | Gets ServiceLaunchRequestsController |
| service_instances | Gets ServiceInstancesController |
| software_management_licenses_v3 | Gets SoftwareManagementLicensesV3Controller |
| campaigns_v3 | Gets CampaignsV3Controller |
| firmware_v3 | Gets FirmwareV3Controller |
| account_subscriptions | Gets AccountSubscriptionsController |
| diagnostics_subscriptions | Gets DiagnosticsSubscriptionsController |
| diagnostics_callbacks | Gets DiagnosticsCallbacksController |
| device_service_management | Gets DeviceServiceManagementController |
| hyper_precise_location_callbacks | Gets HyperPreciseLocationCallbacksController |
| anomaly_settings | Gets AnomalySettingsController |
| anomaly_triggers | Gets AnomalyTriggersController |
| service_launch_profiles | Gets ServiceLaunchProfilesController |
| service_onboarding | Gets ServiceOnboardingController |
| software_management_subscriptions_v2 | Gets SoftwareManagementSubscriptionsV2Controller |
| software_management_subscriptions_v3 | Gets SoftwareManagementSubscriptionsV3Controller |
| diagnostics_history | Gets DiagnosticsHistoryController |
| server_logging | Gets ServerLoggingController |
| performance_metrics | Gets PerformanceMetricsController |
| service_metadata | Gets ServiceMetadataController |
| csp_profiles | Gets CSPProfilesController |
| service_claims | Gets ServiceClaimsController |
| repositories | Gets RepositoriesController |
| token | Gets TokenController |
| oauth_authorization | Gets OauthAuthorizationController |

