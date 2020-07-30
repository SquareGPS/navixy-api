---
title: User UI settings
description: User UI settings
---

# User UI settings

API path: `/user/settings/ui`

The user interface settings are intended for storing settings of client applications that use the API. 
One can imagine that this works similarly to the browser cache / local storage mechanism. The feature is that long-term storage of these settings is provided but not guaranteed - when the quota is exceeded, data could be deleted. 

## read()

Read setting value by key.

#### parameters

**key** - string. Length should be between 1 and 50 is 50 symbols, should only contain English letters, digits, '_' and '-'.


#### returns:

```json
{
  "success": true,
  "value": "previously saved value"
}
```

When nonexistent key is provided:

```json
{
  "success": false,
  "status": {
    "code": 201,
    "description": "Not found in database"
  }
}
```

#### errors

Standard errors


## update()

Set setting value. 

#### parameters

**key** - string. Length should be between 1 and 50 symbols. Should only contain English letters, digits, '_' and '-'.
**value** - string. Length should be between 0 and 8192 symbols. 

#### returns:

```json
{ "success": true }
```

#### errors
* Standard errors
* 268 - over quota. The amount of storage available for the user for these settings has been exhausted. New settings cannot be added until the amount of stored data has been reduced.
