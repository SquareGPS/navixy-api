---
title: Rule
description: API calls to interact with tracker's rules. Rules used to set up conditions according to which the system logs the events and sends notifications to user.
---

# Rule

Contains API calls to interact with tracker's rules. Rules used to set up conditions according to which the system logs
the events and sends notifications to user.

Described creation and using rules step-by-step in the [guide](../../../../guides/rules-notifications/use-rules.md).


## Rule object

```json
{
  "id": 668054,
  "name": "Lock is opened/closed",
  "type": "locking_unlocking",
  "description": "This rule was created automatically",
  "zone_ids": [ 18928 ],
  "trackers": [ 10029750, 10030168, 10031971 ],
  "primary_text": "Lock is opened",
  "secondary_text": "Lock is closed",
  "param": 0,
  "alerts": {
    "sms_phones": [],
    "phones": [],
    "emails": [],
    "push_enabled": true
  },
  "suspended": false,
  "auto_created": true,
  "schedule": [{
    "type": "weekly",
    "from": {
      "weekday": 1,
      "time": "00:00:00"
    },
    "to": {
      "weekday": 7,
      "time": "23:59:59"
    },
    "interval_id": 48732
  }],
  "extended_params": {
    "emergency": false,
    "zone_limit_inverted": false,
    "private_rule": true
  }
}
```

* `id` - int. An ID of a rule.
* `name` - string. Name of a rule.
* `type` - enum. One of pre-defined types of rules. See [rule types](rule_types.md).
* `description` - string. Rule's description.
* `zone_ids` - int array. List of geofence IDs.
* `trackers` - int array. List of bound tracker IDs.
* `primary_text` - string. Primary text of rule notification.
* `secondary_text` - string. Secondary text of rule notification.
* `param` - int. A common parameter. See [rule types](rule_types.md).
* `alerts` - object with destinations for notifications. 
    * `sms_phones` - string array. Phones for SMS notifications.
    * `phones` - string array. Phones for voice calls.
    * `emails` - string array. Emails for notifications.
    * `push_enabled` - boolean. If `true` push notifications available.
    * `emergency` - boolean. If `true` notifications will be marked as emergency with color and sound.
* `suspended` - boolean. `true` if the rule suspended.
* `auto_created` - optional, boolean. `true` means that the rule created automatically.
* `shedule` - optional object. The rule will work in specified period. 
* `extended_params` - optional. An object specified for concrete rule type. See [rule types](rule_types.md).

* **schedule_interval** is one of:

    * **weekly_schedule_interval**
    
    ```json
    {
      "type": "weekly",
      "from": {
        "weekday": 1,
        "time": "00:00:00"
      },
      "to": {
        "weekday": 7,
        "time": "23:59:59"
      },
      "interval_id": 1
    }
    ```
    * **fixed_schedule_interval**
    
    ```json
    {
      "type": "fixed",
      "from": "2014-07-09 07:50:58",
      "to": "2014-07-10 07:50:58",
      "interval_id": 3
    }
    ```

