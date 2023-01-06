# Targets

```python
targets_controller = client.targets
```

## Class Name

`TargetsController`

## Methods

* [Query Target](../../doc/controllers/targets.md#query-target)
* [Delete Target](../../doc/controllers/targets.md#delete-target)
* [Create Target](../../doc/controllers/targets.md#create-target)
* [Generateanexternal ID](../../doc/controllers/targets.md#generateanexternal-id)


# Query Target

Search for targets by property values. Returns an array of all matching target resources.

```python
def query_target(self,
                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`QueryTargetRequest`](../../doc/models/query-target-request.md) | Body, Required | Search for targets by property values. |

## Response Type

[`List of Target`](../../doc/models/target.md)

## Example Usage

```python
body = QueryTargetRequest()
body.accountidentifier = AccountIdentifier()
body.accountidentifier.billingaccountid = '1223334444-00001'
body.resourceidentifier = ResourceIdentifier()
body.resourceidentifier.id = 'dd1682d3-2d80-cefc-f3ee-25154800beff'

result = targets_controller.query_target(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "address": "https://myhost.com:1825",
    "addressscheme": "streamrest",
    "createdon": "2018-12-22T03:59:18.563Z",
    "id": "cee10900-f54e-6eef-e455-bd7f15c4be32",
    "kind": "ts.target",
    "lastupdated": "2018-12-22T03:59:18.563Z",
    "name": "host:port target",
    "version": "1.0",
    "versionid": "f4be7c2b-059d-11e9-bec6-02420a4e1b0a"
  },
  {
    "address": "arn:aws:iam::252156542789:role/ThingSpace",
    "addressscheme": "streamawsiot",
    "createdon": "2019-01-24T19:06:43.577Z",
    "externalid": "lJZnih8BfqsosZrEEkfPuR3aGOk2i-HIr6tXN275ioJF6bezIrQB9EbzpTRep8J7RmV7QH==",
    "id": "cea170cc-a58f-6531-fc4b-fae1ceb1a6c8",
    "kind": "ts.target",
    "lastupdated": "2019-01-24T19:32:31.841Z",
    "name": "AWS Target",
    "region": "us-east-1",
    "version": "1.0",
    "versionid": "caf85ff7-200e-11e9-a85b-02420a621e0a"
  }
]
```


# Delete Target

Remove a target from a ThingSpace account.

```python
def delete_target(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteTargetRequest`](../../doc/models/delete-target-request.md) | Body, Required | The request body identifies the target to delete. |

## Response Type

`void`

## Example Usage

```python
body = DeleteTargetRequest()
body.accountidentifier = AccountIdentifier()
body.accountidentifier.billingaccountid = '0000000000-00001'
body.resourceidentifier = ResourceIdentifier()
body.resourceidentifier.id = '2e61a17d-8fd1-6816-e995-e4c2528bf535'

result = targets_controller.delete_target(body)
```


# Create Target

Define a target to receive data streams, alerts, or callbacks. After creating the target resource, use its ID in a subscription to set up a data stream.

```python
def create_target(self,
                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateTargetRequest`](../../doc/models/create-target-request.md) | Body, Required | The request body provides the details of the target that you want to create. |

## Response Type

[`Target`](../../doc/models/target.md)

## Example Usage

```python
body = CreateTargetRequest()
body.accountidentifier = AccountIdentifier()
body.accountidentifier.billingaccountid = '0000000000-00001'
body.billingaccountid = '0000000000-00001'
body.kind = 'ts.target'
body.address = 'https://your_IoT_Central_Application.azureiotcentral.com'
body.addressscheme = 'streamazureiot'
body.fields = CreateTargetRequestFields()
body.fields.httpheaders = FieldsHttpHeaders()
body.fields.httpheaders.authorization = 'SharedAccessSignature sr=d1f9b6bf-1380-41f6-b757-d9805e48392b&sig=EF5tnXClw3MWkb84OkIOUhMH%2FaS1DRD2nXT69QR8RD8%3D&skn=TSCCtoken&se=1648827260410'
body.fields.devicetypes = ['cHeAssetTracker', 'cHeAssetTrackerV2', 'tgAssetTracker', 'tgAssetTrackerV2']

result = targets_controller.create_target(body)
```

## Example Response *(as JSON)*

```json
{
  "address": "arn:aws:iam::252156542978:role/ThingSpace",
  "addressscheme": "streamawsiot",
  "billingaccountid": "1223334444-00001",
  "createdon": "2018-12-21T04:37:42.651Z",
  "externalid": "lJZnih8BfqsosZrEEkfPuR3aGOk2i-HIr6tXN275ioJF6bezIrQB9EbzpTRep8J7RmV7QH==",
  "id": "0e411230-c3eb-64dc-f5f4-1020364aa81f",
  "kind": "ts.target",
  "lastupdated": "2018-12-21T04:37:42.651Z",
  "name": "AWS Target",
  "region": "us-east-1",
  "version": "1.0",
  "versionid": "27aca5a4-04da-11e9-bff3-02420a5e1b0b"
}
```


# Generateanexternal ID

Create a unique string that ThingSpace will pass to AWS for increased security

:information_source: **Note** This endpoint does not require authentication.

```python
def generateanexternal_id(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GenerateExternalIDRequest`](../../doc/models/generate-external-id-request.md) | Body, Required | The request body only contains the authenticating account. |

## Response Type

[`GenerateExternalIDResult`](../../doc/models/generate-external-id-result.md)

## Example Usage

```python
body = GenerateExternalIDRequest()
body.accountidentifier = AccountIdentifier()
body.accountidentifier.billingaccountid = '0000000000-00001'

result = targets_controller.generateanexternal_id(body)
```

## Example Response *(as JSON)*

```json
{
  "externalid": "ZlJnih8BfqsosZrEEkfPuR3aGOk2i-HIr6tXN275ioJF6bezIrQB9EbzpTRep8J7RmV7QH=="
}
```

