---
title: Retranslator
description: Retranslator
---

# Retranslator

API path: `/retranslator`.

CRUD actions for retranslators.

#### objects
**retranslator_protocol** is: 
```json
{
    "id": <int>,                       // protocol ID
    "name": <string>,                  // protocol name
    "has_login": <boolean>,            // true if this protocol use login
    "has_password": <boolean>,         // true if this protocol use password
    "fake_device_id_pattern": <string>, // regex pattern for fake_device_id validation, optional
    "required_login": <boolean>,        // true if for this protocol login is required
    "required_password": <boolean>      // true if for this protocol password is required
}
```

**retranslator** is:
```json
{
    "id": <int>,          // retranslator ID, e.g. 1
    "name": <string>,     // zone label, e.g. "Some Wialon server"
    "protocol_id": <int>, // protocol ID
    "address": <string>,  // network address, e.g. "127.0.0.1 or localhost"
    "port": <int>,        // port, e.g. 15000
    "login": <string>,    // optional
    "password": <string>, // optional
    "enabled": <boolean>  // status
}
```


### create

Create new retranslator.

**required subuser rights**: admin (available only to master users)

#### parameters

name|description|type
---|---|---
retranslator|<retranslator> without "id" field|<retranslator>

#### response
```json
{
    "success": true,
    "id": <int> // ID of the created retranslator
}
```

#### errors

*   247 (Entity already exists) - if retranslator with this address, port and login already exists
*   7 (Invalid parameters) - if retranslator have required fields (login or password), but was send empty
*   268 (Over quota) – if the user's quota for retranslators is exceeded


### delete

Delete user's retranslator with ID = **retranslator_id**.

**required subuser rights**: admin (available only to master users)

#### parameters
*   retranslator_id

#### response
```json
{ "success": true }
```

#### errors
* 201 (Not found in database).



### list

Get all user's [retranslators](#objects).

#### response
```json
{
    "success": true,
    "list": [ <retranslator>, ... ]
}
```


### update

Update retranslator parameters for the specified retranslator. Note that retranslator must exist, must belong to the current user.

**required subuser rights**: admin (available only to master users)

#### parameters
*   `retranslator`

#### response
```json
{ "success": true }
```

#### errors

*   201 (Not found in database) – if retranslator with the specified ID cannot be found or belongs to another user.
*   247 (Entity already exists) – if retranslator with this address, port and login already exists.




### /retranslator/protocols/

### list
Return all available retranslator protocols.

#### response
```json
{
    "success": true,
    "list": [ <retranslator_protocol>, ... ]
}
```

