---
title: User actions
description: A user account lets you start working with the platform as well as customize your experience within it. Contains user object structure and API calls to interact with users.
---

# User

A user account lets you start working with the platform as well as customize your experience within it. Contains user object structure and API calls to interact with users.



## User object structure

```json
{
    "success": true,
    "paas_id": 7,
    "paas_settings": <paas_settings>,
    "user_info": {
        "id": 43568,
        "login": "demo@navixy.com",
        "title": "John Smith",
        "phone": "79123456789",
        "creation_date": "2016-05-20 01:10:34",
        "balance": 74.31,
        "bonus": 0,
        "locale": "en_US",
        "demo": true,
        "verified" : true,
        "legal_type" : "individual",
        "default_geocoder": "google",
        "route_provider": "google",
        "time_zone": "America/New_York",
        "measurement_system" : "metric",
        "date_format": "ddMMyyyy_dots",
        "hour_mode": "TWENTY_FOUR_HOURS",
        "tin": "2345678239",
        "iec": "",
        "post_country": "USA",
        "post_region": "NY",
        "post_index": "10120",
        "post_city": "New York",
        "post_street_address": "1556 Broadway, suite 416",
        "registered_country": "USA",
        "registered_region": "NY",
        "registered_index": "10120",
        "registered_city": "New York",
        "registered_street_address": "1556 Broadway, suite 416",
        "first_name": "John",
        "middle_name": "Walker",
        "last_name": "Smith",
        "legal_name": "QWER Inc."
    },
    "master": {
        "id": 1234,
        "demo": false,
        "legal_type": "individual",
        "first_name": "David",
        "middle_name": "Middle",
        "last_name": "Blane",
        "legal_name": "Blah LLC",
        "title": "David Blane",
        "balance": 0.0,
        "bonus": 89.78
    },
    "tariff_restrictions": {
        "allowed_maps": ["roadmap","osm"]
    },
    "premium_gis": true,
    "features": ["branding_web"],
    "privileges": {
        "rights": ["tag_update"]
    },
    "user_menu": {
        "title": "menu-editor.default-preset",
        "account": [],
        "main": [],
        "applications": [],
        "footer": {
            "title": null,
            "items": []
        }
    }
}
```

