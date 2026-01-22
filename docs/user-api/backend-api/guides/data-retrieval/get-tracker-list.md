# Getting List of GPS Trackers

This guide describes how to obtain a list of GPS devices linked to a user account via the Navixy API. Accessing this information is fundamental for efficiently managing and monitoring multiple devices in the Navixy system.

## Prerequisites

Before you begin, make sure you have an active Navixy account and a valid [API key for authentication](../../../authentication.md#id-2.-api-keys-recommended-authentication). This key is required to access the API and perform authorized requests within the system.

## Make the API request

To retrieve the list of trackers, send a POST request to the [`/tracker/list`](../../resources/tracking/tracker/#list) endpoint. The following sections provide detailed information and examples to guide you through this process.

### API endpoint

`https://api.{region}.navixy.com/v2/tracker/list`

### API request to retrieve all trackers in account

**cURL**

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.navixy.com/v2/tracker/list' \
	-H 'Content-Type: application/json' \
	-d '{"hash": "your_api_key_hash"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
```http
https://api.navixy.com/v2/tracker/list?hash=your_api_key_hash
```
{% endtab %}
{% endtabs %}

**Response**

If the request is successful, the response will return a list of trackers linked to your account.

```json
{
  "list": [
    {
      "id": 10191086,
      "label": "Chevrolet Equinox",
      "group_id": 0,
      "source": {
        "status_listing_id": null,
        "id": 10118726,
        "creation_date": "2023-03-08",
        "blocked": false,
        "device_id": "359632100002001",
        "tariff_id": 5856,
        "model": "telfmm00a",
        "tariff_end_date": "2025-12-01",
        "phone": "359632100002001"
      },
      "tag_bindings": [],
      "clone": false
    },
    {
      "id": 10191087,
      "label": "Peterbilt 579",
      "group_id": 0,
      "source": {
        "status_listing_id": null,
        "id": 10118727,
        "creation_date": "2023-03-08",
        "blocked": false,
        "device_id": "359632100002002",
        "tariff_id": 5856,
        "model": "ruptela_pro5",
        "tariff_end_date": "2025-12-01",
        "phone": "359632100002002"
      },
      "tag_bindings": [],
      "clone": false
    },
    {
      "id": 10191088,
      "label": "X-GPS",
      "group_id": 0,
      "source": {
        "status_listing_id": null,
        "id": 10118728,
        "creation_date": "2023-03-08",
        "blocked": false,
        "device_id": "156616052918",
        "tariff_id": 5856,
        "model": "iosnavixytracker_xgps",
        "tariff_end_date": "2025-12-01",
        "phone": null
      },
      "tag_bindings": [],
      "clone": false
    },
    {
      "id": 10191089,
      "label": "Ford Fiesta",
      "group_id": 0,
      "source": {
        "status_listing_id": null,
        "id": 10118821,
        "creation_date": "2023-03-08",
        "blocked": false,
        "device_id": "359632100002003",
        "tariff_id": 5856,
        "model": "eelink_got8",
        "tariff_end_date": "2025-12-01",
        "phone": "3463463456456456"
      },
      "tag_bindings": [],
      "clone": false
    }
  ],
  "success": true
}
```

* `id` (integer): The unique identifier of each tracker object within the list. This identifier, known as the `tracker_id` or `object_id`, uniquely distinguishes the tracker on the platform and is used in all subsequent API calls related to trackers.
* `label` (string): The name of the tracker object.
* `group_id` (integer): Indicates the group to which the tracker belongs.
* `source` (object): Provides information about the data source for the tracker object, associating the platform tracker with a specific physical device.
  * `creation_date` (string, ISO 8601 date): The date the tracker was created on the platform.
  * `blocked` (boolean): Indicates if the tracker is blocked due to user tariff restrictions.
  * `device_id` (string): The ID used to register the physical device; may be IMEI, serial number, or manually assigned ID depending on the device model.
  * `tariff_id` (integer): The tariff plan assigned to the device.
  * `model` (string): The tracker device model code, which determines available settings, rules, and sensors.
  * `tariff_end_date` (string, ISO 8601 date): The date when the next tariff charge is due.
  * `phone` (string|null): The last known phone number for the tracker, used by the platform to send SMS commands.
* `tag_bindings` (array of integers): Lists all tag IDs assigned to the tracker.
* `clone` (boolean): Indicates if the tracker is a clone (true) or original (false).

### API request to retrieve filtered list of trackers by label

If an account contains many trackers but you only need specific ones, you can use an optional filter parameter in the request to return only the matching records.

To do this, include the `labels` parameter in your request body. This parameter is an array of tracker label filters. When specified, the response will include only trackers whose labels contain any of the specified filter values. The filtering logic applies a logical OR between the items, meaning trackers matching any of the specified labels will be returned. Partial matching on tracker names is supported.

The `labels` parameter has the following constraints:

* Array size: minimum 1, maximum 1024 items
* Item length: minimum 1 character, maximum 60 characters
* No null or duplicate items are allowed

In our previous example we received 4 trackers. Let's assume we need only "Chevrolet Equinox" and "Peterbilt 579" trackers to be received within the filtered list. Then we should add parameter labels, which will contain at least part of their names.

```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/list' \
   -H 'Content-Type: application/json' \
   -d '{"hash": "your_api_key_hash", "labels": ["Chevrolet", "Peterbilt"]}'
```

**Usage notes**

* The `/tracker/list` endpoint requires a POST request with a valid API key for authentication.
* Use the `id` field returned in the response to reference trackers in subsequent API calls as `tracker_id` or `object_id`.
* The `labels` filter supports partial matching on tracker names and can be used to efficiently narrow down results when dealing with large numbers of trackers.
* Tracker objects in the response represent logical entities within the platform, each linked to a specific physical device identified by device\_id, which can be an IMEI or serial number.
