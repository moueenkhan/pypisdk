# Diagnostics History

```python
diagnostics_history_controller = client.diagnostics_history
```

## Class Name

`DiagnosticsHistoryController`


# Get Diagnostics History

This endpoint allows the user to get the history data

```python
def get_diagnostics_history(self,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`HistorySearchRequest`](../../doc/models/history-search-request.md) | Body, Required | History data information |

## Response Type

[`List of History`](../../doc/models/history.md)

## Example Usage

```python
body = HistorySearchRequest()
body.filter = HistorySearchFilter()
body.filter.account_name = '0000123456-00001'
body.filter.device = Device()
body.filter.device.id = '15-digit IMEI'
body.filter.device.kind = 'IMEI'
body.filter.attributes = HistorySearchFilterAttributes()
body.filter.attributes.name = 'LINK_QUALITY'

result = diagnostics_history_controller.get_diagnostics_history(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "accountName": "0000123456-00001",
    "attributes": {
      "createdOn": "2022-02-10T16:02:21.406Z",
      "name": "LINK_QUALITY",
      "value": "47"
    },
    "device": {
      "id": "15-digit IMEI",
      "kind": "IMEI"
    }
  },
  {
    "accountName": "0000123456-00001",
    "attributes": {
      "createdOn": "2022-02-10T16:02:05.316Z",
      "name": "LINK_QUALITY",
      "value": "47"
    },
    "device": {
      "id": "15-digit IMEI",
      "kind": "IMEI"
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`DeviceDiagnosticsResultException`](../../doc/models/device-diagnostics-result-exception.md) |

