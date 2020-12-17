---
title: /user
description: /user
---


# Data structures
 
** User object structure **
```json
{ 
    "dealer_id": 5001,                // dealer id
    "activated": true,                // true if user is activated (allowed to login)
    "verified": true,                 // true if user's email is verified
    "login": "user@test.com",         // User email as login. Must be valid unique email address
    "first_name": ${string},          // Contact person first name
    "middle_name": ${string},         // Contact person middle name
    "last_name": ${string},           // Contact person last name
	"legal_name": "E. Biasi GmbH",    // user legal name (for "legal_entity" only)
    "legal_type": "legal_entity",     // either "legal_entity", "individual" or "sole_trader"
    "phone": "491761234567",          // Contact phone (10-15 digits)
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
 	"okpo_code": ${string},           // All-Russian Classifier of Enterprises and Organizations, used in Russia for "legal_entity" / "sole_trader"
    "iec": ${string},                 // Industrial Enterprises Classifier aka "KPP" (used in Russia. for "legal_entity" only)
    "id": 38935,                      // user id
    //this fields are read-only, they should not be used in user/update(..)
    "balance" : 10.01,                // user balance
    "bonus": 0,                       // user bonus balance
    "creation_date" : "2014-03-01 13:00:00", // date/time when user was created, in UTC
	"trackers_count": 10 //user trackers count
}
```

** Discount object structure **

```json
{
    "value": 5.5, //personal discount percent, min 0 max 100
    "min_trackers": 10, //min active trackers to apply discount, min 0
    "end_date": "2017-03-01", //discount end date, null means open date, nullable
    "strategy": "sum_with_progressive" // one of no_summing, sum_with_progressive
  }
```
  
## change_password

`change_password(user_id, password)`

Change password of the user.

** Parameters **

| Name | Description  | Type |
| --- | --- | --- |
| user_id |	id of the user | Int |
| password |	User password, 6 to 20 printable characters | String |

** Required permissions **

* `users: "update"`

** Return **

```json
{ "success": true }
```

** Errors **

