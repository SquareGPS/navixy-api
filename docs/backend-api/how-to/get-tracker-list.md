---
title: Get tracker list
description: Sample for get tracker list
---

# How to get tracker list

Now that we [have a hash](./get-session-hash.md) — let's start with essential basics. 

Navixy has tracking device as a main unit, so most requests would require you to specify one or several tracker ids. 
You can receive a list of all trackers in user's account with [tracker/list](../resources/tracking/tracker/tracker.md#list) API request:

    {{ extra.api_example_url }}/tracker/list?hash=your_hash

It will return to you
```json
{
    "success": true,
    "list": [ ${tracker}, ... ] // list of JSON-objects
}
```

If account has a large amount of trackers and you only need certain ones, 
you can add an optional filter parameter to the request that will only return matching records. 

This parameter has following constraints:
*   labels array size: minimum 1, maximum 1024
*   no null items
*   no duplicate items
*   item length: minimum 1, maximum 60

To get a list of trackers with labels matching the filter use this API call:

    {{ extra.api_example_url }}/tracker/list?hash=your_hash&label=[“tracker’s_name_contains”,…]

Tracker object structure is next:
```json
{
    "id": ${int},                          // tracker id aka object_id
    "label": ${string},                    // tracker label
    "clone": ${boolean},                   // true if this tracker is clone
    "group_id": ${int},                    // tracker group id, 0 if no group
    "avatar_file_name" : ${string},        // optional. passed only if present
    "source": {
        "id": ${int},                      // source id
        "device_id": ${string},            // aka source_imei
        "model": ${string},                // tracker model name from "models" table
        "blocked": ${boolean},             // true if tracker was blocked due to tariff end, etc.
        "tariff_id": ${int},               // id of tracker's tariff from "main_tariffs" table
        "status_listing_id": 102,          //id of the status listing associated with this tracker, or null
        "creation_date": "2011-09-21",
        "tariff_end_date": "2016-03-24",   // date of next tariff prolongation or null
        "phone" : ${string}                // phone of the device. can be null or empty if device has no GSM module
                                           // or uses bundled SIM which number is hidden from the user
    }
    "tag_bindings": [${tag_binding}, ...}  // list of attached tags. only for “tracker/list()“. 
}
```



