---
title: /calibration_data
description: /calibration_data
---

## read()
Get calibration data for sensor.

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **sensor_id** - **int**. Id of the sensor.

#### return
```javascript
{
    "success": true,
    "value": [<object>, ...] // List of objects containing calibration data, e.g. [{"in":0.0,"out":0.0},{"in":0.7,"out":60.0}]
}
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   228 – Not supported by the sensor (if sensor doesn’t support calibration)

## update()
Replaces the calibration data for sensor.

**required subuser rights:** tracker_update

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **sensor_id** - **int**. Id of the sensor.
* **data** - **array of JSON object**. Array of calibration data objects, e.g. [{“in”:0.0,”out”:0.0},{“in”:0.7,”out”:60.0}]

#### return

```json
{ "success": true }
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   228 – Not supported by the sensor (if sensor doesn’t support calibration)
*   219 – Not allowed for clones of the device (if tracker is clone)

## upload_omnicomm()
Replaces the calibration data for sensor from Omnicomm LLSmonitor’s XML configuration file.
If XML file contains information about multiple sensors, user must specify which sensor number to use.

**required subuser rights:** tracker_update

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being an XML file upload (with the name “file”).

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **sensor_id** - **int**. Id of the sensor.
* **sensor_number** - **int**. Optional. A number of the sensor in XML file (starting at 1).
* **file** - **file upload**. A file upload containing LLSmonitor XML file

#### return

```json
{ "success": true }
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   228 – Not supported by the sensor (if sensor doesn’t support calibration)
*   219 – Not allowed for clones of the device (if tracker is clone)
*   233 – No data file (if file part is missing)
*   234 – Invalid data format (if supplied file is not a valid LLSmonitor XML file)
*   235 – Missing calibration data (if there is no calibration data for the specified sensor number)

