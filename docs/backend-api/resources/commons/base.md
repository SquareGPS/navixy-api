---
title: Base
description: Base
---

# Base

API path: `/base`.

### nothing

The report for health-check. It will do nothing.

#### example

    {{ extra.api_example_url }}/base/nothing?hash=22eac1c27af4be7b9d04da2ce1af111b

#### response

```json
{ "success": true }
```


### send_email

Sends email from the platform to any email address with specified title and text. Needs ROOT access level.

#### structure:

    {{ extra.api_example_url }}/base/send_email?hash=your_hash&from=sender_mail&to=recipient_mail&title=text_title&message=text_message&service_id=1&service_pass=1

#### parameters

| name | description | type| format|
| :------: | :------: | :-----:| :------:|
| from | from email address | string| from@mail.com |
| to | to email address | string | to@mail.com|
| title | title of the email | string | example title|
| message | text of the email | string | example message |
| service_id | service parameter | int | 1 |
| service_pass | service parameter | int | 1 |

#### example

    {{ extra.api_example_url }}/base/send_email?hash=22eac1c27af4be7b9d04da2ce1af111b&from=b2field@mail.com&to=user@mail.com&title=text+of+email+title&message=text+of+the+message&service_id=1&service_pass=1

#### response

```json
{ "success": true }
```
