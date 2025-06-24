---
title: Login redirect
description: >-
  There are a number of options to user login page URL, which you can submit as
  GET-parameters. You may use this feature for providing the links on external
  resources (e.g. your website) to let your use
---

# Login redirect

There are a number of options to user login page URL, which you can submit as GET-parameters.\
You may use this feature for providing the links on external resources (e.g. your website)\
to let your users go straight to the section they need, use some language by default, etc.

### Page section

You can define the section which your users land by default with `partition` parameter:

* `user`– user login page (used by default)
* `demo` – access a chosen demo account
* `register_fast` – quick registration form
* `register_full` – full registration form
* `password_remind` – password reminder

### Language

Use `locale` parameter to define which language will be used:

* `en_EN`– English
* `es_ES` – Spanish
* `ru_RU` – Russian
* etc.

If this parameter is omitted, the language which was set by default for your service will be used.

### Examples

The next code will land user on login section with Spanish language:

```
http://<your_login_page_url>/login/?partition=demo&locale=es_ES
```

The code below lands user on quick registration form with default language set by default:

```
http://<your_login_page_url>/login/?partition=quick_register&locale=es_ES
```
