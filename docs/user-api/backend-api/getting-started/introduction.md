---
title: Introduction
description: Getting started with Navixy Backend API
---
Welcome to the Navixy Backend API documentation. This guide is designed to help developers integrate third-party 
solutions with the Navixy platform. Here, you will find comprehensive information on API calls, workflows, and best practices.

## Overview

The Navixy API provides a set of RESTful endpoints that allow you to interact with various entities such as geofences, rules, objects, and more. The API calls for CRUD and other operations with these entities follow a consistent naming convention, making it easier to understand and use.

## Standard Workflow

To give you a clear idea of how to work with the Navixy API, let's go through a standard workflow using a common example – requesting track points data.

1. **Determine the URL to API calls**:
    - Depending on the physical location of the platform, the base URL will be:

        * `https://api.eu.navixy.com/v2` for European Navixy platform;
        * `https://api.us.navixy.com/v2` for North American Navixy Splatform;
        * `https://api.your_domain` for self-hosted (On-Premise) installations.

2. **[Obtain hash of an API key](authentication.md)**:
    - Authenticate and obtain a user key via the authentication call.

3. **Get objects lists with `tracker/list`**:
    - Example API call:
    ```sh
    $ curl -X POST 'https://api.navixy.com/v2/tracker/list' \
        -H 'Content-Type: application/json' \
        -d '{
              "hash": "your_api_key_hash"
            }'
    ```

4. **Get track lists with `track/list`**:
    - Example API call:
    ```sh
    $ curl -X POST 'https://api.navixy.com/v2/track/list' \
        -H 'Content-Type: application/json' \
        -d '{
              "hash": "your_api_key_hash",
              "tracker_id": 12345
            }'
    ```

5. **Get the track itself with `track/read`**:
    - Example API call:
    ```sh
    $ curl -X POST 'https://api.navixy.com/v2/track/read' \
        -H 'Content-Type: application/json' \
        -d '{
              "hash": "your_api_key_hash",
              "track_id": 67890
            }'
    ```

## API Base URL

Depending on the physical location of the platform, use one of the following base URLs:

- **European Navixy platform**:
  ```
  https://api.eu.navixy.com/v2
  ```

- **North American Navixy platform**:
  ```
  https://api.us.navixy.com/v2
  ```

- **Self-hosted (On-Premise) installations**:
  ```
  https://api.your_domain
  ```

For example, to make a `user/auth` API call on the European Navixy ServerMate platform, you should use the URL:
```
https://api.eu.navixy.com/v2/user/auth
```

## API Calls Format

API calls follow a consistent notation:
```
/resource/sub_resource/action(parameter1, parameter2, [parameter3])
```

Parameters can be passed in different ways:
- **HTTP POST `application/json`**: Recommended
- **HTTP POST `application/x-www-form-urlencoded`**: Parameters in the request body
- **HTTP GET**: Not recommended, should be used only for idempotent requests with small parameter size

### Examples

#### HTTP POST `application/json`

```sh
$ curl -X POST '[api_base_url]/resource/sub_resource/action' \
    -H 'Content-Type: application/json' \
    -d '{"param1": "value1", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### HTTP POST `application/x-www-form-urlencoded`

```sh
$ curl -X POST '[api_base_url]/resource/sub_resource/action' \
    -d 'param1=value' \
    -d 'hash=a6aa75587e5c59c32d347da438505fc3'
