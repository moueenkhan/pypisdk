
# Node Status Capacity

## Structure

`NodeStatusCapacity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cpu_count` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `ephemeral_storage_kb` | `long\|int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `memory_kb` | `long\|int` | Optional | **Constraints**: `>= 0`, `<= 1024` |

## Example (as JSON)

```json
{
  "cpuCount": null,
  "ephemeralStorageKB": null,
  "memoryKB": null
}
```

