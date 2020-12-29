---
title: User settings 
description: CRUD actions for user settings.
---

# User settings

CRUD actions for user settings.

API path: `/user/settings`.

`settings` type is JSON object:

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

* `time_zone` - string enum. ISO timezone id.
* `locale` - string enum. Locale code.
* `measurement_system` - string enum. Measurement system. Can be "metric", "imperial", "us" or "metric_gal_us".
* `geocoder` - string enum. Preferred geocoder type. Can be "google", "yandex", "progorod", "osm" or "locationiq".
* `route_provider` - string enum. Preferred route finding provider. Can be "google", "progorod" or "osrm".
* `translit` - boolean. `true` if sms notification should be transliterated, `false` otherwise.

`balance_alert_settings` type is JSON object:

```json
{
    "emails": ["email1@example.com", "email2@example.com"]
}
```

* `emails` - array of string. List of emails to send alert message about balance. Empty array means disclaimer of notifications.

`file_storage_settings` type is JSON object:

```json
{
    "auto_overwrite": true
}
```

* `auto_overwrite` - boolean. If `true` new files will replace old ones when file storage is full. Default is `false`.

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

### update

Update current user's settings.

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| time_zone | ISO timezone id. | string enum |
| locale | Locale code. | string enum |
| measurement_system | Measurement system. Can be "metric", "imperial", "us" or "metric_gal_us". | string enum |
| geocoder | Preferred geocoder type. Can be "google", "yandex", "progorod", "osm" or "locationiq". | string enum |
| route_provider | Preferred route finding provider. Can be "google", "progorod" or "osrm". | string enum |
| translit | `true` if sms notification should be transliterated, `false` otherwise. | boolean |
| balance_alert_settings | Object containing array of emails. | JSON object |
| file_storage_settings | Object containing file storage settings. | JSON object |

**required sub-user rights** for `balance_alert_settings` and `file_storage_settings`: `admin` (available only to master users).

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
