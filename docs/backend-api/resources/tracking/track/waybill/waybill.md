---
title: /waybill
description: /waybill
---

## download()
Download a waybill report DOCX file for tracks of the specified tracker and time period.

#### parameters:
* **tracker_id** - **int**. ID of the tracker (aka “object_id”). Tracker must belong to authorized user and must not be blocked.
* **from** - **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user’s timezone)
* **to** - **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user’s timezone). Specified date must be after “from” date
* **filter** - **boolean**. (optional, default=true) If true, tracks which are too short (in terms of length and number of points) will be omitted from resulting list.
* **split** - **boolean**. (optional, default=true) If false, all tracks will be merged into single one.
* **include_gsm_lbs** - **boolean**. (optional, default=true) If false, GSM LBS tracks will be filtered out.
* **cluster_single_reports** - **boolean**. (optional, default=false) If true, single point reports will be clustered by its coordinates.
* **type** - **string**. Should be one of “form3”, “form3ext”, “form4c”
* **fill_history** - **boolean**. If false, only basic info about driver/garage/vehicle will be filled (no trips or parkings)
* **fill_odometer** - **boolean**. (optional, default=false) If true, mileage readings will be inserted in appropriate fields of the document
* **series** - **string**. (optional) Waybill series
* **number** - **string**. Waybill number

#### return:
A docx file with the waybill.

#### errors:
*   236 (Feature unavailable due to tariff restrictions) – if one of the trackers has tariff without “app_fleet” feature
