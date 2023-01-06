# Diagnostics Observations

```python
diagnostics_observations_controller = client.diagnostics_observations
```

## Class Name

`DiagnosticsObservationsController`

## Methods

* [Start Diagnostics Observation](../../doc/controllers/diagnostics-observations.md#start-diagnostics-observation)
* [Stop Diagnostics Observation](../../doc/controllers/diagnostics-observations.md#stop-diagnostics-observation)


# Start Diagnostics Observation

This endpoint allows the user to start or change observe diagnostics

```python
def start_diagnostics_observation(self,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ObservationRequest`](../../doc/models/observation-request.md) | Body, Required | Device Observe information |

## Response Type

[`StartDiagnosticsObservationResult`](../../doc/models/start-diagnostics-observation-result.md)

## Example Usage

```python
body = ObservationRequest()
body.account_name = 'TestQAAccount'
body.devices = []

body.devices.append(Device())
body.devices[0].id = '864508030026238'
body.devices[0].kind = 'IMEI'

body.attributes = []

body.attributes.append(ObservationRequestAttribute())
body.attributes[0].name = AttributeIdentifierEnum.RADIO_SIGNAL_STRENGTH

body.attributes.append(ObservationRequestAttribute())
body.attributes[1].name = AttributeIdentifierEnum.LINK_QUALITY

body.attributes.append(ObservationRequestAttribute())
body.attributes[2].name = AttributeIdentifierEnum.NETWORK_BEARER

body.attributes.append(ObservationRequestAttribute())
body.attributes[3].name = AttributeIdentifierEnum.CELL_ID

body.frequency = NumericalData()
body.frequency.value = 15
body.frequency.unit = NumericalDataUnitEnum.SECOND
body.duration = NumericalData()
body.duration.value = 15
body.duration.unit = NumericalDataUnitEnum.SECOND

result = diagnostics_observations_controller.start_diagnostics_observation(body)
```

## Example Response *(as JSON)*

```json
{
  "createdOn": "2019-09-10T19:05:33.33Z",
  "transactionID": "9c7bb124-11f5-4ff3-8a88-0eec1ba99205",
  "status": "CANCEL_OBSERVE_PENDING"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |


# Stop Diagnostics Observation

This endpoint allows the user to stop or reset observe diagnostics

```python
def stop_diagnostics_observation(self,
                                transaction_id,
                                account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `string` | Query, Required | the ID value associated with the transaction |
| `account_name` | `string` | Query, Required | the numeric account name |

## Response Type

[`StopDiagnosticsObservationResult`](../../doc/models/stop-diagnostics-observation-result.md)

## Example Usage

```python
transaction_id = '5f4bd2ff-5d7f-444d-af17-3f6a80bb2a94'
account_name = '0000123456-00001'

result = diagnostics_observations_controller.stop_diagnostics_observation(transaction_id, account_name)
```

## Example Response *(as JSON)*

```json
{
  "createdOn": "2019-09-10T19:05:33.33Z",
  "transactionID": "9c7bb124-11f5-4ff3-8a88-0eec1ba99205",
  "status": "CANCEL_OBSERVE_PENDING"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |

