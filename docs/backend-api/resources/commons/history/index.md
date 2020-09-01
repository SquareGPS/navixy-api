---
title: History
description: History
---

# History

API path: `/history`.

## Tracker history entry

```json
{
    "id": 1,
    "type": "tracker",
    "is_read": false,
    "message": "Alarm",
    "time": "2020-01-01 00:00:00",
    "event": "offline",          // type of history event extension
    "tracker_id": 2,     // column object_id
    "rule_id": 3,        // column event_id 
    "track_id": 4,
    "location":{ 
        "lat": 50.0,
        "lng": 60.0,
        "precision": 50
    },
    "address": "address",        // string. address of location or "" (empty string)
    "extra": {
        "task_id": null , //related task identifier 
        "parent_task_id": null, //related parent task identifier (for task checkpoint related history entries)
        "counter_id": null, //related counter identifier
        "service_task_id": null, //related service task id
        "checkin_id": null, //related check-in marker
        "place_ids": null, //related place identifiers,
        "last_known_location": false, //true if location may be outdated,
        "tracker_label": "Tracker label",//tracker label
        "emergency": false //true for events with a same flag, optional
    }
}
```


Date/time type described in [data types description section](../../../getting-started.md#data-types).


### read

Returns history entry with the specified id.

#### parameters

*   id – **int**. [history entry](#tracker-history-entry) ID
*   add\_tracker\_label – **boolean**. optional, if true tracker label will be added to message

#### response

```json
{
    "success": true,
    "value": ${history_entry}
}
```

where `history_entry` described in [Tracker history entry](#tracker-history-entry).

#### errors

*   201 – Not found in database (when there are no history entries with that id)



### mark_read

Mark history entry as read by **id** (see: [Tracker history entry](#tracker-history-entry)).

#### parameters

*   id – **int**. [Tracker history entry](#tracker-history-entry) ID

#### response

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (when there are no history entries with that id)




### mark_read_all

Mark all user’s history entries read.

#### response

```json
{ "success": true }
```
    
