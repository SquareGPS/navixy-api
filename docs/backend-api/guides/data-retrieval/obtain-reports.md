
Reports offer essential insights to effectively manage your fleet or mobile workforce. At times, you may need to extract report data for use in external applications or to generate custom business reports, such as those detailing trip information alongside fuel consumption, drains, and refills. Follow these steps to obtain report information using the Navixy API.

## Generate Report

To receive data for processing, you first need to generate the report. This can be done using the [`report/tracker/generate`](../../resources/commons/report/report_tracker.md#generate) call.

Necessary parameters for this call:

* `from` - A string containing [date/time](../../getting-started/introduction.md#datetime-formats). Data in the report will be from this moment.
* `to` - A string containing [date/time](../../getting-started/introduction.md#datetime-formats). The specified date must be after the `from` date. Data in the report will be up to this moment.
* `title` - Report title. If null, the default title will be used.
* `trackers` - List of [tracker IDs](../../resources/tracking/tracker/index.md#list) to be included in the report (if the report is by trackers).
* `employees` - List of [employee IDs](../../resources/field_service/employee/index.md#list) to be included in the report (if the report is by employees).
* `time_filter` - An object containing daily time and weekday limits for processed data, e.g., `{"to":"18:00", "from":"12:00", "weekdays":[1,2,3,4,5]}`.
* `plugin` - A plugin object. See the list of all [report plugins](../../resources/commons/plugin/report_plugins.md).

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/report/tracker/generate' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "title": "Trip report", "trackers": [669673], "from": "2020-10-05 00:00:00", "to": "2020-10-06 23:59:59", "time_filter": {"from": "00:00:00", "to": "23:59:59", "weekdays": [1,2,3,4,5,6,7]}, "plugin": {"hide_empty_tabs": true, "plugin_id": 4, "show_seconds": false, "include_summary_sheet_only": false, "split": true, "show_idle_duration": false, "show_coordinates": false, "filter": true, "group_by_driver": false}}'
    ```

The response will include the generated report ID:

```json
{
  "success": true,
  "id": 222
}
```

## Retrieve Report

To obtain the generated report data in JSON format, use the `report/tracker/retrieve` call.

Use the `report_id` from the previous call response.

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

You will receive the report in JSON format:

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
                                          "v": "02:39 - Downtown Los Angeles, CA, USA",
                                          "raw": 1601941188000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 34.040713,
                                              "lng": -118.246769
                                          }
                                      },
                                      "from": {
                                          "v": "00:47 - Santa Monica, CA, USA",
                                          "raw": 1601934439000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 34.019454,
                                              "lng": -118.491191
                                          }
                                      },
                                      "time": {
                                          "v": "01:52",
                                          "raw": 6749.0,
                                          "type": "value"
                                      },
                                      "length": {
                                          "v": "24.30",
                                          "raw": 24.30,
                                          "type": "value"
                                      },
                                      "avg_speed": {
                                          "v": "13",
                                          "raw": 13.0,
                                          "type": "value"
                                      },
                                      "max_speed": {
                                          "v": "27",
                                          "raw": 27.0,
                                          "type": "value"
                                      }
                                  },
                                  {
                                      "to": {
                                          "v": "05:10 - Hollywood, Los Angeles, CA, USA",
                                          "raw": 1601950218000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 34.092809,
                                              "lng": -118.328661
                                          }
                                      },
                                      "from": {
                                          "v": "03:11 - Downtown Los Angeles, CA, USA",
                                          "raw": 1601943083000.0,
                                          "type": "value",
                                          "location": {
                                              "lat": 34.040713,
                                              "lng": -118.246769
                                          }
                                      },
                                      "time": {
                                          "v": "01:58",
                                          "raw": 7135.0,
                                          "type": "value"
                                      },
                                      "length": {
                                          "v": "8.5",
                                          "raw": 8.5,
                                          "type": "value"
                                      },
                                      "avg_speed": {
                                          "v": "4.3",
                                          "raw": 4.3,
                                          "type": "value"
                                      },
                                      "max_speed": {
                                          "v": "19",
                                          "raw": 19.0,
                                          "type": "value"
                                      }
                                  }
                              ],
                              "total": {
                                  "text": "In total:",
                                  "time": {
                                      "v": "03:50",
                                      "raw": 13740.0,
                                      "type": "value"
                                  },
                                  "length": {
                                      "v": "32.8",
                                      "raw": 32.8,
                                      "type": "value"
                                  },
                                  "avg_speed": {
                                      "v": "8.5",
                                      "raw": 8.5,
                                      "type": "value"
                                  },
                                  "max_speed": {
                                      "v": "27",
                                      "raw": 27.0,
                                      "type": "value"
                                  }
                              },
                              "header": "Oct 6, 2020 (Tue) : 2"
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
                              "v": "2",
                              "raw": 2.0,
                              "name": "Trips",
                              "highlight": false
                          },
                          {
                              "v": "32.8",
                              "raw": 32.8,
                              "name": "Total trips length, km",
                              "highlight": false
                          },
                          {
                              "v": "03:50",
                              "raw": 230.0,
                              "name": "Travel time",
                              "highlight": false
                          },
                          {
                              "v": "8.5",
                              "raw": 8.5,
                              "name": "Average speed, km/h",
                              "highlight": false
                          },
                          {
                              "v": "27",
                              "raw": 27.0,
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

## Deleting Reports

Once you have received and processed the report information, you can delete the generated report to clean up resources. Use the `report/tracker/delete` call.

Use the `report_id` from the `generate` call response.

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