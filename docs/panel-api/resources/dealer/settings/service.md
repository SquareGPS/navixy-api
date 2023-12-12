---
title: Service
description: API calls to read and update panel's service settings. 
---

# Service

API calls to read and update panel's service settings.

***

## Service settings object

```json
{
    "service_title": "monitoring service",
    "locale": "en_US",
    "demo_login": "demo",
    "demo_password": "demo",
    "maps": ["osm", "wikimapia", "yandexpublic", "osmmapnik"],
    "default_map": {
      "type": "osm",
      "location": {
        "lat": 33.0, 
        "lng": 22.0
      },
      "zoom": 2
    },
    "currency": "EUR",
    "payment_link": "http://payme.ru",
    "promo_url": "http://monitoring.com/about",
    "google_client_id": "io54p54ijy54",
    "domain": "track.agent.com",
    "favicon": "http://test.com/favicon.ico",
    "app_logo": "paas/5001/app_logo.png",
    "logo": "paas/5001/logo.png",
    "document_logo": "paas/5001/document_logo.png",
    "login_wallpaper": "paas/5001/login.png",
    "desktop_wallpaper": "http://test.com/test.jpg",
    "login_footer": "All rights reserved.",
    "allow_registration": true,
    "show_mobile_apps": true,
    "default_user_settings": {
      "geocoder": "google",
      "route_provider": "progorod",
      "measurement_system": "metric",
      "translit": false
    },
    "display_model_features_link": false,
    "limited_domain": false,
    "allowed_maps": ["osm", "wikimapia", "yandexpublic", "osmmapnik"],
    "color_theme": "aqua",
    "app_color_theme": "blue_1",
    "privacy_policy_link": "http://privacy-policy-url",
    "tos": "Terms Of Service text",
    "no_register_commands": false,
    "default_user_time_zone": "Europe/London"
}
```

