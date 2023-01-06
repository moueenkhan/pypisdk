
# Anomaly Detection Settings

Settings for Anomaly Detection.

## Structure

`AnomalyDetectionSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | Indicates if the account name used has Anomaly Detection.<br />Success - The account has Anomaly Detection<br />Failure - The account does not have Anomaly Detection |
| `sensitivity_parameter` | [`SensitivityParameters`](../../doc/models/sensitivity-parameters.md) | Optional | Sensitivity parameters details |
| `status` | `string` | Optional | Indicates if Anomaly Detection is active on the account<br />Active - Anomaly Detection is active<br />Disabled- Anomaly Detection is not active |

## Example (as JSON)

```json
{
  "accountName": "Success",
  "sensitivityParameter": {
    "abnormalMaxValue": 1.1,
    "enableAbnormal": true,
    "enableVeryAbnormal": true,
    "veryAbnormalMaxValue": 0.55
  },
  "status": "Active"
}
```

