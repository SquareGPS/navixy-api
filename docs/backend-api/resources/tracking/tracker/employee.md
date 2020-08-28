---
title: Assigning employee to tracker
description: Assigning employee to tracker
---

# Assigning employee to tracker

API base path: `/tracker/employee`

Allows to assign employee ("driver") to a device. Also, read who is on a vehicle now, hardware key and when, where was assigned. 

### assign

Assigns another employee (“driver”) to the tracker.

**required sub-user rights:** `employee_update`
**required tariff feature:** `app_fleet`

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| new_employee_id | Id of the new employee. | int | 12345 |

#### examples

=== cURL

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/employee/assign' \
        -H 'Content-Type: application/json' \ 
        -d '{"tracker_id": "123456", "new_employee_id": "12345", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== HTTP GET

    ```
    {{ extra.api_example_url }}/tracker/employee/assign?tracker_id=123456&new_employee_id=12345&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no tracker or employee with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
* 263 – No change needed, old and new values are the same (if new employee matches a currently assigned employee).

### read

Requests to read the current employee assigned to tracker, and when it was assigned.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |

#### examples

=== cURL

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/employee/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"tracker_id": "123456", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== HTTP GET

    ```
    {{ extra.api_example_url }}/tracker/employee/read?tracker_id=123456&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
  "success": true,
  "current": {
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
  "last_change": {
    "id": 25,
    "old_employee_id": null,
    "new_employee_id": 1,
    "location": {
      "lat": 11.0,
      "lng": 22.0,
      "address": "Haraze-Mangueigne"
    },
    "changed": "2016-11-17 17:01:20",
    "origin": "tracker",
    "hardware_key": "ab8def"
  }
}
```

* `current` - current employee info, standard employee object, CAN BE NULL.
* `last_change` - information about when did last change occur, MAY BE NULL.
* `old_employee_id` - can be null.
* `new_employee_id` - can be null.
* `location` - where it was.
* `origin` - `supervisor` or `tracker`.
* `hardware_key` - hardware key used to change driver.

#### errors

* 201 – Not found in the database (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
