---
title: Departments
description: Departments
---

# Departments

Department is essentially just a group of [employees](employee/index.md). They can be assigned to departments by specifying 
non-null `department_id`.

<a name="structure"></a>
`<department>` is:

```json
{
    "id": 222, <int>
    "label": "Drivers",
    "location": {   //optional, location associated with this departments. should be valid or null
        "lat": 46.9,
        "lng": 7.4,
        "address": "Rosenweg 3", //address of the location
        "radius": 150  //radius of location zone in meters
    },
}
```


## API actions

API base path: `/department`.
  
### list

Gets all departments belonging to user.

#### example

    {{ extra.api_example_url }}/department/list?hash=your_hash

#### response

```json
{
    "success": true,
    "list": [ <department>, ... ]
}
```
#### errors

*   7 – Invalid parameters
*   211 – Requested time span is too big (more than **maxReportTimeSpan** config option)
*   217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or doesn't have required tariff features
*   221 – Device limit exceeded (if device limit set for the user's dealer has been exceeded)


### create

Creates a new department with specified parameters. Required subuser rights: `employee_update`.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| department | an [department object](#structure) | object | `{"label":"Name","location":{"lat": 1.12345,"lng": 2.67890, "address": "address of the department", "radius": "123"}` |

#### example

    {{ extra.api_example_url }}/department/create?hash=22eac1c27af4be7b9d04da2ce1af111b&department={"label":"My Department","location":{"lat": 46.9,"lng": 7.4,"address": "Rosenweg 3", "radius": "50"}}

#### response

```json
{
    "success": true,
    "id": 111 //id of the created department
}
```

#### errors

*   7 – Invalid parameters
*   211 – Requested time span is too big (more than **maxReportTimeSpan** config option)
*   217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or doesn't have required tariff features
*   221 – Device limit exceeded (if device limit set for the user's dealer has been exceeded)


### update

Updates existing department with a new specified parameters. Required subuser rights: `employee_update`.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| department | an [department object](#structure) | object | `{"label":"Name","location":{"lat": 1.12345,"lng": 2.67890, "address": "address of the department", "radius": "123"}` |

#### example

    {{ extra.api_example_url }}/department/update?hash=22eac1c27af4be7b9d04da2ce1af111b&department={"label":"My Department","location":{"lat": 46.9,"lng": 7.4,"address": "Rosenweg 3", "radius": "50"}}

#### response

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (if there is no department with such id)


### delete

Deletes department with the specified id. Required subuser rights: `employee_update`.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| department_id | Id of the department | int | 12345 |

#### example

    {{ extra.api_example_url }}/department/delete?hash=22eac1c27af4be7b9d04da2ce1af111b&department_id=65878

#### response

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (if there is no department with such id).
