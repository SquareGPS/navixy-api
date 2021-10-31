---
title: User settings 
description: CRUD actions for user settings.
---

# User settings

CRUD actions for user settings.

***

## settings object

```json
{
    "time_zone": "Europe/Amsterdam",
    "locale": "nl_NL",
    "measurement_system": "metric",
    "geocoder": "osm",
    "route_provider": "google",
    "translit": false
}
```

* `time_zone` - [enum](../../../../getting-started.md#data-types). ISO timezone id.
* `locale` - [enum](../../../../getting-started.md#data-types). Locale code.
* `measurement_system` - [enum](../../../../getting-started.md#data-types). Measurement system. Can be "metric", "imperial", "us", "metric_gal_us" or "nautical".
* `geocoder` - [enum](../../../../getting-started.md#data-types). Preferred geocoder type. Can be "google", "yandex", "progorod", "osm" or "locationiq".
* `route_provider` - [enum](../../../../getting-started.md#data-types). Preferred route finding provider. Can be "google", "progorod" or "osrm".
* `translit` - boolean. `true` if sms notification should be transliterated, `false` otherwise.

`balance_alert_settings` type is JSON object:

```json
{
    "emails": ["email1@example.com", "email2@example.com"]
}
```

* `emails` - string array. List of emails to send alert message about balance. Empty array means disclaimer of notifications.

`file_storage_settings` type is JSON object:

```json
{
    "auto_overwrite": true
}
```

* `auto_overwrite` - boolean. If `true` new files will replace old ones when file storage is full. Default is `false`.

***

## API actions

API path: `/user/settings`.

### read

Reads current user's settings.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/settings/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/settings/read?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "settings": {
        "time_zone": "Europe/Amsterdam",
        "locale": "nl_NL",
        "measurement_system": "metric",
        "geocoder": "osm",
        "route_provider": "google",
        "translit": false
    },
    "file_storage_settings": {
         "auto_overwrite": true
    },
    "balance_alert_settings": {
         "emails": ["email1@example.com", "email2@example.com"]
    },
    "first_user_balance_warning_period": "7d",
    "second_user_balance_warning_period": "2d"
}
```

* `first_user_balance_warning_period` - string. The first interval to send alert. "7d" means send the first alert warning 7 days before.
* `second_user_balance_warning_period` - string. The second interval to send alert. Send the second alert warning n days before.
* Where `settings`, `balance_alert_settings` and `file_storage_settings` described above.

**required sub-user rights** for `balance_alert_settings` and `file_storage_settings` fields: `admin` (available only to master users).

***

### update

Update current user's settings.

**required sub-user rights** for `balance_alert_settings` and `file_storage_settings`: `admin` (available only to master users).

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| time_zone | ISO timezone id. | [enum](../../../../getting-started.md#data-types) |
| locale | Locale code. | [enum](../../../../getting-started.md#data-types) |
| measurement_system | Measurement system. Can be "metric", "imperial", "us", "metric_gal_us" or "nautical". | [enum](../../../../getting-started.md#data-types) |
| geocoder | Preferred geocoder type. Can be "google", "yandex", "progorod", "osm" or "locationiq". | [enum](../../../../getting-started.md#data-types) |
| route_provider | Preferred route finding provider. Can be "google", "progorod" or "osrm". | [enum](../../../../getting-started.md#data-types) |
| translit | `true` if sms notification should be transliterated, `false` otherwise. | boolean |
| balance_alert_settings | Object containing array of emails. | JSON object |
| file_storage_settings | Object containing file storage settings. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/settings/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "time_zone": "Europe/Amsterdam", "locale": "nl_NL", "measurement_system": "metric", "geocoder": "osm", "route_provider": "google", "translit": false, "balance_alert_settings": {"emails": ["email1@example.com", "email2@example.com"]}, "file_storage_settings": {"auto_overwrite": true}}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* [General](../../../../getting-started.md#error-codes) types only.

***

### file_storage/update

Updates current user's file storage settings.

**required sub-user rights:** `admin` (available only to master users).

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| file_storage_settings | Object containing file storage settings. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/settings/file_storage/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "file_storage_settings": {"auto_overwrite": true}}'
    ```

#### errors

* 13 – Operation not permitted – if user has insufficient rights.
