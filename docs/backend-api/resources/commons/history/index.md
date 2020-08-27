---
title: History
description: History
---

# History

API path: `/history`.

**history entry** is one of:

# History entries

*   **common\_history\_entry**
```json
{
    "id": ,
    "type": "common",
    "is_read": ,
    "message": ,
    "time": ,
    "event":            // type of history event
}
```    

*   **tracker\_history\_entry**

```json
{
    "id": ,
    "type": "tracker"
    "is_read": ,
    "message": ,
    "time": ,
    "event": ,          // type of history event extension
    "tracker_id": ,     // column object_id
    "rule_id": ,        // column event_id 
    "track_id": ,
    "location":{ 
        "lat": ,
        "lng": ,
        "precision": 
    },
    "address": "address",        // string. address of location or "" (empty string)
    "extra": {
        "task_id": , //related task identifier 
        "parent_task_id": , //related parent task identifier (for task checkpoint related history entries)
        "counter_id": , //related counter identifier
        "service_task_id": , //related service task id
        "checkin_id": , //related check-in marker
        "place_ids": , //related place identifiers,
        "last_known_location": , //true if location may be outdated,
        "tracker_label": ,//tracker label
        "emergency": ${boolean} //true for events with a same flag, optional
    }
}
```


### Deprecated event types

*   **camera\_history\_entry**
```json
{
    "id": ,
    "type": "camera"
    "is_read": ,
    "message": ,
    "time": ,
    "event": ,          // type of history event
    // extension
    "camera_id": ,
    "pack_id":     // photos pack id
}
```

*   **socket\_history\_entry**

```json
{
    "id": ,
    "type": "camera"
    "is_read": ,
    "message": ,
    "time": ,
    "event": ,          // type of history event
    // extension
    "socket_id":
}
```


Date/time type described in [data types description section](../../../getting-started.md#data-types).


### read

Returns history entry with the specified id.

#### parameters

*   id – **int**. [history entry](#history-entries) ID
*   add\_tracker\_label – **boolean**. optional, if true tracker label will be added to message

#### response

```json
{
    "success": true,
    "value": ${history_entry}
}
```

where `_history_entry` described in [History entries](#history-entries).

#### errors

*   201 – Not found in database (when there are no history entries with that id)



### mark_read

Mark history entry as read by **id** (see: [History entries](#history-entries)).

#### parameters

*   id – **int**. [history entry](#history-entries) ID

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
    
