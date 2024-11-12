---
title: Mobile app register
description: API call to register a mobile application. Deprecated.
---
# Mobile app register

!!! warning "Deprecated"
    This API action deprecated and should not be used.

API call to register a mobile application. Use [tracker/register](index.md#register) with `plugin_id` 35.


## API actions

API base path: `/tracker/mobile`.

### register

Registers new mobile client application.

**required sub-user rights:** `tracker_register`.

#### Parameters

Part of parameters are registration plugin-specific. See "Registration plugins" section.

Common parameters are:

| name                   | description                                                                                                                                                                                 | type    | format          |
|:-----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|:----------------|
| label                  | User-defined label for this tracker. Must consist of printable characters and have length between 1 and 60.                                                                                 | string  | "Courier"       |
| group_id               | Tracker group id, 0 if tracker does not belong to any group. The specified group must exist. See [group/list](group.md#list).                                                               | int     | 0               |
| device_id              | **Must** be specified if device model uses fixed device id. See [tracker/list_models](index.md#list_models).                                                                                | string  | "4568005588562" |
| send_register_commands | Indicates send or not to send activation commands to device (via SMS or GPRS channel). If parameter is not specified or equals  `null` will be used the platform settings. Default: `null`. | boolean | true/false      |

#### Response

```json
{
    "success": true,
    "value": {<tracker>}
}
```

For `tracker` object structure, see [tracker/](index.md#tracker-object-structure).

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 204 – Entity not found - if specified group does not exist.
* 221 – Device limit exceeded - if device limit set for the user's dealer has been exceeded.
* 224 – Device ID already in use - if specified device ID already registered in the system.
* 225 – Not allowed for this legal type - if tariff of the new device is not compatible with user's legal type.
