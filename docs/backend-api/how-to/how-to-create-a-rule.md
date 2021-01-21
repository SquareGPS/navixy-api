---
title: How to use rules
description: Rules used to set up conditions according to which the system logs the events and sends notifications to user.
---

# How to use rules

Rules used to set up conditions according to which the system logs the events and sends notifications to user.

When a server receives a new portion of data from the device, it checks whether the conditions set are true 
or false for this data. If they are true, the server generates an event in history, logs it and immediately sends SMS or
 Email, as specified.
 
### Create

Let's create a rule with conditions according to which the platform will generate events and schedule intervals when this
 rule should work. The user must have access to rule update.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| name | The name of created rule. | string |
| description | Rule's description. | string |
| zone_ids | List of zones to bind where the rule will work. Leave it empty if rule should work everywhere. | array of int |
| trackers | List of tracker ids belong to user for which the rule will work. | array of int |
| type | One of pre-defined types of rules. See [rule types](../resources/tracking/tracker/rules/rule_types.md). | string enum |
| primary_text | Primary text of rule notification when condition is true. | string |
| secondary_text | Secondary text of rule notification when condition is false. | string |
| param | A common parameter that responsible for integer conditions. See [rule types](../resources/tracking/tracker/rules/rule_types.md). | int |
| alerts | An object with destinations for notifications. Described below. | JSON object |
| suspended | Starts and stops the rule. `true` if the rule suspended. | boolean |
| schedule | An optional object. Configures the time - when the rule works. Described below. | JSON object |
| extended_params | An optional object. Specified for concrete rule type. See [rule types](../resources/tracking/tracker/rules/rule_types.md). | JSON object |

Alerts object:

```json
{
  "sms_phones": ["98829991"],
  "phones": ["98829991"],
  "emails": ["example@test.com"],
  "push_enabled": true,
  "emergency": false
}
```

* `sms_phones` - array of int. Phone numbers with country code and without "+" sign for SMS notifications.
* `phones` - array of string. Phone numbers with country code and without "+" sign for voice calls.
* `emails` - array of string. Emails for notifications.
* `push_enabled` - boolean. If `true` push notifications available.
* `emergency` - boolean. If `true` notifications will be marked as emergency with color and sound.

Schedule object can be:

* **weekly_schedule_interval**

```json
{
  "type": "weekly",
  "from": {
    "weekday":1,
    "time":"00:00:00"
  },
  "to": {
    "weekday":7,
    "time":"23:59:59"
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

* `date/time` and `local_time` types described at the [data types description section](../getting-started.md#data-types).

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"description": "", "type": "work_status_change", "primary_text": "status changed", "secondary_text": "", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": "false", "append_zone_title": "", "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "status_ids": [319281,319282,319283]}, "param": "", "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7,"time": "23:59:59"}, "type": "weekly"}], "zone_ids": [], "group_id": 1}}'
    ```

#### response

You will get created rule ID.

```json
{
    "success": true,
    "id": 123
}
```

#### errors

* 204 - Entity not found – when associated zone is not exist.

### Bind/Unbind

When a rule created, bind devices to it. For example, a newly registered device must have the same rule. Unnecessary
to create another rule. Bind this device to an already existing rule.
Unbinding works similarly. When a rule is not necessary for some devices, unbind them without deleting rules.

#### parameters
 
| name | description | type |
| :------ | :------ | :----- |
| rule_id | Id of a rule. You can get ids using the [rule/list](../resources/tracking/tracker/rules/rule.md#list) call. | int |
| trackers | Ids of trackers. Trackers which do not exist, owned by other user or deleted ignored without errors. | array of int |
 
#### examples
 
=== "Bind"

 ```shell
 curl -X POST '{{ extra.api_example_url }}/tracker/rule/bind' \
     -H 'Content-Type: application/json' \
     -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule_id": "123", "trackers": [265489]}'
 ```

=== "Unbind"

 ```shell
 curl -X POST '{{ extra.api_example_url }}/tracker/rule/unbind' \
     -H 'Content-Type: application/json' \
     -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule_id": "123", "trackers": [265489]}'
 ```
 
#### response

You will get status of request.

```json
{
    "success": true
}
```

### Update

If the rule must be updated, for example, one more phone number must be added for SMS notifications, you can use the 
rule/update call. It is much better than deleting an existing rule and creating a new one.

#### parameters

All parameters must be in the request.

| name | description | type |
| :------ | :------ | :----- |
| id | Id of a rule. You can get ids using the [rule/list](../resources/tracking/tracker/rules/rule.md#list) call. | int |
| name | The name of created rule. | string |
| description | Rule's description. | string |
| zone_ids | List of zones to bind where the rule will work. Leave it empty if rule should work everywhere. | array of int |
| trackers | List of tracker ids belong to user for which the rule will work. | array of int |
| type | One of pre-defined types of rules. See [rule types](../resources/tracking/tracker/rules/rule_types.md). | string enum |
| primary_text | Primary text of rule notification when condition is true. | string |
| secondary_text | Secondary text of rule notification when condition is false. | string |
| param | A common parameter that responsible for integer conditions. See [rule types](../resources/tracking/tracker/rules/rule_types.md). | int |
| alerts | An object with destinations for notifications. Described [above](#create). | JSON object |
| suspended | Starts and stops the rule. `true` if the rule suspended. | boolean |
| schedule | An optional object. Configures the time - when the rule works. Described [above](#create). | JSON object |
| extended_params | An optional object. Specified for concrete rule type. See [rule types](../resources/tracking/tracker/rules/rule_types.md). | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"id": 123, "description": "", "type": "work_status_change", "primary_text": "status changed", "secondary_text": "", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": "false", "append_zone_title": "", "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "status_ids": [319281,319282,319283]}, "param": "", "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7, "time": "23:59:59"}, "type": "weekly"}], "zone_ids": [], "group_id": 1}}'
    ```
 
### Suspend

To suspend the rule use the rule/update call and change only one parameter `suspended` to `true`. All other parameters 
should be in the call without changes.
 
#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"id": 123, "description": "", "type": "work_status_change", "primary_text": "status changed", "secondary_text": "", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": "true", "append_zone_title": "", "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "status_ids": [319281,319282,319283]}, "param": "", "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7, "time": "23:59:59"}, "type": "weekly"}], "zone_ids": [], "group_id": 1}}'
    ```