---
title: Requesting tracker raw data
description: How to request raw tracker data from Navixy Data Warehouse and typical use cases. 
---

# Requesting tracker raw data

Sometimes, TSP, integrators, and developers need to look at the original, unprocessed data from tracking devices, often
called "raw data". This helps them to get more accurate information and a better understanding of the collected data.
It can also help fix issues with the tracking process. Plus, they can utilize this raw data in other systems for more
analysis or use in different parts of the business.

## Typical use case

To efficiently manage fuel consumption, especially for fleet management or cargo transportation businesses, integrating
your ERP system with the Navixy platform is crucial. This integration enables you to seamlessly request raw fuel data
from specific devices, enhancing your overall fuel monitoring and expense tracking capabilities.

In this situation, you may need to retrieve the following data:
* Fuel Level
* Device location
* Mileage (odometer)
* Speed
* Date and time
* Any other data valuable to your business

It is important to realize that in this case we will not get human-readable information about fuel drains and refills, 
excessive consumption, idling and other analytics. Here we are talking about raw data received directly from the device 
and decoded by Navixy platform, in other words, instantaneous data readings for a certain period. Data obtained in this 
way is suitable for further processing and analyzing on your side.

## Requesting inputs list

Tracking devices from different manufacturers have different specifics of work and send data in different forms. In 
addition, sensors can be of different types: digital and analog, wired and wireless, built-in and external. Also, there 
can be several sensors monitoring the same type of readings: for example, two fuel sensors in two tanks, internal and 
external temperature sensors, etc.

It is for this reason that before requesting raw data, we have to understand what data the device is capable to report 
to the platform, and what the data inputs are named. To do this, we need to use `raw_data/get_inputs` request.

Example for a device with ID 123456:

=== "cURL"

    ```shell
    curl -X 'POST' \
    'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/get_inputs' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "6dc7d304dec4434f4c4202ec42817f83","tracker_id": 123456}'
    ```

The platform will notify us about success, and we will see the following JSON object in response:

```json
{
  "discrete_inputs": 2,
  "discrete_outputs": 1,
  "inputs": [
    "analog_1",
    "battery_voltage",
    "board_voltage",
    "ext_temp_sensor_4",
    "freq_1",
    "hw_mileage",
    "impulse_counter_1",
    "lls_level_4",
    "lls_temperature_4"
  ],
  "states": [
    "hardware_key"
  ],
  "success": true
}
```

Among the obtained inputs we see the one of interest to us - `lls_level_4`. This is a fuel level input, and the index 4 
indicates the value is a range of LLS levels from `1` to `4`. This means the device can send fuel data on maximum of four 
inputs: from `lls_level_1` to `lls_level_4`.

We also see the `hw_mileage` which will allow us to get value of the hardware odometer.

!!! note "The presence of some inputs in the received response does not mean that data is certainly available on these inputs. It 
means that data may come on them, but whether it is actually available or not depends on the configuration of a 
particular device."

## Requesting raw data readings

Now we know the name of the inputs where the fuel data comes from, and we can use them in the API query. However, we also 
need other parameters for more accurate analysis. This data is not related to sensors, so the above query does not return 
it. They come in simple columns and are listed on the appropriate documentation page.

We will use the following columns:

* `lat`
* `lng`
* `speed`

In addition, we will use names for inputs according to the information obtained earlier:

* `inputs.lls_level_1`
* `inputs.hw_mileage`

!!! note "We specify inputs.lls_level_1 because we know that our device only sends data on this input. If we didn't know the input number, we could have specified all four possible inputs, and then the inputs without data would just get zero values."

The API request for raw data in our case must look like below:

=== "cURL"

    ```shell
    curl -X 'POST' \
    'https://api.eu.navixy.com/dwh/v1/tracker/raw_data/read' \
    -H 'accept: text/csv' \
    -H 'Content-Type: application/json' \
    -d '{
    "hash": "6dc7d304dec4434f4c4202ec42817f83",
    "tracker_id": "123456",
    "from": "2023-11-29T08:31:00Z",
    "to": "2023-11-29T08:32:00Z",
    "columns": ["lat","lng","speed","inputs.lls_level_1","inputs.hw_mileage"]}'
    ```

The response is returned in a CSV table format:

```
"msg_time","lat","lng","speed","inputs.lls_level_1","inputs.hw_mileage"
"2023-11-29T08:31:10Z",54.2312716,69.5261833,0,3307,24250.798
"2023-11-29T08:31:12Z",54.1811183,69.5331349,24,3274,24257.16
"2023-11-29T08:31:27Z",54.1802066,69.5333599,21,\N,\N
"2023-11-29T08:31:27Z",54.1802066,69.5333599,21,3274,24257.262
"2023-11-29T08:31:30Z",54.180055,69.533395,20,3274,24257.279
"2023-11-29T08:31:31Z",54.180005,69.5334083,20,3274,24257.285
"2023-11-29T08:31:33Z",54.179915,69.5334266,17,3274,24257.295
"2023-11-29T08:31:34Z",54.1798766,69.533435,15,3274,24257.299
"2023-11-29T08:31:36Z",54.1798116,69.5334433,12,3274,24257.306
"2023-11-29T08:31:37Z",54.179785,69.5334416,10,3274,24257.309
"2023-11-29T08:31:39Z",54.1797366,69.533425,9,3274,24257.315
"2023-11-29T08:31:40Z",54.1797183,69.5334083,8,3274,24257.315
"2023-11-29T08:31:42Z",54.1796883,69.5333449,10,3274,24257.322
"2023-11-29T08:31:43Z",54.17968,69.5333016,12,3274,24257.325
"2023-11-29T08:31:45Z",54.1796816,69.53318,15,3274,24257.333
"2023-11-29T08:31:47Z",54.1796816,69.533025,20,3274,24257.343
```

In the above example we see the output only for one minute of tracking. When querying raw data over a long period of time, 
the response can reach significant sizes - this must be considered.

!!! note "In one of the lines we see `\N` instead of fuel level and mileage values. This means that no such information was received in this data packet. The `\N` symbol represents `NULL`."

The above example is one of the simplest, but clearly demonstrates the process of using an API request to read raw data. 
You can query a lot of data at once and over large periods of time, depending on your objectives.
