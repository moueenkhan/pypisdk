
# Aggregate Session Report Request

Aggregated report request.

## Structure

`AggregateSessionReportRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Required | Account Number |
| `start_date` | `string` | Optional | Start date of session to include. If not specified information will be shown from the earliest available (180 days). Can be either date in ISO 8601 format or predefined constants. |
| `end_date` | `string` | Optional | End date of session to include. If not specified information will be shown to the latest available. Can be either date in ISO 8601 format or predefined constants. |
| `imei` | `string` | Required | Devices for which return usage info. Could be 0, 1 or more. In case of 0 will return all devices belonging to customer (except of filtered by other parameters) |
| `device_group` | `string` | Optional | Optional filter parameter |
| `data_plan` | `string` | Optional | Optional filter parameter |
| `no_session_flag` | `string` | Optional | Optional filter parameter which return only devices with no sessions |

## Example (as JSON)

```json
{
  "accountNumber": "accountNumber2",
  "startDate": null,
  "endDate": null,
  "imei": "imei6",
  "deviceGroup": null,
  "dataPlan": null,
  "noSessionFlag": null
}
```

