---
title: Feedback
description: Contains API call to send a feedback email, ask for help or suggest a new feature.
---

# Feedback

Contains API call to send a feedback email, ask for help or suggest a new feature.

API path: `/feedback`.

## Feedback object

```JSON
{
  "text": "My feedback",
  "useragent": "Chrome/87.0.4280.88",
  "platform": "Windows NT 10.0; Win64; x64",
  "screenshots": ["encoded image1", "encoded image2"],
  "log": <log_file>
}
```

* `text` - string. Feedback text. May not be null.
* `useragent` - optional string. Information about the browser of user.
* `platform` - optional string. Information about the platform of user.
* `screenshots` - optional array of string. base64-encoded data:url image, example: data:image/jpeg;base64,`[encoded image]`.
* `log` - optional log file. Contains log of the browser.

### send_email

Sends an email with user's feedback, ask for help, or suggestion a new feature. The message will be sent to dealer's 
email address for feedback.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| feedback | Message from the user. Screenshot and log will be added to email as attachments. | JSON object |
| type | Optional. One of strings: `support_request` (default), `feature_request` and `review`.  | string enum |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/feedback/send_email' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "feedback": {"text": "I love this platform"}, "type": "review"}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* [General](../../getting-started.md#error-codes) types only.