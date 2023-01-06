# Hyper Precise Location Callbacks

```python
hyper_precise_location_callbacks_controller = client.hyper_precise_location_callbacks
```

## Class Name

`HyperPreciseLocationCallbacksController`

## Methods

* [Deregister Callback](../../doc/controllers/hyper-precise-location-callbacks.md#deregister-callback)
* [List Registered Callbacks](../../doc/controllers/hyper-precise-location-callbacks.md#list-registered-callbacks)
* [Register Callback](../../doc/controllers/hyper-precise-location-callbacks.md#register-callback)


# Deregister Callback

Stops ThingSpace from sending callback messages for the specified account and listener name.

```python
def deregister_callback(self,
                       account_number,
                       name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Query, Required | A unique identifier for a `Account`. |
| `name` | `string` | Query, Required | The name of the callback service that will be deleted |

## Response Type

[`ApiResponseCode`](../../doc/models/api-response-code.md)

## Example Usage

```python
account_number = 'accountNumber2'
name = 'name0'

result = hyper_precise_location_callbacks_controller.deregister_callback(account_number, name)
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


# List Registered Callbacks

Find registered callback listener for account by account number.

```python
def list_registered_callbacks(self,
                             account_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Query, Required | A unique identifier for an account. |

## Response Type

[`List of CallBackCreated`](../../doc/models/call-back-created.md)

## Example Usage

```python
account_number = 'accountNumber2'

result = hyper_precise_location_callbacks_controller.list_registered_callbacks(account_number)
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


# Register Callback

Registers a URL at which an account receives asynchronous responses and other messages from a ThingSpace Platform callback service. The messages are REST messages. You are responsible for creating and running a listening process on your server at that URL to receive and parse the messages.

```python
def register_callback(self,
                     account_number,
                     name,
                     url,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Query, Required | A unique identifier for an account. |
| `name` | `string` | Header, Required | The name to be assigned to the lister service |
| `url` | `string` | Header, Required | The address of the listerner service |
| `body` | [`HyperPreciseLocationCallback`](../../doc/models/hyper-precise-location-callback.md) | Body, Required | - |

## Response Type

[`CallBackCreated`](../../doc/models/call-back-created.md)

## Example Usage

```python
account_number = 'accountNumber2'
name = 'name0'
url = 'url4'
body = HyperPreciseLocationCallback()
body.aname = 'aname0'
body.name = 'name6'
body.url = 'url0'

result = hyper_precise_location_callbacks_controller.register_callback(account_number, name, url, body)
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

