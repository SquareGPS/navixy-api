---
title: /feedback
description: /feedback
---

# feedback/

    <feedback> = {
      "text": <feedback text, string, may not be null>,
      "useragent": <optional, string>,
      "platform": <optional, string>,
      "screenshots": <optional, array of strings, base64-encoded data:url image, example: data:image/jpeg;base64,[encoded image]>,
      "log": <optional, log file>
    }

## send_email(…)

#### parameters

*   feedback
*   type – optional

Send email with feedback message on feedback.toEmail Where **type** is one of strings: **support_request**(default), **feature_request** and **review**.  
Screenshot and log will be added to email as attachments.

#### return

```json
{ "success": true }
```
