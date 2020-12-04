---
title: Driver journal proposal
description: Driver journal proposal
---

# Driver journal proposal

API path: `/driver/journal/proposal`.

### list

Gets proposal objects that could be used for driver journal entry creation. 
Proposal objects  created by a track's division by driver changes. 
If there was no driver change on the track, then the track will be returned entirely. 
Tracks selected by intersecting their date range with date range from request (`from` and `to` parameters).

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| from | Include tracks which end after this date | string |
| to | Include tracks which start before this date | string |
| tracker_id | Id of the tracker | int |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/proposal/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 123456, "from": "2020-10-13 00:00:00", "to": "2020-10-14 00:00:00"}'
    ```

#### response

```json
{
    "success": true,
    "list": [{
        "tracker_id": 1,
        "employee_id": 1,
        "start_date": "2020-10-14 07:03:39",
        "end_date": "2020-10-15 08:05:02",
        "start_location": {
         "lat": 11.111111,
         "lng": 22.222222,
         "address": "Address string"
        },
        "end_location": {
         "lat": 33.333333,
         "lng": 44.444444,
         "address": "Address string"
        },
        "length": 2.1,
        "start_odometer": 50.2,
        "end_odometer": 52.0,
        "overlapped": false
    }]
}
```

* `tracker_id` - int. An id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. 
* `employee_id` - nullable int. An id of employee (driver).
* `start_date` - string date/time. Start date of a journal entry.
* `end_date` - string date/time. End date of a journal entry.
* `start_location` - location object. Where entry starts.
* `end_location` - location object. Where entry ends.
* `length` - float. Length of the trip km.
* `start_odometer` - nullable float. Odometer's value at the start.
* `end_odometer` - nullable float. Odometer's value at the end.
* `overlapped` - boolean. `true` if there is already driver journal entry with date range which is intersecting this proposal object's date range.
