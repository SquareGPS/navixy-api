---
title: Tracker's working status list
description: Contains API call which link together trackers and working status lists.
---

# Tracker's working status list

Contains api call which link together trackers and working status lists.


## API actions

API base path: `/status/listing/tracker`.

### `assign`

Assigns a working status list (or remove assignment) to the tracker.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name       | description                                                                                       | type | format |
|:-----------|:--------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.   | int  | 123456 |
| listing_id | ID of the working status list. Omit this parameter completely, if you want remove the assignment. | int  | 12345  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/tracker/assign' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "listing_id": 12345}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/status/listing/tracker/assign?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&listing_id=12345
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if there is no tracker with such ID belonging to authorized user.
* 204 - Entity not found – if there is no working status list with such ID.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 219 - Not allowed for clones of the device – if specified tracker is a clone.
* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "statuses" tariff feature 
available.

