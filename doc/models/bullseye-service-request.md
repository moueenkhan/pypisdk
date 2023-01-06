
# Bullseye Service Request

Account number and List of devices

## Structure

`BullseyeServiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_list` | [`List of DeviceServiceRequest`](../../doc/models/device-service-request.md) | Required | A list of devices. |
| `account_number` | `string` | Required | A unique identifier for an account. |

## Example (as JSON)

```json
{
  "deviceList": [
    {
      "imei": "imei0",
      "BullseyeEnable": false
    },
    {
      "imei": "imei9",
      "BullseyeEnable": true
    }
  ],
  "accountNumber": "accountNumber2"
}
```

