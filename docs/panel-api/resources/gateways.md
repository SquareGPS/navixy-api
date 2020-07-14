---
title: /gateways
description: /gateways
---

## email(...)

Email gateway can be owned by dealer or leased from platform owner.

Own email gateway:
Now supported only SMTP provider.

    {
      "id": 2, //unique ID
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


Leasable email gateway:

     {
         "id": 1,
         "label": "Platform gate",
         "default_from_address": "no-reply@domain.tld"
     }