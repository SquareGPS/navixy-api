---
title: Subscription
description: API calls to interact with payment subscriptions
---

# Subscription

API calls to interact with payment subscriptions

<hr>

## API actions

API path: `/subscription`.

### /subscription/avangate/

Working with [2Checkout](https://www.2checkout.com) (formerly [Avangate](http://www.avangate.com)) subscriptions (renewals).

<hr>

### cancel

Unsubscribe from auto-renewal by reference.

**required sub-user rights:** `payment_create`.

#### parameters

| name | description | type|
| :------ | :------ | :-----|
| reference | Internal 2Checkout (formerly Avangate) subscription code. Get it from [list](#list) call. | string |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subscription/avangate/cancel' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "reference": "5EAD4B0B2F"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subscription/avangate/cancel?hash=&reference=
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 215 – External service error.

<hr>

### list

List active [2Checkout](https://www.2checkout.com) [formerly Avangate](http://www.avangate.com) subscriptions (renewals).

**required sub-user rights:** `payment_create`.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subscription/avangate/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subscription/avangate/list?hash=
    ```

#### response

```json
{
    "success": true,
    "list": [{
        "reference": "5EAD4B0B2F",
        "code": "4679109",
        "quantity": 123,
        "expiration_date": "2021-01-28 13:32:11"
    }]
}
```

* `reference` - string. Internal 2Checkout (formerly Avangate) subscription code. Pass it to /subscription/avangate/cancel.
* `code` - string. 2Checkout (formerly Avangate) product code.
* `quantity` - int. Count.
* `expiration_date` - [date/time](../../getting-started.md#data-types). Next renew date/time.

#### errors

* 215 – External service error.
