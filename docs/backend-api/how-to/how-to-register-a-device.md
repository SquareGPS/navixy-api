---
title: Device registration
description: Instruction about device registration on the platform step by step.
---

# How to register a device

Instruction about device registration on the platform step by step.  

It is possible to activate any GPS tracking device listed in the supported models list. 
Every model will be shown with all integrated input types, available rule types and other necessary information.
We need to make several steps to get the device registered on the platform.

Step 1. Check that the platform support registering device model with [list_models](../resources/tracking/tracker/index.md#list_models) 
   API call.

Step 2. Check all plugins available for the user with [plugin/list](../resources/commons/plugin/index.md#list) request.

&ensp;We are interested in the next plugin ids that are used for registration:

* 44 - device registration with optional activation code.
* 37 - device registration with mandatory activation code.
* 35 - mobile app registration with optional activation code.
* 68 - mobile app registration with mandatory activation code.

&ensp;Full information about activation codes and for what purposes they needed 
is [here](https://www.navixy.com/docs/admin-panel-docs/activation-codes/).
     
Step 3. Register the device using the [tracker/register](../resources/tracking/tracker/index.md#register) action.

<hr>

## Tracker registration

There is information about tracker registration with plugins 44 and 37.

### Common parameters

* phone - device's phone number with country code and without `+` sign.
* apn_name - this is the apn that depends on your device's SIM GSM carrier.
* apn_user - it depends on your device's SIM too. нужно про пустые юзер и пассворд сделать, чтобы здесь написать. 
* apn_password - this parameter depends on the GSM carrier as two previous parameters.
* device_id - device's ID. What Id type is used in your device can be found with [list_models](../resources/tracking/tracker/index.md#list_models)
  action and [ID type field](../resources/tracking/tracker/index.md#id-type)
* model - name of the model in the platform's code. It can be found in the [list_models](../resources/tracking/tracker/index.md#list_models) request too.
* label - label for the device.
* group_id - tracker group id, 0 if tracker does not belong to any group. The specified group must exist. See [group/list](../resources/tracking/tracker/group.md#list).
* plugin_id - what parameter ID to use. It must be listed in available [plugins list for the user](../resources/commons/plugin/index.md#list).
* activation_code - optional string with activation code. Not necessary for plugin 44 and mandatory for plugin 37.

<hr>

### Using plugin id 44

For example, we have a Teltonika FMB 140 device with IMEI 986575154632586. SIM's phone is 999999999969 and APN settings are
internet, user, and passwd. It is supported on the platform and user has the plugin 44. Activation codes are optional for this plugin.
We don't need to register it to the special group, so the group_id will be 0. The label should be as my car's plate 
number T571TO for convenience.

The API call will be the next:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/register' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "label": "T571TO", "group_id": 0, "plugin_id": 44, "model": "telfmb140", "phone": "999999999969", "device_id": "986575154632586", "apn_name": "internet", "apn_user": "user", "apn_password": "passwd"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/register?hash=a6aa75587e5c59c32d347da438505fc3&label=T571TO&group_id=0&plugin_id=44&model=telfmb140&phone=999999999969&device_id=986575154632586&apn_name=internet&apn_user=user&apn_password=passwd
    ```

After sending the platform will respond with the next information:

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

* Tracker object fields described [here](../resources/tracking/tracker#tracker-object-structure).

<hr>

### Using plugin id 37

In this example we need to specify an activation code during the registration. All other information will be the same as
for the plugin 44. In this case, we have empty apn_user and apn_password to show the usage.

The API call will be the next:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/register' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "label": "T571TO", "group_id": 0, "plugin_id": 37, "activation_code": "6045325592", "model": "telfmb140", "phone": "999999999969", "device_id": "986575154632586", "apn_name": "internet"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/register?hash=a6aa75587e5c59c32d347da438505fc3&label=T571TO&group_id=0&plugin_id=37&activation_code=6045325592&model=telfmb140&phone=999999999969&device_id=986575154632586&apn_name=internet
    ```

The platform will confirm with the same information as for plugin 44.

<hr>

## Mobile app registration

### Common parameters

* notification_email - optional parameter. Notification with invitation to install the app will be sent to the specified in
parameter email.
* notification_phone - optional parameter. Invitation to install the app will be sent to the specified phone. Phone should
be specified in international format without `+` sign.
* model - enum with model always the same = `mobile_unknown_xgps`.
* label - string with name of your device.
* group_id - tracker group id, 0 if tracker does not belong to any group. The specified group must exist. See [group/list](../resources/tracking/tracker/group.md#list).
* plugin_id - what parameter ID to use. It must be listed in available [plugins list for the user](../resources/commons/plugin/index.md#list).
* activation_code - optional string with activation code. Not necessary for plugin 35 and mandatory for plugin 68.

<hr>

### Using parameter 35

For example, we need to activate the app for our employee Andrew. So we can name the device with his name for 
convenience. Also, we will send an invitation by SMS using his phone number.

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

<hr>

### Using plugin id 68

If our user has mandatory activation codes (plugin 68) we should use this parameter when registering a new device.

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

<hr>

## The device doesn't register

There could be several reasons - why the device doesn't register. If we omit the problems with the SMS gateway, and it works
perfectly - all issues listed [here](https://www.navixy.com/docs/troubleshooting/user-interface/device-activation-problems/).
When we eliminated all possible issues and checked that everything works well we can send 
[tracker/register_retry](../resources/tracking/tracker/index.md#register_retry)  request to not create the same unit for
the user. Moreover, it is not possible to register two devices with the same ID on the platform.

