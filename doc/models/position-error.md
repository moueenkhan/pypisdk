
# Position Error

Position error

## Structure

`PositionError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time` | `string` | Optional | time location obtained |
| `utcoffset` | `string` | Optional | utc offset of time |
| `mtype` | `string` | Optional | error type returned from location server |
| `info` | `string` | Optional | additional information about the error |

## Example (as JSON)

```json
{
  "time": "20170525214342",
  "type": "POSITION METHOD FAILURE",
  "info": "Exception code=ABSENT SUBSCRIBER"
}
```

