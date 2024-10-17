---
title: Working with employees and drivers
description: Employee object and API calls to work with. Employees (drivers) used to represent people working at one's organization. They can be linked with other entities such as trackers, vehicles, places, etc.
---

# Working with employees and drivers

Employees and drivers used to represent people working at one's organization. They can be linked with other entities such as 
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
    "driver_license_issue_date": "2008-01-01",
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
    "ssn": "123-45-6789",
    "tags": [1,2]
}
```

* `id` - int. Internal ID. Can be passed as null only for "create" action.
* `tracker_id` - int. An ID of the tracker currently assigned to this employee or driver. `null` means no tracker assigned.
* `first_name` - string. First name. Cannot be empty. Max 100 characters.
* `middle_name` - string. Middle name. Can be empty, cannot be null. Max 100 characters.
* `last_name` - string. Last name. Can be empty, cannot be null. Max 100 characters.
* `email` - string. Employee's email. Must be valid email address. Can be empty, cannot be null. Max 100 characters.
* `phone` - string. Employee's phone without "+" sign. Can be empty, cannot be null. Max 32 characters.
* `driver_license_number` - string. Driver license number. Can be empty, cannot be null. Max 32 characters.
* `driver_license_cats` - string. Driver license categories. Max 32 characters.
* `driver_license_issue_date` - string date (yyyy-MM-dd). Issue date of a driver license. Can be null.
* `driver_license_valid_till` - string date (yyyy-MM-dd). Date till a driver license valid. Can be null.
* `hardware_key` - string. A hardware key. Can be null. Max 64 characters.
* `icon_id` - int. An icon ID. Can be null, can only be updated via [avatar/assign](avatar.md#assign).
* `avatar_file_name` - string. A name of the updated avatar file. Nullable, can only be updated 
via [avatar/upload](avatar.md#upload).
* `department_id` - int. An ID of the department to which employee assigned. Can be null.
* `location` - optional object. Location associated with this employee, should be valid or null.
    * `address` - string. Address of the location.
* `personnel_number` - optional string. Max length is 15.
* `ssn` - optional string. Social Security number. Max length is 32.
* `tags` - int array. List of tag IDs.


## API actions

API base path: `/employee`.

### `list`

Gets all employees and drivers belonging to user.

#### Parameters

| name   | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | type         |
|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| limit  | Pagination. Maximum number of employee records to return.                                                                                                                                                                                                                                                                                                                                                                                                                                              | int          |
| offset | Pagination. Get employee records starting from.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | int          |
| sort   | Optional. Set of sort options. Each option is a pair of property name and sorting direction, e.g. `["first_name=desc","object_label=asc"]`. Maximum 2 options in request. Available properties:<br/> - ID<br/> - first_name<br/> - object_label<br/> - department_label<br/> - personnel_number<br/> - hardware_key<br/> - phone<br/> - email<br/> - address<br/> - driver_license_number<br/> - driver_license_cats<br/> - driver_license_valid_till<br/> - driver_license_valid_till<br/> - ssn<br/> | string array |
| filter | Get a list of employees filtered by properties, at least one property must contain the desired string. All properties from the sorting list are used in filtering. Maximum 100 characters or null.                                                                                                                                                                                                                                                                                                     | string       |

#### Examples

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

#### Response

```json
{
    "success": true,
    "list": [<employee>],
    "count": 12
}
```

* `list` - a list of employees.
* `count` - int. Total number of employees (ignoring offset and limit).

#### Errors

[General](../../../getting-started/errors.md#error-codes) types only.


### `create`

Creates a new employee/driver.

**required sub-user rights**: `employee_update`.

#### Parameters

| name     | description                                                          | type        |
|:---------|:---------------------------------------------------------------------|:------------|
| employee | An [employee object](#employee-object) without `id` field. Non-null. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/employee/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "employee": {"tracker_id": 625987, "first_name": "John", "middle_name": "Jane", "last_name": "Smith", "email": "smith@example.com", "phone": "442071111111", "driver_license_number": "SKIMP407952HJ9GK 06", "driver_license_cats": "C", "driver_license_valid_till": "2018-01-01", "hardware_key": null, "icon_id" : 55, "avatar_file_name": null, "department_id": null, "location": {"lat": 52.5, "lng": 13.4, "address": "Engeldamm 18"}, "personnel_number": "1059236", "tags": [1,2]}'
    ```

#### Response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An ID of the created employee (driver).

#### Errors

* 247 – Entity already exists, if `tracker_id`!=null and exists an employee that already bound to this `tracker_id`.


### `read`

Gets employee/driver by his ID.

#### Parameters

| name        | description        | type |
|:------------|:-------------------|:-----|
| employee_id | ID of an employee. | int  |

#### Examples

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

#### Response

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
     "driver_license_issue_date": "2008-01-01",
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
     "ssn": "123-45-6789",
     "tags": [1,2]
 }
}
```

* `value` - an employee object.

#### Errors

* 201 – Not found in the database - if there is no employee/driver with such an ID.


### `update`

Updates existing employee/driver.

**required sub-user rights**: `employee_update`.

#### Parameters

| name     | description                                                       | type        |
|:---------|:------------------------------------------------------------------|:------------|
| employee | An [employee object](#employee-object) with `id` field. Non-null. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/employee/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "employee": {"employee_id": 111, "tracker_id": 625987, "first_name": "John", "middle_name": "Jane", "last_name": "Smith", "email": "smith@example.com", "phone": "442071111111", "driver_license_number": "SKIMP407952HJ9GK 06", "driver_license_cats": "C", "driver_license_valid_till": "2018-01-01", "hardware_key": null, "icon_id" : 55, "avatar_file_name": null, "department_id": null, "location": {"lat": 52.5, "lng": 13.4, "address": "Engeldamm 18"}, "personnel_number": "1059236", "tags": [1,2]}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if there is no employee/driver with such an ID.
* 247 – Entity already exists, if `tracker_id`!=null and exists an employee that already bound to this `tracker_id`.


### `delete`

Deletes an employee/driver with the specified ID.

**required sub-user rights**: `employee_update`.

#### Parameters

| name        | description                           | type |
|:------------|:--------------------------------------|:-----|
| employee_id | ID of an employee (driver) to delete. | int  |

#### Examples

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
    
#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if there is no employee/driver with such an ID.


### `batch_convert`

Converts batch of tab-delimited employees/drivers and returns list of checked employees/drivers with errors.

**Required sub-user rights:** `employee_update`.

#### Parameters

| name           | description                                                                                                | type         |
|:---------------|:-----------------------------------------------------------------------------------------------------------|:-------------|
| batch          | Batch of tab-delimited employees/drivers.                                                                  | string       |
| file_id        | Preloaded file ID.                                                                                         | string       |
| fields         | Optional. Array of field names. Default is `["first_name", "middle_name", "last_name", "email", "phone"]`. | string array |
| geocoder       | Geocoder type.                                                                                             | string       |
| default_radius | Optional. Radius for point in meters. Default is 100.                                                      | int          |

* If `file_id` is set – `batch` parameter will be ignored.

#### Response

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
        "driver_license_issue_date": "2008-01-01",
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
        "ssn": "123-45-6789",
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

* `list` - list of checked employees/drivers.
    * `errors` - optional array of errors.
* `limit_exceeded` - boolean. `true` if given batch constrained by a limit.

#### Errors

* 234 - Invalid data format.
