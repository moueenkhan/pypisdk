
# Aggregate Usage Item

Contains usage per device

## Structure

`AggregateUsageItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `string` | Optional | International Mobile Equipment Idnetifier. This is the ID of the device reporting usage. |
| `number_of_sessions` | `int` | Optional | Number of sessions established by the device reporting usage. |
| `bytes_transferred` | `int` | Optional | The amount of data transferred by the device reporting usage, maesured in Bytes. |

## Example (as JSON)

```json
{
  "imei": null,
  "numberOfSessions": null,
  "bytesTransferred": null
}
```

