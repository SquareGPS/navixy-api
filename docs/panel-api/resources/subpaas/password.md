---
title: /password
description: /password
---

API base path: `/subpaas/password`

## change 

Change subpaas's password

#### parameters

*   **subpaas_id** – **int**. Subpaas's id
*   **new_password** – **string**. New subpaas's password

#### errors

* 13 –
    * The dealer is not paas
    * The dealer has different status than NOT_BLOCKED
    * The dealer's tariff doesn't allow subpaases
    * Found subpaas is in DELETED status

#### response

```json5
{ "success": true }
```