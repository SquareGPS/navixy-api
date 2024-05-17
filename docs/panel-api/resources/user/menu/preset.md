---
title: Menu preset
description: API calls to work with user menu presets.
---

# Menu preset

API calls to work with user menu presets.

## Entity description

Menu presets allows you to customize sidebar user menu and assign these presets to users.

### MenuPreset

| Name   | Description                             | Type            |
|--------|-----------------------------------------|-----------------|
| id     | An identifier for the preset            | int             |
| title  | The title of the preset in the editor   | string          |
| main   | A list of item groups in the sidebar    | MenuGroup array |
| footer | A list of items in the sidebar's footer | MenuItem array  |

### MenuGroup

| Name  | Description              | Type           |
|-------|--------------------------|----------------|
| title | The title of the group   | string?        |
| items | A list of the menu items | MenuItem array |

### MenuItem

| Name  | Description                 | Type          |
|-------|-----------------------------|---------------|
| title | The title of the menu item  | string        |
| icon  | The icon of the menu item   | string?       |
| tabs  | A list of tabs in this item | MenuTab array |

### MenuTab

| Name        | Description                | Type   |
|-------------|----------------------------|--------|
| title       | The title of the tab       | string |
| destination | The destination of the tab | string |

### MenuPresetAssignment

| Name | Description                               | Type                     |
|------|-------------------------------------------|--------------------------|
| type | Assignment type                           | MenuPresetAssignmentType |
| ids  | User ids to assign to (if type = "users") | int array                |

### MenuPresetAssignmentType

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
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
        -H 'Content-Type: application/json'
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
                    "title": "common.menu.location_links"
                  }
                ],
                "title": "common.menu.location_links"
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
                  }
                ],
                "title": "common.menu.reports"
              }
            ],
            "title": null
          }, {
            "items": [
              {
                "icon": "task",
                "tabs": [
                  {
                    "destination": "tasks",
                    "title": "common.menu.tasks"
                  }, {
                    "destination": "task_schedules",
                    "title": "common.menu.task_schedules"
                  }, {
                    "destination": "forms",
                    "title": "common.menu.forms"
                  }, {
                    "destination": "task_courier",
                    "title": "common.menu.task_courier"
                  }
                ],
                "title": "common.menu.tasks"
              }
            ],
            "title": null
          }, {
            "items": [
              {
                "icon": null,
                "tabs": [
                  {
                    "destination": "places",
                    "title": "common.menu.places"
                  }
                ],
                "title": "common.menu.places"
              }
            ],
            "title": null
          }
        ],
        "footer": [
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
          }
        ]
      }
    }
  ]
}
```

#### ListItem

| Name        | Description                         | Type                       |
|-------------|-------------------------------------|----------------------------|
| preset      | An instance of MenuPreset           | MenuPreset                 |
| owner       | The owner of the preset             | PresetOwner                |
| assignments | A set of assignments for the preset | MenuPresetAssignment array |

#### PresetOwner

| Name     | Description             |
|----------|-------------------------|
| platform | Default platform preset |
| dealer   | Created by dealer       |

### create

Creates given menu preset.

#### Parameters

| Name   | Description          | Type       |
|--------|----------------------|------------|
| preset | New preset structure | MenuPreset |

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

| Name   | Description                                                      | Type       |
|--------|------------------------------------------------------------------|------------|
| preset | New preset structure with id of the existing preset to overwrite | MenuPreset |

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
* 201 – Not found in the database - if preset with given id not found.

### delete

Updates the menu preset.

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

* 201 – Not found in the database - if preset with given id not found.

### assign

Updates the menu preset.

#### Parameters

| Name      | Description         | Type                 |
|-----------|---------------------|----------------------|
| preset_id | Preset id to assign | int                  |
| target    | The assignment      | MenuPresetAssignment |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/menu/preset/assign' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
        -H "Content-Type: application/json" \
        -d '{ "presetId": 2, "target": { "type": "users", "ids": [3] } }'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 7 – Invalid parameters - invalid request structure (see error description for details).
* 201 – Not found in the database - if preset with given id not found.

### items/list

Lists all available menu items.

#### Example

=== "cURL"

    ```shell
    curl -X GET '{{ extra.api_example_url }}/panel/user/menu/preset/items/list' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
        -H 'Content-Type: application/json'
    ```

#### Response

```json
{
  "success": true,
  "list": [
    { "title": "common.menu.dashboard", "destination": "dashboard" },
    { "title": "common.menu.tracking", "destination": "tracking" },
    { "title": "common.menu.location_links", "destination": "location_links" },
    { "title": "common.menu.reports", "destination": "reports" },
    { "title": "common.menu.report_schedules", "destination": "report_schedules" },
    { "title": "common.menu.fleet", "destination": "fleet" },
    { "title": "common.menu.garages", "destination": "garages" },
    { "title": "common.menu.service_tasks", "destination": "service_tasks" },
    { "title": "common.menu.staff", "destination": "staff" },
    { "title": "common.menu.departments", "destination": "departments" },
    { "title": "common.menu.driver_journal", "destination": "driver_journal" },
    { "title": "common.menu.driver_skills", "destination": "driver_skills" },
    { "title": "common.menu.tasks", "destination": "tasks" },
    { "title": "common.menu.task_schedules", "destination": "task_schedules" },
    { "title": "common.menu.forms", "destination": "forms" },
    { "title": "common.menu.task_courier", "destination": "task_courier" },
    { "title": "common.menu.places", "destination": "places" },
    { "title": "common.menu.notifications", "destination": "notifications" },
    { "title": "common.menu.chat", "destination": "chat" },
    { "title": "common.menu.device_activation", "destination": "device_activation" },
    { "title": "common.menu.device_settings", "destination": "device_settings" }
  ]
}
```
