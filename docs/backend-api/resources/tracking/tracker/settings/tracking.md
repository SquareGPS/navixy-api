---
title: Tracking mode
description: API calls for setting data transmission and operating modes of devices.
---

# Tracking mode

API calls for reading and setting data transmission and operating modes of devices. It is responsible for the tracking 
mode portlet in devices and settings tab in the UI. The list of settings can vary depending on model of the used tracker, 
the principle of its work and its functionality. 

<hr>

## API actions

API base path: `/tracker/settings/tracking`.

### read

Gets tracking settings for the specified tracker.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 123456 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/settings/tracking/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/settings/tracking/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
    ```

#### response

Returned fields may differ from model to model. See tracking profiles for more information.

```json
{
    "success": true,
    "value" : {<tracking settings>}
}
```

#### errors

* 201 – Not found in the database - if there is no tracker with such id belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 214 – Requested operation or parameters are not supported by the device - if device model has no tracking settings at all.

<hr>

### update

Sends new tracking settings to the specified tracker.

**required sub-user rights:** `tracker_configure`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int |
| tracking_settings | Set of fields which differ from model to model. See [tracking profiles](./tracking_profiles.md)  for more information. | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/settings/tracking/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "tracking_settings": {"tracking_angle": 30, "tracking_distance": 100, "tracking_interval": 60, "on_stop_tracking_interval": 180, "sleep_mode": "disabled", "stop_detection": "ignition"}}'
    ```

#### response

Returned fields may differ from model to model. See tracking profiles for more information.

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database - if there is no tracker with such id belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 214 – Requested operation or parameters are not supported by the device - if device model has no tracking settings 
at all.
* 219 – Not allowed for clones of the device - if specified tracker is clone of another tracker.
