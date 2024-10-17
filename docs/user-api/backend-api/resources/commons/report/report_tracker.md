---
title: Report tracker
description: User reports allow acquiring all-round statistics and analytics. The summary data can be shown in various perspectives, in tables and graphs.Contains API calls to interact with tracker reports.
---

# Report Tracker

User reports enable comprehensive statistics and analytics, presenting summary data in various perspectives through tables and graphs. This section details API calls to interact with tracker reports.

For information on how to obtain data from reports, refer to the [guide](../../../guides/data-retrieval/obtain-reports.md).

## API actions

API path: `/report/tracker`.

### `delete`

Deletes a report from the database.

*required sub-user rights*: `reports`.

#### Parameters

| name      | description                            | type |
|:----------|:---------------------------------------|:-----|
| report_id | ID of a report that should be deleted. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "report_id": 1234567}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/report/tracker/delete?hash=a6aa75587e5c59c32d347da438505fc3&report_id=1234567
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 101 – In demo mode this function disabled.


### `download`

Retrieve generated report as a file.

**required sub-user rights**: `reports`

#### Parameters

| name      | description                                                                                       | type                                           |
|:----------|:--------------------------------------------------------------------------------------------------|:-----------------------------------------------|
| report_id | ID of a report that should be deleted.                                                            | int                                            |
| format    | A format of report that should be downloaded. Can be "xls", xlsx" or "pdf".                       | [enum](../../../getting-started/introduction.md#data-types) | 
| headless  | Optional parameter. Default=`false`. If need report without title page and TOC, set it to `true`. | boolean                                        |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/download' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "report_id": 1234567, "format": "pdf"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/report/tracker/download?hash=a6aa75587e5c59c32d347da438505fc3&report_id=1234567&format=pdf
    ```

#### Response

A report rendered to file (standard file download).

#### Errors

* 204 - Entity not found - if report with the specified ID not found.
* 229 - Requested data is not ready yet - if report exists, but its generation is still in progress.


### `generate`

Requests a report generation with the specified parameters.

**required sub-user rights**: `reports`.

#### Parameters

| name        | description                                                                                                                                                          | type        |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| from        | A string containing [date/time](../../../getting-started/introduction.md#datetime-formats).                                                                                       | string      |
| to          | A string containing [date/time](../../../getting-started/introduction.md#datetime-formats). Specified date must be after "from" date.                                             | string      |
| title       | Report title. Default title will be used if null.                                                                                                                    | string      |
| geocoder    | Which geocoder to use. See [geocoder/](../../tracking/geocoder.md).                                                                                                  | string      |
| trackers    | List of trackers' IDs to be included in report (if report is by trackers).                                                                                           | int array   |
| employees   | List of employees' IDs to be included in report (if report is by employees. For example, [plugin ID 82](../plugin/report_plugins.md#eco-driving-report-by-drivers)). | int array   |
| time_filter | An object which contains everyday time and weekday limits for processed data, e.g. `{"to":"18:00", "from":"12:00", "weekdays":[1,2,3,4,5]}`.                         | JSON object |
| plugin      | A plugin object (see below).                                                                                                                                         | JSON object |

#### Parameter object fields:

Part of parameters are plugin-specific. See ["Tracker report plugins"](../plugin/report_plugins.md) section. Common parameters are:

| name         | description                                                                                                                        | type    |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------|:--------|
| plugin_id    | An ID of a tracker report plugin which will be used to generate report.                                                            | int     |
| show_seconds | Flag to define whether time values in report should have format with seconds. `true` - show seconds, `false` - don't show seconds. | boolean |

#### Plugin example:

```json
{
  "details_interval_seconds": 300,
  "plugin_id": 9,
  "show_seconds": false,
  "graph_type": "time",
  "smoothing": false,
  "sensors": [
    {
      "tracker_id": 123456,
      "sensor_id": 123456
    }
  ]
}
```

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Trip report", "trackers": [669673], "from": "2020-10-05 00:00:00", "to": "2020-10-06 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs": true, "plugin_id": 4, "show_seconds": false, "include_summary_sheet_only": false, "split": true, "show_idle_duration": false, "show_coordinates": false, "filter": true, "group_by_driver": false}}'
    ```

#### Response

```json
{
  "success": true,
  "id": 222
}
```

* `id` - int. An ID of the report queued for generation. Can be used to request report generation status and to retrieve generated report.

#### Errors

* 15 - Too many requests / rate limit exceeded - the number of reports created by one user in parallel limited.
* 211 - Requested time span is too big - interval from `from` to `to` is bigger then max allowed time span (see response).

```json
{
  "success": false,
  "status": {
    "code": 211,
    "description": "Requested time span is too big"
  },
    "max_time_span": "P90D"
}
```

* `max_time_span` - string. ISO 8601 duration.

