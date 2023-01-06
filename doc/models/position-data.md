
# Position Data

Position data

## Structure

`PositionData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time` | `string` | Optional | time location obtained |
| `utcoffset` | `string` | Optional | utc offset of time |
| `x` | `string` | Optional | x coordinate of location |
| `y` | `string` | Optional | y coordinate of location |
| `radius` | `string` | Optional | radius of the location in meters |
| `qos` | `bool` | Optional | whether requested accurary is met |

## Example (as JSON)

```json
{
  "qos": false,
  "radius": "5571",
  "time": "20170520004421",
  "x": "33.45324",
  "y": "-84.59621"
}
```

