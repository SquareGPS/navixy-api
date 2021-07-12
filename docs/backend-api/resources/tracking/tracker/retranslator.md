---
title: Retranslator
description: Contains tracker retranslator binding object and API calls to bind/unbind it to tracker or get already binded one.
---
# Retranslator

Contains tracker retranslator binding object and API calls to bind/unbind it to tracker or get already binded one.

<hr>

## Tracker retranslator binding object

```json
{
    "retranslator_id": 4548,
    "fake_device_id": "AI568T"
}
```

* `retranslator_id` - int. An id of the [retranslator](../../../tracking/retranslator/).
* `fake_device_id` - string. Optional. If this field is set retranslator use it instead of real device id to forward data.

<hr>

## API actions

API base path: `/tracker/retranslator`.

### bind

Creates or updates binding.

**required sub-user rights:** `admin` (available only to master users).

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 999199 |
| retranslator_id | Retranslator ID. | int | 123 |
| fake_device_id | Optional. If set the retranslator will use this value instead of real device ID to forward data. | string | "AI568T" |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/retranslator/bind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 265489, "retranslator_id": 123}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/retranslator/bind?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=265489&retranslator_id=123
    ```

#### response

```json
{ "success": true }
```

#### errors
* 201 - Not found - either tracker or retranslator are not found by provided ID
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 219 - Not allowed for clones of the device – if tracker is a clone.
* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "retranslation" tariff feature available.
* 242 - There were errors during content validation – if `fake_device_id` is invalid for the retranslator's protocol.

<hr>

### list

List tracker retranslators bound to tracker with ID=`tracker_id`.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 999199 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/retranslator/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 265489}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/retranslator/list?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=265489
    ```

#### response

```json
{
   "success": true,
   "list": [{
     "retranslator_id": 4548,
     "fake_device_id": "AI568T"
   }]
}
```

#### errors

* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions, or some other reason.

<hr>

### unbind

Unbinds a tracker from retranslator.

**required sub-user rights:** `admin` (available only to master users).

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 999199 |
| retranslator_id | Retranslator ID. | int | 123 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/retranslator/unbind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 265489, "retranslator_id": 123}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/retranslator/unbind?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=265489&retranslator_id=123
    ```

#### response

```json
{ "success": true }
```

#### errors

* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions, or some other reason.
* 219 - Not allowed for clones of the device – if tracker is a clone.
