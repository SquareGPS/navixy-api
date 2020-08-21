---
title: /tariff
description: /tariff
---

# tariff data structure:

    {
        "id": ${int},                      // tariff id
        "name": ${string},                 // tariff name
        "group_id": ${int},                // tariff group number
        "active": ${boolean},              // true if user is allowed to change current tariff to this one
        "type": ${string},                 // type of tariff "monthly" or "activeday" (for "tracker" device_type only)
        "price": ${double},                // tariff subscription price (usually per month)
        "early_change_price": 23.0, // (double) price of change tariff from current to other 
                // with the last change in less than 30 days (**tariff.freeze.period** config option).
                // When not passed or "null" user cannot change tariff frequently.
        "device_limit": ${int},            // maximum limit of devices per user. not used for cameras and sockets
        "has_reports": ${boolean},
        "store_period": ${string},         // data storage period, e.g. "2h" (2 hours), "3d" (3 days), "5m" (5 months), "1y" (one year)
        "device_type": ${string},          // Device type. Can be "tracker", "camera" or "socket"
        "proportional_charge": ${boolean}, // true if monthly fee will be smaller
                // when device was blocked during month (for "monthly" tariffs only)
        "service_prices": ${prices}        // prices JSON object (see below)
    }
    

#### service_prices data structure:

    {
        "incoming_sms": ${double}, // incoming sms price
        "outgoing_sms": ${double}, // outgoing sms price
        "service_sms": ${double},  // service sms price
        "phone_call": ${double},   // phone voice notification sms price
        "traffic": ${double}       // traffic price per megabyte
    }
    
## create

#### create(tariff)

Creates new tariff.

#### parameters

*   **tariff** – (see above) without **id**.

#### required permissions:

*   **tariffs**: "create"

#### response

    {
        "success": true,
        "id" : <int> // id of the created tariff
    }


#### errors

*   201 – Not found in database (if specified tariff does not exist or belongs to different dealer)
*   214 – Requested operation or parameters are not supported by the device (when **device_type** does not support specified tariff **type**)
*   244 – Duplicate entity label (if there’s another dealer’s tariff with the same “name”)

## defaults/

#### **defaults** JSON object data structure:

    {
        "tariff_id": 1234,           // id of the default tariff for this device type
        "activation_bonus": 0,       // int. activation bonus (amout of money added to bonus balance upon device registration)
        "free_days": 14,             // amount of free (without tariff fee) days after device registration
        "free_days_device_limit": 3  // maximum number of activated user's devices with free period (null means no limit)
    }

### read

Returns current tariff defaults for trackers and cameras.

#### required permissions:

* `tariffs: "read"`

#### response

    {
        "success": true,
        "tracker": ${defaults},
        "camera": ${defaults}
    }

### update

`update(tracker,camera)`


Updates current tariff defaults for trackers and cameras. tracker, camera are objects.

#### required permissions:

*   `tariffs: "update"`

#### response

    { "success": true }


#### errors

*   239 – New tariff doesn’t exist (if tariff with such id does not exist).
*   237 – Invalid tariff (if new tariff has incompatible device type).

## list

Returns list of all tariffs belonging to dealer.

If "filter" is used, entities will be returned only if filter string is contained within one of the following fields:
id, name, price, device_type

#### required permissions:

*   `tariffs: "read"`

#### parameters

*   **device_type** – (optional). Filter by device type. One of “tracker”, “camera” or “socket”;
*   **filter** – **string** (optional). Text filter string.
*   **order_by** – **string** (optional). Specify list ordering.
    One of: **id**, **name**, **device_type**, **group_id**, **price**
*   **ascending** – **boolean** (default: **true**). If true, ordering will be ascending, descending otherwise.
*   **offset** – **int** (optional. default: **0**). Starting offset, used for pagination.
*   **limit** – **int** (optional). Max number of records to return, used for pagination.

#### response

    {
        "success": true,
        "list" : [ ${tariff}, ... ],
        "wholesale_service_prices" : ${prices}, //a wholesale prices for all services (what dealer will pay per sms, per call, per mb, etc.)
        "count" : 42 //total number of records (ignoring offset and limit)
    }


See **tariff** object structure [here](#tariff-data-structure).

## read

Returns tariff with the specified id.

#### required permissions:

*   `tariffs: "read"`

#### parameters

*   **tariff_id**

#### response

    {
        "success": true,
        "value": ${tariff}
    }


See **tariff** object structure [here](#tariff-data-structure).

#### errors

*   201 – Not found in database (if specified tariff does not exist or belongs to different dealer)

## update

update(tariff)

Updates existing tariff. See above. Warning: “device_type” field is ignored, it can only be specified during tariff creation.

**required permissions:**

*   `tariffs: "update"`

#### response

    { "success": true }


#### errors

*   201 – Not found in database (if specified tariff does not exist or belongs to different dealer)
*   214 – Requested operation or parameters are not supported by the device (when **device_type** does not support specified tariff **type**)
*   244 – Duplicate entity label (if there’s another dealer’s tariff with the same “name”)