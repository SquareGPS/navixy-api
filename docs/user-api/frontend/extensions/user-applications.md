---
title: User apps
description: Information about adding of created apps to the UI
---

# User apps

You can add your own application to the user interface. It will appear as an additional tab in the "Applications" menu.
In order for the app to work within the platform, it needs to support iframe feature.
If you don't have an iframe option, the app can be added as a separate link, in which case a new browser tab will open 
when you click on it.
Some apps have been developed by our partners and are available in [Marketplace](https://marketplace.navixy.com/). 
To add them, contact the developer of the application.

!!! note "If your domain is using an HTTPS connection, the link to the application must also be HTTPS. Otherwise, you will encounter a mixed content error." 


## Authorization in the application

When you open an application through the Navixy interface, user session hash will be sent to the URL of the application by 
GET method. This hash can be used for authorization within the application.


## Cookie

By default, the web server sends the following cookies when an external application link opens:

* User session hash as `hash=a6aa75587e5c59c32d347da438505fc3`.
* Locale as `locale=en`.

!!! note "If you do not want the server to send cookies, inform technical support and this function will be disabled."

## How to add an application

### Cloud version

Contact [Navixy technical support](../../../general/contacts.md) and specify the following parameters:

* Application name.
* External URL link.
* Opening method - iframe or a new tab.
* Installation destination - user_id or panel_id.
* Cookies sending - user session hash and/or locale or nothing.

Our specialists will do everything necessary, and the application will be available in the user interface.
The application can be installed for all users or for a specific one.

!!! note "If the app will be installed to the specific user, please contact the support team every time you need to add this app to another user. If the app installed for whole panel - all new users will automatically get the app. Also, the app can be installed to whole panel instead of specific users."


### Standalone version

You can find the instruction on installation of the software [here](https://docs.navixy.com/on-premise/applications).
