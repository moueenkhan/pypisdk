
# Device Diagnostics Callback

Callback information of an existing Diagnostics subscription

## Structure

`DeviceDiagnosticsCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Required | The name of the billing account for which callback messages will be sent. Format: "##########-#####". |
| `service_name` | `string` | Required | The name of the callback service, which identifies the type and format of messages that will be sent to the registered URL. |
| `endpoint` | `string` | Required | The URL for your web server. |
| `created_on` | `datetime` | Required | The date and time of when this request was created. |
| `http_headers` | `object` | Optional | Your http headers. |

## Example (as JSON)

```json
{
  "accountName": "TestQAAccount",
  "serviceName": "Diagnostics",
  "endpoint": "https://yourwebsite.com",
  "createdOn": "2019-09-07T23:57:53.292Z"
}
```

