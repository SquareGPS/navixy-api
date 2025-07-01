---
description: API calls to interact with Subpaases.
---

# Subpaas

## Subdealer (Sub PaaS) actions

IIn Navixy, a Subdealer (Sub PaaS) account is designed for dealers who need to manage multiple accounts that provide services independently. This feature is ideal for dealers who act as larger distributors or service providers. With Sub PaaS accounts, dealers can create and manage additional sub-accounts, each with its own users, devices, and settings.

These sub-accounts function similarly to the main dealer account but allow for more granular control and management. This setup is perfect for servicing other dealers (subdealers) or larger enterprises that require separate PaaS accounts, such as a service run on their own domain. It streamlines operations of multiple independent organizations, while maintaining oversight from the main dealer account.

## Subdealer (Sub PaaS) object

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

* `subpaas_id` - int. SubPaas id.
* `title` - string. SubPaas' name.
* `jur_name` - string. Legal company name.
* `creation_date` - string. Creation date.
* `block_type` - [enum](../../../user-api/backend-api/#data-types). Panel and Subpaas' users block status. One of:\
  "NOT\_BLOCKED", "INITIAL\_BLOCK", "BLOCK\_LOGIN" or "CLIENTS\_BLOCKED".
* `users_count` - int. Count of users.
* `active_users_count` - int. Count of active users.
* `trackers_count` - int. All devices of SubPaas.
* `active_trackers_count` - int. Active devices of SubPaas.
* `contact_fio` - string. Contact person.
* `contact_post` - string. Contact post (position).
* `contact_phone` - string. Contact's phone.

## API actions

API base path: `panel/subpaas`.

### create

Creates a subPaaS. After creation, its `dealer_block_type` will be in `INITIAL_BLOCK` status.

#### Parameters

| name             | description           | type   |
| ---------------- | --------------------- | ------ |
| password         | Subpaas' password.    | string |
| title            | Subpaas' name.        | string |
| email            | Company email.        | string |
| jur\_name        | Legal company name.   | string |
| jur\_country     | Subpaas' country      | string |
| link\_monitoring | Subpaas' domain name. | string |

#### Example

cURL

{% code overflow="wrap" %}
```sh
curl -X POST '{{ extra.api_example_url }}/panel/subpaas/create' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "fa7bf873fab9333144e171372a321b06", "password": "B1r7d@Y", "title": "Company", "email": "email@company.com", "jur_name": "Company", "jur_country": "Finland", "link_monitoring": "company.com"}'
```
{% endcode %}

#### Response

```json
{
  "success": true
}
```

#### Errors

* 13 – If the dealer
  * is not paas.
  * has different status than `NOT_BLOCKED`.
  * his tariff doesn't allow subpaases.

### list

Gets a list of all SubPaaS accounts of a Dealer. Dealer ID will be taken from the session key.

#### Parameters

| name      | description                                                                                                                           | type                                              |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| order\_by | Optional. Sort option. Can be "subpaas\_id", "title", "jur\_name", "login", "block\_type", "creation\_date". Default is `subpaas_id`. | [enum](../../../user-api/backend-api/#data-types) |
| ascending | Optional. If `true` ordering will be ascending, descending otherwise. Default is `true`.                                              | boolean                                           |
| limit     | Optional. Pagination. Maximum subpaases to return                                                                                     | int                                               |
| offset    | Optional. Pagination. Get subpaases starting from.                                                                                    | int                                               |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST '{{ extra.api_example_url }}/panel/subpaas/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
{{ extra.api_example_url }}/panel/subpaas/list?hash=fa7bf873fab9333144e171372a321b06
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

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

* `list` - array of objects. List of [subpaas objects](./#subdealer-sub-paas-object) described above.

#### Errors

* 13 – If the dealer:
  * is not of the PaaS type.
  * has a status other than `NOT_BLOCKED`.
  * their plan does not allow SubPaaS accounts.

### read

Gets Sub PaaS account info by its id.

#### Parameters

| name        | description | type |
| ----------- | ----------- | ---- |
| subpaas\_id | Subpaas ID. | int  |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST '{{ extra.api_example_url }}/panel/subpaas/read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "fa7bf873fab9333144e171372a321b06", "subpaas_id": 97834}' 
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
{{ extra.api_example_url }}/panel/subpaas/read?hash=fa7bf873fab9333144e171372a321b06&subpaas_id=97834
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

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

* `value` - [subpaas object](./#subdealer-sub-paas-object) described above.

#### Errors

* 13 – If the dealer:
  * is not of the PaaS type.
  * has a status other than `NOT_BLOCKED`.
  * their plan does not allow SubPaaS accounts.

### update

Updates a SubPaas account with the specified ID.

#### Parameters

| name             | description                                                                                                        | type                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| subpaas\_id      | Subpaas' ID.                                                                                                       | int                                               |
| password         | Subpaas' password.                                                                                                 | string                                            |
| title            | Subpaas' name.                                                                                                     | string                                            |
| email            | Company email.                                                                                                     | string                                            |
| jur\_name        | Legal (juristic) company name.                                                                                     | string                                            |
| jur\_country     | Subpaas' country                                                                                                   | string                                            |
| link\_monitoring | Subpaas' domain name.                                                                                              | string                                            |
| contact\_fio     | Contact person.                                                                                                    | string                                            |
| contact\_post    | Contact post (position).                                                                                           | string                                            |
| contact\_phone   | Contact's phone.                                                                                                   | string                                            |
| block\_type      | Panel and PaaS users block status. One of: "NOT\_BLOCKED", "INITIAL\_BLOCK", "BLOCK\_LOGIN" or "CLIENTS\_BLOCKED". | [enum](../../../user-api/backend-api/#data-types) |

#### Example

cURL

{% code overflow="wrap" %}
```sh
curl -X POST '{{ extra.api_example_url }}/panel/subpaas/create' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "fa7bf873fab9333144e171372a321b06", "password": "B1r7d@Y", "title": "Company", "email": "email@company.com", "jur_name": "Company", "jur_country": "Finland", "link_monitoring": "company.com", "contact_fio": "fio", "contact_post": "CEO", "contact_phone": "79999902190", "block_type": "NOT_BLOCKED"}'
```
{% endcode %}

#### Response

```json
{
  "success": true
}
```

#### Errors

* 13 –
  * The dealer is not PaaS.
  * The dealer has a status other than `NOT_BLOCKED`.
  * SubPaaS accounts are not permitted for the dealer.
  * `block_type` is `DELETED`.
  * The found SubPaaS is in `DELETED` status.
  * The found SubPaaS is not in `INITIAL_BLOCK` status and `block_type` is `INITIAL_BLOCK`.
  * The found SubPaaS is in `INITIAL_BLOCK` status and `block_type` is not `INITIAL_BLOCK`.
