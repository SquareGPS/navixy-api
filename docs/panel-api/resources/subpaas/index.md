---
title: Subpaas actions
description: Subpaas actions
---

**Dealer** means parent of subpaas.

**dealer\_block\_type** type is enum object:

 * NOT_BLOCKED
 * INITIAL_BLOCK
 * BLOCK_LOGIN
 * CLIENTS_BLOCKED
 * DELETED

API base path: `/subpaas`

## create

Create subpaas. After creation its dealer_block_type will be in INITIAL_BLOCK status

#### parameters

*   **password** – **string**. Subpaas's password
*   **title** – **string**. Subpaas's name
*   **email** – **string**. Company email
*   **jur_name** – **string**. Legal (juristic) company name
*   **link_monitoring** – **string**. Subpaas's domain name
*   **jur_country** – **string**. Subpaas's country

#### errors

* 13 – If the dealer
    * is not paas
    * has different status than NOT_BLOCKED
    * his tariff doesn't allow subpaases


#### response

```json
{ "success": true }
```

## list

Get list of all subpaases for dealer. Dealer id will be taken from the session.

#### parameters

*   **order_by** – **string** (default: **subpaas_id**). Sort option. Possible values:
    <br> — subpaas_id
    <br> — title
    <br> — jur_name
    <br> — login
    <br> — block_type
    <br> — creation_date
*   **ascending** – **boolean** (default: **true**). If true, ordering will be ascending, descending otherwise.
*   **limit** – **int**. Pagination. Maximum subpaases to return, e.g. 10
*   **offset** – **int**. Pagination. Get subpaases starting from, e.g. 0

#### errors 

* 13 – If the dealer
    * is not paas
    * has different status than NOT_BLOCKED
    * his tariff doesn't allow subpaases

#### response

```js
{
  "success": true,
  "list": [
    {
      "subpaas_id": 18,
      "title": "SubppaasTitle",
      "jur_name": "SubppaasJurName",
      "login": "subpaaslogin",
      "creation_date": "2018-11-15",
      "block_type": "NOT_BLOCKED", // <dealer_block_type>
      "users_count": 2,
      "active_users_count": 1,
      "trackers_count": 0,
      "active_trackers_count": 0
    }
  ]
}
```

## read

Get subpaas info by its id.

#### parameters

*   **subpaas_id** – **int**. Subpaas id

#### errors

* 13 – If the dealer
    * is not paas
    * has different status than NOT_BLOCKED
    * his tariff doesn't allow subpaases

#### response

```js
{
  "success": true,
  "value": {
    "subpaas_id": 18,
    "block_type": "NOT_BLOCKED", // <dealer_block_type>
    "title": "Rus Sub-PaaS",
    "jur_name": "OOO Sub-PaaS",
    "email": "sub-dealer@email.com",
    "jur_country": "country",
    "link_monitoring": "link",
    "contact_fio": "fio", // The contact person
    "contact_post": "post", // The contact post (position)
    "contact_phone": "phone" // The contact phone
  }
}
```

## update

Update subpaas.

#### parameters

*   **subpaas_id** – **id**. Subpaas's id
*   **password** – **string**. Subpaas's password
*   **title** – **string**. Subpaas's company name
*   **email** – **string**. Subpaas's email
*   **jur_name** – **string**. Legal (juristic) subpaas's company name
*   **link_monitoring** – **string**. Subpaas's domain name
*   **jur_country** – **string**. Subpaas's country
*   **contact_fio** – **string**. The contact person
*   **contact_post** – **string**. The contact post (position)
*   **contact_phone** – **string**. The contact phone
*   **block_type** – **string**. <dealer\_block\_type>

#### errors

* 13 –
    * The dealer is not paas
    * The dealer has different status than NOT_BLOCKED
    * The dealer's tariff doesn't allow subpaases
    * block_type is DELETED
    * Found subpaas is in DELETED status
    * Found subpaas is not in INITIAL_BLOCK status and block_type is INITIAL_BLOCK
    * Found subpaas is in INITIAL_BLOCK status and block_type is not INITIAL_BLOCK

#### response

```json
{ "success": true }
```