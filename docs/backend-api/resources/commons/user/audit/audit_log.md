---
title: User audit log 
description: Using the audit log, account owner can track the activity of all users added through the "Access rights" section.Contains audit object and list method to get the audit log.
---

# User audit log

Using the audit log, account owner can track the activity of all users added through the "Access rights" section. Contains
audit object and list method to get the audit log.


## Audit object

```json
{
  "id": 44504790,
  "user_id": 3,
  "subuser_id": 184541,
  "entry_category": "custom_field",
  "entry_id": null,
  "action": "create",
  "payload": {
    "name": "Decimal number"
  },
  "host": "94.140.138.215",
  "user_agent": "Apache-HttpClient/4.1.1 (java 1.5)",
  "action_date": "2020-12-21 17:54:01"
}
```

* `id` - int. An ID of the audit record.
* `user_id` - int. Master user's ID.
* `subuser_id` - int. ID of the sub-user who made an action.
* `entry_category` - string. Category of the entry on which an action made.
* `entry_id` - int. ID of the entry on which an action made. Nullable.
* `action` - string. Action on entry.
* `payload` - Nullable JSON object. Additional information about action.
* `host` - string. Host from which an action made. IPv4 or IPv6.
* `user_agent` - string. User agent.
* `action_date` - [date/time](../../../../getting-started/introduction.md#data-types). Date and time of the action.


## API actions

API path: `/user/audit/log`.

### `list`

Gets list of audit records available for current user.

**required sub-user rights**: `admin` (available only to master users).

#### Parameters

| name        | description                                                                                                                           | type                                                                |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| from        | Include audit objects recorded after this date.                                                                                       | [date/time](../../../../getting-started/introduction.md#data-types) |
| to          | Include audits before this date.                                                                                                      | [date/time](../../../../getting-started/introduction.md#data-types) |
| subuser_ids | Optional. Include audits for specific sub-users.                                                                                      | int array                                                           |
| actions     | Optional. Include audits for specific actions only.                                                                                   | string array                                                        |
| limit       | Pagination. Maximum number of audit records to return.                                                                                | int                                                                 |
| offset      | Pagination. Get audits starting from.                                                                                                 | int                                                                 |
| sort        | Optional. Set of sort options. Each option is a pair of property name and sorting direction, e.g. `["action_date=asc", "user=desc"]`. | string array                                                        |
| grouping    | Optional. Group log by "user", "action_date", "action" or don't group "default".                                                      | [enum](../../../../getting-started/introduction.md#data-types)      |

Properties available for sorting by:

* `action`.
* `action_date` - sort only by date, not considering time part.
* `action_datetime` - sort by date including time.
* `user` - sort by user's (sub-user) last+first+middle name, not by ID.
* `host`.
If no sort param is specified, then sorting equivalent to option `["action_date=asc"]` will be applied.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/audit/log/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "from": "2020-12-25 03:24:00", "to": "2020-12-28 06:24:00", "limit": 50, "offset": 0}'
    ```

#### Response

```json
{
  "success": true,
  "list": [
    {
      "id": 44504790,
      "user_id": 3,
      "subuser_id": 184541,
      "entry_category": "custom_field",
      "entry_id": null,
      "action": "create",
      "payload": {
        "name": "Decimal number"
      },
      "host": "94.140.138.215",
      "user_agent": "Apache-HttpClient/4.1.1 (java 1.5)",
      "action_date": "2020-12-21 17:54:01"
    }
  ]
}
```

#### Errors

* [General](../../../../getting-started/errors.md#error-codes) types only.
