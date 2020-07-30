---
title: Report schedule
description: Report schedule
---

# Report schedule

API path: `/report/schedule`.

#### report/schedule object:

    <schedule_entry> =
       {
            "id": 1, // int, schedule id, ignored on create
            "enabled": true, // boolean
            "parameters": {
                "period": "1m", // report period, Xm|w|d|y
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
                "emails": ["email@example.ru"], // optional list of emails
                "email_format": "pdf", // pdf|xls
                "email_zip": false,
                "sending_time": "12:00:00" // optional, local time for sending reports, default "00:00:00", hourly granularity
            },
            "fire_time": "2014-09-05 00:00:00", // optional, last schedule fire time, ignored on create/update
            "last_result": { // last report creation result
                "success": true,
                "id": 1
            }
        }

## create()
Create new report schedule entry. 
**required subuser rights**: reports

#### parameters
name | description | type
--- | --- | ---
schedule|<schedule_entry> object without fields which are _IGNORED_| JSON object

#### return

```ja
{
    "success": true,
    "id": 111 //id of the created schedule entry
}
```

#### errors
* 217 - List contains nonexistent entities (if one or more of tracker ids belong to nonexistent tracker (or to a tracker belonging to different user))
* 222 - Plugin not found (if specified report plugin is not found)
* 236 - Feature unavailable due to 


## delete()

Delete report schedule with the specified id.

**required subuser rights**: reports

#### parameters
name | description | type
--- | --- | ---
schedule_id | Id of the report schedule to delete | int

#### return

```json
{
    "success": true
}
```
  
#### errors

*   201 - Not 



## list()

Get all report schedules belonging to user.

**required subuser rights**: reports

#### return

```js
{
    "success": true,
    "list": [ <schedule_entry>, ... ]
}
```

#### errors

general types only


## update()

Update existing report schedule. **required subuser rights**: reports

#### parameters
name | description | type
--- | --- | ---
schedule | <schedule> object without fields which are _IGNORED_| JSON object

#### return

```json
{
    "success": true
}
```
    
#### errors

*   217 - List contains nonexistent entities (if one or more of tracker ids belong to nonexistent tracker (or to a tracker belonging to different user))
*   222 - Plugin not found (if specified report plugin is not found)
*   236 - Feature unavailable due to tariff restrictions (if device's tariff does not allow usage of reports)