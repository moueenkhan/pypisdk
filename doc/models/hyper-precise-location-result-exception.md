
# Hyper Precise Location Result Exception

Error Response

## Structure

`HyperPreciseLocationResultException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | [`ErrorResponseCodeEnum`](../../doc/models/error-response-code-enum.md) | Required | Error Code. Available values: INVALID_ACCESS, INVALID_PARAMETER, INTERNAL_ERROR, SUCCESS |
| `error_message` | `string` | Required | Error Message |

## Example (as JSON)

```json
{
  "errorCode": "INVALID_ACCESS",
  "errorMessage": "errorMessage8"
}
```

