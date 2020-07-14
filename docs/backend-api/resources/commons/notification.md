---
title: /notification
description: /notification
---

## list()
List user notifications.

#### return:
```javascript
{
    "success": true,
    "list": [<notification>, ...]
}
```

where
```javascript
<notification> =
    {
        "id": <int>,
        "message": <string>,
        "show_till": <date/time> // date until notification should be showed, e.g. "2014-08-03 17:27:28"
    }
```
