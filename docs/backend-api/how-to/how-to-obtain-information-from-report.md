---
title: How to obtain report's information
description: How to generate reports and obtain information from them in retrieved format
---

# How to obtain report's information

Reports consider information that can be used to manage your fleet successfully. Sometimes it is necessary to get a 
report's information that can be used in programs or specific reports in needs for business. For example, necessary 
information about trips + fuel consumption, drains and refills. 
Follow the next steps, to obtain report's information.

***

## Generate report

To receive data for processing, it must be generated. This can be done using a call 
[report/tracker/generate](../resources/commons/report/report_tracker.md#generate).

Parameters that necessary for this call:

* `from` - A string containing [date/time](../getting-started.md#datetime-formats). Data in a report will be 
from that moment.
* `to` - A string containing [date/time](../getting-started.md#datetime-formats). Specified date must be 
after `from` date. Data in a report will be till specified moment.
* `title` - Report title. Default title will be used if null.
* `trackers` - List of [trackers' ids](./get-tracker-list.md) to be included in report (if report is by trackers).
* `employees` - List of [employees' ids](../resources/field_service/employee/index.md#list) to be included in report 
(if report is by employees).
* `time_filter` - An object which contains everyday time and weekday limits for processed data,
 e.g. `{"to":"18:00", "from":"12:00", "weekdays":[1,2,3,4,5]}`.
* `plugin` -  A plugin object. The list of all [report plugins](../resources/commons/plugin/report_plugins.md).
  
API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Trip report", "trackers": [669673], "from": "2020-10-05 00:00:00", "to": "2020-10-06 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs": true, "plugin_id": 4, "show_seconds": false, "include_summary_sheet_only": false, "split": true, "show_idle_duration": false, "show_coordinates": false, "filter": true, "group_by_driver": false}}'
    ```

It will respond with generated report_id.

```json
{
  "success": true,
  "id": 222
}
```

***

## Retrieve report

To obtain all generated analytic data from the report in JSON format use 
[report/tracker/retrieve](../resources/commons/report/report_tracker.md#retrieve).

Use the report_id from the previous call response.

API request:

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

You will get the report in a JSON format:

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

***

## Deleting reports

When the information has been received and processed, there is no need to leave the generated report. It can be removed.
Use [report/tracker/delete](../resources/commons/report/report_tracker.md#delete).

Use the report_id from `generate` call response.

API request:

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


