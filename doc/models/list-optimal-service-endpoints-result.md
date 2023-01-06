
# List Optimal Service Endpoints Result

Response on successful retrieval of optimal service endpoints for clients

## Structure

`ListOptimalServiceEndpointsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_endpoints` | [`List of ResourcesEdgeHostedService`](../../doc/models/resources-edge-hosted-service.md) | Optional | An array of optimal Service Endpoint IDs for clients to connect to<br>**Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "serviceEndpoints": null
}
```

