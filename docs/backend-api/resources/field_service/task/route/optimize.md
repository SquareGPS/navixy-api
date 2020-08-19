---
title: Task route optimize
description: Task route optimize
---

# Task route optimize

API path: `/task/route/points/optimize`.

## optimize

Suggest optimal order for given route points. Suggested order will correspond to route points time windows:
points with earlier time windows will have lower ordinal numbers. If time windows overlaps each other, such
points can have any order due to maximizing summary efficiency of the route.

**required subuser rights**: task_update

#### parameters

* **start_point** - (object) coordinates of location, from where performer will come
```js
{ "lat": 15.233, "lng": -5.554 }
```
* **route_points** - (array of objects) points, which performer must visit
```js
[
  {"location": {"lat": 11.111, "lng": 11.111}, "from": "2019-04-05 13:45:00", "to": "2019-04-05 14:00:00"},
  {"location": {"lat": 22.222, "lng": -2.222}, "from": "2019-04-05 13:45:00", "to": "2019-04-05 14:00:00"},
  {"location": {"lat": -3.333, "lng": 33.333}, "from": "2019-04-05 15:45:00", "to": "2019-04-05 16:00:00"},
  {"location": {"lat": -4.444, "lng": -4.444}, "from": "2019-04-05 16:45:00", "to": "2019-04-05 17:00:00"},
  {"location": {"lat": 55.555, "lng": 55.555}, "from": "2019-04-05 18:45:00", "to": "2019-04-05 19:00:00"}
]
```

#### return

```js
{
  "success": true,
  "result": [2, 0, 1]
}
```

for route points:
```js
[
   {route_point_0}, // index in list = 0
   {route_point_1}, // index in list = 1
   {route_point_2}  // index in list = 2
]
```
returns:
``[2, 0, 1]``

it means "change points order as following:
```js
point at index 2 move to index 0,
point at index 0 move to index 1,
point at index 1 move to index 0"
```

#### errors

*   6 - Invalid parameters
*   79 - Timeout not reached (too high api call rate)
*   general types of errors

