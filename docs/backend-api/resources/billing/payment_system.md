---
title: Payment system
description: Payment system settings object and API calls for working with payment systems and make payments.
---

# Payment system

Payment system settings object and API calls for working with payment systems and make payments.

<hr>

## Payment system settings object

```json
{
    "type": "rbkmoney",
    "url": "https:rbkmoney.com/acceptpurchase.aspx",
    "account": "John Doe",
    "currency": "EUR",
    "payment_code": "Navixy Demo",
    "subscription_code": "4671292",
    "methods": ["method1", "method2"],
    "prices": {
        "Loccate_default_pay_1": 0.99,
        "Loccate_default_pay_5": 4.99,
        "Loccate_default_pay_10": 9.99,
        "Loccate_default_pay_20": 19.99
    }
}
```

* `type` - string. Payment system type.
* `url` - string. URL to send payment info.
* `account` - optional string. Dealer account in payment system (eshopId for RBK).
* `currency` - string. 3-letter ISO 4217 currency code.
* `payment_code` - optional string. Code for payments.
* `subscription_code` - string. Subscription code. The same as "payment_code" for 2Checkout (formerly Avangate) but for subscriptions.
* `methods` - optional string array. List of available payment methods (it may be empty).
* `prices` - optional object with prices. For type == `ios_inapp` only.

<hr>

## API actions

API path: `/payment_system`.

### list

Returns list of payment systems available for specified user.

**required sub-user rights:** `payment_create`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/payment_system/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/payment_system/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "list": [{
         "type": "rbkmoney",
         "url": "https:rbkmoney.com/acceptpurchase.aspx",
         "account": "John Doe",
         "currency": "EUR",
         "payment_code": "Navixy Demo",
         "subscription_code": "4671292",
         "methods": ["method1", "method2"]
    }]
}
```

* `list` - array of objects. List of [payment system objects](#payment-system-settings-object).

#### errors

* 201 – Not found in the database.

<hr>

### estimate/get

Returns the estimate of the monthly payment amount

**required sub-user rights**: `payment_create`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/payment_system/estimate/get' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/payment_system/estimate/get?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "value": 400.0
}
```

* `value` - float. Payment amount, rounded up to hundreds for rubles or to tens for other currencies.

<hr>

### mobile/pay

Create a bill using 'mobile' payment system (AKA Qiwi Bank).

**required sub-user rights:** `payment_create`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| phone | 10-digit phone number without "+" sign and country code. | string |
| sum | amount of money to pay, e.g. 100.50 . minimum is 1.00, maximum is 99999.00. | double |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/payment_system/mobile/pay' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "phone": "6156680000", "sum": 1000.00}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 13 – Operation not permitted - if this payment system not enabled for user's PaaS platform.
* 201 – Not found in the database - if payment system not configured properly.
* 215 – External service error - if QIWI payment gateway returned an error.
