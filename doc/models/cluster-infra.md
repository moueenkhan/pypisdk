
# Cluster Infra

## Structure

`ClusterInfra`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `modified_at` | `string` | Optional | - |
| `organization_id` | `string` | Optional | - |
| `partner_id` | `string` | Optional | - |
| `country` | `string` | Optional | - |
| `city` | `string` | Optional | - |
| `latitude` | `string` | Optional | - |
| `longitude` | `string` | Optional | - |
| `cluster_id` | `string` | Optional | - |
| `status` | `string` | Optional | - |
| `cert` | `string` | Optional | - |
| `passphrase` | `string` | Optional | - |
| `id` | `string` | Optional | - |
| `cname` | `string` | Optional | - |
| `arecord` | `string` | Optional | - |
| `base_ratio` | `float` | Optional | - |
| `ha_enabled` | `bool` | Optional | - |
| `display_name` | `string` | Optional | - |
| `upgrade_status` | `string` | Optional | - |
| `provider_id` | `string` | Optional | - |
| `auto_create` | `bool` | Optional | - |
| `auto_approve_nodes` | `bool` | Optional | - |
| `provision_id` | `string` | Optional | - |
| `is_monitor_enabled` | `bool` | Optional | - |
| `health` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `health_status_modified_at` | `string` | Optional | - |
| `manufacturer` | `string` | Optional | - |
| `cluster_type` | `string` | Optional | - |
| `cluster_blueprint` | `string` | Optional | - |
| `gimage_used` | `string` | Optional | - |
| `reason` | `string` | Optional | - |
| `is_master_dedicated` | `bool` | Optional | - |
| `project_id` | `string` | Optional | - |
| `provision_os` | `string` | Optional | - |
| `default_storage_class` | `string` | Optional | - |
| `storage_class_map` | [`StorageClassMap`](../../doc/models/storage-class-map.md) | Optional | - |
| `cni_provider` | `string` | Optional | - |
| `provision_k_8_s` | `string` | Optional | - |
| `etcd_version` | `string` | Optional | - |
| `consul_version` | `string` | Optional | - |
| `cluster_blueprint_version` | `string` | Optional | - |
| `upgrade_protection` | `bool` | Optional | - |
| `provision` | [`ClusterInfraProvision`](../../doc/models/cluster-infra-provision.md) | Optional | - |
| `metro` | [`Metro`](../../doc/models/metro.md) | Optional | - |
| `nodes` | [`List of Node`](../../doc/models/node.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `cluster_provider_params` | [`ClusterProviderParams`](../../doc/models/cluster-provider-params.md) | Optional | - |
| `nodegroups` | [`List of NodeGroupItem`](../../doc/models/node-group-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `cluster_version_info` | [`ClusterVersionInfo`](../../doc/models/cluster-version-info.md) | Optional | - |
| `projects` | [`List of ProjectItem`](../../doc/models/project-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `cluster` | [`Cluster`](../../doc/models/cluster.md) | Optional | - |

## Example (as JSON)

```json
{
  "name": null,
  "created_at": null,
  "modified_at": null,
  "organization_id": null,
  "partner_id": null,
  "country": null,
  "city": null,
  "latitude": null,
  "longitude": null,
  "cluster_id": null,
  "status": null,
  "cert": null,
  "passphrase": null,
  "id": null,
  "cname": null,
  "arecord": null,
  "base_ratio": null,
  "ha_enabled": null,
  "display_name": null,
  "upgradeStatus": null,
  "provider_id": null,
  "auto_create": null,
  "auto_approve_nodes": null,
  "provision_id": null,
  "is_monitor_enabled": null,
  "health": null,
  "health_status_modified_at": null,
  "manufacturer": null,
  "cluster_type": null,
  "cluster_blueprint": null,
  "gimage_used": null,
  "reason": null,
  "is_master_dedicated": null,
  "project_id": null,
  "provision_os": null,
  "default_storage_class": null,
  "storage_class_map": null,
  "cni_provider": null,
  "provision_k8s": null,
  "etcd_version": null,
  "consul_version": null,
  "cluster_blueprint_version": null,
  "upgrade_protection": null,
  "provision": null,
  "Metro": null,
  "nodes": null,
  "cluster_provider_params": null,
  "nodegroups": null,
  "cluster_version_info": null,
  "projects": null,
  "cluster": null
}
```

