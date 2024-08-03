---
title: Driver journal entry
description: Contains driver journal entry object description and API calls to work with it.
---

# Driver journal entry

Contains driver journal entry object description and API calls to work with it. Using the driver journal, you can monitor trips and categorize them by status to see the full picture of transport usage. Driver Entry is an already categorized trip.

To get information on how-to work with driver journals refer to our [instructions](../../../guides/fleet-management/driver-journals.md).


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
    },
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

* `id` - int. An ID of an entry.
* `tracker_id` - int. An ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. 
* `start_date` - [date/time](../../../getting-started/introduction.md#data-types). Start date of a journal entry.
* `end_date` - [date/time](../../../getting-started/introduction.md#data-types). End date of a journal entry.
* `employee_id` - nullable int. An ID of employee (driver).
* `type` - [enum](../../../getting-started/introduction.md#data-types). Type of journal entry. Can be "work", "personal", "other".
* `comment` - nullable string. Comment for entry.
* `start_location` - location object. Where entry starts.
* `end_location` - location object. Where entry ends.
* `length` - float. Length of the trip km.
* `start_odometer` - nullable float. Odometer's value at the start.
* `end_odometer` - nullable float. Odometer's value at the end.


## API actions

API path: `/driver/journal/entry`.

### `list`

Gets driver journal entries. 
There are two ways to get entries: by their IDs or by specifying date range.
If there are no `entry_ids` in request, entries will be selected by intersecting their date range with date range from
 request (`from` and `to` parameters).

#### Parameters

| name       | description                                                                                                                        | type                                                |
|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.                                    | int                                                 |
| from       | Include tracks which end after this date, e.g. "2020-10-13 00:00:00".                                                              | [date/time](../../../getting-started/introduction.md#data-types) |
| to         | Include tracks which end after this date, e.g. "2020-10-14 00:00:00".                                                              | [date/time](../../../getting-started/introduction.md#data-types) |
| entry_ids  | Optional. Array of entry IDs.                                                                                                      | int array                                           |
| types      | Optional. Types of the driver journal entry, e.g. `["work", "personal", "other"]`.                                                 | string array                                        |
| sort       | Optional. Set of sort options. Each option is a pair of column name and sorting direction, e.g. `["start_date=asc", "type=desc"]`. | string array                                        |

* Possible columns of `sort` parameter:

    * `start_date` - Sort only by date, not considering time part.
    * `start_datetime` - Just raw column value.
    * `end_date` - Sort only by date, not considering time part.
    * `end_datetime` - Just raw column value.
    * `start_address` - Sort only by start address.
    * `end_address` - Sort only by the end address.
    * `driver` - Sort by last+first+middle driver name, not by driver ID. 
    * `type` - Sort by type. 
    * If no `sort` param is specified, then `sort` option will be "start_date=asc".

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 123456, "from": "2020-10-13 00:00:00", "to": "2020-10-14 00:00:00"}'
    ```

#### Response

```json
{
    "success": true,
    "list": [{
        "id": 127722,
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
        },
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

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.


### `create`

Creates driver journal entries.

#### Parameters

| name    | description                                                 | type             |
|:--------|:------------------------------------------------------------|:-----------------|
| entries | Array of `driver_journal_entry` objects without `id` field. | array of objects |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "entries": [{"tracker_id": 1, "start_date": "2020-10-13 07:03:39", "end_date": "2020-10-14 08:05:02", "employee_id": 1, "type": "work", "comment": "comment string", "start_location": {"lat": 11.0, "lng": 22.0, "address": "address value"}, "end_location": {"lat": 11.0, "lng": 22.0, "address": "address value"}, "length": 1.44, "start_odometer": 1.34, "end_odometer": 5.34}]}'
    ```

#### Response

```json
{ "success": true}
```

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types.


### `update`

Updates driver journal entry. Only two fields `type` and `comment` are available to update.

#### Parameters

| name  | description                                            | type        |
|:------|:-------------------------------------------------------|:------------|
| entry | `driver_journal_entry_update_request` type. See below. | JSON object |

* `driver_journal_entry_update_request` object:
  
```json
{
  "id": 1,
  "type": "work",
  "comment": "new comment"
}
```

* `id` - int. An ID of the driver journal entry.
* `type` - [enum](../../../getting-started/introduction.md#data-types). Type of journal entry. Can be "work", "personal", "other".
* `comment` - string. New comment of the driver journal entry.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "entry": {"id": 1, "type": "work", "comment": "new comment"}}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors
* 201 – if tracker not found
* 204 - if entry not found. 
* [General](../../../getting-started/errors.md#error-codes) types only.


### `delete`

Deletes driver journal entries.

#### Parameters

| name      | description                           | type      |
|:----------|:--------------------------------------|:----------|
| entry_ids | Array of driver journal entries' IDs. | int array |

#### Examples

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

#### Response

```json
{ "success": true }
```

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.


### `download`

Gets driver journal entries. Entries selected by intersecting their date range with date range from request (`from` 
and `to` parameters).

#### Parameters

| name                | description                                                                                                                                 | type                                                |
|:--------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|
| tracker_id          | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.                                             | int                                                 |
| from                | Include tracks which end after this date, e.g. "2020-10-13 00:00:00".                                                                       | [date/time](../../../getting-started/introduction.md#data-types) |
| to                  | Include tracks which end after this date, e.g. "2020-10-14 00:00:00".                                                                       | [date/time](../../../getting-started/introduction.md#data-types) |
| entry_ids           | Optional. Array of entry IDs.                                                                                                               | int array                                           |
| types               | Optional. Types of the driver journal entry, e.g. `["work", "personal", "other"]`.                                                          | string array                                        |
| sort                | Optional. Set of [sort options](#list). Each option is a pair of column name and sorting direction, e.g. `["start_date=asc", "type=desc"]`. | string array                                        |
| add_filename_header | If `true` then Content-Disposition header will be appended to the response. Default value is `true`.                                        | boolean                                             |
| format              | File format: "pdf", "xls" and "xlsx".                                                                                                       | string                                              |
| group_by            | Optional. If specified, grouped entries will be in different sections of the table.                                                         | string                                              |

* Possible values of `group_by` parameter:
    * `type` - group entries by entry type.
    * `date` - group entries by start_date per day.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/driver/journal/entry/download' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 123456, "from": "2020-10-13 00:00:00", "to": "2020-10-14 00:00:00", "add_filename_header": true, "format": "pdf"}'
    ```

#### Response

A driver journal report file (standard file download).

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.
