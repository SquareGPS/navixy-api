---
title: Assigning employee to tracker
description: API calls for assigning employee ("driver") to a device and reading who is already assigned.
---

# Assigning employee to tracker

Allows assigning employee ("driver") to a device. Also, read who is on a vehicle now, hardware key and when, where was
assigned.


## API actions

API base path: `/tracker/employee`.

### `assign`

Assigns another employee ("driver") to the tracker.

**required sub-user rights:** `employee_update`.
**required tariff feature:** `app_fleet`.

#### Parameters

| name            | description                                                                                     | type | format |
|:----------------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id      | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 123456 |
| new_employee_id | ID of the new employee.                                                                         | int  | 12345  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/employee/assign' \
        -H 'Content-Type: application/json' \
        -d '{"tracker_id": 123456, "new_employee_id": 12345, "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/employee/assign?tracker_id=123456&new_employee_id=12345&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Not found in the database - if there is no tracker or employee with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 263 – No change needed, old and new values are the same - if new employee matches a currently assigned employee.


### `read`

Requests to read the current employee (driver) assigned to tracker, and when it was assigned.

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 123456 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/employee/read' \
        -H 'Content-Type: application/json' \
        -d '{"tracker_id": 123456, "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/employee/read?tracker_id=123456&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

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
    "driver_license_issue_date": "2005-06-04",
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

* `current` - current employee (driver) info, standard employee object, can be `null`.
* `last_change` - information about the employee's last assignment, can be `null`.
    * `old_employee_id` - deprecated. Always `null`.
    * `new_employee_id` - ID of an employee assigned to the tracker. Can be `null`.
    * `location` - an address where it was. Can be `null`.
        * `lat` - latitude.
        * `lng` - longitude.
        * `address` - an address where it was. Can be `null`.
    * `origin` - `supervisor` (if the assignment was made through the [API](#assign)) or `tracker`
      (if the assignment was made through the hardware/driver key).
    * `hardware_key` - hardware key used to change employee.

#### Errors

* 201 – Not found in the database - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
