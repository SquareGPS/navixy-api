---
title: /settings
description: /settings
---

### read
Get last waybill number. Waybill number is saved when new waybill had downloaded. If it had only digits, then it was incremented before saving.

#### return
```js
{
    "success": true,
    "value": {
        "number": "test123"
    }
}
```

#### errors
*   201 (Not found in database) – if user have never downloaded a waybill.
