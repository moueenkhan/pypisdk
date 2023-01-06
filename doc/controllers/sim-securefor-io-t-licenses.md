# SIM Securefor Io T Licenses

```python
sim_securefor_io_t_licenses_controller = client.sim_securefor_io_t_licenses
```

## Class Name

`SIMSecureforIoTLicensesController`

## Methods

* [Assign License to Devices](../../doc/controllers/sim-securefor-io-t-licenses.md#assign-license-to-devices)
* [Unassign License to Devices](../../doc/controllers/sim-securefor-io-t-licenses.md#unassign-license-to-devices)


# Assign License to Devices

This corresponds to the M2M-MC SOAP interface, `ChangeDeviceSkuSubscription`.

```python
def assign_license_to_devices(self,
                             body,
                             x_request_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssignLicenseRequest`](../../doc/models/assign-license-request.md) | Body, Required | Request |
| `x_request_id` | `string` | Header, Optional | Transaction Id<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]-[0-9]{3,32}$` |

## Response Type

[`SecuritySuccessResult`](../../doc/models/security-success-result.md)

## Example Usage

```python
body = AssignLicenseRequest()
body.account_name = '0000123456-00001'
body.devices = []

body.devices.append(LicenseDeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(LicenseDeviceId())
body.devices[0].device_ids[0].id = '864508030109877'
body.devices[0].device_ids[0].kind = 'IMEI'


body.sku_number = 'SIMSec-IoT-Lt'

result = sim_secure_for_io_t_licenses_controller.assign_license_to_devices(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "c3f3d17c-79ff-4b35-82df-94446785b6e0"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 401 | Unauthorized | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 403 | Forbidden | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 404 | Not Found / Does not exist | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 406 | Format / Request Unacceptable | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 429 | Too many requests | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| Default | Error response | [`SecurityResultException`](../../doc/models/security-result-exception.md) |


# Unassign License to Devices

This corresponds to the M2M-MC SOAP interface, `ChangeDeviceSkuSubscription`.

```python
def unassign_license_to_devices(self,
                               x_request_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_request_id` | `string` | Header, Required | Transaction Id<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]-[0-9]{3,32}$` |

## Response Type

[`SecuritySuccessResult`](../../doc/models/security-success-result.md)

## Example Usage

```python
x_request_id = 'X-Request-ID2'

result = sim_secure_for_io_t_licenses_controller.unassign_license_to_devices(x_request_id)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "1f28c944-d007-44c9-9543-003b8820cc69"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 401 | Unauthorized | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 403 | Forbidden | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 404 | Not Found / Does not exist | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 406 | Format / Request Unacceptable | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 429 | Too many requests | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| Default | Error response | [`SecurityResultException`](../../doc/models/security-result-exception.md) |

