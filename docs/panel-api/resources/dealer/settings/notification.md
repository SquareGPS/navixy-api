---
title: /notification
description: /notification
---

## read

Get current monitoring notification settings.

#### required permissions:

*   **notification_settings**: "read"

#### response

    {
        "success": true, 
        "value": {
            "email_from": ${string},     // email from which notification messages are sent. 
                                         // can be email address (noreply@whereami.ru) or email with name ("DEMO NAVIXY" <no-reply@gdemoi.ru>) 
            "email_footer": "\n\n---nSincerely, Navixy", // footer which is added to all notification emails. 
                                         // Arbitrary text up to 600 characters.
            "email_special": ${string},  // special email address for PaaS reports
            "sms_originator": ${string}, // max length is 20, must match (p{L}|d|[-'" .,:/])* . E.g. "demo.navixy.com" or "491761234567" 
            "caller_id": ${string}       // voice messages originator. Max length is 20, must match (p{L}|d|[-'" .,:/])* . E.g. "491761234543"
        }
    }
    

#### errors

No specific errors.

## update

Update notification settings for the current dealer. 

#### required permissions:

*   **notification_settings**: "update"

#### parameters
 
all fields from the dealer/settings/notification/read response 

#### response

    {"success": true}
    

#### errors
 
No specific errors.