
# Resources Service Endpoint

Service Endpoint path, address, and port.

## Structure

`ResourcesServiceEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uri` | `string` | Optional | URI of Service Endpoint if available<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `\w+:(/?/?)[^\s]+` |
| `fqdn` | `string` | Optional | FQDN of Service Endpoint if available<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9.]{3,32}$` |
| `i_pv_4_address` | `string` | Optional | IPv4 Address of Service Endpoint if available<br>**Constraints**: *Maximum Length*: `32` |
| `i_pv_6_address` | `string` | Optional | IPv6 Address of Service Endpoint if available<br>**Constraints**: *Maximum Length*: `64` |
| `port` | `int` | Optional | Port information of Service Endpoint if IPv4 or IPv6 is mentioned<br>**Constraints**: `>= 1`, `<= 10000` |

## Example (as JSON)

```json
{
  "URI": null,
  "FQDN": null,
  "IPv4Address": null,
  "IPv6Address": null,
  "port": null
}
```

