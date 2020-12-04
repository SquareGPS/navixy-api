---
title: /password
description: /password
---

API base path: `/dealer/password`

## update

Changes password for logined dealer. 

#### required permissions:

*   **password**: "update"

#### parameters

*   **old_password** \- **string**. Current password of the user 
*   **new_password** \- **string**. New password for the user, 6 to 20 printable characters

#### response

    { "success": true }
    

#### errors

*   225 - New password must be different (if **old_password** = **new_password**)
*   248 - Wrong password (if **old_password** is wrong)