
# Virtual Machine

## Structure

`VirtualMachine`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `repository` | [`EdgeServiceRepository`](../../doc/models/edge-service-repository.md) | Required | - |
| `revision` | [`Revision`](../../doc/models/revision.md) | Optional | - |
| `template_type` | [`TemplateTypeEnum`](../../doc/models/template-type-enum.md) | Required | type of the template to be used for deployment<br>**Default**: `'Terraform'` |
| `values` | [`EdgeServiceRepository`](../../doc/models/edge-service-repository.md) | Optional | - |
| `provider` | [`CloudProviderEnum`](../../doc/models/cloud-provider-enum.md) | Optional | Cloud provider where you plan to provision and operate your Kubernetes cluster |

## Example (as JSON)

```json
{
  "repository": {
    "endpoint": "https://charts.bitnami.com/bitnami",
    "name": "example-repo",
    "reacheability": "Internet",
    "type": "Git"
  },
  "templateType": "Terraform"
}
```