* `paas_id` - int. Dealer ID.
* `paas_settings` - object. The same as `settings` in [/dealer/get_ui_config response](../dealer.md#get_ui_config).
* `user_info` - object. Info about user.
    * `id` - int. User ID.
    * `login` - string. User's login (in most cases it's an email address).
    * `title` - string. User first and last name or organization title.
    * `phone` - string. User phone (if not empty).
    * `creation_date` - [date/time](../../../getting-started/introduction.md#data-types). User registration date/time.
    * `balance` - float. User balance, max. 2 digits after dot. For sub-users, this field should be ignored.
    * `bonus` - float. User bonus, max. 2 digits after dot. For sub-users, this field should be ignored.
    * `locale` - [enum](../../../getting-started/introduction.md#data-types). User locale, for example "en_EN".
    * `demo` - boolean. `true` if this is a demo user, `false` otherwise.
    * `verified` - boolean. `true` if user email already verified.
    * `legal_type` - [enum](../../../getting-started/introduction.md#data-types). Can bed "legal_entity", "individual" or "sole_trader".
    * `default_geocoder` - [enum](../../../getting-started/introduction.md#data-types). User's default geocoder. Can be "google", "yandex",
     "progorod", "osm", or "locationiq".
    * `route_provider` - [enum](../../../getting-started/introduction.md#data-types). User's route provider. Can be "progorod", "google" or "osrm".
    * `time_zone` - [enum](../../../getting-started/introduction.md#data-types). User timezone name.
    * `measurement_system` - [enum](../../../getting-started/introduction.md#data-types). User's measurement system "metric", "imperial", "us", "metric_gal_us" or "nautical".
    * `date_format` - Optional [enum](../../../getting-started/introduction.md#data-types). Date representation. Can be "ddMMyyyy_dots"("dd.MM.yyyy", "01.12.2021"), "ddMMyyyy_slashes"("dd/MM/yyyy", "01/12/2021"), "MMddyyyy_hyphens"("MM-dd-yyyy", "12-01-2021"), "yyyyMMdd_hyphens"("yyyy-MM-dd", "2021-12-01"), "dMMMy"("d MMM y", "1 Dec 2021") or "dMMMMy"("d MMMM y", "1 December 2021")
    * `hour_mode` - Optional [enum](../../../getting-started/introduction.md#data-types). Time representation. Can be "TWENTY_FOUR_HOURS" (24-hour clock, "HH:mm" or "HH:mm:ss", "17:45"/"17:45:46") or "TWELVE_HOURS" (12-hour clock, "h:mm a" or "h:mm:ss a", "5:45 PM"/"5:45:46 PM")
    * `tin` - string. Taxpayer identification number aka "VATIN" or "INN".
    * `iec` - optional string. Industrial Enterprises Classifier aka "KPP". Used in Russia for legal entities.
    * `post_country` - string. Country part of user's post address.
    * `post_index` - string. Post index or ZIP code.
    * `post_region` - string. Region part of post address (oblast, state, etc.).
    * `post_city` - string. City from postal address.
    * `post_street_address` - string. Street address.
    * `registered_country` - string. Country part of user's registered address.
    * `registered_index` - string. Index part of user's registered address.
    * `registered_region` - string. Region part of user's registered address.
    * `registered_city` - string. City from registered address.
    * `registered_street_address` - string. User's registered address.
    * `first_name` - string. User's or contact person first name.
    * `middle_name` - string. User's or contact person middle name.
    * `last_name` - string. User's or contact person last name.
    * `legal_name` - optional string. A juridical name.
    * `master` - object. Returned only if current user is sub-user. All fields have same meaning as in "user_info", but for 
    master user's account.
    * `tariff_restrictions` - tariff restrictions object, for more info see [user/get_tariff_restrictions](#get_tariff_restrictions).
        * `allowed_maps` - string array. List of allowed maps.
    * `premium_gis` - boolean. `true` if a dealer has premium GIS tariff.
    * `features` - string array. Set of allowed [Dealer features](../dealer.md#dealer-features).
    * `privileges` - object only returned for sub-users. Describes effective sub-user privileges. 
    * `rights` - string array. A set of rights granted to sub-user. Described in [security group rights](../subuser/security_group.md#security-group-rights).
* `user_menu` - [User menu](../../../../../panel-api/resources/user/menu/preset.md#menu-preset). Menu structure for the current user.
    * `account` - [Menu item](../../../../../panel-api/resources/user/menu/preset.md#menu-item) array. Menu items for account management.
    * `applications` - [Menu item](../../../../../panel-api/resources/user/menu/preset.md#menu-item) array. Menu items for applications.



## API actions

API path: `/user`.

### `activate`

Activates previously registered user with the provided session hash 
(it is contained in activation link from email sent to user).
Available only to master users.

!!! attention 
    This call will receive only session hash from registration email.
    Any other hash will result in result error code 4 (User or API key not found or session ended).
    The only thing that API calls with a user session will work for is creating, 
    reading, and deleting API keys.

#### Response

```json
{ "success": true }
```

### `auth`

Tries to authenticate the user and get hash.

It does not need authentication/hash and is available at `UNAUTHORIZED` access level.

!!! note "It is strongly recommended using [API keys](../../../getting-started/authentication.md) instead of user session hash."

#### Parameters

| name      | description                                                                                            | type   | restrictions                            |
|:----------|:-------------------------------------------------------------------------------------------------------|:-------|:----------------------------------------|
| login     | User email as login (or demo login).                                                                   | string | not null.                               |
| password  | User password.                                                                                         | string | not null, 1 to 40 printable characters. |
| dealer_id | If specified, API will check that user belongs to this dealer, and if not, error 102 will be returned. | int    | optional.                               |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/auth' \
        -H 'Content-Type: application/json' \
        -d '{"login": "user@email.com", "password": "12@14Y$"}'
    ```

#### Response

=== "Default"

    ```json
    {
        "success": true,
        "type": "authenticated",
        "hash": "22eac1c27af4be7b9d04da2ce1af111b"
    }
    ```

    * `type` - [enum](../../../getting-started/introduction.md#data-types). Always `authenticated`. 
    * `hash` - string. Session hash.

=== "With 2FA enabled"

    ```json
    {
        "success": true,
        "type": "second_factor_required",
        "factor_type": "email",
        "hash": "22eac1c27af4be7b9d04da2ce1af111b"
    }
    ```

    * `type` - [enum](../../../getting-started/introduction.md#data-types). Always `second_factor_required`.
    * `factor_type` - [enum](../../../getting-started/introduction.md#data-types).
    Which type of the second factor is used.
    Only `email` is available at the moment.
    * `hash` - string. Session hash. Can be used only for [authentication code](./auth/code.md) actions

#### Errors

* 11 – Access denied - if dealer blocked.
* 102 – Wrong login or password.
* 103 – User not activated.
* 104 – Logins limit exceeded, please reuse existing sessions instead (see also user/session/renew).
* 105 – Login attempts limit exceeded, try again later.

### `get_info`

Gets user information and some settings.

#### Parameters

| name        | description                                                                            | type   | restrictions |
|:------------|:---------------------------------------------------------------------------------------|:-------|:-------------|
| application | If specified, the response will contain a description of the application's custom menu | string | optional     |

#### Examples

=== "cURL"

    ```shell
    curl -X GET '{{ extra.api_example_url }}/user/get_info' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
    ```

#### Response

```json
{
    "success": true,
    "paas_id": 7,
    "paas_settings": <paas_settings>,
    "user_info": {
        "id": 43568,
        "login": "demo@navixy.com",
        "title": "John Smith",
        "phone": "79123456789",
        "creation_date": "2016-05-20 01:10:34",
        "balance": 74.31,
        "bonus": 0,
        "locale": "en_US",
        "demo": true,
        "verified" : true,
        "legal_type" : "individual",
        "default_geocoder": "google",
        "route_provider": "google",
        "time_zone": "America/New_York",
        "measurement_system" : "metric",
        "date_format": "ddMMyyyy_dots",
        "hour_mode": "TWENTY_FOUR_HOURS",
        "tin": "2345678239",
        "iec": "",
        "post_country": "USA",
        "post_region": "NY",
        "post_index": "10120",
        "post_city": "New York",
        "post_street_address": "1556 Broadway, suite 416",
        "registered_country": "USA",
        "registered_region": "NY",
        "registered_index": "10120",
        "registered_city": "New York",
        "registered_street_address": "1556 Broadway, suite 416",
        "first_name": "John",
        "middle_name": "Walker",
        "last_name": "Smith",
        "legal_name": "QWER Inc."
    },
    "master": {
        "id": 1234,
        "demo": false,
        "legal_type": "individual",
        "first_name": "David",
        "middle_name": "Middle",
        "last_name": "Blane",
        "legal_name": "Blah LLC",
        "title": "David Blane",
        "balance": 0.0,
        "bonus": 89.78
    },
    "tariff_restrictions": {
        "allowed_maps": ["roadmap","osm"]
    },
    "premium_gis": true,
    "features": ["branding_web"],
    "privileges": {
        "rights": ["tag_update"]
    },
    "user_menu": <customizable_user_menu>
}
```

* `user_object` - for more info see [user object structure](#user-object-structure).

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.

### `get_tariff_restrictions`

Gets user plan restrictions.

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/get_tariff_restrictions' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/get_tariff_restrictions?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "value": {
         "allowed_maps": ["roadmap","osm"]
    }
}
```

* `allowed_maps` - string array. List of allowed maps.

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.


### `logout`

Destroys current user session.
Works only with standard user session (not with API key).

#### Parameters

Only session `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/logout' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/logout?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.

### `resend_activation`

Sends a new activation link to user.

It does not need authentication/hash and is available at `UNAUTHORIZED` access level.

#### Parameters

| name  | description         | type   | restrictions |
|:------|:--------------------|:-------|:-------------|
| login | User login (email). | string | not null.    |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/resend_activation' \
        -H 'Content-Type: application/json' \
        -d '{"login": "user@login.com"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/resend_activation?login=user@login.com
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – user with a passed login not found.
* 209 - Failed sending email – can't send email.
* 264 - Timeout not reached – previous activation link generated less than 5 minutes ago (or other configured on server timeout).
    ```json
    {
      "success": false,
      "status": {
          "code": 264,
          "description": "Timeout not reached"
      },
      "timeout": "PT5M",
      "remainder": "PT4M31.575S"
    }
    ```
    * `timeout` - string. timeout between sending activation links in ISO 8601 duration format.
    * `remainder` - string. remaining time to next try in ISO 8601 duration format
* 265 - Already done – user already activated and verified.
