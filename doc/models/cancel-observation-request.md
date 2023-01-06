
# Cancel Observation Request

Specification of diagnostics services you want to cancel.

## Structure

`CancelObservationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `string` | Required | transactionID identifier |
| `account_name` | `string` | Required | Account identifier in "##########-#####". |
| `devices` | [`List of Device`](../../doc/models/device.md) | Optional | list of devices |
| `attributes` | [`List of ObservationRequestAttribute`](../../doc/models/observation-request-attribute.md) | Optional | Attributes are streaming RF parameters that you want to observe. |

## Example (as JSON)

```json
{
  "transactionID": "5f4bd2ff-5d7f-444d-af17-3f6a80bb2a94",
  "accountName": "TestQAAccount",
  "devices": [
    {
      "id": "15-digit IMEI",
      "kind": "IMEI"
    }
  ],
  "attributes": [
    {
      "name": "RADIO_SIGNAL_STRENGTH"
    },
    {
      "name": "LINK_QUALITY"
    },
    {
      "name": "NETWORK_BEARER"
    },
    {
      "name": "CELL_ID"
    }
  ]
}
```

