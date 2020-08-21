---
title: Vehicle status listing
description: Vehicle status listing
---

# Vehicle status listing

API path: `/vehicle/status/listing`.

`vehicle_status_entry` type is JSON object:

```json5
{
    "id": 1, // int, id of the status
    "order": 0, // int, position of the status. ignored when update because statuses already have position in array 
    "label": "label123", // string, status's description 
    "color": "FFFFFF" // string, RGB-color
}
```

### read

Gets all of user's vehicle statuses.

#### response

```json5
{
    "success": true,
    "list": [ <vehicle_status_entry>, ... ]
}
```

### update

Update user's vehicle statuses.

#### parameters

*   **statuses** – **vehicle\_status\_entry**[]. If status's id is not null, then update, else create new vehicle status.
Old vehicle statuses, which are not present is this array, will be deleted.

#### response

```json5
{ "success": true }
```
