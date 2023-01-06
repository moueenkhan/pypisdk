# Campaigns V2

```python
campaigns_v2_controller = client.campaigns_v2
```

## Class Name

`CampaignsV2Controller`

## Methods

* [Update Campaign Firmware Devices](../../doc/controllers/campaigns-v2.md#update-campaign-firmware-devices)
* [Cancel Campaign](../../doc/controllers/campaigns-v2.md#cancel-campaign)
* [Update Campaign Dates](../../doc/controllers/campaigns-v2.md#update-campaign-dates)
* [Schedule Campaign Firmware Upgrade](../../doc/controllers/campaigns-v2.md#schedule-campaign-firmware-upgrade)
* [Get Campaign Information](../../doc/controllers/campaigns-v2.md#get-campaign-information)


# Update Campaign Firmware Devices

This endpoint allows user to Add or Remove devices to an existing software upgrade.

```python
def update_campaign_firmware_devices(self,
                                    account,
                                    campaign_id,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Software upgrade information |
| `body` | [`V2AddOrRemoveDeviceRequest`](../../doc/models/v2-add-or-remove-device-request.md) | Body, Required | Add or remove device to existing software upgrade information |

## Response Type

[`V2AddOrRemoveDeviceResult`](../../doc/models/v2-add-or-remove-device-result.md)

## Example Usage

```python
account = '0000123456-00001'
campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'
body = V2AddOrRemoveDeviceRequest()
body.mtype = 'remove'
body.device_list = ['990013907884259', '990013907835573', '990013907833575']

result = campaigns_v2_controller.update_campaign_firmware_devices(account, campaign_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Cancel Campaign

This endpoint allows user to cancel software upgrade. A software upgrade already started can not be cancelled.

```python
def cancel_campaign(self,
                   account,
                   campaign_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Software upgrade information |

## Response Type

[`FotaV2SuccessResult`](../../doc/models/fota-v2-success-result.md)

## Example Usage

```python
account = '0000123456-00001'
campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'

result = campaigns_v2_controller.cancel_campaign(account, campaign_id)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Update Campaign Dates

This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged should be also provided

```python
def update_campaign_dates(self,
                         account,
                         campaign_id,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Software upgrade information |
| `body` | [`V2ChangeCampaignDatesRequest`](../../doc/models/v2-change-campaign-dates-request.md) | Body, Required | New dates and time windows |

## Response Type

[`CampaignSoftware`](../../doc/models/campaign-software.md)

## Example Usage

```python
account = '0000123456-00001'
campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'
body = V2ChangeCampaignDatesRequest()
body.start_date = dateutil.parser.parse('2020-08-21').date()
body.end_date = dateutil.parser.parse('2020-08-22').date()
body.download_after_date = dateutil.parser.parse('2020-08-21').date()
body.download_time_window_list = []

body.download_time_window_list.append(V2TimeWindow())
body.download_time_window_list[0].start_time = 3
body.download_time_window_list[0].end_time = 4

body.install_after_date = dateutil.parser.parse('2020-08-21').date()
body.install_time_window_list = []

body.install_time_window_list.append(V2TimeWindow())
body.install_time_window_list[0].start_time = 5
body.install_time_window_list[0].end_time = 6


result = campaigns_v2_controller.update_campaign_dates(account, campaign_id, body)
```

## Example Response *(as JSON)*

```json
{
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "accountName": "0402196254-00001",
  "campaignName": "FOTA_Verizon_Upgrade",
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "distributionType": "HTTP",
  "make": "Verizon",
  "model": "Model-A",
  "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
  "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
  "startDate": "2020-08-21",
  "endDate": "2020-08-22",
  "downloadAfterDate": "2020-08-21",
  "downloadTimeWindowList": [
    {
      "startTime": 3,
      "endTime": 4
    },
    {
      "startTime": 5,
      "endTime": 6
    }
  ],
  "installAfterDate": "2020-08-21",
  "installTimeWindowList": [
    {
      "startTime": 5,
      "endTime": 6
    },
    {
      "startTime": 6,
      "endTime": 7
    }
  ],
  "status": "RequestPending"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Schedule Campaign Firmware Upgrade

This endpoint allows user to schedule a software upgrade.

```python
def schedule_campaign_firmware_upgrade(self,
                                      account,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `body` | [`CampaignSoftwareUpgrade`](../../doc/models/campaign-software-upgrade.md) | Body, Required | Software upgrade information |

## Response Type

[`CampaignSoftware`](../../doc/models/campaign-software.md)

## Example Usage

```python
account = '0000123456-00001'
body = CampaignSoftwareUpgrade()
body.campaign_name = 'FOTA_Verizon_Upgrade'
body.software_name = 'FOTA_Verizon_Model-A_02To03_HF'
body.software_from = 'FOTA_Verizon_Model-A_00To01_HF'
body.software_to = 'FOTA_Verizon_Model-A_02To03_HF'
body.distribution_type = 'HTTP'
body.start_date = dateutil.parser.parse('2020-08-21').date()
body.end_date = dateutil.parser.parse('2020-08-22').date()
body.download_after_date = dateutil.parser.parse('2020-08-21').date()
body.download_time_window_list = []

body.download_time_window_list.append(V2TimeWindow())
body.download_time_window_list[0].start_time = 20
body.download_time_window_list[0].end_time = 21

body.install_after_date = dateutil.parser.parse('2020-08-21').date()
body.install_time_window_list = []

body.install_time_window_list.append(V2TimeWindow())
body.install_time_window_list[0].start_time = 22
body.install_time_window_list[0].end_time = 23

body.device_list = ['990013907835573', '990013907884259']

result = campaigns_v2_controller.schedule_campaign_firmware_upgrade(account, body)
```

## Example Response *(as JSON)*

```json
{
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "accountName": "0402196254-00001",
  "campaignName": "FOTA_Verizon_Upgrade",
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "distributionType": "HTTP",
  "make": "Verizon",
  "model": "Model-A",
  "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
  "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
  "startDate": "2020-08-21",
  "endDate": "2020-08-22",
  "downloadAfterDate": "2020-08-21",
  "downloadTimeWindowList": [
    {
      "startTime": 20,
      "endTime": 21
    }
  ],
  "installAfterDate": "2020-08-21",
  "installTimeWindowList": [
    {
      "startTime": 22,
      "endTime": 23
    }
  ],
  "status": "CampaignRequestPending"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |


# Get Campaign Information

This endpoint allows user to get information of a software upgrade.

```python
def get_campaign_information(self,
                            account,
                            campaign_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Software upgrade identifier |

## Response Type

[`CampaignSoftware`](../../doc/models/campaign-software.md)

## Example Usage

```python
account = '0000123456-00001'
campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'

result = campaigns_v2_controller.get_campaign_information(account, campaign_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "accountName": "0402196254-00001",
  "campaignName": "FOTA_Verizon_Upgrade",
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "distributionType": "HTTP",
  "make": "Verizon",
  "model": "Model-A",
  "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
  "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
  "startDate": "2020-08-21",
  "endDate": "2020-08-22",
  "downloadAfterDate": "2020-08-21",
  "downloadTimeWindowList": [
    {
      "startTime": 20,
      "endTime": 21
    }
  ],
  "installAfterDate": "2020-08-21",
  "installTimeWindowList": [
    {
      "startTime": 22,
      "endTime": 23
    }
  ],
  "status": "CampaignEnded"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`FotaV2ResultException`](../../doc/models/fota-v2-result-exception.md) |

