---
title: Driver journal entry
description: Driver journal entry
---

# Driver journal entry

API path: `/driver/journal/entry`.

## Driver journal entry object

```json
{
    "id":127722,
    "tracker_id": 1,
    "start_date": "2020-10-13 07:03:39",
    "end_date": "2020-10-14 08:05:02",
    "employee_id": 1,
    "type": "work",
    "comment": "comment string",
    "start_location": {
        "lat": 11.0,
        "lng": 22.0,
        "address": "address value"
    "end_location": {
        "lat": 11.0,
        "lng": 22.0,
        "address": "address value"
    },
    "length": 1.44,
    "start_odometer": 1.34,
    "end_odometer": 5.34
}
```

* `id` - int. An id of an entry.
* `tracker_id` - int. An id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. 
* `start_date` - string date/time. Start date of a journal entry.
* `end_date` - string date/time. End date of a journal entry.
* `employee_id` - nullable int. An id of employee (driver).
* `type` - string enum. Type of journal entry. Can be "work", "personal", "other".
* `comment` - nullable string. Comment for entry.
* `start_location` - location object. Where entry starts.
* `end_location` - location object. Where entry ends.
* `length` - float. Length of the trip km.
* `start_odometer` - nullable float. Odometer's value at the start.
* `end_odometer` - nullable float. Odometer's value at the end.

### list

Gets driver journal entries. 
There are two ways to get entries: by their ids or by specifying date range.
If there are no `entry_ids` in request, entries will be selected by intersecting their date range with date range from
 request (`from` and `to` parameters).

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int |
| entry_ids | Optional. Array of entry ids. | array of int |
| from | Optional. Include tracks which end after this date, e.g. "2020-10-13 00:00:00". | string date/time |
| to | Optional. Include tracks which end after this date, e.g. "2020-10-14 00:00:00". | string date/time |
| types | Optional. Types of the driver journal entry, e.g. `["work", "personal", "other"]`. | array of string |
| sort | Optional. Set of sort options. Each option is a pair of column name and sorting direction, e.g. `["start_date=acs", "type=desc"]`. | array of string |

* Possible columns of `sort` parameter:

    * `start_date` - Sort only by date, not considering time part.
    * `start_datetime` - Just raw column value.
    * `end_date` - Sort only by date, not considering time part.
    * `end_datetime` - Just raw column value.
    * `start_address` - Sort only by start address.
    * `end_address` - Sort only by the end address.
    * `driver` - Sort by last+first+middle driver name, not by driver id. 
    * `type` - Sort by type. 
    * If no `sort` param is specified, then `sort` option will be "start_date=acs".

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 123456, "from": "2020-10-13 00:00:00", "to": "2020-10-14 00:00:00"}'
    ```

#### response

```json
{
    "success": true,
    "list": [{
        "id":127722,
        "tracker_id": 1,
        "start_date": "2020-10-13 07:03:39",
        "end_date": "2020-10-14 08:05:02",
        "employee_id": 1,
        "type": "work",
        "comment": null,
        "start_location": {
         "lat": 23.25658,
         "lng": 21.89892,
         "address": "address"
        "end_location": {
         "lat": 23.26227,
         "lng": 21.59321,
         "address": "address"
        },
        "length": 1.44,
        "start_odometer": 1.34,
        "end_odometer": 5.34
    }]
}
```

### create

Creates driver journal entries.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| entries | Array of `driver_journal_entry` objects without `id` field. | array of objects |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "entries": [{"tracker_id": 1, "start_date": "2020-10-13 07:03:39", "end_date": "2020-10-14 08:05:02", "employee_id": 1, "type": "work", "comment": "comment string", "start_location": {"lat": 11.0, "lng": 22.0, "address": "address value"}, "end_location": {"lat": 11.0, "lng": 22.0, "address": "address value"}, "length": 1.44, "start_odometer": 1.34, "end_odometer": 5.34}]}'
    ```

#### response

```json
{ "success": true}
```

### update

Updates driver journal entry. Only two fields `type` and `comment` are available to update.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| entry | `driver_journal_entry_update_request` type. See below. | object |

* `driver_journal_entry_update_request` object:
  
```json
{
  "id": 1,
  "type": "work",
  "comment": "new comment"
}
```

* `id` - int. An id of the driver journal entry.
* `type` - string enum. Type of journal entry. Can be "work", "personal", "other".
* `comment` - string. New comment of the driver journal entry.

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "entry": {"id": 1, "type": "work", "comment": "new comment"}}'
    ```

#### response

```json
{ "success": true }
```

### delete

Deletes driver journal entries.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| entry_ids | Array of driver journal entries' ids. | array of int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "entry_ids": [127722, 127724]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/driver/journal/entry/delete?hash=a6aa75587e5c59c32d347da438505fc3&entry_id=[127722, 127724]
    ```

#### response

```json
{ "success": true }
```

### download

Gets driver journal entries. Entries selected by intersecting their date range with date range from request (`from` 
and `to` parameters).

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int |
| entry_ids | Optional. Array of entry ids. | array of int |
| from | Optional. Include tracks which end after this date, e.g. "2020-10-13 00:00:00". | string date/time |
| to | Optional. Include tracks which end after this date, e.g. "2020-10-14 00:00:00". | string date/time |
| types | Optional. Types of the driver journal entry, e.g. `["work", "personal", "other"]`. | array of string |
| sort | Optional. Set of [sort options](#list). Each option is a pair of column name and sorting direction, e.g. `["start_date=acs", "type=desc"]`. | array of string |
| add_filename_header | If `true` then Content-Disposition header will be appended to the response. Default value is `true`. | boolean |
| format | File format: "pdf", "xls" and "xlsx" | string |
| group_by | Optional. If specified, grouped entries will be in different sections of the table. | string |

* Possible values of `group_by` parameter:
    * `type` - group entries by entry type.
    * `date` - group entries by start_date per day.

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/download' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 123456, "from": "2020-10-13 00:00:00", "to": "2020-10-14 00:00:00", "add_filename_header": true, "format": "pdf"}'
    ```

#### response

A driver journal report file (standard file download).