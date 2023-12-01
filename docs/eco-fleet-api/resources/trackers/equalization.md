---
title: Tracker's data equalization
description: Contains API calls to interact with trackers's data.
---

# Tracker's data equalization

Contains API calls to interact with trackers's data.

## Resource

`/trackers/$tracker_id/equalization`.

### POST

This method allows to retrieve some data on trackers and fuel sensors. The response is presented in a convenient CSV table format, incorporating columns below:

`Time` - timestamp (depending on the timezone the tracker is located)

`SPEED` - object speed (km/h)

`MOVEMENT` - movement status (0 - parking, 1 - moving, 2 - Idle)

`LNG` - longitude

`LAT` - latitude

[FUEL_SENSOR_NAME] - Raw Fuel level (The column name is derived based on the sensor name. There could be more than 1 column)

#### parameters

| name               | description                                                                      | type              |
|:-------------------|:---------------------------------------------------------------------------------|:------------------|
| interval           | Sensor readings' datetime interval which will be analyzed. Last week by default. | interval          |
| step_size          | Equalization step in minutes                                                     | int               |
| equalization_props | Array of data equalization parameters for various data types                   | equalization_prop |

#### Additional list of equalization parameters

| name                | description                                                                                             | JSON type |
|:--------------------|:--------------------------------------------------------------------------------------------------------|:----------|
| data_type           | Data type. Options: FUEL, SPEED,MOVEMENT, LNG, LAT                                                      | string    |
| equalization_method | Equalization method. Options: FOLLOWING, PREVIOUS, MEDIAN_IN_WINDOW, AVERAGE_IN_WINDOW, AVERAGE         | string    |
| delta               | Delta time in seconds. Has different meaning for different algorithms                                   | int       |
| fixed_value         | A fixed value that will be used if no data is found in the interval. You can specify null or any number | number    |

#### Description of equalization_method

`FOLLOWING` -  In this series, the subsequent value is utilized to substitute any missing values. Consequently, neighboring missing values are all substituted with the subsequent valid value. If there are any missing values at the end of the series, they are replaced with the preceding valid value. If delta is not null than algorithm changes: if the time interval [T-Δ, T+0] contains at least one value, otherwise fixed_value.

`PREVIOUS` - The previous value in the series is utilized to substitute missing values. Consequently, the neighboring missing values are replaced with the earliest preceding valid value. If delta is not null than algorithm changes: if the time interval [T-0, T+Δ] contains at least one value, otherwise fixed_value.

`MEDIAN_IN_WINDOW` - In this algorithm, the presence of delta is imperative. The average of all the neighboring values in the series within the interval [T-Δ, T+Δ], fixed_value if no values

`AVERAGE_IN_WINDOW `- In this algorithm, the presence of delta is imperative. The median of all the neighboring values in the series within the interval [T-Δ, T+Δ], fixed_value if no values

`AVERAGE` - To replace missing values in a series, we use the average of the two neighboring values. For any missing values between valid ones, we replace them with the average of the surrounding valid values. If the series begins or ends with missing values, we substitute them with the next or previous valid value accordingly. If delta is not equal to null than algorithm changes: if the interval [T-Δ, T+Δ] contains at least one value, otherwise fixed_value.

#### examples

```shell
curl -X 'POST' \
  'https://api.navixy.com/eco_fleet/v1/trackers/12345/data_equalization?interval=P7D/2020-12-31T00:00Z' \
  -H 'accept: text/csv' \
  -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
  -H 'Content-Type: application/json' \
  -d '{
  "step_size": 1,
  "equalization_props": [
    {
      "data_type": "FUEL",
      "equalization_method": "PREVIOUS",
      "delta": 600,
      "fixed_value": null
    },
    {
      "data_type": "SPEED",
      "equalization_method": "PREVIOUS",
      "delta": null,
      "fixed_value": null
    },
    {
      "data_type": "MOVEMENT",
      "equalization_method": "PREVIOUS",
      "delta": null,
      "fixed_value": null
    },
    {
      "data_type": "LNG",
      "equalization_method": "PREVIOUS",
      "delta": null,
      "fixed_value": null
    },
    {
      "data_type": "LAT",
      "equalization_method": "PREVIOUS",
      "delta": null,
      "fixed_value": null
    }
  ]
}'
```

#### response

```csv
Time,Fuel level,SPEED,MOVEMENT,LNG,LAT
2023-08-24T08:04,132.85823,38.0,1,37.68325,55.580612
2023-08-24T08:05,132.85823,38.0,1,37.68325,55.580612
2023-08-24T08:06,131.57695,38.0,1,37.68325,55.580612
2023-08-24T08:07,128.12737,38.0,1,37.68325,55.580612
2023-08-24T08:08,130.59135,38.0,1,37.68325,55.580612
```

#### errors

* `errors/entity/not-found` - Entity not found. Thrown if tracker table is missing.
* `errors/external-api/navixy` - Error accessing Navixy API. See `detail` field and consult Backend API documentation.