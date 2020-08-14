---
title: Working with employees
description: Working with employees
---

Employees are used to represent people working at one's organization. They can be linked with other entities such as 
trackers, vehicles, places, etc.

<a name="structure"></a>
`<employee>` is:

```js
{
    "id": 222, //internal ID. Can be passed as null only for "create" action. 
    "tracker_id": null, //id of the tracker currently assigned to this employee. null means no tracker assigned
    "first_name": "John", //First name. Cannot be empty. Max 100 characters.
    "middle_name": "Jane", //Middle name. Can be empty, cannot be null. Max 100 characters.
    "last_name": "Smith", //Last name. Can be empty, cannot be null. Max 100 characters.
    "email": "smith@example.com", //Employee's email. Must be valid email address. Can be empty, cannot be null. Max 100 characters.
    "phone": "+442071111111", //Employee's phone. Can be empty, cannot be null. Max 32 characters.
    "driver_license_number": "SKIMP407952HJ9GK 06", //Driver license number. Can be empty, cannot be null. Max 32 characters.
    "driver_license_cats": "C", //String, driver license categories. Max 32 characters.
    "driver_license_valid_till": "2018-01-01", //Date (yyyy-MM-dd). Can be null.
    "hardware_key": null,//String. Can be null. Max 64 characters.
    "icon_id" : 55, // int, can be null, can only be updated via "avatar/assign"
    "avatar_file_name": null,//String, nullable, can only be updated via "avatar/upload"
    "department_id": null, //Id of the department to which employee is assigned. Can be null.
    "location": {   //optional, location associated with this employee, should be valid or null
        "lat": 52.5,
        "lng": 13.4,
        "address": "Engeldamm 18" //address of the location
    },
    "personnel_number": "1059236", // optional, string, max length is 15
    "tags": [1,2] //array of tag ids
}
```

# API actions:

API base path: `/employee`.

## list

Get all employees belonging to user.

#### return

```js
{
    "success": true,
    "list": [ <employee>, ... ]
}
```

#### errors

general types only

## create

Create new employee.

**required subuser rights**: employee_update

#### parameters

*   **employee** – an [employee object](#structure) Non-null.

#### return

```js
{
    "success": true,
    "id": 111 //id of the created employee
}
```

#### errors

*   247 – Entity already exists, if tracker\_id!=null and exists employee that already binded to this tracker\_id


## read

Get employee by id.

#### parameters

*   **employee_id** – Id of the employee, int.

#### return

```js
{
    "success": true,
    "value": <employee>
}
```

#### errors

*   201 – Not found in database (if there is no employee with such id)


## update

Update existing employee.

**required subuser rights**: employee_update

#### parameters

*   **employee** – an [employee object](#structure) Non-null.

#### return

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (if there is no employee with such id)
*   247 – Entity already exists, if tracker\_id!=null and exists employee that already binded to this tracker\_id

## delete

Delete employee with the specified id.

**required subuser rights**: employee_update

#### parameters

*   **employee_id** – Id of the employee, int.

#### return

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (if there is no employee with such id)
