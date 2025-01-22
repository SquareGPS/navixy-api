---
title: Notification
description: API calls to read and update notification settings. 
---

# Notification Settings

Notification settings in the Navixy Admin Panel are used to manage and configure alerts and notifications for various events and conditions. These settings allow you to customize notification channels, specifying how notifications are delivered, including options like email, SMS, or push notifications.

## Notification Settings Object

Let's explore the Notification Setting object using the following example:

```json
{
    "email_from": "Navixy <no-reply@navixy.com>", 
    "email_footer": "\n\n—-nSincerely, Navixy",
    "email_special": "no-reply@navixy.com",
    "sms_originator": "demo.navixy.com",
    "caller_id": "491761234543"
}
```

* `email_from` - string. The email address from which notification messages will be sent. This can be a simple email address ("no-reply@navixy.com") or an email address with a name ("Navixy <no-reply@navixy.com>").
* `email_footer` - string. A footer added to all notification emails. This can be any text up to 600 characters.
* `email_special` - string. A special email address used for PaaS reports.
* `sms_originator` - string. The originator for SMS notifications. The maximum length is 20 characters and must match the regex pattern `(p{L}|d|[-'" .,:/])*`, e.g., "demo.navixy.com" or "491761234567".
* `caller_id` - string. The originator for voice messages. The maximum length is 20 characters and must match the regex pattern `(p{L}|d|[-'" .,:/])*`, e.g., "491761234543".


## API actions

API path: `panel/dealer/settings/notification`.

### `read`

Gets current monitoring notification settings.

*required permissions*: `notification_settings: "read"`.

#### Parameters

Only session `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/settings/notification/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/dealer/settings/notification/read?hash=fa7bf873fab9333144e171372a321b06
    ```

#### Response

```json
{
    "success": true, 
    "value": {
        "email_from": "NAVIXY <no-reply@navixy.com>", 
        "email_footer": "\n\n---nSincerely, Navixy",
        "email_special": "no-reply@navixy.com",
        "sms_originator": "demo.navixy.com",
        "caller_id": "491761234543"
    }
}
``` 

* `value` - [Notification settings object](#notification-settings-object) described above.

#### Errors

[General](../../../../user-api/backend-api/getting-started/errors.md#error-codes) types only.


### `update`

Updates notification settings for the current dealer. 

*required permissions*: `notification_settings: "update"`.

#### Parameters
 
| name           | description                                                                                     | type   |
|:---------------|:------------------------------------------------------------------------------------------------|:-------|
| email_from     | Email from which notification messages will be sent. Can be email address or email with a name. | string |
| email_footer   | Footer which is added to all notification emails. Arbitrary text up to 600 characters.          | string |
| email_special  | Optional. Special email address for PaaS reports.                                               | string |
| sms_originator | SMS originator. Max length is 20.                                                               | string |
| caller_id      | Voice messages originator. Max length is 20.                                                    | string |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/settings/notification/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "email_from": "NAVIXY <no-reply@navixy.com>", "email_footer": "\n\n---nSincerely, Navixy", "sms_originator": "demo.navixy.com", "caller_id": "491761234543"}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors
 
[General](../../../../user-api/backend-api/getting-started/errors.md#error-codes) types only.