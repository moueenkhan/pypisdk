
# Session Level

Session Report for a Device

## Structure

`SessionLevel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sessions` | [`List of DailyUsageItem`](../../doc/models/daily-usage-item.md) | Optional | Contains only dates when device had sessions |
| `id` | `string` | Required | The 10-digit ID of the device. |
| `txid` | `string` | Required | A unique string that associates the request with the location report information that is sent in asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the request. All of the callback messages will have the same txid. |

## Example (as JSON)

```json
{
  "id": "1234567890",
  "txid": null
}
```

