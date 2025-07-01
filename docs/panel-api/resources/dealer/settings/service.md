---
title: Service
description: API calls to read and update panel's service settings.
---

# Service Settings

Service settings in Navixy allow administrators to configure and customize various aspects of the monitoring service. These settings control the appearance and functionality of the platform, such as default maps, user interfaces, branding elements, and user registration options. By adjusting these parameters, administrators can tailor the platform to better meet the needs of their users and reflect their company's branding and operational requirements.

## Service settings object

Let's explore the Service Settings object using the following example:

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

* `service_title` - string. Name of the service.
* `locale` - [enum](../../../../user-api/backend-api/#data-types). Default locale of the dealer.
* `demo_login` - string. Login used for demo authorization if not empty.
* `demo_password` - string. Password used for demo authorization if not empty.
* `maps` - [enum](../../../../user-api/backend-api/#data-types) array. Maps available in the monitoring system. Only free maps are available if the domain is the platform owner's subdomain.
* `default_map` - Default map settings object.
  * `type` - [enum](../../../../user-api/backend-api/#data-types). Default map code.
  * `location` - Location object. Default location to show on the map when monitoring opens. Described in the [data types description section](../../../../user-api/backend-api/#data-types).
  * `zoom` - int. Default zoom level to use.
* `currency` - [enum](../../../../user-api/backend-api/#data-types). Currency code shown in the UI.
* `payment_link` - string. Link to the dealer's payment system. Can be null or empty.
* `promo_url` - string. Customizable "About company" URL. Can be null or empty.
* `google_client_id` - string. Google Maps client ID (not supported by the interface yet).
* `domain` - string. Domain used for the monitoring system.
* `favicon` - string. Path or URL to the dealer's interface favicon. Nullable.
* `app_logo` - string. Path or URL to the dealer's mobile app logotype. Nullable.
* `logo` - string. Path or URL to the dealer's logotype. Nullable.
* `document_logo` - string. Path or URL to the dealer's logotype for documents. Nullable.
* `login_wallpaper` - string. Path or URL to the dealer's interface login wallpaper. Nullable.
* `desktop_wallpaper` - string. Path to the dealer's interface wallpaper. Nullable.
* `login_footer` - string. Footer included on the login page. Nullable.
* `allow_registration` - boolean. Allows self-registration of users if `true`.
* `show_mobile_apps` - boolean. Prompts users to download the mobile app or continue using the mobile web UI when entering the service from a mobile device or tablet if `true`.
* `default_user_settings` - Default user settings object.
  * `geocoder` - string. Default geocoder.
  * `route_provider` - string. Default route provider.
  * `measurement_system` - [enum](../../../../user-api/backend-api/#data-types). Measurement system.
  * `date_format` - Optional [enum](../../../../user-api/backend-api/#data-types). Date representation.
  * `hour_mode` - Optional [enum](../../../../user-api/backend-api/#data-types). Time representation.
  * `translit` - boolean. SMS transliteration. Reduces the number of characters in an SMS by replacing the characters of the national alphabet with close Latin ones if `true`.
* `display_model_features_link` - boolean. Shows a link to navixy.com in model info if `true` (UI option).
* `limited_domain` - boolean. Indicates whether the PaaS domain has limitations if `true`.
* `allowed_maps` - [enum](../../../../user-api/backend-api/#data-types). List of maps available for selection in the "maps" list.
* `color_theme` - string. Max 128 characters. Color theme code or empty string (for the default theme).
* `app_color_theme` - string. Max 128 characters. Mobile app color theme code or empty string (for the default theme).
* `privacy_policy_link` - string. Nullable, privacy policy link (it may be empty).
* `tos` - string. Nullable, terms of service text (it may be empty).
* `no_register_commands` - boolean. Prevents sending commands to devices on activation if `true`.
* `default_user_time_zone` - string. [Time zone ID](../../timezone.md) for new users created via [user/upload](broken-reference). This time zone is also selected by default when creating a new user in the Navixy Admin Panel.

## API actions

API path: `panel/dealer/settings/service`.

### read

Gets current monitoring service settings.

_required permissions_: `service_settings: "read"`.

#### Parameters

Only session `hash`.

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST '{{ extra.api_example_url }}/panel/dealer/settings/service/read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
{{ extra.api_example_url }}/panel/dealer/settings/service/read?hash=fa7bf873fab9333144e171372a321b06
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

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

* `value` - [Service settings object](service.md#service-settings-object) described above.

#### Errors

[General](../../../../user-api/backend-api/errors.md#error-codes) types only.

### update

Updates monitoring service settings for the current dealer.

Note: wallpapers, logos and favicons cannot be edited here.

_required permissions_: `service_settings: "update"`.

#### Parameters

| name                           | description                                                                     | type                                                       |
| ------------------------------ | ------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| service\_title                 | Service name.                                                                   | string                                                     |
| demo\_login                    | If not empty, demo button will use this login to authorize.                     | string                                                     |
| demo\_password                 | If not empty, demo button will use this password to authorize.                  | string                                                     |
| maps                           | Maps available in monitoring system.                                            | [enum](../../../../user-api/backend-api/#data-types) array |
| default\_map                   | Default map settings object.                                                    | JSON object                                                |
| currency                       | Code of the currency which will be shown in UI.                                 | [enum](../../../../user-api/backend-api/#data-types)       |
| payment\_link                  | A link to dealer's payment system. Can be null or empty.                        | string                                                     |
| promo\_url                     | Customizable "About company" URL. Can be null or empty.                         | string                                                     |
| google\_client\_id             | Google maps client ID.                                                          | string                                                     |
| domain                         | Domain which will be used for monitoring system.                                | string                                                     |
| login\_footer                  | Nullable, footer which will be included in login page.                          | string                                                     |
| allow\_registration            | If `true` allows self-registration of users.                                    | boolean                                                    |
| show\_mobile\_apps             | If `true` shows mobile apps to users who opens mobile web UI.                   | boolean                                                    |
| default\_user\_settings        | Default user settings object.                                                   | JSON object                                                |
| display\_model\_features\_link | When `true` shows in model info link to navixy.com (UI option).                 | boolean                                                    |
| limited\_domain                | If `true`, paas domain has limitations.                                         | boolean                                                    |
| allowed\_maps                  | List of maps available for selection in "maps" list.                            | [enum](../../../../user-api/backend-api/#data-types)       |
| color\_theme                   | 128 chars max. Color theme code or empty string (for default theme).            | string                                                     |
| app\_color\_theme              | 128 chars max. Mobile app color theme code or empty string (for default theme). | string                                                     |
| privacy\_policy\_link          | A link to privacy policy.                                                       | string                                                     |
| tos                            | Terms Of Service text.                                                          | string                                                     |
| no\_register\_commands         | If `true` then do not send commands to devices on activation.                   | boolean                                                    |
| default\_user\_time\_zone      | Time zone by default for new users.                                             | string                                                     |

#### Example

cURL

{% code overflow="wrap" %}
```sh
curl -X POST '{{ extra.api_example_url }}/panel/dealer/settings/notification/update' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "fa7bf873fab9333144e171372a321b06", "service_title": "monitoring service", "locale": "en_US", "demo_login": "demo", "demo_password": "demo", "maps": ["osm", "wikimapia", "yandexpublic", "osmmapnik"], "default_map": {"type": "osm", "location": {"lat": 33.0, "lng": 22.0}, "zoom": 2}, "currency": "EUR", "payment_link": "http://payme.ru", "promo_url": "http://monitoring.com/about", "google_client_id": "io54p54ijy54", "domain": "track.agent.com", "login_footer": "All rights reserved.", "allow_registration": true, "show_mobile_apps": true, "default_user_settings": {"geocoder": "google", "route_provider": "progorod", "measurement_system": "metric", "translit": false}, "display_model_features_link": false, "limited_domain": false, "allowed_maps": ["osm", "wikimapia", "yandexpublic", "osmmapnik"], "color_theme": "aqua", "app_color_theme": "blue_1", "privacy_policy_link": "http://privacy-policy-url", "tos": "Terms Of Service text", "no_register_commands": false, "default_user_time_zone": "Europe/London"}'
```
{% endcode %}

#### Response

```json
{
  "success": true
}
```

#### Errors

* 247 - Entity already exists(409) - when `domain` already used by other dealer.
