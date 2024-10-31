---
title: Addons
description: API calls to work with addons.
---

# Addons

API calls to work with addons.

### `/addon/list`

Lists all existing user's addons.

#### Response

```json
{
  "success": true,
  "list": [
    {
      "id": 221,
      "label": "An addon",
      "url_template": "https://domain.example/{language}",
      "enabled": true,
      "authorization": {
        "type": "user_session"
      },
      "display_method": "new_tab",
      "icon": "extension",
      "description": "A description"
    }
  ]
}
```

* `list` - array of [Addon](#addon). Unique ID of the created addon.

##### Addon

* `id` - int. Addon's ID.
* `label` - string. Addon's name.
* `url_template` - string. [URL template (including variables)](https://en.wikipedia.org/wiki/URI_Template).
* `enabled` - boolean. Determines visibility in the users' side menu. `true` by default.
* `authorization` - [Addon authorization](#addon-authorization).
  Authorization that will be used while accessing the URL.
  User session by default.
* `display_method` - [Display method](#display-method).
  Determines how the addon will be opened.
  `new_tab` by default.
* `icon` - string. Addon's icon identifier. `extension` by default.
* `description` - string. Longer plain text description is shown to users. Empty by default.

##### Addon authorization

=== "API key"

    | name | type    | description                    |
    |:-----|:--------|:-------------------------------|
    | type | string  | Always `"api_key"`             |
    | hash | string  | An [API key](api-keys.md) hash |

=== "User session"

    | name | type    | description             |
    |:-----|:--------|:------------------------|
    | type | string  | Always `"user_session"` |

##### Display method

* `new_tab` - the addon will be opened in a new tab.
* `embedded` - the addon page will be embedded into the platform UI.

### `/addon/create`

Creates a new addon.

#### Parameters

| name  | description      | type                              |
|:------|:-----------------|:----------------------------------|
| addon | Addon to create. | [Create request](#create-request) |

##### Create request

| name           | description                                              | type                                        |
|:---------------|:---------------------------------------------------------|:--------------------------------------------|
| label          | Addon's name.                                            | string                                      |
| url_template   | URL template (including variables).                      | string                                      |
| authorization  | Authorization that will be used while accessing the URL. | [Addon authorization](#addon-authorization) |
| display_method | Determines how the addon will be opened.                 | [Display method](#display-method)           |
| icon           | Addon's icon identifier.                                 | string                                      |
| description    | Longer plain text description is shown to users.         | string                                      |

#### Response

```json
{
  "success": true,
  "id": 779
}
```

* `id` - integer. Unique ID of the created addon.

### `/addon/update`

Updates an existing addon.

#### Parameters

| name  | description    | type            |
|:------|:---------------|:----------------|
| addon | Updated addon. | [Addon](#addon) |

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Addon not found.

### `/addon/delete`

Deletes a specified addon by its unique identifier.

#### Parameters

| name     | description           | type    |
|:---------|:----------------------|:--------|
| addon_id | Addon's id to delete. | integer |

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Addon not found.

### `/addon/enabled/set`

Toggles addon visibility in the side menu.

#### Parameters

| name     | description           | type    |
|:---------|:----------------------|:--------|
| addon_id | Addon's id to update. | integer |
| enabled  | State to set.         | boolean |

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Addon not found.
