---
title: Datalogger
description: API call for uploading datalogger information.
---
# Datalogger

API call for uploading datalogger information.


## API actions

API base path: `/tracker/datalogger`.

### `upload`

Uploads track data for specified tracker. Tracker must be a datalogger.

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a CSV file upload 
(with the name "file").

#### Parameters

| name       | description                                                                                     | type |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  |
| file       | A CSV file upload containing datalogger track data.                                             | file |

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if there is no tracker with such ID belonging to authorized user.
* 219 – Not allowed for clones of the device - if tracker is clone.
* 233 – No data file - if file part is missing.
* 214 – Requested operation or parameters are not supported by the device - if specified tracker is not datalogger.
