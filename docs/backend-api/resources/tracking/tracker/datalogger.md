---
title: Datalogger
description: Uploading datalogger information
---
# Datalogger

API base path: `/tracker/datalogger`

### upload

Uploads track data for specified tracker. Tracker must be a datalogger.

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a CSV file upload (with the name “file”).

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| file | A CSV file upload containing datalogger track data. | file | name.csv |

#### response

```json
{ "success": true }
```

#### errors
* 201 – Not found in the database (if there is no tracker with such id belonging to authorized user).
* 219 – Not allowed for clones of the device (if tracker is clone).
* 233 – No data file (if file part is missing).
* 214 – Requested operation or parameters are not supported by the device (if specified tracker is not datalogger).
