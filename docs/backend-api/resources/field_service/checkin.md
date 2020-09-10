---
title: Check-ins
description: Check-ins
---

# Check-ins

Check-ins are created using Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)).
They contain date/time, address, coordinates and additional information (comment, photo, filled form) which is provided by app
user after pressing the "Check-in" in the tracker app.
Using check-ins field personnel can provide information to their HQ while on site. For example, provide photo proof of the 
work done, or notify about a malfunction along with filled form describing the problem.

Check-ins cannot be created using web API, so all actions are read-only.

`<checkin>` is:
```json
{
    "id": 1, //identifier
    "marker_time": "2017-03-15 12:36:27", // non-null, time of check-in creation
    "user_id": 111, // non-null, id of the master user
    "tracker_id": 222, // non-null, id of the tracker which created this check-in
    "employee_id": 333, // optional, id of the employee assigned to the tracker
    "location": {   // non-null, location associated with this check-in marker
        "lat": 56.5,
        "lng": 60.5,
        "address": "Moltkestrasse 32", // address of the location
        "precision": 150
    },
    "comment": "houston, we have a problem", // optional, comment provided by app user
    "files": [<checkin_file>, ...], // non-null, may be empty   
    "form_id": 23423, //id of the form which was sent along with check-in, can be null
    "form_label": "Service request form" //label of the form which was sent along with check-in, can be null
}
```           

`<checkin_file>` is:

```json
{
    "id": 16, // file id
    "storage_id": 1,
    "user_id": 12203,
    "type": "image", // "image" or "file"
    "created": "2017-09-06 11:54:28", // date when file was created
    "uploaded": "2017-09-06 11:55:14", // date when file was uploaded, can be null if file is not yet uploaded
    "name": "lala.jpg", // filename
    "size": 72594, // in bytes. If file not uploaded, show maximum allowed size for upload
    "mime_type": "image/png",
    "metadata": nullable, <metadata_object>,
    "state": "uploaded", // can be "created", "in_progress", "uploaded", "deleted"
    "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg", // actual url at which file is available. Can be null if file is not yet uploaded
}
```

`<metadata_object>` is:
```json
{
 "orientation":  <int, image exif orientation>,
}
```

## API actions

API path: `/checkin`.

### read

Get check-in which id is equal to `checkin_id`. Required tariff features: `checkin`.

#### parameters

| name | description | type | format |
| :--- | :--- | :--- | :--- |
| checkin_id | id of the check-in entry | int | 123456 | 

#### example

    {{ extra.api_example_url }}/checkin/read?hash=22eac1c27af4be7b9d04da2ce1af111b&checkin_id=132215

#### response

```json
{
    "success": true,
    "value": <checkin>
}
```

#### errors

*   7 – Invalid parameters
*   204 – Entity not found – when the marker entry is not exists

### list

Gets marker entries on map for trackers and for the specified time interval. Required tariff features: `checkin`.

#### parameters

| name | description | type | example |
| :--- | :--- | :--- | :--- |
| trackers | array of tracker ids. all trackers must not be deleted or blocked (if list_blocked=false). Optional. If not specified, all available trackers will be used as value.| array of ints | `[123456,223456,...]` |
| from | start date/time for searching. Optional. | date/time | `2020-01-01 00:00:00` |
| to | end date/time for searching. must be after “from” date. Optional.  | date/time | `2020-02-02 00:00:00` |
| conditions | optional, search conditions to apply to list. | Array of search conditions, see [Search conditions](../../commons/entity/search_conditions/). Allowed fields are `employee`, `location`, `marker_time`, `comment` | |
| sort | optional, offset, default is 0 | string[], list of sort expressions. See below. | `["location=asc", "marker_time=desc"]`  |
| limit | optional, max number of records to return | int | |
| offset | optional, offset (starting index of first returned record), default is 0.  | int | |
| format | Optional. If empty, JSON will be returned. Otherwise server will return file download in specified format. Can be "pdf" or "xlsx" | string | `pdf` |

##### sort 
It's a set of sort options. Each option is a pair of field name and sorting direction, e.g. `["location=asc", "employee=desc", "marker_time=desc"]`. 
Possible fields: `employee`, `location`, `marker_time`, `comment`.

#### example

    {{ extra.api_example_url }}/checkin/list?hash=22eac1c27af4be7b9d04da2ce1af111b&trackers=[616384,345623]&from=2020-08-05 03:06:00&to=2020-09-05 03:00:00&offset=20&limit=100&format=xlsx

#### response

```json
{
    "success": true,
    "list": [<checkin>, ... ], // list of check-ins
    "count": 22 //total number of checkins (ignoring offset and limit)
}
```

#### errors
*   7 – Invalid parameters
*   211 – Requested time span is too big (more than **maxReportTimeSpan** config option)
*   217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or doesn't have required tariff features
*   221 – Device limit exceeded (if device limit set for the user’s dealer has been exceeded)

### delete

Delete checkins with the specified id-s.

**required subuser rights:** checkin_update

#### parameters

| name | description | type | format |
| :--- | :--- | :--- | :--- |
| checkin_ids | array of checkin ids.  | array of ints | [123456,223456,...] |


#### example

    {{ extra.api_example_url }}/checkin/delete?hash=22eac1c27af4be7b9d04da2ce1af111b&checkin_ids=[213,4533]

#### response

```json
{
    "success": true
}
```

#### errors
*   7 – Invalid parameters
*   201 - Not found in database - checkins with the specified ids don't exist or their corresponding trackers are not
    available to current subuser