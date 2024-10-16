# Tracking Stationary Objects with BLE Tags

Integrating objects into the Internet of Things (IoT) is simplified with the Navixy platform, which supports tracking both **movable** and **stationary** objects. Examples of stationary objects include heavy equipment, agricultural machinery, cargo, goods, and security equipment. Installing GPS devices on each of these objects can be very expensive. A more cost-effective solution is to install one device on a vehicle or site and track the rest using inexpensive Bluetooth Low Energy (BLE) tags.

In this tutorial, we will guide you through the process of tracking stationary objects. We will discuss the following:

- How to organize tracking for stationary objects
- Which GPS devices and BLE tags to use for data collection
- Step-by-step setup instructions, using truck trailers as an example
- How to obtain information about trips and usage for subsequent service work
- The API calls needed to retrieve information about the tags
- Additional use cases based on real-world scenarios

Additionally, you can read more about configuration examples in our [Expert Center](https://docs.navixy.com/expert-center/tracking-of-stationary-objects).

## What you need to track stationary objects

Various devices are able to read data from BLE beacons: Galileosky, Quecklink, Ruptela, Teltonika, TopFlyTech. In this example, we will use the Teltonika FMB920 model and the BLE beacon Eye Sensor. To begin tracking stationary objects, you'll need the following:

1. **A GPS device that can read BLE tags and is supported by the platform.**
2. **BLE tags that are compatible with the GPS device.** Many BLE tags can transmit information about temperature, humidity, and their battery charge, enhancing their tracking capabilities. For our purposes, we will focus on stationary objects specifically.
3. **Platform APIs** that provide information about which GPS device a particular tag is near. To create custom solutions for your users using these APIs, you will need developers. Clients typically hire their own developers or contract third-party teams.

Now let's examine the procedure for implementing a real-world case study: tracking truck trailers for trip and usage information and subsequent service work.

## How to get information about BLE beacons near the GPS device

```json
{
  "tracker_id": 10181654,
  "hardware_id": "7cf9501df3d6924e423cabcde4c924ff",
  "rssi": -101,
  "get_time": "2023-04-17 17:14:42",
  "latitude": 50.3487321,
  "longitude": 7.58238,
  "ext_data": {
    "voltage": 3.075,
    "temperature": 24.0
  }
}
```

You can read information from it:
- `tracker_id` - int. The ID of the tracker (also known as “object_id”).
- `hardware_id` - string. The ID of the beacon.
- `rssi` - int. RSSI stands for received signal strength indicator and represents the power of the received signal on a device. This value helps determine the distance between the beacon and the tracker.
- `get_time` - date/time. The timestamp when this data was received.
- `latitude` - float. Latitude coordinate.
- `longitude` - float. Longitude coordinate.
- `ext_data` - object. Additional beacon data, such as:
	- `voltage` - float. The voltage of the beacon.
	- `temperature` - float. The temperature reading from the beacon.


## API calls to get information about BLE tags

There are two API calls that allow you to get all the necessary information about BLE beacons:
### Historical data from BLE tags

The first call retrieves [historical data from devices](../../resources/tracking/beacon/index.md#read). You can set the `from` and `to` parameters for obtaining data during a specific period about connected BLE beacons. Since we need the information from the BLE tags' point of view, i.e., the trailers, let's request the information using the `beacons` parameter.

**Request example:**

cURL
```shell
curl -X POST 'https://api.navixy.com/v2/beacon/data/read' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "59be129c1855e34ea9eb272b1e26ef1d",
        "from": "2023-04-17 17:00:00",
        "to": "2023-04-17 18:00:00",
        "beacons": ["7cf9501df3d6924e423cabcde4c924ff"]
    }'
```


This will show which devices were in the vicinity of this BLE beacon during period

```json
{
  "list": [
    {
      "tracker_id": 10181654,
      "hardware_id": "7cf9501df3d6924e423cabcde4c924ff",
      "rssi": -101,
      "get_time": "2023-04-17 17:05:42",
      "latitude": 50.3487321,
      "longitude": 7.58238,
      "ext_data": {
        "voltage": 3.075,
        "temperature": 24.0
      }
    },
    {
      "tracker_id": 10181654,
      "hardware_id": "7cf9501df3d6924e423cabcde4c924ff",
      "rssi": -101,
      "get_time": "2023-04-17 17:40:22",
      "latitude": 55.348890,
      "longitude": 6.59403,
      "ext_data": {
        "voltage": 3.075,
        "temperature": 24.0
      }
    }
  ],
  "success": true
}
```

### Last data from BLE tags

The second call retrieves information about [currently connected beacons](../../resources/tracking/beacon/index.md#last-values) to a specific device. For example, if you want to know which trailer is currently near the device, use the following request:

**Request example:**

cURL
```shell
curl -X POST 'https://api.navixy.com/v2/beacon/data/last_values' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "59be129c1855e34ea9eb272b1e26ef1d",
        "trackers": [10181654],
        "skip_older_than_seconds": 1200
    }'
```

```json
{
  "list": [
    {
      "tracker_id": 10181654,
      "hardware_id": "7cf9501df3d6924e423cabcde4c924ff",
      "rssi": -101,
      "get_time": "2023-04-17 17:40:22",
      "latitude": 55.348890,
      "longitude": 6.59403,
      "ext_data": {
        "voltage": 3.075,
        "temperature": 24.0
      }
    }
  ],
  "success": true
}
```

This will provide information that there is a trailer with the identifier `7cf9501df3d6924e423cabcde4c924ff` located next to the device.




## Obtaining information on trip details and usage time

We've already gathered historical data using the first of the presented API calls, which showed on which devices the trailer was displayed at a specific time. To get information about the journeys and usage time of this trailer, we simply need to use one of the two API calls:

### Overall trip info

API call [track/list](../../resources/tracking/track/index.md#list) to get trip information for the period. This will provide general information about the trips, such as where and when they started and ended, maximum speed, mileage, and more.

Request example:

=== "cURL"

```shell
curl -X POST 'https://api.navixy.com/v2/beacon/data/last_values' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "59be129c1855e34ea9eb272b1e26ef1d",
        "trackers": [10181654],
        "skip_older_than_seconds": 1200
    }'
```

Response:

```json
{
    "id": 11672,
    "start_date": "2023-04-17 17:05:42",
    "start_address": "10470, County Road, Town of Clarence, Erie County, New York, United States, 14031",
    "max_speed": 62,
    "end_date": "2023-04-17 17:40:22",
    "end_address": "Fast Teddy's, 221, Main Street, City of Tonawanda, New York, United States, 14150",
    "length": 18.91,
    "points": 59,
    "avg_speed": 49,
    "event_count": 3,
    "norm_fuel_consumed": 6.32,
    "type": "regular",
    "gsm_lbs": false
}
```

From this data, we can see that the trip lasted nearly 35 minutes (end_date - start_date), with an average speed of 49 km/h and a maximum speed of 62 km/h. The trip length was 18.91 km. This information allows us to determine how much to pay the driver for transporting the cargo, whether the contractual speed was exceeded, and other details. Additionally, the trip length can be used in the future to calculate the number of kilometers until the next maintenance of the trailer.

### Detailed trip info

If you want a detailed track record of the trailer where the beacon is installed for displaying it in a report, for example, you can use the track/read request. This will give us data on all the points received by the platform during the journey.

Request example:

=== "cURL"

```shell
curl -X POST 'https://api.navixy.com/v2/track/read' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "22eac1c27af4be7b9d04da2ce1af111b",
        "tracker_id": 10181654,
        "from": "2023-04-17 17:00:00",
        "to": "2023-04-17 18:00:00",
        "filter": true
    }'
```

Response:

```json
{
    "success": true,
    "limit_exceeded": true,
    "list": [
        {
        "address": "10470, County Road, Town of Clarence, Erie County, New York, United States, 14031",
        "satellites": 10,
        "mileage": 0,
        "heading": 173,
        "speed": 42,
        "get_time": "2023-04-17 17:05:42",
        "alt": 0,
        "lat": 43.0318683,
        "lng": -78.5985733
        }
    ]
}
```

You can use these points together with your preferred maps API to display them on a map.


## Other examples of using BLE tags

Here are some other examples of how to use BLE tags with a short algorithm to get the necessary results need:

### Child seats

Child seats are mandatory for passengers traveling with children. If you or the user operates a passenger transportation service, knowing whether a child seat is available in a vehicle can help you quickly determine which drivers are suitable for certain passengers and avoid wasting time and fuel. You can also find out which driver currently has a child seat installed in their vehicle. Additionally, it's important to consider passengers with two or more children and identify cars equipped with more than one child seat.

To address this, you'll need to install a BLE beacon on each child seat. Next, let's say your transport booking app needs to request information from all drivers who have a child seat installed. To do this, use the `beacon/last_values` API call to gather information about which drivers can be assigned to a particular order.

You can also use the RSSI parameter to determine if the seat is located inside the vehicle or in the trunk. To accomplish this, you'll need to conduct a few tests. For example, if the RSSI value is lower in the passenger compartment than in the trunk, the seat is likely in the trunk. As a result, you can prioritize your search for vehicles – first, those with a child seat in the passenger compartment, and then those with a child seat in the trunk. This approach ensures that you efficiently match passengers with appropriate vehicles and drivers.

### Agricultural machinery

Suppose your client has agricultural machinery that can be connected to various equipment. How can you track which tractor is using a seeder and which has a plow? This information will help you understand the frequency and extent of tool usage, and also determine their current location. This way, workers can spend more time working in the field rather than searching for equipment. To achieve this, install devices on tractors and combines, as well as in tool storage areas. Place one BLE beacon on each tool in a secure spot where it is difficult to remove, preventing it from getting lost during work. Next, to determine how long the tools have been in use, query the `beacon/read` API call. The information from the response will be helpful, just like with the trailers in our detailed example. To determine the location of a specific tool, query `beacon/last_values` with a search for beacons to identify where and on which device the tool is installed. This approach ensures efficient tracking and utilization of your agricultural equipment, ultimately increasing productivity.

### Use on construction sites

Construction sites often have numerous tools and expensive equipment. While installing a beacon for tracking purposes is beneficial, another concern arises – how can you ensure that the equipment is tracked frequently, and that the GPS tracker doesn't run out of power? To monitor the usage and location of the equipment, BLE beacons can also come in handy.

The solution for construction sites can be similar to that of agricultural machinery – install devices on the machinery as well as on storage sites. This approach allows you to effectively track your valuable equipment, ensuring that it's being used efficiently and minimizing the risk of loss or misplacement. By keeping a close eye on your tools and machinery, you can optimize productivity at the construction site.

### Indoor tracking

You can effectively track items indoors using the platform and BLE tags. All you need to do is install GPS devices in different parts of the warehouse or building and tag the objects you want to track. Here are a few examples:

* Tracking employees in various areas of a warehouse or store: This allows you to know which area an employee is in or how many sales assistants are near the information desk. Having this information helps improve efficiency and ensures that staff members are where they need to be.
* Tracking goods or machinery in different areas of the warehouse: Knowing the location of goods or equipment saves time, as you don't have to search for them throughout the warehouse. This streamlines the retrieval process, making your operations more efficient.

### Tracking goods with BLE beacons

Utilizing BLE beacons for tracking can greatly benefit transport companies by allowing them to determine which truck is carrying a specific pallet of goods at any given moment. This method not only enables the tracking of goods' paths but also helps calculate transport costs more accurately.

By adopting this innovative approach, transport companies can enhance their operations, making them more efficient and precise. This ultimately leads to better service for clients and more streamlined business processes.