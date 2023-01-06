
# Advance Configuration

## Structure

`AdvanceConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_role_arn` | `string` | Optional | - |
| `service_role_permission_boundary` | `string` | Optional | - |
| `enable_proxy` | `bool` | Optional | **Default**: `False` |
| `http_proxy` | `string` | Optional | - |
| `https_proxy` | `string` | Optional | - |
| `no_proxy` | `string` | Optional | - |
| `proxy_root_ca` | `string` | Optional | - |
| `enable_tls_traffic` | `bool` | Optional | **Default**: `False` |
| `enable_auto_approve` | `bool` | Optional | **Default**: `False` |
| `enable_multi_master` | `bool` | Optional | **Default**: `False` |
| `enable_dedicated_master` | `bool` | Optional | **Default**: `False` |

## Example (as JSON)

```json
{
  "serviceRoleArn": null,
  "serviceRolePermissionBoundary": null,
  "enableProxy": null,
  "httpProxy": null,
  "httpsProxy": null,
  "noProxy": null,
  "proxyRootCA": null,
  "enableTlsTraffic": null,
  "enableAutoApprove": null,
  "enableMultiMaster": null,
  "enableDedicatedMaster": null
}
```

