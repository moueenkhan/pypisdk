
# Device Service Information

Device service information

## Structure

`DeviceServiceInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_type` | [`ApiResponseCode`](../../doc/models/api-response-code.md) | Optional | ResponseCode and/or a message indicating success or failure of the request. |
| `imei` | `string` | Required | The International Mobile Equipment Identifier of the device. |
| `bullseye_enable` | `bool` | Required | Shows if Hyper Precise is enabled (true) or disabled (false). |

## Example (as JSON)

```json
{
  "responseType": null,
  "imei": "imei6",
  "BullseyeEnable": false
}
```

