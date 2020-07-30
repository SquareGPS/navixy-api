---
title: Garage
description: Garage
---

# Garage

API path: `/garage`.

    <garage> =
       {
            "id": 222, <int>
            "location": { //valid location or null
                "lat": 40.4,
                "lng": -3.6,
                "address": "Calle Salitre, 58",
                "radius": 150
            },
            "mechanic_name": "Martinez",
            "dispatcher_name": "Velasquez",
            "organization_name": "Bankia"
        }

## list()

Get all garages belonging to user.

#### return

```js
{
    "success": true,
    "list": [ <garage>, ... ]
}
```
    

#### errors

general types only



## create()

Create new garage.

**required subuser rights**: vehicle_update

#### parameters

*   **garage** – an [garage object](#garage) Non-null.

#### return

```js
{
    "success": true,
    "id": 111 //id of the created garage
}
```

#### errors

general types only



## update()

Update existing garage.

**required subuser rights**: vehicle_update

#### parameters

*   **garage** – an [garage object](#garage) Non-null.

#### return

```json
{ "success": true }
```


#### errors

*   201 – Not found in database (if there is no garage with such id)


## delete()
Delete garage with the specified id.

**required subuser rights**: vehicle_update

#### parameters

| name | description | type |
|------|-------------|------|
| garage_id | Id of the garage to delete | int

#### return

```json
{ "success": true }
```
    

#### errors

*   201 – Not found in database (if there is no garage with such id)