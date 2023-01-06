# Account Subscriptions

```python
account_subscriptions_controller = client.account_subscriptions
```

## Class Name

`AccountSubscriptionsController`


# List Account Subscriptions

This corresponds to the M2M-MC SOAP interface, `GetSubscriptionInformation`.

```python
def list_account_subscriptions(self,
                              body,
                              x_request_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SecuritySubscriptionRequest`](../../doc/models/security-subscription-request.md) | Body, Required | Account Subscription Request |
| `x_request_id` | `string` | Header, Optional | Transaction Id<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]-[0-9]{3,32}$` |

## Response Type

[`SecuritySubscriptionResult`](../../doc/models/security-subscription-result.md)

## Example Usage

```python
body = SecuritySubscriptionRequest()
body.account_name = '000012345600001'
body.sku_number = 'SIMSec-IoT-Lt'

result = account_subscriptions_controller.list_account_subscriptions(body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "000012345600001",
  "subscriptionList": [
    {
      "skuNumber": "TS-BUNDLE-KTO-SIMSEC-MRC",
      "licenseType": "Flexible Bundle",
      "licensePurchased": 9,
      "licenseAssigned": 7,
      "licenseAvailable": 1
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 401 | Unauthorized | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 403 | Forbidden | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 404 | Not Found / Does not exist | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 406 | Format / Request Unacceptable | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| 429 | Too many requests | [`SecurityResultException`](../../doc/models/security-result-exception.md) |
| Default | Error response | [`SecurityResultException`](../../doc/models/security-result-exception.md) |

