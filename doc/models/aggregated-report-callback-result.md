
# Aggregated Report Callback Result

Aggregated Usage Report (Asynchronous).

## Structure

`AggregatedReportCallbackResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `string` | Required | A unique string that associates the request with the location report information that is sent in asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the request. All of the callback messages will have the same txid. |
| `status` | [`AggregatedReportCallbackStatusEnum`](../../doc/models/aggregated-report-callback-status-enum.md) | Optional | QUEUED or COMPLETED. Requests for IoT devices with cacheMode=0 (cached) have status=COMPLETED; all other requests are QUEUED. |

## Example (as JSON)

```json
{
  "txid": "txid2",
  "status": null
}
```

