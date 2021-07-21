---
title: Getting Started
description: Overview of Navixy Panel API
---

## Navixy Panel API

The structure of Panel API (aka Administration API) – request paths, 
response and error formats – is the same as for user API, so we highly 
recommend reading [Backend API: getting started][1].

  [1]: ../backend-api/getting-started.md

Two main differences are _authorization system_ and _request paths_.

<hr>

### Panel API base URL

Panel API resides in `panel/` subsection of API url. So you can determine URL to API calls like this:

*  `https://api.eu.navixy.com/v2/panel/` for European Navixy ServerMate platform.
*  `https://api.us.navixy.com/v2/panel/` for American Navixy ServerMate platform.
*  `https://api.your_domain/panel/` for the self-hosted (On-Premise) installations.

For example, to make `account/auth` 
API call in Navixy ServerMate, you should use the URL: 

    {{ extra.api_example_url }}/panel/account/auth

<hr>

### Authorization

In order to authorize, you should make a GET or POST request to 
`/account/auth/` with `login` (your administration panel login) 
and `password` (its password), which returns JSON object, 
containing `hash` (hexademical unique string) of the newly 
created Panel API session, which you should use in other Panel API calls.

Please note that you cannot use Panel API session hash in user API or vice versa.

You must keep in mind that string type containing any symbols except ASCII 
codes from 32 to 127 must be [URL encoded][2] before transfer.

   [2]: https://en.wikipedia.org/wiki/Percent-encoding

For example, in on-premise installations, there is a default user with login 
`admin` and password `admin`. You can authorize with it like this 
(all HTTP request examples are made using [curl](https://curl.haxx.se/) *nix utility):

=== "POST"
    ```abap
    $ curl -d 'login=admin&password=admin' \
           -X POST http://api.domain.com/v2/panel/account/auth/
    ```

=== "GET"
    This method is not recommended. Just for example:
    ```abap
    $ curl http://api.domain.com/panel/v2/account/auth/?login=admin&password=admin
    ```


And you'll get answer like this:

```json
{
  "hash": "1dc2b813769d846c2c15030884948117",
  "success": true,
  "permissions": { ... }
}
```

The value returned in `hash` field (in this example it is 
`1dc2b813769d846c2c15030884948117`) should be saved for further use.

If API call completes successfully, the HTTP response code is `200 OK`, 
and `success` field in returned JSON is equal to `true`.

If there is any error, for example, wrong credentials were used, HTTP 
response code differs from 200, `success` field is `false`, and `status` 
field contains the description of the error.

For example:

```json
{
  "success": false,
  "status": {
    "code": 12,
    "description": "Dealer not found"
  }
}
```

The "description" field is just a human-readable hint, you should not check 
its contents programmatically as it may change in the future.

For more info, please see `account/auth`.

<hr>

### Using session hash

After successful authorization, you can make other Panel API calls. 
You should **always** pass the session hash you obtained earlier as the `hash` parameter.
This parameter is not listed in parameters list of every API call, but still required by default.

For example, to list first ten users belonging to your system account,
you can use the following Panel API call (the hash is from previous example):

```abap
$ curl -X POST 'http://api.domain.com/v2/panel/user/list/' \
       -d 'hash=1dc2b813769d846c2c15030884948117&limit=10'
```

<hr>

### Session expiration

Every session (and thus, a hash key associated with it) has a limited 
lifetime (30 days by default). So you should obtain new hash key periodically.

If you will try to make a Panel API call with expired session hash, you'll 
get the following error:

```json
{
  "success": false,
  "status": {
    "code": 4,
    "description": "User not found or session ended"
  }
}
```

In this case, just obtain new hash using `account/auth`.

<hr>

### Panel API Permissions

Every call to panel api requires a set (possibly empty) of permissions. 
To determine if user is allowed to execute api call, user's permissions 
is compared with call's required permissions. If user does not have at least 
one required permission, the call is not executed and error "Operation not permitted" is returned.

Each permission is defined as a pair of category (e.g. `trackers`) and operation (e.g. `read`).
A set of permissions within one category is often grouped as in the following example:

*   `trackers`: create, read

This defines two permissions: (`trackers`, `create`) and (`trackers`, `read`).

List of all possible categories and operations:

*   `accounting`: generate
*   `activation_code`: create, read, update
*   `base`: get_dealer_info
*   `notification_settings`: read, update
*   `service\_settings`: read, update
*   `tariffs`: create, read, update
*   `trackers`: create, read, update, delete
*   `transactions`: create, read, update
*   `users`: create, read, update, delete
*   `user\_sessions`: create
*   `sms`: create
*   `tracker\_bundles`: read, update
