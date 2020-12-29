---
title: Report schedule
description: Contains report schedule object description and API calls to interact with it.
---

# Report schedule

Contains report schedule object description and API calls to interact with it.

API path: `/report/schedule`.

## schedule_entry object:

```json
{
  "id": 1,
  "enabled": true,
  "parameters": {
    "period": "1m",
    "schedule": {
      "type": "weekdays",
      "weekdays": [1, 2, 3, 4, 5]
    },
    "report": {
      "trackers": [1],
      "title": "Title",
      "time_filter": {
        "from": "00:00:00",
        "to": "23:59:59",
        "weekdays": [1, 2, 3, 4, 5, 6, 7]
      },
      "geocoder": "yandex",
      "plugin": {
        "plugin_id": 4,
        "show_idle_duration": false
      }
    },
    "emails": ["email@example.ru"],
    "email_format": "pdf",
    "email_zip": false,
    "sending_time": "12:00:00"
  },
  "fire_time": "2014-09-05 00:00:00",
  "last_result": {
    "success": true,
    "id": 1
  }
}
```

* `id` - int. Schedule id, ignored on create.
* `enabled` - boolean. `true` if the scheduled report enabled.
* `period` - string. Report period, "Xm" | "w" | "d" | "y".
* `emails` - optional array of string. List of emails.
* `email_format` - string enum. Can be "pdf" | "xls".
* `sending_time` - optional string. Local time for sending reports, default "00:00:00", hourly granularity.
* `fire_time` - optional string. Last schedule fire time, ignored on create/update.
* `last_result`  object with last report creation result.
    * `id` - int. An id of generated report.

### create

Create new report schedule entry.

**required sub-user rights**: `reports`

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| schedule | schedule object without fields "id", "fire_time", "last_result". | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/schedule/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "shedule": {"enabled": true, "parameters": {"report": {"title": "Trip report", "trackers": [669673], "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs": true, "plugin_id": 4, "show_seconds": false, "include_summary_sheet_only": false, "split": true, "show_idle_duration": false, "show_coordinates": false, "filter": true, "group_by_driver": false}}, "period": "1w", "email_zip":false, "email_format":"xls", "emails": ["test@example.com"], "sending_time": "00:00:00", "schedule": {"type": "weekdays", "weekdays": [1]}}}}}'
    ```

#### response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An id of the created schedule entry.

#### errors

* 217 - List contains nonexistent entities - if one or more of tracker ids belong to nonexistent tracker (or to a tracker belonging to different user).
* 222 - Plugin not found - if specified report plugin not found.
* 236 - Feature unavailable due to.


### delete

Delete report schedule with the specified id.

**required sub-user rights**: `reports`

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| schedule_id | Id of the report schedule to delete. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/schedule/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "schedule_id": "1234567"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/report/schedule/delete?hash=a6aa75587e5c59c32d347da438505fc3&schedule_id=1234567
    ```

#### response

```json
{
    "success": true
}
```
  
#### errors

* 201 - Not found in the database - if there is no schedule with specified id.

### list

Get all report schedules belonging to user.

**required sub-user rights**: `reports`

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/schedule/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/report/schedule/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "list": [{
      "id": 1,
      "enabled": true,
      "parameters": {
        "period": "1m",
        "schedule": {
          "type": "weekdays",
          "weekdays": [1, 2, 3, 4, 5]
        },
        "report": {
          "trackers": [1],
          "title": "Title",
          "time_filter": {
            "from": "00:00:00",
            "to": "23:59:59",
            "weekdays": [1, 2, 3, 4, 5, 6, 7]
          },
          "geocoder": "yandex",
          "plugin": {
            "plugin_id": 4,
            "show_idle_duration": false
          }
        },
        "emails": ["email@example.ru"],
        "email_format": "pdf",
        "email_zip": false,
        "sending_time": "12:00:00"
      },
      "fire_time": "2014-09-05 00:00:00",
      "last_result": {
        "success": true,
        "id": 1
      }
    }]
}
```

#### errors

[General](../../../getting-started.md#error-codes) types only.

### update

Update existing report schedule. 

**required sub-user rights**: `reports`

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| schedule | schedule object without fields "id", "fire_time", "last_result". | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/schedule/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "shedule": {"enabled": true, "parameters": {"report": {"title": "Trip report", "trackers": [669673], "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs": true, "plugin_id": 4, "show_seconds": false, "include_summary_sheet_only": false, "split": true, "show_idle_duration": false, "show_coordinates": false, "filter": true, "group_by_driver": false}}, "period": "1w", "email_zip":false, "email_format":"xls", "emails": ["test@example.com"], "sending_time": "00:00:00", "schedule": {"type": "weekdays", "weekdays": [1]}}}}}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 217 - List contains nonexistent entities - if one or more of tracker ids belong to nonexistent tracker (or to a tracker belonging to different user).
* 222 - Plugin not found - if specified report plugin not found.
* 236 - Feature unavailable due to tariff restrictions - if device's tariff does not allow usage of reports.