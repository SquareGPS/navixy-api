---
title: /service
description: /service
---

## read

Get current monitoring service settings.

#### required permissions:

*   **service_settings**: "read"

#### response

```js
{
  "success": true,
  "value": {
    "service_title": "monitoring service", // service name
    "locale": "en_US",        // locale
    "demo_login": "demo",     // if not empty, demo button will use this login to authorize
    "demo_password": "demo",  // if not empty, demo button will use this password to authorize
    "maps": ["osm", "wikimapia", "yandexpublic", "osmmapnik"], // list of strings. 
                              // maps available in monitoring system. 
                              // when domain is platform owner's sub-domain then only free maps are available
    "default_map": { //default map settings
      "type": "osm", // default map code
      "location": {"lat": 33.0, "lng": 22.0}, // default location to show on the map (location object)
      "zoom": 2      // int. default zoom level to use
    },
    "currency": "EUR",                  // code of the currency which can be shown in UI
    "payment_link": "http://payme.ru",  // link to dealer's payment system. can be null or empty.
    "promo_url": "http://monitoring.com/about", // customizable "About company" url. can be null or empty
    "google_client_id": "io54p54ijy54", // google maps client ID (not supported by interface yet).
    "domain": "track.agent.com",        // domain which will be used for monitoring system
    "favicon": "paas/5001/custom.ico",  //nullable, path or url to dealer's interface favicon, 
                                        // e.g. "http://test.com/favicon.ico"
    "app_logo": "paas/5001/app_logo.png",       //nullable, path or url to dealer's mobile app logotype, 
    "logo": "paas/5001/logo.png",       /nullable,/ path or url to dealer's logotype, 
                                        // e.g. "http://test.com/logo.png"
    "document_logo": "paas/5001/document_logo.png",       //nullable, path or url to dealer's logotype for documents, 
    "login_wallpaper": "paas/5001/login.png", //nullable, path or url to dealer's interface login wallpaper, 
                                        // e.g. "http://test.com/test.jpg"
    "desktop_wallpaper": "http://test.com/test.jpg", //nullable, path to dealer's interface wallpaper.
    "login_footer": "All rights reserved.", // footer which will be included in login page. can be null.
    "allow_registration": true,
    "show_mobile_apps": true,           // if true then dealer's users can use mobile applications
    "default_user_settings": {
      "geocoder": "google",             // default geocoder
      "route_provider": "progorod",     // default router
      "measurement_system": "metric",   // measurement system
      "translit": false
    },
    "display_model_features_link": false, // when true show in model info link to squaregps.com (UI option)
    "limited_domain": false,            // if true, paas domain has limitations
    "allowed_maps": [${string}, ...],   // list of maps available for selection in "maps" list
    "color_theme": "aqua",              // (string. 128 chars max) color theme code or empty string (for default theme)
    "app_color_theme": "blue_1",         // (string. 128 chars max) mobile app color theme code or empty string (for default theme)
    "privacy_policy_link": "http://privacy-policy-url",
    "tos": "Terms Of Service text",
    "no_register_commands": false // if true then do not send commands to devices on activation
  }
}
```

where **location** described in [data types description section](../../../../backend-api/getting-started.md#data-types).

## update

Update monitoring service settings for the current dealer. Note: wallpapers, logos and favicons cannot be edited here. 

#### required permissions:

*   **service_settings**: "update"

#### parameters

All fields from the [/dealer/service/settings/read](#read) response.

#### response

```json
{ "success": true }
```

#### errors

*   247 - Entity already exists(409) - when **domain** already used by other dealer
