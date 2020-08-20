---
title: Tariff tracker
description: Tariff tracker
---

# Tariff tracker

API path: `/tariff/tracker/`.

User of **dealer** can switch tracker from tariff **t1** to tariff **t2** if:

1.  tracker belongs to user and isn’t a _clone_.
2.  tracker’s tariff last changed more than **tariff.freeze.period** (config option. default 30 days) ago.
3.  **t1.tariff_id** != **t2.tariff_id**, i.e. new tariff must be differ from current.
4.  **t1.dealer_id** = **t2.dealer_id** = **dealer.effectiveDealerId**, i.e. current and new tariffs must belongs to user’s effective dealer
5.  **t2.active** = **1**, i.e. new tariff is _active_ (tariff’s option “Allow users to switch to this tariff independently” in **panel** is set **on**)
6.  **t1.grouping** = **t2.grouping**, i.e. user can change tariff only within one group of tariffs
7.  **t2.device** = **tracker**, i.e. new tariff must be for trackers
8.  new tariff is [available to user’s legal type](index.md#tariff)

User’s **effective dealer** is

1.  user’s dealer if its **dealer_id** = **defaultDealerId** (config option) or **dogovor_type** = ‘paas’
2.  parent of user’s dealer elsewise

#### errors

*   201 – Not found in database (if user doesn’t have trackers with given **tracker_id**)
*   219 – Not allowed for clones of the device
*   237 – Invalid tariff (if there are no tariff with tracker.tariff_id and belongs to user’s **effective dealer**)

### change

Change tariff of tracker (with **tracker_id**) to new tariff (with **tariff_id**).

**required subuser rights**: admin (available only to master users)

#### return

```js
{ "success": true }
```

#### errors

*   221 (Device limit exceeded) – when new tariff device limit is less then count of trackers in cabinet.
*   238 (Changing tariff is not allowed) – user can’t switch tracker to that tariff.
*   239 – New tariff doesn’t exist.
*   240 (Not allowed to change tariff too frequently) – tariff last changed less or equal to 30 days (**tariff.freeze.period** config option).


### list

List tariffs on which user can switch passed tracker (even when tariff last changed less or equal than **tariff.freeze.period** time ago).

#### parameters

*   tracker_id

#### return

```js
{
  "success": true,
  "list": [${tariff}, ...],
  "days_to_next_change": ${int} // days to next free change, or 0 if free change available.
}
```

See **tariff** object structure [here](index.md#tariff).
