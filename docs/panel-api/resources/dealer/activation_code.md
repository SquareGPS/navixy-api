---
title: /activation_code
description: /activation_code
---

API base path: `/dealer/activation_code`

## create

Create **count** activation codes with passed **tariff_id**, **bonus_amount** and **free_days**. And return count of created codes.

#### required permissions:

*   **activation_code**: "read", "create"

#### parameters

*   **count** \- **int**. count of codes to creation.
*   **tariff_id** \- id of new tariff (have to belongs to current dealer)
*   **bonus_amount** \- new bonus
*   **free_days** \- new free period

#### response

    {
        "success": true,
        "count": <int> // count of actually updated codes
    }
    

#### errors

*   201 - Not found in database (when tariff with **tariff_id** not found for current dealer)


## list

List all dealer's activation codes. If "filter" is used, entities will be returned only if filter string is contained within one of the following fields: code, tariff\_id, device\_id, device_type 

#### required permissions:

*   **activation_code**: "read"

#### parameters

*   **filter**  – **string** (optional). Text filter string.
*   **order_by**  – **string** (optional). Specify list ordering. Can be one of code, activated, tariff\_id, tariff\_name, device\_type, money\_amount, bonus\_amount, free\_days 
*   **ascending**  – **boolean** (optional). If true, ordering will be ascending, descending otherwise. Default is true.
*   **offset** – **int** (optional). Starting offset, used for pagination. Default is 0.
*   **limit** – **int** (optional). Max number of records to return, used for pagination.

#### response

    {
        "success": true,
        "list": [<activation_code>, ...],
        "count" : <int> // total number of records (ignoring offset and limit), e.g. 42
    }
    
## update

Change **tariff_id**, **bonus_amount** and **free_days** for all activation codes which: 
1. has **code** listed in **codes** parameter 
2. belongs to current dealer 
3. not activated yet 
4. belongs to same device_type as new tariff And return count of updated codes. 

#### required permissions:

*   **activation_code**: "update"

#### parameters

*   **codes** \- JSON list of strings - codes to update
*   **tariff_id** \- id of new tariff (have to belongs to current dealer)
*   **bonus_amount** \- new bonus
*   **free_days** \- new free period

#### response

    {
        "success": true,
        "count": <int> // count of actually updated codes
    }
    

#### errors

*   201 - Not found in database (when tariff with **tariff_id** not found for current dealer)