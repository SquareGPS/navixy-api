---
title: Getting Started
description: Overview of Navixy Backend API
---

# Navixy Backend API


## General

Each API resource semantically corresponds to some entity, for example: 
geofences, rules, objects, etc. The API calls for CRUD and other operations 
with these entities have similar names regardless the resource used: list, read, create, delete.

## Standard workflow (example)

Let's describe standard workflow for API developer using very simple and most 
common example — requesting the track points data:

1.  Determine [URL to API calls](#api-base-url).
1.  Authorize with [`user/auth`](resources/commons/user/index.md#auth). 
    This API method [will return the hash](./how-to/get-session-hash.md) 
    you should use for all your next API calls.
1.  Get objects lists with [`tracker/list`](./how-to/get-tracker-list.md).
1.  Get track lists with [`track/list`](resources/tracking/track/index.md#list).
1.  Get the track itself: [`track/read`](resources/tracking/track/index.md#read).

In other words, to start working with API, the developers should have API call 
description (as provided herein), and know user login and password.

## API base URL

In the all examples used placeholder `[api_url]`. 
Depending on the physical location of the platform it will be:

*  `https://api.eu.navixy.com/v2` for European Navixy ServerMate platform.
*  `https://api.us.navixy.com/v2` for American Navixy ServerMate platform.
*  `https://api.your_domain` for the self-hosted (On-Premise) installations.

For example, to make [`user/auth`](resources/commons/user/index.md#auth) 
API call on the European Navixy ServerMate, you should use the URL: 

    https://api.eu.navixy.com/v2/user/auth

## API calls format

Notation used in this doc:

    /resource/sub_resource/action(parameter1,parameter2,[parameter3])

Which means that you should use the following URL:

    [api_base_url]/resource/sub_resource/action

with named parameters:

*   parameter1
*   parameter2
*   parameter3 is optional

Parameters can be passed in the: 

* `HTTP POST application/json` with JSON content, **recommended**
* `HTTP POST application/x-www-form-urlencoded` with parameters in the request body 
* `HTTP GET` - **not recommended**, should be used only for idempotent requests with small parameters size

=== "HTTP POST `application/json`"
    ```abap
    $ curl -X POST '[api_base_url]/resource/sub_resource/action' \
      -H 'Content-Type: application/json' \ 
      -d '{"param1": "value1", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP POST `application/x-www-form-urlencoded`"
    ```abap
    $ curl -X POST '[api_base_url]/resource/sub_resource/action' \
      -d 'param1=value' \
      -d 'hash=a6aa75587e5c59c32d347da438505fc3' 
    ```

=== "HTTP GET"
    ```abap
    $ curl '[api_base_url]/resource/sub_resource/action?param1=value1&hash=a6aa75587e5c59c32d347da438505fc3'
    ```

!!! warning "[Hash](./how-to/get-session-hash.md) is required for most API calls to identify user."

Typical actions:

*   `list` – list all resource entities with IDs and minimum additional info
*   `read` – read one entity by ID
*   `update` – update one entity by ID
*   `delete` – delete one entity by ID

### Request and response format

To make API call, for example, `resource/action` send `POST` request to 

    [api_base_url]/resource/action/

The response will be given with `application/json` content type, even errors 
(see [error handling](#error-handling)). Response fields and object structure 
is specific to API call.

!!! warning "Ensuring compatibility"
    Our API evolves over time, and new methods and JSON object fields are being added.
    We are doing our best to ensure our API remains backwards compatible with legacy API clients. 
    However, you **must** ensure that any JSON object fields which are not supported 
    by your app are **ignored**, and that in event if new JSON fields are returned, 
    your application will not break. Also, sometimes, to reduce response size, 
    JSON fields which are NULL are omitted. Your JSON parser should handle 
    missing JSON fields as if they were NULL.

!!! note "For example"
    To read [user's tracker list](./how-to/get-tracker-list.md) 
    use `[api_base_url]/tracker/list/?hash=a6aa75587e5c59c32d347da438505fc3` and get response:
    ```json
    {
      "success": true,
      "list": [
        {
          "id": 560,
          "label": "GV55",
          "group_id": 12,
          "avatar_file_name": "super-avatar.jpg",
          "source": {
            "id": 2915,
            "model": "gv55lite",
            "blocked": false,
            "tariff_id": 2,
            "phone": "111",
            "status_listing_id": 333,
            "creation_date": "2014-02-02",
            "device_id": "888888888888888"
          },
          "tag_bindings": [
            {
              "tag_id": 1,
              "ordinal": 1
            }
          ],
          "clone": true
        },
        {
          "id": 2799,
          "label": "2799",
          "group_id": 0,
          "source": {
            "id": 2692,
            "model": "m7",
            "blocked": true,
            "tariff_id": 5,
            "phone": null,
            "status_listing_id": null,
            "creation_date": "2006-02-10",
            "device_id": "333333333333333"
          },
          "tag_bindings": [
            {
              "tag_id": 9,
              "ordinal": 3
            }
          ],
          "clone": false
        }
      ]
    }
    ```

Or error if hash is wrong:
```json
{
  "success": false,
  "status": {
    "code": 4,
    "description": "User not found or session ended"
  }
}
```

### HTTP codes

If `success` is `true`, HTTP code is always `200 OK` (unless otherwise stated).
If there is an error, HTTP code is `400 BAD REQUEST` (may vary depending on error type) 
(see [error](#error-codes)).

### Authorization and access levels

Unless otherwise noted, every API call requires a valid user session hash
(A String containing 32 hexademical characters) that can be passed (in order of lookup priority):

1. As `hash` parameter of the request body (root-level property for `application/json`).
2. As `hash` parameter of the HTTP query string.
3. As value of the HTTP header `Authorization` in the following form:
```
Authorization: NVX SessionHashValue
```
Following is pseudogrammar that illustrates the construction of the `Authorization` request header:
```
Authorization = "NVX" + " " + SessionHashValue ;
SessionHashValue = 32 hexademical characters;
```


Session hash can be obtained via `user/auth` API call:

=== "cURL"
    ```abap
    $ curl -X POST '[api_base_url]/user/auth' \
           -H 'Content-Type: application/json' \ 
           -d '{"login": "demo", "password": "demo"}'
    ```

=== "GET"
    This method is not recommended. Just for example:

    [api_base_url]/user/auth?login=demo&password=demo

### Data types

*   `bool`, boolean - logical type: `true` of `false`. 
*   `byte` - signed 8 bits integer in range `[-128 .. 128]`.
*   `short` - signed 16 bits integer in range `[-32,768 .. 32,767]`.
*   `int`, integer - signed 32 bits integer in range `[-2,147,483,648 .. 2,147,483,647]`.
*   `long` - signed 64 bits integer in range 
    `[-9,223,372,036,854,775,808 .. 9,223,372,036,854,775,807]`.
*   `float` - signed 32 bits float number `[3.40282347 x 10^38, 1.40239846 x 10^-45]`.
*   `double` - signed 64 bits float number 
    `[1.7976931348623157 x 10^308, 4.9406564584124654 x 10^-324]`.
*   `string` - string literals.
*   `enum` - string literals from predefined set.
*   `date/time` – is a string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user’s timezone).
*   `local_time` – is a string containing local time in `HH:mm:ss` format.
*   `location` – is json object contains geographical coordinates, e.g.
```json
{"lat": 56.827001, "lng": 60.594296}
```
*   `locale` – string in format `language\[_country\]`, where `language` is 
    [ISO 639 alpha-2](https://www.loc.gov/standards/iso639-2/php/English_list.php) language code, 
    and `country` is [ISO 3166 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-2#Current_codes) 
    country code, e.g. `en_US` or `ru`. User interface support only language codes: 
    `ru, en, es, ar, de, pt, ro and uk`.

### Constants

*   **maxHistoryLimit** = 1000 – maximum count of history entries from [listing requests](./resources/commons/history/history_tracker.md)
*   **maxReportTimeSpan** = 120 days – maximum interval in for most requests


### Error handling

If an error occurs, API returns special error response. You can also detect error by checking 
HTTP response code. If it’s not `200 OK`, you should parse and handle response body as an error response.
In the event of error occurs, the response will be in the following format:
```json
{
  "success": false,
  "status": {
    "code": 1,
    "description": "Database error"
  }
}
```
where `code` is one on the [error codes](#error-codes).

#### Error codes

Default HTTP code is 400. Common error codes (should be handled for all API calls) 
are 1-100 and resource or action specific errors are 101-300.

|code|description|HTTP code|
|--- |--- |--- |
|1|Database error|500|
|2|Service Auth error|403|
|3|Wrong user hash||
|4|User not found or session ended||
|5|Wrong request format||
|6|Unexpected error|500|
|7|Invalid parameters||
|8|Queue service error, try again later|503|
|9|Too large request|412|
|11|Access denied|403|
|12|Dealer not found||
|13|Operation not permitted|403|
|14|Database unavailable|503|
|15|Too many requests (rate limit exceeded)|429|
|101|In demo mode this function is disabled|403|
|102|Wrong login or password||
|103|User not activated||
|111|Wrong handler||
|112|Wrong method||
|201|Not found in database||
|202|Too many points in zone||
|203|Delete entity associated with||
|204|Entity not found|404|
|206|Login already in use||
|207|Invalid captcha||
|208|Device blocked|403|
|209|Failed sending email||
|210|Geocoding failed||
|211|Requested time span is too big||
|212|Requested limit is too big||
|213|Cannot perform action: the device is offline||
|214|Requested operation or parameters are not supported by the device||
|215|External service error||
|217|List contains nonexistent entities||
|218|Malformed external service parameters||
|219|Not allowed for clones of the device|403|
|220|Unknown device model||
|221|Device limit exceeded|403|
|222|Plugin not found||
|223|Phone number already in use||
|224|Device ID already in use||
|225|Not allowed for this legal type|403|
|226|Wrong ICCID||
|227|Wrong activation code||
|228|Not supported by sensor||
|229|Requested data is not ready yet|404|
|230|Not supported for this entity type||
|231|Entity type mismatch|409|
|232|Input already in use||
|233|No data file||
|234|Invalid data format||
|235|Missing calibration data||
|236|Feature unavailable due to tariff restrictions|402|
|237|Invalid tariff||
|238|Changing tariff is not allowed|403|
|239|New tariff doesn't exist|404|
|240|Not allowed to change tariff too frequently|403|
|241|Cannot change phone to bundled sim. Contact tech support.||
|242|There were errors during content validation||
|243|Device already connected.||
|244|Duplicate entity label.||
|245|New password must be different||
|246|Invalid user ID||
|247|Entity already exists|409|
|248|Wrong password||
|249|Operation available for clones only|403|
|250|Not allowed for deleted devices|403|
|251|Insufficient funds|403|
|252|Device already corrupted||
|253|Device has clones||
|254|Cannot save file|500|
|255|Invalid task state||
|256|Location already actual||
|257|Registration forbidden|403|
|258|Bundle not found|404|
|259|Payments count not comply with summary||
|260|Payments sum not comply with summary||
|261|Entity has external links|403|
|262|Entries list is missing some entries or contains nonexistent entries||
|263|No change needed, old and new values are the same||
|264|Timeout not reached|403|
|265|Already done|403|
|266|Cannot perform action for the device in current status|403|
|267|Too many entities||
|268|Over quota|402|
|269|Invalid file state||
|270|Too many sensors of same type already exist||
|271|File over max size|413|
