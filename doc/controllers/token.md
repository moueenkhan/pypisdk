# Token

```python
token_controller = client.token
```

## Class Name

`TokenController`


# Get Token

:information_source: **Note** This endpoint does not require authentication.

```python
def get_token(self,
             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Token`](../../doc/models/token.md) | Body, Required | - |

## Response Type

`mixed`

## Example Usage

```python
body = Token()
body.client_id = 'client_id8'
body.client_secret = 'client_secret4'
body.grant_type = 'grant_type8'

result = token_controller.get_token(body)
```

