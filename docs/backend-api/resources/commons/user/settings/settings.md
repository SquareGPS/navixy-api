---
title: User settings 
description: User settings
---

# User settings

API path: `/user/settings`.

CRUD actions for user settings.

`settings` type is JSON object:

```js
{
    "time_zone": "Europe/Amsterdam",  // ISO timezone id
    "locale": "nl_NL",                // locale code
    "measurement_system": "metric"    // measurement system ("metric", "imperial", "us" or "metric_gal_us")
    "geocoder": "osm",                // preferred geocoder type ("google", "yandex", "progorod", "osm" or "locationiq")
    "route_provider": "google",       // preferred route finding provider ("google", "progorod" or "osrm")
    "translit": false                 // true if sms notification should be transliterated, false otherwise
}
```

`balance_alert_settings` type is JSON object:

```js
{
    "emails": ["email1@example.com", "email2@example.com"]  // array of emails to send alert message about balance
                                                            // empty array means disclaimer of notifications
}
```

`file_storage_settings` type is JSON object:

```js
{
    "auto_overwrite": <true|false> // default - false,
}
```

## read()

Read current user’s settings.

#### return

```js
{
    "success": true,
    "settings": ${settings},                             // JSON object
    "file_storage_settings": ${file_storage_settings},   // JSON object
    "balance_alert_settings": ${balance_alert_settings}, // JSON object
    "first_user_balance_warning_period": "7d",           // first interval to send alert
    "second_user_balance_warning_period": "2d"           // second interval to send alert
}
```

Where `settings`, `balance_alert_settings` and `file_storage_settings` described above.

**required subuser rights** for **balance\_alert\_settings** and **file\_storage\_settings** fields: admin (available only to master users)


## update()

Update current user’s settings.

#### parameters

*   **time_zone** – ISO timezone id
*   **locale** – locale code
*   **measurement_system** – measurement system (“metric”, “imperial”, “us” or "metric_gal_us"). If field is not passed then default (**metric**) system will be used.
*   **geocoder** – preferred geocoder type (“google”, “yandex”, “progorod”, “osm” or "locationiq")
*   **route_provider** – preferred route finding provider (“google”, “progorod” or “osrm”)
*   **translit** – true if sms notification should be transliterated, false otherwise
*   **balance\_alert\_settings** – JSON object containing array of emails
*   **file\_storage\_settings** – JSON object

**required subuser rights** for **balance\_alert\_settings** and **file\_storage\_settings**: admin (available only to master users)

See examples above.

#### return

```json
{ "success": true }
```

## file_storage/update()

Update current user’s file storage settings

**required subuser rights:** admin (available only to master users)

#### parameters

*    `file_storage_settings` – JSON object.

#### errors

*    13 – Operation not permitted – if user has insufficient rights
