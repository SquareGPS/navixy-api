---
title: /session
description: /session
---

## create(...)

Create subpaas session

#### parameters:

*   **subpaas_id** – **int**. Subpaas's id

#### errors

* 13 –
    * The dealer is not paas
    * The dealer has different status than NOT_BLOCKED
    * The dealer's tariff doesn't allow subpaases
    * Found subpaas is not in NOT_BLOCKED status

#### return:

```javascript
    {
        "success": true,
        "hash": "600d4a5400000000600d4a5400000000"
    }
```
