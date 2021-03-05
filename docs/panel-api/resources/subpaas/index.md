---
title: Subpaas actions
description: API calls to interact with Subpaases.
---

# Subpaas actions

API calls to interact with Subpaases.

API base path: `panel/subpaas`.

## Subpaas object

```json
{
  "subpaas_id": 18,
  "title": "SubppaasTitle",
  "jur_name": "SubppaasJurName",
  "login": "subpaaslogin",
  "creation_date": "2018-11-15",
  "block_type": "NOT_BLOCKED",
  "users_count": 2,
  "active_users_count": 1,
  "trackers_count": 0,
  "active_trackers_count": 0,
  "contact_fio": "fio",
  "contact_post": "post"
}
```

* `subpaas_id` - int. Subpaas id.
* `title` - string. Subpaas's name.
* `jur_name` - string. Legal (juristic) company name.
* `creation_date` - string. Creation date.
* `block_type` - [enum](../../../backend-api/getting-started.md#data-types). Panel and Subpaas's users block status. One of: 
"NOT_BLOCKED", "INITIAL_BLOCK", "BLOCK_LOGIN" or "CLIENTS_BLOCKED".
* `users_count` - int. Count of users.
* `active_users_count` - int. Count of active users.
* `trackers_count` - int. All devices of Subpaas.
* `active_trackers_count` - int. Active devices of Subpaas.
* `contact_fio` - string. Contact person.
* `contact_post` - string. Contact post (position).
* `contact_phone` - string. Contact's phone.

### create

Creates subpaas. After creation its `dealer_block_type` will be in `INITIAL_BLOCK` status.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| password | Subpaas's password. | string |
| title | Subpaas's name. | string |
| email | Company email. | string |
| jur_name | Legal (juristic) company name. | string |
| jur_country | Subpaas's country | string |
| link_monitoring | Subpaas's domain name. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/subpaas/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "password": "B1r7d@Y", "title": "Company", "email": "email@company.com", "jur_name": "Company", "jur_country": "Finland", "link_monitoring": "company.com"}'

#### response

```json
{
    "success": true
}
```

#### errors

* 13 – If the dealer
    * is not paas.
    * has different status than `NOT_BLOCKED`.
    * his tariff doesn't allow subpaases.

### list

Gets a list of all subpaases for a dealer. Dealer id will be taken from the session key.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| order_by | Optional. Sort option. Can be "subpaas_id", "title", "jur_name", "login", "block_type", "creation_date". Default is `subpaas_id`. | [enum](../../../backend-api/getting-started.md#data-types) |
| ascending | Optional. If `true` ordering will be ascending, descending otherwise. Default is `true`. | boolean |
| limit | Optional. Pagination. Maximum subpaases to return | int |
| offset | Optional. Pagination. Get subpaases starting from. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/subpaas/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
        
    === "HTTP GET"
    
        ```
        {{ extra.api_example_url }}/panel/subpaas/list?hash=fa7bf873fab9333144e171372a321b06
        ```

#### response

```json
{
  "success": true,
  "list": [
    {
      "subpaas_id": 18,
      "title": "SubppaasTitle",
      "jur_name": "SubppaasJurName",
      "login": "subpaaslogin",
      "creation_date": "2018-11-15",
      "block_type": "NOT_BLOCKED",
      "users_count": 2,
      "active_users_count": 1,
      "trackers_count": 0,
      "active_trackers_count": 0
    }
  ]
}
```

* `list` - array of objects. List of [subpaas objects](#subpaas-object) described above.

#### errors 

* 13 – If the dealer
    * is not paas.
    * has different status than `NOT_BLOCKED`.
    * his tariff doesn't allow subpaases.

### read

Gets subpaas info by its id.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| subpaas_id | Subpaas id. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/subpaas/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "subpaas_id": 97834}'
        
    === "HTTP GET"
    
        ```
        {{ extra.api_example_url }}/panel/subpaas/read?hash=fa7bf873fab9333144e171372a321b06&subpaas_id=97834
        ```

#### response

```json
{
  "success": true,
  "value": {
    "subpaas_id": 18,
    "block_type": "NOT_BLOCKED",
    "title": "Rus Sub-PaaS",
    "jur_name": "OOO Sub-PaaS",
    "email": "sub-dealer@email.com",
    "jur_country": "country",
    "link_monitoring": "link",
    "contact_fio": "fio",
    "contact_post": "post",
    "contact_phone": "phone"
  }
}
```

* `value` - [subpaas object](#subpaas-object) described above.

#### errors

* 13 – If the dealer
    * is not paas.
    * has different status than `NOT_BLOCKED`.
    * his tariff doesn't allow subpaases.
    
### update

Updates a subpaas with specified id.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| subpaas_id | Subpaas's id. | int |
| password | Subpaas's password. | string |
| title | Subpaas's name. | string |
| email | Company email. | string |
| jur_name | Legal (juristic) company name. | string |
| jur_country | Subpaas's country | string |
| link_monitoring | Subpaas's domain name. | string |
| contact_fio | Contact person. | string |
| contact_post | Contact post (position). | string |
| contact_phone | Contact's phone. | string |
| block_type | Panel and PaaS users block status. One of: "NOT_BLOCKED", "INITIAL_BLOCK", "BLOCK_LOGIN" or "CLIENTS_BLOCKED". | [enum](../../../backend-api/getting-started.md#data-types) |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/subpaas/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "password": "B1r7d@Y", "title": "Company", "email": "email@company.com", "jur_name": "Company", "jur_country": "Finland", "link_monitoring": "company.com", "contact_fio": "fio", "contact_post": "CEO", "contact_phone": "79999902190", "block_type": "NOT_BLOCKED"}'

#### response

```json
{
    "success": true
}
```

#### errors

* 13 –
    * The dealer is not paas.
    * The dealer has different status than `NOT_BLOCKED`.
    * Subpaases are not permitted for dealer.
    * `block_type` is `DELETED`.
    * Found subpaas is in `DELETED` status.
    * Found subpaas is not in `INITIAL_BLOCK` status and `block_type` is `INITIAL_BLOCK`.
    * Found subpaas is in `INITIAL_BLOCK` status and `block_type` is not `INITIAL_BLOCK`.