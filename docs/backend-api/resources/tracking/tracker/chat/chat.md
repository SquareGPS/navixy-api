---
title: /chat
description: /chat
---

## list()
Get list of chat messages.

#### parameters:
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **from** - **DateTime**. optional, start date/time for searching. Default value is now − 7 days.
* **to** - **DateTime**. optional, end date/time for searching. Default value is now.
* **limit** - **int**. optional, limit. Default and max limit is 1024.
* **ascending** - **boolean**. optional, order direction. Default value is true.

#### return:
```javascript
{
    "success": true,
    "list":[...] //[array of messages]
}
```
**Message** is
```javascript
{
  "id": 1,
  "submit_time": "2014-04-15 09:02:24", //submit time
  "update_time": null, //delivering time for outgoing messages
  "text": "incoming",
  "type": "INCOMING", //INCOMING or OUTGOING
  "status": "PENDING" //PENDING or DELIVERED,
  "employee_id": <int> //optional, nullable employee identifier

}
```

#### errors:
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   214 – Requested operation or parameters are not supported by the device
*   236 – Feature unavailable due to tariff restrictions (if one of the trackers has tariff without “chat” feature)

## mark_read_all()
Mark all incoming chat messages as read for all or given user trackers.

#### parameters:
* **trackers** - **array of int**. Optional array of Ids of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### return:
```javascript
{ "success": true }
```
#### errors:
*   201 – Not found in database

## mark_read()
Mark incoming chat message as read by **message_id** or array of **message_ids**.

#### parameters:
* **message_id** **int**
OR
* **message_ids** **array of int**

#### return:
```javascript
{ "success": true }
```
#### errors:
*   201 – Not found in database

## send()
Send chat message to specified tracker.

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **message** - **string**. message text, not null, max size - 20000

#### return:
```javascript
{
    "success": true,
    "id": 222 //id of the submitted message
}
```

#### errors:
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   214 – Requested operation or parameters are not supported by the device
*   236 – Feature unavailable due to tariff restrictions (if one of the trackers has tariff with disabled reports – (“has_reports” is false))

## broadcast()
Send chat message to specified trackers.

#### parameters
* **trackers** - **array of int**. List of the tracker’s IDs, max size - 300
* **message** - **string**. message text, not null, max size - 20000

#### return:
```js
{
    "success": true,
    "sent_to": [14], // list of trackers' IDs to whom the message was sent
    "not_sent_to": [5234] // list of trackers' IDs, who failed to send the message
}
```

#### errors:
*   217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or doesn't have required tariff features
*   221 – Device limit exceeded (if device limit set for the user’s dealer has been exceeded)

## updated/list()
Get date-times of last messages in the chats

#### parameters
* **trackers** - **array of int**. List of the tracker’s IDs

#### return:
```js
{
    "success": true,
    "value": { // map of trackers` IDs to date-times
        "101": "2016-02-29 00:23:00",
        "122": "2017-02-28 00:23:00",
        ...
    }
}
```

#### errors:
*   217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or doesn't have required tariff features
*   221 – Device limit exceeded (if device limit set for the user’s dealer has been exceeded)

## unread/count()
Get count of user’s unread chat messages grouped by tracker id.

#### return:
```js
{
    "success": true,
    "value": { // map of trackers` IDs to counts
      "1": 123,
      "2": 321
    }
}
```

#### errors:
*   236 – Feature unavailable due to tariff restrictions (if there is no tracker which has tariff with “chat” feature)
