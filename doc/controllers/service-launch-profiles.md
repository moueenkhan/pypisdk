# Service Launch Profiles

```python
service_launch_profiles_controller = client.service_launch_profiles
```

## Class Name

`ServiceLaunchProfilesController`

## Methods

* [Submit Service Profile](../../doc/controllers/service-launch-profiles.md#submit-service-profile)
* [Create Service Profile](../../doc/controllers/service-launch-profiles.md#create-service-profile)
* [Update Service Profile](../../doc/controllers/service-launch-profiles.md#update-service-profile)


# Submit Service Profile

Submit a service profile

```python
def submit_service_profile(self,
                          id,
                          body,
                          account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | Unique service profile ID.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |
| `body` | [`ServicesProfileRegistration`](../../doc/models/services-profile-registration.md) | Body, Required | The request body passes all of the needed parameters to create a service profile. |
| `account_name` | `string` | Header, Optional | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |

## Response Type

[`ServicesProfileRegistrationResult`](../../doc/models/services-profile-registration-result.md)

## Example Usage

```python
id = 'eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1'
body = ServicesProfileRegistration()
body.id = '6789409c-12c3-4fc9-b64f-71d1611c4f09'
body.name = 'mongo-pmec-profile-mdp7'
body.service_name = 'mongodb-customer-prerun'
body.service_version = '1.0.0'
body.version = '1.0.0'
body.state = ServicesProfileRegistrationStateEnum.DRAFT
body.customer_id = 'acme'
body.created_by = 'acme-user'
body.created_at = '2022-08-03T03:43:17.504Z'
body.last_updated_at = '2022-08-03T03:43:17.504Z'
body.linked_service_instances = []

body.access_intents = AccessIntents()
body.placement_intents = PlacementIntents()
body.placement_intents.intent_chain = []

body.placement_intents.intent_chain.append(IntentChainItem())
body.placement_intents.intent_chain[0].name = 'Compliance'
body.placement_intents.intent_chain[0].input = jsonpickle.decode('{"deploymentLocations":[{"csp":"AWS_WL","region":"US_WEST_2","zoneId":["us-west-2-wl1-den-wlz-1"]}]}')

body.deployment_locations = []

account_name = 'test_account1'

result = service_launch_profiles_controller.submit_service_profile(id, body, account_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 401 | HTTP 401 Unauthorized | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 412 | Precondition Failed | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 500 | Internal Server Error | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | HTTP 500 Internal Server Error | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |


# Create Service Profile

Creates a service profile that describes the resource requirements of a service.

```python
def create_service_profile(self,
                          account_name,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |
| `body` | [`CreateServiceProfileRequest`](../../doc/models/create-service-profile-request.md) | Body, Required | The request body passes all of the needed parameters to create a service profile. |

## Response Type

[`ServicesProfileRegistration`](../../doc/models/services-profile-registration.md)

## Example Usage

```python
account_name = 'test_account1'
body = CreateServiceProfileRequest()
body.name = 'mongo-pmec-profile-mdp7'
body.service_name = 'mongodb-customer-prerun'
body.service_version = '1.0.0'

result = service_launch_profiles_controller.create_service_profile(account_name, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 401 | HTTP 401 Unauthorized | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | HTTP 500 Internal Server Error | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |


# Update Service Profile

Update the definition of a Service Profile.

```python
def update_service_profile(self,
                          id,
                          body,
                          account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | Unique ID of the service profile.<br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `body` | [`CreateServiceProfileRequest`](../../doc/models/create-service-profile-request.md) | Body, Required | The request body passes the rest of the needed parameters to create a service profile. Parameters other than `serviceProfileId` will be edited |
| `account_name` | `string` | Header, Optional | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |

## Response Type

[`ServicesProfileRegistration`](../../doc/models/services-profile-registration.md)

## Example Usage

```python
id = 'eda2cb4e-50ef-4ae8-b304-7d2f0f7a21c1'
body = CreateServiceProfileRequest()
body.name = 'mongo-pmec-profile-mdp7'
body.service_name = 'mongodb-customer-prerun'
body.service_version = '1.0.0'
account_name = 'test_account1'

result = service_launch_profiles_controller.update_service_profile(id, body, account_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| 401 | HTTP 401 Unauthorized | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |
| Default | HTTP 500 Internal Server Error | [`EdgeServiceLaunchResultException`](../../doc/models/edge-service-launch-result-exception.md) |

