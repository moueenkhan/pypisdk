
# Session Report Request

Session report request.

## Structure

`SessionReportRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Required | Account Number |
| `start_date` | `string` | Optional | Start date of session to include. If not specified information will be shown from the earliest available (180 days). Can be either date in ISO 8601 format or predefined constants. |
| `end_date` | `string` | Optional | End date of session to include. If not specified information will be shown to the latest available. Can be either date in ISO 8601 format or predefined constants. |
| `imei` | `string` | Required | DeviceIds |
| `duration_low` | `int` | Optional | Optional filter parameter |
| `duration_high` | `int` | Optional | Optional filter parameter |

## Example (as JSON)

```json
{
  "accountNumber": "accountNumber2",
  "startDate": null,
  "endDate": null,
  "imei": "imei6",
  "durationLow": null,
  "durationHigh": null
}
```

