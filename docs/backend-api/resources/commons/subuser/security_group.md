---
title: Subuser security group
description: Subuser security group
---

# Subuser security group

API path: `/subuser/security_group/`.

Contains API calls related to security groups, that is, groups of sub-users with the specified set of rights and privileges.

### Security group object structure

```json5
${security_group} = {
      "id": 103, //group id, can be null (when creating new security group)
      "label": "Managers", //group label
      "privileges": {
        "rights": [
          "tag_update", "tracker_register" //a set of rights granted to security group (see below)
        ],
        "store_period": "1d" // optional, period of viewing history in legacy duration format, e.g. "2h" (2 hours), "3d" (3 days), "5m" (5 months), "1y" (one year)
      }
    }
```

### Default security group

Default (or empty) security group is the group which is effective when sub-users’ “security_group_id” is null. It has empty “rights” array.

### Master user’s rights

Master user always has all rights, including exclusive “admin” right.

### Security group rights

Absolute majority of read operations does not require any rights (that is, they are available to all sub-users, even with “null” security group). However, some entities may be hidden because they are associated with the trackers unavailable to sub-user.
Most f data-modifying operations, on the contrary, require some rights to be present.

Possible rights are:

*   admin, – master user-only, can't be assigned to security groups
*   tracker_update,
*   tracker_register,
*   tracker_rule_update,
*   tracker_configure,
*   tracker_set_output,
*   tag_update,
*   task_update,
*   zone_update,
*   place_update,
*   employee_update,
*   vehicle_update,
*   payment_create
*   form_template_update,
*   reports;

### create

Create new security group.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters

* **group** - **JSON object**. ${security_group} without “id” field

#### response

```json5
{
    "success": true,
    "id": ${id of the created security group}
}
```

#### errors
*   13 – Operation not permitted – if user has insufficient rights
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without “multilevel_access” tariff feature)


### delete

Delete existing security group.
All sub-users belonging to this group will be assigned to default (null) security group.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters
* **security_group_id** - **int**. id of security group, which must be deleted.

#### response

```json5
{
    "success": true,
}
```

#### errors
*   13 – Operation not permitted – if user has insufficient rights
*   201 – Not found in database – when group with the specified security_group_id does not exist
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without “multilevel_access” tariff feature)

### list

List all security groups belonging to current user.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters
none.

#### response

```json5
{
    "success": true,
    "list": [${security_group}, ... ] //list of all sub-users belonging to this master account
}
```
Security group object is described [here](#security-group-object-structure).

#### errors

*   13 – Operation not permitted – if user has insufficient rights
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without “multilevel_access” tariff feature)

### update

Update existing security group.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters
* **group** - **JSON object**. ${security_group} with “id” field

#### response

```json5
{
    "success": true
}
```

#### errors
*   13 – Operation not permitted – if user has insufficient rights
*   201 – Not found in database – when security group with the specified id does not exist
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without “multilevel_access” tariff feature)

