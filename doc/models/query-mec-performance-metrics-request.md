
# Query MEC Performance Metrics Request

Request to query the most recent data for Key Performance Indicators (KPIs) like network availability, MEC hostnames and more.

## Structure

`QueryMECPerformanceMetricsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `string` | Required | The 15-digit International Mobile Equipment Identifier. |
| `msisdn` | `string` | Required | The 12-digit Mobile Station International Subscriber Directory Number. |

## Example (as JSON)

```json
{
  "IMEI": "440246108109673",
  "MSISDN": "10691876598"
}
```

