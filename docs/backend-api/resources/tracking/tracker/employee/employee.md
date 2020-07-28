---
title: /employee
description: /employee
---

## assign()
Assign another employee (“driver”) to this tracker

**required subuser rights:** employee_update
**required tariff feature:** app_fleet

#### parameters:
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **new_employee_id** - **int**. Id of the new employee.

#### return:

```json
{ "success": true }
```

#### errors:
*   201 – Not found in database (if there is no tracker or employee with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   263 – No change needed, old and new values are the same (if new employee matches currently assigned employee)

## read()
Request to read the current employee assigned to tracker, and when it was assigned.

#### parameters:
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### return:
```js
{
  "success": true,
  "current": { //current employee info, standard employee object, CAN BE NULL
    "id": 1,
    "icon_id": 55,
    "tracker_id": 560,
    "first_name": "John",
    "middle_name": "M",
    "last_name": "Johnson",
    "email": "",
    "phone": "",
    "driver_license_number": "34534545",
    "driver_license_cats": "AB, sgeg",
    "driver_license_valid_till": "2015-06-04",
    "hardware_key": "ab8def",
    "department_id": null,
    "location": {
      "lat": 0.0,
      "lng": 0.0,
      "address": ""
    }
  },
  "last_change": { //information about when did last change occur, MAY BE NULL
    "id": 25,
    "old_employee_id": null, //can be null
    "new_employee_id": 1, //can be null
    "location": { //where did ths
      "lat": 11.0,
      "lng": 22.0,
      "address": "Haraze-Mangueigne"
    },
    "changed": "2016-11-17 17:01:20",
    "origin": "tracker", //"supervisor" or "tracker"
    "hardware_key": "ab8def" //hardware key used to change driver
  }
}
```

#### errors:
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

