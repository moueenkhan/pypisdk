
# V3 Account Device List

Array of devices.

## Structure

`V3AccountDeviceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Required | Account name |
| `has_more_data` | `bool` | Required | has more device flag |
| `last_seen_device_id` | `string` | Optional | Last seen device identifier |
| `max_page_size` | `int` | Required | Maximum page size |
| `device_list` | [`List of V3AccountDevice`](../../doc/models/v3-account-device.md) | Required | Account device list |

## Example (as JSON)

```json
{
  "accountName": "0000123456-00001",
  "maxPageSize": 1000,
  "hasMoreData": true,
  "lastSeenDeviceId": "15-digit IMEI",
  "deviceList": [
    {
      "deviceId": "15-digit device ID",
      "mdn": "10-digit MDN",
      "model": "BG96",
      "make": "QUECTEL",
      "firmware": "BG96MAR04A04M1G",
      "licenseAssigned": false,
      "fotaEligible": "",
      "status": "Active",
      "protocol": "LWM2M",
      "softwareList": [
        {
          "name": "VZ_MDM_IOT",
          "version": "0.14",
          "upgradeTime": "2012-04-23T18:25:43.511Z"
        }
      ],
      "createTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "upgradeTime": "2021-06-03 00:03:56.079 +0000 UTC",
      "refreshTime": "2021-06-03 00:03:56.079 +0000 UTC"
    }
  ]
}
```

