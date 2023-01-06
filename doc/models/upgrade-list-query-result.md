
# Upgrade List Query Result

Upgrade information

## Structure

`UpgradeListQueryResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_flag` | `bool` | Optional | True if there are more devices to retrieve. |
| `last_seen_upgrade_id` | `int` | Optional | If hasMoreData=true, the startIndex to use for the next request. 0 if hasMoreData=false. |
| `report_list` | [`List of FirmwareUpgrade`](../../doc/models/firmware-upgrade.md) | Optional | Array of upgrade objects with the specified status. |

## Example (as JSON)

```json
{
  "hasMoreFlag": null,
  "lastSeenUpgradeId": null,
  "reportList": null
}
```