* 217 - List contains nonexistent entities - when one or more of tracker IDs belong to nonexistent tracker (or to a tracker belonging to different user).
* 222 - Plugin not found - when specified report plugin not found.
* 236 - Feature unavailable due to tariff restrictions - when one of the trackers has tariff with disabled reports ("has_reports" is false).


### `list`

Returns info about all available generated or in-progress reports.

**required sub-user rights**: `reports`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/report/tracker/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,"list": [
    {
        "created": "2020-10-08 21:59:30",
        "time_filter": {
          "from":"00:00:00",
          "to":"23:59:59",
          "weekdays":[1,2,3,4,5,6,7]},
        "title": "Trip report",
        "id": 5601797,
        "parameters": { 
          "geocoder": "google",
          "trackers": [669673],
          "plugins": [{
            "plugin_id": 4,
            "filter": true,
            "hide_empty_tabs": true,
            "show_coordinates": false,
            "split": true,
            "include_summary_sheet_only": false,
            "show_seconds": false,
            "group_by_driver": false,
            "show_idle_duration": false
          }],
          "locale_info": {
            "locale": "ru_RU",
            "time_zone": "Asia/Yekaterinburg",
            "measurement_system": "metric"
          }
        }, 
        "percent": 100,
        "type": "user",
        "from": "2020-10-05 00:00:00",
        "to": "2020-10-06 23:59:59"
    }
]}
```

* `created` - string. Date when report created.
* `time_filter` - object.
    * `from` - string. Control time "from" of day.
    * `to` - string. Control time "to" of day.
    * `weekdays` - int array. Control "weekdays" of the report. Can be 1 - 7.
* `title` - string. Report title.
* `id` - int. Report ID which can be used to retrieve or download report.
* `parameters` - object with report parameters.
    * `trackers` - int array. List of tracker IDs used for report.
    * `plugins` - array of objects. List of parameters for all plugins which were used to generate report.
    * `locale_info` - object with information about the locale, timezone, and measurement system used for the report.
* `percent` - int. Report readiness in percent.
* `type` - [enum](../../../getting-started/introduction.md#data-types). Type of created report.
* `from` - string. "from" parameter from generate.
* `to` - string. "to" parameter from generate.

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.


### `retrieve`

Retrieves a generated report as JSON.

**required sub-user rights**: `reports`.

#### Parameters

| name      | description                            | type |
|:----------|:---------------------------------------|:-----|
| report_id | ID of a report that should be deleted. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/retrieve' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "report_id": 1234567}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/report/tracker/retrieve?hash=a6aa75587e5c59c32d347da438505fc3&report_id=1234567
    ```

#### Response

