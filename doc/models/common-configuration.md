
# Common Configuration

## Structure

`CommonConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cloud_credentials` | [`CloudCredential`](../../doc/models/cloud-credential.md) | Optional | - |
| `k_8_s_version` | [`K8sVersionEnum`](../../doc/models/k8-s-version-enum.md) | Optional | Version of K8s platform<br>**Default**: `'1.18'` |
| `blueprint` | [`Blueprint`](../../doc/models/blueprint.md) | Optional | - |

## Example (as JSON)

```json
{
  "blueprint": {
    "name": "default",
    "version": "latest"
  },
  "cloudCredentials": {
    "clusterProvisioning": {
      "provider": "AWS"
    },
    "name": "acme-aws-qa-mdp-5"
  },
  "k8sVersion": "1.21"
}
```

