---
title: Tag
description: Tag is a label, or a key word that is used for a quick and easy search. They help find the needed places, geofences, employees, tasks, trackers, and vehicles. Contains tag object and API calls to interact with it.
---

# Tag

API path: `/tag`.

Tag is a label, or a key word that is used for a quick and easy search. They help find the needed places, geofences, 
employees, tasks, trackers, and vehicles. Contains tag object and API calls to interact with it.

#### tag object

```json
{
  "id": 3,
  "avatar_file_name": "avatar.jpg",
  "name": "hop",
  "color": "FF0000"
}
```

* `id` - int. Tag id.
* `avatar_file_name` - optional string. File name with extension.
* `name` - string. Tag's name.
* `color` - string. Tag color in 3-byte RGB hex format.

#### tagged entity types

* place
* task
* task_schedule
* employee
* vehicle
* zone
* tracker

### create

Creates a new tag.

**required sub-user rights**: `tag_update`.

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| tag | Tag object without `id` field. | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tag/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag": {"name": "hop", "color": "FF0000"}}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tag/create?hash=a6aa75587e5c59c32d347da438505fc3&tag={"name": "hop", "color": "FF0000"}
    ```

#### response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An id of the created tag.

#### errors

[General](../../../getting-started.md#error-codes) types only.

### delete

Deletes tag with the specified id.

**required sub-user rights**: `tag_update`.

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| tag_id | Id of the tag to delete. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tag/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag_id": 1}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tag/delete?hash=a6aa75587e5c59c32d347da438505fc3&tag_id=1
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 201 – Not found in the database - if there is no tag with such an id.

### list

Gets all tags belonging to user with optional filtering.

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| filter | Optional filter for tag name. 3-60 characters or null. | string |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tag/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tag/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "list": [{
       "id": 3,
       "avatar_file_name": "avatar.jpg",
       "name": "hop",
       "color": "FF0000"
    }]
}
```

#### errors

[General](../../../getting-started.md#error-codes) types only.

### search

Search entities that bound with all of specified tags.

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| tag_ids | List of tag IDs to search. | int array |
| entity_types | Optional. List of [tagged entity types](#tag) to filter. | string array |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tag/search' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag_ids": [1, 2, 3]}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tag/search?hash=a6aa75587e5c59c32d347da438505fc3&tag_ids=[1, 2, 3]
    ```

#### response

```json
{
    "success": true,
    "result": {
      "place": [<place>],
      "task": [<task>],
      "task_schedule": [<task_schedule>],
      "employee": [<employee>],
      "vehicle": [<vehicle>],
      "zone": [<zone>],
      "tracker": [<tracker>]
    }
}
```

* `place` - array of objects. List of place objects.
* `task` - array of objects. List of task objects.
* `task_schedule` - array of objects. List of task_schedule objects.
* `employee` - array of objects. List of employee objects.
* `vehicle` - array of objects. List of vehicle objects.
* `zone` - array of objects. List of zone objects.
* `tracker` - array of objects. List of tracker objects.

#### errors

[General](../../../getting-started.md#error-codes) types only.

### update

Updates existing tag.

**required sub-user rights**: `tag_update`.

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| tag | Tag object with `id` field. | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tag/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag": {"id": 3, "name": "hop", "color": "FF0000"}}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tag/update?hash=a6aa75587e5c59c32d347da438505fc3&tag={"id": 3, "name": "hop", "color": "FF0000"}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 201 – Not found in the database - if there is no tag with such an id.
