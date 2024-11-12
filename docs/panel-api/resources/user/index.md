---
title: User actions
description: API calls on work with users in the admin panel.
---

# User

In the Navixy Admin Panel, a User refers to the accounts of Organizations or Individuals who are customers of the Dealer (or Sub Dealer). For example, an organization 'ABC Inc.' can be a User with the type "legal_entity," and John Doe can be a User with the type "individual."

!!! note "User accounts may have additional sub-accounts, commonly referred to as 'sub-users,' allowing larger organizations to grant access to multiple employees."

This page describes the User object and the API actions that can be performed with it within the Admin Panel.

## User Object Structure

The User object structure defines the attributes and details of a user account within the Navixy platform, including personal information, contact details, legal identifiers, and account-specific data like balance.

```json
{ 
    "dealer_id": 5001,
    "activated": true,
    "verified": true,
    "login": "user@test.com",
    "first_name": "John",
    "middle_name": "William",
    "last_name": "Smith",
    "legal_name": "ABC Inc.",
    "legal_type": "legal_entity",
    "phone": "2135551234",
    "post_country": "United States",
    "post_index": "90001",
    "post_region": "California",
    "post_city": "Los Angeles", 
    "post_street_address": "1234 Sunset Blvd",
    "registered_country": "United States",
    "registered_index": "90001",
    "registered_region": "California",
    "registered_city": "Los Angeles",
    "registered_street_address": "1234 Sunset Blvd",
    "state_reg_num": "12-3456789",
    "tin": "1131145180",
    "okpo_code": "93281776",
    "iec": "773101001",
    "id": 38935,
    "balance": 10.01,
    "bonus": 0,
    "creation_date": "2021-03-01 13:00:00",
    "trackers_count": 10,
    "comment": "about user"
}
```