* 201 – Not found in database (if specified user does not exist or belongs to different dealer)
* [Standard errors](../../backend-api/getting-started.md#error-codes)

## corrupt

`corrupt(user_id, login)`

Mark user and its sub users and trackers as deleted and corrupt all user trackers.
login parameter must match user login.

** Required permissions **

* `users: "corrupt"`

** Return **

* `{"success": true}`

** Errors **

* 201 – Not found in database (if user was not found)
* 252 – Device already corrupted (if some of user tracker already corrupted)
* 253 – Device has clones (if some of user tracker has clone)

```json
{
    "success": false,
    "status": {
        "code": 253,
        "description": "Device has clones"
    }
}
```

## create

** Required permissions **

```json
users: "create"
users: "global" // optional. allow to create users of users, not only owned 
                // by current dealer (use user.dealer_id parameter for other owners).
```

** Parameters **

| Name | Description  | Type |
| --- | --- | --- |
| `user` |	user object without the "id" and "dealer_id" fields	| JSON object |
| `time_zone` |	User timezone (e.g. "Europe/Moscow" ) | String |
| `locale` |	User locale (e.g. "en_US") | String |
| `password` |	User password, 6 to 20 printable characters | String |
| `discount` |	discount object | JSON object |

If `user.verified` not passed then it set equal to `user.activated`.

** Return **

```json
{
    "success": true, 
    "id" : 15534 // id of the created user
}
```

** Errors **

* 206 (Login already in use) – if this email already registered
* [Standard errors](../../backend-api/getting-started.md#error-codes)

## export

Returns list of all users belonging to dealer as file.

If `filter` is used (parameter `filter` is passed, it is not empty and do not consist only of space characters),
entities will be returned only if filter string is contained within one of the following fields:
`id`, `login`, `last_name`, `first_name`, `middle_name`, `phone`,
`post_city`, `post_region`, `post_country`, `post_index`, `post_street_address`,
`registered_country`, `registered_index`, `registered_region`, `registered_city`, `registered_street_address`,
`tin`, `iec`, `legal_name`.

** Required permissions **

* `users: "read"`

** Parameters **

| Name | Description  | Type |
| --- | --- | --- |
| `filter` | Text filter string | string, optional |
| `order_by` | Specify list ordering. May be one of: id, login, last_name, balance, bonus, phone, post_city | string, optional (default: id) |
| `ascending` | If true, ordering will be ascending, descending otherwise. | boolean, optional (default: true) |
| `limit` |  Max number of records to return, used for pagination. | int, optional |
| `offset` | Starting offset, used for pagination | int, optional (default: 0) |
| `hide_inactive` | If true only activated users will be returned |  boolean, optional (default: false) |
| `format` | xlsx or csv | string, optional (default: xlsx) |
| `columns` | list of columns to export | array of string, (default: ["id", "login", "first_name", "middle_name", "last_name", "phone"]) |

About user object structure see [above](#data-structures).

** Return **

XLSX or CSV file

** Errors **

* Only [standard errors](../../backend-api/getting-started.md#error-codes)


# list

Returns list of all users belonging to dealer.

If `filter` is used (parameter `filter` is passed, it is not empty and do not consist only of space characters),
entities will be returned only if filter string is contained within one of the following fields:
`id`, `login`, `last_name`, `first_name`, `middle_name`, `phone`,
`post_city`, `post_region`, `post_country`, `post_index`, `post_street_address`,
`registered_country`, `registered_index`, `registered_region`, `registered_city`, `registered_street_address`,
`tin`, `iec`, `legal_name`.

** Required permissions **

* `users: "read"`

** Parameters **

| Name | Description  | Type |
| --- | --- | --- |
| `filter` | Text filter string | string, optional |
| `order_by` | Specify list ordering. May be one of: id, login, last_name, balance, bonus, phone, post_city | string, optional (default: id) |
| `ascending` | If true, ordering will be ascending, descending otherwise. | boolean, optional (default: true) |
| `limit` |  Max number of records to return, used for pagination. | int, optional |
| `offset` | Starting offset, used for pagination | int, optional (default: 0) |
| `hide_inactive` | If true only activated users will be returned |  boolean, optional (default: false) |

** Return **

```json
{
    "success": true,
    "list" : [ ${user} , ... ], // list of JSON-objects
    "count" : 42 // total number of records (ignoring offset and limit)
}
```

About user object structure see [above](#data-structures).

** Errors **

* Only [standard errors](../../backend-api/getting-started.md#error-codes)

## read

Returns user info by it's id.

** Required permissions **

* `users: "read"`

** Parameters **

| Name | Description  | Type |
| --- | --- | --- |
| `user_id` | | int |

** Return **

```json
{
    "success": true,
    "value" : ${user},
    "discount": ${discount}
}
```

About user object structure see [above](#data-structures).

** Errors **

* 201 (Not found in database) – when user with specified id not found or belongs to other dealer.
* [Standard errors](../../backend-api/getting-started.md#error-codes)

## update

Updates existing user with new field values (see user [above](#data-structures)). User must 
exist and must belong to authorized dealer. Changing of legal_type do not permitted, i.e. 
this field will not be changed.

** Required permissions **

* `users: "update"`

** Parameters **

| Name | Description  | Type |
| --- | --- | --- |
| user | user |  JSON object
| discount | discount |  JSON object

About user and discount object structure see [above](#data-structures).

If `user.verified` not passed then it set equal to `user.activated`.

** Return **

```json
{ "success": true }
```

** Errors **

* 201 (Not found in database) – if specified user does not exist or belongs to different dealer.
* 206 (Login already in use) – if specified "login" is used by another user.
* [Standard errors](../../backend-api/getting-started.md#error-codes).

## session/

### create

Creates an interface session for specified user and returns the hash for the created session.

** Required permissions **

```
users: "read"
user_sessions: "create"
user_sessions: "global" // optional. allow to create sessions of users, not only owned by current dealer.
```

** Parameters **

| Name | Description  | Type |
| --- | --- | --- |
| `user_id` | ID of monitoring user | int |

** Return **

```json
{
    "success": true,
    "hash" : "a2caa32267f028bd41b982980467132c" // hash of the created session
}
```

** Errors **

* 201 (Not found in database) – if specified user does not exist or belongs to different dealer.
* [Standard errors](../../backend-api/getting-started.md#error-codes).

## transaction/

### change_balance

Change user balance (increase or decrease) or bonus and write this change in transactions (type = payment, subtype = partner).

New balance (bonus) must be not negative.

** Required permissions **

```
users: "update"
transactions: "create"
```

** Parameters **

| Name | Description  | Type |
| --- | --- | --- |
| user_id | id of user whom balance changed | int |
| amount | add it to passed type of balance | double (2 digits after decimal mark) |
| type | Type of balance to change ("balance" or "bonus") | string |
| text | description of transaction | string(min length is 5 chars) |

** Return **

```json
{ "success": true }
```

** Errors **

* 201 – Not found in database – If user not found or not owned by current dealer.
* 251 – Insufficient funds(403) – If user have not enough funds to withdraw passed (negative) amount.
* [Standard errors](../../backend-api/getting-started.md#error-codes).

### list

Same as [/transaction/list](../../backend-api/resources/billing/transaction.md#list) from main api.

** Required permissions **

```
users: "read"
transactions: "read"
```

** Parameters **

| Name | Description  | Type |
| --- | --- | --- |
| `user_id` | id of user whom transactions listed. must be owned by current dealer | int
| `from` | start date/time for searching | date/time
| `to` | end date/time for searching. must be after "from" date  | date/time
| `limit` | maxumum number of returned transactions (optional) | int

** Return **

```json
{
  "success": true, 
  "list": [
     {
        "description": ,  // transaction description, e.g. "Recharge bonus balance during tracker registration"
        "type": ,         // type, e.g. "bonus_charge"
        "subtype": ,      // subtype, e.g. "register"
        "timestamp": , // date/time at which transaction was created, e.g. "2013-08-02 08:16:40"
        "user_id": ,         // user Id, e.g. 12203
        "dealer_id": ,       // dealer Id, e.g. 5001
        "tracker_id": ,      // tracker id, e.g., 3036, or 0 if transaction is not associated with tracker
        "amount": ,       // amount of money in transaction, can be negative. e.g. -10.0000 means 10 money units were removed from user`s balance
        "new_balance": ,  // user`s money balance after transaction, e.g. 800.0000
        "old_balance": ,  // user`s money balance before transaction, e.g. 810.0000
        "bonus_amount": , // amount of bonus used in transaction, can be negative. e.g. 10.0000 means 10 bonuses units were added to user`s bonus balance
        "new_bonus": ,    // user`s bonus balance after transaction, e.g. 10.0000
        "old_bonus":      // user`s bonus balance before transaction, e.g. 0.0000
     }, ...
  ]
}
```

** Errors **

* 201 – Not found in database (if user not found or not owned by current dealer)
* [Standard errors](../../backend-api/getting-started.md#error-codes).
