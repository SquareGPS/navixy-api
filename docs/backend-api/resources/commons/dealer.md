---
title: Dealer
description: Contains API call to get dealer info and dealer-specific UI settings.
---

# Dealer

Contains API call to get dealer info and dealer-specific UI settings.


## API actions

API path: `/dealer`.

### `get_ui_config`

Gets dealer info and dealer-specific UI settings by a domain or hash.

It doesn't require authentication and available in **UNAUTHORIZED** access level.

#### Parameters

| name   | description                                                               | type   |
|:-------|:--------------------------------------------------------------------------|:-------|
| domain | Dealer's monitoring interface domain, e.g. "panel.navixy.com".            | string |
| hash   | Used instead of a domain to identify a dealer if there is a user session  | string |

Params `domain` and `hash` is not required both, but one of them must be specified.
If `hash` is specified the `domain` shouldn't be used.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/dealer/get_ui_config' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "domain": "panel.navixy.com"}'
    ```

#### Response

```json
{
    "success": true,
    "dealer": {
        "id": 5001,
        "ui_domain": "demo.navixy.com",
        "company_url": "navixy.com"
    },
    "settings": {
        "domain" : "demo.navixy.com",
        "service_title": "Navixy Demo",
        "locale": "at_AT",
        "demo_login": "demo",
        "demo_password": "demo",
        "maps": ["roadmap", "osm"],
        "default_map": {
            "type": "roadmap",
            "location": {
                "lat": 57.0,
                "lng": 61.0
            },
            "zoom": 10
        },
        "currency": "EUR",
        "payment_link": "http://site.de/pay.php", 
        "promo_url": "http://site.de/about/",
        "google_client_id": "clientID",
        "favicon": "paas/5001/custom.ico",
        "logo": "paas/5001/logo.png",
        "app_logo": "paas/5001/app_logo.png",
        "login_wallpaper": "paas/5001/login.png",
        "desktop_wallpaper": "http://test.com/test.jpg",
        "monitoring_logo": "http://test.com/test.jpg",
        "login_footer": "All rights reserved.",
        "allow_registration": true,
        "show_mobile_apps" : true,
        "show_call_notifications" : true,
        "default_user_settings": {
            "geocoder": "google",
            "route_provider": "progorod",
            "measurement_system": "metric",
            "translit": false
        },
        "display_model_features_link" : true,
        "color_theme": "aqua",
        "app_color_theme": "blue_1",
        "privacy_policy_link": "http://privacy-policy-url",
        "tos": "Terms Of Service text",
        "tracker_model_filter": {
            "exclusion": true,
            "values": []
        },
        "internal": {
            "light_registration": true,
            "demo_tracker_source_id": 14,
            "demo_tracker_label": "Demo tracker"
        },
        "no_register_commands": false
    },
    "demo_ends": "2014-01-01",
    "premium_gis": true,
    "features": ["branding_web"],
    "platform": {
        "iso_datetime_support": true,
        "history.max_limit": 10,
        "report.max_time_span": "P90D",
        "stats.max_allowed_trackers": 128,
        "stats.max_time_span": "P31D",
        "file_storage.hard_max_file_size": 16777216,
        "form.max_fields_count": 128,
        "form.file_field.max_file_size": 16777216,
        "form.file_field.max_files_per_field": 6,
        "form.file_field.max_count": 16
    }
}
```

* `id` - int. Dealer's ID.
* `ui_domain` - string. Dealer's UI domain.
* `company_url` - string. Dealer's promo site URL.
* `settings` - object. Custom settings.
    * `domain` - string. The same as dealer.ui_domain.
    * `service_title` - string. Title of the service.
    * `locale` - [enum](../../getting-started/introduction.md#data-types). Default locale of the dealer.
    * `demo_login` - string. Dealer's login for demo user or empty string if no demo user available.
    * `demo_password` - string. Dealer's password for demo user or empty string if no demo user available.
    * `maps` - string array. List of available maps, 
    e.g. `["roadmap", "cdcom", "osm", "wikimapia", "yandexpublic", "hybrid", "satellite"]`.
    * `default_map` - object. Default map settings.
    * `type` - [enum](../../getting-started/introduction.md#data-types). Default map type.
    * `location` - object. Default map center location.
    * `lat` - float. Latitude.
    * `long` - float. Longitude.
    * `zoom` - int. Default map zoom level.
    * `currency` - [enum](../../getting-started/introduction.md#data-types). Dealer's currency ISO 4217 code.
    * `payment_link` - string. PaaS-dependent link that can be used to refill user's account. Can be null or empty.
    * `promo_url` - string. Customizable "About company" url.
    * `google_client_id` - string. Client ID which must be used to work with Google API or null.
    * `favicon` - string. Path or URL to dealer's interface favicon.
    * `logo` - string. Path or URL to dealer's logotype.
    * `app_logo` - string. Nullable, path or URL to dealer's mobile app logotype.
    * `login_wallpaper` - string. Path or URL to dealer's interface login wallpaper.
    * `desktop_wallpaper` - string. Path to dealer's interface wallpaper or null.
    * `monitoring_logo` - string. Path to dealer's interface monitoring logo or null.
    * `login_footer` - string. Footer which will be included in login page.
    * `allow_registration` - boolean. If `true` then registration is available for dealer's users. All HTML 
    special chars escaped using HTML entities.
    * `show_mobile_apps` - boolean. If `true` then mobile applications are available for dealer's users.
    * `show_call_notifications` - boolean. If `true` then call notifications are available for dealer's users.
    * `geocoder` - [enum](../../getting-started/introduction.md#data-types). Default geocoder.
    * `route_provider` - [enum](../../getting-started/introduction.md#data-types). Default router.
    * `measurement_system` - [enum](../../getting-started/introduction.md#data-types). Measurement system.
    * `display_model_features_link` - boolean. When `true` show in model info link to squaregps.com (UI option).
    * `color_theme` - [enum](../../getting-started/introduction.md#data-types). Color theme code or empty string (for default theme).
    * `app_color_theme` - [enum](../../getting-started/introduction.md#data-types). Mobile app color theme code or empty string (for default theme).
    * `privacy_policy_link` - string. Nullable, privacy policy link (it may be empty).
    * `tos` - string. Nullable, terms of service text (it may be empty).
    * `tracker_model_filter` - object. A filter which describes tracker models available for registration.
    * `exclusion` - boolean. If `true` models in the `values` will be excluded.
    * `values` - string array. If it is empty - all models available.
    * `internal` - object with additional options.
    * `light_registration` - boolean. If `true` use "very simple" registration with demo tracker.
    * `demo_tracker_source_id` - int. An ID of tracker created on `light_registration`.
    * `demo_tracker_label` - string. Label of tracker created on `light_registration`.
    * `no_register_commands` - boolean. If `true` then do not send commands to devices on activation.
* `demo_ends` - string. A date when demo for this dealer ends. Is null when dealer is not on Trial tariff.
* `premium_gis` - boolean. If `true` dealer has Premium GIS package.
* `features` - string array. Set of the allowed features for a dealer (all list see below in "Dealer features").
* `platform` - key-value object. Global platform settings.
    * `iso_datetime_support` - boolean, if `true` platform supports ISO 8601 [date/time format](../../getting-started/introduction.md#datetime-formats). 
    * `history.max_limit` - int, max limit for [history](history/index.md) list actions.
    * `report.max_time_span` - ISO 8601 duration, max timespan for [reports generation](report/report_tracker.md#generate).
    * `stats.max_allowed_trackers` - int, max allowed trackers for [stats actions](../tracking/tracker/stats/stats_mileage.md).
    * `stats.max_time_span` - ISO 8601 duration,max timespan for [stats actions](../tracking/tracker/stats/stats_mileage.md).
    * `file_storage.hard_max_file_size` - long, hard max file size in bytes for uploading files to the file storage.
    * `form.max_fields_count` - integer, max fields per form.
    * `form.file_field.max_file_size` - long, max file size in bytes for the form file.
    * `form.file_field.max_files_per_field` - integer, max files per form field.
    * `form.file_field.max_count` - integer, max file fields per form.
  
#### Dealer features

| name            | description                                                                       |
|:----------------|:----------------------------------------------------------------------------------|
| branding_web    | Allow to use custom logos, color theme, domain and favicon in UI for web version. |
| branding_mobile | Allow to use custom icon, logo, color theme in the mobile applications.           |
| subpaas         | Allow to use Sub-Dealers (can be used only together with `navixy_label`).         |
| navixy_label    | Show "Powered by Navixy" in UI (required for subpaas feature).                    |

#### Errors

* 12 – Dealer not found (if corresponding dealer not found in the database).
* 201 – Not found in the database (if there is no Ui settings data for corresponding dealer).
