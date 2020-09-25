---
title: Waybill
description: Waybill
---

# Waybill

API path: `/track/waybill`.

### download

Downloads a waybill report DOCX file for tracks of the specified tracker and time period.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| from | From time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone). | string date/time | "2020-09-23 03:24:00" |
| to | To time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone). Specified date must be after "from" date. | string date/time | "2020-09-23 06:24:00" |
| filter | Optional, default=`true`. If `true`, tracks which are too short (in terms of length and number of points) will be omitted from resulting list. | boolean | true |
| split | Optional, default=`true`. If `false`, all tracks will be merged into single one. | boolean | false |
| include_gsm_lbs | Optional, default=`true`. If `false`, GSM LBS tracks will be filtered out. | boolean | false |
| cluster_single_reports | Optional, default=`false`. If `true`, single point reports will be clustered by its coordinates. | boolean | false |
| type | Should be one of "form3", "form3ext", "form4c". | string enum | "form4c" |
| fill_history | If `false`, only basic info about driver/garage/vehicle will be filled (no trips or parkings). | boolean | false |
| fill_odometer | Optional, default=`false`. If `true`, mileage readings will be inserted in appropriate fields of the document. | boolean | false |
| series | Optional. Waybill series. | string | "A-1" |
| number | Waybill number. | string | "123456789" |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/track/waybill/download' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456", "from": "2020-09-23 03:24:00", "to": "2020-09-23 06:24:00", "type": "form3", "fill_history": "false", "number": "1234567"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/track/waybill/download?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&from=2020-09-23 03:24:00&to=2020-09-23 06:24:00&type=form3&fill_history=false&number=1234567
    ```

#### response

A docx file with the waybill.

#### errors

* 236 (Feature unavailable due to tariff restrictions) – if one of the trackers has tariff without "app_fleet" feature.
