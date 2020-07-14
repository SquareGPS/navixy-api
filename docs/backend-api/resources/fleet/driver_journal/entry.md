---
title: /driver/journal/entry
description: /driver/journal/entry
---

# entry/

**driver\_journal\_entry** type is JSON object:

    {
        "tracker_id": 1,  // Id of the tracker
        "start_date": "2018-08-28 07:03:39",  // Start date
        "end_date": "2018-08-28 08:05:02",  // End date
        "employee_id": 1,  // nullable. Driver
        "type": "work",  // Type ('work', 'personal', 'other')
        "comment": "comment string",  // nullable
        "start_location": {
            "lat": 11.0, // latitude
            "lng": 22.0, // longitude
            "address": "address value" // address
        },
        "end_location": {
            "lat": 11.0, // latitude
            "lng": 22.0, // longitude
            "address": "address value" // address
        },
        "length": 1.44,  // length
        "start_odometer": 1.34,  // nullable. Odometer's value at the start
        "end_odometer": 5.34,  // nullable. Odometer's value at the end
    }


## list(…)

Get driver journal entries. 
There are two ways to get entries: by their ids or by specifying date range.
If there no **entry_ids** in request, entries are selected by intersecting their date range with date range from request (**from** and **to** parameters).

#### parameters:

*   **tracker_id** – **int**. Id of the tracker
*   **entry_ids** – **int\[\]**. (optional) Ids of the entries.
*   **from** – **string**. (optional) Include tracks which end after this date, e.g. “2014-07-01 00:00:00”
*   **to** – **string**. (optional) Include tracks which start before this date, e.g. “2014-07-01 00:00:00”
*   **types** – **string[\]**. (optional) Types of the driver journal entry, e.g. \[\"work\", \"personal\"\]
*   **sort** – **string\[\]**. (optional) Set of sort options. Each option is a pair of column name and sorting direction, e.g. \[“start_date=acs”, “type=desc”\]. Possible columns:
    <br> — start_date (sort only by date, not considering time part)
    <br> — start_datetime (just raw column value)
    <br> — end_date (sort only by date, not considering time part)
    <br> — end_datetime (just raw column value)
    <br> — start_address
    <br> — end_address
    <br> — driver (sort by last+first+middle driver name, not by driver id)
    <br> — type
    <br> If no sort param is specified, then sort option will be “start_date=acs”

#### return:

    {
        "success": true,
        "list": [ <driver_journal_entry>, ... ]
    }

----
## create(…)

Create driver journal entries.

#### parameters:

*   **entries** – **driver\_journal\_entry\[\]**. Array of **driver\_journal\_entry** objects without id.

#### return:

    {
        "success": true
    }

----
## update(…)

Update driver journal entry. Only two fields (**type** and **comment**) are available for update.

#### parameters:

*   **entry** – **driver\_journal\_entry\_update\_request** type. See below.

#### return:

    {
        "success": true
    }


**driver\_journal\_entry\_update\_request** type is JSON object:

    {
          "id": 1, // id of the driver journal entry
          "type": 1, // new type of the driver journal entry
          "comment": "new comment" // new comment of the the driver journal entry
    }

---

## delete(…)

Delete driver journal entries.

#### parameters:

*   **entry_ids** – **int\[\]**. Array of driver journal entries’ ids.

#### return:

    {
        "success": true
    }

---

## download(…)

Get driver journal entries. Entries are selected by intersecting their date range with date range from request (**from** and **to** parameters).


#### parameters:

same as in list(...) method plus:

*   **add_filename_header** – **boolean**. Default value is true. If true then Content-Disposition header will be appended to the response.
*   **format** – **string**. File format: ‘pdf’, ‘xls’ and ‘xlsx’
*   **group_by** – **string**. (optional) If specified, grouped entries will be in different sections of the table.
    Possible values:
    — type (group entries by entry type)
    — date (group entries by start_date per day)

#### return:

    A driver journal report file (standard file download).