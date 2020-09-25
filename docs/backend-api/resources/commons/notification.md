---
title: Notification
description: Notification
---

# Notification

API path: `/notification`.

### list
List user notifications.

#### response
```json
{
    "success": true,
    "list": [<notification>, ...]
}
```

where

```json
<notification> =
    {
        "id": <int>,
        "message": <string>,
        "show_till": <date/time> // date until notification should be showed, e.g. "2014-08-03 17:27:28"
    }
```
