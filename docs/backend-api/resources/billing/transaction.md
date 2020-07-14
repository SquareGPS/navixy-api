---
title: /transaction
description: /transaction
---

## list(...)

Get list of user’s billing transactions for the specified period.

**required subuser rights**: payment_create

#### parameters:

* **from** – date/time. Start date/time for searching.
* **to** – date/time. End date/time for searching. must be after “from” date.
* **limit** – int (optional). Maximum number of returned transactions.

#### return:

    {
      "success": true,
      "list": [
         {
            "description": ,  // transaction description, e.g. "Recharge bonus balance during tracker registration"
            "type": ,         // type, e.g. "bonus_charge"
            "subtype": ,      // subtype, e.g. "register"
            "timestamp": , // date/time at which transaction was created, e.g. "2013-08-02 08:16:40"
            "user_id": ,         // user Id, e.g. 12203
            "dealer_id": ,       // dealer Id, e.g. 5001
            "tracker_id": ,      // tracker id, e.g., 3036, or 0 if transaction is not associated with tracker
            "amount": ,       // amount of money in transaction, can be negative. e.g. -10.0000 means 10 money units were removed from user`s balance
            "new_balance": ,  // user`s money balance after transaction, e.g. 800.0000
            "old_balance": ,  // user`s money balance before transaction, e.g. 810.0000
            "bonus_amount": , // amount of bonus used in transaction, can be negative. e.g. 10.0000 means 10 bonuses units were added to user`s bonus balance
            "new_bonus": ,    // user`s bonus balance after transaction, e.g. 10.0000
            "old_bonus":      // user`s bonus balance before transaction, e.g. 0.0000
         }, ...
      ]
    }


#### errors:

* 211 – Requested time span is too big (more than **maxReportTimeSpan** config option)
