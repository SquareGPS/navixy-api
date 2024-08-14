---
title: Fuel data resampling
---

# Fuel data resampling
!!! note "Navixy Eco Fleet Lab has developed a solution for complex fuel data analysis. This method regenerates data sets which will be beneficial for variety of exercises, enabling researchers, developers, and diagnostics experts to leverage the **processed data**."

**Diagnostic process** is an important procedure undertaken by numerous partners and investigators. Its primary purpose is to identify the underlying causes, which is essential for efficient fuel management by identifying any abnormalities. For example, they analyze key events - drains and refueling for fraud or look for a reason for the appearance of noise in the fuel data.

When partners or integrators incorporate fuel-related data into third-party systems for **further analysis and processing, including machine learning**, it can be highly effective in identifying behavioral patterns and detecting exceptions. This allows for more efficient investigations and enhances overall data processing capabilities.

Effective data management relies on **accurate and synchronized raw data**. However, inconsistencies in different data sets (i.e. position, speed, and fuel level) across various timeframes can pose challenges.

To tackle the challenges posed by incomplete or inconsistent data, we utilize advanced statistical models. With our API requests, you can easily **access and download processed datasets** from our platform for specific time periods. This API request specifically provides fuel-related data in a convenient CSV format.

!!! note "**Data resampling** refers to the joint process of creating a uniform data structure by organizing existing values and generating new ones (for missing values) in a chronological order, while considering equal time intervals. This approach ensures data integrity and facilitates analysis."

## data_resampling
### Description

The API response is presented in a convenient CSV format, incorporating columns below:

* Time - timestamp (depending on the timezone the tracker is located)
* [FUEL_SENSOR_NAME] - Fuel level (The column name is derived based on the sensor name. There could be more than 1 column)
* SPEED - object speed (km/h)
* MOVEMENT - movement status (0 - parking, 1 - moving, 2 - Idle)
* LNG - Longitude
* LAT - Latitude

**API path:** `/trackers/$tracker_id/resampling`
### Parameters

Standard list

| name             | description                                                                                      | type             | format                                            |
|:-----------------|:-------------------------------------------------------------------------------------------------|:-----------------|---------------------------- ----------------------|
| hash             | Hash of an API key is required for API calls to identify user.                                   | string           | "NVX c459c3589336ebf26ff18257a8d93a45"            |
| tracker_id       | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.  | int              | 123456                                            |
| interval         | Sensor readings' datetime interval which will be analyzed. Last week by default.                 | interval         | 2023-08-24T08:04:36.306Z/2023-08-26T08:04:36.306Z |
| step_size        | Resampling step in minutes                                                                       | int              | 1                                                 | 
| resampling_props | Array of data resampling parameters for various data types                                       | resampling_props | array                                             |

Additional list of resampling parameters

| name              | description                                                                                              | type   | format      |
|:------------------|:---------------------------------------------------------------------------------------------------------|:-------|-------------|
| data_type         | Data type. Options: FUEL, SPEED,MOVEMENT, LNG, LAT                                                       | string | "SPEED"     |
| resampling_method | Resampling method.  Options: FOLLOWING, PREVIOUS, MEDIAN_IN_WINDOW, AVERAGE_IN_WINDOW, AVERAGE.          | string | "FOLLOWING" |
| delta             | Delta time in seconds. Has different meaning for different algorithms.                                   | int    | null/1      |
| fixed_value       | A fixed value that will be used if no data is found in the interval. You can specify null or any number. | float  | nulll/5.5   |

##### Description of resampling_method

* FOLLOWING - In this series, the subsequent value is utilized to substitute any missing values. Consequently, neighboring missing values are all substituted with the subsequent valid value. If there are any missing values at the end of the series, they are replaced with the preceding valid value. If delta is not null than algorithm changes: if the time interval [T-Δ, T+0] contains at least one value, otherwise fixed_value.
* PREVIOUS - The previous value in the series is utilized to substitute missing values. Consequently, the neighboring missing values are replaced with the earliest preceding valid value. If delta is not null than algorithm changes: if the time interval [T-0, T+Δ] contains at least one value, otherwise fixed_value.
* MEDIAN_IN_WINDOW - In this algorithm, the presence of delta is imperative. The average of all the neighboring values in the series within the interval [T-Δ, T+Δ], fixed_value if no values.
* AVERAGE_IN_WINDOW- In this algorithm, the presence of delta is imperative. The median of all the neighboring values in the series within the interval [T-Δ, T+Δ], fixed_value if no values.
* AVERAGE - To replace missing values in a series, we use the average of the two neighboring values. For any missing values between valid ones, we replace them with the average of the surrounding valid values. If the series begins or ends with missing values, we substitute them with the next or previous valid value accordingly. If delta is not equal to null than algorithm changes: if the interval [T-Δ, T+Δ] contains at least one value, otherwise fixed_value.

!!! note "We recommend utilizing distinct methods for varying data types, as outlined in the table below. However, the choice of which methods to employ ultimately depends on your individual needs and expectations."

| Method     | Data type            | Use case                                                                               |
|:-----------|:---------------------|:---------------------------------------------------------------------------------------|
| Following  | Ordered              | Data that is missing at the end of a time series or sequence, i.e Fuel, Movement       |
| Previous   | Ordered              | Data that is missing at the beginning of a time series or sequence, i.e Fuel, Movement |
| Median     | Evenly distributed   | Data that is not normally distributed, i.e. Fuel, Speed                                |
| Average    | Normally distributed | Data that is not evenly distributed, i.e. Fuel, Speed                                  |

### Example

```shell
curl -X 'POST' \
  '{{ extra.eco_fleet_api_example_url }}/trackers/12345/resampling?interval=P7D/2020-12-31T00:00Z' \
  -H 'accept: text/csv' \
  -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
  -H 'Content-Type: application/json' \
  -d '{
  "step_size": 1,
  "resampling_props": [
    {
      "data_type": "FUEL",
      "resampling_method": "PREVIOUS",
      "delta": 600,
      "fixed_value": null
    },
    {
      "data_type": "SPEED",
      "resampling_method": "PREVIOUS",
      "delta": null,
      "fixed_value": null
    },
    {
      "data_type": "MOVEMENT",
      "resampling_method": "PREVIOUS",
      "delta": null,
      "fixed_value": null
    },
    {
      "data_type": "LNG",
      "resampling_method": "PREVIOUS",
      "delta": null,
      "fixed_value": null
    },
    {
      "data_type": "LAT",
      "resampling_method": "PREVIOUS",
      "delta": null,
      "fixed_value": null
    }
  ]
}'
```

#### Response

```csv
Time,Fuel level,SPEED,MOVEMENT,LNG,LAT
2023-08-24T08:04,132.85823,38.0,1,37.68325,55.580612
2023-08-24T08:05,132.85823,38.0,1,37.68325,55.580612
2023-08-24T08:06,131.57695,38.0,1,37.68325,55.580612
2023-08-24T08:07,128.12737,38.0,1,37.68325,55.580612
2023-08-24T08:08,130.59135,38.0,1,37.68325,55.580612
```

### Errors
* 204 - Entity not found – if there is no tracker with such ID belonging to authorized user.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.