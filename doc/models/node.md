
# Node

## Structure

`Node`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `modified_at` | `string` | Optional | - |
| `node_id` | `string` | Optional | - |
| `private_ip` | `string` | Optional | - |
| `num_cores` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `total_memory` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `cluster_id` | `string` | Optional | - |
| `roles` | `List of string` | Optional | **Constraints**: *Maximum Items*: `100` |
| `id` | `string` | Optional | - |
| `approved` | `bool` | Optional | - |
| `status` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "name": null,
  "created_at": null,
  "modified_at": null,
  "node_id": null,
  "private_ip": null,
  "num_cores": null,
  "total_memory": null,
  "cluster_id": null,
  "roles": null,
  "id": null,
  "approved": null,
  "status": null
}
```

