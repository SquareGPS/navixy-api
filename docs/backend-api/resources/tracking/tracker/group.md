---
title: Group
description: Group
---
# Group

Tracker group used to organize trackers in user interface. Currently, its function is purely visual.

## Group object structure:

```json
{
    "id": 167,
    "title": "Main office",
    "color": "FF6DDC"
}
```

* `id` - int. Group id. Used to reference group in objects and API calls. Read-only, assigned automatically by the server.
* `title` - string. User-specified group title, 1 to 60 printable characters, e.g. "Employees".
* `color` - string. Group color in web format (without #), e.g. "FF6DDC". Determines the color of tracker markers on the map.

## API actions

API base path: `/tracker/group`

### assign

Assigns multiple trackers to the specified group.

**required sub-user rights:** `admin` (available only to master users).

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| id | Group id, or 0 if trackers should be removed from any group. | int | 167 |
| trackers | Array of Ids of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | array of int | `[999199, 999919]` |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/group/assign' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "trackers": "[999199, 991999]", "id": "167"}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if no group found with the specified id (or group belongs to another user).
* 217 (List contains nonexistent entities) – if one or more of tracker ids belong to nonexistent tracker 
(or to a tracker belonging to different user).

### create

Creates a new empty group.

**required sub-user rights:** `admin` (available only to master users).

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| title | Ser-specified group title, 1 to 60 printable characters. | string | "Employees" |
| color | Group color. | string | "FF6DDC" |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/group/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Employees", "color": "FF6DDC"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/group/create?hash=a6aa75587e5c59c32d347da438505fc3&title=Employees&color=FF6DDC
    ```

#### response

```json
{
    "success": true,
    "id": 222
}
```

* `id` - int. An id of created group, e.g. 222.

#### errors

[General](../../../getting-started.md#error-codes) types only.

### delete

Deletes group with the specified id. The group must belong to authorized user. All trackers from this group will be 
assigned to default group (0).

**required sub-user rights:** `admin` (available only to master users).

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| id | Id of group to delete. | int | 167 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/group/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "id": "167"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/group/delete?hash=a6aa75587e5c59c32d347da438505fc3&id=167
    ```
    
#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if no group found with the specified id (or group belongs to another user).

### list

Gets all user tracker groups. There is always "default" unnamed group with id = 0. It cannot be modified, deleted, 
and is not returned by this API call.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/group/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/group/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "list": [
        {
            "title": "test",
            "color": "FF6DDC",
            "id": 129301
        }
    ]
}
```

#### errors

[General](../../../getting-started.md#error-codes) types only.

### update

Updates specified tracker group. Group must belong to the authorized user.

**required sub-user rights**: `admin` (available only to master users).

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| id | Id of group to update. | int | 167 |
| title | Ser-specified group title, 1 to 60 printable characters. | string | "Employees" |
| color | Group color. | string | "FF6DDC" | 

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/group/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "id": "167", "title": "Employees", "color": "FF6DDC"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/group/update?hash=a6aa75587e5c59c32d347da438505fc3&id=167&title=Employees&color=FF6DDC
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if no group found with the specified id (or group belongs to another user).
