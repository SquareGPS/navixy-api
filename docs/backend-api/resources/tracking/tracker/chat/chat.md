---
title: Сhat
description: Сhat with tracker
---

## list()

Gets a list of chat messages.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999199 |
| from | optional. Start date/time of searching. Default value is now minus 7 days | date/time | `yyyy-MM-dd HH:mm:ss` |
| to | optional. End date/time for searching. Default value is now | date/time | `yyyy-MM-dd HH:mm:ss` |
| limit | optional. Limit of messages in list. Default and max limit is 1024 | int | 1024 |
| ascending | optional. Ascending order direction from the first message to last. Default value is true | boolean | true/false |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/chat/list/' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "999199", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "list":[...] // [array of messages]
}
```

Where **message** object is:

```js
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

#### errors

* 201 – Not found in database (if there is no tracker with such id belonging to authorized user)
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
* 214 – Requested operation or parameters are not supported by the device
* 236 – Feature unavailable due to tariff restrictions (if one of the trackers has tariff without “chat” feature)

## mark_read_all()

Marks all incoming chat messages as read for all or for given user trackers.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| trackers | Optional array of Ids of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | array of int | [999199, 999919,...] |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/chat/mark_read_all/' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in database

## mark_read()

Marks incoming chat message as read by **message_id** or array of **message_ids**.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| message_id | Id of incoming message | int | 123 |
| message_ids | Ids of incoming messages | array og int | [123,213,...] |

Use only one parameter.

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/chat/mark_read/' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "message_id": "123"}'
```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in database

## send()

Sends chat message to specified tracker

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999199 |
| message | message text, not null, max size - 20000 | string | Hello World |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/chat/send/' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "999199", "message": "Hello World"}'
```

#### response

```js
{
    "success": true,
    "id": 222 //id of the submitted message
}
```

#### errors

* 201 – Not found in database (if there is no tracker with such id belonging to authorized user)
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
* 214 – Requested operation or parameters are not supported by the device
* 236 – Feature unavailable due to tariff restrictions (if one of the trackers has tariff with disabled reports – (“has_reports” is false))

## broadcast()

Sends chat message to specified trackers

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| trackers | array of Ids of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. Max size - 300 | array of int | [999199, 999919,...] |
| message | message text, not null, max size - 20000 | string | Hello World |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/chat/broadcast/' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "trackers": "[999199, 991999,...]", "message": "Hello World"}'
```

#### response

```js
{
    "success": true,
    "sent_to": [14], // list of trackers' IDs to whom the message was sent
    "not_sent_to": [5234] // list of trackers' IDs, who failed to send the message
}
```

#### errors

* 217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or doesn't have required tariff features
* 221 – Device limit exceeded (if device limit set for the user’s dealer has been exceeded)

## updated/list()

Gets date-times of last messages in chat of trackers

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| trackers | array of Ids of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. Max size - 300 | array of int | [999199, 999919,...] |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/chat/updated/list/' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "trackers": "[999199, 991999,...]"}'
```

#### response

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

#### errors

* 217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or doesn't have required tariff features
* 221 – Device limit exceeded (if device limit set for the user’s dealer has been exceeded)

## unread/count()

Gets count of user’s unread chat messages grouped by tracker id.

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/chat/unread/count/' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "value": { // map of trackers` IDs to counts
      "1": 123,
      "2": 321
    }
}
```

#### errors

* 236 – Feature unavailable due to tariff restrictions (if there is no tracker which has tariff with “chat” feature)
