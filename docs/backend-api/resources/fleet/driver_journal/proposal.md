---
title: Driver journal proposal
description: Driver journal proposal
---

# Driver journal proposal

API path: `/driver/journal/proposal`.

## list()
Get proposal objects that could be used for driver journal entry creation. 
Proposal objects are created by track’s division by driver changes. 
If there was no driver change on the track, then the track will be returned entirely. 
Tracks are selected by intersecting their date range with date range from request (`from` and `to` parameters).

#### structure:

    https://api.navixy.com/v2/driver/journal/proposal/list?hash=your_hash&from=YYYY-MM-DD HH:MM:SS&to=YYYY-MM-DD HH:MM:SS&tracker_id=123456

#### parameters

| name | description | type| format|
| :------: | :------: | :-----:| :------:|
| from | Include tracks which end after this date | string| YYYY-MM-DD HH:MM:SS |
| to | Include tracks which start before this date | string | YYYY-MM-DD HH:MM:SS |
| tracker_id | Id of the tracker | int | 123456 |

#### example

    https://api.navixy.com/v2/driver/journal/proposal/list?hash=22eac1c27af4be7b9d04da2ce1af111b&from=2020-05-01 00:00:00&to=2020-05-15 23:59:59&tracker_id=518076

#### response

```js
{
    "success": true,
    "list": [ <proposal_object>, ... ]
}
```

#### where

`proposal_object` is:

```js
{
      "tracker_id": 1, // id of the tracker
      "employee_id": 1, // nullable. Driver's id on the current "subtrack"
      "start_date": "2018-08-28 07:03:39", // start 
      "end_date": "2018-08-28 08:05:02", // end
      "start_location": {
        "lat": 11.111111, // latitude
        "lng": 22.222222, // longitude
        "address": "Address string" // address
      },
      "end_location": {
        "lat": 33.333333, // latitude
        "lng": 44.444444, // longitude
        "address": "Address string"  // address
      },
      "length": 2.1, // length of the current "subtrack"
      "start_odometer": 50.2, // nullable. Odometer's value at the start
      "end_odometer": 52.0, // nullable. Odometer's value at the end
      "overlapped": false // boolean flag. True if there is already driver journal entry with date range which is intersecting this proposal object's date range
}
```