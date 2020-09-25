---
title: LBS settings
description: LBS settings
---

# LBS settings

API base path: `/tracker/settings/lbs`

### read

Gets LBS settings for the specified tracker.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/settings/lbs/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/settings/lbs/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
    ```

#### response

```json
{
    "success": true,
    "max_radius": 300
}
```

* `max_radius` - int. Max allowed radius for LBS points in meters. Min=0, max=10000.

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).

### update

Updates LBS settings for the specified tracker.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| max_radius | Max allowed radius for LBS points in meters. Min=0, max=10000. | int | 1000 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/settings/lbs/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456", "max_radius": "1000"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/settings/lbs/update?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&max_radius=1000
    ```

#### response

```json
{ "success": true }
```

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
