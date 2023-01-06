
# Node Status

## Structure

`NodeStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state` | `string` | Optional | - |
| `conditions` | [`List of StatusConditionItem`](../../doc/models/status-condition-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `node_info` | [`NodeStatusInfo`](../../doc/models/node-status-info.md) | Optional | - |
| `capacity` | [`NodeStatusCapacity`](../../doc/models/node-status-capacity.md) | Optional | - |
| `allocatable` | [`NodeStatusAllocatable`](../../doc/models/node-status-allocatable.md) | Optional | - |
| `allocated` | [`NodeStatusAllocated`](../../doc/models/node-status-allocated.md) | Optional | - |
| `ips` | [`List of IP`](../../doc/models/ip.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "state": null,
  "conditions": null,
  "nodeInfo": null,
  "capacity": null,
  "allocatable": null,
  "allocated": null,
  "ips": null
}
```

