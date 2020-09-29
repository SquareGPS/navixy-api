---
title: Sensor calibration data
description: Sensor calibration data
---

# Sensor calibration data

API path: `/tracker/sensor/calibration_data`.

### read

Gets calibration data for sensor.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| sensor_id | Id of the sensor. | int | 12345 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/calibration_data/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456", "sensor_id": "12345"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/sensor/calibration_data/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&sensor_id=12345
    ```

#### response

```json
{
    "success": true,
    "value": [{"in":0.0,"out":0.0},{"in":0.7,"out":60.0}]
}
```

* `value` - list of objects containing calibration data. 

#### errors

* 201 – Not found in the database (if there is no tracker with such id belonging to authorized user).
* 228 – Not supported by the sensor (if sensor doesn't support calibration).

### update

Replaces the calibration data for a sensor.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| sensor_id | Id of the sensor. | int | 12345 |
| data | Array of calibration data objects. | array of JSON object  | `[{“in”:0.0,”out”:0.0},{“in”:0.7,”out”:60.0}]` |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/calibration_data/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456", "sensor_id": "12345", "data": [{“in”:0.0,”out”:0.0},{“in”:0.7,”out”:60.0}]}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no tracker with such id belonging to authorized user).
* 228 – Not supported by the sensor (if sensor doesn't support calibration).
* 228 – Not supported by the sensor (if sensor doesn't support calibration).
* 219 – Not allowed for clones of the device (if tracker is clone).

### upload_omnicomm

Replaces the calibration data for a sensor from Omnicomm LLSmonitor's XML configuration file.
If XML file contains information about multiple sensors, user must specify which sensor number to use.

**required sub-user rights:** `tracker_update`

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being an XML file upload 
(with the name “file”).

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int |
| sensor_id | Id of the sensor. | int |
| file | A file upload containing LLSmonitor XML file. | file upload |

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no tracker with such id belonging to authorized user).
* 228 – Not supported by the sensor (if sensor doesn't support calibration).
* 219 – Not allowed for clones of the device (if tracker is clone).
* 233 – No data file (if file part is missing).
* 234 – Invalid data format (if supplied file is not a valid LLSmonitor XML file).
* 235 – Missing calibration data (if there is no calibration data for the specified sensor number).

