---
title: Subuser
description: API calls related to sub-users, that is, additional users who have access to your account and monitoring assets.
              Sub-users is a convenient way for corporate clients to provide multiple employees, who have different roles and privileges,
              with access to the monitoring system.
---

# Subuser

Contains API calls related to sub-users, that is, additional users who have access to your account and monitoring assets.
 Sub-users is a convenient way for corporate clients to provide multiple employees, who have different roles and privileges,
 with access to the monitoring system.

"Usual" user account called "master account" in relation to sub-users.

Every sub-user can operate on a subset of trackers from your "master account". Every entity, which is associated with
 unavailable trackers, also becomes hidden from sub-user. This is called "scoping".
Sub-users' rights can also be limited to prevent unauthorized changes to your data and application setting.

NOTE: Sub-users cannot have any "exclusive" objects. Every tracker, rule, task, etc., even created or edited by sub-user,
 still belongs to your account.
The only exception is reporting system: every sub-user has its own reports pool and reports schedule.


## Sub-user object structure

Sub-user object is almost identical to usual user.

```json
{
      "id": 103,
      "activated": true,
      "login": "user@test.com",
      "first_name": "Charles",
      "middle_name": "Henry",
      "last_name": "Pearson",
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
      "legal_name": "E. Biasi GmbH",
      "iec": "",
      "security_group_id": 333,
      "creation_date": "2016-05-20 00:00:00"
    }
```

* `id` - int. Sub-user's ID, can be null (when creating new sub-user).
* `activated` - boolean. `true` if sub-user activated (allowed to log in).
* `login` - string. Sub-user email as login. Must be valid unique email address.
* `first_name` - string. Sub-user's or contact person first name.
* `middle_name` - string. Sub-user's or contact person middle name.
* `last_name` - string. Sub-user's or contact person last name.
* `legal_type` - [enum](../../../getting-started/introduction.md#data-types). Can bed "legal_entity", "individual" or "sole_trader".
* `phone` - string. Sub-user's or contact phone (10-15 digits).
* `post_country` - string. Country part of sub-user's post address.
* `post_index` - string. Index part of sub-user's post address.
* `post_region` - string. Region part of sub-user's post address.
* `post_city` - string. City from postal address.
* `post_street_address` - string. Street address.
* `registered_country` - string. Country part of sub-user's registered address.
* `registered_index` - string. Index part of sub-user's registered address.
* `registered_region` - string. Region part of sub-user's registered address.
* `registered_city` - string. City from registered address.
* `registered_street_address` - string. Sub-user's registered address.
* `state_reg_num` - string. State registration number. E.g. EIN in the USA, OGRN in Russia. 15 characters max.
* `tin` - string. Taxpayer identification number aka "VATIN" or "INN".
* `legal_name` - string. Sub-user's legal name (for "legal_entity" only).
* `iec` - optional string. Industrial Enterprises Classifier aka "KPP" (used in Russia. For "legal_entity" only).
* `security_group_id` - int. An ID of the security group to which sub-user belongs to. Can be null, which means default 
group with no privileges.
* `creation_date` - [date/time](../../../getting-started/introduction.md#data-types). Date and time when sub-user was created. This field is read-only, it should not be
 used in subuser/update.


## API actions

API path: `/subuser`.

### `delete`

Deletes sub-user. This operation cannot be reversed.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name       | description                                      | type |
|:-----------|:-------------------------------------------------|:-----|
| subuser_id | ID of the sub-user belonging to current account. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "subuser_id": 123567}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/delete?hash=a6aa75587e5c59c32d347da438505fc3&subuser_id=123567
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.
* 201 – Not found in the database – if sub-user with such an ID does not exist or does not belong to current master user.


### `list`

List all sub-users belonging to current user.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list": [{
       "id": 103,
       "activated": true,
       "login": "user@test.com",
       "first_name": "Charles",
       "middle_name": "Henry",
       "last_name": "Pearson",
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
       "legal_name": "E. Biasi GmbH",
       "iec": "",
       "security_group_id": 333,
       "creation_date": "2016-05-20 00:00:00"
    }]
}
```

* `list` -  array of objects. List of all sub-users belonging to this master account.

Sub-user object described [here](#sub-user-object-structure).

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.


### `register`

Allows you to create sub-users associated to your master account.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name     | description                                  | type        |
|:---------|:---------------------------------------------|:------------|
| user     | `subuser object` without `id` field.         | JSON object |
| password | New sub-user's password. 6 to 20 characters. | string      |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/register' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "password": 123456, "user": {"activated": true, "login": "user@test.com", "first_name": "Charles", "middle_name": "Henry", "last_name": "Pearson", "legal_type": "legal_entity", "phone": "491761234567", "post_country": "Germany", "post_index": "61169", "post_region": "Hessen", "post_city": "Wiesbaden", "post_street_address": "Marienplatz 2", "registered_country": "Germany", "registered_index": "61169", "registered_region": "Hessen", "registered_city": "Wiesbaden", "registered_street_address": "Marienplatz 2", "state_reg_num": "12-3456789", "tin": "1131145180", "legal_name": "E. Biasi GmbH", "iec": "", "security_group_id": 333}}'
    ```

#### Response

```json
{
    "success": true,
    "id": 121458
}
```

* `id` - int. An ID of the created sub-user.

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.
* 201 – Not found in the database – when specified security_group_id does not exist.
* 206 – login already in use - if this login email already registered.


### `update`

Updates sub-user data.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name | description                       | type        |
|:-----|:----------------------------------|:------------|
| user | `subuser object` with `id` field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "user": {"id": 123451, "activated": true, "login": "user@test.com", "first_name": "Charles", "middle_name": "Henry", "last_name": "Pearson", "legal_type": "legal_entity", "phone": "491761234567", "post_country": "Germany", "post_index": "61169", "post_region": "Hessen", "post_city": "Wiesbaden", "post_street_address": "Marienplatz 2", "registered_country": "Germany", "registered_index": "61169", "registered_region": "Hessen", "registered_city": "Wiesbaden", "registered_street_address": "Marienplatz 2", "state_reg_num": "12-3456789", "tin": "1131145180", "legal_name": "E. Biasi GmbH", "iec": "", "security_group_id": 333}}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.
* 201 – Not found in the database – if sub-user with such an ID does not exist or does not belong to current master user.
 Also, when specified `security_group_id` does not exist.

