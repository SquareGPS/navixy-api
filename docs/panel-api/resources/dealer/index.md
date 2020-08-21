---
title: Dealer actions
description: Dealer actions
---

## get_info

#### required permissions:

*   **base**: "get\_dealer\_info"

#### response

    {
        "success": true,
        "id": 9000,                   // dealer id
        "seller_id": 3
        "parent_dealer_id": 5001,     // id of parent dealer
        "contract_type": "PAAS",      // contract type: PARTNER, AGENT or PAAS 
        "tariff_id": 5,               // PaaS tariff id
        "tariff": {                   // PaaS tariff info
            "id": 5,
            "name": "PaaS Tariff",
            "type": "monthly",
            "currency": "RUB",
            "license_price": null,    // null or double
            "min_license_pay": null,  // null or double
            "vat": false,
            "trial": false,
            "premium_gis": true,
            "service_prices": {
                "incoming_sms": 2.0,
                "outgoing_sms": 0.95,
                "service_sms": 0.95,
                "phone_call": 15,
                "traffic": 1.5            
            },
            "store_period": "P3Y"     // max user data store period
        },
        "demo_tariff": false,         // true for "TRIAL" PaaS tariffs
        "tracker_tariff_end_date": "2015-12-31",
        "store_period": "P6M",        // max user data store period
        "demo_ends": null,            // TRIAL period end date or null
        "title": "Navixy Demo",   
        "block_status": "NOT_BLOCKED" // (string) Panel and PaaS users block status. 
                                      // One of: "NOT_BLOCKED", "INITAL_BLOCK", "BLOCK_LOGIN" or "CLIENTS_BLOCKED"
        "legal_name": ${string},
        "active_amount": 99,          // amount of all active trackers (with Sub-PaaSes)
        "active_amount_own": 80,      // amount of active trackers (without Sub-PaaSes)
        "active_amount_subpaas": 19,  // amount of the Sub-PaaSes active trackers
        "active_limit": 100,          // active trackers limit
        "locale": "en_US",            // dealer's default locale
        "domain" : "demo.navixy.com", // dealer's domain
        "favicon": "paas/5001/custom.ico", // path or URL to dealer's interface favicon or null
        "logo": "paas/5001/logo.png", // path or URL to dealer's logotype or null
        "enable_trackers": true,
        "enable_cameras": false,
        "paas_activation_date": "2015-03-01", // date of activation pay
        "license_balance": 0.0,
        "seller_currency": "USD",
        "features": ["branding_web"]  // set of the allowed features for dealer
    }
    
where **features** is a set of allowed [Dealer features](../../../backend-api/resources/commons/dealer.md#dealer-features).

#### errors

*   201 - Not found in database