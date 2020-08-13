---
title: Checkin
description: Checkin
---

# Checkin

API path: `/checkin`.

## read()

Gets marker on map for the `checkin_id`. Required tariff features: `checkin`.

#### structure:

    https://api.navixy.com/v2/fsm/checkin/read?hash=your_hash&checkin_id=123456

#### parameters

| name | description | type | format |
| :--- | :--- | :--- | :--- |
| checkin_id | id of the marker entry | int | 123456 | 

#### example

    https://api.navixy.com/v2/fsm/checkin/read?hash=22eac1c27af4be7b9d04da2ce1af111b&checkin_id=132215

#### response

```js
{
    "success": true,
    "value": <checkin_marker> // marker on map (see below)
}
```

#### errors

*   7 – Invalid parameters
*   204 – Entity not found – when the marker entry is not exists

## list()

Gets marker entries on map for trackers and for the specified time interval. Required tariff features: `checkin`.

####structure:

    https://api.navixy.com/v2/fsm/checkin/list?hash=your_hash&trackers=[tracker_id_n]&from=YYYY-MM-DD HH:MM:SS&to=YYYY-MM-DD HH:MM:SS

#### parameters

| name | description | type | format |
| :--- | :--- | :--- | :--- |
| trackers | array of tracker ids. all trackers must not be deleted or blocked (if list_blocked=false) | array of ints | [123456,223456,...] |
| from | start date/time for searching | date/time | 2020-01-01 00:00:00 |
| to | end date/time for searching. must be after “from” date  | date/time | 2020-02-02 00:00:00 |

#### example

    https://api.navixy.com/v2/fsm/checkin/list?hash=22eac1c27af4be7b9d04da2ce1af111b&trackers=[616384,345623]&from=2020-08-05 03:06:00&to=2020-09-05 03:00:00

#### response

```js
{
    "success": true,
    "list": [<checkin_marker>, ... ] // list of markers on map
}
```

where `checkin_marker` is:

```js
{
    "id": 1,
    "marker_time": "2017-03-15 12:36:27", // required, time of marker creation
    "user_id": 111, // required
    "tracker_id": 222, // required
    "employee_id": 333, // optional
    "location": {   // required, location associated with this check-in marker
        "lat": 56.5,
        "lng": 60.5,
        "address": "Moltkestrasse 32", // address of the location
        "precision": 150
    },
    "comment": "houston, we have a problem", // optional, employee comment
    "files": [<checkin_file>, ...] // required, may be empty
}
```

where `checkin_file` is:

```js
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
    "metadata": <nullable, metadata object>,
    "state": "uploaded", // can be "created", "in_progress", "uploaded", "deleted"
    "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg", // actual url at which file is available. Can be null if file is not yet uploaded
}
```

#### errors
*   7 – Invalid parameters
*   211 – Requested time span is too big (more than **maxReportTimeSpan** config option)
*   217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or doesn't have required tariff features
*   221 – Device limit exceeded (if device limit set for the user’s dealer has been exceeded)
