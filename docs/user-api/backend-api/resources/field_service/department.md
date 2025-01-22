---
title: Departments
description: API calls to work with departments
---

# Departments

Department is essentially just a group of [employees](employee/index.md). They can be assigned to departments by
 specifying non-null `department_id`.


## Department object

```json
{
    "id": 222,
    "label": "Drivers",
    "location": {
        "lat": 46.9,
        "lng": 7.4,
        "address": "Rosenweg 3",
        "radius": 150
    }
}
```

* `id` - int. An ID of department.
* `label` - string. Name of department.
* `location` - optional object. Location associated with these departments. Should be valid or null.
    * `address` - string. Address of the location.
    * `radius` - int. Radius of location zone in meters.


## API actions

API base path: `/department`.

### `list`

Gets all departments belonging to user.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/department/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/department/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list": [{
         "id": 222,
         "label": "Drivers",
         "location": {
             "lat": 46.9,
             "lng": 7.4,
             "address": "Rosenweg 3",
             "radius": 150
         }
    }]
}
```

#### Errors

* 7 – Invalid parameters.
* 217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or 
doesn't have required tariff features.
* 221 – Device limit exceeded - if device limit set for the user’s dealer has been exceeded.


### `create`

Creates a new department with specified parameters.

**required sub-user rights:** `employee_update`.

#### Parameters

| name       | description                                                    | type        |
|:-----------|:---------------------------------------------------------------|:------------|
| department | An [department object](#department-object) without `id` field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/department/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "department": {"label": "My Department", "location": {"lat": 46.9, "lng": 7.4, "address": "Rosenweg 3", "radius": 50}}'
    ```

#### Response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An ID of the created department.

#### Errors

* 7 – Invalid parameters.
* 217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or 
doesn't have required tariff features.
* 221 – Device limit exceeded - if device limit set for the user’s dealer has been exceeded.


### `update`

Updates existing department with a new specified parameters. 

**required sub-user rights:** `employee_update`.

#### Parameters

| name       | description                                 | type        |
|:-----------|:--------------------------------------------|:------------|
| department | An [department object](#department-object). | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/department/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "department": {"id": 111, "label": "My Department", "location": {"lat": 46.9, "lng": 7.4, "address": "Rosenweg 3", "radius": 50}}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if there is no department with specified ID.


### `delete`

Deletes department with the specified ID.

**required sub-user rights:** `employee_update`.

#### Parameters

| name          | description              | type | 
|:--------------|:-------------------------|:-----|
| department_id | An ID of the department. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/department/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "department_id": 111}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/department/delete?hash=a6aa75587e5c59c32d347da438505fc3&department_id=111
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if there is no department with specified ID.
