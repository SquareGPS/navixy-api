---
title: Retranslator
description: Retranslator
---

# Retranslator

Retranslator and retranslator protocol objects and CRUD actions for retranslators. They can be used to redirect the data
that comes from a device to the platform to some third-party application specified by the user.


## Retranslator protocol object
 
```json
{
    "id": 123456,
    "name": "protocol",
    "has_login": true,
    "has_password": false,
    "fake_device_id_pattern": "id_pattern",
    "required_login": true,
    "required_password": false
}
```

* `id` - int. Protocol ID.
* `name` - string. Protocol name.
* `has_login` - boolean. `true` if this protocol use login.
* `has_password` - boolean. `true` if this protocol use password.
* `fake_device_id_pattern` - optional string. Regex pattern for `fake_device_id` validation.
* `required_login` - boolean. `true` if for this protocol login required.
* `required_password` - boolean. `true` if for this protocol password required.


## Retranslator object

```json
{
    "id": 1,
    "name": "Some server",
    "protocol_id": 123456,
    "address": "127.0.0.1",
    "port": 15000,
    "login": "login",
    "password": "password",
    "enabled": true
}
```

* `id` - int. Retranslator ID.
* `name` - string. Zone label.
* `protocol_id` - int. Protocol ID.
* `address` - string. Network address, e.g. `127.0.0.1` or `localhost`.
* `port` - int. Port number.
* `login` - optional string.
* `password` - optional string.
* `enabled` - boolean. Status.


## API actions

API path: `/retranslator`.

### `create`

Creates new retranslator.

**required sub-user rights**: `admin` (available only to master users).

#### Parameters

| name         | description                             | type        |
|:-------------|:----------------------------------------|:------------|
| retranslator | Retranslator object without `id` field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/retranslator/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "retranslator": {"name": "Some server", "protocol_id": 123456, "address": "127.0.0.1", "port": 15000, "login": "proto", "password": "qewtyr", "enabled": true}}'
    ```

#### Response

```json
{
    "success": true,
    "id": 123456
}
```

* `id` - int. ID of the created retranslator.

#### Errors

* 247 - Entity already exists - if retranslator with this address, port and login already exists.
* 7 - Invalid parameters - if retranslator have required fields (login or password), but was send empty.
* 268 - Over quota – if the user's quota for retranslators exceeded.


### `delete`

Deletes user's retranslator with specified `retranslator_id`.

**required sub-user rights**: `admin` (available only to master users).

#### Parameters

| name            | description                                  | type | format |
|:----------------|:---------------------------------------------|:-----|:-------|
| retranslator_id | ID of the retranslator that will be deleted. | int  | 123456 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/retranslator/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "retranslator_id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/retranslator/delete?hash=a6aa75587e5c59c32d347da438505fc3&retranslator_id=123456
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database.


### `list`

Get all users' retranslators.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/retranslator/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/retranslator/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```
    
#### Response

```json
{
    "success": true,
    "list": [{
      "id": 1,
      "name": "Some server",
      "protocol_id": 123456,
      "address": "127.0.0.1",
      "port": 15000,
      "login": "login",
      "password": "password",
      "enabled": true
    }]
}
```

* `id` - int. Retranslator ID.
* `name` - string. Zone label.
* `protocol_id` - int. Protocol ID.
* `address` - string. Network address, e.g. `127.0.0.1` or `localhost`.
* `port` - int. Port number.
* `login` - optional string.
* `password` - optional string.
* `enabled` - boolean. Status.


### `update`

Updates retranslator parameters for the specified retranslator. Note that retranslator must exist, and must belong to 
the current user.

**required sub-user rights**: `admin` (available only to master users).

#### Parameters

| name         | description                             | type        |
|:-------------|:----------------------------------------|:------------|
| retranslator | Retranslator object without `id` field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/retranslator/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "retranslator": {"name": "Some server", "protocol_id": 123456, "address": "127.0.0.1", "port": 15000, "login": "proto", "password": "qewtyr", "enabled": true}}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if retranslator with the specified ID cannot be found or belongs to another user.
* 247 - Entity already exists – if retranslator with this address, port and login already exists.


### `protocol/list`

Returns all available retranslator protocols.

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/retranslator/protocol/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/retranslator/protocol/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list": [{
      "id": 123456,
      "name": "protocol",
      "has_login": true,
      "has_password": false,
      "fake_device_id_pattern": "id_pattern",
      "required_login": true,
      "required_password": false
    }]
}
```

* `id` - int. Protocol ID.
* `name` - string. Protocol name.
* `has_login` - boolean. `true` if this protocol use login.
* `has_password` - boolean. `true` if this protocol use password.
* `fake_device_id_pattern` - optional string. Regex pattern for `fake_device_id` validation.
* `required_login` - boolean. `true` if for this protocol login required.
* `required_password` - boolean. `true` if for this protocol password required.
