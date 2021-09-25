---
title: User
description: API calls on work with users in the admin panel.
---

# User

API calls on work with users in the admin panel.

<hr>

## User object structure

```json
{ 
    "dealer_id": 5001,
    "activated": true,
    "verified": true,
    "login": "user@test.com",
    "first_name": "John",
    "middle_name": "William",
    "last_name": "Smith",
	"legal_name": "E. Biasi GmbH",
    "legal_type": "legal_entity",
    "phone": "491761234567",
    "post_country": "Germany",
    "post_index": "61169",
    "post_region": "Hessen",
    "post_city": "Wiesbaden", 
    "post_street_address": "Marienplatz 2",
    "registered_country": "Germany",
    "registered_index": "61169",
    "registered_region": "Hessen",
    "registered_city": "Wiesbaden",
    "registered_street_address": "Marienplatz 2",
    "state_reg_num": "12-3456789",
    "tin": "1131145180",
 	"okpo_code": "93281776",
    "iec": "773101001",
    "id": 38935,
    "balance" : 10.01,
    "bonus": 0,
    "creation_date" : "2021-03-01 13:00:00",
	"trackers_count": 10,
    "comment": "about user"
}
```

* `dealer_id` - int. Dealer ID.
* `activated` - boolean. `true` if user activated (allowed to login).
* `verified` - boolean. `true` if user's email verified.
* `login` - string. User email as login. Must be valid unique email address.
* `first_name` - string. Contact person first name.
* `middle_name` - string. Contact person middle name.
* `last_name` - string. Contact person last name.
* `legal_name` - string. User legal name (for "legal_entity" only).
* `legal_type` - [enum](../../backend-api/getting-started.md#data-types). Can be "legal_entity", "individual" or "sole_trader".
* `phone` - string. Contact phone 10-15 digits without "+" sign.
* `post_country` - string. Country part of user's post address.
* `post_index` - string. Index part of user's post address.
* `post_region` - string. Region part of user's post address.
* `post_city` - string. City from postal address.
* `post_street_address` - string. Street address.
* `registered_country` - string. Country part of user's registered address.
* `registered_index` - string. Index part of user's registered address.
* `registered_region` - string. Region part of user's registered address.
* `registered_city` - string. City from registered address.
* `registered_street_address` - string. User's registered address.
* `state_reg_num` - string. State registration number. E.g. EIN in USA, OGRN in Russia. 15 characters max.
* `tin` - string. Taxpayer identification number aka "VATIN".
* `okpo_code` - string, optional. All-Russian Classifier of Enterprises and Organizations, used in Russia for "legal_entity" or "sole_trader".
* `iec` - string, optional. Industrial Enterprises Classifier aka "KPP" (used in Russia. for "legal_entity" only).
* `id` - int. User id.
Next fields are read-only, they should not be used in `user/update` and `user/create`.
* `balance` - double. User balance.
* `bonus` - double. User bonus balance.
* `creation_date` - [date/time](../../backend-api/getting-started.md#data-types). Date and time when user created, in UTC.
* `trackers_count` - user trackers count.
* `comment` - comment about user (when creating and editing, the field must be separate from this object).

<hr>

## Discount object structure

```json
{
    "value": 5.5,
    "min_trackers": 10,
    "end_date": "2021-03-01",
    "strategy": "sum_with_progressive"
}
```

* `value` - double. Personal discount percent, min 0 max 100.
* `min_trackers` - int. Minimum active trackers to apply discount, min 0.
* `end_date` - [date/time](../../backend-api/getting-started.md#data-types). Discount end date, null means open date, nullable.
* `strategy` - [enum](../../backend-api/getting-started.md#data-types). One of "no_summing", "sum_with_progressive".\

<hr>

## API actions

API path: `panel/user`.

### change_password

Changes password of a user.

*required permissions*: `users: "update"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| user_id |	Id of a user. | int |
| password | User's new password, 6 to 20 printable characters. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}panel/user/change_password' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "user_id": 231432, "password": "12@14Y$"}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 201 – Not found in the database - if specified user does not exist or belongs to different dealer.

<hr>

### corrupt

Marks user and its sub users and trackers as deleted and corrupt all user trackers.


*required permissions*: `users: "corrupt"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| user_id | User id. | int |
| login | Login of a user. Login parameter must match user login. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}panel/user/corrupt' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "user_id": 231432, "login": "user@login.com"}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 201 – Not found in the database - if a user not found.
* 252 – Device already corrupted - if some of user's tracker already corrupted.
* 253 – Device has clones - if some of user's tracker has a clone.

```json
{
    "success": false,
    "status": {
        "code": 253,
        "description": "Device has clones"
    }
}
```

<hr>

### create

Creates a new user.

*required permissions*: `[users: "corrupt", "global"]`.

* `users: "global"` - Optional. Allows creating users of users, not only owned by a current dealer (use `user.dealer_id` parameter for other owners).

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| user | [User object](#user-object-structure) without the `id`, `dealer_id`, `comment` and read-only fields. | JSON object |
| time_zone |	User timezone. | string |
| locale | User locale. | string |
| password | User password, 6 to 20 printable characters. | string |
| discount | [Discount object](#discount-object-structure). | JSON object |
| default_tariff_id | Optional. ID of a default tariff plan for user's trackers |  int |
| `comment` |	Comment | String, max length 255, only printable characters |

If `user.verified` not passed then it set equal to `user.activated`.

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}panel/user/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "user": {"activated": true, "verified": true, "login": "user@test.com", "first_name": "John", "middle_name": "William", "last_name": "Smith", "legal_name": "E. Biasi GmbH", "legal_type": "legal_entity", "phone": "491761234567", "post_country": "Germany", "post_index": "61169", "post_region": "Hessen", "post_city": "Wiesbaden", "post_street_address": "Marienplatz 2", "registered_country": "Germany", "registered_index": "61169", "registered_region": "Hessen", "registered_city": "Wiesbaden", "registered_street_address": "Marienplatz 2", "state_reg_num": "12-3456789", "tin": "1131145180", "okpo_code": "93281776", "iec": "773101001"}, "time_zone": "Europe/Moscow", "locale": "en_US", "password": "12@14Y$", "discount": {"value": 5.5, "min_trackers": 10, "end_date": null, "strategy": "sum_with_progressive"}, "comment": "about user"}'
    ```

#### response

```json
{
    "success": true, 
    "id" : 15534
}
```

* `id` - int. An id of the created user.

#### errors

* 206 - Login already in use – if this email already registered.

<hr>

### export

Returns list of all users belonging to dealer as file.

If `filter` is used (parameter `filter` is passed, it isn't empty and does not consist only of space characters),
entities will be returned only if filter string is contained within one of the following fields:
`id`, `login`, `last_name`, `first_name`, `middle_name`, `phone`,
`post_city`, `post_region`, `post_country`, `post_index`, `post_street_address`,
`registered_country`, `registered_index`, `registered_region`, `registered_city`, `registered_street_address`,
`tin`, `iec`, `legal_name`.

*required permissions*: `users: "read"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| filter | Optional. Text filter string. | string |
| order_by | Optional. Specify list ordering. May be one of: `id`, `login`, `last_name`, `balance`, `bonus`, `phone`, `post_city`. Default is `id`. | string |
| ascending | Optional. If `true`, ordering will be ascending, descending otherwise. Default is `true`. | boolean |
| limit |  Optional. Max number of records to return, used for pagination. | int |
| offset | Optional. Starting offset, used for pagination. Default is `0`. | int |
| hide_inactive | Optional. If `true` only activated users will be returned. Default is `false`. |  boolean |
| format | Optional. Format of exported list. Can be `xlsx` or `csv`. Default is `xlsx`.  | string |
| columns | Optional. A list of columns to export. Default is `["id", "login", "first_name", "middle_name", "last_name", "phone"]`. | string array |

About user object structure see [above](#user-object-structure).

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/export' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/user/export?hash=fa7bf873fab9333144e171372a321b06
    ```

#### response

`XLSX` or `CSV` file download starts.

#### errors

* [Genreal](../../backend-api/getting-started.md#error-codes) types only.

<hr>

### list

Returns a list of all users belonging to dealer.

If `filter` is used (parameter `filter` is passed, it is not empty and does not consist only of space characters),
entities will be returned only if filter string is contained within one of the following fields:
`id`, `login`, `last_name`, `first_name`, `middle_name`, `phone`,
`post_city`, `post_region`, `post_country`, `post_index`, `post_street_address`,
`registered_country`, `registered_index`, `registered_region`, `registered_city`, `registered_street_address`,
`tin`, `iec`, `legal_name`.

*required permissions*: `users: "read"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| filter | Optional. Text filter string. | string |
| order_by | Optional. Specify list ordering. May be one of: `id`, `login`, `last_name`, `balance`, `bonus`, `phone`, `post_city`. Default is `id`. | string |
| ascending | Optional. If `true`, ordering will be ascending, descending otherwise. Default is `true`. | boolean |
| limit |  Optional. Max number of records to return, used for pagination. | int |
| offset | Optional. Starting offset, used for pagination. Default is `0`. | int |
| hide_inactive | Optional. If `true` only activated users will be returned. Default is `false`. |  boolean |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/user/list?hash=fa7bf873fab9333144e171372a321b06
    ```

#### response

```json
{
    "success": true,
    "list" : [{ 
      "dealer_id": 5001,
      "activated": true,
      "verified": true,
      "login": "user@test.com",
      "first_name": "John",
      "middle_name": "William",
      "last_name": "Smith",
      "legal_name": "E. Biasi GmbH",
      "legal_type": "legal_entity",
      "phone": "491761234567",
      "post_country": "Germany",
      "post_index": "61169",
      "post_region": "Hessen",
      "post_city": "Wiesbaden", 
      "post_street_address": "Marienplatz 2",
      "registered_country": "Germany",
      "registered_index": "61169",
      "registered_region": "Hessen",
      "registered_city": "Wiesbaden",
      "registered_street_address": "Marienplatz 2",
      "state_reg_num": "12-3456789",
      "tin": "1131145180",
      "okpo_code": "93281776",
      "iec": "773101001",
      "id": 38935,
      "balance" : 10.01,
      "bonus": 0,
      "creation_date" : "2021-03-01 13:00:00",
      "trackers_count": 10,
      "comment": "about user"
    }],
    "count" : 1
}
```

* `list` - array of JSON objects. A list of [user objects](#user-object-structure).
* `count` - int. Total number of records (ignoring offset and limit).

#### errors

* [Genreal](../../backend-api/getting-started.md#error-codes) types only.

<hr>

### read

Returns user info by its id.

*required permissions*: `users: "read"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| user_id | An id of a user to read. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "user_id": 231485}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/user/read?hash=fa7bf873fab9333144e171372a321b06&user_id=231485
    ```

#### response

```json
{
    "success": true,
    "value" : { 
        "dealer_id": 5001,
        "activated": true,
        "verified": true,
        "login": "user@test.com",
        "first_name": "John",
        "middle_name": "William",
        "last_name": "Smith",
        "legal_name": "E. Biasi GmbH",
        "legal_type": "legal_entity",
        "phone": "491761234567",
        "post_country": "Germany",
        "post_index": "61169",
        "post_region": "Hessen",
        "post_city": "Wiesbaden", 
        "post_street_address": "Marienplatz 2",
        "registered_country": "Germany",
        "registered_index": "61169",
        "registered_region": "Hessen",
        "registered_city": "Wiesbaden",
        "registered_street_address": "Marienplatz 2",
        "state_reg_num": "12-3456789",
        "tin": "1131145180",
        "okpo_code": "93281776",
        "iec": "773101001",
        "id": 38935,
        "balance" : 10.01,
        "bonus": 0,
        "creation_date" : "2021-03-01 13:00:00",
        "trackers_count": 10,
        "comment": "about user"
    },
    "discount": {
        "value": 5.5,
        "min_trackers": 10,
        "end_date": "2021-03-01",
        "strategy": "sum_with_progressive"
    },
    "default_tariff_id": 123
}
```

* `value` - JSON object. [User object](#user-object-structure) described above.
* `discount` - JSON object. [Discount object](#discount-object-structure) described above.
* `default_tariff_id` - integer number, nullable. ID of a tariff plan which will be applied to user's trackers by default.

#### errors

* 201 - Not found in the database – when user with specified id not found or belongs to other dealer.

<hr>

### update

Updates existing user with new field values (see [user object](#user-object-structure)). User must 
exist and must belong to authorized dealer. Changing of `legal_type` is not permitted, i.e. 
this field will not be changed.

*required permissions*: `users: "update"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| user | [User object](#user-object-structure) without `comment` and read-only fields. | JSON object |
| discount | [Discount object](#discount-object-structure). | JSON object |
| default_tariff_id | Optional. ID of a default tariff plan for user's trackers | int |
| `comment` | Comment | String, max length 255, only printable characters |

If `user.verified` not passed then it set equal to `user.activated`.

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}panel/user/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "user": {"dealer_id": 5001, "activated": true, "verified": true, "login": "user@test.com", "first_name": "John", "middle_name": "William", "last_name": "Smith", "legal_name": "E. Biasi GmbH", "legal_type": "legal_entity", "phone": "491761234567", "post_country": "Germany", "post_index": "61169", "post_region": "Hessen", "post_city": "Wiesbaden", "post_street_address": "Marienplatz 2", "registered_country": "Germany", "registered_index": "61169", "registered_region": "Hessen", "registered_city": "Wiesbaden", "registered_street_address": "Marienplatz 2", "state_reg_num": "12-3456789", "tin": "1131145180", "okpo_code": "93281776", "iec": "773101001", "id": 38935}, "discount": {"value": 5.5, "min_trackers": 10, "end_date": null, "strategy": "sum_with_progressive"}, "comment": "about user"}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 201 - Not found in the database – if specified user does not exist or belongs to different dealer.
* 206 - Login already in use – if specified "login" is used by another user.

<hr>

### session/create

Creates an interface session for specified user and returns the hash for the created session.

*required permissions*: `[users: "update", user_sessions: ["create", "global"]`.

user_sessions: "global" - Optional. Allows sessions of users creation, not only owned by a current dealer.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| user_id | An id of a user to create session. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/session/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "user_id": 231485}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/user/session/create?hash=fa7bf873fab9333144e171372a321b06&user_id=231485
    ```

#### response

```json
{
    "success": true,
    "hash" : "a2caa32267f028bd41b982980467132c"
}
```

* `hash` - string. Hash of the created session.

#### errors

* 201 - Not found in the database – if specified user does not exist or belongs to different dealer.

<hr>

### transaction/change_balance

Changes user balance (increase or decrease) or bonus and write this change in transactions (type = `payment`, subtype = `partner`).

New balance (bonus) must be not negative.

*required permissions*: `[users: "update", transactions: "create"]`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| user_id | An id of user whom balance changed. | int |
| amount | Amount to change. Can be negative. | double (2 digits after decimal mark) |
| type | Type of balance to change. Can be "balance" or "bonus". | [enum](../../backend-api/getting-started.md#data-types) |
| text | Description of transaction. | string (min length is 5 chars) |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/transaction/change_balance' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "user_id": 231485, "amount": 2.05, "type": "balance", "text": "additional payment"}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 201 – Not found in the database – if user not found or not owned by a current dealer.
* 251 – Insufficient funds (403) – if user have not enough funds to withdraw passed (negative) amount.

<hr>

### transaction/list

Gets list of user's billing transactions for the specified period. Same as [/transaction/list](../../backend-api/resources/billing/transaction.md#list) from main api.

*required permissions*: `[users: "read", transactions: "read"]`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| user_id | An id of user whom transactions listed. must be owned by a current dealer. | int |
| from | Start date/time for searching. | [date/time](../../backend-api/getting-started.md#data-types) |
| to | End date/time for searching. Must be after "from" date.  | [date/time](../../backend-api/getting-started.md#data-types) |
| limit | Optional. A maximum number of the returned transactions. | int |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/transaction/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "user_id": 231485, "from": "2020-02-03 03:04:00", "to": "2021-02-03 03:04:00"}'
    ```

#### response

```json
{
  "success": true, 
  "list": [{
    "description": "Recharge bonus balance during tracker registration",
    "type": "bonus_charge",
    "subtype": "register",
    "timestamp": "2021-01-28 08:16:40",
    "user_id": 12203,
    "dealer_id": 5001,
    "tracker_id": 303126,
    "amount": -10.0000,
    "new_balance": 800.0000,
    "old_balance": 810.0000,
    "bonus_amount": 10.0000,
    "new_bonus": 10.0000,
    "old_bonus": 0.0000
  }]
}
```

* `list` - array of objects. List of transaction objects.
    * `description` - string. Transaction description.
    * `type` - [enum](../../backend-api/getting-started.md#data-types). Type of transaction.
    * `subtype` - [enum](../../backend-api/getting-started.md#data-types). Subtype of transaction.
    * `timestamp` - [date/time](../../backend-api/getting-started.md#data-types). When transaction created.
    * `user_id` - int. ID of a user which made a transaction.
    * `dealer_id` - int. ID of a dealer.
    * `tracker_id` - int. Tracker id. 0 if transaction not associated with tracker.
    * `amount` - double. Amount of money in transaction, can be negative. e.g. -10.0000 means 10 money units removed from user`s balance.
    * `new_balance` - double. User`s money balance after transaction.
    * `old_balance` - double. User`s money balance before transaction.
    * `bonus_amount` - double. Amount of bonus used in transaction, can be negative. e.g. 10.0000 means 10 bonuses units added to user`s bonus balance.
    * `new_bonus` - double. User`s bonus balance after transaction.
    * `old_bonus` - double. User`s bonus balance before transaction.

#### errors

* 201 – Not found in the database - if user not found or not owned by a current dealer.

### upload

Upload users from CSV or XLS file.

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a CSV or XLS file upload (with the name "file").

CSV column separator is `;`. Columns header for CSV and XLS (headers with `*` is required):
 
`Email address*;Password*;Status*;Legal status*;Surname*;Name*;Middle name;Phone number;Сomment;Country;Region;City;Street, address;Zip code;Legal name;Tax number;IEC;Registration country;Registration region;Registration city;Registration address;Registration zip code;Discount;End date of discount;Device limit`

For RU locale:

`Адрес электронной почты*;Пароль*;Статус*;Юридический статус*;Фамилия*;Имя*;Отчество;Номер телефона;Комментарий;Страна;Регион;Город;Улица, дом, квартира;Почтовый индекс;Юридическое название;ИНН;КПП;ОГРН;ОКПО;Страна регистрации;Регион регистрации;Город регистрации;Улица, дом регистрации;Почтовый индекс регистрации;Скидка;Дата окончания скидки;Минимальное число устройств для скидки`

Legal status must be one of the following numbers:

 * 1 - individual
 * 2 - legal entity
 * 3 - sole trader

For legal entity (2) and sole trader (3) in addition to the required`*` the following columns must be present and filled with data:

`Country;Region;City;Street, address;Zip code;Legal name;Registration region;Registration city;Registration address;Registration zip code`

Except `Legal name` for sole trader (3) it is not required.

The remaining columns are optional and can be omitted. All columns can be in any order.

New users will be created with the time zone specified in `default_user_time_zone` service [setting](./dealer/settings/service.md).


*required permissions*: `[users: "create"]`.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| file | A XLS or CSV file containing users data. | File upload |
| redirect_target | Optional URL to redirect. If **redirect_target** passed return redirect to `<redirect_target>?response=<urlencoded_response_json>`. | string |


#### response

```json
{
  "success": true,
  "total": 1,
  "errors": 0
}
```

#### errors

Most error responses include `row_number` - the line number in the file where the error was found.

* 206 – Login already in use – if this email already registered.
```json
{
  "row_number" : 2,
  "status" : {
    "code" : 206,
    "description" : "Login already in use"
  },
  "success" : false
}
```
* 273 – Duplicate login in source file.
```json
{
  "row_number" : 4,
  "status" : {
    "code" : 273,
    "description" : "Duplicate login"
  },
  "success" : false
}
```
* 274 – Empty data file. No rows to load were found in the source file.
```json
{
  "status" : {
    "code" : 274,
    "description" : "Empty data file"
  },
  "success" : false
}
```
* 7 – Invalid parameters. Required columns not found or there has data validation errors.
```json
{
  "errors" : [ {
    "error" : "required column not found",
    "parameter" : "users_import.password"
  }, {
    "error" : "required column not found",
    "parameter" : "users_import.email"
  } ],
  "row_number" : 1,
  "status" : {
    "code" : 7,
    "description" : "Invalid parameters"
  },
  "success" : false
}
```
```json
{
  "errors" : [ {
    "error" : "E-mail must be valid",
    "parameter" : "user.login"
  } ],
  "row_number" : 2,
  "status" : {
    "code" : 7,
    "description" : "Invalid parameters"
  },
  "success" : false
}
```