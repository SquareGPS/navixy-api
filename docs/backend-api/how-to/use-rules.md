---
title: How to use rules
description: How to work with rules that used to set up conditions according to which the system logs the events and sends notifications to user.
---

# How to use rules

Rules used to set up conditions according to which the system logs the events and sends notifications to user.

When a server receives a new portion of data from the device, it checks whether the conditions set are true 
or false for this data. If they are true, the server generates an event in history, logs it and immediately sends SMS,
push message or email and saves event in history.
 
### Create

To start work the rule must be created. Let's create a rule with conditions according to which the platform will generate events and schedule intervals when this
 rule should work using the [rule/create](../resources/tracking/tracker/rules/rule.md#create). The user must have access to rule update.

Necessary parameters for this call. Availability of some parameters depends on used rule type:

* `name` - A string containing a name of created rule.
* `description` - A string containing rule's description.
* `zone_ids` - An int array. A list of zones to bind where the rule will work. Leave it empty if rule should work 
everywhere. Parameter `zone_ids` is not allowed for rule `offline` and required for `route` and `inoutzone` rule types.
* `trackers` - An int array. A list of tracker ids belong to user for which the rule will work.
* `type` - A string containing one of pre-defined types of rules. See [rule types](../resources/tracking/tracker/rules/rule_types.md).
* `primary_text` - A string with primary text of rule notification when condition is `true`.
* `secondary_text` - An optional string with secondary text of rule notification when condition is `false`. The availability of 
this parameter depends on rule type. Not every rule has the `secondary_text`.
* `param` - An optional integer. A common parameter that responsible for integer conditions. 
The availability of this parameter depends on rule type. See [rule types](../resources/tracking/tracker/rules/rule_types.md). 
* `alerts` - An object with destinations for notifications. Answers the question - who and how will receive notifications. Described in [rule object](../resources/tracking/tracker/rules/rule.md).
* `suspended` - A boolean which starts and stops the rule. `true` if the rule suspended.
* `schedule` - An optional object which configures the time - when the rule works. Described in [rule object](../resources/tracking/tracker/rules/rule.md).
* `extended_params` - An optional object. Specified for concrete rule type. See [rule types](../resources/tracking/tracker/rules/rule_types.md).

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"description": "", "type": "work_status_change", "primary_text": "status changed", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": false, "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "status_ids": [319281,319282,319283]}, "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7,"time": "23:59:59"}, "type": "weekly"}], "zone_ids": []}}'
    ```

You will get ID of created rule in response. 

```json
{
    "success": true,
    "id": 123
}
```

### Bind/Unbind

When a rule created, [bind](../resources/tracking/tracker/rules/rule.md#bind) devices to it. For example, a newly registered device must have the same rule. Unnecessary
to create another rule. Bind this device to an already existing rule.
Unbinding works similarly. When a rule is not necessary for some devices, [unbind](../resources/tracking/tracker/rules/rule.md#unbind) them without deleting rules.

Necessary parameters for both calls the same.
 
* `rule_id` - An id of a rule. You can get ids using the [rule/list](../resources/tracking/tracker/rules/rule.md#list) call.
* `trackers` - An int array. List trackers' IDs. Trackers which do not exist, owned by other user or deleted ignored without errors.
 
API requests:
 
=== "Bind"

 ```shell
 curl -X POST '{{ extra.api_example_url }}/tracker/rule/bind' \
     -H 'Content-Type: application/json' \
     -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule_id": 123, "trackers": [265489]}'
 ```

=== "Unbind"

 ```shell
 curl -X POST '{{ extra.api_example_url }}/tracker/rule/unbind' \
     -H 'Content-Type: application/json' \
     -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule_id": 123, "trackers": [265489]}'
 ```

### Update

If the rule must be updated, for example, one more phone number must be added for SMS notifications, you can use the 
[rule/update](../resources/tracking/tracker/rules/rule.md#update) call. It is much better than deleting an existing rule and creating a new one.

List of necessary parameters is the same as in [rule/create](#create) call plus `id` parameter.

* `id` - An integer with id of the updating rule. You can get ids using the [rule/list](../resources/tracking/tracker/rules/rule.md#list) call.

API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"id": 123, "description": "", "type": "work_status_change", "primary_text": "status changed", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": false, "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "status_ids": [319281,319282,319283]}, "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7, "time": "23:59:59"}, "type": "weekly"}], "zone_ids": []}}'
    ```
 
### Suspend

To suspend the rule use the [rule/update](../resources/tracking/tracker/rules/rule.md#update) call and change only one parameter `suspended` to `true`. All other parameters 
should present in the call without changes.
 
API request:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"id": 123, "description": "", "type": "work_status_change", "primary_text": "status changed", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": true, "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "status_ids": [319281,319282,319283]}, "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7, "time": "23:59:59"}, "type": "weekly"}], "zone_ids": []}}'
    ```