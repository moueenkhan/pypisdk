
# Eds Discovery Intent

## Structure

`EdsDiscoveryIntent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ue_identity` | `string` | Optional | ueIdentity to discover EDS location service<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `ue_identity_type` | [`UEIdentityTypeEnum`](../../doc/models/ue-identity-type-enum.md) | Optional | default ueIdentityType type<br>**Default**: `'IPAddress'` |

## Example (as JSON)

```json
{
  "ueIdentity": null,
  "ueIdentityType": null
}
```