???+ example "Response"

    ```json
    {
    "success": true,
    "report": {
      "created": "2020-10-06 16:01:46",
      "time_filter": {
          "from": "00:00:00",
          "to": "23:59:59",
          "weekdays": [
              1,
              2,
              3,
              4,
              5,
              6,
              7
          ]
      },
      "title": "Trip report",
      "id": 5602232,
      "sheets": [
          {
              "header": "Samantha (Ford Focus)",
              "sections": [
                  {
                      "data": [
                          {
                              "rows": [
                                  {
                                      "to": {
                                          "v": "02:39 - Serpukhov, Moscow Oblast, Russia, 142253",
                                          "raw": 1601941188000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 54.9218516,
                                              "lng": 37.335545
                                          }
                                      },
                                      "from": {
                                          "v": "00:47 - Selyatino, Naro-Fominskii gor. okrug, Moscow Oblast, Russia, 143370",
                                          "raw": 1601934439000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 55.5311083,
                                              "lng": 36.96743
                                          }
                                      },
                                      "time": {
                                          "v": "01:52",
                                          "raw": 6749.0,
                                          "type": "value"
                                      },
                                      "length": {
                                          "v": "106.29",
                                          "raw": 106.29,
                                          "type": "value"
                                      },
                                      "avg_speed": {
                                          "v": "57",
                                          "raw": 57.0,
                                          "type": "value"
                                      },
                                      "max_speed": {
                                          "v": "94",
                                          "raw": 94.0,
                                          "type": "value"
                                      }
                                  },
                                  {
                                      "to": {
                                          "v": "05:10 - Selyatino, Naro-Fominskii gor. okrug, Moscow Oblast, Russia, 143370",
                                          "raw": 1601950218000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 55.5308216,
                                              "lng": 36.967315
                                          }
                                      },
                                      "from": {
                                          "v": "03:11 - Serpukhov, Moscow Oblast, Russia, 142253",
                                          "raw": 1601943083000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 54.9218116,
                                              "lng": 37.3354833
                                          }
                                      },
                                      "time": {
                                          "v": "01:58",
                                          "raw": 7135.0,
                                          "type": "value"
                                      },
                                      "length": {
                                          "v": "106.97",
                                          "raw": 106.97,
                                          "type": "value"
                                      },
                                      "avg_speed": {
                                          "v": "54",
                                          "raw": 54.0,
                                          "type": "value"
                                      },
                                      "max_speed": {
                                          "v": "94",
                                          "raw": 94.0,
                                          "type": "value"
                                      }
                                  },
                                  {
                                      "to": {
                                          "v": "07:54 - Khievskii pereulok, 10, TNKh, Rassudovo, Troitsky Administrative Okrug, Moscow, Russia, 143340",
                                          "raw": 1601960075000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 55.4666366,
                                              "lng": 36.9216966
                                          }
                                      },
                                      "from": {
                                          "v": "07:38 - Selyatino, Naro-Fominskii gor. okrug, Moscow Oblast, Russia, 143370",
                                          "raw": 1601959081000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 55.53122,
                                              "lng": 36.9672916
                                          }
                                      },
                                      "time": {
                                          "v": "00:16",
                                          "raw": 994.0,
                                          "type": "value"
                                      },
                                      "length": {
                                          "v": "10.03",
                                          "raw": 10.03,
                                          "type": "value"
                                      },
                                      "avg_speed": {
                                          "v": "36",
                                          "raw": 36.0,
                                          "type": "value"
                                      },
                                      "max_speed": {
                                          "v": "85",
                                          "raw": 85.0,
                                          "type": "value"
                                      }
                                  },
                                  {
                                      "to": {
                                          "v": "09:36 - Serpukhov, Moscow Oblast, Russia, 142253",
                                          "raw": 1601966165000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 54.926835,
                                              "lng": 37.3341066
                                          }
                                      },
                                      "from": {
                                          "v": "07:58 - Khievskii pereulok, 10, TNKh, Rassudovo, Troitsky Administrative Okrug, Moscow, Russia, 143340",
                                          "raw": 1601960315000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 55.46661,
                                              "lng": 36.9216516
                                          }
                                      },
                                      "time": {
                                          "v": "01:37",
                                          "raw": 5850.0,
                                          "type": "value"
                                      },
                                      "length": {
                                          "v": "95.31",
                                          "raw": 95.31,
                                          "type": "value"
                                      },
                                      "avg_speed": {
                                          "v": "59",
                                          "raw": 59.0,
                                          "type": "value"
                                      },
                                      "max_speed": {
                                          "v": "91",
                                          "raw": 91.0,
                                          "type": "value"
                                      }
                                  },
                                  {
                                      "to": {
                                          "v": "09:53 - Serpukhov, Moscow Oblast, Russia, 142253",
                                          "raw": 1601967190000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 54.921935,
                                              "lng": 37.33551
                                          }
                                      },
                                      "from": {
                                          "v": "09:43 - Serpukhov, Moscow Oblast, Russia, 142253",
                                          "raw": 1601966585000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 54.9264033,
                                              "lng": 37.3336633
                                          }
                                      },
                                      "time": {
                                          "v": "00:10",
                                          "raw": 605.0,
                                          "type": "value"
                                      },
                                      "length": {
                                          "v": "0.95",
                                          "raw": 0.95,
                                          "type": "value"
                                      },
                                      "avg_speed": {
                                          "v": "6",
                                          "raw": 6.0,
                                          "type": "value"
                                      },
                                      "max_speed": {
                                          "v": "13",
                                          "raw": 13.0,
                                          "type": "value"
                                      }
                                  },
                                  {
                                      "to": {
                                          "v": "12:36 - Selyatino, Naro-Fominskii gor. okrug, Moscow Oblast, Russia, 143370",
                                          "raw": 1601977017000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 55.5309666,
                                              "lng": 36.9674183
                                          }
                                      },
                                      "from": {
                                          "v": "10:27 - Serpukhov, Moscow Oblast, Russia, 142253",
                                          "raw": 1601969226000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 54.9219933,
                                              "lng": 37.335495
                                          }
                                      },
                                      "time": {
                                          "v": "02:09",
                                          "raw": 7791.0,
                                          "type": "value"
                                      },
                                      "length": {
                                          "v": "108.48",
                                          "raw": 108.48,
                                          "type": "value"
                                      },
                                      "avg_speed": {
                                          "v": "50",
                                          "raw": 50.0,
                                          "type": "value"
                                      },
                                      "max_speed": {
                                          "v": "89",
                                          "raw": 89.0,
                                          "type": "value"
                                      }
                                  },
                                  {
                                      "to": {
                                          "v": "16:01 - KhP \"Lesnoe ozero\", Dernopol'e, gor. okrug Serpukhov, Moscow Oblast, Russia, 142279",
                                          "raw": 1601989300000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 54.9875133,
                                              "lng": 37.3093183
                                          }
                                      },
                                      "from": {
                                          "v": "13:34 - Selyatino, Naro-Fominskii gor. okrug, Moscow Oblast, Russia, 143370",
                                          "raw": 1601980444000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 55.5309966,
                                              "lng": 36.96738
                                          }
                                      },
                                      "time": {
                                          "v": "02:27",
                                          "raw": 8856.0,
                                          "type": "value"
                                      },
                                      "length": {
                                          "v": "95.79",
                                          "raw": 95.79,
                                          "type": "value"
                                      },
                                      "avg_speed": {
                                          "v": "39",
                                          "raw": 39.0,
                                          "type": "value"
                                      },
                                      "max_speed": {
                                          "v": "88",
                                          "raw": 88.0,
                                          "type": "value"
                                      }
                                  }
                              ],
                              "total": {
                                  "text": "In total:",
                                  "time": {
                                      "v": "10:33",
                                      "raw": 37980.0,
                                      "type": "value"
                                  },
                                  "length": {
                                      "v": "523.8",
                                      "raw": 523.8,
                                      "type": "value"
                                  },
                                  "avg_speed": {
                                      "v": "50",
                                      "raw": 50.0,
                                      "type": "value"
                                  },
                                  "max_speed": {
                                      "v": "94",
                                      "raw": 94.0,
                                      "type": "value"
                                  }
                              },
                              "header": "Oct 6, 2020 (Tue) : 7"
                          }
                      ],
                      "type": "table",
                      "header": "Trips",
                      "columns": [
                          {
                              "align": "left",
                              "field": "from",
                              "title": "Movement start",
                              "width": 4,
                              "weight": 3,
                              "highlight_min_max": false
                          },
                          {
                              "align": "left",
                              "field": "to",
                              "title": "Movement end",
                              "width": 4,
                              "weight": 3,
                              "highlight_min_max": false
                          },
                          {
                              "align": "right",
                              "field": "length",
                              "title": "Total trips length,\nkm",
                              "width": 1,
                              "weight": 0,
                              "highlight_min_max": false
                          },
                          {
                              "align": "right",
                              "field": "time",
                              "title": "Travel time",
                              "width": 1,
                              "weight": 0,
                              "highlight_min_max": false
                          },
                          {
                              "align": "right",
                              "field": "avg_speed",
                              "title": "Average speed,\nkm/h",
                              "width": 1,
                              "weight": 0,
                              "highlight_min_max": false
                          },
                          {
                              "align": "right",
                              "field": "max_speed",
                              "title": "Max. speed,\nkm/h",
                              "width": 1,
                              "weight": 0,
                              "highlight_min_max": false
                          }
                      ],
                      "column_groups": []
                  },
                  {
                      "rows": [
                          {
                              "v": "7",
                              "raw": 7.0,
                              "name": "Trips",
                              "highlight": false
                          },
                          {
                              "v": "523.8",
                              "raw": 523.8,
                              "name": "Total trips length, km",
                              "highlight": false
                          },
                          {
                              "v": "10:33",
                              "raw": 633.0,
                              "name": "Travel time",
                              "highlight": false
                          },
                          {
                              "v": "50",
                              "raw": 50.0,
                              "name": "Average speed, km/h",
                              "highlight": false
                          },
                          {
                              "v": "94",
                              "raw": 94.0,
                              "name": "Max. speed, km/h",
                              "highlight": false
                          },
                          {
                              "v": "515855",
                              "raw": 515855.0,
                              "name": "Odometer value *, km",
                              "highlight": false
                          }
                      ],
                      "type": "map_table",
                      "header": "Summary"
                  },
                  {
                      "text": "Odometer value at the end of the selected period.",
                      "type": "text",
                      "style": "small_print"
                  }
              ],
              "entity_ids": [
                  311852
              ],
              "additional_field": ""
          }
      ],
      "from": "2020-10-06 00:00:00",
      "to": "2020-10-06 23:59:59"
    }
    ```

* `report` - object. Body of the generated report. Its contents are plugin-dependent.

#### Errors

* 204 - Entity not found - if report with the specified ID not found.
* 229 - Requested data is not ready yet - if report exists, but its generation is still in progress.


### `status`

Returns a report generation status for the specified report id.

**required sub-user rights**: `reports`.

#### Parameters

| name      | description                            | type |
|:----------|:---------------------------------------|:-----|
| report_id | ID of a report that should be deleted. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/status' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "report_id": 1234567}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/report/tracker/status?hash=a6aa75587e5c59c32d347da438505fc3&report_id=1234567
    ```

#### Response

```json
{
  "success": true,
  "percent_ready": 75
}
```

* `percent_ready` - int. Report readiness in percent.

#### Errors

* 204 - Entity not found - if report with the specified ID not found.
