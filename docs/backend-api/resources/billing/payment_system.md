---
title: Payment system
description: Payment system
---

# Payment system

API path: `/payment_system`.

### list
Return list of payment systems available for user.

**required subuser rights:** payment_create

#### response
```javascript
{
    "success": true,
    "list": [<payment_system_settings>, ...]
}
```

where **payment_system_settings** is:
```javascript
{
    "type": "rbkmoney", // payment system type
    "url": "https:_rbkmoney.com/acceptpurchase.aspx", // URL to send payment info,
    "account": <string>, // (optional) dealer account in payment system (eshopId for RBK)
    "currency": "EUR", // 3-letter ISO 4217 currency code
    "payment_code": "Navixy Demo", // (optional) code for payments
    "subscription_code": "4671292", // (string) subscription code. same as "payment_code" for 2Checkout (formerly Avangate) but for subscriptions
    "methods": [<string>, ...] // (optional) list of available payment methods (may be empty)
    // for type == "ios_inapp" only:
    "prices": {
        "Loccate_default_pay_1": 0.99,
        "Loccate_default_pay_5": 4.99,
        "Loccate_default_pay_10": 9.99,
        "Loccate_default_pay_20": 19.99
    }
}
```

#### errors
* 201 – Not found in database.

### estimate/get
Returns the estimate of the monthly payment amount

**required subuser rights:** payment_create

#### response
```javascript
{
    "success": true,
    "value": 400.0 // payment amount, rounded up to hundreds for rubles or to tens for other currencies
}
```

### mobile/pay
Create bill using 'mobile' payment system (AKA Qiwi Bank)

**required subuser rights:** payment_create

#### parameters
name | description | type
--- | --- | ---
phone | 10-digit phone number without country code (e.g. 6156680000) | String
sum | amount of money to pay, e.g. 100.50 . minimum is 1.00, maximum is 99999.00 | double

#### response
```javascript
{
    "success": true
}
```

#### errors
* 13 – Operation not permitted. (if this payment system is not enabled for user's PaaS platform)
* 201 – Not found in database. (if payment system was not configured properly)
* 215 – External service error (if QIWI payment gateway returned an error)
