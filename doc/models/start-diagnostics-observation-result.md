
# Start Diagnostics Observation Result

A success response containing the current status of the request.

## Structure

`StartDiagnosticsObservationResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `string` | Required | transactionID identifier |
| `status` | `string` | Required | status of the request |
| `created_on` | `datetime` | Required | createdOn timestamp |

## Example (as JSON)

```json
{
  "createdOn": "2019-09-10T19:05:33.33Z",
  "transactionID": "9c7bb124-11f5-4ff3-8a88-0eec1ba99205",
  "status": "CANCEL_OBSERVE_PENDING"
}
```

