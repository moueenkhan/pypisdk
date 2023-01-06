# Device Reports

```python
device_reports_controller = client.device_reports
```

## Class Name

`DeviceReportsController`

## Methods

* [Get Sessions Report](../../doc/controllers/device-reports.md#get-sessions-report)
* [Calculate Aggregated Report Synchronous](../../doc/controllers/device-reports.md#calculate-aggregated-report-synchronous)
* [Calculate Aggregated Report Asynchronous](../../doc/controllers/device-reports.md#calculate-aggregated-report-asynchronous)


# Get Sessions Report

Detailed report of session duration and number of bytes transferred per day.

```python
def get_sessions_report(self,
                       account_number,
                       imei,
                       body,
                       start_date=None,
                       end_date=None,
                       duration_low=None,
                       duration_high=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Header, Required | The unique identifier for the account |
| `imei` | `string` | Header, Required | International Mobile Device Identifier. The unique identifier of the device. |
| `body` | [`SessionReportRequest`](../../doc/models/session-report-request.md) | Body, Required | Session report request example |
| `start_date` | `string` | Header, Optional | Start date of session to include. If not specified information will be shown from the earliest available (180 days). ISO 8601 format. |
| `end_date` | `string` | Header, Optional | End date of session to include. If not specified information will be shown to the latest available. ISO 8601 format. |
| `duration_low` | `int` | Header, Optional | The Low value of session duration. |
| `duration_high` | `int` | Header, Optional | The High value of session duration. |

## Response Type

[`SessionLevel`](../../doc/models/session-level.md)

## Example Usage

```python
account_number = 'accountNumber2'
imei = 'imei6'
body = SessionReportRequest()
body.account_number = 'accountNumber6'
body.imei = 'imei0'

result = device_reports_controller.get_sessions_report(account_number, imei, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 403 | Forbidden request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 404 | Bad request. Not found. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 409 | Bad request. Conflict state. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 500 | Internal Server Error. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |


# Calculate Aggregated Report Synchronous

Calculate aggregated report per day with number of sessions and usage information. User will receive synchronous response for specified list of devices (Max 10) and date range (Max 180 days).

```python
def calculate_aggregated_report_synchronous(self,
                                           account_number,
                                           imei,
                                           body,
                                           start_date=None,
                                           end_date=None,
                                           device_group=None,
                                           data_plan=None,
                                           no_session_flag=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Header, Required | The unique identifier for the account |
| `imei` | `string` | Header, Required | Number of devices returning usage info. Could be 0, 1 or more. If 0 the query will return all devices belonging to customer. |
| `body` | [`AggregateSessionReportRequest`](../../doc/models/aggregate-session-report-request.md) | Body, Required | Aggregated report request example |
| `start_date` | `string` | Header, Optional | Start date of session to include. If not specified information will be shown from the earliest available (180 days). ISO 8601 format. |
| `end_date` | `string` | Header, Optional | End date of session to include. If not specified information will be shown to the latest available. ISO 8601 format. |
| `device_group` | `string` | Header, Optional | User defined group name the devices are a member of. |
| `data_plan` | `string` | Header, Optional | The data plan the devices beign queried belong to. |
| `no_session_flag` | `string` | Header, Optional | filters on devices which return only "no sessions". |

## Response Type

[`TotalLevel`](../../doc/models/total-level.md)

## Example Usage

```python
account_number = 'accountNumber2'
imei = 'imei6'
body = AggregateSessionReportRequest()
body.account_number = 'accountNumber6'
body.imei = 'imei0'

result = device_reports_controller.calculate_aggregated_report_synchronous(account_number, imei, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 403 | Forbidden request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 404 | Bad request. Not found. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 409 | Bad request. Conflict state. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 500 | Internal Server Error. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |


# Calculate Aggregated Report Asynchronous

Calculate aggregated report per day with number of sessions and usage information. User will receive an asynchronous callback for the specified list of devices (Max 10000) and date range (Max 180 days).

```python
def calculate_aggregated_report_asynchronous(self,
                                            x_portal_initiated,
                                            account_number,
                                            imei,
                                            body,
                                            start_date=None,
                                            end_date=None,
                                            device_group=None,
                                            data_plan=None,
                                            no_session_flag=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_portal_initiated` | `bool` | Header, Required | A flag for using a listener. Set to true or false. |
| `account_number` | `string` | Header, Required | The unique identifier for the account |
| `imei` | `string` | Header, Required | Number of devices returning usage info. Could be 0, 1 or more. If 0 the query will return all devices belonging to customer. |
| `body` | [`AggregateSessionReportRequest`](../../doc/models/aggregate-session-report-request.md) | Body, Required | Aggregated report request example |
| `start_date` | `string` | Header, Optional | Start date of session to include. If not specified information will be shown from the earliest available (180 days). ISO 8601 format. |
| `end_date` | `string` | Header, Optional | End date of session to include. If not specified information will be shown to the latest available. ISO 8601 format. |
| `device_group` | `string` | Header, Optional | User defined group name the devices are a member of. |
| `data_plan` | `string` | Header, Optional | The data plan the devices beign queried belong to. |
| `no_session_flag` | `string` | Header, Optional | filters on devices which return only "no sessions". |

## Response Type

[`AggregatedReportCallbackResult`](../../doc/models/aggregated-report-callback-result.md)

## Example Usage

```python
x_portal_initiated = False
account_number = 'accountNumber2'
imei = 'imei6'
body = AggregateSessionReportRequest()
body.account_number = 'accountNumber6'
body.imei = 'imei0'

result = device_reports_controller.calculate_aggregated_report_asynchronous(x_portal_initiated, account_number, imei, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 403 | Forbidden request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 404 | Bad request. Not found. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 409 | Bad request. Conflict state. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 500 | Internal Server Error. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |

