---
title: /tracker
description: /tracker
---

# /status/listing/tracker/
Contains api calls which link together trackers and status listings.

### assign
Assign a status listing (or remove assignment) to the tracker.

**required subuser rights:** tracker_update

#### parameters
* **tracker_id** – **int**. ID of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **listing_id** – **int**. ID of the status listing. Omit this parameter completely, if you want remove the assignment.

#### return
```json
{ "success": true }
```

#### errors
*   201 (Not found in database) – if there is no tracker with such ID belonging to authorized user
*   204 (Entity not found) – if there is no listing with such ID
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason
*   219 (Not allowed for clones of the device) – if specified tracker is a clone
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available

