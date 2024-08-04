---
title: Chat 
description: API calls to work with chat module.
---
# Chat

API calls to work with chat module. A chat module allows remote employees and supervisors quickly exchange their 
ideas and feedback, as well as helps employers to boost team culture. This can prove to be a useful communication tool.


## API actions

API base path: `/tracker/chat`.

### `list`

Gets a list of chat messages.

#### Parameters

| name       | description                                                                                     | type                                                                   | format                |
| :--------- | :---------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- | :-------------------- |
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int                                                                    | 999199                |
| from       | Optional. Start date/time of searching. Default value is now minus 7 days.                      | [date/time](../../../getting-started/introduction.md#datetime-formats) | `yyyy-MM-dd HH:mm:ss` |
| to         | Optional. End date/time for searching. Default value is now.                                    | [date/time](../../../getting-started/introduction.md#datetime-formats)              | `yyyy-MM-dd HH:mm:ss` |
| limit      | Optional. Limit of messages in list. Default and max limit is 1024.                             | int                                                                    | 1024                  |
| ascending  | Optional. Ascending order direction from the first message to last. Default value is `true`.    | boolean                                                                | true/false            |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/chat/list' \
        -H 'Content-Type: application/json' \
        -d '{"tracker_id": 123456, "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/chat/list?tracker_id=123456&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list": [{<message1>}, {<message2>}]
}
```

* `list` - `array` of messages.

Where **message** object is:

```json
{
  "id": 1,
  "submit_time": "2014-04-15 09:02:24",
  "update_time": null,
  "text": "text of message",
  "type": "INCOMING",
  "status": "PENDING",
  "employee_id": 123456
}
```

* `submit_time` - time when the message submitted.
* `update_time` - delivering time for outgoing messages.
* `type` - `INCOMING` or `OUTGOING`.
* `status` - `PENDING` or `DELIVERED`.
* `employee_id` - optional, nullable employee identifier.

#### Errors

* 201 – Not found in the database (if there is no tracker with such ID belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
* 214 – Requested operation or parameters are not supported by the device.
* 236 – Feature unavailable due to tariff restrictions (if one of the trackers has tariff without "chat" feature).


### `mark_read_all`

Marks all incoming chat messages as read for all or for given user trackers.

#### Parameters

| name     | description                                                                                                        | type      | format             |
|:---------|:-------------------------------------------------------------------------------------------------------------------|:----------|:-------------------|
| trackers | Optional array of IDs of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int array | `[999199, 999919]` |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/chat/mark_read_all' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/chat/mark_read_all?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database.


### `mark_read`

Marks incoming chat message as read by `message_id` or array of `message_ids`.

#### Parameters

| name        | description               | type      | format      |
|:------------|:--------------------------|:----------|:------------|
| message_id  | ID of incoming message.   | int       | 123         |
| message_ids | IDs of incoming messages. | int array | `[123,213]` |

Use only one parameter.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/chat/mark_read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "message_id": 123}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/chat/mark_read?hash=a6aa75587e5c59c32d347da438505fc3&message_id=123
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database.


### `send`

Sends chat message to a specified tracker.

#### Parameters

| name       | description                                                                                     | type   | format        |
|:-----------|:------------------------------------------------------------------------------------------------|:-------|:--------------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int    | 123456        |
| message    | Message text, not null, max size - 20000.                                                       | string | "Hello World" |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/chat/send' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 123456, "message": "Hello World"}'
    ```

#### Response

```json
{
    "success": true,
    "id": 222
}
```

* `id` - ID of the submitted message.

#### Errors

* 201 – Not found in the database - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 214 – Requested operation or parameters are not supported by the device.
* 236 – Feature unavailable due to tariff restrictions - if one of the trackers has tariff with disabled reports ("has_reports" is `false`).


### `broadcast`

Sends chat message to specified trackers.

#### Parameters

| name     | description                                                                                                               | type      | format             |
|:---------|:--------------------------------------------------------------------------------------------------------------------------|:----------|:-------------------|
| trackers | Array of IDs of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. Max size - 300. | int array | `[999199, 999919]` |
| message  | Message text, not null, max size - 20000.                                                                                 | string    | "Hello World"      |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/chat/broadcast' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "trackers": [999199, 991999], "message": "Hello World"}'
    ```

#### Response

```json
{
    "success": true,
    "sent_to": [14],
    "not_sent_to": [5234]
}
```

* `sent_to` - list of tracker IDs to whom the message sent.
* `not_sent_to` - list of tracker IDs, who failed to send the message.

#### Errors

* 217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or doesn't have required tariff features.
* 221 – Device limit exceeded - if device limit set for the user's dealer has been exceeded.


### `updated/list`

Gets date-times of last messages in chat of trackers.

#### Parameters

| name     | description                                                                                                               | type      | format             |
|:---------|:--------------------------------------------------------------------------------------------------------------------------|:----------|:-------------------|
| trackers | Array of IDs of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. Max size - 300. | int array | `[999199, 999919]` |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/chat/updated/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "trackers": [999199, 991999]}'
    ```

#### Response

```json
{
    "success": true,
    "value": {
        "101": "2016-02-29 00:23:00",
        "122": "2017-02-28 00:23:00"
    }
}
```

* `value` - map of tracker IDs to date-times.

#### Errors

* 217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or 
doesn't have required tariff features.
* 221 – Device limit exceeded - if device limit set for the user's dealer has been exceeded.


### `unread/count`

Gets count of user's unread chat messages grouped by tracker ID.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/chat/unread/count' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/chat/unread/count?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "value": {
      "1": 123,
      "2": 321
    }
}
```

* `value` - map of tracker IDs to counts.

#### Errors

* 236 – Feature unavailable due to tariff restrictions - if there is no tracker which has a tariff with "chat" feature.
