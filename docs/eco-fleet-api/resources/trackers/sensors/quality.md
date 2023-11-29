---
title: Fuel Sensor Quality Index
description: Contains API calls to interact with fuel sensor quality index.
---

# Fuel Sensor Quality Index

Contains API calls to interact with fuel sensor quality index.

## Resource

`/trackers/$tracker_id/sensors/$sensor_id/quality`.

### GET

Returns given fuel sensor quality index calculated based on sensor readings in a given datetime period.

#### parameters

| name     | description                                                                      | type      |
|:---------|:---------------------------------------------------------------------------------|:----------|
| interval | Sensor readings' datetime interval which will be analyzed. Last week by default. | interval? |

#### examples

```shell
curl -X GET 'https://api.navixy.com/eco_fleet/v1/trackers/123/sensors/321/quality?interval=P7D/2020-12-31T00:00Z' \
    -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
```

#### response

```json
{
    "smoothness": 8.29
}
```

* `smoothness` - a smoothness `score` of the given sensor's readings. Greater values mean less noise in readings sent by the sensor and vice versa.

##### types

| Name  | Description                    | JSON type | Restrictions     |
|-------|--------------------------------|-----------|------------------|
| Score | An abstract measurement score. | number    | \>=1.0 && <=10.0 |


#### errors

* `errors/entity/not-found` - Entity not found. Thrown if sensor or calibration table is missing.
* `errors/external-api/navixy` - Error accessing Navixy API. See `detail` field and consult Backend API documentation.
* `errors/sensors/quality/not-enough-readings` - Not enough sensor readings in given interval. Try using interval with enough vehicle usage or changing readings' sending frequency and waiting for data accumulation.
