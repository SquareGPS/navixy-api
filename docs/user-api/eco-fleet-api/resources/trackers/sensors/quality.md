---
title: Fuel Sensor Quality Index
description: Contains API calls to interact with fuel sensor quality index.
---

# Fuel Sensor Quality Index

Contains API calls to interact with fuel sensor quality index.

## Resource

Resource path: `/trackers/$tracker_id/sensors/$sensor_id/quality`.

### GET

Returns the fuel sensor quality index calculated from sensor readings within a specified datetime period.

#### Parameters

| name       | description                                                                      | type      |
|:-----------|:---------------------------------------------------------------------------------|:----------|
| tracker_id | ID of the tracker which has the sensor.                                          | integer   |
| sensor_id  | ID of the sensor to analyze.                                                     | integer   |
| interval   | Sensor readings' datetime interval which will be analyzed. Last week by default. | interval  |

#### Examples

```shell
curl -X GET '{{ extra.eco_fleet_api_example_url }}/trackers/123/sensors/321/quality?interval=P7D/2020-12-31T00:00Z' \
    -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
```

#### Response

```json
{
    "smoothness": 8.29
}
```

* `smoothness` - a smoothness score of the sensor readings. Higher values indicate reduced noise in sensor readings, while lower values suggest increased noise.

##### Types

| Name  | Description                    | JSON type | Restrictions     |
|-------|--------------------------------|-----------|------------------|
| Score | An abstract measurement score. | number    | \>=1.0 && <=10.0 |


#### Errors

* `errors/entity/not-found` - Entity not found. Thrown if sensor or calibration table is missing.
* `errors/external-api/navixy` - Error accessing Navixy API. See `detail` field and consult [Backend API documentation](../../../../backend-api/getting-started/errors.md).
* `errors/sensors/quality/not-enough-readings` - Not enough sensor readings in given interval. Try using interval with enough vehicle usage or changing readings' sending frequency and waiting for data accumulation.
