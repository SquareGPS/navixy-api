---
title: Check-ins
description: Check-ins
---

# Check-ins

Check-ins are created using Mobile Tracker App 
([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) /
 [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)).
They contain date/time, address, coordinates and additional information (comment, photo, filled form) which is 
provided by app user after pressing the "Check-in" in the tracker app.
Using check-ins field personnel can provide information to their HQ while on site. For example, provide photo proof 
of the work done, or notify about a malfunction along with filled form describing the problem.

Check-ins cannot be created using web API, so all actions are read-only.

## Check-in object

```json
{
    "id": 1,
    "marker_time": "2017-03-15 12:36:27",
    "user_id": 111,
    "tracker_id": 222,
    "employee_id": 333,
    "location": {
        "lat": 56.5,
        "lng": 60.5,
        "address": "Moltkestrasse 32",
        "precision": 150
    },
    "comment": "houston, we have a problem",
    "files": [{
        "id": 16,
        "storage_id": 1,
        "user_id": 12203,
        "type": "image",
        "created": "2017-09-06 11:54:28",
        "uploaded": "2017-09-06 11:55:14",
        "name": "lala.jpg",
        "size": 72594,
        "mime_type": "image/png",
        "metadata": {
          "orientation": 1
        }
        "state": "uploaded",
        "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg"
    }],
    "form_id": 23423,
    "form_label": "Service request form"
}
```    

* `id` - int. An id of a check-in.
* `marker_time` - [date/time](../../getting-started.md#data-types). Non-null. The time of check-in creation.
* `user_id` - int. Non-null. An id of the master user.
* `tracker_id` - int. Non-null. An id of the tracker which created this check-in.
* `employee_id` - optional int. An id of the employee assigned to the tracker.
* `location` - non-null object. Location associated with this check-in marker.
    * `address` - string. Address of the location.
* `comment` - optional string. A comment provided by app user.
* `files` - list of <check-in_file> objects. Non-null. May be empty.
    * `id` - int. File id.
    * `storage_id` - int. Storage id.
    * `user_id` - int. An id of the user.
    * `type` - [enum](../../getting-started.md#data-types). Can be "image" | "file".
    * `created` - [date/time](../../getting-started.md#data-types). Date when file created.
    * `uploaded` - [date/time](../../getting-started.md#data-types). Date when file uploaded, can be null if file not yet uploaded.
    * `name` - string. A name of the file.
    * `size` int. File size in bytes. If file not uploaded, show maximum allowed size for an upload.
    * `metadata` - metadata object. 
        * `orientation` - int. Image exif orientation.
    * `state` - [enum](../../getting-started.md#data-types). Can be "created" | "in_progress" | "uploaded" | "deleted".
    * `download_url` - string. Actual url at which file is available. Can be null if file not yet uploaded.
* `form_id` - int. An id of the form which was sent along with a check-in, can be null.
* `form_label` - string. Label of the form which was sent along with a check-in, can be null.

## API actions

API path: `/checkin`.

### read

Get check-in which id is equal to `checkin_id`.
 
**required sub-user rights:** `employee_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| checkin_id | Id of the check-in entry. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/checkin/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkin_id": 1}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/checkin/read?hash=a6aa75587e5c59c32d347da438505fc3&checkin_id=1
    ```

#### response

```json
{
    "success": true,
    "value": {
        "id": 1,
        "marker_time": "2017-03-15 12:36:27",
        "user_id": 111,
        "tracker_id": 222,
        "employee_id": 333,
        "location": {
         "lat": 56.5,
         "lng": 60.5,
         "address": "Moltkestrasse 32",
         "precision": 150
        },
        "comment": "houston, we have a problem",
        "files": [{
         "id": 16,
         "storage_id": 1,
         "user_id": 12203,
         "type": "image",
         "created": "2017-09-06 11:54:28",
         "uploaded": "2017-09-06 11:55:14",
         "name": "lala.jpg",
         "size": 72594,
         "mime_type": "image/png",
         "metadata": {
           "orientation": 1
         }
         "state": "uploaded",
         "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg"
        }],
        "form_id": 23423,
        "form_label": "Service request form"
    }
}
```

#### errors

* 7 – Invalid parameters.
* 204 – Entity not found – when the marker entry is not exists.

### list

Gets marker entries on a map for trackers and for the specified time interval.

**required sub-user rights:** `employee_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| trackers | Optional. Array of tracker ids. All trackers must not be deleted or blocked (if list_blocked=false). If not specified, all available trackers will be used as value. | array of int |
| from | Optional. Start date/time for searching. | date/time |
| to | Optional. End date/time for searching. Must be after "from" date. | date/time |
| conditions | Optional. Search conditions to apply to list. See [Search conditions](../commons/entity/search_conditions.md). Allowed fields are `employee`, `location`, `marker_time`, `comment`. | array of string |
| sort | Optional, offset, default is 0. List of sort expressions. See below. | array of string |
| location | Optional, location with radius, inside which check-ins must reside | Location JSON. For example, ```{ "lat": 56.823777, "lng": 60.594164, "radius": 350 }``` | 
| limit | Optional. Max number of records to return | int |
| offset | Optional, offset (starting index of first returned record), default is 0. | int |
| format | Optional. If empty, JSON will be returned. Otherwise server will return file download in specified format. Can be "pdf" or "xlsx" | string |

##### condition fields

| Name | Type | Comment |
| :---: | :---: | :---: |
| employee | number? | id |
| tracker_id | number |  |
| marker_time | DateTime |  |
| location | string | address |
| comment | string |  |
| form | number | template's id |

##### sort 

It's a set of sort options. Each option is a pair of field name and sorting direction, e.g. `["location=asc", "employee=desc", "marker_time=desc"]`. 

##### sort fields

| Name | Type | Comment |
| :---: | :---: | :---: |
| employee | string? | full name |
| tracker_id | number |  |
| marker_time | DateTime |  |
| location | string | address |
| comment | string |  |
| form | string | label |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/checkin/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "trackers": [616384,345623], "from": "2020-08-05 03:06:00", "to": "2020-09-05 03:00:00", "offset": 20, "limit": 100, "format": "xlsx"}'
    ```

#### response

```json
{
    "success": true,
    "list": [<checkin>],
    "count": 22
}
```

* `list` - list of check-in objects.
* `count` - int. Total number of check-ins (ignoring offset and limit).

#### errors

* 7 – Invalid parameters.
* 211 – Requested time span is too big (more than **maxReportTimeSpan** config option).
* 217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or 
doesn't have required tariff features.
* 221 – Device limit exceeded (if device limit set for the user's dealer has been exceeded).

### delete

Deletes check-ins with the specified id-s.

**required sub-user rights:** `checkin_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| checkin_ids | List of check-in ids.  | array of int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/checkin/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkin_ids": [2132,4533]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/checkin/delete?hash=a6aa75587e5c59c32d347da438505fc3&checkin_ids=[2132,4533]
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 7 – Invalid parameters.
* 201 - Not found in the database - check-ins with the specified ids don't exist, or their corresponding 
trackers are not available to current sub-user.
