---
title: Contact
description: API call to get user's trackers with special grouping by "contacts"
---
# Contact 

!!! warning "Deprecated"
    This API action deprecated and should not be used.

API call to get user's trackers with special grouping by "contacts"


## API actions

API base path: `/tracker/contact`.

### `list`

Gets all user's trackers with special grouping by "contacts".

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/contact/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/contact/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "contacts": [{<contact1>}, {<contact n>}],
    "trackers": [{<tracker1>}, {<tracker n>}]
}
```

* `contacts` - all established contacts.
* `trackers` - normal trackers belonging to current user.

where `contact` object is:

```json
{
    "user_id": 12059,
    "first_name": "Adam",
    "middle_name": "James",
    "last_name": "Williams",
    "trackers": [{<tracker1>}, {<tracker n>}]
}
```

* `user_id` - ID of the user with which "contact" is established.
* `trackers` - trackers belonging to "contact" which locations shared with current user.
Click to see descriptions of type [tracker](index.md#tracker-object-structure).

#### Errors

* 201 – Not found in the database.
