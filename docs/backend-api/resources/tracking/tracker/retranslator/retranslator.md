---
title: /retranslator
description: /retranslator
---

## retranslator

**tracker_retranslator_binding** is:
```js
{
    "retranslator_id": <retranslator id>, //int
    "fake_device_id": <optional, if this field is set retranslator use it instead of real device id to retranslate data> //string
}
```

## bind(…)
Create or update binding.

**required subuser rights:** admin (available only to master users)

#### parameters:
* **tracker_id** – **int**. ID of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **retranslator_id** – **int**. retranslator ID
* **fake_device_id** – **string**. if this field is set retranslator use it instead of real device ID to retranslate data.

#### return:
```js
{ "success": true }
```

#### errors:
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason
*   219 (Not allowed for clones of the device) – if tracker is clone
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “retranslation” tariff feature available
*   242 (There were errors during content validation) – if **fake_device_id** is invalid for the protocol

## list(…)
List tracker retranslators binded to tracker with ID=**tracker_id**.

#### parameters:
* **tracker_id** – **int**. ID of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### return:
```js
{
   "success": true,
   "list": [ <tracker_retranslator_binding>, ... ] // list of bindings
}
```

#### errors:
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason

## unbind(…)
Unbind tracker from retranslator.

**required subuser rights:** admin (available only to master users)

#### parameters:
* **tracker_id** – **int**. ID of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **retranslator_id** – **int**. retranslator ID

#### return:
```js
{ "success": true }
```

#### errors:
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason
*   219 (Not allowed for clones of the device) – if tracker is clone
