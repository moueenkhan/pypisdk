# Diagnostics Callbacks

```python
diagnostics_callbacks_controller = client.diagnostics_callbacks
```

## Class Name

`DiagnosticsCallbacksController`

## Methods

* [Register Diagnostics Callback URL](../../doc/controllers/diagnostics-callbacks.md#register-diagnostics-callback-url)
* [Get Diagnostics Subscription Callback Info](../../doc/controllers/diagnostics-callbacks.md#get-diagnostics-subscription-callback-info)
* [Unregister Diagnostics Callback](../../doc/controllers/diagnostics-callbacks.md#unregister-diagnostics-callback)


# Register Diagnostics Callback URL

This endpoint allows user update the callback HTTPS address of an existing diagnostics subscription

```python
def register_diagnostics_callback_url(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CallbackRegistrationRequest`](../../doc/models/callback-registration-request.md) | Body, Required | Callback Url Registration |

## Response Type

[`DeviceDiagnosticsCallback`](../../doc/models/device-diagnostics-callback.md)

## Example Usage

```python
body = CallbackRegistrationRequest()
body.account_name = 'TestQAAccount'
body.service_name = 'Diagnostics'
body.endpoint = 'https://yourwebsite.com'
body.http_headers = jsonpickle.decode('{}')

result = diagnostics_callbacks_controller.register_diagnostics_callback_url(body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "TestQAAccount",
  "serviceName": "string",
  "endpoint": "https://yourwebsite.com",
  "httpHeaders": {},
  "createdOn": "2019-09-07T23:57:53.292Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |


# Get Diagnostics Subscription Callback Info

This endpoint allows user to get the registered callback information of an existing diagnostics subscription

```python
def get_diagnostics_subscription_callback_info(self,
                                              account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Query, Required | Account identifier |

## Response Type

[`List of DeviceDiagnosticsCallback`](../../doc/models/device-diagnostics-callback.md)

## Example Usage

```python
account_name = '0000123456-00001'

result = diagnostics_callbacks_controller.get_diagnostics_subscription_callback_info(account_name)
```

## Example Response *(as JSON)*

```json
[
  {
    "accountName": "TestQAAccount",
    "serviceName": "string",
    "endpoint": "https://yourwebsite.com",
    "httpHeaders": {},
    "createdOn": "2019-09-07T23:57:53.292Z"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |


# Unregister Diagnostics Callback

This endpoint allows user to delete a registered callback Url and credential.

```python
def unregister_diagnostics_callback(self,
                                   account_name,
                                   service_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Query, Required | Account identifier |
| `service_name` | `string` | Query, Required | Service name for Callback Notification |

## Response Type

[`DeviceDiagnosticsCallback`](../../doc/models/device-diagnostics-callback.md)

## Example Usage

```python
account_name = '0000123456-00001'
service_name = 'string'

result = diagnostics_callbacks_controller.unregister_diagnostics_callback(account_name, service_name)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "TestQAAccount",
  "serviceName": "string",
  "endpoint": "https://yourwebsite.com",
  "httpHeaders": {},
  "createdOn": "2019-09-07T23:57:53.292Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |

