---
title: Optimizing routes
description: API call to get optimized order of route checkpoints. To minimize transit time and costs, it may be beneficial to reorder route checkpoints so total travel time between them  is minimal. Our platform provides a way to perform such optimization. You don't even need to create route and checkpoints, you just provide data required to optimize and algorithm returns order in which points should be visited.
---

# Optimizing routes

To reduce transit time and costs, it may be helpful to rearrange route checkpoints so that the total travel time between them is minimized. Our platform offers a way to perform this optimization. You don't even need to create a route and checkpoints; you simply provide the necessary data for optimization, and the algorithm returns the order in which the points should be visited.


## API actions

API path: `/task/route/points/optimize`.

### `optimize`

The suggested order for the given route points will correspond to the time windows (from and to) of each point. Points with earlier time windows will have lower ordinal numbers. If time windows overlap, the order of such points may vary to maximize the overall efficiency of the route. The maximum distance per route optimization is 5000 kilometers. When using APIs, the maximum number of points per route optimization is 49 points to visit, plus 1 start point.

**required sub-user rights**: `task_update`.

#### Parameters

* **start_point** - (object) the coordinates of the location from where the performer will depart. The departure time is optional parameter. 

  
```json
{
  "lat": 15.233,
  "lng": -5.554,
  "departure": "2024-03-19 13:30:00"
}
```

* **route_points** - (array of objects) the points that the performer must visit, and the count of points must be within the range of 2 to 49. For example:

```json
[
  {"location": {"lat": 11.111, "lng": 11.111}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"},
  {"location": {"lat": 22.222, "lng": -2.222}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"},
  {"location": {"lat": -3.333, "lng": 33.333}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"},
  {"location": {"lat": -4.444, "lng": -4.444}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"},
  {"location": {"lat": 55.555, "lng": 55.555}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}
]
```

#### Response

```json
{
  "success": true,
  "result": [2, 0, 1] 
}
```

The `result` will return the order in which the points should be visited.

If for route points:

```
[
   {route_point_0}, // index in list = 0
   {route_point_1}, // index in list = 1
   {route_point_2}  // index in list = 2
]
```

this action returns: ```[2, 0, 1]```

it means "change points order as following":

```
point at index 2 move to index 0,
point at index 0 move to index 1,
point at index 1 move to index 0
```

or with a more tangible example with 5 points. You have the next points to be reordered

```json
[
{"location": {"lat": 38.81673961922754,"lng": -77.15569496154785}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, // it has index 0
{"location": {"lat": 38.82767290746902,"lng": -77.1445369720459}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, // it has index 1
{"location": {"lat": 38.834760258479704,"lng": -77.14093208312988}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, // this one with index 2
{"location": {"lat": 38.81583679562883,"lng": -77.14814186096191}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, // this with index 3
{"location": {"lat": 38.81031929163279,"lng":7.15582370758057}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"} // and this one has index 4
]
```

The API request will be

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/route/points/optimize' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "start_point": {"lat": 38.81476676765485,  "lng": -77.1608018875122}, "route_points": [{"location": {"lat": 38.81673961922754,"lng": -77.15569496154785}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, {"location": {"lat": 38.82767290746902,"lng": -77.1445369720459}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, {"location": {"lat": 38.834760258479704,"lng": -77.14093208312988}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, {"location": {"lat": 38.81583679562883,"lng": -77.14814186096191}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, {"location": {"lat": 38.81031929163279,"lng":7.15582370758057}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}]}'
    ```

The platform will reply to you with:

```json
{
  "result": [4,0,3,1,2],
  "success": true
}
```

So the optimized route with start point from "lat": 38.81476676765485, "lng": -77.1608018875122 should be:

```json
[
{"location": {"lat": 38.81031929163279,"lng":7.15582370758057}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, // this one had index 4, now it is the first point to visit
{"location": {"lat": 38.81673961922754,"lng": -77.15569496154785}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, // it had index 0, now it is the second point to visit
{"location": {"lat": 38.81583679562883,"lng": -77.14814186096191}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, // this with index 3 becomes the third point to visit
{"location": {"lat": 38.82767290746902,"lng": -77.1445369720459}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"}, // it had index 1, now it is the fourth point to visit
{"location": {"lat": 38.834760258479704,"lng": -77.14093208312988}, "from": "2024-03-19 00:00:00", "to": "2024-03-19 23:59:00"} // and this one with index 2, now it is the last fifth point to visit
]
```

#### Errors

* 7 - Invalid parameters.
* 210 - Path distance exceeds the max distance limit - if the overal route distance is more than 5000 km.
* 264 - Timeout not reached - too high api call rate.

