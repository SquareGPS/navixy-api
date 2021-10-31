---
title: Account
description: API calls on getting the panel's hash, getting permissions and logout.
---

# Account

API calls on getting the panel's hash, getting permissions and logout.

***

## API actions

API path: `panel/account`.

### auth

Does not require session hash and does not need any permissions. Auths dealer in a panel (planned also for dealer's "sub-users")
 and gets hash. 

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| login | A panel's login (number). | string |
| password | A panel's password. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/account/auth' \
        -H 'Content-Type: application/json' \ 
        -d '{"login": "20410", "password": "12f@14Y$"}'
    ```

#### response

```json
{
    "hash": "fa7bf873fab9333144e171372a321b06",
    "success": true,
    "permissions": {
        "base": [
            "get_dealer_info"
        ],
        "service_settings": [
            "read",
            "update"
        ],
        "notification_settings": [
            "read",
            "update"
        ],
        "trackers": [
            "corrupt",
            "create",
            "delete",
            "global",
            "read",
            "report",
            "update"
        ],
        "users": [
            "corrupt",
            "create",
            "read",
            "update"
        ],
        "user_sessions": [
            "create"
        ],
        "tariffs": [
            "create",
            "read",
            "update"
        ],
        "transactions": [
            "create",
            "read"
        ],
        "activation_code": [
            "read",
            "update"
        ],
        "password": [
            "update"
        ],
        "email_gateways": [
            "create",
            "delete",
            "read",
            "send_email",
            "update"
        ],
        "subpaas": [
            "create",
            "delete",
            "read",
            "update"
        ]
    }
}
```

* `hash` - string. A session key.
* `permissions` - object representing permissions for the panel. See panel account [permissions](../getting-started.md#panel-api-permissions).
    
#### errors

* 11 - Access denied - if dealer blocked.
* 12 - Dealer not found.

***

### get_permissions

Returns permissions for current panel session. 

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/account/get_permissions' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/account/get_permissions?hash=fa7bf873fab9333144e171372a321b06
    ```

#### response

```json
{
    "success": true,
    "permissions": {
        "base": [
            "get_dealer_info"
        ],
        "service_settings": [
            "read",
            "update"
        ],
        "notification_settings": [
            "read",
            "update"
        ],
        "trackers": [
            "corrupt",
            "create",
            "delete",
            "global",
            "read",
            "report",
            "update"
        ],
        "users": [
            "corrupt",
            "create",
            "read",
            "update"
        ],
        "user_sessions": [
            "create"
        ],
        "tariffs": [
            "create",
            "read",
            "update"
        ],
        "transactions": [
            "create",
            "read"
        ],
        "activation_code": [
            "read",
            "update"
        ],
        "password": [
            "update"
        ],
        "email_gateways": [
            "create",
            "delete",
            "read",
            "send_email",
            "update"
        ],
        "subpaas": [
            "create",
            "delete",
            "read",
            "update"
        ]
    }
}
```

#### errors

[General](../../backend-api/getting-started.md#error-codes) types only.

***

### logout

Ends the current session.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/account/logout' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/account/logout?hash=fa7bf873fab9333144e171372a321b06
    ```

#### response

```json
{
    "success": true
}
```

#### errors

[General](../../backend-api/getting-started.md#error-codes) types only.