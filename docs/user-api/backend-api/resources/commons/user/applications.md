---
title: User Applications
description: API calls to work with user applications.
---

# User Applications

API calls to work with user applications.

### `/user/application/list`

Lists all existing user applications.

#### Response

```json
{
  "success": true,
  "list": [
    {
      "id": 221,
      "label": "An application",
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

* `list` - array of [Application](#application). Unique ID of the created application.

##### Application

* `id` - int. Application's ID.
* `label` - string. Application's name.
* `url_template` - string. [URL template (including variables)](https://en.wikipedia.org/wiki/URI_Template).
* `enabled` - boolean. Determines visibility in the users' side menu. `true` by default.
* `authorization` - [Application authorization](#application-authorization).
  Authorization that will be used while accessing the URL.
  User session by default.
* `display_method` - [Display method](#display-method).
  Determines how the application will be opened.
  `new_tab` by default.
* `icon` - string. Application's icon identifier. `extension` by default.
* `description` - string. Longer plain text description is shown to users. Empty by default.

##### Application authorization

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

* `new_tab` - the application will be opened in a new tab.
* `embedded` - the application page will be embedded into the platform UI.

### `/user/application/create`

Creates a new application.

#### Parameters

| name        | description            | type                              |
|:------------|:-----------------------|:----------------------------------|
| application | Application to create. | [Create request](#create-request) |

##### Create request

| name           | description                                              | type                                                    |
|:---------------|:---------------------------------------------------------|:--------------------------------------------------------|
| label          | Application's name.                                      | string                                                  |
| url_template   | URL template (including variables).                      | string                                                  |
| authorization  | Authorization that will be used while accessing the URL. | [Application authorization](#application-authorization) |
| display_method | Determines how the application will be opened.           | [Display method](#display-method)                       |
| icon           | Application's icon identifier.                           | string                                                  |
| description    | Longer plain text description is shown to users.         | string                                                  |

#### Response

```json
{
  "success": true,
  "id": 779
}
```

* `id` - integer. Unique ID of the created application.

### `/user/application/update`

Updates an existing application.

#### Parameters

| name        | description          | type                        |
|:------------|:---------------------|:----------------------------|
| application | Updated application. | [Application](#application) |

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Application not found.

### `/user/application/delete`

Deletes a specified application by its unique identifier.

#### Parameters

| name           | description                 | type    |
|:---------------|:----------------------------|:--------|
| application_id | Application's id to delete. | integer |

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Application not found.

### `/user/application/enabled/set`

Toggles application visibility in the side menu.

#### Parameters

| name           | description                 | type    |
|:---------------|:----------------------------|:--------|
| application_id | Application's id to update. | integer |
| enabled        | State to set.               | boolean |

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Application not found.
