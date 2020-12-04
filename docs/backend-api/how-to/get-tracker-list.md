---
title: Get tracker list
description: Sample for get tracker list
---

# How to get tracker list

Now we [have a hash](./get-session-hash.md) — let's start with essential basics. 

Navixy has tracking device as a main unit, so most requests would require you to specify one or several tracker ids. 
You can receive a list of all trackers in user's account with [tracker/list](../resources/tracking/tracker/index.md#list) 
API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

It will return to you

```json
{
    "success": true,
    "list": [{
      "id": 123456,
      "label": "tracker label",
      "clone": false,
      "group_id": 167,
      "avatar_file_name" : "file name",
      "source": {
        "id": 234567,
        "device_id": 9999999988888,
        "model": "telfmb920",
        "blocked": false,
        "tariff_id": 345678,
        "status_listing_id": null,
        "creation_date": "2011-09-21",
        "tariff_end_date": "2016-03-24",
        "phone" : "+71234567890"
      }
      "tag_bindings": [{
      "tag_id": 456789,
      "ordinal": 4
    }]
```  
        
* `id` - int. Tracker id aka object_id.
* `label` - string. Tracker label.
* `clone` - boolean. True if this tracker is clone.
* `group_id` - int. Tracker group id, 0 when no group.
* `avatar_file_name` - string. Optional. Passed only if present.
* `source` - object.
    * `id` - int. Source id.
    * `device_id` - string. Device id aka source_imei.
    * `model` - string. Tracker model name from "models" table.
    * `blocked` - boolean. True if tracker blocked due to tariff end.
    * `tariff_id` - int. An id of tracker tariff from "main_tariffs" table.
    * `status_listing_id` - int. An id of the status listing associated with this tracker, or null.
    * `creation_date` - date/time. Date when the tracker registered.
    * `tariff_end_date` - date/time. Date of next tariff prolongation, or null.
    * `phone` - string. Phone of the device. Can be null or empty if device has no GSM module or uses bundled SIM which number hidden from the user.
* `tag_binding` - object. List of attached tags. Appears only for "tracker/list" call.
    * `tag_id` - int. An id of tag. Must be unique for a tracker.
    * `ordinal` - int. Number that can be used as ordinal or kind of tag. Must be unique for a tracker. Max value is 5.

If account has a large amount of trackers, and you only need certain ones, 
you can add an optional filter parameter to the request that will only return matching records. 

This parameter has following constraints:
*   labels array size: minimum 1, maximum 1024
*   no null items
*   no duplicate items
*   item length: minimum 1, maximum 60

To get a list of trackers with labels matching the filter use this API call:

```shell
curl -X POST '{{ extra.api_example_url }}/tracker/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "labels": ["aa", "b"]}'
```





