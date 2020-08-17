---
title: Form templates
description: Form templates
---

Form is a "one-shot" entity; after it was filled by someone, it cannot be reused. It's stored along with filled fields 
for future reference. Usually people need to fill forms with the same fields over an over again, so forms are created on
 the basis of form templates. It's similar to paper forms: each paper form can be filled only once, but there's an 
 electronic document, a template, on basis of which all paper forms are printed.  
 
 The reason for such API design is that template fields can be changed over time (deleted, removed, reordered, etc)  
 and it should not affect already filled forms. By separating filled forms and templates, one can always view filled form 
 in exactly same state regardless of how template changed.
 
User can assign form to the task or checkin by choosing template without the need to create all form fields every time.

`<form_template>` is:
```js
{
  "id": 1,
  "label": "Order form", //user-defined form label, from 1 to 100 characters
  "fields": [
    //multiple <form_field> objects can be here
  ],
  "created": "2017-03-15 12:36:27", //date when this template was created. Read-only field
  "submit_in_zone": true, //if true, form can be submitted only in task zone
  "updated": "2017-03-16 15:22:53", //date when this template was last modified. Read-only field
  "default": false //if true,
}
```

# API actions

API base path: `/form/template`.

## list

Get all form templates belonging to current master user.

#### parameters

none

#### return

```js
{
    "success": true,
    "list":[...] //ordered array of <form_template> objects
}
```

#### errors

no specific errors

## create

Create new form template.

**required subuser rights**: form\_template\_update

#### parameters

*   **template** – Non-null <form_template>.

#### return

```js
{
    "success": true,
    "id": 111 //id of the created form template
}
```

#### errors

*   101 – In demo mode this function is disabled (if current user has “demo” flag)


## read

Get form template belonging to current master user by id.

#### parameters

*   **template_id** – Id of the form template, int.

#### return

```js
{
    "success": true,
    "list":[...] //ordered array of <form_template> objects
}
```

#### errors

*   201 – Not found in database (if there is no template with such id)


## update

Update existing form template.

**required subuser rights**: form\_template\_update

#### parameters

*   **template** – Non-null.

#### return

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (if template with the specified id does not exist)
*   101 – In demo mode this function is disabled (if current user has “demo” flag)


## delete

Delete form template.

**required subuser rights**: form\_template\_update

#### parameters

*   **template_id** – Id of the form template, int.

#### return

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (if template with the specified id does not exist)
*   101 – In demo mode this function is disabled (if current user has “demo” flag)


## stats/read

Return template usage statistics

**required subuser rights**: –

#### parameters

*   **template_id** – Id of the form template, int.

#### return

```js
{
  "success": true,
  "tasks": { // maps task status to number of tasks with this status which use specified template
    "unassigned": 0,
    "assigned": 6,
    "done": 0,
    "failed": 0,
    "delayed": 9,
    "arrived": 0,
    "faulty": 0
  },
  "scheduled": 2 // number of task schedules using this template
}
```

#### errors

*   201 – Not found in database (if template with the specified id does not exist)
