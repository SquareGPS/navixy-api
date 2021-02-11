---
title: Working with employees
description: Working with employees
---

# Working with employees

Employees used to represent people working at one's organization. They can be linked with other entities such as 
trackers, vehicles, places, etc.

## Employee object

```json
{
    "id": 222,
    "tracker_id": null,
    "first_name": "John",
    "middle_name": "Jane",
    "last_name": "Smith",
    "email": "smith@example.com",
    "phone": "442071111111",
    "driver_license_number": "SKIMP407952HJ9GK 06",
    "driver_license_cats": "C",
    "driver_license_valid_till": "2018-01-01",
    "hardware_key": null,
    "icon_id" : 55,
    "avatar_file_name": null,
    "department_id": null,
    "location": {
        "lat": 52.5,
        "lng": 13.4,
        "address": "Engeldamm 18"
    },
    "personnel_number": "1059236",
    "tags": [1,2]
}
```

* `id` - int. Internal ID. Can be passed as null only for "create" action.
* `tracker_id` - int. An id of the tracker currently assigned to this employee. `null` means no tracker assigned.
* `first_name` - string. First name. Cannot be empty. Max 100 characters.
* `middle_name` - string. Middle name. Can be empty, cannot be null. Max 100 characters.
* `last_name` - string. Last name. Can be empty, cannot be null. Max 100 characters.
* `email` - string. Employee's email. Must be valid email address. Can be empty, cannot be null. Max 100 characters.
* `phone` - string. Employee's phone without "+" sign. Can be empty, cannot be null. Max 32 characters.
* `driver_license_number` - string. Driver license number. Can be empty, cannot be null. Max 32 characters.
* `driver_license_cats` - string. Driver license categories. Max 32 characters.
* `driver_license_valid_till` - string date (yyyy-MM-dd). Date till a driver license valid. Can be null.
* `hardware_key` - string. A hardware key. Can be null. Max 64 characters.
* `icon_id` - int. An icon id. Can be null, can only be updated via [avatar/assign](./avatar.md#assign).
* `avatar_file_name` - string. A name of the updated avatar file. Nullable, can only be updated 
via [avatar/upload](./avatar.md#upload).
* `department_id` - int. An id of the department to which employee assigned. Can be null.
* `location` - optional object. Location associated with this employee, should be valid or null.
    * `address` - string. Address of the location.
* `personnel_number` - optional string. Max length is 15.
* `tags` - int array. List of tag ids.

## API actions

API base path: `/employee`.

### list

Gets all employees belonging to user.

#### response

```json
{
    "success": true,
    "list": [<employee>]
}
```

* `list` - a list of employee objects.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/employee/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/employee/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### errors

[General](../../../getting-started.md#error-codes) types only.

### create

Creates a new employee.

**required sub-user rights**: `employee_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| employee | An [employee object](#employee-object) without `id` field. Non-null. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/employee/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "employee": {"tracker_id": 625987, "first_name": "John", "middle_name": "Jane", "last_name": "Smith", "email": "smith@example.com", "phone": "442071111111", "driver_license_number": "SKIMP407952HJ9GK 06", "driver_license_cats": "C", "driver_license_valid_till": "2018-01-01", "hardware_key": null, "icon_id" : 55, "avatar_file_name": null, "department_id": null, "location": {"lat": 52.5, "lng": 13.4, "address": "Engeldamm 18"}, "personnel_number": "1059236", "tags": [1,2]}'
    ```

#### response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An id of the created employee.

#### errors

* 247 – Entity already exists, if `tracker_id`!=null and exists an employee that already bound to this `tracker_id`.

### read

Gets employee by its id.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| employee_id | Id of an employee. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/employee/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "employee_id": 111}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/employee/read?hash=a6aa75587e5c59c32d347da438505fc3&employee_id=111
    ```

#### response

```json
{
    "success": true,
    "value": {
     "id": 222,
     "tracker_id": null,
     "first_name": "John",
     "middle_name": "Jane",
     "last_name": "Smith",
     "email": "smith@example.com",
     "phone": "442071111111",
     "driver_license_number": "SKIMP407952HJ9GK 06",
     "driver_license_cats": "C",
     "driver_license_valid_till": "2018-01-01",
     "hardware_key": null,
     "icon_id" : 55,
     "avatar_file_name": null,
     "department_id": null,
     "location": {
         "lat": 52.5,
         "lng": 13.4,
         "address": "Engeldamm 18"
     },
     "personnel_number": "1059236",
     "tags": [1,2]
 }
}
```

* `value` - an employee object.

#### errors

* 201 – Not found in the database (if there is no employee with such an id).

### update

Updates existing employee.

**required sub-user rights**: `employee_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| employee | An [employee object](#employee-object) with `id` field. Non-null. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/employee/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "employee": {"employee_id": 111, "tracker_id": 625987, "first_name": "John", "middle_name": "Jane", "last_name": "Smith", "email": "smith@example.com", "phone": "442071111111", "driver_license_number": "SKIMP407952HJ9GK 06", "driver_license_cats": "C", "driver_license_valid_till": "2018-01-01", "hardware_key": null, "icon_id" : 55, "avatar_file_name": null, "department_id": null, "location": {"lat": 52.5, "lng": 13.4, "address": "Engeldamm 18"}, "personnel_number": "1059236", "tags": [1,2]}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no employee with such an id).
* 247 – Entity already exists, if `tracker_id`!=null and exists an employee that already bound to this `tracker_id`.

### delete

Deletes an employee with the specified id.

**required sub-user rights**: `employee_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| employee_id | Id of an employee to delete. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/employee/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "employee_id": 111}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/employee/delete?hash=a6aa75587e5c59c32d347da438505fc3&employee_id=111
    ```
    
#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no employee with such an id).

### batch_convert

Convert batch of tab-delimited employees and return list of checked employees with errors.

**Required sub-user rights:** `employee_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| batch | Batch of tab-delimited employees. | string |
| file_id | Preloaded file ID. | string |
| fields | Optional. Array of field names. Default is `["first_name", "middle_name", "last_name", "email", "phone"]`. | string array |
| geocoder | Geocoder type. | string |
| default_radius | Optional. Radius for point in meters. Default is 100. | int |

* If `file_id` is set – `batch` parameter will be ignored.

#### response

```json
{
    "success": true,
    "list": [{
      "success": true,
      "value": {
        "id": 222,
        "tracker_id": null,
        "first_name": "John",
        "middle_name": "Jane",
        "last_name": "Smith",
        "email": "smith@example.com",
        "phone": "442071111111",
        "driver_license_number": "SKIMP407952HJ9GK 06",
        "driver_license_cats": "C",
        "driver_license_valid_till": "2018-01-01",
        "hardware_key": null,
        "icon_id": 55,
        "avatar_file_name": null,
        "department_id": null,
        "location": {
          "lat": 52.5,
          "lng": 13.4,
          "address": "Engeldamm 18"
        },
        "personnel_number": "1059236",
        "tags": [
          1,
          2
        ],
        "errors": <array_of_objects>
      }
    }],
    "limit_exceeded": false    
}
```

* `list` - list of checked employees.
    * `errors` - optional array of errors.
* `limit_exceeded` - boolean. `true` if given batch constrained by a limit.

#### errors

* 234 - (Invalid data format).
