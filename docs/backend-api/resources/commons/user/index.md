---
title: User actions
description: User actions
---

# User

API path: `/user`.

User specific actions:

* [/user/activate](#activate)
* [/user/auth](#auth)
* [/user/get_info](#get_info)
* [/user/get_tariff_restrictions](#get_tariff_restrictions)
* [/user/resend_activation](#resend_activation)

### activate

Activates previously registered user with the provided session hash 
(it is contained in activation link from email sent to user).
Available only to master users.

!!! attention 
    This call will receive only session hash from registration email.
    Any other hash will result in result error code 4 (user not found or session ended).


#### response

```json
{ "success": true }
```

### auth

Try to authenticate user.

It does not need authentication/hash and is available at `UNAUTHORIZED` access level.

#### parameters

| name  | description | type  | restrictions |
| :---- | :----       | :---- | :----        |
|login | User email as login (or demo login) | string | not null |
|password | User password | string | not null, 1 to 40 printable characters |
|dealer_id | If specified, API will check that user belongs to this dealer, and if not, error 102 will be returned. | int | optional |


#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/user/auth' \
-H 'Content-Type: application/json' \ 
-d '{ "login": "test@email.com", "password": "password123456" }'
```

#### response

```js
{
    "success": true,
    "hash": <string> // session hash
}
```

#### errors

*   11 – Access denied (if dealer blocked)
*   102 – Wrong login or password
*   103 – User not activated
*   104 – Logins limit exceeded, please reuse existing sessions instead (see also user/session/renew)
*   105 – Login attempts limit exceeded, try again later


### get_info

Gets user information and some settings.

#### parameters

Only session `hash`.

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/user/get_info' \
-H 'Content-Type: application/json' \ 
-d '{ "hash": "a6aa75587e5c59c32d347da438505fc3" }'
```

Get basic user info.

#### response

```js
{
    "success": true,
    "paas_id": 7,
    "paas_settings": ${pass_settings},
    "user_info": {
        "id": 43568,                     // user id
        "login": "demo@navixy.com",      // user's login (in most cases it's an email address)
        "title": "John Smith",           // user first and last name or organization title
        "phone": "79123456789",          // user phone (if not empty)
        "creation_date": "2016-05-20 01:10:34", // user registration date/time
        "balance": 74.31,                // user balance, max. 2 digits after dot. For subusers, this field should be ignored
        "bonus": 0,                      // user bonus, max. 2 digits after dot. For subusers, this field should be ignored
        "locale": "en_US",               // user locale, for example "en_EN"
        "demo": true,                    // true if this is a demo user, false otherwise
        "verified" : true,               // true if user email already verified
        "legal_type" : "individual",     // string. "individual", "legal_entity" or "sole_trader"
        "default_geocoder": "google",    // user's default geocoder ("google", "yandex", "progorod", "osm", or "locationiq")
        "route_provider": "google",      // user's route provider ("progorod", "google" or "osrm")
        "time_zone": "America/New_York", // user timezone name
        "measurement_system" : "metric", // user's measurement system ("metric", "imperial" or "us")
        "tin": "2345678239",             // Taxpayer identification number aka "VATIN" or "INN"
        "iec": ${string},                // Industrial Enterprises Classifier aka "KPP". Used in Russia for legal entities. Optional.
        // postal address
        "post_country": "USA",           // country
        "post_region": "NY",             // region part of post address (oblast, state, etc.)
        "post_index": "10120",           // post index or ZIP code
        "post_city": "New York",         // city part of post address
        "post_street_address": "1556 Broadway, suite 416" // tail part of post address
        // legal (juridical) address
        "registered_country": "USA",           // country
        "registered_region": "NY",             // region part of post address (oblast, state, etc.)
        "registered_index": "10120",           // post index or ZIP code
        "registered_city": "New York",         // city part of post address
        "registered_street_address": "1556 Broadway, suite 416" // tail part of post address
        "first_name": "John",
        "middle_name": "Walker",
        "last_name": "Smith",
        "legal_name": "QWER Inc." // juridical name (optional)
    },
    "master": { // returned only if current user is sub-user. All fields have same meaning as in "user_info", but for master user's account
    "id": 1234, // same as in "user_info"
    "demo": false, // same as in "user_info"
    "legal_type": "individual", // same as in "user_info"
    "first_name": "David", // same as in "user_info"
    "middle_name": "Middle", // same as in "user_info"
    "last_name": "Blane", // same as in "user_info"
    "legal_name": "Blah LLC", // same as in "user_info"
    "title": "David Blane", // same as in "user_info"
        "balance": 0.0, // master user balance, max. 2 digits after dot. Only returned if subuser has "payment_create" right
        "bonus": 89.78, // master user bonus, max. 2 digits after dot. Only returned if subuser has "payment_create" right
    },
    "tariff_restrictions": ${tariff_restrictions},
    "premium_gis": true,
    "features": ["branding_web"],
    "privileges": { // only returned for subusers. Describes effective subuser privileges
        "rights": [
            "tag_update"
        ]
    }
}
```

where

* `paas_settings` same as `settings` in [/dealer/get_ui_config response](../dealer.md#get_ui_config),
* `tariff_restrictions` is JSON object same as in [/user/get_tariff_restrictions](#get_tariff_restrictions) response,
* `features` is a set of allowed [Dealer features](../dealer.md#dealer-features).


### get_tariff_restrictions

Gets user tariff restrictions.

#### parameters

Only session `hash`.

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/user/get_tariff_restrictions' \
-H 'Content-Type: application/json' \ 
-d '{ "hash": "a6aa75587e5c59c32d347da438505fc3" }'
```

#### response

```js
{
    "success": true,
    "value": ${tariff_restrictions}
}
```

where `tariff_restrictions` is JSON object:

```js
{
    "allowed_maps": [${map_name}, ...] // [string]. list of allowed maps, e.g. ["roadmap","osm"]
}
```

### logout

Destroys current user session.

#### parameters

Only session `hash`.

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/user/logout' \
-H 'Content-Type: application/json' \ 
-d '{ "hash": "a6aa75587e5c59c32d347da438505fc3" }'
```

#### response

```json
{ "success": true }
```


### resend_activation

Send new activation link to user.

It does not need authentication/hash and is available at `UNAUTHORIZED` access level.

#### parameters

| name  | description | type  | restrictions |
| :---- | :----       | :---- | :----        |
|login | user login (email) | string | not null |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/user/logout' \
-H 'Content-Type: application/json' \ 
-d '{ "login": "users_login" }'
```

#### response

```json
{ "success": true }
```

#### errors

*   201 (Not found in database) – user with passed login not found.
*   209 (Failed sending email) – can't send email.
*   264 (Timeout not reached) – previous activation link generated less than 5 minutes ago (or other configured on server timeout).
    ```js
    {
        "success": false,
        "status": {
            "code": 264,
            "description": "Timeout not reached"
        },
        "timeout": "PT5M", // timeout between sending activation links in ISO-8601 duration format
        "remainder": "PT4M31.575S" // remaining time to next try in ISO-8601 duration format
    }
    ```
*   265 (Already done) – user already activated and verified
