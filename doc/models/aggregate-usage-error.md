
# Aggregate Usage Error

Error Response

## Structure

`AggregateUsageError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `string` | Optional | International Mobile Equipment Idnetifier. This is the ID of the device reporting errors. |
| `error_message` | `string` | Optional | A general error message. |
| `error_response` | [`IErrorMessage`](../../doc/models/i-error-message.md) | Optional | Error Message |

## Example (as JSON)

```json
{
  "imei": null,
  "errorMessage": null,
  "errorResponse": null
}
```

