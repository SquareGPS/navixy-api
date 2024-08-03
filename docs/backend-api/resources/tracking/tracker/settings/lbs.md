---
title: LBS settings
description: API calls for reading and changing LBS settings.
---

# LBS settings

Contains API calls for reading and changing LBS settings. It is responsible for the LBS detection radius portlet in devices
and settings tab in the UI. LBS (Location-based service) technology allows to determine the tracker's location without using 
standard location services such as GPS, GLONASS, Galileo or Beidou.
LBS locates the position using cellular base stations or Wi-Fi access points.


## API actions

API base path: `/tracker/settings/lbs`.

### `read`

Gets LBS settings for the specified tracker.

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 123456 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/settings/lbs/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/settings/lbs/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
    ```

#### Response

```json
{
    "success": true,
    "max_radius": 300
}
```

* `max_radius` - int. Max allowed radius for LBS points in meters. Min=0, max=10000.

#### Errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.


### `update`

Updates LBS settings for the specified tracker.

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 123456 |
| max_radius | Max allowed radius for LBS points in meters. Min=0, max=10000.                                  | int  | 1000   |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/settings/lbs/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "max_radius": 1000}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/settings/lbs/update?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&max_radius=1000
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