* `service_title` - string. Service name.
* `locale` - [enum](../../../../backend-api/getting-started.md#data-types). Default locale of the dealer.
* `demo_login` - string. If not empty, demo button will use this login to authorize.
* `demo_password` - string. If not empty, demo button will use this password to authorize.
* `maps` - [enum](../../../../backend-api/getting-started.md#data-types) array. Maps available in monitoring system. When a domain is platform owner's subdomain then only free maps are available.
* `default_map` - default map settings object.
    * `type` - [enum](../../../../backend-api/getting-started.md#data-types). Default map code.
    * `location` - location object. Default location to show on the map when monitoring opens. Location object described
     in [data types description section](../../../../backend-api/getting-started.md#data-types).
    * `zoom` - int. Default zoom level to use.
* `currency` - [enum](../../../../backend-api/getting-started.md#data-types). Code of the currency which can be shown in UI.
* `payment_link` - string. A link to dealer's payment system. Can be null or empty.
* `promo_url` - string. Customizable "About company" URL. Can be null or empty.
* `google_client_id` - string. Google Maps client ID (not supported by the interface yet).
* `domain` - string. Domain which will be used for monitoring system.
* `favicon` - string. Nullable, path or URL to dealer's interface favicon.
* `app_logo` - string. Nullable, path or URL to dealer's mobile app logotype.
* `logo` - string. Nullable, path or URL to dealer's logotype.
* `document_logo` - string. Nullable, path or URL to dealer's logotype for documents.
* `login_wallpaper` - string. Nullable, path or URL to dealer's interface login wallpaper.
* `desktop_wallpaper` - string. Nullable, path to dealer's interface wallpaper.
* `login_footer` - string. Nullable, footer which will be included in login page.
* `allow_registration` - boolean. If `true` allows self-registration of users.
* `show_mobile_apps` - boolean. If `true` when entering the service from a mobile device or tablet, users will be prompted
 to download the mobile application or continue using the mobile web UI.
* `default_user_settings` - default user settings object.
    * `geocoder` - string. Default geocoder.
    * `route_provider` - string. Default route provider.
    * `measurement_system` - [enum](../../../../backend-api/getting-started.md#data-types). Measurement system.
    * `translit` - boolean. SMS transliteration. If `true` allows you to reduce the number of characters in an SMS message
     by replacing the characters of the national alphabet with close Latin ones.
* `display_model_features_link` - boolean. When `true` shows in model info link to navixy.com (UI option).
* `limited_domain` - boolean. If `true`, paas domain has limitations.
* `allowed_maps` - [enum](../../../../backend-api/getting-started.md#data-types). List of maps available for selection in "maps" list.
* `color_theme` - string. 128 chars max. Color theme code or empty string (for default theme).
* `app_color_theme` - string. 128 chars max. Mobile app color theme code or empty string (for default theme).
* `privacy_policy_link` - string. A link to privacy policy.
* `tos` - string. Terms Of Service text.
* `no_register_commands` - boolean. If `true` then do not send commands to devices on activation.
* `default_user_time_zone` - string. [Time zone id](../../timezone.md) for new users to be created via [user/upload](../../user/index.md#upload).
  Also, this zone will be selected by default when creating a new user in the Navixy Admin Panel.

***

## API actions

API path: `panel/dealer/settings/service`.

### read

Gets current monitoring service settings.

*required permissions*: `service_settings: "read"`.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/settings/service/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/dealer/settings/service/read?hash=fa7bf873fab9333144e171372a321b06
    ```

#### response

```json
{
  "success": true,
  "value": {
       "service_title": "monitoring service",
       "locale": "en_US",
       "demo_login": "demo",
       "demo_password": "demo",
       "maps": ["osm", "wikimapia", "yandexpublic", "osmmapnik"],
       "default_map": {
         "type": "osm",
         "location": {
           "lat": 33.0, 
           "lng": 22.0
         },
         "zoom": 2
       },
       "currency": "EUR",
       "payment_link": "http://payme.ru",
       "promo_url": "http://monitoring.com/about",
       "google_client_id": "io54p54ijy54",
       "domain": "track.agent.com",
       "favicon": "http://test.com/favicon.ico",
       "app_logo": "paas/5001/app_logo.png",
       "logo": "paas/5001/logo.png",
       "document_logo": "paas/5001/document_logo.png",
       "login_wallpaper": "paas/5001/login.png",
       "desktop_wallpaper": "http://test.com/test.jpg",
       "login_footer": "All rights reserved.",
       "allow_registration": true,
       "show_mobile_apps": true,
       "default_user_settings": {
         "geocoder": "google",
         "route_provider": "progorod",
         "measurement_system": "metric",
         "translit": false
       },
       "display_model_features_link": false,
       "limited_domain": false,
       "allowed_maps": ["osm", "wikimapia", "yandexpublic", "osmmapnik"],
       "color_theme": "aqua",
       "app_color_theme": "blue_1",
       "privacy_policy_link": "http://privacy-policy-url",
       "tos": "Terms Of Service text",
       "no_register_commands": false,
       "default_user_time_zone": "America/New_York"
  }
}
```

* `value` - [Service settings object](#service-settings-object) described above.

#### errors

[General](../../../../backend-api/getting-started.md#error-codes) types only.

***

### update

Updates monitoring service settings for the current dealer. 

Note: wallpapers, logos and favicons cannot be edited here. 

*required permissions*: `service_settings: "update"`.

#### parameters

| name                        | description                                                                     | type                                                                |
|:----------------------------|:--------------------------------------------------------------------------------|:--------------------------------------------------------------------|
| service_title               | Service name.                                                                   | string                                                              |
| locale                      | Default locale of the dealer.                                                   | [enum](../../../../backend-api/getting-started.md#data-types)       |
| demo_login                  | If not empty, demo button will use this login to authorize.                     | string                                                              |
| demo_password               | If not empty, demo button will use this password to authorize.                  | string                                                              |
| maps                        | Maps available in monitoring system.                                            | [enum](../../../../backend-api/getting-started.md#data-types) array |
| default_map                 | Default map settings object.                                                    | JSON object                                                         |
| currency                    | Code of the currency which will be shown in UI.                                 | [enum](../../../../backend-api/getting-started.md#data-types)       |
| payment_link                | A link to dealer's payment system. Can be null or empty.                        | string                                                              |
| promo_url                   | Customizable "About company" URL. Can be null or empty.                         | string                                                              |
| google_client_id            | Google maps client ID.                                                          | string                                                              |
| domain                      | Domain which will be used for monitoring system.                                | string                                                              |
| login_footer                | Nullable, footer which will be included in login page.                          | string                                                              |
| allow_registration          | If `true` allows self-registration of users.                                    | boolean                                                             |
| show_mobile_apps            | If `true` shows mobile apps to users who opens mobile web UI.                   | boolean                                                             |
| default_user_settings       | Default user settings object.                                                   | JSON object                                                         |
| display_model_features_link | When `true` shows in model info link to navixy.com (UI option).                 | boolean                                                             |
| limited_domain              | If `true`, paas domain has limitations.                                         | boolean                                                             |
| allowed_maps                | List of maps available for selection in "maps" list.                            | [enum](../../../../backend-api/getting-started.md#data-types)       |
| color_theme                 | 128 chars max. Color theme code or empty string (for default theme).            | string                                                              |
| app_color_theme             | 128 chars max. Mobile app color theme code or empty string (for default theme). | string                                                              |
| privacy_policy_link         | A link to privacy policy.                                                       | string                                                              |
| tos                         | Terms Of Service text.                                                          | string                                                              |
| no_register_commands        | If `true` then do not send commands to devices on activation.                   | boolean                                                             |
| default_user_time_zone      | Time zone by default for new users.                                             | string                                                              |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/settings/notification/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "service_title": "monitoring service", "locale": "en_US", "demo_login": "demo", "demo_password": "demo", "maps": ["osm", "wikimapia", "yandexpublic", "osmmapnik"], "default_map": {"type": "osm", "location": {"lat": 33.0, "lng": 22.0}, "zoom": 2}, "currency": "EUR", "payment_link": "http://payme.ru", "promo_url": "http://monitoring.com/about", "google_client_id": "io54p54ijy54", "domain": "track.agent.com", "login_footer": "All rights reserved.", "allow_registration": true, "show_mobile_apps": true, "default_user_settings": {"geocoder": "google", "route_provider": "progorod", "measurement_system": "metric", "translit": false}, "display_model_features_link": false, "limited_domain": false, "allowed_maps": ["osm", "wikimapia", "yandexpublic", "osmmapnik"], "color_theme": "aqua", "app_color_theme": "blue_1", "privacy_policy_link": "http://privacy-policy-url", "tos": "Terms Of Service text", "no_register_commands": false, "default_user_time_zone": "Europe/London"}'
    ```
    
#### response

```json
{
    "success": true
}
```

#### errors

* 247 - Entity already exists(409) - when `domain` already used by other dealer.
