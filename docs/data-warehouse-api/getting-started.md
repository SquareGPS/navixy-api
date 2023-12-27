---
title: Getting Started
description: Overview of Navixy Data Warehouse API.
---

# Navixy Data Warehouse API

The structure of Data Warehouse API is mostly similar to [Backend API](../backend-api/getting-started.md), so if you're familiar with the basics of 
user API, this will be a great advantage.

***

## Base URL

Data Warehouse API resides in `dwh` subsection of API URL and does not belong to backend APIv2. You need to determine URL 
to API calls like this:
*  `https://api.eu.navixy.com/dwh/v1` for European Navixy ServerMate platform.
*  `https://api.us.navixy.com/dwh/v1` for American Navixy ServerMate platform.

For example, to make raw data readings API request in European Navixy ServerMate, you need to use this URL:

```
https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read
```

***

## Auth

***

### Authentication

Authentication is handled by [Backend API](../backend-api/how-to/get-api-key.md).

***

### Authorization

Requests to Data Warehouse API are made using user session hash or API key. It can be passed as the Authorization HTTP 
header with NVX auth scheme, or within a `-d` (data) command.

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

***

## Response format

Depending on the API request, the responses can be in application/json or CSV markdown content types.

***

### Errors

Errors are distinguished by HTTP status code (>= 400) and follow [RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807).

Example:

```json
{
  "type": "errors/default/bad-request",
  "title": "Bad Request",
  "status": 400,
  "detail": "id: must be greater than or equal to 1"
}
```

***

#### Common error types

* `errors/default/bad-request` - Causes: missing or invalid parameter value.
* `errors/default/unauthorized` - Causes: missing `Authorization` header or credentials are insufficient or expired.

***

### Date/time formats

According to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). Described details on date/time formats and examples in 
[Raw data request - date and time](./how-to/raw-data-request-date-and-time.md).

