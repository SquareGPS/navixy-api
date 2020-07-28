---
title: /history/type
description: /history/type
---

# /history/type/

## list(…)
=======

Returns available history types with localized descriptions.

#### parameters:

*   **locale** – locale code
*   **only_tracker_events** – boolean (optional). Default - true.

#### return:

```js
{
    "success": true, 
    "list": [<history_type>, ...]
}
```   

where **history_type** is

```js
{
    "type": <string>,       // history type, e.g. "alarmcontrol"
    "description": <string> // localized description, e.g. "Car alarm"
}
```