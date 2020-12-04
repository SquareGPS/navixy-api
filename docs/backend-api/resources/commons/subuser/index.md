---
title: Subuser
description: Subuser
---

# Subuser

API path: `/subuser`.

Contains API calls related to sub-users, that is, additional users who have access to your account and monitoring assets. Sub-users is convenient way for corporate clients to provide multiple employees, who have different roles and priveleges, with access to the monitoring system.

"Usual" user account is called "master account" in relation to sub-users.

Every sub-user can operate on a subset of trackers from your "master account". Every entity, which is associated with unavailable trackers, also becomes hidden from sub-user. This is called "scoping".
Sub-users's rights can also be limited to prevent unauthorized changes to your data and application setting.

NOTE: Sub-users cannot have any "exclusive" objects. Every tracker, rule, task, etc., even created or edited by sub-user, still belongs to your account.
The only exception is reporting system: every sub-user has its own reports pool and reports schedule.

# Sub-user object structure

Sub-user object is almost identical to usual user.
```javascript
<subuser> = {
      "id": 103, //sunuser id, can be null (when creating new sub-user)
      "activated": true,                // true if user is activated (allowed to login)
      "login": "user@test.com",         // User email as login. Must be valid unique email address
      "first_name": ${string},          // User's or contact person first name
      "middle_name": ${string},         // User's or contact person middle name
      "last_name": ${string},           // User's or contact person last name
      "legal_type": "legal_entity",     // either "legal_entity", "individual" or "sole_trader"
      "phone": "491761234567",          // User's or contact phone (10-15 digits)
      "post_country": "Germany",        // country part of user's post address
      "post_index": "61169",            // index part of user's post address
      "post_region": "Hessen",          // region part of user's post address
      "post_city": "Wiesbaden",         // city from postal address
      "post_street_address": "Marienplatz 2", // street address
      "registered_country": "Germany",  // country part of user's registered address
      "registered_index": "61169",      // index part of user's registered address
      "registered_region": "Hessen",    // region part of user's registered address
      "registered_city": "Wiesbaden",   // city from registered address
      "registered_street_address": "Marienplatz 2", // User's registered address
      "state_reg_num": ${string},       // State registration number. E.g. EIN in USA, OGRN in Russia. 15 characters max.
      "tin": ${string},                 // Taxpayer identification number aka "VATIN"
      "legal_name": "E. Biasi GmbH",    // user legal name (for "legal_entity" only)
      "iec": ${string},                 // Industrial Enterprises Classifier aka "KPP" (used in Russia. for "legal_entity" only)
      "security_group_id": 333,         // Id of the security group to whic sub-user belongs to. Can be null, which means default group with no privileges
      //this fields are read-only, they should not be used in user/update
      "creation_date": "2016-05-20 00:00:00" // date/time when user was created
    }
```

### delete

Delete sub-user. This operation cannot be reversed.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters
* **subuser_id** - **int**. id of the sub-user belonging to current account

#### response

```json
{
    "success": true
}
```

#### errors
*   13 – Operation not permitted – if user has insufficient rights
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without "multilevel_access" tariff feature)
*   201 – Not found in database – if sub-user with such id does not exist or does not belong to current master user.

### list

List all subusers belonging to current user.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters

none

#### response

```json
{
    "success": true,
    "list": [<subuser>, ... ] //list of all sub-users belonging to this master account
}
```

Subuser object is described [here](#sub-user-object-structure).

#### errors

*   13 – Operation not permitted – if user has insufficient rights
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without "multilevel_access" tariff feature)

### register

Allows you to create sub-users associated to your master account.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters

* **user** - **JSON object**. <subuser> object without "id" field
* **password** - **printable string**. 6 to 20 characters. New sub-user's password.

#### response

```json
{
    "success": true,
    "id": <id of the created sub-user>
}
```

Subuser object is described [here](#sub-user-object-structure).

#### errors
*   13 – Operation not permitted – if user has insufficient rights
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without "multilevel_access" tariff feature)
*   201 – Not found in database – when specified security_group_id does not exist
*   206 – login already in use (if this login email already registered)

### update

Update subuser data.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters
* **user** - **JSON object**. <subuser> object with "id" field

#### response

```json
{
    "success": true
}
```

Subuser object is described [here](#sub-user-object-structure).

#### errors
*   13 – Operation not permitted – if user has insufficient rights
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without "multilevel_access" tariff feature)
*   201 – Not found in database – if sub-user with such id does not exist or does not belong to current master user. Also when specified security_group_id does not exist

