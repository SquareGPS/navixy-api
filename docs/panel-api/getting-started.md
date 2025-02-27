---
title: Getting Started
description: Overview of Navixy Admin Panel API
---

# Navixy Admin Panel API

The Admin Panel API (or Panel API for short) allows developers to manage various entities within the Navixy Admin Panel. This documentation provides detailed information on how to interact with the API, including the methods and parameters required for effective management of your Navixy environment.

## Introduction

The Admin Panel API is designed to help administrators and developers manage the Navixy platform more efficiently. Whether you are managing users, devices, or settings, this API provides the necessary tools to automate and streamline these tasks.

The structure of the Admin Panel API mirrors that of the Backend API, making it advantageous to read [Backend API: Getting Started](../user-api/backend-api/getting-started/introduction.md). The only differences lie in the authorization system and request paths.

### Base URL

The Admin Panel API is accessible via the `panel/` subsection of the API URL. The URLs for different Navixy platforms are as follows:

* European Navixy ServerMate platform: `https://api.eu.navixy.com/v2/panel/`
* American Navixy ServerMate platform: `https://api.us.navixy.com/v2/panel/`
* Self-hosted (On-Premise) installations: `https://api.your_domain/panel/`

For example, to make an `account/auth` API call on the Navixy ServerMate platform, you would use the following URL:

    {{ extra.api_example_url }}/panel/account/auth

### Authorization

To authorize, make a GET or POST request to `/account/auth/` with your `login` (your administration panel login) and `password`. This will return a JSON object containing a `hash` (a unique hexadecimal string) for the newly created Admin Panel API session. Use this session hash in other Panel API calls.

Please note that you cannot use the Admin Panel API session hash in the user API, and vice versa.

Keep in mind that any string containing symbols outside ASCII codes 32 to 127 must be [URL encoded](https://en.wikipedia.org/wiki/Percent-encoding) before transfer.

#### Example Authorization

In on-premise installations, there is a default user with login `admin` and password `admin`. You can authorize with these credentials as follows (all HTTP request examples are made using the [curl](https://curl.haxx.se/) *nix utility):

##### POST Request
```sh
$ curl -d 'login=admin&password=admin' \
       -X POST http://api.domain.com/v2/panel/account/auth/
```

##### GET Request
This method is not recommended and provided just for example:
```sh
$ curl http://api.domain.com/panel/v2/account/auth/?login=admin&password=admin
```

##### Response
You will receive a response like this:
```json
{
  "hash": "1dc2b813769d846c2c15030884948117",
  "success": true,
  "permissions": { ... }
}
```

The value returned in the `hash` field (in this example, `1dc2b813769d846c2c15030884948117`) should be saved for further use.

### Error Handling

When an API call completes successfully, the HTTP response code will be `200 OK`, and the `success` field in the returned JSON will be `true`.

In case of an error, such as incorrect credentials, the HTTP response code will differ from 200, the `success` field will be `false`, and the `status` field will contain a description of the error.

#### Example Error Response
```json
{
  "success": false,
  "status": {
    "code": 12,
    "description": "Dealer not found"
  }
}
```

The `description` field provides a human-readable hint and should not be used programmatically as it may change in the future.

For more information, please refer to `account/auth`.

### Using Session Hash

After successful authorization, you can make other Admin Panel API calls. Always pass the session hash you obtained earlier as the `hash` parameter. This parameter is required by default, even though it is not listed in the parameter list of every API call.

#### Example
To list the first ten users belonging to your system account, use the following Admin Panel API call (using the hash from the previous example):

```bash
$ curl -X POST 'http://api.domain.com/v2/panel/user/list/' \
       -d 'hash=1dc2b813769d846c2c15030884948117&limit=10'
```

### Session Expiration

Each session, along with its associated hash key, has a default lifespan of 24 hours. You need to periodically obtain a new hash key.

If you attempt to make a Admin Panel API call with an expired session hash, you will receive an error:

```json
{
  "success": false,
  "status": {
    "code": 4,
    "description": "User not found or session ended"
  }
}
```

To resolve this, simply obtain a new hash using `account/auth`.

### How to Securely Share Panel's Credentials

To securely share access to the admin panel, we recommend creating supplemental technical (service) accounts. At this time it can be done by [contacting the Navixy support team](../general/contacts.md) and providing the email address for the technical account. You will then receive a login and password for the account.

Capabilities of a technical accounts:

* Add new users
* Modify data of current users
* Add new trackers
* Clone current trackers
* Change owner of a tracker
* Change tracker data plan
* Analyze incoming data with the air console

Restrictions for technical accounts:

* Delete users
* Remove trackers
* Add, change, or delete plans
* Change platform settings

### Admin Panel API Permissions

Every call to the Admin Panel API requires a set (possibly empty) of permissions. To determine if a user is allowed to execute an API call, the user's permissions are compared with the required permissions for the call. If the user does not have at least one required permission, the call is not executed, and an "Operation not permitted" error is returned.

Each permission is defined as a pair of category (e.g., `trackers`) and operation (e.g., `read`). A set of permissions within one category is often grouped, as shown in the following example:

* `trackers`: create, read

This defines two permissions: (`trackers`, `create`) and (`trackers`, `read`).

List of all possible categories and operations:

* `accounting`: generate
* `activation_code`: create, read, update
* `base`: get_dealer_info
* `notification_settings`: read, update
* `service_settings`: read, update
* `tariffs`: create, read, update
* `trackers`: create, read, update, delete
* `transactions`: create, read, update
* `users`: create, read, update, delete
* `user_sessions`: create
* `sms`: create
* `tracker_bundles`: read, update
