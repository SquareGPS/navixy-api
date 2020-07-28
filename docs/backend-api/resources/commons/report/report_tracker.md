---
title: /report/tracker
description: /report/tracker
---

# /report/tracker

## delete(…)

Delete report from db.

*required subuser rights*: reports

#### parameters:

`report_id`

#### return:

```json
{
    "success": true
}
```

#### errors:

* 101 – In demo mode this function is disabled


## download(…)

Retrieve generated report as a file.

**required subuser rights**: reports

#### parameters:

*   report_id
*   format

(also, there is hidden boolean parameter named "headless". If you, for some reason, need report without title page and TOC, set it to "true", otherwise - don't). Currently, 'pdf', 'xls' and 'xlsx' formats is supported.

#### return:

A report rendered to file (standard file download).


#### errors:

*   204 - Entity not found (if report with the specified id was not found)
*   229 - Requested data is not ready yet (if report exists, but its generation is still in progress)



## generate(…)

Requests a report generation with the specified parameters. **required subuser rights**: reports

#### parameters:

name|description|type
---|---|---
from|A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone)|String
to|A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone). Specified date must be after "from" date|String
title|Report title. Default title will be used if null|String
geocoder|Which geocoder to use. See [geocoder/](../../tracking/geocoder.md)|String
trackers|list of tracker's ids to be included in report (if report is by trackers)|integer
employees|list of employees' ids to be included in report (if report is by employees)|integer
time_filter|An object which contains everyday time and weekday limits for processed data, e.g. {"to":"18:00", "from":"12:00", "weekdays":\[1,2,3,4,5\]} |Object
plugin|a plugin parameter object (see below)|JSON object

#### Parameter object fields:

Part of parameters are plugin-specific. See ["Tracker report plugins"](../plugin/report_plugins.md) section. Common parameters are:

name|description|type
---|---|---
plugin_id|An id of a tracker report plugin which will be used to generate report.|Integer
show_seconds|Flag to define whether time values in report should have format with seconds. true - show seconds, false - don't show seconds|boolean

#### plugin example:

    plugin:{
        "details_interval_minutes":60,
        "plugin_id": 9,
        "show_seconds": false,
        "graph_type": "time",
        "smoothing":false,
        "sensors":[
            {
                "tracker_id":tracker_id,
                "sensor_id":sensor_id
            }
        ]
    }

#### return:

```js
{
    "success": true,
    "id": 222 // (int) id of the report queued for generation. 
              // Can be used to request report generation status and to retrieve generated report
}
```

#### errors:
*   15 (Too many requests / rate limit exceeded) - the number of reports created by one user in parallel is limited.
*   211 (Requested time span is too big) - interval from 'from' to 'to' is bigger then max allowed time span (see response)
    ```js
    {
        "success": false,
        "status": {
            "code": 211,
            "description": "Requested time span is too big"
        },
        "max_time_span": "P90D" // ISO-8601 interval
    }
    ```
*   217 (List contains nonexistent entities) - when one or more of tracker ids belong to nonexistent tracker (or to a tracker belonging to different user)
*   222 (Plugin not found) - when specified report plugin is not found
*   236 (Feature unavailable due to tariff restrictions) - when one of the trackers has tariff with disabled reports - ("has_reports" is false)



## list(…)

Returns info about all available generated or in-progress reports.

**required subuser rights**: reports

#### return:

```js
{
    "success": true,"list": [
    {
        "from": <"from" parameter from generate(..)>, //string
        "to": <"to" parameter from generate(..)>, //string
        "created": <date when report was created, e.g. "2013-08-08 19:00:00">, //string
        "time_filter": <"time_filter" parameter from generate(..)>,
        "title": <report title, e.g. "Trip report">,
        "parameters": { 
            "geocoder": <geocoder which was used for report, e.g. "google">, //string
            "trackers": <list of tracker ids used for report, e.g. [3029]>,  //int[]
            "plugins": [ //list of parameters for all plugins which were used to generate report
                {
                    "plugin_id": <plugin id>, //int
                    <plugin-specific parameters>
                }, 
                ...
            ]
        }, 
        "percent": <report readiness in percent, e.g. 75>,   //int
        "id": <report id which can be used to retrieve or download report> //int
    },
    ...
]}
```

#### errors:

*   No specific errors.


## retrieve(…)

Retrieve generated report as JSON. 

**required subuser rights**: reports

#### parameters:

*   report_id

#### return:

```js
{
    "success": true,
    "report": <body of the generated report. Its contents are plugin-dependent>   //Object
}
```

#### errors:

*   204 - Entity not found (if report with the specified id was not found)
*   229 - Requested data is not ready yet (if report exists, but its generation is still in progress)


## status(…)
Returns a report generation status for the specified report id. **required subuser rights**: reports

#### parameters:

*   report_id

#### return:

```js
{
    "success": true,
    "percent_ready": <report readiness in percent, e.g. 75>   //int
}
```

#### errors:

*   204 - Entity not found (if report with the specified id was not found)