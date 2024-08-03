---
title: Tracker label and group
description: API calls to get and change tracker's label and group.
---

# Tracker settings actions

Contains API calls to get and change tracker's label and group.


## API actions

API base path: `/tracker/settings`.

### `read`

Gets base settings for the specified tracker.

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 123456 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/settings/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/settings/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
    ```

#### Response

```json
{
    "success": true,
    "settings": {
        "label": "Courier",
        "group_id": 1
    }
}
```

* `label` - string. User-defined label for this tracker, e.g. "Courier".
* `group_id` - int. Tracker group id. 0 if tracker does not belong to any group.

#### Errors

* 201 – Not found in the database - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.


### `update`

Updates the settings of the specified tracker.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name       | description                                                                                                                                                     | type   | format    |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------|:----------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.                                                                 | int    | 123456    |
| group_id   | Tracker group ID. 0 if tracker does not belong to any group. The specified group must exist.                                                                    | int    | 1         |
| label      | User-defined label for this tracker, e.g. "Courier". Must consist of printable characters and have length between 1 and 60. Cannot contain `<` and `>` symbols. | string | "Courier" |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/settings/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "group_id": 1, "label": "Courier"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/settings/update?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&group_id=1&label=Courier
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 204 – Entity not found - if there is no group with the specified group id.

