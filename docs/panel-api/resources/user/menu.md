---
title: Customizable user menu
description: It contains calls to customize user menus.
---

# Customizable user menu

Menu customization allows you to customize which sections will be available to all PaaS users or some specific ones.

## Entity description

For now, menu customization is only available for one application.

#### navixy_web:

Menu description for Navixy Web UI.

```json
{
  "application": "navixy_web",
  "account_menu": [
    {
      "name": "subusers"
    },
    {
      "name": "info"
    },
    {
      "name": "bills"
    },
    {
      "name": "entities"
    },
    {
      "name": "auth-journal"
    },
    {
      "name": "plugins"
    },
    {
      "name": "tags"
    }
  ],
  "main_menu": [
    {
      "name": "online_main",
      "items": [
        {
          "name": "online"
        },
        {
          "name": "mix"
        }
      ]
    },
    {
      "name": "reports_main",
      "items": [
        {
          "name": "reports"
        },
        {
          "name": "schedule"
        }
      ]
    },
    {
      "name": "fleet_main",
      "items": [
        {
          "name": "fleet"
        },
        {
          "name": "fleet_app"
        },
        {
          "name": "fleetStaff"
        },
        {
          "name": "driver_journal"
        },
        {
          "name": "driver_skills"
        },
        {
          "name": "service_works"
        }
      ]
    },
    {
      "name": "tasks_main",
      "items": [
        {
          "name": "tasks"
        },
        {
          "name": "tasks_app"
        },
        {
          "name": "templates"
        },
        {
          "name": "forms"
        },
        {
          "name": "places"
        },
        {
          "name": "staff"
        },
        {
          "name": "departments"
        },
        {
          "name": "process"
        },
        {
          "name": "oldTasks"
        }
      ]
    },
    {
      "name": "applications"
    }
  ],
  "footer_menu": [
    {
      "name": "registration"
    },
    {
      "name": "chat"
    },
    {
      "name": "notifications"
    },
    {
      "name": "configuration"
    },
    {
      "name": "help"
    },
    {
      "name": "chat_support"
    }
  ]
}
```

## API actions

API base path: `panel/user/menu`

### read

Reads the menu description specified for a particular user.

#### parameters

| name        | description                         | type   |
|:------------|:------------------------------------|:-------|
| user_id     | ID of a user (required master user) | int    |
| application | Application ID, e.g. "navixy_web"   | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/menu/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "user_id": 231432, "application": "navixy_web"}'
    ```

#### response

```json
{
  "success": true,
  "value": <customizable_user_menu>
}
```

#### errors

* 201 – Not found in the database - if a master user not found.

### update

Updates the menu description specified for a particular user. 

#### parameters

| name    | description                         | type        |
|:--------|:------------------------------------|:------------|
| user_id | ID of a user (required master user) | int         |
| value   | A new value of menu description     | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/menu/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "user_id": 231432, "value": {"application":"navixy_web","account_menu":[],"main_menu":[],"footer_menu":[]}}'
    ```

#### response

```json
{
  "success": true
}
```

#### errors

* 201 – Not found in the database - if a master user not found.

### default/read

Reads the default menu description for all users.

#### parameters

| name        | description                       | type   |
|:------------|:----------------------------------|:-------|
| application | Application ID, e.g. "navixy_web" | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/menu/default/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "application": "navixy_web"}'
    ```

#### response

```json
{
  "success": true,
  "value": <customizable_user_menu>
}
```

### default/update

Updates the default menu description for all users.

#### parameters

| name    | description                     | type        |
|:--------|:--------------------------------|:------------|
| value   | A new value of menu description | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/menu/default/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "value": {"application":"navixy_web","account_menu":[],"main_menu":[],"footer_menu":[]}}'
    ```

#### response

```json
{
  "success": true
}
```
