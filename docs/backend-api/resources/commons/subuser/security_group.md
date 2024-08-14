---
title: Sub-user security group
description: Contains security group object structure and API calls related to security groups, that is, groups of sub-users with the specified set of rights
 and privileges.
---

# Subuser security group

Contains security group object structure and API calls related to security groups, that is, groups of sub-users with the specified set of rights and privileges.


## Security group object structure

```json
{
    "id": 103,
    "label": "Managers",
    "privileges": {
    "rights": ["tag_update", "tracker_register"],
    "store_period": "1d"
    }
}
```

* `id` - int. Group id, can be null (when creating new security group).
* `label` - string. Group label.
* `privileges` - object containing privileges of group.
    * `rights` - string array. A set of rights granted to security group (see below).
    * `store_period` - optional string. Period of viewing history in legacy duration format, e.g. "2h" (2 hours), 
    "3d" (3 days), "5m" (5 months), "1y" (one year).


### Default security group

Default (or empty) security group is the group which is effective when sub-users' `security_group_id` is null. 
It has empty `rights` array.


### Master user's rights

Master user always has all rights, including exclusive "admin" right.


### Security group rights

Absolute majority of read operations does not require any rights (that is, they are available to all sub-users, even 
with "null" security group). However, some entities may be hidden because they are associated with the trackers 
unavailable to sub-user.
Most of data-modifying operations, on the contrary, require some rights to be present.

Possible rights are:

* admin – master user-only. Can't be assigned to security groups,
* tracker_update,
* tracker_register,
* tracker_rule_update,
* tracker_configure,
* tracker_set_output,
* tag_update,
* task_update,
* zone_update,
* place_update,
* employee_update,
* vehicle_update,
* payment_create
* form_template_update,
* reports,
* checkin_update.


## API actions

API path: `/subuser/security_group/`.

### `create`

Creates new security group.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name  | description                                 | type        |
|:------|:--------------------------------------------|:------------|
| group | `security_group` object without "id" field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/security_group/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "group": {"label": "Managers", "privileges": {"rights": ["tag_update", "tracker_register"], "store_period": "1d"}}}'
    ```

#### Response

```json
{
    "success": true,
    "id": 103
}
```

* `id` - int. An ID of the created security group.

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.


### `delete`

Deletes existing security group.
All sub-users belonging to this group will be assigned to default (null) security group.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name              | description                                  | type |
|:------------------|:---------------------------------------------|:-----|
| security_group_id | ID of security group, which must be deleted. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/security_group/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 103}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/security_group/delete?hash=a6aa75587e5c59c32d347da438505fc3&id=103
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 201 – Not found in the database – when group with the specified security_group_id does not exist.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.


### `list`

List all security groups belonging to current user.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/security_group/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/security_group/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list": [{
         "id": 103,
         "label": "Managers",
         "privileges": {
         "rights": ["tag_update", "tracker_register"],
         "store_period": "1d"
         }
    }]
}
```

* `list` - array of objects. List of all security groups belonging to this master account.

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without `multilevel_access` tariff feature).


### `update`

Updates existing security group.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name  | description                       | type        |
|:------|:----------------------------------|:------------|
| group | `security_group` with "id" field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/security_group/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "group": {"id": 103, "label": "Managers", "privileges": {"rights": ["tag_update", "tracker_register"], "store_period": "1d"}}}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 201 – Not found in the database – when security group with the specified ID does not exist.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.


### `assign`

Assigns (removes) a security group to sub-users.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name        | description                      | type      |
|:------------|:---------------------------------|:----------|
| group_id    | Nullable, ID of a security group | int       |
| subuser_ids | IDs of sub-users                 | int array |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/security_group/assign' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "group_id": 3, subuser_ids: [12, 34]}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 201 – Not found in the database – when security group with the specified ID does not exist.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.
