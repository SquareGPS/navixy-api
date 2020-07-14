---
title: /tag
description: /tag
---

# tag/

#### tag object

    <tag> =
       {
          "id": 3,
          "avatar_file_name": "asdf.jpg",
          "name": "hop",
          "color": "FF0000"
        }

#### tagged entity types
*   place
*   task
*   task_schedule
*   employee
*   vehicle



---
## create(…)
Create new tag.

**required subuser rights**: tag_update

#### parameters:
* **tag** - JSON object.

#### return:
```js
{
    "success": true,
    "id": 111 //id of the created tag
}
```

#### errors:
general types only



---
## delete(…)
Delete tag with the specified id.

**required subuser rights**: tag_update

#### parameters:
* **tag_id** - (int) id of the tag to delete.

#### return:
```js
{
    "success": true
}
```

#### errors:
* 201 – Not found in database (if there is no tag with such id)



---
## list(…)
Get all tags belonging to user with optional filtering.

#### parameters:
* **filter** - (string) optional filter for tag name, 3-60 characters or null.

#### return:
```js
{
    "success": true,
    "list": [ <tag>, ... ]
}
```

#### errors:
general types only



---
## search(…)
Search entities that bound with specified tags.

#### parameters:
* **tag_ids** - (Array or int) tag IDs.
* **entity_types** - (Array of [tagged entity types](#tag)) optional, filter for entity types.

#### return:
```js
{
    "success": true,
    "result": {
      "place": [...], //array of place objects
      "task": [...], //array of task objects
      "task_schedule": [...], //array of task schedule objects
      "employee": [...], //array of employee objects
      "vehicle": [...] //array of vehicle objects
    }
}
```

#### errors:
general types only



---
## update(…)
Update existing tag.

**required subuser rights**: tag_update

#### parameters:
* **tag** - JSON object.

#### return:
```js
{
    "success": true
}
```

#### errors:
* 201 – Not found in database (if there is no tag with such id)
