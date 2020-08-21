---
title: /status
description: /status
---

# status/
Statuses are used to track current activity for employees (in fact, of tracking devices owned by employees). Simplest example is “busy” / “not busy”. This is a status listing consisting of two elements. Different trackers can be assigned different status lists.

#### objects
**status** is:
```js
{
    "id": 5, // unique identifier of this status. Read-only.
    "label": "Busy", // human-readable label for this status
    "color": "E57373" // hex-representation of RGB color used to display this status
}
```

**status_listing** is:
```js
{
    "id": 1, // unique identifier of this status listing. Read-only.
    "label": "Taxi driver statuses", // human-readable label for this status listing
    "employee_controlled": true, // if true, employees can change their own status, e.g. using mobile tracking app
    "supervisor_controlled": false, // if true,
    "entries": [ 5, 2, 1, 4, 6] // list of IDs of statuses which belong to this listing. Order matters, and is preserved.
}
```
### create
Create new possible status for the specified status listing.

**required subuser rights:** tracker_update
#### parameters
* **listing_id** – **int**. ID of the listing for this status to attach to.
* **status** – **JSON object**. <status> object without ID field.

#### response
```js
{
    "success": true,
    "id": 111 // ID of the created status
}
```

#### errors
*    201 (Not found in database) – if listing with the specified ID does not exist
*    236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available
*    268 (Over quota) – if the user's quota for statuses is exceeded

### delete
Delete status entry.

**required subuser rights:** tracker_update

#### parameters
* **status_id** – **int**. ID of the status belonging to authorized user.

#### response
```json
{ "success": true }
```

#### errors
*   201 (Not found in database) – if status with the specified ID does not exist
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available

### list
Get statuses belonging to the specified status listing.

#### parameters
* **listing_id** – **int**. ID of the status listing belonging to authorized user.

#### response
```js
{
    "success": true,
    "list":[…] // ordered array of <status> objects
}
```

#### errors
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available


### update

Update status properties.

**required subuser rights:** tracker_update
#### parameters
* **status** – **JSON object**. <status> object with ID field

#### response
```json
{ "success": true }
```

#### errors
*   201 (Not found in database) – if status with the specified ID does not exist
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available
