---
title: Notification
description: API calls to read and update notification settings. 
---

# Notification

API calls to read and update notification settings.

***

## Notification settings object

```json
{
    "email_from": "NAVIXY <no-reply@navixy.com>", 
    "email_footer": "\n\n---nSincerely, Navixy",
    "email_special": "no-reply@navixy.com",
    "sms_originator": "demo.navixy.com",
    "caller_id": "491761234543"
}
```

* `email_from` - string. Email from which notification messages will be sent. Can be email address ("no-reply@navixy.com") or email with a name ("NAVIXY <no-reply@navixy.com>").
* `email_footer` - string. Footer which is added to all notification emails. Arbitrary text up to 600 characters.
* `email_special` - string. Special email address for PaaS reports.
* `sms_originator` - string. Max length is 20, must match `(p{L}|d|[-'" .,:/])*`. E.g. "demo.navixy.com" or "491761234567".
* `caller_id` - string. Voice messages originator. Max length is 20, must match `(p{L}|d|[-'" .,:/])*`. E.g. "491761234543".

***

## API actions

API path: `panel/dealer/settings/notification`.

### read

Gets current monitoring notification settings.

*required permissions*: `notification_settings: "read"`.

#### parameters

Only session `hash`.

#### examples

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

#### response

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

#### errors

[General](../../../../backend-api/getting-started.md#error-codes) types only.

***

### update

Updates notification settings for the current dealer. 

*required permissions*: `notification_settings: "update"`.

#### parameters
 
| name | description | type|
| :------ | :------ | :----- |
| email_from | Email from which notification messages will be sent. Can be email address or email with a name. | string |
| email_footer | Footer which is added to all notification emails. Arbitrary text up to 600 characters. | string |
| email_special | Optional. Special email address for PaaS reports. | string |
| sms_originator | SMS originator. Max length is 20. | string |
| caller_id | Voice messages originator. Max length is 20. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/settings/notification/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "email_from": "NAVIXY <no-reply@navixy.com>", "email_footer": "\n\n---nSincerely, Navixy", "sms_originator": "demo.navixy.com", "caller_id": "491761234543"}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors
 
[General](../../../../backend-api/getting-started.md#error-codes) types only.