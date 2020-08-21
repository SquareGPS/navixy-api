---
title: History type
description: History type
---

# History type

API path: `/history/type`.

### list

Returns available history types with localized descriptions.

#### parameters

*   **locale** – locale code
*   **only_tracker_events** – boolean (optional). Default - true.

#### response

```json
{
    "success": true, 
    "list": [<history_type>, ...]
}
```   

where **history_type** is

```json
{
    "type": <string>,       // history type, e.g. "alarmcontrol"
    "description": <string> // localized description, e.g. "Car alarm"
}
```