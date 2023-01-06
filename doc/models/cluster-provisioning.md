
# Cluster Provisioning

## Structure

`ClusterProvisioning`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `provider` | [`ClusterProvideEnum`](../../doc/models/cluster-provide-enum.md) | Optional | credential provider |
| `access_key` | [`AccessKey`](../../doc/models/access-key.md) | Optional | - |
| `role` | [`Role`](../../doc/models/role.md) | Optional | Role of the user calling API. |

## Example (as JSON)

```json
{
  "provider": "AWS"
}
```

