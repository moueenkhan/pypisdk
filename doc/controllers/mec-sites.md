# MEC Sites

```python
mec_sites_controller = client.mec_sites
```

## Class Name

`MECSitesController`

## Methods

* [List MEC Site Locations](../../doc/controllers/mec-sites.md#list-mec-site-locations)
* [List ERN Cluster Namespaces](../../doc/controllers/mec-sites.md#list-ern-cluster-namespaces)


# List MEC Site Locations

Supports fetching MEC locations so the user can view the city.

```python
def list_mec_site_locations(self,
                           account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Optional | User account name<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |

## Response Type

[`MECSiteLocationsResult`](../../doc/models/mec-site-locations-result.md)

## Example Usage

```python
account_name = 'test_account1'

result = mec_sites_controller.list_mec_site_locations(account_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |


# List ERN Cluster Namespaces

Get list of cluster and namespaces for a given ERN

```python
def list_ern_cluster_namespaces(self,
                               ern,
                               account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ern` | `string` | Template, Required | Edge Resource Number<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `account_name` | `string` | Header, Optional | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |

## Response Type

[`ClustersNamespaces`](../../doc/models/clusters-namespaces.md)

## Example Usage

```python
ern = 'us-east-1-wl1-atl-wlz-1'
account_name = 'test_account1'

result = mec_sites_controller.list_ern_cluster_namespaces(ern, account_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 404 | Not found | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 500 | Internal Server Error | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | unexpected error | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |

