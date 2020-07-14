---
title: /listing
description: /listing
---

# listing/
## create(…)
Create new empty status listing.

**required subuser rights:** tracker_update

#### parameters:
* **listing** – **JSON object**. <status_listing> object without “id” and “entries” fields

#### return:
```js
{
    "success": true,
    "id": 111 //ID of the created status listing
}
```

#### errors:
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available
*   268 (Over quota) – if the user's quota for listings is exceeded

## delete(…)
Delete status listing.

**required subuser rights:** tracker_update
#### parameters:
* **listing_id** – **int**. ID of the status listing belonging to authorized user.

#### return:
```js
{ "success": true }
```

#### errors:
*   201 (Not found in database) – if listing with the specified ID does not exist
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available

## list()
Get status listings belonging to authorized user.

#### return:
```js
{
    "success": true,
    "list":[...] //ordered array of <status_listing> objects
}
```

#### errors:
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available

## update(…)
Update status listing properties.

**required subuser rights:** tracker_update

**entries** field allows to change order of statuses attached to this listing.

#### parameters:
* **listing** – **JSON object**. <status_list> object with “id” and “entries” fields

#### return:
```js
{ "success": true, }
```

#### errors:
*   201 (Not found in database) – if status listing with the specified ID does not exist
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available
*   262 (Entries list is missing some entries or contains nonexistent entries) – if entries does not contain full set of status IDs associated with this status listing, or if it contains nonexistent status IDs

