---
title: Bill
description: Bill
---

# Bill

API path: `/bill`.

### create

Creates new bill for the user. Required subuser rights: `payment_create`.

#### parameters

| name | description | type| restrictions|
| :------ | :------ | :-----| :------|
| payer | some payer description | string| Payer Name |
| sum |bill sum in default currency of the panel | int | 1000 |

#### example

    {{ extra.api_example_url }}/bill/create?hash=22eac1c27af4be7b9d04da2ce1af111b&payer=John Doe&sum=500

#### response

```json5
{
    "success": true,
    "value": 6421     // created bill id
}
```

#### errors

*   222 – Plugin not found (when plugin **29** not available for user)

### list

Shows list of bills with their parameters in array. Required subuser rights: payment_create

#### structure:

    {{ extra.api_example_url }}/bill/list?hash=your_hash&limit=number_of_bills&offset=start_from

#### parameters


| name | description | type| format|
| :------ | :------ | :----- | :------ |
| limit | maximum number of bills in list (maximum and default **10 000**) - optional | int | 10000 |
| offset | get bills starting from **offset** (default **0**) - optional | int | 0 |

#### example

    {{ extra.api_example_url }}/bill/list?hash=22eac1c27af4be7b9d04da2ce1af111b&limit=9500&offset=0

#### response

```json5
{
    "success": true,
    "count": 7,      // total number of bills
    "bills": [${bill}, ...]
}
```

where **bill** is

```json5
{
    "order_id": 63602,                 // unique id
    "created": "2012-03-05 11:55:03",  // creation date/time
    "sum": 150.0,                      // bill sum in rubbles
    "status": "created",               // bill order status
    "positions": ["The subscription fee for the services of Gdemoi Account W3"],  // list of position names.
                                       // usually contains one element for bill
    "link": "http://bill.navixy.com/xK1QEYK" // url to order
}
```

If bill created using [/bill/create](#create) call then **positions** will contains exactly one element.

**status** may be one of:

* created – but not settled
* settled
* canceled 

_Note for Standalone version_: Base part of **link** may be changed by **billing.orders.baseUrl** config option.

#### errors

*   222 – Plugin not found (when plugin **29** not available for user)
