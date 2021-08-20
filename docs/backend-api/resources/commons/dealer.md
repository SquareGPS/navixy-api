---
title: Dealer
description: Contains API call to get dealer info and dealer-specific UI settings.
---

# Dealer

Contains API call to get dealer info and dealer-specific UI settings.

<hr>

## API actions

API path: `/dealer`.

### get_ui_config

Gets dealer info and dealer-specific UI settings by a domain.

It doesn't need authentication and available in **UNAUTHORIZED** access level.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| domain | Dealer's monitoring interface domain, e.g. "panel.navixy.com". | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/dealer/get_ui_config' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "domain": "panel.navixy.com"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/dealer/get_ui_config?hash=&domain=
    ```

#### response

```json
{
  "success": true,
  "dealer": {
    "id": 20410,
    "ui_domain": "20410.navixy.ru",
    "company_url": ""
  },
  "settings": {
    "domain": "20410.navixy.ru",
    "service_title": "Astarsys",
    "locale": "en_US",
    "demo_login": "",
    "demo_password": "",
    "maps": [
      "roadmap",
      "satellite",
      "hybrid",
      "yandexpublic",
      "osm",
      "osmmapnik",
      "wikimapia"
    ],
    "default_map": {
      "type": "roadmap",
      "location": {
        "lat": 57.0,
        "lng": 61.0
      },
      "zoom": 10
    },
    "currency": "USD",
    "payment_link": "",
    "promo_url": "",
    "google_client_id": "ID",
    "favicon": null,
    "logo": null,
    "app_logo": null,
    "login_wallpaper": null,
    "desktop_wallpaper": null,
    "monitoring_logo": null,
    "monitoring_logo_clickable": true,
    "login_footer": "",
    "allow_registration": true,
    "show_mobile_apps": false,
    "show_call_notifications": false,
    "display_model_features_link": false,
    "color_theme": "metromorph",
    "app_color_theme": "blue_2",
    "has_https": false,
    "privacy_policy_link": "",
    "tos": "",
    "no_register_commands": false,
    "geocoders": [],
    "route_providers": [],
    "lbs_providers": [],
    "matrix_providers": [],
    "tracker_model_filter": {
      "exclusion": true,
      "values": []
    },
    "gis_package": "premium",
    "credentials": {
      "google": {
        "maps_js_api_key": "Key"
      }
    }
  },
  "demo_ends": null,
  "premium_gis": true,
  "allow_branding": true,
  "features": [
    "branding_web",
    "branding_mobile",
    "navixy_label",
    "tracking",
    "reports",
    "fleet",
    "field_service",
    "premium_gis"
  ],
  "platform": {
    "iso_datetime_support": true,
    "history.max_limit": 1000,
    "report.max_time_span": "P120D",
    "stats.max_allowed_trackers": 128,
    "stats.max_time_span": "P31D",
    "file_storage.hard_max_file_size": 16777216,
    "form.file_field.max_file_size": 16777216,
    "form.file_field.max_files_per_field": 6,
    "form.file_field.max_count": 16
  }
}
```

* `id` - int. Dealer's ID.
* `ui_domain` - string. Dealer's UI domain.
* `company_url` - string. Dealer's promo site URL.
* `settings` - object. Custom settings. May be null if dealer has not set any custom settings.
    * `domain` - string. The same as dealer.ui_domain.
    * `service_title` - string. Title of the service.
    * `locale` - [enum](../../getting-started.md#data-types). Default locale of the dealer.
    * `demo_login` - string. Dealer's login for demo user or empty string if no demo user available.
    * `demo_password` - string. Dealer's password for demo user or empty string if no demo user available.
    * `maps` - string array. List of available maps, 
    e.g. `["roadmap", "cdcom", "osm", "wikimapia", "yandexpublic", "hybrid", "satellite"]`.
    * `default_map` - object. Default map settings.
    * `type` - [enum](../../getting-started.md#data-types). Default map type.
    * `location` - object. Default map center location.
    * `lat` - float. Latitude.
    * `long` - float. Longitude.
    * `zoom` - int. Default map zoom level.
    * `currency` - [enum](../../getting-started.md#data-types). Dealer's currency ISO 4217 code.
    * `payment_link` - string. PaaS-dependent link that can be used to refill user's account. Can be null or empty.
    * `promo_url` - string. Customizable "About company" url.
    * `google_client_id` - string. Client id which must be used to work with google API or null.
    * `favicon` - string. Path or url to dealer's interface favicon.
    * `logo` - string. Path or url to dealer's logotype.
    * `app_logo` - string. Nullable, path or url to dealer's mobile app logotype.
    * `login_wallpaper` - string. Path or url to dealer's interface login wallpaper.
    * `desktop_wallpaper` - string. Path to dealer's interface wallpaper or null.
    * `monitoring_logo` - string. Path to dealer's interface monitoring logo or null.
    * `monitoring_logo_clickable` - boolean. `true` if click on the logo will open the company website. 
    * `login_footer` - string. Footer which will be included in login page.
    * `allow_registration` - boolean. If `true` then registration is available for dealer's users. All HTML 
    special chars escaped using HTML entities.
    * `show_mobile_apps` - boolean. If `true` then mobile applications are available for dealer's users.
    * `show_call_notifications` - boolean. If `true` then call notifications are available for dealer's users.
    * `geocoders` - [enum](../../getting-started.md#data-types). A list of allowed geocoders.
    * `route_providers` - [enum](../../getting-started.md#data-types). A list of allowed route providers.
    * `route_providers` - [enum](../../getting-started.md#data-types). A list of allowed route providers.
    * `display_model_features_link` - boolean. When `true` show in model info link to squaregps.com (UI option).
    * `color_theme` - [enum](../../getting-started.md#data-types). Color theme code or empty string (for default theme).
    * `app_color_theme` - [enum](../../getting-started.md#data-types). Mobile app color theme code or empty string (for default theme).
    * `has_https` - boolean. If `true` the domain has SSL certificate.
    * `privacy_policy_link` - string. A link to a privacy policy document.
    * `tos` - string. Terms of service text.
    * `tracker_model_filter` - object. A filter which describes tracker models available for registration.
    * `exclusion` - boolean. If `true` models in the `values` will be excluded.
    * `values` - string array. If it is empty - all models available.
    * `internal` - object with additional options.
    * `light_registration` - boolean. If `true` use "very simple" registration with demo tracker.
    * `demo_tracker_source_id` - int. An id of tracker created on `light_registration`.
    * `demo_tracker_label` - string. Label of tracker created on `light_registration`.
    * `no_register_commands` - boolean. If `true` then do not send commands to devices on activation.
* `demo_ends` - string. A date when demo for this dealer ends. Is null when dealer is not on Trial tariff.
* `premium_gis` - boolean. If `true` dealer has Premium GIS package.
* `features` - string array. Set of the allowed features for a dealer (all list see below in "Dealer features").
* `platform` - key-value object. Global platform settings.
    * `iso_datetime_support` - boolean, if `true` platform supports ISO 8601 [date/time format](../../getting-started.md#datetime-formats). 
    * `history.max_limit` - int, max limit for [history](history/index.md) list actions.
    * `report.max_time_span` - ISO8601 period, max timespan for [reports generation](report/report_tracker.md#generate).
    * `stats.max_allowed_trackers` - int, max allowed trackers for [stats actions](../tracking/tracker/stats/stats_mileage.md).
    * `stats.max_time_span` - ISO8601 period,max timespan for [stats actions](../tracking/tracker/stats/stats_mileage.md).
    * `file_storage.hard_max_file_size` - long, hard max file size in bytes for uploading files to the file storage.
    * `form.file_field.max_file_size` - long, max file size in bytes for the form file.
    * `form.file_field.max_files_per_field` - integer, max files per form field.
    * `form.file_field.max_count` - integer, max file fields per form.
  
#### Dealer features

| name | description |
| :------ | :------ |
| branding_web | Allow to use custom logos, color theme, domain and favicon in UI for web version. |
| branding_mobile | Allow to use custom icon, logo, color theme in the mobile applications. |
| subpaas | Allow to use Sub-Dealers (can be used only together with `navixy_label`). |
| navixy_label | Show "Powered by Navixy" in UI (required for subpaas feature). |
| tracking | Main tracking feature in the UI. |
| reports | Allows to use reports. |
| fleet | Allows to use fleet management. |
| field_service | Allows to use field service and tasks. |
| premium_gis | Appears if dealer uses the Premium GIS tariff. | 

#### errors

* 12 – Dealer not found - if corresponding dealer not found in the database.
* 201 – Not found in the database - if there is no Ui settings data for corresponding dealer.
