---
title: Sub-user security group
description: Contains security group object structure and API calls related to security groups, that is, groups of sub-users with the specified set of rights
 and privileges.
---

# Subuser security group

Contains security group object structure and API calls related to security groups, that is, groups of sub-users with the specified set of rights and privileges.

<hr>

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

<hr>

### Default security group

Default (or empty) security group is the group which is effective when sub-users' `security_group_id` is null. 
It has empty `rights` array.

<hr>

### Master user's rights

Master user always has all rights, including exclusive "admin" right.

<hr>

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

<hr>

## API actions

API path: `/subuser/security_group/`.

### create

Creates new security group.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| group | `security_group` object without "id" field. | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/security_group/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "group": {"label": "Managers", "privileges": {"rights": ["tag_update", "tracker_register"], "store_period": "1d"}}}'
    ```

=== "template for API tools"

    ```
    {{ extra.api_example_url }}/subuser/security_group/create?hash=&group": {"label": "", "privileges": {"rights": ["", ""], "store_period": ""}}
    ```

#### response

```json
{
    "success": true,
    "id": 103
}
```

* `id` - int. An id of the created security group.

#### errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.

<hr>

### delete

Deletes existing security group.
All sub-users belonging to this group will be assigned to default (null) security group.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| security_group_id | Id of security group, which must be deleted. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/security_group/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "security_group_id": 103}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/security_group/delete?hash=&security_group_id=
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 13 – Operation not permitted – if user has insufficient rights.
* 201 – Not found in the database – when group with the specified security_group_id does not exist.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.

<hr>

### list

List all security groups belonging to current user.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/security_group/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/security_group/list?hash=
    ```

#### response

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

#### errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without `multilevel_access` tariff feature).

<hr>

### update

Updates existing security group.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| group | `security_group` with "id" field. | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/security_group/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "group": {"id": 103, "label": "Managers", "privileges": {"rights": ["tag_update", "tracker_register"], "store_period": "1d"}}}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/security_group/update?hash=&group": {"id": , "label": "", "privileges": {"rights": ["", ""], "store_period": ""}}
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 13 – Operation not permitted – if user has insufficient rights.
* 201 – Not found in the database – when security group with the specified id does not exist.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.

