---
title: Group
description: Group
---
# Group

### group
Tracker group is used to organize trackers in user interface. Currently, its function is purely visual.
In FSM api, groups are read-only and represent departments of the employees assigned to trackers.
Group id `0` means employee has no department, group id `-1` means tracker has no employee assigned.

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

