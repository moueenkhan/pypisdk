# Anomaly Triggers

```python
anomaly_triggers_controller = client.anomaly_triggers
```

## Class Name

`AnomalyTriggersController`

## Methods

* [Update Anomaly Detection Trigger](../../doc/controllers/anomaly-triggers.md#update-anomaly-detection-trigger)
* [List Anomaly Detection Trigger Settings](../../doc/controllers/anomaly-triggers.md#list-anomaly-detection-trigger-settings)
* [Create Anomaly Detection Trigger](../../doc/controllers/anomaly-triggers.md#create-anomaly-detection-trigger)


# Update Anomaly Detection Trigger

Updates an existing trigger using the account name.

```python
def update_anomaly_detection_trigger(self,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List of UpdateTriggerRequestOptions`](../../doc/models/update-trigger-request-options.md) | Body, Required | Update Trigger Request |

## Response Type

[`IntelligenceSuccessResult`](../../doc/models/intelligence-success-result.md)

## Example Usage

```python
body = []

body.append(UpdateTriggerRequestOptions())
body[0].trigger_id = '595f5c44-c31c-4552-8670-020a1545a84d'
body[0].trigger_name = 'Anomaly Daily Usage REST Test-Patch Update 4'
body[0].trigger_category = 'UsageAnomaly'
body[0].account_name = '0000123456-00001'
body[0].anomaly_trigger_request = AnomalyTriggerRequest()
body[0].anomaly_trigger_request.account_names = '0000123456-00001'
body[0].anomaly_trigger_request.include_abnormal = True
body[0].anomaly_trigger_request.include_very_abnormal = True
body[0].anomaly_trigger_request.include_under_expected_usage = False
body[0].anomaly_trigger_request.include_over_expected_usage = True
body[0].notification = Notification()
body[0].notification.notification_type = 'DailySummary'
body[0].notification.callback = True
body[0].notification.email_notification = False
body[0].notification.notification_group_name = 'Anomaly Test API'
body[0].notification.notification_frequency_factor = 3
body[0].notification.notification_frequency_interval = 'Hourly'
body[0].notification.external_email_recipients = 'placeholder@verizon.com'
body[0].notification.sms_notification = True
body[0].notification.sms_numbers = []

body[0].notification.sms_numbers.append(SMSNumber())
body[0].notification.sms_numbers[0].carrier = 'US Cellular'
body[0].notification.sms_numbers[0].number = '9299280711'

body[0].notification.reminder = True
body[0].notification.severity = 'Critical'


result = anomaly_triggers_controller.update_anomaly_detection_trigger(body)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |


# List Anomaly Detection Trigger Settings

Retrieves the values for a specific trigger ID

```python
def list_anomaly_detection_trigger_settings(self,
                                           trigger_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `string` | Template, Required | The trigger ID of a specific trigger |

## Response Type

[`AnomalyTriggerResult`](../../doc/models/anomaly-trigger-result.md)

## Example Usage

```python
trigger_id = 'be1b5958-3e11-41db-9abd-b1b7618c0035'

result = anomaly_triggers_controller.list_anomaly_detection_trigger_settings(trigger_id)
```

## Example Response *(as JSON)*

```json
{
  "triggers": [
    {
      "triggerId": "BE1B5958-3E11-41DB-9ABD-B1B7618C0035",
      "triggerName": "Anomaly Daily Usage REST Test-1",
      "organizationName": "AnamolyDetectionRTRTest",
      "triggerCategory": "UsageAnomaly",
      "triggerAttributes": [
        {
          "key": "DataPercentage50",
          "value": false
        }
      ],
      "createdAt": "2021-10-21T23:57:03.397.0000Z",
      "modifiedAt": "2021-10-21T23:57:03.397.0000Z",
      "notification": {
        "notificationType": "DailySummary",
        "callback": true,
        "emailNotification": true,
        "notificationGroupName": "Anomaly Test API",
        "notificationFrequencyFactor": -2147483648,
        "externalEmailRecipients": "placeholder@verizon.com",
        "smsNotification": true,
        "smsNumbers": [
          {
            "carrier": "US Cellular",
            "number": "9299280711"
          }
        ],
        "reminder": false,
        "severity": "Critical"
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |


# Create Anomaly Detection Trigger

Creates the trigger to identify an anomaly.

```python
def create_anomaly_detection_trigger(self,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List of CreateTriggerRequestOptions`](../../doc/models/create-trigger-request-options.md) | Body, Required | Create Trigger Request |

## Response Type

[`AnomalyDetectionTrigger`](../../doc/models/anomaly-detection-trigger.md)

## Example Usage

```python
body = []

body.append(CreateTriggerRequestOptions())
body[0].name = 'Anomaly Daily Usage REST Test-Patch 1'
body[0].trigger_category = 'UsageAnomaly'
body[0].account_name = '0000123456-00001'
body[0].anomaly_trigger_request = AnomalyTriggerRequest()
body[0].anomaly_trigger_request.account_names = '0000123456-00001'
body[0].anomaly_trigger_request.include_abnormal = True
body[0].anomaly_trigger_request.include_very_abnormal = True
body[0].anomaly_trigger_request.include_under_expected_usage = True
body[0].anomaly_trigger_request.include_over_expected_usage = True
body[0].notification = Notification()
body[0].notification.notification_type = 'DailySummary'
body[0].notification.callback = True
body[0].notification.email_notification = False
body[0].notification.notification_group_name = 'Anomaly Test API'
body[0].notification.notification_frequency_factor = 3
body[0].notification.notification_frequency_interval = 'Hourly'
body[0].notification.external_email_recipients = 'placeholder@verizon.com'
body[0].notification.sms_notification = True
body[0].notification.sms_numbers = []

body[0].notification.sms_numbers.append(SMSNumber())
body[0].notification.sms_numbers[0].carrier = 'US Cellular'
body[0].notification.sms_numbers[0].number = '9299280711'

body[0].notification.reminder = True
body[0].notification.severity = 'Critical'


result = anomaly_triggers_controller.create_anomaly_detection_trigger(body)
```

## Example Response *(as JSON)*

```json
{
  "triggerId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`IntelligenceResultException`](../../doc/models/intelligence-result-exception.md) |

