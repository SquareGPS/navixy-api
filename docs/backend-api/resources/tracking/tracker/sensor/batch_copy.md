---
title: Copy sensors
description: Copying sensors from base tracker to same model other trackers
---

# Copy sensors

API path: `/tracker/sensor/batch_copy`.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| base_tracker_id | Id of the base tracker (aka "object_id") from which you want to copy sensors. Tracker must belong to authorized user and not be blocked. | int | 123456 |
| trackers | Id of trackers. Target trackers for copying sensors. | [int] | [12345, 54321] |


=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/batch_copy' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "base_tracker_id": 123456, "trackers": [56789, 54321]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/sensor/calibration_data/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&sensor_id=12345
    ```

#### response

```json
{
    "success": true
}
```
#### errors

* 201 – Not found in the database (if there is no tracker with such id belonging to authorized user).
* 400 – Trackers must have same models (if base tracker and one of target trackers has a different model).