```

#### HTTP GET

```sh
$ curl '[api_base_url]/resource/sub_resource/action?param1=value1&hash=a6aa75587e5c59c32d347da438505fc3'
```

## Request and Response Format

To make an API call, send a `POST` request to:
```
[api_base_url]/resource/action/
```

The response will be given with `application/json` content type, even for errors. Response fields and object structure are specific to the API call.

### Ensuring Compatibility

Our API evolves over time, and new methods and JSON object fields are added. We strive to maintain backward compatibility with legacy API clients. However, you **must** ensure that any unsupported JSON object fields by your app are **ignored**, and that your application can handle new JSON fields without breaking. Also, to reduce response size, JSON fields that are NULL are omitted. Your JSON parser should handle missing JSON fields as if they were NULL.

## Authorization and Access Levels

Unless otherwise noted, every API call requires a valid API Key hash. This hash can be passed in one of the following ways:

1. **As a `hash` parameter of the request body** (root-level property for `application/json`).
2. **As a `hash` parameter of the HTTP query string**.
3. **As a value of the HTTP header `Authorization`** in the following form:
   ```
   Authorization: NVX SessionHashValue
   ```

## Data Types

| Type       | Description                                                                                                                                                                                                                                                                                                                                             |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `bool`     | Boolean: logical type (`true` or `false`).                                                                                                                                                                                                                                                                                                              |
| `byte`     | Signed 8 bits integer in range `[-128 .. 128]`.                                                                                                                                                                                                                                                                                                         |
| `short`    | Signed 16 bits integer in range `[-32,768 .. 32,767]`.                                                                                                                                                                                                                                                                                                  |
| `int`      | Signed 32 bits integer in range `[-2,147,483,648 .. 2,147,483,647]`.                                                                                                                                                                                                                                                                                    |
| `long`     | Signed 64 bits integer in range `[-9,223,372,036,854,775,808 .. 9,223,372,036,854,775,807]`.                                                                                                                                                                                                                                                            |
| `float`    | Signed 32 bits float number `[3.40282347 x 10^38, 1.40239846 x 10^-45]`.                                                                                                                                                                                                                                                                                |
| `double`   | Signed 64 bits float number `[1.7976931348623157 x 10^308, 4.9406564584124654 x 10^-324]`.                                                                                                                                                                                                                                                              |
| `string`   | String literals. See validation rules below.                                                                                                                                                                                                                                                                                                            |
| `enum`     | String literals from a predefined set.                                                                                                                                                                                                                                                                                                                  |
| `date/time`| String containing date/time in defined formats.                                                                                                                                                                                                                                                                                                         |
| `local_time`| String containing local time in `HH:mm:ss` format.                                                                                                                                                                                                                                                                                                      |
| `location` | JSON object containing geographical coordinates, e.g., `{"lat": 34.178868, "lng": -118.599672}`.                                                                                                                                                                                                                                                        |
| `locale`   | String in format `language[_country]`, where `language` is an <a href="https://www.loc.gov/standards/iso639-2/php/English_list.php" target="_blank">[ISO 639 alpha-2]</a> language code, and `country` is an <a href="https://en.wikipedia.org/wiki/ISO_3166-2#Current_codes" target="_blank">ISO 3166 alpha-2</a> country code, e.g., `en_US` or `de`. |

## String Validation Rules

This validation ensures that the provided string adheres to specific content rules. The rules may vary depending on the particular field being validated. The string is checked for the following criteria:

- Empty strings or null values: may be allowed or restricted depending on the specific field.
- Character types:

    * Regular spaces are always allowed (Unicode category "Zs").
    * Other whitespace characters (tabs, line breaks, etc.): may be allowed or restricted depending on the specific field.
    * Control characters (category "Cc" except whitespace characters): not allowed.
    * Private Use characters (category "Co"): not allowed.
    * Surrogate characters (category "Cs"): not allowed.
    * Characters requiring more than 3 bytes in UTF-8 encoding (e.g., some emojis): may be allowed or restricted depending on the specific field.
    * All other characters are allowed.

- Strings consisting entirely of whitespace may be considered invalid for some fields.

## Date/Time Formats

Date/time type can be represented with the following formats:
- `yyyy-MM-dd HH:mm:ss` format (in user's timezone), default
- <a href="https://en.wikipedia.org/wiki/ISO_8601" target="_blank">[ISO 8601]</a> `yyyy-MM-dd'T'HH:mm:ssZZ`

To use ISO 8601 date/time format, pass `true` to:

1. `iso_datetime` parameter of the request body (root-level property for `application/json`).
2. `iso_datetime` parameter of the HTTP query string.
3. HTTP header `NVX-ISO-DateTime`.

### Example

#### JSON request body parameter

```sh
$ curl -X POST '[api_base_url]/resource/sub_resource/action' \
    -H 'Content-Type: application/json' \
    -d '{"iso_datetime": true, "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### Form request parameter

```sh
$ curl -X POST '[api_base_url]/resource/sub_resource/action' \
    -d 'iso_datetime=true' \
    -d 'hash=a6aa75587e5c59c32d347da438505fc3'
```

#### HTTP Header

```sh
$ curl -X POST '[api_base_url]/resource/sub_resource/action' \
    -H 'Content-Type: application/json' \
    -H 'NVX-ISO-DateTime: true' \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

### Response Example with Fixed Offset Date/Time

```json
{
  "success": true,
  "user_time": "2014-07-09T07:50:58+05:00",
  "list": [
    {
      "type": "odometer",
      "value": 100500.1,
      "update_time": "2014-03-06T13:57:00+05:00"
    }
  ]
}
```

### Response Example with UTC Date/Time

```json
{
  "success": true,
  "user_time": "2014-07-09T02:50:58Z",
  "list": [
    {
      "type": "odometer",
      "value": 100500.1,
      "update_time": "2014-03-06T17:57:00Z"
    }
  ]
}
```

## Next Steps

- [Authentication](authentication.md): Learn how to authenticate and obtain a user key 
- [errors](errors.md): Understand how to handle errors in the Navixy API


