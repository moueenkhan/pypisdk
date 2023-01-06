
# Cloud

## Structure

`Cloud`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `provider` | [`CloudProviderEnum`](../../doc/models/cloud-provider-enum.md) | Optional | Cloud provider where you plan to provision and operate your Kubernetes cluster |
| `distribution` | [`CloudDestributionEnum`](../../doc/models/cloud-destribution-enum.md) | Optional | Supported Kubernetes distribution for the selected cloud provider |
| `common_config` | [`CommonConfiguration`](../../doc/models/common-configuration.md) | Optional | - |
| `cluster_config` | [`ClusterConfiguration`](../../doc/models/cluster-configuration.md) | Optional | - |
| `node_config` | [`NodeConfiguration`](../../doc/models/node-configuration.md) | Optional | - |
| `node_configs` | [`List of NodeConfiguration`](../../doc/models/node-configuration.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `advance_config` | [`AdvanceConfiguration`](../../doc/models/advance-configuration.md) | Optional | - |

## Example (as JSON)

```json
{
  "clusterConfig": {
    "autoCreateNetworkInfra": true,
    "networkNatMode": "single"
  },
  "commonConfig": {
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
  },
  "distribution": "AmazonEKS",
  "nodeConfigs": [
    {
      "autoCreateServiceRoles": true,
      "enableAlbAccess": true,
      "enableAppMeshAccess": true,
      "enableAsgAccess": true,
      "enableDnsAccess": true,
      "enableEfsAccess": true,
      "enableFullAccessToEcr": true,
      "endPointAccessType": "private",
      "instanceType": "m5.xlarge",
      "isManagedNodeGroup": false,
      "isSpotInstanceNeeded": false,
      "isWavelengthZone": false,
      "labels": {},
      "name": "ng-22",
      "nodeAmiFamily": "AmazonLinux2",
      "nodePrivateNetworking": false,
      "nodeVolumeSize": 80,
      "nodeVolumeType": "gp3",
      "nodes": 2,
      "nodesMax": 2,
      "nodesMin": 2,
      "tags": {},
      "useVolumeEncryption": true
    },
    {
      "autoCreateServiceRoles": true,
      "enableAlbAccess": true,
      "enableAppMeshAccess": true,
      "enableAsgAccess": true,
      "enableDnsAccess": true,
      "enableEfsAccess": true,
      "enableFullAccessToEcr": true,
      "endPointAccessType": "private",
      "instanceType": "t3.xlarge",
      "isManagedNodeGroup": false,
      "isSpotInstanceNeeded": false,
      "isWavelengthZone": true,
      "labels": {},
      "name": "ng-wavelength-test22",
      "nodeAmiFamily": "AmazonLinux2",
      "nodePrivateNetworking": false,
      "nodeVolumeSize": 80,
      "nodeVolumeType": "gp2",
      "nodes": 2,
      "nodesMax": 2,
      "nodesMin": 2,
      "subnetCidrBlock": "192.168.192.0/19",
      "tags": {},
      "useVolumeEncryption": true
    }
  ]
}
```

