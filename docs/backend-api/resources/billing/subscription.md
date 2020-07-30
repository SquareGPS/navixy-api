---
title: Subscription
description: Subscription
---

# Subscription

API path: `/subscription`.

Payment subscriptions


## /subscription/avangate/

Working with [2Checkout](https://www.2checkout.com) (formerly [Avangate](http://www.avangate.com)) subscriptions (renewals).

### cancel()

Unsubscribe from auto-renewal by reference.

**required subuser rights:** payment_create

#### parameters

* **reference** - **string**. internal 2Checkout (formerly Avangate) subscription code. Get it from [list()](#list) call.

#### return
```javascript
{
    "success": true
}
```

#### errors
*   215 – External service error

### list()

List active [2Checkout](https://www.2checkout.com) [formerly Avangate](http://www.avangate.com) subscriptions (renewals).

**required subuser rights:** payment_create

#### parameters
no parameters


#### return
```javascript
{
    "success": true,
    "list": [
        {
            "reference": "5EAD4B0B2F" // pass it to /subscription/avangate/cancel()
            "code": "4679109" // 2Checkout (formerly Avangate) product code
            "quantity": 123 // count
            "expiration_date": "2016-03-10 13:32:11" // next renew date/time
        },
        ...
    ]
}
```

#### errors

 *   215 – External service error
