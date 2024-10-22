---
title: Getting Started
description: Overview of Navixy Raw IoT Data API.
---
# Navixy Raw IoT Data API

Navixy Raw IoT Data API is a powerful tool designed for developers and data engineers who need access to comprehensive, raw data from GPS and telematics devices. This API allows you to extract unprocessed data with high granularity, enabling detailed analysis and customized solutions. With the Navixy Raw IoT Data API, you can seamlessly integrate with our platform, retrieve essential data, and leverage it for various applications, including analytics, reporting, and data science.

## Overview

The structure of the Raw IoT Data API is mostly similar to the [Backend API](../backend-api/getting-started/introduction.md). If you're familiar with the basics of the user API, you will find this API intuitive and easy to work with. The Raw IoT Data API provides robust methods to access raw, unprocessed data, ensuring you can harness the full potential of your connected devices.

## Time Frame Limits

The Raw IoT Data API allows you to request raw data for periods ranging from one to several months, depending on your plan restrictions. The maximum time frame for data retrieval is determined by your subscription plan, with a common limit for lower tiers being 30 days from the current date. Data stored beyond this period cannot be requested through the Raw IoT Data API.

## Base URL

Raw IoT Data API resides in the `dwh` subsection of the API URL and does not belong to backend APIv2. You need to determine the URL to API calls like this:
* `https://api.eu.navixy.com/dwh/v1` for the European Navixy ServerMate platform.
* `https://api.us.navixy.com/dwh/v1` for the American Navixy ServerMate platform.

For example, to make raw data readings API request in the European Navixy ServerMate, you need to use this URL:

```
https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read
```

## Authentication and Authorization

### Authentication

Authentication is handled by the [Backend API](../backend-api/getting-started/authentication.md).

### Authorization

Requests to the Raw IoT Data API are made using a user session hash or API key. It can be passed as the Authorization HTTP header with the NVX auth scheme or within a `-d` (data) command.

Example:

=== "with Authorization header"

```shell
curl -X 'POST' \
  'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/get_inputs' \
  -H 'accept: text/csv' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: NVX 8a41497ed8e77fa68b9c4a9420971fdb' \
  -d '{"tracker_id": 123456'}'
```

=== "with hash"

```shell
curl -X 'POST' \
  'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/get_inputs' \
  -H 'accept: text/csv' \
  -H 'Content-Type: application/json' \
  -d '{"hash": "6dc7d304dec4434f4c4202ec42817f83","tracker_id": 123456}'
```

## Response Format

Depending on the API request, responses can be in `application/json` or `text/csv` content types.

### Errors

Errors are distinguished by HTTP status codes (>= 400) and follow [RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807).

Example:

```json
{
  "type": "errors/default/bad-request",
  "title": "Bad Request",
  "status": 400,
  "detail": "id: must be greater than or equal to 1"
}
```

#### Common Error Types

* `errors/default/bad-request` - Causes: missing or invalid parameter value.
* `errors/default/unauthorized` - Causes: missing `Authorization` header or credentials are insufficient or expired.

### Date/Time Formats

The API uses date/time formats according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). For detailed information on date/time formats and examples, refer to [Raw Data Request - Specifying Time Frame](../data-warehouse-api/guides/raw-data.md#specifying-time-frame).

## Examples

### Example of Getting Inputs

This example shows how to use the `get_inputs` method to retrieve available metering inputs and state fields of a device.

```shell
curl -X 'POST' \
  'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/get_inputs' \
  -H 'Content-Type: application/json' \
  -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "tracker_id": 123456
  }'
```

### Example of Reading Raw IoT Data

This example shows how to use the `read` method to fetch parsed raw data values received from tracking devices and decoded by the platform.

```shell
curl -X 'POST' \
  'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
  -H 'accept: text/csv' \
  -H 'Content-Type: application/json' \
  -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "tracker_id": "123456",
    "from": "2023-11-30T07:13:00.000Z",
    "to": "2023-11-30T07:15:00.000Z",
    "columns": [
      "lat",
      "lng",
      "speed",
      "inputs.ble_lls_level_1",
      "inputs.hw_mileage",
      "discrete_inputs.*"
    ]
  }'
```

By leveraging the Navixy Raw IoT Data API, developers and data engineers can access and analyze detailed raw data from their GPS and telematics devices, enabling a wide range of custom solutions and insights.