* `dealer_id` - int. Dealer ID.
* `activated` - boolean. `true` if the user is activated (allowed to log in).
* `verified` - boolean. `true` if the user's email is verified.
* `login` - string. User email used as a login. Must be a valid unique email address.
* `first_name` - string. Contact person's first name.
* `middle_name` - string. Contact person's middle name.
* `last_name` - string. Contact person's last name.
* `legal_name` - string. User's legal name (for "legal_entity" only).
* `legal_type` - [enum](../../../user-api/backend-api/getting-started/introduction.md#data-types). Can be "legal_entity", "individual", or "sole_trader".
* `phone` - string. Contact phone number with 10-15 digits, without the "+" sign.
* `post_country` - string. Country part of the user's postal address.
* `post_index` - string. Postal / ZIP code of the user's address.
* `post_region` - string. Region part of the user's postal address.
* `post_city` - string. City in the postal address.
* `post_street_address` - string. Street address.
* `registered_country` - string. Country part of the user's registered address.
* `registered_index` - string. Postal code of the user's registered address.
* `registered_region` - string. Region part of the user's registered address.
* `registered_city` - string. City in the registered address.
* `registered_street_address` - string. User's registered address.
* `state_reg_num` - string. State registration number. E.g., EIN in the USA. Max 15 characters.
* `tin` - string. Taxpayer Identification Number, also known as "VATIN".
* `okpo_code` - string, optional. Classifier of Enterprises and Organizations, used in some countries for "legal_entity" or "sole_trader".
* `iec` - string, optional. Industrial Enterprises Classifier, used in some countries, for "legal_entity".
* `id` - int. User ID.
  
Next fields are read-only and should not be used in `user/update` and `user/create`:

* `balance` - double. User balance.
* `bonus` - double. User bonus balance.
* `creation_date` - [date/time](../../../user-api/backend-api/getting-started/introduction.md#data-types). Date and time when the user was created, in UTC.
* `trackers_count` - int. Number of trackers associated with the user.
* `comment` - string. Comment about the user (when creating and editing, this field must be separate from this object).

## Discount Object Structure

The discount object structure defines a discount applied to a user's account based on specific conditions. It includes the discount percentage, the minimum number of active trackers required to apply the discount, the discount's end date, and the strategy for calculating the discount. This setup allows for flexible discount management, tailored to user activity and specified time frames.

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
* `end_date` - [date/time](../../../user-api/backend-api/getting-started/introduction.md#data-types). Discount end date, null means open date, nullable.
* `strategy` - [enum](../../../user-api/backend-api/getting-started/introduction.md#data-types). One of "no_summing", "sum_with_progressive".\


## API actions

API path: `panel/user`.

### `create`

Creates a new user.

*required permissions*: `[users: "corrupt", "global"]`.

* `users: "global"` - Optional. Allows creating users of users, not only owned by a current dealer (use `user.dealer_id` parameter for other owners).

#### Parameters

| name              | description                                                                                          | type                                              |
|:------------------|:-----------------------------------------------------------------------------------------------------|:--------------------------------------------------|
| user              | [User object](#user-object-structure) without the `id`, `dealer_id`, `comment` and read-only fields. | JSON object                                       |
| time_zone         | User timezone.                                                                                       | string                                            |
| locale            | User locale.                                                                                         | string                                            |
| password          | User password, 6 to 20 printable characters.                                                         | string                                            |
| discount          | [Discount object](#discount-object-structure).                                                       | JSON object                                       |
| default_tariff_id | Optional. ID of a default tariff plan for user's trackers                                            | int                                               |
| `comment`         | Comment                                                                                              | String, max length 255, only printable characters |

If `user.verified` not passed then it set equal to `user.activated`.

#### Example

```markdown
=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/create' \
        -H 'Content-Type: application/json' \
        -d '{
              "hash": "22eac1c27af4be7b9d04da2ce1af111b",
              "user": {
                "activated": true,
                "verified": true,
                "login": "user@test.com",
                "first_name": "John",
                "middle_name": "William",
                "last_name": "Smith",
                "legal_name": "ABC Inc.",
                "legal_type": "legal_entity",
                "phone": "2135551234",
                "post_country": "United States",
                "post_index": "90001",
                "post_region": "California",
                "post_city": "Los Angeles",
                "post_street_address": "123 Main Street",
                "registered_country": "United States",
                "registered_index": "90001",
                "registered_region": "California",
                "registered_city": "Los Angeles",
                "registered_street_address": "123 Main Street",
                "state_reg_num": "12-3456789",
                "tin": "1131145180",
                "okpo_code": "93281776",
                "iec": "773101001"
              },
              "time_zone": "America/Los_Angeles",
              "locale": "en_US",
              "password": "12@14Y$",
              "discount": {
                "value": 5.5,
                "min_trackers": 10,
                "end_date": null,
                "strategy": "sum_with_progressive"
              },
              "comment": "about user"
            }'
    ```
```
#### Response

```json
{
    "success": true, 
    "id" : 15534
}
```

* `id` - int. An ID of the created user.

#### Errors

* 206 - Login already in use – if this email already registered.


### `read`

Returns user info by its id.

*required permissions*: `users: "read"`.

#### Parameters

| name    | description              | type |
|:--------|:-------------------------|:-----|
| user_id | An ID of a user to read. | int  |

#### Examples

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

#### Response
```json
{
    "success": true,
    "value": { 
        "dealer_id": 5001,
        "activated": true,
        "verified": true,
        "login": "user@test.com",
        "first_name": "John",
        "middle_name": "William",
        "last_name": "Smith",
        "legal_name": "ABC Inc.",
        "legal_type": "legal_entity",
        "phone": "3231234567",
        "post_country": "USA",
        "post_index": "90001",
        "post_region": "California",
        "post_city": "Los Angeles", 
        "post_street_address": "123 Main St",
        "registered_country": "USA",
        "registered_index": "90001",
        "registered_region": "California",
        "registered_city": "Los Angeles",
        "registered_street_address": "123 Main St",
        "state_reg_num": "12-3456789",
        "tin": "1131145180",
        "okpo_code": "93281776",
        "iec": "773101001",
        "id": 38935,
        "balance": 10.01,
        "bonus": 0,
        "creation_date": "2021-03-01 13:00:00",
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

#### Errors

* 201 - Not found in the database – when user with specified ID not found or belongs to other dealer.


### `update`

Updates existing user with new field values (see [user object](#user-object-structure)). User must 
exist and must belong to authorized dealer. Changing of `legal_type` is not permitted, i.e. 
this field will not be changed.

*required permissions*: `users: "update"`.

#### Parameters

| name              | description                                                                   | type                                              |
|:------------------|:------------------------------------------------------------------------------|:--------------------------------------------------|
| user              | [User object](#user-object-structure) without `comment` and read-only fields. | JSON object                                       |
| discount          | [Discount object](#discount-object-structure).                                | JSON object                                       |
| default_tariff_id | Optional. ID of a default tariff plan for user's trackers                     | int                                               |
| `comment`         | Comment                                                                       | String, max length 255, only printable characters |

If `user.verified` not passed then it set equal to `user.activated`.

#### Example

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/panel/user/update' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "22eac1c27af4be7b9d04da2ce1af111b", 
        "user": {
            "dealer_id": 5001, 
            "activated": true, 
            "verified": true, 
            "login": "user@test.com", 
            "first_name": "John", 
            "middle_name": "William", 
            "last_name": "Smith", 
            "legal_name": "ABC Inc.", 
            "legal_type": "legal_entity", 
            "phone": "3231234567", 
            "post_country": "USA", 
            "post_index": "90001", 
            "post_region": "California", 
            "post_city": "Los Angeles", 
            "post_street_address": "123 Main St", 
            "registered_country": "USA", 
            "registered_index": "90001", 
            "registered_region": "California", 
            "registered_city": "Los Angeles", 
            "registered_street_address": "123 Main St", 
            "state_reg_num": "12-3456789", 
            "tin": "1131145180", 
            "okpo_code": "93281776", 
            "iec": "773101001", 
            "id": 38935
        }, 
        "discount": {
            "value": 5.5, 
            "min_trackers": 10, 
            "end_date": null, 
            "strategy": "sum_with_progressive"
        }, 
        "comment": "about user"
    }'
```
#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 - Not found in the database – if specified user does not exist or belongs to different dealer.
* 206 - Login already in use – if specified "login" is used by another user.




### `change_password`

Changes password of a user.

*required permissions*: `users: "update"`.

#### Parameters

| name     | description                                        | type   |
|:---------|:---------------------------------------------------|:-------|
| user_id  | ID of a user.                                      | int    |
| password | User's new password, 6 to 20 printable characters. | string |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/change_password' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "user_id": 231432, "password": "12@14Y$"}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if specified user does not exist or belongs to different dealer.


### `corrupt`

Marks user and its sub users and trackers as deleted and corrupt all user trackers.

*required permissions*: `users: "corrupt"`.

#### Parameters

| name           | description                                                                       | type    |
|:---------------|:----------------------------------------------------------------------------------|:--------|
| user_id        | User id.                                                                          | int     |
| login          | Login of a user. Login parameter must match user login.                           | string  |
| corrupt_clones | Optional. Default is `true`. Remove clones of the user's trackers for other users | boolean |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/corrupt' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "user_id": 231432, "login": "user@login.com"}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if a user not found.
* 252 – Device already corrupted - if some of user's tracker already corrupted.
* 253 – Device has clones - if some of user's tracker has a clone and `corrupt_clones` is false.

```json
{
    "success": false,
    "status": {
        "code": 253,
        "description": "Device has clones"
    }
}
```


### `upload`

Upload users from CSV or XLS file.

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being a CSV or XLS file upload (with the name "file").

CSV column separator is `;`. Columns header for CSV and XLS (headers with `*` is required):
 
`Email address*;Password*;Status*;Legal status*;Surname*;Name*;Middle name;Phone number;Comment;Country;Region;City;Street, address;Zip code;Legal name;Tax number;IEC;Registration country;Registration region;Registration city;Registration address;Registration zip code;Discount;End date of discount;Device limit`

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

New users will be created with the time zone specified in `default_user_time_zone` service [setting](../dealer/settings/service.md).


*required permissions*: `[users: "create"]`.

#### Parameters

| name            | description                                                                                                                         | type        | 
|:----------------|:------------------------------------------------------------------------------------------------------------------------------------|:------------|
| file            | A XLS or CSV file containing users data.                                                                                            | File upload |
| redirect_target | Optional URL to redirect. If **redirect_target** passed return redirect to `<redirect_target>?response=<urlencoded_response_json>`. | string      |


#### Response

```json
{
  "success": true,
  "total": 1,
  "errors": 0
}
```

#### Errors

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

### `list`

Returns a list of all users belonging to a dealer.

If the `filter` parameter is used (i.e., it is passed, it is not empty, and it does not consist solely of space characters), the response will include only those entities where the filter string matches any of the following fields:

`id`, `login`, `last_name`, `first_name`, `middle_name`, `phone`, `post_city`, `post_region`, `post_country`, 
`post_index`, `post_street_address`, `registered_country`, `registered_index`, `registered_region`, `registered_city`, 
`registered_street_address`, `tin`, `iec`, `legal_name`.

*Required permissions*: `users: "read"`.

#### Parameters

| name          | description                                                                                                                            | type    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|---------|
| filter        | Optional. Text filter string.                                                                                                          | string  |
| order_by      | Optional. Specify list ordering. May be one of: `id`, `login`, `last_name`, `balance`, `bonus`, `phone`, `post_city`. Default is `id`. | string  |
| ascending     | Optional. If `true`, ordering will be ascending; descending otherwise. Default is `true`.                                              | boolean |
| limit         | Optional. Max number of records to return, used for pagination.                                                                        | int     |
| offset        | Optional. Starting offset, used for pagination. Default is `0`.                                                                        | int     |
| hide_inactive | Optional. If `true`, only activated users will be returned. Default is `false`.                                                        | boolean |
#### Examples

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

#### Response

```json
{
    "success": true,
    "list": [{
        "dealer_id": 5001,
        "activated": true,
        "verified": true,
        "login": "user@test.com",
        "first_name": "John",
        "middle_name": "William",
        "last_name": "Smith",
        "legal_name": "ABC Inc.",
        "legal_type": "legal_entity",
        "phone": "3231234567",
        "post_country": "USA",
        "post_index": "90001",
        "post_region": "California",
        "post_city": "Los Angeles",
        "post_street_address": "123 Main St",
        "registered_country": "USA",
        "registered_index": "90001",
        "registered_region": "California",
        "registered_city": "Los Angeles",
        "registered_street_address": "123 Main St",
        "state_reg_num": "12-3456789",
        "tin": "1131145180",
        "okpo_code": "93281776",
        "iec": "773101001",
        "id": 38935,
        "balance": 10.01,
        "bonus": 0,
        "creation_date": "2021-03-01 13:00:00",
        "trackers_count": 10,
        "comment": "about user"
    }],
    "count": 1
}
```

* `list` - array of JSON objects. A list of [user objects](#user-object-structure).
* `count` - int. Total number of records (ignoring offset and limit).

#### Errors

* [General](../../../user-api/backend-api/getting-started/errors.md#error-codes) types only.



### `export`

This API call returns a file containing a list of all users belonging to a Dealer.

If the `filter` parameter is used (i.e., it is passed, it is not empty, and it does not consist solely of space characters), the response will include only those entities where the filter string matches any of the following fields:

`id`, `login`, `last_name`, `first_name`, `middle_name`, `phone`, `post_city`, `post_region`, `post_country`, `post_index`, 
`post_street_address`, `registered_country`, `registered_index`, `registered_region`, `registered_city`, `registered_street_address`, 
`tin`, `iec`, `legal_name`.

*Required permissions*: `users: "read"`.

#### Parameters

| name          | description                                                                                                                            | type         |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| filter        | Optional. Text filter string.                                                                                                          | string       |
| order_by      | Optional. Specify list ordering. May be one of: `id`, `login`, `last_name`, `balance`, `bonus`, `phone`, `post_city`. Default is `id`. | string       |
| ascending     | Optional. If `true`, ordering will be ascending, descending otherwise. Default is `true`.                                              | boolean      |
| limit         | Optional. Max number of records to return, used for pagination.                                                                        | int          |
| offset        | Optional. Starting offset, used for pagination. Default is `0`.                                                                        | int          |
| hide_inactive | Optional. If `true` only activated users will be returned. Default is `false`.                                                         | boolean      |
| format        | Optional. Format of exported list. Can be `xlsx` or `csv`. Default is `xlsx`.                                                          | string       |
| columns       | Optional. A list of columns to export. Default is `["id", "login", "first_name", "middle_name", "last_name", "phone"]`.                | string array |

About user object structure see [above](#user-object-structure).

#### Examples

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

#### Response

`XLSX` or `CSV` file download starts.

#### Errors

* [General](../../../user-api/backend-api/getting-started/errors.md#error-codes) types only.


### `session/create`

Creates an interface session for specified user and returns the hash for the created session.

*required permissions*: `[users: "update", user_sessions: ["create", "global"]`.

user_sessions: "global" - Optional. Allows sessions of users creation, not only owned by a current dealer.

#### Parameters

| name    | description                        | type |
|:--------|:-----------------------------------|:-----|
| user_id | An ID of a user to create session. | int  |

#### Examples

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

#### Response

```json
{
    "success": true,
    "hash" : "a2caa32267f028bd41b982980467132c"
}
```

* `hash` - string. Hash of the created session.

#### Errors

* 201 - Not found in the database – if specified user does not exist or belongs to different dealer.


### `transaction/list`

Gets list of user's billing transactions for the specified period. Same as [/transaction/list](../../../user-api/backend-api/resources/billing/transaction.md#list) from main api.

*required permissions*: `[users: "read", transactions: "read"]`.

#### Parameters

| name    | description                                                                | type                                                         |
|:--------|:---------------------------------------------------------------------------|:-------------------------------------------------------------|
| user_id | An ID of user whom transactions listed. must be owned by a current dealer. | int                                                          |
| from    | Start date/time for searching.                                             | [date/time](../../../user-api/backend-api/getting-started/introduction.md#data-types) |
| to      | End date/time for searching. Must be after "from" date.                    | [date/time](../../../user-api/backend-api/getting-started/introduction.md#data-types) |
| limit   | Optional. A maximum number of the returned transactions.                   | int                                                          |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/transaction/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "user_id": 231485, "from": "2020-02-03 03:04:00", "to": "2021-02-03 03:04:00"}'
    ```

#### Response

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
    * `type` - [enum](../../../user-api/backend-api/getting-started/introduction.md#data-types). Type of transaction.
    * `subtype` - [enum](../../../user-api/backend-api/getting-started/introduction.md#data-types). Subtype of transaction.
    * `timestamp` - [date/time](../../../user-api/backend-api/getting-started/introduction.md#data-types). When transaction created.
    * `user_id` - int. ID of a user which made a transaction.
    * `dealer_id` - int. ID of a dealer.
    * `tracker_id` - int. Tracker id. 0 if transaction not associated with tracker.
    * `amount` - double. Amount of money in transaction, can be negative. e.g. -10.0000 means 10 money units removed from user's balance.
    * `new_balance` - double. User's money balance after transaction.
    * `old_balance` - double. User's money balance before transaction.
    * `bonus_amount` - double. Amount of bonus used in transaction, can be negative. e.g. 10.0000 means 10 bonuses units added to user's bonus balance.
    * `new_bonus` - double. User's bonus balance after transaction.
    * `old_bonus` - double. User's bonus balance before transaction.

#### Errors

* 201 – Not found in the database - if user not found or not owned by a current dealer.

### `transaction/change_balance`

Changes user balance (increase or decrease) or bonus and write this change in transactions (type = `payment`, subtype = `partner`).

New balance (bonus) must be not negative.

*required permissions*: `[users: "update", transactions: "create"]`.

#### Parameters

| name    | description                                             | type                                                                             |
|:--------|:--------------------------------------------------------|:---------------------------------------------------------------------------------|
| user_id | An ID of user whom balance changed.                     | int                                                                              |
| amount  | Amount to change. Can be negative.                      | double (2 digits after decimal mark)                                             |
| type    | Type of balance to change. Can be "balance" or "bonus". | [enum](../../../user-api/backend-api/getting-started/introduction.md#data-types) |
| text    | Description of transaction.                             | string (min length is 5 chars)                                                   |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/transaction/change_balance' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "user_id": 231485, "amount": 2.05, "type": "balance", "text": "additional payment"}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database – if user not found or not owned by a current dealer.
* 251 – Insufficient funds (403) – if user have not enough funds to withdraw passed (negative) amount.


