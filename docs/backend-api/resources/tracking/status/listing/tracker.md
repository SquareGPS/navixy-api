---
title: Tracker status listing
description: Contains API call which link together trackers and status listings.
---

# Tracker status listing

Contains api call which link together trackers and status listings.

<hr>

## API actions

API base path: `/status/listing/tracker`.

### assign

Assigns a status listing (or remove assignment) to the tracker.

**required sub-user rights:** `tracker_update`.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| listing_id | ID of the status listing. Omit this parameter completely, if you want remove the assignment. | int | 12345 |

#### examples

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

#### response

```json
{ "success": true }
```

#### errors

* 201 - Not found in the database – if there is no tracker with such ID belonging to authorized user.
* 204 - Entity not found – if there is no listing with such ID.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 219 - Not allowed for clones of the device – if specified tracker is a clone.
* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "statuses" tariff feature 
available.

