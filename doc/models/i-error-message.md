
# I Error Message

Error Message

## Structure

`IErrorMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | [`ErrorResponseCodeEnum`](../../doc/models/error-response-code-enum.md) | Optional | Error Code. Available values: INVALID_ACCESS, INVALID_PARAMETER, INTERNAL_ERROR, SUCCESS |
| `error_message` | `string` | Optional | Details and additional information about the error code. |
| `http_status_code` | [`HttpStatusCodeEnum`](../../doc/models/http-status-code-enum.md) | Optional | HTML error code and description. |
| `detail_error_message` | `string` | Optional | More detail and information about the HTML error code. |

## Example (as JSON)

```json
{
  "errorCode": null,
  "errorMessage": null,
  "httpStatusCode": null,
  "detailErrorMessage": null
}
```

