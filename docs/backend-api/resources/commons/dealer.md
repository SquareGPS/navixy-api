---
title: Dealer
description: Dealer
---

# Dealer

API path: `/dealer`.

## get_ui_config()

Gets dealer info and dealer-specific UI settings by domain.

It doesn't need authentication and available in **UNAUTHORIZED** access level.

#### structure:

    {{ extra.api_example_url }}/dealer/get_ui_config?domain=your_domain

#### parameters

| name | description | type| format|
| :------: | :------: | :-----:| :------:|
| domain | dealer’s monitoring interface domain, e.g. “navixy.com“ | string | panel.navixy.com |

#### example

    {{ extra.api_example_url }}/dealer/get_ui_config?domain=panel.navixy.com

#### response

```js
{
    "success": true,
    "dealer": {
        "id": 5001,                     // int. dealer id
        "ui_domain": "demo.navixy.com", // Dealer's UI domain
        "company_url": "navixy.com"     // Dealer's promo site URL
                                        // e.g. "http://www.navixy.com" or "demo.navixy.com"
    },
    "settings": {         //may be null if dealer has not set any custom settings
        "domain" : "demo.navixy.com",   // same as dealer.ui_domain
        "service_title": "Navixy Demo", // Title of the service
        "locale": "at_AT",              // default locale of the dealer
        "demo_login": "demo",           // dealer's login for demo user 
                                        // (or empty string if no demo user available)
        "demo_password": "demo",        // dealer's password for demo user 
                                        // (or empty string if no demo user available)
        "maps": ["roadmap", "osm"],     // list of available  maps, 
                // e.g. ["roadmap", "cdcom", "osm", "wikimapia", "yandexpublic", "hybrid", "satellite"]
        "default_map": {  //default map settings
            "type": "roadmap",          // default map type
            "location": { //default map center location
                "lat": 57.0,            // latitude
                "lng": 61.0             // longitude
            },
            "zoom": 10                  // default map zoom level
        },
        "currency": "EUR",              // dealer's currency ISO 4217 code
        "payment_link": "http://site.de/pay.php", // PaaS-dependent link that can be used 
                                       // to refill user's account. Can be null or empty. 
        "promo_url": "http://site.de/about/",            // customizable "About company" url
        "google_client_id": "clientID", // client id which which must be used to work with google API or null
        "favicon": "paas/5001/custom.ico", // path or url to dealer's interface favicon
        "logo": "paas/5001/logo.png",   // path or url to dealer's logotype
        "app_logo": "paas/5001/app_logo.png",       //nullable, path or url to dealer's mobile app logotype, 
        "login_wallpaper": "paas/5001/login.png", // path or url to dealer's interface login wallpaper
        "desktop_wallpaper": "http://test.com/test.jpg", // path to dealer's interface wallpaper or null
        "monitoring_logo": "http://test.com/test.jpg", // path to dealer's interface monitoring logo or null
        "login_footer": "All rights reserved.", // footer which will be included in login page. 
        "allow_registration": true,     // if true then registration is available for dealer's users 
                                        // all html special chars escaped using HTML entities.
        "show_mobile_apps" : true,      // if true then mobile applications are available for dealer's users 
        "show_call_notifications" : true,      // if true then call notifications are available for dealer's users 
        "default_user_settings": {
            "geocoder": "google",            // default geocoder
            "route_provider": "progorod",    // default router
            "measurement_system": "metric",  // measurement system
            "translit": false
        },
        "display_model_features_link" : true, // when true show in model info link to squaregps.com (UI option)
        "color_theme": "aqua",          // (string) color theme code or empty string (for default theme)
        "app_color_theme": "blue_1",    // (string. 128 chars max) mobile app color theme code or empty string (for default theme)
        "privacy_policy_link": "http://privacy-policy-url",
        "tos": "Terms Of Service text",
        "enable_trackers": true,        // if true, GPS monitoring interface is available for dealer's users
        "enable_cameras": false,        // if true, camera monitoring interface is available for dealer's users
        "tracker_model_filter": {       // a filter which describes tracker models available for registration
            "exclusion": true,          // in this example all models available
            "values": []
        },
        "internal": {  // additional options
            "light_registration": true,           // use "very simple" registration with demo tracker
            "demo_tracker_source_id": 14,         // id of tracker created on 'light_registration'
            "demo_tracker_label": "Demo tracker", // label of of tracker created on 'light_registration'
            ...
        },
        "no_register_commands": false // if true then do not send commands to devices on activation
    },
    "demo_ends": "2014-01-01",          // a date when demo for this PaaS ends. 
                                        // Is null when PaaS is not on demo tariff
    "premium_gis": true,                // true, if dealer has Premium GIS package
    "features": ["branding_web"]        // set of the allowed features for dealer (all list see below in "Dealer features")
}
```

#### Dealer features

| name | description |
| :------ | :------ |
| branding_web | allow to use custom logos, color theme, domain and favicon in UI for web version |
| branding_mobile | allow to use custom icon, logo, color theme in the mobile applications |
| subpaas | allow to use Sub-Dealers (can be used only together with navixy_label) |
| navixy_label | show "Powered by Navixy" in UI (required for subpaas feature) |

#### errors

*   12 – Dealer not found (if corresponding PaaS was not found in database)
*   201 – Not found in database (if there is no Ui settings data for corresponding PaaS)