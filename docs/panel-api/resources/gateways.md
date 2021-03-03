---
title: Gateways
description: Information about email gateways objects. Email gateway can be owned by a dealer or leased from platform owner.
---

# Gateways

Information about email gateway objects. Email gateway can be owned by a dealer or leased from platform owner.

API path: `/gateways/email`.

## Email gateway object

Own email gateway:
Now supported only SMTP provider.

```json
{
  "id": 2,
  "leasable": false,
  "label": "Paas gate",
  "provider": "smtp",
  "params": {
    "default_from_address": "no-reply@domain.tld",
    "mail.smtp.user": null,
    "mail.smtp.password": null,
    "mail.smtp.host": "localhost",
    "mail.smtp.port": 25,
    "mail.smtp.ssl.port": 465,
    "mail.smtp.ssl.trust_all_hosts": false,
    "mail.smtp.auth": true,
    "mail.debug": false,
    "mail.smtp.starttls.enable": false,
    "mail.smtp.starttls.required": false,
    "mail.smtp.use_ssl": false,
    "mail.smtp.timeout": 60000,
    "mail.smtp.connectiontimeout": 60000,
    "mail.transport.protocol": "smtp"
  }
}
```

Leasable email gateway:

```json
{
  "id": 1,
  "label": "Platform gate",
  "default_from_address": "no-reply@domain.tld"
}
```

### list

Gets list of available email gateways for the panel.

*required permissions*: `email_gateways: "read"`.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/gateways/email/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/gateways/email/list?hash=fa7bf873fab9333144e171372a321b06
    ```
   
#### response

```json
{
    "success": true,
    "bound_gateway": 2,
    "own": [{
      "id": 1,
      "leasable": false,
      "label": "Paas gate",
      "provider": "smtp",
      "params": {
        "default_from_address": "no-reply@domain.tld",
        "mail.smtp.user": null,
        "mail.smtp.password": null,
        "mail.smtp.host": "localhost",
        "mail.smtp.port": 25,
        "mail.smtp.ssl.port": 465,
        "mail.smtp.ssl.trust_all_hosts": false,
        "mail.smtp.auth": true,
        "mail.debug": false,
        "mail.smtp.starttls.enable": false,
        "mail.smtp.starttls.required": false,
        "mail.smtp.use_ssl": false,
        "mail.smtp.timeout": 60000,
        "mail.smtp.connectiontimeout": 60000,
        "mail.transport.protocol": "smtp"
      }
    }]
    "leasable": [
        {
            "id": 2,
            "label": "Default",
            "provider": "mandrill_smtp",
            "default_from_address": "no-reply@x-gpsmail.com"
        }
    ]
}
```

#### errors

[General](../../backend-api/getting-started.md#error-codes) types only.