* `date/time` and `local_time` types described at 
the [data types description section](../../../../getting-started/introduction.md#data-types).


## API actions

API base path: `/tracker/rule`.

### `bind`

Binds rule with `rule_id` to trackers list.

**required sub-user rights:** `tracker_rule_update`.

#### Parameters

| name     | description                                                                                          | type      |
|:---------|:-----------------------------------------------------------------------------------------------------|:----------|
| rule_id  | ID of a rule.                                                                                        | int       |
| trackers | IDs of trackers. Trackers which do not exist, owned by other user or deleted ignored without errors. | int array |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/bind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule_id": 123, "trackers": [265489]}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if rule with `rule_id` does not exist or owned by other user.


### `create`

Creates rule and scheduled intervals.

**required sub-user rights:** `tracker_rule_update`.

#### Parameters

Presented parameters are common for all rule types. However, there are specific parameters  `primary_text` and `secondary_text` 
that are described for every rule type if exist in [rule types](rule_types.md).

| name            | description                                                                                                                                                                                                      | type                                              |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------|
| name            | The name of created rule.                                                                                                                                                                                        | string                                            |
| description     | Rule's description.                                                                                                                                                                                              | string                                            |
| trackers        | List of tracker IDs belong to user for which the rule will work.                                                                                                                                                 | int array                                         |
| zone_ids        | List of zones to bind where the rule will work. Leave it empty if rule should work everywhere. Parameter `zone_ids` is not allowed for rule `offline` and can't be empty for `route` and `inoutzone` rule types. | int array                                         |
| type            | One of pre-defined types of rules. See [rule types](rule_types.md).                                                                                                                                            | [enum](../../../../getting-started/introduction.md#data-types) |
| param           | A common parameter that responsible for integer conditions. See [rule types](rule_types.md).                                                                                                                   | int                                               |
| alerts          | An object with destinations for notifications. Described [above](#rule-object).                                                                                                                                  | JSON object                                       |
| suspended       | Starts or stops tracking the rule. `true` if the rule suspended.                                                                                                                                                 | boolean                                           |
| schedule        | An optional object. Configures the time - when the rule works. Described [above](#rule-object).                                                                                                                  | JSON object                                       |
| extended_params | An optional object. Specified for concrete rule type. See [rule types](rule_types.md).                                                                                                                         | JSON object                                       |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"description": "", "type": "work_status_change", "primary_text": "status changed", "secondary_text": "", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": "", "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "append_zone_title": "", "status_ids": [319281,319282,319283]}, "param": "", "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7, "time": "23:59:59"}, "type": "weekly"}], "zone_ids": [], "group_id": 1}}'
    ```

#### Response

```json
{
    "success": true,
    "id": 123
}
```

* `id` - int. An ID of created rule.

#### Errors

* 204 - Entity not found – when associated zone is not exist.


### `delete`

Deletes rule with rule_id and all related objects from the database.

**required sub-user rights:** `tracker_rule_update`.

#### Parameters

| name    | description   | type |
|:--------|:--------------|:-----|
| rule_id | ID of a rule. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule_id": 123}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/rule/delete?hash=a6aa75587e5c59c32d347da438505fc3&rule_id=123
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if rule with `rule_id` does not exist or owned by other user.


### `list`

List tracker rules bound to tracker with an ID=`tracker_id` or all users' tracker rules if `tracker_id` not passed.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/rule/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
   "success": true,
   "list": [{
     "id": 667281,
     "name": "Case intrusion",
     "type": "case_intrusion",
     "description": "This rule was created automatically",
     "zone_id": 0,
     "trackers": [10029448, 10030168],
     "primary_text": "Case is opened",
     "secondary_text": "Case is closed",
     "param": 0,
     "alerts": {
       "sms_phones": [],
       "phones": [],
       "emails": [],
       "push_enabled": true
     },
     "suspended": false,
     "auto_created": true,
     "schedule": [{
       "type": "weekly",
       "from": {
         "weekday": 1,
         "time": "00:00:00"
       },
       "to": {
         "weekday": 7,
         "time": "23:59:59"
       },
       "interval_id": 46892
     }]
   }]
}
```

* `list` - list of rules


### `unbind`

Unbinds trackers from rule with `rule_id`.

**required sub-user rights:** `tracker_rule_update`.

#### Parameters

| name     | description                                                                                          | type      |
|:---------|:-----------------------------------------------------------------------------------------------------|:----------|
| rule_id  | ID of a rule.                                                                                        | int       |
| trackers | IDs of trackers. Trackers which do not exist, owned by other user or deleted ignored without errors. | int array |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/unbind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule_id": 123, "trackers": [265489]}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if rule with `rule_id` does not exist or owned by other user.


### `update`

Updates rule and scheduled intervals.

**required sub-user rights:** `tracker_rule_update`.

#### Parameters

Presented parameters are common for all rules, but there are specific parameters that can be found in [rule types](rule_types.md).

| name            | description                                                                                                                                                                                                                                | type                                              |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------|
| id              | ID of a rule. You can get IDs using the [rule/list](#list) call.                                                                                                                                                                           | int                                               |
| name            | The name of created rule.                                                                                                                                                                                                                  | string                                            |
| description     | Rule's description.                                                                                                                                                                                                                        | string                                            |
| zone_ids        | List of zones to bind where the rule will work. Leave it empty if rule should work everywhere. Parameter `zone_ids` is not allowed for rule `offline` and required for `route` and `inoutzone` rule types (there can be exactly one item). | int array                                         |
| trackers        | List of tracker IDs belong to user for which the rule will work.                                                                                                                                                                           | int array                                         |
| type            | One of pre-defined types of rules. See [rule types](rule_types.md).                                                                                                                                                                      | [enum](../../../../getting-started/introduction.md#data-types) |
| param           | A common parameter that responsible for integer conditions. See [rule types](rule_types.md).                                                                                                                                             | int                                               |
| alerts          | An object with destinations for notifications. Described [above](#rule-object).                                                                                                                                                            | JSON object                                       |
| suspended       | Starts and stops tracking the rule. `true` if the rule suspended.                                                                                                                                                                          | boolean                                           |
| schedule        | An optional object. Configures the time - when the rule works. Described [above](#rule-object).                                                                                                                                            | JSON object                                       |
| extended_params | An optional object. Specified for concrete rule type. See [rule types](rule_types.md).                                                                                                                                                   | JSON object                                       |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"id": 123, "description": "", "type": "work_status_change", "primary_text": "status changed", "secondary_text": "", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": "", "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "append_zone_title": "", "status_ids": [319281,319282,319283]}, "param": "", "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7, "time": "23:59:59"}, "type": "weekly"}], "zone_ids": [], "group_id": 1}}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if rule is not exists or owned by other user.
* 204 - Entity not found – when new associated zone is not exists.
