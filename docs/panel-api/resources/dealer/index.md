---
title: Dealer get info
description: API call to get information about a dealer.
---

# Dealer get info

API call to get information about a dealer.

API path: `panel/dealer/`.

### get_info

Gets information about dealer's tariff, balance, available features, etc.
 
*required permissions*: `base: "get_dealer_info"`.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/get_info' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```    

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/dealer/get_info?hash=fa7bf873fab9333144e171372a321b06
    ```

#### response

```json
{
    "success": true,
    "id": 9000,
    "seller_id": 3,
    "parent_dealer_id": 5001,
    "contract_type": "PAAS",
    "tariff_id": 5,
    "tariff": {
        "id": 5,
        "name": "PaaS Tariff",
        "type": "monthly",
        "currency": "RUB",
        "license_price": null,
        "min_license_pay": null,
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
        "store_period": "P3Y"
    },
    "demo_tariff": false,
    "tracker_tariff_end_date": "2015-12-31",
    "store_period": "P6M",
    "demo_ends": null,
    "title": "Navixy Demo",   
    "block_status": "NOT_BLOCKED",
    "legal_name": "Company",
    "active_amount": 99,
    "active_amount_own": 80,
    "active_amount_subpaas": 19,
    "active_limit": 100,
    "locale": "en_US",
    "domain" : "demo.navixy.com",
    "favicon": "paas/5001/custom.ico",
    "logo": "paas/5001/logo.png",
    "enable_trackers": true,
    "enable_cameras": false,
    "paas_activation_date": "2015-03-01",
    "license_balance": 0.0,
    "seller_currency": "USD",
    "features": [
        "branding_web",
        "branding_mobile",
        "navixy_label",
        "tracking",
        "reports",
        "fleet",
        "field_service",
        "premium_gis"
    ]
}
```

* `id` - int. Dealer id.
* `parent_dealer_id` - int. An id of parent dealer.
* `contract_type` - [enum](../../../backend-api/getting-started.md#data-types). Contract type: "PARTNER", "AGENT" or "PAAS".
* `tariff_id` - int. PaaS tariff id.
* `tariff` - PaaS tariff info.
    * `license_price` - nullable double. Price per license.
    * `min_license_pay` - nullable double. Minimum license payment.
    * `trial` - boolean. If `true` the plan is Trial.
    * `premium_gis` - boolean. If `true` premium GIS enabled for the partner.
    * `store_period` - string. Max data store period for users.
* `demo_tariff` - boolean. `true` for "TRIAL" PaaS tariffs.
* `store_period` - string. Max data store period for users on `demo_tariff`.
* `demo_ends` - string. TRIAL period end date or null.
* `block_status` - [enum](../../../backend-api/getting-started.md#data-types). Panel and PaaS users block status. One of: 
"NOT_BLOCKED", "INITIAL_BLOCK", "BLOCK_LOGIN" or "CLIENTS_BLOCKED".
* `legal_name` - string. Dealer legal name.
* `active_amount` - int. Amount of all active trackers (with Sub-PaaSes).
* `active_amount_own` - int. Amount of active trackers (without Sub-PaaSes).
* `active_amount_subpaas` - int. Amount of Sub-PaaSes' active trackers.
* `active_limit` - int. Active trackers limit.
* `locale` - [enum](../../../backend-api/getting-started.md#data-types). Dealer's default locale.
* `domain` - string. Dealer's domain.
* `favicon` - string. Path or URL to dealer's interface favicon or null.
* `logo` - string. Path or URL to dealer's logotype or null.
* `paas_activation_date` - string. Date of activation pay.
* `features` - string array. Set of the allowed [dealer features](../../../backend-api/resources/commons/dealer.md#dealer-features).

#### errors

* 201 - Not found in the database.