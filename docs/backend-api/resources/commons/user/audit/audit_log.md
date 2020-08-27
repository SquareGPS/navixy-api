---
title: User audit log 
description: User audit log
---

# User audit log

API path: `/user/audit/log`.

**audit_object** type is JSON object:

```json
{
    "id": 1, // ID of the audit record
    "user_id": 3, // Master user's ID
    "subuser_id": 3, // ID of the subuser who made an action
    "entry_category": "user", // Category of the entry on which an action was made
    "entry_id": null, // Nullable. ID of the entry on which an action was made
    "action": "login", // Action on entry
    "payload": null, // Nullable json-object. Additional information about action 
    "host": "192.168.88.1", // Host from which an action was made. IPv4 or IPv6
    "user_agent": "Apache-HttpClient/4.1.1 (java 1.5)", // User agent
    "action_date": "2018-09-03 11:32:34" // Date and time of the action
}
```

### list

Gets list of audit records available for current user.

**required subuser rights**: admin (available only to master users)

#### parameters

*   **from** – **string**. Include audit objects recorded after this date, e.g. `2014-07-01 00:00:00`.
*   **to** – **string**. Include audits before this date, e.g. `2014-07-01 00:00:00`.
*   **subuser_ids** – **int[]**. (optional) Include audits for specific subusers, e.g. `[2, 3]`.
*   **actions** – **string\[\]**. (optional) Include audits for specific actions only, e.g. `["user_checkin"]`. Set of valid values is formed by combinations of entry categories and actions.
*   **limit** – **int**. Pagination. Maximum number of audit records to return, e.g. `10`.
*   **offset** – **int**. Pagination. Get audits starting from, e.g. `0`.
*   **sort** – **string\[\]**. (optional) Set of sort options. Each option is a pair of property name and sorting direction, e.g. `["action_date=acs", "user=desc"]`. Properties available for sorting by:
    <br> — *action*
    <br> — *action_date* (sort only by date, not considering time part)
    <br> — *action_datetime* (sort by date including time)
    <br> — *user* (sort by user's (subuser) last+first+middle name, not by ID)
    <br> — *host*
    <br> If no sort param is specified, then sorting equivalent to option `["action_date=asc"]` will be applied.

#### response

```json
{
    "success": true,
    "list": [ <audit_object>, ... ]
}
```