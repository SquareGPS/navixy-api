---
title: Menu preset
description: API calls to work with user menu presets.
---

# Menu preset

API calls to work with the customizable sidebar structure for end users.
Customizable sidebar allows you to create flexible user menus by adding, rearranging, and renaming menu items and tabs.
Menu presets act as templates that can be assigned to users.

## Entity description

### Menu preset

A template that includes a specific set of menu items, organized into groups and footer items.

| Name   | Description                             | Type                            |
|--------|-----------------------------------------|---------------------------------|
| id     | An identifier for the preset            | int                             |
| title  | The title of the preset in the editor   | string                          |
| main   | A list of item groups in the sidebar    | [Menu group](#menu-group) array |
| footer | A list of items in the sidebar's footer | [Menu item](#menu-item) array   |

### Menu group

A collection of menu items, optionally titled, that are grouped together within the sidebar.

| Name  | Description              | Type                          |
|-------|--------------------------|-------------------------------|
| title | The title of the group   | optional string               |
| items | A list of the menu items | [Menu item](#menu-item) array |

### Menu item

An individual item in the sidebar, which can include an icon and a list of tabs.

| Name  | Description                 | Type                        |
|-------|-----------------------------|-----------------------------|
| title | The title of the menu item  | string                      |
| icon  | The icon of the menu item   | optional string             |
| tabs  | A list of tabs in this item | [Menu tab](#menu-tab) array |

### Menu tab

A subitem within a menu item, providing additional navigation to specific sections or functionalities.

| Name        | Description                | Type   |
|-------------|----------------------------|--------|
| title       | The title of the tab       | string |
| destination | The destination of the tab | string |

### Menu preset assignment

Specifies how a menu preset is assigned to users.
It can be set as a default for all users or targeted to specific user IDs,
allowing for users to have different menu configurations.

| Name | Description                               | Type                                                        |
|------|-------------------------------------------|-------------------------------------------------------------|
| type | Assignment type                           | [Menu preset assignment type](#menu-preset-assignment-type) |
| ids  | User ids to assign to (if type = "users") | int array                                                   |

### Menu preset assignment type

Defines the type of assignment for a menu preset, either as a default for all users or for specific user assignments.

| Name    | Description                                                            |
|---------|------------------------------------------------------------------------|
| default | The preset will be used if there's no specific assignment fro the user |
| users   | Assignment for the specified users                                     |

## API actions

API base path: `panel/user/menu`

### list

Lists all available menu presets with their current assignments.

#### Example

=== "cURL"
    ```shell
    curl -X GET '{{ extra.api_example_url }}/panel/user/menu/preset/list' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
    ```

#### Response

```json
{
  "success": true,
  "list": [
    {
      "assignments": [],
      "owner": "platform",
      "preset": {
        "id": 1,
        "title": "common.menu.default.title",
        "main": [
          {
            "items": [
              {
                "icon": "dashboard",
                "tabs": [
                  {
                    "destination": "dashboard",
                    "title": "common.menu.dashboard"
                  }
                ],
                "title": "common.menu.dashboard"
              }
            ],
            "title": null
          }, {
            "items": [
              {
                "icon": "map",
                "tabs": [
                  {
                    "destination": "tracking",
                    "title": "common.menu.tracking"
                  }
                ],
                "title": "common.menu.tracking"
              }, {
                "icon": "share",
                "tabs": [
                  {
                    "destination": "location_links",
                    "title": "common.menu.location-sharing"
                  }
                ],
                "title": "common.menu.location-sharing"
              }
            ],
            "title": null
          }, {
            "items": [
              {
                "icon": "assessment",
                "tabs": [
                  {
                    "destination": "reports",
                    "title": "common.menu.reports"
                  }, {
                    "destination": "report_schedules",
                    "title": "common.menu.schedule"
                  }
                ],
                "title": "common.menu.reports"
              }
            ],
            "title": null
          }, {
            "items": [
              {
                "icon": "directions_car",
                "tabs": [
                  {
                    "destination": "fleet",
                    "title": "common.menu.vehicles"
                  }, {
                    "destination": "garages",
                    "title": "common.menu.garages"
                  }, {
                    "destination": "drivers",
                    "title": "common.menu.drivers"
                  }, {
                    "destination": "driver_departments",
                    "title": "common.menu.departments"
                  }, {
                    "destination": "driver_journal",
                    "title": "common.menu.driver_journal"
                  }, {
                    "destination": "driver_skills",
                    "title": "common.menu.driver_skills"
                  }, {
                    "destination": "service_tasks",
                    "title": "common.menu.service_tasks"
                  }
                ],
                "title": "common.menu.fleet"
              }, {
                "icon": "groups",
                "tabs": [
                  {
                    "destination": "staff",
                    "title": "common.menu.staff"
                  }, {
                    "destination": "tasks",
                    "title": "common.menu.tasks"
                  }, {
                    "destination": "task_schedules",
                    "title": "common.menu.templates"
                  }, {
                    "destination": "forms",
                    "title": "common.menu.forms"
                  }, {
                    "destination": "task_courier",
                    "title": "common.menu.task_courier"
                  }, {
                    "destination": "departments",
                    "title": "common.menu.departments"
                  }, {
                    "destination": "places",
                    "title": "common.menu.places"
                  }
                ],
                "title": "common.menu.field_service"
              }
            ],
            "title": null
          }
        ],
        "footer": {
          "items": [
            {
              "icon": "notifications",
              "tabs": [
                {
                  "destination": "notifications",
                  "title": "common.menu.notifications"
                }
              ],
              "title": "common.menu.notifications"
            }, {
              "icon": "textsms",
              "tabs": [
                {
                  "destination": "chat",
                  "title": "common.menu.chat"
                }
              ],
              "title": "common.menu.chat"
            }, {
              "icon": "custom-icon-add_device",
              "tabs": [
                {
                  "destination": "device_activation",
                  "title": "common.menu.device_activation"
                }
              ],
              "title": "common.menu.device_activation"
            }, {
              "icon": "settings",
              "tabs": [
                {
                  "destination": "device_settings",
                  "title": "common.menu.device_settings"
                }
              ],
              "title": "common.menu.device_settings"
            }, {
              "icon": "help_outline",
              "tabs": [
                {
                  "destination": "feedback",
                  "title": "common.menu.help"
                }
              ],
              "title": "common.menu.help"
            }
          ],
          "title": null
        }
      }
    }
  ]
}
```

#### List item

| Name        | Description                         | Type                                                    |
|-------------|-------------------------------------|---------------------------------------------------------|
| preset      | An instance of menu preset          | [Menu preset](#menu-preset)                             |
| owner       | The owner of the preset             | [Preset owner](#preset-owner)                           |
| assignments | A set of assignments for the preset | [Menu preset assignment](#menu-preset-assignment) array |

#### Preset owner

| Name     | Description             |
|----------|-------------------------|
| platform | Default platform preset |
| dealer   | Created by dealer       |

### create

Creates given menu preset.

#### Parameters

| Name   | Description          | Type                                     |
|--------|----------------------|------------------------------------------|
| preset | New preset structure | [Menu preset](#menu-preset) (without id) |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/menu/preset/create' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
        -H 'Content-Type: application/json' \
        -d '{ "preset": { "title": "Created", "main": [ { "title": "Monitoring", "items": [ { "title": "Tasks", "tabs": [ { "title": "Tasks", "destination": "tasks" } ] } ] } ], "footer": [] } }'
    ```

#### Response

```json
{
  "success": true,
  "id": 2
}
```

#### Errors

* 7 – Invalid parameters - invalid menu preset structure (see error description for details).

### update

Updates the menu preset.

#### Parameters

| Name   | Description                                                      | Type                        |
|--------|------------------------------------------------------------------|-----------------------------|
| preset | New preset structure with id of the existing preset to overwrite | [Menu preset](#menu-preset) |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/menu/preset/update' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
        -H 'Content-Type: application/json' \
        -d '{ "preset": { "id": 2, "title": "Updated", "main": [ { "title": "Monitoring", "items": [ { "title": "Tasks", "tabs": [ { "title": "Tasks", "destination": "tasks" } ] } ] } ], "footer": [] } }'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 7 – Invalid parameters - invalid menu preset structure (see error description for details).
* 201 – Not found in the database — if there is no preset with the specified ID.

### delete

Deletes the menu preset.

#### Parameters

| Name      | Description         | Type |
|-----------|---------------------|------|
| preset_id | preset id to delete | int  |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/menu/preset/delete?preset_id=2' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Not found in the database — if preset with given id not found.

### assign

Assigns the menu preset to users.

#### Parameters

| Name      | Description         | Type                                              |
|-----------|---------------------|---------------------------------------------------|
| preset_id | Preset id to assign | int                                               |
| target    | The assignment      | [Menu preset assignment](#menu-preset-assignment) |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/menu/preset/assign' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
        -H "Content-Type: application/json" \
        -d '{ "preset_id": 2, "target": { "type": "users", "ids": [3] } }'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 7 – Invalid parameters - invalid request structure (see error description for details).
* 201 – Not found in the database — if preset with given id not found.

### items/list

Lists all available menu items.

#### Example

=== "cURL"

    ```shell
    curl -X GET '{{ extra.api_example_url }}/panel/user/menu/preset/items/list' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
    ```

#### Response

```json
[
  { "title": "common.menu.dashboard", "destination": "dashboard" },
  { "title": "common.menu.tracking", "destination": "tracking" },
  { "title": "common.menu.location-sharing", "destination": "location_links" },
  { "title": "common.menu.reports", "destination": "reports" },
  { "title": "common.menu.schedule", "destination": "report_schedules" },
  { "title": "common.menu.vehicles", "destination": "fleet" },
  { "title": "common.menu.garages", "destination": "garages" },
  { "title": "common.menu.drivers", "destination": "drivers" },
  { "title": "common.menu.departments", "destination": "driver_departments" },
  { "title": "common.menu.driver_journal", "destination": "driver_journal" },
  { "title": "common.menu.driver_skills", "destination": "driver_skills" },
  { "title": "common.menu.service_tasks", "destination": "service_tasks" },
  { "title": "common.menu.staff", "destination": "staff" },
  { "title": "common.menu.tasks", "destination": "tasks" },
  { "title": "common.menu.templates", "destination": "task_schedules" },
  { "title": "common.menu.forms", "destination": "forms" },
  { "title": "common.menu.task_courier", "destination": "task_courier" },
  { "title": "common.menu.departments", "destination": "departments" },
  { "title": "common.menu.places", "destination": "places" },
  { "title": "common.menu.notifications", "destination": "notifications" },
  { "title": "common.menu.chat", "destination": "chat" },
  { "title": "common.menu.device_activation", "destination": "device_activation" },
  { "title": "common.menu.device_settings", "destination": "device_settings" },
  { "title": "common.menu.help", "destination": "feedback" }
]
```
