---
title: Feedback
description: Contains feedback object and API call to send a feedback email, ask for help or suggest a new feature.
---

# Feedback

Contains feedback object API call to send a feedback email, ask for help or suggest a new feature.

<hr>

## Feedback object

```JSON
{
  "text": "My feedback",
  "log": "User agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36\nClient Id: 184541\nhttp://20410.navixy.ru/#/staff/tasks"
}
```

* `text` - string. Feedback text. May not be null.
* `log` - optional log file. Contains log of the browser, user agent, browser platform.

<hr>

## API actions

API path: `/feedback`.

### send_email

Sends an email with user's feedback, ask for help, or suggestion a new feature. The message will be sent to dealer's 
email address for feedback.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| feedback | Message from the user. Screenshot and log will be added to email as attachments. | JSON object |
| type | Optional. One of strings: `support_request` (default), `feature_request` and `review`.  | [enum](../../getting-started.md#data-types) |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/feedback/send_email' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "feedback": {"text": "I love this platform"}, "type": "review"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/feedback/send_email?hash=&feedback={"text": ""}&type=
    ```

#### response

```json
{
  "success": true
}
```

#### errors

* [General](../../getting-started.md#error-codes) types only.
