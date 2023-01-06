
# Cluster Metadata

## Structure

`ClusterMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | name of the cluster to be used<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `description` | `string` | Optional | Description of the cluster<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-\s]{1,500}$` |
| `cluster_type` | [`ClusterTypeEnum`](../../doc/models/cluster-type-enum.md) | Optional | - |
| `cloud` | [`Cloud`](../../doc/models/cloud.md) | Optional | - |
| `data_center` | [`DataCenter`](../../doc/models/data-center.md) | Optional | - |
| `labels` | [`List of EdgeServiceLaunchParams`](../../doc/models/edge-service-launch-params.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `ingress_ips` | [`ClusterIngressIP`](../../doc/models/cluster-ingress-ip.md) | Optional | - |
| `upgrade_protection` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "cloud": {
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
  },
  "clusterType": "publicCloud",
  "description": "Cluster Details",
  "name": "dev-acme-aws-us-west-2-wl1-den-wlz-1"
}
```

