---
title: User settings 
description: CRUD actions for user settings.
---

# User settings

CRUD actions for user settings.


## settings object

```json
{
    "time_zone": "Europe/Amsterdam",
    "locale": "nl_NL",
    "measurement_system": "metric",
    "date_format": "ddMMyyyy_dots",
    "hour_mode": "TWENTY_FOUR_HOURS",
    "geocoder": "osm",
    "route_provider": "google",
    "translit": false
}
```

* `time_zone` - [enum](../../../../getting-started/introduction.md#data-types). ISO timezone ID.
* `locale` - [enum](../../../../getting-started/introduction.md#data-types). Locale code.
* `measurement_system` - [enum](../../../../getting-started/introduction.md#data-types). Measurement system. Can be "metric", "imperial", "us", "metric_gal_us" or "nautical".
* `date_format` - Optional [enum](../../../../getting-started/introduction.md#data-types). Date representation. Can be "ddMMyyyy_dots"("dd.MM.yyyy", "01.12.2021"), "ddMMyyyy_slashes"("dd/MM/yyyy", "01/12/2021"), "MMddyyyy_hyphens"("MM-dd-yyyy", "12-01-2021"), "yyyyMMdd_hyphens"("yyyy-MM-dd", "2021-12-01"), "dMMMy"("d MMM y", "1 Dec 2021") or "dMMMMy"("d MMMM y", "1 December 2021")
* `hour_mode` - Optional [enum](../../../../getting-started/introduction.md#data-types). Time representation. Can be "TWENTY_FOUR_HOURS" (24-hour clock, "HH:mm" or "HH:mm:ss", "17:45"/"17:45:46") or "TWELVE_HOURS" (12-hour clock, "h:mm a" or "h:mm:ss a", "5:45 PM"/"5:45:46 PM")
* `geocoder` - [enum](../../../../getting-started/introduction.md#data-types). Preferred geocoder type. Can be "google", "yandex", "progorod", "osm" or "locationiq".
* `route_provider` - [enum](../../../../getting-started/introduction.md#data-types). Preferred route finding provider. Can be "google", "progorod" or "osrm".
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


## API actions

API path: `/user/settings`.

### `read`

Reads current user's settings.

#### Parameters

Only API key `hash`.

#### Examples

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

#### Response

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


### `update`

Update current user's settings.

**required sub-user rights** for `balance_alert_settings` and `file_storage_settings`: `admin` (available only to master users).

#### Parameters

| name                   | description                                                                            | type                                              |
|:-----------------------|:---------------------------------------------------------------------------------------|:--------------------------------------------------|
| time_zone              | ISO timezone ID.                                                                       | [enum](../../../../getting-started/introduction.md#data-types) |
| locale                 | Locale code.                                                                           | [enum](../../../../getting-started/introduction.md#data-types) |
| measurement_system     | Measurement system. Can be "metric", "imperial", "us", "metric_gal_us" or "nautical".  | [enum](../../../../getting-started/introduction.md#data-types) |
| geocoder               | Preferred geocoder type. Can be "google", "yandex", "progorod", "osm" or "locationiq". | [enum](../../../../getting-started/introduction.md#data-types) |
| route_provider         | Preferred route finding provider. Can be "google", "progorod" or "osrm".               | [enum](../../../../getting-started/introduction.md#data-types) |
| translit               | `true` if sms notification should be transliterated, `false` otherwise.                | boolean                                           |
| balance_alert_settings | Object containing array of emails.                                                     | JSON object                                       |
| file_storage_settings  | Object containing file storage settings.                                               | JSON object                                       |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/settings/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "time_zone": "Europe/Amsterdam", "locale": "nl_NL", "measurement_system": "metric", "geocoder": "osm", "route_provider": "google", "translit": false, "balance_alert_settings": {"emails": ["email1@example.com", "email2@example.com"]}, "file_storage_settings": {"auto_overwrite": true}}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* [General](../../../../getting-started/errors.md#error-codes) types only.


### `file_storage/update`

Updates current user's file storage settings.

**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name                  | description                              | type        |
|:----------------------|:-----------------------------------------|:------------|
| file_storage_settings | Object containing file storage settings. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/settings/file_storage/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "file_storage_settings": {"auto_overwrite": true}}'
    ```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
