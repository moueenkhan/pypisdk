
# Hyper Precise Location Callback

Callback request.

## Structure

`HyperPreciseLocationCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Required | The billing account information: |
| `name` | `string` | Required | The name of the callback service that you want to subscribe to: |
| `url` | `string` | Required | The address on your server where you have enabled a listening service for the specific type of callback messages. Specify a URL that is reachable from the Verizon data centers. If your service is running on HTTPS, you should use a one-way authentication certificate with a white-listed IP address. |

## Example (as JSON)

```json
{
  "aname": "aname4",
  "name": "name0",
  "url": "url4"
}
```

