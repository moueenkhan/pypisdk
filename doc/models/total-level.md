
# Total Level

Session and usage details for up to 10 devices.

## Structure

`TotalLevel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `string` | Required | A unique string that associates the request with the location report information that is sent in asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the request. All of the callback messages will have the same txid. |
| `usage` | [`List of AggregateUsageItem`](../../doc/models/aggregate-usage-item.md) | Optional | Contains usage per device<br>**Constraints**: *Unique Items Required* |
| `errors` | [`List of AggregateUsageError`](../../doc/models/aggregate-usage-error.md) | Optional | An object containing any errors reported by the device.<br>**Constraints**: *Unique Items Required* |

## Example (as JSON)

```json
{
  "txid": "txid2",
  "usage": null,
  "errors": null
}
```

