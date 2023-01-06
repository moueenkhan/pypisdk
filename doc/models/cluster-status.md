
# Cluster Status

## Structure

`ClusterStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conditions` | [`List of ConditionItem`](../../doc/models/condition-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `token` | `string` | Optional | - |
| `published_blueprint` | `string` | Optional | - |
| `nodes` | [`List of NodeStatusItem`](../../doc/models/node-status-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `system_task_count` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `custom_task_count` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `auxiliary_task_count` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `projects` | [`List of StatusProjectItem`](../../doc/models/status-project-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `extra` | [`ClusterStatusExtra`](../../doc/models/cluster-status-extra.md) | Optional | - |

## Example (as JSON)

```json
{
  "conditions": null,
  "token": null,
  "publishedBlueprint": null,
  "nodes": null,
  "systemTaskCount": null,
  "customTaskCount": null,
  "auxiliaryTaskCount": null,
  "projects": null,
  "extra": null
}
```

