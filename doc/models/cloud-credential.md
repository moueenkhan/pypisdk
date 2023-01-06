
# Cloud Credential

## Structure

`CloudCredential`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | name of the credentials |
| `cluster_provisioning` | [`ClusterProvisioning`](../../doc/models/cluster-provisioning.md) | Optional | - |
| `data_backup` | [`DataBackup`](../../doc/models/data-backup.md) | Optional | - |

## Example (as JSON)

```json
{
  "clusterProvisioning": {
    "provider": "AWS"
  },
  "name": "acme-aws-qa-mdp-5"
}
```

