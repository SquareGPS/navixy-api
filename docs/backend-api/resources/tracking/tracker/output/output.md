---
title: /output
description: /output
---

## set_all()
Request to change the states of all digital outputs of the device. The device must be online.

**required subuser rights:** tracker_set_output

#### parameters:
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **outputs** - **array of boolean**. Array of desired states of all digital outputs, e.g. [true, true, false] means output 1 is on, output 2 is on, output 3 is off

#### return:
```json
{ "success": true }
```

#### errors:
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   213 – Cannot perform action: the device is offline (if corresponding tracker is not connected to the server)
*   214 – Requested operation or parameters are not supported by the device (if device does not support batch mode, or has a different number of outputs)
*   219 – Not allowed for clones of the device (if tracker is clone)

## set()
Request to change the state of the specified digital output of the device. The device must be online.

**required subuser rights:** tracker_set_output

#### parameters:
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **output** - **int**. The number of the output to control, starting from 1.
* **enable** - **boolean**. True if the requested output should be enabled, or false if it should be disabled..

#### return:
```json
{ "success": true }
```

#### errors:
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   213 – Cannot perform action: the device is offline (if corresponding tracker is not connected to the server)
*   214 – Requested operation or parameters are not supported by the device (if device does not support controlling single output, does not have specified digital output, or the specified output is reserved to “engine block” feature. In this case, output cannot be controlled by this command for safety reasons.)
*   219 – Not allowed for clones of the device (if tracker is clone)

