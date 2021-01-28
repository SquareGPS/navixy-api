---
title: Transaction
description: API call to get list of user's billing transactions for the specified period.
---

# Transaction

API path: `/transaction`.

API call to get user's billing transactions.

## Transaction object

```json
{
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
}
```

* `description` - string. Transaction description.
* `type` - string enum. Type of transaction.
* `subtype` - string enum. Subtype of transaction.
* `timestamp` - string date/time. When transaction created.
* `user_id` - int. ID of a user which made a transaction.
* `dealer_id` - int. ID of a dealer.
* `tracker_id` - int. Tracker id. 0 if transaction not associated with tracker.
* `amount` - double. Amount of money in transaction, can be negative. e.g. -10.0000 means 10 money units removed from user`s balance.
* `new_balance` - double. User`s money balance after transaction.
* `old_balance` - double. User`s money balance before transaction.
* `bonus_amount` - double. Amount of bonus used in transaction, can be negative. e.g. 10.0000 means 10 bonuses units added to user`s bonus balance.
* `new_bonus` - double. User`s bonus balance after transaction.
* `old_bonus` - double. User`s bonus balance before transaction.

### list

Gets list of user's billing transactions for the specified period.

**required sub-user rights**: `payment_create`.

#### parameters

| name | description | type|
| :------ | :------ | :-----|
| from | Start date/time for searching. | string date/time |
| to | End date/time for searching. Must be after `from` date. | string date/time |
| limit | Optional. Maximum number of returned transactions. | int |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/transaction/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "from": "2021-01-20 08:16:40", "to": "2021-01-28 08:16:40"}'
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

* `list` - array of objects. List of [transactions objects](#transaction-object).

#### errors

* 211 – Requested time span is too big - more than **maxReportTimeSpan** config option.
