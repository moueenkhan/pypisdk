
# Check in History Item

Check-in history for a device

## Structure

`CheckInHistoryItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Required | Device IMEI |
| `client_type` | `string` | Required | Client type |
| `result` | `string` | Required | Result |
| `failure_type` | `string` | Required | Failure type |
| `time_completed` | `datetime` | Required | Time completed |

## Example (as JSON)

```json
{
  "deviceId": "990013907835573",
  "clientType": null,
  "result": null,
  "failureType": null,
  "timeCompleted": "10/22/2020 19:35:07"
}
```

