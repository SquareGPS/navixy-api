---
title: /employee
description: /employee
---

# employee/actions:

**employee** is:
```js
{
    "id": 222,//<int>
    "tracker_id": null, //<int>
    "first_name": "John", //<string>
    "middle_name": "Jane", //<string>
    "last_name": "Smith", //<string>
    "email": "smith@example.com", //<string>
    "phone": "+442071111111", //<string>
    "driver_license_number": "SKIMP407952HJ9GK 06", //<string>
    "driver_license_cats": "C", //<string, driver license categories>
    "driver_license_valid_till": "2018-01-01", //<date>
    "hardware_key": null,//<string>
    "icon_id" : 55, // int, can be null, can only be updated via avatar/assign(...)
    "avatar_file_name": null,//<string>,
    "department_id": null, //<optional, int>,
    "location": {   //optional, location associated with this employee, shoul be valid or null
        "lat": 52.5,
        "lng": 13.4,
        "address": "Engeldamm 18" //address of the location
    },
    "personnel_number": "1059236", // optional, string, max lenght is 15
    "tags": [1,2] //array of tag ids
}
```

## list()

Get all employees belonging to user.

#### return:

```js
{
    "success": true,
    "list": [ <employee>, ... ]
}
```

#### errors:

general types only

## create(…)

Create new employee.

**required subuser rights**: employee_update

#### parameters:

*   **employee** – an [employee object](#employeeactions) Non-null.

#### return:

```js
{
    "success": true,
    "id": 111 //id of the created employee
}
```

#### errors:

*   247 – Entity already exists, if tracker\_id!=null and exists employee that already binded to this tracker\_id


## read(…)

Get employee by id.

#### parameters:

*   **employee_id** – Id of the employee, int.

#### return:

```js
{
    "success": true,
    "value": <employee>
}
```

#### errors:

*   201 – Not found in database (if there is no employee with such id)


## update(…)

Update existing employee.

**required subuser rights**: employee_update

#### parameters:

*   **employee** – an [employee object](#employeeactions) Non-null.

#### return:

```json
{ "success": true }
```

#### errors:

*   201 – Not found in database (if there is no employee with such id)
*   247 – Entity already exists, if tracker\_id!=null and exists employee that already binded to this tracker\_id

## delete(…)

Delete employee with the specified id.

**required subuser rights**: employee_update

#### parameters:

*   **employee_id** – Id of the employee, int.

#### return:

```json
{ "success": true }
```

#### errors:

*   201 – Not found in database (if there is no employee with such id)
