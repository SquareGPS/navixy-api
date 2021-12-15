---
title: Obtain API Key
description: How to obtain hash of an API key
---

# Obtaining hash of an API Key

"Hash", "Session key" or "API Key" is a randomly generated string that is used to verify and authenticate actions.
The hash of API key must be passed in most API calls.

!!! warning "Session hash is deprecated"
    To work with the API, it is necessary to use the API key, not the user's session hash.
    Work with API through the user's session is deprecated and will be disabled in the future.
    The only thing that API calls with a user session will work for is creating,
    reading, and deleting API keys.

To get the API key, you first need to get the hash of the user's session,
because creating a new API key using the another API key is not available.

You can get the user's session hash by [user/auth](../resources/commons/user/index.md#auth) 
call with credentials of a user:

    {{ extra.api_example_url }}/user/auth?login=user_login&password=user_password

The response will be like this:

```json
{
  "success": true,
  "hash": "882fb333405d006df0d5a3f410115e92"
}
```                                                             

Where resulting user's session hash is `882fb333405d006df0d5a3f410115e92` (just an example, you will get a different hex string).

After that, you need to get a [list of API keys](../resources/commons/api-keys.md#list) or create a new one using 
the [/api/key/create](../resources/commons/api-keys.md#create) call with obtained user's session hash:

    {{ extra.api_example_url }}/api/key/list?hash=882fb333405d006df0d5a3f410115e92&title=Integration+Key

The response will be like this:

```json
{
  "success": true,
  "value": {
    "hash": "c915157ac483e7319b0b257408bc04e1",
    "create_date": "2021-10-29 12:00:36",
    "title": "Integration Key"
  }
}
```

You must pass API Key hash value with most API calls along other parameters required to make the call.
Otherwise, you will get an error response:

```json
{
  "success": false,
  "status": {
    "code": 3,
    "description": "Wrong hash"
  }
}
``` 

Whenever you see such response, it means that you did not pass hash value properly.

