
# Metadata

## Structure

`Metadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `display_name` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `modified_at` | `string` | Optional | - |
| `labels` | [`MetadataLabel`](../../doc/models/metadata-label.md) | Optional | - |
| `annotations` | [`MetadataAnnotation`](../../doc/models/metadata-annotation.md) | Optional | - |
| `organization_id` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `partner_id` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `project_id` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `id` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "name": null,
  "displayName": null,
  "createdAt": null,
  "modifiedAt": null,
  "labels": null,
  "annotations": null,
  "organizationID": null,
  "partnerID": null,
  "projectID": null,
  "id": null
}
```

