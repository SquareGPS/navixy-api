---
title: Base
description: Contains API calls to health-check and send email.
---

# Base

Contains API calls to health-check and send email.

<hr>

## API actions

API path: `/base`.

### nothing

The report for health-check. It will do nothing.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/base/nothing' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/base/nothing?hash=
    ```

#### response

```json
{ "success": true }
```

#### errors

* [General](../../getting-started.md#error-codes) types only.

<hr>

### send_email

Sends email from the platform to any email address with specified title and text. Needs ROOT access level.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| from | From email address. | string|
| to | To email address. | string |
| title | Title of the email. | string |
| message | Text of the email. | string |
| service_id | Service parameter. | int |
| service_pass | Service parameter. | int |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/base/send_email' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "from": "gps@navixy.com", "to" : "customer@email.com", "title": "test email", "message": "this email for test", "service_id": 1, "service_pass": 28}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/base/send_email?hash=&from=&to=&title=&message=&service_id=&service_pass=
    ```

#### response

```json
{ "success": true }
```

#### errors

* [General](../../getting-started.md#error-codes) types only.
