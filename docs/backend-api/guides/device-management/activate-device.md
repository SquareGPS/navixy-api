
This guide offers detailed, step-by-step instructions on using the Navixy API to activate GPS tracking devices and X-GPS Mobile Apps on the platform.

Within a user account, you can activate:
* Any GPS tracking device listed in the [supported models](https://navixy.com/devices) list
* X-GPS Mobile Apps

Follow these steps to successfully activate your device on the platform:

####  Step 1: Verify device model support

Ensure that the platform supports the device model using the [`list_models`](../../resources/tracking/tracker/index.md#list_models) API call.


#### Step 2: Check available plugins

Check all plugins available for the user with the [`plugin/list`](../../resources/commons/plugin/index.md#list) request. The following plugin IDs are used for activation:

- 44 - Device activation with optional activation code.
- 37 - Device activation with mandatory activation code.
- 35 - Mobile app activation with optional activation code.
- 68 - Mobile app activation with mandatory activation code.

Full information about activation codes and their purposes is available [here](https://docs.navixy.com/admin-panel/activation-codes).


#### Step 3: Activate the device

Activate the device using the [`tracker/register`](../../resources/tracking/tracker/index.md#register) action.

## GPS tracker activation

This section provides information about activating GPS trackers using plugins 44 and 37, and the [`tracker/register`](../../resources/tracking/tracker/index.md#register) action.

**Common parameters**

* `phone` - Device's phone number with country code and without the `+` sign.
* `apn_name` - The APN that depends on your device's SIM GSM carrier. Max length 40.
* `apn_user` - This depends on your device's SIM too. Max length 40, can be empty.
* `apn_password` - This parameter depends on the GSM carrier as the two previous parameters. Max length 40, can be empty.
* `device_id` - Device's ID. The ID type used in your device can be found with the [list_models](../../resources/tracking/tracker/index.md#list_models) action and [ID type field](../../resources/tracking/tracker/index.md#id-type).
* `model` - Name of the model in the platform's code. It can be found in the [list_models](../../resources/tracking/tracker/index.md#list_models) request too.
* `label` - Label for the device.
* `group_id` - Tracker group ID, 0 if the tracker does not belong to any group. The specified group must exist. See [group/list](../../resources/tracking/tracker/group.md#list).
* `plugin_id` - Parameter ID to use. It must be listed in the available [plugins list for the user](../../resources/commons/plugin/index.md#list).
* `activation_code` - Optional string with activation code. Not necessary for plugin 44 and mandatory for plugin 37.


### Activation with optional activation code

By using plugin 44, the activation process is simplified, as the [activation code](https://docs.navixy.com/admin-panel/activation-codes) is not mandatory, making it easier to manage multiple devices without needing individual codes for each.

For example, let's consider a Teltonika FMB 140 device with IMEI `986575154632586`. The device's SIM phone number is `999999999969` and its APN settings are `internet`, `user`, and `passwd`. This device is supported on the platform, and the user has plugin 44, which allows for device activation with an optional activation code.

In this case, we don't need to assign the device to a specific group, so `group_id` will be set to `0`. For convenience, the device label can be set to a descriptive name, such as a car's plate number, e.g., `T571TO`.

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/tracker/register' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "a6aa75587e5c59c32d347da438505fc3",
        "label": "T571TO",
        "group_id": 0,
        "plugin_id": 44,
        "model": "telfmb140",
        "phone": "999999999969",
        "device_id": "986575154632586",
        "apn_name": "internet",
        "apn_user": "user",
        "apn_password": "passwd"
    }'
```

=== "HTTP GET"

```
{{ extra.api_example_url }}/tracker/register?hash=a6aa75587e5c59c32d347da438505fc3&label=T571TO&group_id=0&plugin_id=44&model=telfmb140&phone=999999999969&device_id=986575154632586&apn_name=internet&apn_user=user&apn_password=passwd
```

After sending the platform will respond with the following information:

```json
{
  "success":true,
  "value":{
    "id":833389,
    "label":"T571TO",
    "group_id":0,
    "source":{
      "id":526383,
      "device_id":"986575154632586",
      "model":"telfmb140",
      "blocked":false,
      "tariff_id":12163,
      "phone":"999999999969",
      "status_listing_id":null,
      "creation_date":"2021-06-03",
      "tariff_end_date":"2021-06-17"
    },
    "clone":false
  }
}
```

Tracker object fields are described [here](../../resources/tracking/tracker/index.md#tracker-object-structure).

### Activation with mandatory activation code

When  [activation codes](https://docs.navixy.com/admin-panel/activation-codes)  are required for device activation, use plugin 37.

For example, we have a Teltonika FMB 140 device with IMEI `986575154632586`. The device's SIM phone number is `999999999969`, and its APN settings are `internet`, with `apn_user` and `apn_password` left empty. This device is supported on the platform, and the user has plugin 37, which mandates the use of an activation code.

The API call will be as follows:

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/tracker/register' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "a6aa75587e5c59c32d347da438505fc3",
        "label": "T571TO",
        "group_id": 0,
        "plugin_id": 37,
        "activation_code": "6045325592",
        "model": "telfmb140",
        "phone": "999999999969",
        "device_id": "986575154632586",
        "apn_name": "internet"
    }'
```

=== "HTTP GET"

```
{{ extra.api_example_url }}/tracker/register?hash=a6aa75587e5c59c32d347da438505fc3&label=T571TO&group_id=0&plugin_id=37&activation_code=6045325592&model=telfmb140&phone=999999999969&device_id=986575154632586&apn_name=internet
```

The platform will confirm with the same information as for plugin 44.

### Activation without sending activation commands 

The [`register_quick`](../../resources/tracking/tracker/index.md#register_quick) API endpoint allows for the rapid registration of a new tracker using only its IMEI. This method is designed for situations where the device is already preconfigured and does not require automatic SMS commands to be sent for activation. It is particularly useful for managing bundles of devices efficiently.

#### Why use `register_quick`

Using the `register_quick` method streamlines the activation process by minimizing the parameters required for registration. This is ideal for scenarios where a large number of preconfigured GPS devices need to be activated quickly, without the need for additional configuration or SMS commands.

#### How to use `register_quick`

To use the `register_quick` API call, ensure that you have the necessary sub-user rights (`tracker_register`). The following parameters are required:

- `label`: A user-defined label for the tracker. It must consist of printable characters and have a length between 1 and 60.
- `group_id`: The ID of the tracker group. Use `0` if the tracker does not belong to any group. The specified group must exist (see `group/list`).
- `imei`: The IMEI of the tracker.

**Example Request:**

=== "cURL"

```shell
curl -X POST 'https://api.navixy.com/v2/tracker/register_quick' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "a6aa75587e5c59c32d347da438505fc3",
        "label": "Courier",
        "group_id": 0,
        "imei": "35645587458999"
    }'
```

**Example Response:**

```json
{
    "success": true,
    "value": {
        "id": 123456,
        "label": "tracker label",
        "clone": false,
        "group_id": 167,
        "avatar_file_name": "file name",
        "source": {
            "id": 234567,
            "device_id": 9999999988888,
            "model": "telfmb920",
            "blocked": false,
            "tariff_id": 345678,
            "status_listing_id": null,
            "creation_date": "2011-09-21",
            "tariff_end_date": "2016-03-24",
            "phone": "71234567890"
        },
        "tag_bindings": [{
            "tag_id": 456789,
            "ordinal": 4
        }]
    }
}
```

For more details on the tracker object structure, see [tracker](../../resources/tracking/tracker/index.md#tracker-object-structure).

Using the `register_quick` endpoint can significantly speed up the process of activating multiple preconfigured devices, making it an essential tool for managing device bundles efficiently.

### Troubleshooting GPS tracker activation

There could be several reasons why a device doesn't activate. If we exclude SMS gateway issues, and it is functioning correctly, all other potential issues are listed [here](https://www.navixy.com/docs/user/get-started-docs/tracker-activation/device-activation-problems/).

After eliminating all possible issues and ensuring everything is working properly, you can send the [`tracker/register_retry`](../../resources/tracking/tracker/index.md#register_retry) request to avoid creating the same unit again for the user. Additionally, it is not possible to activate two devices with the same ID on the platform.

## Mobile app activation

X-GPS Tracker mobile app allow for real-time monitoring of employees with smartphones and tablets. This section provides information about adding mobile devices with X-GPS Tracker mobile apps to a user account using the [`tracker/register`](../../resources/tracking/tracker/index.md#register) action.

**Common parameters**

* `notification_email` - Optional parameter. A notification with an invitation to install the app will be sent to the specified email.
* `notification_phone` - Optional parameter. An invitation to install the app will be sent to the specified phone. The phone should be specified in international format without the `+` sign.
* `model` - Enum with model always set to `mobile_unknown_xgps`.
* `label` - String with the name of your device.
* `group_id` - Tracker group ID, 0 if the tracker does not belong to any group. The specified group must exist. See [`group/list`](../../resources/tracking/tracker/group.md#list).
* `plugin_id` - Parameter ID to use. It must be listed in the available [plugins list for the user](../../resources/commons/plugin/index.md#list).
* `activation_code` - Optional string with an activation code. Not necessary for plugin 35 and mandatory for plugin 68.

### Activation with optional activation code

For example, we need to activate the app for our employee Andrew. To make it convenient, we can name the mobile device after him. Additionally, we will send an invitation via SMS using his phone number.

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/tracker/register' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "label": "Andrew", "group_id": 0, "plugin_id": 35, "model": "mobile_unknown_xgps", "notification_phone": "999877459965"}'
```

=== "HTTP GET"

```
{{ extra.api_example_url }}/tracker/register?hash=a6aa75587e5c59c32d347da438505fc3&label=Andrew&group_id=0&plugin_id=35&model=mobile_unknown_xgps&notification_phone=999877459965
```

The platform will notify us about success and with information about this device. The platform will automatically assign 
`device_id` to the app.

```json
{
   "success": true,
   "value": {
      "id": 833997,
      "label": "Andrew",
      "group_id": 0,
      "source": {
         "id": 526785,
         "device_id": "186196632419",
         "model": "mobile_unknown_xgps",
         "blocked": false,
         "tariff_id": 12163,
         "phone": null,
         "status_listing_id": null,
         "creation_date": "2021-06-04",
         "tariff_end_date": "2021-06-18"
      },
      "clone": false
   }
}
```

### Activation with mandatory activation code

If a user is required to use [activation codes](https://docs.navixy.com/admin-panel/activation-codes) (plugin 68), we should use this parameter when activating a new device.

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/tracker/register' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "label": "Andrew", "group_id": 0, "plugin_id": 68, "activation_code": "6045325592", "model": "mobile_unknown_xgps", "notification_phone": "999877459965"}'
```

=== "HTTP GET"

```
{{ extra.api_example_url }}/tracker/register?hash=a6aa75587e5c59c32d347da438505fc3&label=Andrew&group_id=0&plugin_id=68&activation_code=6045325592&model=mobile_unknown_xgps&notification_phone=999877459965
```

The platform will respond with the same information as for plugin 35.


