# Using Rules

Rules are used to set up conditions according to which the system logs events and sends notifications to users.

When a server receives new data from a device, it checks whether the set conditions are true or false for this data. If they are true, the server generates an event in history, logs it, immediately sends an SMS, push message, or email, and saves the event in history.

## Creating a Rule

To start working with rules, you must first create one. This involves setting up conditions under which the platform will generate events and scheduling intervals during which the rule should be active using the [`rule/create`](../../resources/tracking/tracker/rules/rule.md#create) API call. The user must have access to rule updates.

### Required Parameters

Availability of some parameters depends on the rule type used:

* `name`: A string containing the name of the created rule.
* `description`: A string containing the rule's description.
* `zone_ids`: An array of integers. A list of zones where the rule will be active. Leave it empty if the rule should work everywhere. `zone_ids` is not allowed for the `offline` rule and is required for `route` and `inoutzone` rule types.
* `trackers`: An array of integers. A list of tracker IDs that belong to the user for which the rule will work.
* `type`: A string containing one of the predefined rule types. See [rule types](../../resources/tracking/tracker/rules/rule_types.md).
* `primary_text`: A string with the primary text of the rule notification when the condition is `true`.
* `secondary_text`: An optional string with the secondary text of the rule notification when the condition is `false`. The availability of this parameter depends on the rule type.
* `param`: An optional integer for common integer conditions. The availability of this parameter depends on the rule type. See [rule types](../../resources/tracking/tracker/rules/rule_types.md).
* `alerts`: An object with destinations for notifications. Defines who and how notifications will be received. Described in the [rule object](../../resources/tracking/tracker/rules/rule.md).
* `suspended`: A boolean that starts and stops the rule. `true` if the rule is suspended.
* `schedule`: An optional object that configures the time when the rule works. Described in the [rule object](../../resources/tracking/tracker/rules/rule.md).
* `extended_params`: An optional object specified for a particular rule type. See [rule types](../../resources/tracking/tracker/rules/rule_types.md).

### API Request

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/tracker/rule/create' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"description": "", "type": "work_status_change", "primary_text": "status changed", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": false, "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "status_ids": [319281,319282,319283]}, "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7,"time": "23:59:59"}, "type": "weekly"}], "zone_ids": []}}'
```

The platform will respond with the ID of the created rule.

```json
{
    "success": true,
    "id": 123
}
```

## Binding and Unbinding Rules

Once a rule is created, you can bind devices to it using the [`rule/bind`](../../resources/tracking/tracker/rules/rule.md#bind) call. For instance, if a newly registered device needs to follow an existing rule, bind it to the rule without creating a new one. Similarly, use the [`rule/unbind`](../../resources/tracking/tracker/rules/rule.md#unbind) call to remove devices from a rule when it is no longer needed for them.

### Required Parameters

* `rule_id`: The ID of the rule. You can get rule IDs using the [`rule/list`](../../resources/tracking/tracker/rules/rule.md#list) call.
* `trackers`: An array of integers. List of tracker IDs. Trackers that do not exist, are owned by another user, or are deleted will be ignored without errors.

### API Requests

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

## Updating a Rule

If a rule needs to be updated, such as adding another phone number for SMS notifications, use the [`rule/update`](../../resources/tracking/tracker/rules/rule.md#update) call. This method is more efficient than deleting an existing rule and creating a new one.

### Required Parameters

The list of necessary parameters is the same as in the [`rule/create`](#creating-a-rule) call, plus the `id` parameter.

* `id`: An integer with the ID of the rule to be updated. You can get rule IDs using the [`rule/list`](../../resources/tracking/tracker/rules/rule.md#list) call.

### API Request

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/tracker/rule/update' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"id": 123, "description": "", "type": "work_status_change", "primary_text": "status changed", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": false, "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "status_ids": [319281,319282,319283]}, "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7, "time": "23:59:59"}, "type": "weekly"}], "zone_ids": []}}'
```

## Suspending a Rule

To suspend a rule, use the [`rule/update`](../../resources/tracking/tracker/rules/rule.md#update) call and change only the `suspended` parameter to `true`. All other parameters should remain unchanged.

### API Request

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/tracker/rule/update' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"id": 123, "description": "", "type": "work_status_change", "primary_text": "status changed", "alerts": {"push_enabled": true, "emails": ["example@gmail.com"], "emergency": false, "sms_phones": ["745494878945"], "phones": []}, "suspended": true, "name": "Status changing", "trackers": [123456], "extended_params": {"emergency": false, "zone_limit_inverted": false, "status_ids": [319281,319282,319283]}, "schedule": [{"from": {"weekday": 1, "time": "00:00:00"}, "to": {"weekday": 7, "time": "23:59:59"}, "type": "weekly"}], "zone_ids": []}}'
```