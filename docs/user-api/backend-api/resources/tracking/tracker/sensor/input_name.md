---
title: Sensor inputs
description: API call to get descriptions of all sensor inputs existing in the system. 
---

# Input name

API base path: `/tracker/sensor/input_name`.

API call to get all sensor inputs and state fields existing in the system and their descriptions.


## API actions

### `list`

This will provide descriptions of all sensor inputs and state fields present in the system. These descriptions will be 
given in the language according to the user's locale.

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/input_name/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/sensor/input_name/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

For every input following properties returned: `input_name` and `description`.

`input_name` is an enum member, same as in [sensor object](index.md).

`description` is made in current user's language (according to [locale settings](../../../commons/user/settings/index.md)).

???+ example "Response"

    ```json
    {
    "success": true,
    "list": [
        {
            "input_name": "acceleration",
            "description": "Acceleration"
        },
        {
            "input_name": "analog_1",
            "description": "Analog sensor #1"
        },
        {
            "input_name": "analog_2",
            "description": "Analog sensor #2"
        },
        {
            "input_name": "analog_3",
            "description": "Analog sensor #3"
        },
        {
            "input_name": "analog_4",
            "description": "Analog sensor #4"
        },
        {
            "input_name": "analog_5",
            "description": "Analog sensor #5"
        },
        {
            "input_name": "analog_6",
            "description": "Analog sensor #6"
        },
        {
            "input_name": "analog_7",
            "description": "Analog sensor #7"
        },
        {
            "input_name": "analog_8",
            "description": "Analog sensor #8"
        },
        {
            "input_name": "axis_x",
            "description": "Acceleration by X axis"
        },
        {
            "input_name": "axis_y",
            "description": "Acceleration by Y axis"
        },
        {
            "input_name": "axis_z",
            "description": "Acceleration by Z axis"
        },
        {
            "input_name": "battery_current",
            "description": "Battery current"
        },
        {
            "input_name": "battery_level",
            "description": "Battery level"
        },
        {
            "input_name": "battery_voltage",
            "description": "Battery voltage"
        },
        {
            "input_name": "ble_battery_level_1",
            "description": "BLE: Battery level #1"
        },
        {
            "input_name": "ble_battery_level_10",
            "description": "BLE: Battery level #10"
        },
        {
            "input_name": "ble_battery_level_11",
            "description": "BLE: Battery level #11"
        },
        {
            "input_name": "ble_battery_level_12",
            "description": "BLE: Battery level #12"
        },
        {
            "input_name": "ble_battery_level_13",
            "description": "BLE: Battery level #13"
        },
        {
            "input_name": "ble_battery_level_14",
            "description": "BLE: Battery level #14"
        },
        {
            "input_name": "ble_battery_level_15",
            "description": "BLE: Battery level #15"
        },
        {
            "input_name": "ble_battery_level_16",
            "description": "BLE: Battery level #16"
        },
        {
            "input_name": "ble_battery_level_2",
            "description": "BLE: Battery level #2"
        },
        {
            "input_name": "ble_battery_level_3",
            "description": "BLE: Battery level #3"
        },
        {
            "input_name": "ble_battery_level_4",
            "description": "BLE: Battery level #4"
        },
        {
            "input_name": "ble_battery_level_5",
            "description": "BLE: Battery level #5"
        },
        {
            "input_name": "ble_battery_level_6",
            "description": "BLE: Battery level #6"
        },
        {
            "input_name": "ble_battery_level_7",
            "description": "BLE: Battery level #7"
        },
        {
            "input_name": "ble_battery_level_8",
            "description": "BLE: Battery level #8"
        },
        {
            "input_name": "ble_battery_level_9",
            "description": "BLE: Battery level #9"
        },
        {
            "input_name": "ble_battery_voltage_1",
            "description": "BLE: Battery voltage #1"
        },
        {
            "input_name": "ble_battery_voltage_10",
            "description": "BLE: Battery voltage #10"
        },
        {
            "input_name": "ble_battery_voltage_11",
            "description": "BLE: Battery voltage #11"
        },
        {
            "input_name": "ble_battery_voltage_12",
            "description": "BLE: Battery voltage #12"
        },
        {
            "input_name": "ble_battery_voltage_13",
            "description": "BLE: Battery voltage #13"
        },
        {
            "input_name": "ble_battery_voltage_14",
            "description": "BLE: Battery voltage #14"
        },
        {
            "input_name": "ble_battery_voltage_15",
            "description": "BLE: Battery voltage #15"
        },
        {
            "input_name": "ble_battery_voltage_16",
            "description": "BLE: Battery voltage #16"
        },
        {
            "input_name": "ble_battery_voltage_2",
            "description": "BLE: Battery voltage #2"
        },
        {
            "input_name": "ble_battery_voltage_3",
            "description": "BLE: Battery voltage #3"
        },
        {
            "input_name": "ble_battery_voltage_4",
            "description": "BLE: Battery voltage #4"
        },
        {
            "input_name": "ble_battery_voltage_5",
            "description": "BLE: Battery voltage #5"
        },
        {
            "input_name": "ble_battery_voltage_6",
            "description": "BLE: Battery voltage #6"
        },
        {
            "input_name": "ble_battery_voltage_7",
            "description": "BLE: Battery voltage #7"
        },
        {
            "input_name": "ble_battery_voltage_8",
            "description": "BLE: Battery voltage #8"
        },
        {
            "input_name": "ble_battery_voltage_9",
            "description": "BLE: Battery voltage #9"
        },
        {
            "input_name": "ble_humidity_1",
            "description": "BLE: Humidity sensor #1"
        },
        {
            "input_name": "ble_humidity_10",
            "description": "BLE: Humidity sensor #10"
        },
        {
            "input_name": "ble_humidity_11",
            "description": "BLE: Humidity sensor #11"
        },
        {
            "input_name": "ble_humidity_12",
            "description": "BLE: Humidity sensor #12"
        },
        {
            "input_name": "ble_humidity_13",
            "description": "BLE: Humidity sensor #13"
        },
        {
            "input_name": "ble_humidity_14",
            "description": "BLE: Humidity sensor #14"
        },
        {
            "input_name": "ble_humidity_15",
            "description": "BLE: Humidity sensor #15"
        },
        {
            "input_name": "ble_humidity_16",
            "description": "BLE: Humidity sensor #16"
        },
        {
            "input_name": "ble_humidity_2",
            "description": "BLE: Humidity sensor #2"
        },
        {
            "input_name": "ble_humidity_3",
            "description": "BLE: Humidity sensor #3"
        },
        {
            "input_name": "ble_humidity_4",
            "description": "BLE: Humidity sensor #4"
        },
        {
            "input_name": "ble_humidity_5",
            "description": "BLE: Humidity sensor #5"
        },
        {
            "input_name": "ble_humidity_6",
            "description": "BLE: Humidity sensor #6"
        },
        {
            "input_name": "ble_humidity_7",
            "description": "BLE: Humidity sensor #7"
        },
        {
            "input_name": "ble_humidity_8",
            "description": "BLE: Humidity sensor #8"
        },
        {
            "input_name": "ble_humidity_9",
            "description": "BLE: Humidity sensor #9"
        },
        {
            "input_name": "ble_lls_level_1",
            "description": "BLE: LLS #1 level"
        },
        {
            "input_name": "ble_lls_level_10",
            "description": "BLE: LLS #10 level"
        },
        {
            "input_name": "ble_lls_level_2",
            "description": "BLE: LLS #2 level"
        },
        {
            "input_name": "ble_lls_level_3",
            "description": "BLE: LLS #3 level"
        },
        {
            "input_name": "ble_lls_level_4",
            "description": "BLE: LLS #4 level"
        },
        {
            "input_name": "ble_lls_level_5",
            "description": "BLE: LLS #5 level"
        },
        {
            "input_name": "ble_lls_level_6",
            "description": "BLE: LLS #6 level"
        },
        {
            "input_name": "ble_lls_level_7",
            "description": "BLE: LLS #7 level"
        },
        {
            "input_name": "ble_lls_level_8",
            "description": "BLE: LLS #8 level"
        },
        {
            "input_name": "ble_lls_level_9",
            "description": "BLE: LLS #9 level"
        },
        {
            "input_name": "ble_lls_temperature_1",
            "description": "BLE: LLS #1 temperature"
        },
        {
            "input_name": "ble_lls_temperature_10",
            "description": "BLE: LLS #10 temperature"
        },
        {
            "input_name": "ble_lls_temperature_2",
            "description": "BLE: LLS #2 temperature"
        },
        {
            "input_name": "ble_lls_temperature_3",
            "description": "BLE: LLS #3 temperature"
        },
        {
            "input_name": "ble_lls_temperature_4",
            "description": "BLE: LLS #4 temperature"
        },
        {
            "input_name": "ble_lls_temperature_5",
            "description": "BLE: LLS #5 temperature"
        },
        {
            "input_name": "ble_lls_temperature_6",
            "description": "BLE: LLS #6 temperature"
        },
        {
            "input_name": "ble_lls_temperature_7",
            "description": "BLE: LLS #7 temperature"
        },
        {
            "input_name": "ble_lls_temperature_8",
            "description": "BLE: LLS #8 temperature"
        },
        {
            "input_name": "ble_lls_temperature_9",
            "description": "BLE: LLS #9 temperature"
        },
        {
            "input_name": "ble_luminosity_1",
            "description": "BLE: Luminosity #1"
        },
        {
            "input_name": "ble_luminosity_10",
            "description": "BLE: Luminosity #10"
        },
        {
            "input_name": "ble_luminosity_11",
            "description": "BLE: Luminosity #11"
        },
        {
            "input_name": "ble_luminosity_12",
            "description": "BLE: Luminosity #12"
        },
        {
            "input_name": "ble_luminosity_13",
            "description": "BLE: Luminosity #13"
        },
        {
            "input_name": "ble_luminosity_14",
            "description": "BLE: Luminosity #14"
        },
        {
            "input_name": "ble_luminosity_15",
            "description": "BLE: Luminosity #15"
        },
        {
            "input_name": "ble_luminosity_16",
            "description": "BLE: Luminosity #16"
        },
        {
            "input_name": "ble_luminosity_2",
            "description": "BLE: Luminosity #2"
        },
        {
            "input_name": "ble_luminosity_3",
            "description": "BLE: Luminosity #3"
        },
        {
            "input_name": "ble_luminosity_4",
            "description": "BLE: Luminosity #4"
        },
        {
            "input_name": "ble_luminosity_5",
            "description": "BLE: Luminosity #5"
        },
        {
            "input_name": "ble_luminosity_6",
            "description": "BLE: Luminosity #6"
        },
        {
            "input_name": "ble_luminosity_7",
            "description": "BLE: Luminosity #7"
        },
        {
            "input_name": "ble_luminosity_8",
            "description": "BLE: Luminosity #8"
        },
        {
            "input_name": "ble_luminosity_9",
            "description": "BLE: Luminosity #9"
        },
        {
            "input_name": "ble_signal_strength_1",
            "description": "BLE: Signal strength #1"
        },
        {
            "input_name": "ble_signal_strength_10",
            "description": "BLE: Signal strength #10"
        },
        {
            "input_name": "ble_signal_strength_11",
            "description": "BLE: Signal strength #11"
        },
        {
            "input_name": "ble_signal_strength_12",
            "description": "BLE: Signal strength #12"
        },
        {
            "input_name": "ble_signal_strength_13",
            "description": "BLE: Signal strength #13"
        },
        {
            "input_name": "ble_signal_strength_14",
            "description": "BLE: Signal strength #14"
        },
        {
            "input_name": "ble_signal_strength_15",
            "description": "BLE: Signal strength #15"
        },
        {
            "input_name": "ble_signal_strength_16",
            "description": "BLE: Signal strength #16"
        },
        {
            "input_name": "ble_signal_strength_2",
            "description": "BLE: Signal strength #2"
        },
        {
            "input_name": "ble_signal_strength_3",
            "description": "BLE: Signal strength #3"
        },
        {
            "input_name": "ble_signal_strength_4",
            "description": "BLE: Signal strength #4"
        },
        {
            "input_name": "ble_signal_strength_5",
            "description": "BLE: Signal strength #5"
        },
        {
            "input_name": "ble_signal_strength_6",
            "description": "BLE: Signal strength #6"
        },
        {
            "input_name": "ble_signal_strength_7",
            "description": "BLE: Signal strength #7"
        },
        {
            "input_name": "ble_signal_strength_8",
            "description": "BLE: Signal strength #8"
        },
        {
            "input_name": "ble_signal_strength_9",
            "description": "BLE: Signal strength #9"
        },
        {
            "input_name": "ble_temp_sensor_1",
            "description": "BLE: temperature sensor #1"
        },
        {
            "input_name": "ble_temp_sensor_10",
            "description": "BLE: temperature sensor #10"
        },
        {
            "input_name": "ble_temp_sensor_11",
            "description": "BLE: temperature sensor #11"
        },
        {
            "input_name": "ble_temp_sensor_12",
            "description": "BLE: temperature sensor #12"
        },
        {
            "input_name": "ble_temp_sensor_13",
            "description": "BLE: temperature sensor #13"
        },
        {
            "input_name": "ble_temp_sensor_14",
            "description": "BLE: temperature sensor #14"
        },
        {
            "input_name": "ble_temp_sensor_15",
            "description": "BLE: temperature sensor #15"
        },
        {
            "input_name": "ble_temp_sensor_16",
            "description": "BLE: temperature sensor #16"
        },
        {
            "input_name": "ble_temp_sensor_2",
            "description": "BLE: temperature sensor #2"
        },
        {
            "input_name": "ble_temp_sensor_3",
            "description": "BLE: temperature sensor #3"
        },
        {
            "input_name": "ble_temp_sensor_4",
            "description": "BLE: temperature sensor #4"
        },
        {
            "input_name": "ble_temp_sensor_5",
            "description": "BLE: temperature sensor #5"
        },
        {
            "input_name": "ble_temp_sensor_6",
            "description": "BLE: temperature sensor #6"
        },
        {
            "input_name": "ble_temp_sensor_7",
            "description": "BLE: temperature sensor #7"
        },
        {
            "input_name": "ble_temp_sensor_8",
            "description": "BLE: temperature sensor #8"
        },
        {
            "input_name": "ble_temp_sensor_9",
            "description": "BLE: temperature sensor #9"
        },
        {
            "input_name": "ble_tire_pressure_1",
            "description": "BLE: Tire pressure #1"
        },
        {
            "input_name": "ble_tire_pressure_10",
            "description": "BLE: Tire pressure #10"
        },
        {
            "input_name": "ble_tire_pressure_11",
            "description": "BLE: Tire pressure #11"
        },
        {
            "input_name": "ble_tire_pressure_12",
            "description": "BLE: Tire pressure #12"
        },
        {
            "input_name": "ble_tire_pressure_13",
            "description": "BLE: Tire pressure #13"
        },
        {
            "input_name": "ble_tire_pressure_14",
            "description": "BLE: Tire pressure #14"
        },
        {
            "input_name": "ble_tire_pressure_15",
            "description": "BLE: Tire pressure #15"
        },
        {
            "input_name": "ble_tire_pressure_16",
            "description": "BLE: Tire pressure #16"
        },
        {
            "input_name": "ble_tire_pressure_17",
            "description": "BLE: Tire pressure #17"
        },
        {
            "input_name": "ble_tire_pressure_18",
            "description": "BLE: Tire pressure #18"
        },
        {
            "input_name": "ble_tire_pressure_19",
            "description": "BLE: Tire pressure #19"
        },
        {
            "input_name": "ble_tire_pressure_2",
            "description": "BLE: Tire pressure #2"
        },
        {
            "input_name": "ble_tire_pressure_20",
            "description": "BLE: Tire pressure #20"
        },
        {
            "input_name": "ble_tire_pressure_21",
            "description": "BLE: Tire pressure #21"
        },
        {
            "input_name": "ble_tire_pressure_22",
            "description": "BLE: Tire pressure #22"
        },
        {
            "input_name": "ble_tire_pressure_23",
            "description": "BLE: Tire pressure #23"
        },
        {
            "input_name": "ble_tire_pressure_24",
            "description": "BLE: Tire pressure #24"
        },
        {
            "input_name": "ble_tire_pressure_25",
            "description": "BLE: Tire pressure #25"
        },
        {
            "input_name": "ble_tire_pressure_26",
            "description": "BLE: Tire pressure #26"
        },
        {
            "input_name": "ble_tire_pressure_27",
            "description": "BLE: Tire pressure #27"
        },
        {
            "input_name": "ble_tire_pressure_28",
            "description": "BLE: Tire pressure #28"
        },
        {
            "input_name": "ble_tire_pressure_29",
            "description": "BLE: Tire pressure #29"
        },
        {
            "input_name": "ble_tire_pressure_3",
            "description": "BLE: Tire pressure #3"
        },
        {
            "input_name": "ble_tire_pressure_30",
            "description": "BLE: Tire pressure #30"
        },
        {
            "input_name": "ble_tire_pressure_4",
            "description": "BLE: Tire pressure #4"
        },
        {
            "input_name": "ble_tire_pressure_5",
            "description": "BLE: Tire pressure #5"
        },
        {
            "input_name": "ble_tire_pressure_6",
            "description": "BLE: Tire pressure #6"
        },
        {
            "input_name": "ble_tire_pressure_7",
            "description": "BLE: Tire pressure #7"
        },
        {
            "input_name": "ble_tire_pressure_8",
            "description": "BLE: Tire pressure #8"
        },
        {
            "input_name": "ble_tire_pressure_9",
            "description": "BLE: Tire pressure #9"
        },
        {
            "input_name": "ble_tire_temperature_1",
            "description": "BLE: Tire air temperature #1"
        },
        {
            "input_name": "ble_tire_temperature_10",
            "description": "BLE: Tire air temperature #10"
        },
        {
            "input_name": "ble_tire_temperature_11",
            "description": "BLE: Tire air temperature #11"
        },
        {
            "input_name": "ble_tire_temperature_12",
            "description": "BLE: Tire air temperature #12"
        },
        {
            "input_name": "ble_tire_temperature_13",
            "description": "BLE: Tire air temperature #13"
        },
        {
            "input_name": "ble_tire_temperature_14",
            "description": "BLE: Tire air temperature #14"
        },
        {
            "input_name": "ble_tire_temperature_15",
            "description": "BLE: Tire air temperature #15"
        },
        {
            "input_name": "ble_tire_temperature_16",
            "description": "BLE: Tire air temperature #16"
        },
        {
            "input_name": "ble_tire_temperature_17",
            "description": "BLE: Tire air temperature #17"
        },
        {
            "input_name": "ble_tire_temperature_18",
            "description": "BLE: Tire air temperature #18"
        },
        {
            "input_name": "ble_tire_temperature_19",
            "description": "BLE: Tire air temperature #19"
        },
        {
            "input_name": "ble_tire_temperature_2",
            "description": "BLE: Tire air temperature #2"
        },
        {
            "input_name": "ble_tire_temperature_20",
            "description": "BLE: Tire air temperature #20"
        },
        {
            "input_name": "ble_tire_temperature_21",
            "description": "BLE: Tire air temperature #21"
        },
        {
            "input_name": "ble_tire_temperature_22",
            "description": "BLE: Tire air temperature #22"
        },
        {
            "input_name": "ble_tire_temperature_23",
            "description": "BLE: Tire air temperature #23"
        },
        {
            "input_name": "ble_tire_temperature_24",
            "description": "BLE: Tire air temperature #24"
        },
        {
            "input_name": "ble_tire_temperature_25",
            "description": "BLE: Tire air temperature #25"
        },
        {
            "input_name": "ble_tire_temperature_26",
            "description": "BLE: Tire air temperature #26"
        },
        {
            "input_name": "ble_tire_temperature_27",
            "description": "BLE: Tire air temperature #27"
        },
        {
            "input_name": "ble_tire_temperature_28",
            "description": "BLE: Tire air temperature #28"
        },
        {
            "input_name": "ble_tire_temperature_29",
            "description": "BLE: Tire air temperature #29"
        },
        {
            "input_name": "ble_tire_temperature_3",
            "description": "BLE: Tire air temperature #3"
        },
        {
            "input_name": "ble_tire_temperature_30",
            "description": "BLE: Tire air temperature #30"
        },
        {
            "input_name": "ble_tire_temperature_4",
            "description": "BLE: Tire air temperature #4"
        },
        {
            "input_name": "ble_tire_temperature_5",
            "description": "BLE: Tire air temperature #5"
        },
        {
            "input_name": "ble_tire_temperature_6",
            "description": "BLE: Tire air temperature #6"
        },
        {
            "input_name": "ble_tire_temperature_7",
            "description": "BLE: Tire air temperature #7"
        },
        {
            "input_name": "ble_tire_temperature_8",
            "description": "BLE: Tire air temperature #8"
        },
        {
            "input_name": "ble_tire_temperature_9",
            "description": "BLE: Tire air temperature #9"
        },
        {
            "input_name": "ble_user_data_1",
            "description": "BLE custom user data #1"
        },
        {
            "input_name": "ble_user_data_10",
            "description": "BLE custom user data #10"
        },
        {
            "input_name": "ble_user_data_11",
            "description": "BLE custom user data #11"
        },
        {
            "input_name": "ble_user_data_12",
            "description": "BLE custom user data #12"
        },
        {
            "input_name": "ble_user_data_13",
            "description": "BLE custom user data #13"
        },
        {
            "input_name": "ble_user_data_14",
            "description": "BLE custom user data #14"
        },
        {
            "input_name": "ble_user_data_15",
            "description": "BLE custom user data #15"
        },
        {
            "input_name": "ble_user_data_16",
            "description": "BLE custom user data #16"
        },
        {
            "input_name": "ble_user_data_17",
            "description": "BLE custom user data #17"
        },
        {
            "input_name": "ble_user_data_18",
            "description": "BLE custom user data #18"
        },
        {
            "input_name": "ble_user_data_19",
            "description": "BLE custom user data #19"
        },
        {
            "input_name": "ble_user_data_2",
            "description": "BLE custom user data #2"
        },
        {
            "input_name": "ble_user_data_20",
            "description": "BLE custom user data #20"
        },
        {
            "input_name": "ble_user_data_21",
            "description": "BLE custom user data #21"
        },
        {
            "input_name": "ble_user_data_22",
            "description": "BLE custom user data #22"
        },
        {
            "input_name": "ble_user_data_23",
            "description": "BLE custom user data #23"
        },
        {
            "input_name": "ble_user_data_24",
            "description": "BLE custom user data #24"
        },
        {
            "input_name": "ble_user_data_25",
            "description": "BLE custom user data #25"
        },
        {
            "input_name": "ble_user_data_26",
            "description": "BLE custom user data #26"
        },
        {
            "input_name": "ble_user_data_27",
            "description": "BLE custom user data #27"
        },
        {
            "input_name": "ble_user_data_28",
            "description": "BLE custom user data #28"
        },
        {
            "input_name": "ble_user_data_29",
            "description": "BLE custom user data #29"
        },
        {
            "input_name": "ble_user_data_3",
            "description": "BLE custom user data #3"
        },
        {
            "input_name": "ble_user_data_30",
            "description": "BLE custom user data #30"
        },
        {
            "input_name": "ble_user_data_31",
            "description": "BLE custom user data #31"
        },
        {
            "input_name": "ble_user_data_32",
            "description": "BLE custom user data #32"
        },
        {
            "input_name": "ble_user_data_33",
            "description": "BLE custom user data #33"
        },
        {
            "input_name": "ble_user_data_34",
            "description": "BLE custom user data #34"
        },
        {
            "input_name": "ble_user_data_35",
            "description": "BLE custom user data #35"
        },
        {
            "input_name": "ble_user_data_36",
            "description": "BLE custom user data #36"
        },
        {
            "input_name": "ble_user_data_37",
            "description": "BLE custom user data #37"
        },
        {
            "input_name": "ble_user_data_38",
            "description": "BLE custom user data #38"
        },
        {
            "input_name": "ble_user_data_39",
            "description": "BLE custom user data #39"
        },
        {
            "input_name": "ble_user_data_4",
            "description": "BLE custom user data #4"
        },
        {
            "input_name": "ble_user_data_40",
            "description": "BLE custom user data #40"
        },
        {
            "input_name": "ble_user_data_41",
            "description": "BLE custom user data #41"
        },
        {
            "input_name": "ble_user_data_42",
            "description": "BLE custom user data #42"
        },
        {
            "input_name": "ble_user_data_43",
            "description": "BLE custom user data #43"
        },
        {
            "input_name": "ble_user_data_44",
            "description": "BLE custom user data #44"
        },
        {
            "input_name": "ble_user_data_45",
            "description": "BLE custom user data #45"
        },
        {
            "input_name": "ble_user_data_46",
            "description": "BLE custom user data #46"
        },
        {
            "input_name": "ble_user_data_47",
            "description": "BLE custom user data #47"
        },
        {
            "input_name": "ble_user_data_48",
            "description": "BLE custom user data #48"
        },
        {
            "input_name": "ble_user_data_49",
            "description": "BLE custom user data #49"
        },
        {
            "input_name": "ble_user_data_5",
            "description": "BLE custom user data #5"
        },
        {
            "input_name": "ble_user_data_50",
            "description": "BLE custom user data #50"
        },
        {
            "input_name": "ble_user_data_6",
            "description": "BLE custom user data #6"
        },
        {
            "input_name": "ble_user_data_7",
            "description": "BLE custom user data #7"
        },
        {
            "input_name": "ble_user_data_8",
            "description": "BLE custom user data #8"
        },
        {
            "input_name": "ble_user_data_9",
            "description": "BLE custom user data #9"
        },
        {
            "input_name": "board_voltage",
            "description": "Board voltage"
        },
        {
            "input_name": "braking",
            "description": "Braking"
        },
        {
            "input_name": "can_adblue_level",
            "description": "CAN: Level of AdBlue fluid"
        },
        {
            "input_name": "can_axle_load_1",
            "description": "CAN: Axle #1 load"
        },
        {
            "input_name": "can_axle_load_10",
            "description": "CAN: Axle #10 load"
        },
        {
            "input_name": "can_axle_load_11",
            "description": "CAN: Axle #11 load"
        },
        {
            "input_name": "can_axle_load_12",
            "description": "CAN: Axle #12 load"
        },
        {
            "input_name": "can_axle_load_13",
            "description": "CAN: Axle #13 load"
        },
        {
            "input_name": "can_axle_load_14",
            "description": "CAN: Axle #14 load"
        },
        {
            "input_name": "can_axle_load_15",
            "description": "CAN: Axle #15 load"
        },
        {
            "input_name": "can_axle_load_2",
            "description": "CAN: Axle #2 load"
        },
        {
            "input_name": "can_axle_load_3",
            "description": "CAN: Axle #3 load"
        },
        {
            "input_name": "can_axle_load_4",
            "description": "CAN: Axle #4 load"
        },
        {
            "input_name": "can_axle_load_5",
            "description": "CAN: Axle #5 load"
        },
        {
            "input_name": "can_axle_load_6",
            "description": "CAN: Axle #6 load"
        },
        {
            "input_name": "can_axle_load_7",
            "description": "CAN: Axle #7 load"
        },
        {
            "input_name": "can_axle_load_8",
            "description": "CAN: Axle #8 load"
        },
        {
            "input_name": "can_axle_load_9",
            "description": "CAN: Axle #9 load"
        },
        {
            "input_name": "can_consumption",
            "description": "CAN: Total fuel used"
        },
        {
            "input_name": "can_consumption_relative",
            "description": "CAN: Relative fuel consumption"
        },
        {
            "input_name": "can_coolant_t",
            "description": "CAN: Coolant temperature"
        },
        {
            "input_name": "can_engine_hours",
            "description": "CAN: Engine hours"
        },
        {
            "input_name": "can_engine_hours_relative",
            "description": "CAN: Relative engine hours"
        },
        {
            "input_name": "can_engine_load",
            "description": "CAN: Engine load"
        },
        {
            "input_name": "can_engine_revolutions",
            "description": "CAN: Total engine revolutions"
        },
        {
            "input_name": "can_engine_temp",
            "description": "CAN: Engine temp."
        },
        {
            "input_name": "can_fuel",
            "description": "CAN: Fuel level"
        },
        {
            "input_name": "can_fuel_2",
            "description": "CAN: Fuel level #2"
        },
        {
            "input_name": "can_fuel_economy",
            "description": "CAN: Fuel consumption"
        },
        {
            "input_name": "can_fuel_litres",
            "description": "CAN: Fuel (litres)"
        },
        {
            "input_name": "can_fuel_rate",
            "description": "CAN: Instant fuel rate"
        },
        {
            "input_name": "can_intake_air_t",
            "description": "CAN: Intake air temp."
        },
        {
            "input_name": "can_mileage",
            "description": "CAN: Mileage"
        },
        {
            "input_name": "can_mileage_relative",
            "description": "CAN: Relative mileage"
        },
        {
            "input_name": "can_pto_duration",
            "description": "CAN: Total duration of PTO when stand still"
        },
        {
            "input_name": "can_pto_fuel_used",
            "description": "CAN: Total fuel used during PTO when stand still"
        },
        {
            "input_name": "can_r_prefix",
            "description": "CAN: R-prefix"
        },
        {
            "input_name": "can_rpm",
            "description": "CAN: RPM"
        },
        {
            "input_name": "can_speed",
            "description": "CAN: Speed"
        },
        {
            "input_name": "can_throttle",
            "description": "CAN: Throttle"
        },
        {
            "input_name": "composite",
            "description": "input.composite"
        },
        {
            "input_name": "cornering",
            "description": "Cornering"
        },
        {
            "input_name": "ext_battery_voltage",
            "description": "External battery voltage"
        },
        {
            "input_name": "ext_temp_sensor_1",
            "description": "External temperature #1"
        },
        {
            "input_name": "ext_temp_sensor_10",
            "description": "External temperature #10"
        },
        {
            "input_name": "ext_temp_sensor_2",
            "description": "External temperature #2"
        },
        {
            "input_name": "ext_temp_sensor_3",
            "description": "External temperature #3"
        },
        {
            "input_name": "ext_temp_sensor_4",
            "description": "External temperature #4"
        },
        {
            "input_name": "ext_temp_sensor_5",
            "description": "External temperature #5"
        },
        {
            "input_name": "ext_temp_sensor_6",
            "description": "External temperature #6"
        },
        {
            "input_name": "ext_temp_sensor_7",
            "description": "External temperature #7"
        },
        {
            "input_name": "ext_temp_sensor_8",
            "description": "External temperature #8"
        },
        {
            "input_name": "ext_temp_sensor_9",
            "description": "External temperature #9"
        },
        {
            "input_name": "freq_1",
            "description": "Frequency sensor #1"
        },
        {
            "input_name": "freq_2",
            "description": "Frequency sensor #2"
        },
        {
            "input_name": "freq_3",
            "description": "Frequency sensor #3"
        },
        {
            "input_name": "freq_4",
            "description": "Frequency sensor #4"
        },
        {
            "input_name": "freq_5",
            "description": "Frequency sensor #5"
        },
        {
            "input_name": "freq_6",
            "description": "Frequency sensor #6"
        },
        {
            "input_name": "freq_7",
            "description": "Frequency sensor #7"
        },
        {
            "input_name": "freq_8",
            "description": "Frequency sensor #8"
        },
        {
            "input_name": "fuel_consumption",
            "description": "Fuel consumption"
        },
        {
            "input_name": "fuel_frequency",
            "description": "LLS: Frequency"
        },
        {
            "input_name": "fuel_level",
            "description": "LLS: Level"
        },
        {
            "input_name": "fuel_temperature",
            "description": "LLS: Temperature"
        },
        {
            "input_name": "humidity_1",
            "description": "Relative humidity sensor #1"
        },
        {
            "input_name": "humidity_2",
            "description": "Relative humidity sensor #2"
        },
        {
            "input_name": "humidity_3",
            "description": "Relative humidity sensor #3"
        },
        {
            "input_name": "humidity_4",
            "description": "Relative humidity sensor #4"
        },
        {
            "input_name": "hw_mileage",
            "description": "Mileage"
        },
        {
            "input_name": "impulse_counter_1",
            "description": "Impulse counter #1"
        },
        {
            "input_name": "impulse_counter_2",
            "description": "Impulse counter #2"
        },
        {
            "input_name": "impulse_counter_3",
            "description": "Impulse counter #3"
        },
        {
            "input_name": "impulse_counter_4",
            "description": "Impulse counter #4"
        },
        {
            "input_name": "impulse_counter_5",
            "description": "Impulse counter #5"
        },
        {
            "input_name": "impulse_counter_6",
            "description": "Impulse counter #6"
        },
        {
            "input_name": "impulse_counter_7",
            "description": "Impulse counter #7"
        },
        {
            "input_name": "impulse_counter_8",
            "description": "Impulse counter #8"
        },
        {
            "input_name": "input_status",
            "description": "input.input_status"
        },
        {
            "input_name": "lls_level_1",
            "description": "LLS #1: Level"
        },
        {
            "input_name": "lls_level_10",
            "description": "LLS #10: Level"
        },
        {
            "input_name": "lls_level_11",
            "description": "LLS #11: Level"
        },
        {
            "input_name": "lls_level_12",
            "description": "LLS #12: Level"
        },
        {
            "input_name": "lls_level_13",
            "description": "LLS #13: Level"
        },
        {
            "input_name": "lls_level_14",
            "description": "LLS #14: Level"
        },
        {
            "input_name": "lls_level_15",
            "description": "LLS #15: Level"
        },
        {
            "input_name": "lls_level_16",
            "description": "LLS #16: Level"
        },
        {
            "input_name": "lls_level_2",
            "description": "LLS #2: Level"
        },
        {
            "input_name": "lls_level_3",
            "description": "LLS #3: Level"
        },
        {
            "input_name": "lls_level_4",
            "description": "LLS #4: Level"
        },
        {
            "input_name": "lls_level_5",
            "description": "LLS #5: Level"
        },
        {
            "input_name": "lls_level_6",
            "description": "LLS #6: Level"
        },
        {
            "input_name": "lls_level_7",
            "description": "LLS #7: Level"
        },
        {
            "input_name": "lls_level_8",
            "description": "LLS #8: Level"
        },
        {
            "input_name": "lls_level_9",
            "description": "LLS #9: Level"
        },
        {
            "input_name": "lls_level_raw_1",
            "description": "LLS #1: Level (raw)"
        },
        {
            "input_name": "lls_level_raw_2",
            "description": "LLS #2: Level (raw)"
        },
        {
            "input_name": "lls_level_raw_3",
            "description": "LLS #3: Level (raw)"
        },
        {
            "input_name": "lls_level_raw_4",
            "description": "LLS #4: Level (raw)"
        },
        {
            "input_name": "lls_level_raw_5",
            "description": "LLS #5: Level (raw)"
        },
        {
            "input_name": "lls_level_raw_6",
            "description": "LLS #6: Level (raw)"
        },
        {
            "input_name": "lls_level_raw_7",
            "description": "LLS #7: Level (raw)"
        },
        {
            "input_name": "lls_level_raw_8",
            "description": "LLS #8: Level (raw)"
        },
        {
            "input_name": "lls_temperature_1",
            "description": "LLS #1: Temperature"
        },
        {
            "input_name": "lls_temperature_10",
            "description": "LLS #10: Temperature"
        },
        {
            "input_name": "lls_temperature_11",
            "description": "LLS #11: Temperature"
        },
        {
            "input_name": "lls_temperature_12",
            "description": "LLS #12: Temperature"
        },
        {
            "input_name": "lls_temperature_13",
            "description": "LLS #13: Temperature"
        },
        {
            "input_name": "lls_temperature_14",
            "description": "LLS #14: Temperature"
        },
        {
            "input_name": "lls_temperature_15",
            "description": "LLS #15: Temperature"
        },
        {
            "input_name": "lls_temperature_16",
            "description": "LLS #16: Temperature"
        },
        {
            "input_name": "lls_temperature_2",
            "description": "LLS #2: Temperature"
        },
        {
            "input_name": "lls_temperature_3",
            "description": "LLS #3: Temperature"
        },
        {
            "input_name": "lls_temperature_4",
            "description": "LLS #4: Temperature"
        },
        {
            "input_name": "lls_temperature_5",
            "description": "LLS #5: Temperature"
        },
        {
            "input_name": "lls_temperature_6",
            "description": "LLS #6: Temperature"
        },
        {
            "input_name": "lls_temperature_7",
            "description": "LLS #7: Temperature"
        },
        {
            "input_name": "lls_temperature_8",
            "description": "LLS #8: Temperature"
        },
        {
            "input_name": "lls_temperature_9",
            "description": "LLS #9: Temperature"
        },
        {
            "input_name": "obd_absolute_load_value",
            "description": "Absolute load value"
        },
        {
            "input_name": "obd_consumption",
            "description": "OBD: Fuel consumption"
        },
        {
            "input_name": "obd_control_module_voltage",
            "description": "Control module voltage"
        },
        {
            "input_name": "obd_coolant_t",
            "description": "OBD: Coolant temperature"
        },
        {
            "input_name": "obd_custom_fuel_litres",
            "description": "OBD: Real Fuel (litres)"
        },
        {
            "input_name": "obd_custom_odometer",
            "description": "OBD: Odometer"
        },
        {
            "input_name": "obd_engine_load",
            "description": "OBD: Engine load"
        },
        {
            "input_name": "obd_fuel",
            "description": "OBD: Fuel"
        },
        {
            "input_name": "obd_intake_air_pressure",
            "description": "OBD: Intake air pressure"
        },
        {
            "input_name": "obd_intake_air_t",
            "description": "OBD: Intake air temp."
        },
        {
            "input_name": "obd_mil_run_time",
            "description": "Time run with MIL on"
        },
        {
            "input_name": "obd_oil_temperature",
            "description": "OBD: Oil temperature"
        },
        {
            "input_name": "obd_rpm",
            "description": "OBD: RPM"
        },
        {
            "input_name": "obd_speed",
            "description": "OBD: Speed"
        },
        {
            "input_name": "obd_throttle",
            "description": "OBD: Throttle"
        },
        {
            "input_name": "obd_time_since_engine_start",
            "description": "Run time since engine start"
        },
        {
            "input_name": "passengers_entered_1",
            "description": "Passenger counter #1: Entry"
        },
        {
            "input_name": "passengers_entered_2",
            "description": "Passenger counter #2: Entry"
        },
        {
            "input_name": "passengers_entered_3",
            "description": "Passenger counter #3: Entry"
        },
        {
            "input_name": "passengers_entered_4",
            "description": "Passenger counter #4: Entry"
        },
        {
            "input_name": "passengers_entered_5",
            "description": "Passenger counter #5: Entry"
        },
        {
            "input_name": "passengers_entered_6",
            "description": "Passenger counter #6: Entry"
        },
        {
            "input_name": "passengers_entered_7",
            "description": "Passenger counter #7: Entry"
        },
        {
            "input_name": "passengers_entered_8",
            "description": "Passenger counter #8: Entry"
        },
        {
            "input_name": "passengers_exit_1",
            "description": "Passenger counter #1: Exit"
        },
        {
            "input_name": "passengers_exit_2",
            "description": "Passenger counter #2: Exit"
        },
        {
            "input_name": "passengers_exit_3",
            "description": "Passenger counter #3: Exit"
        },
        {
            "input_name": "passengers_exit_4",
            "description": "Passenger counter #4: Exit"
        },
        {
            "input_name": "passengers_exit_5",
            "description": "Passenger counter #5: Exit"
        },
        {
            "input_name": "passengers_exit_6",
            "description": "Passenger counter #6: Exit"
        },
        {
            "input_name": "passengers_exit_7",
            "description": "Passenger counter #7: Exit"
        },
        {
            "input_name": "passengers_exit_8",
            "description": "Passenger counter #8: Exit"
        },
        {
            "input_name": "physiologic_blood_pressure_dt",
            "description": "Diastolic blood pressure"
        },
        {
            "input_name": "physiologic_blood_pressure_st",
            "description": "Systolic blood pressure"
        },
        {
            "input_name": "physiologic_heart_rate",
            "description": "Heart rate"
        },
        {
            "input_name": "raw_can_1",
            "description": "CAN: Raw data #1"
        },
        {
            "input_name": "raw_can_10",
            "description": "CAN: Raw data #10"
        },
        {
            "input_name": "raw_can_11",
            "description": "CAN: Raw data #11"
        },
        {
            "input_name": "raw_can_12",
            "description": "CAN: Raw data #12"
        },
        {
            "input_name": "raw_can_13",
            "description": "CAN: Raw data #13"
        },
        {
            "input_name": "raw_can_14",
            "description": "CAN: Raw data #14"
        },
        {
            "input_name": "raw_can_15",
            "description": "CAN: Raw data #15"
        },
        {
            "input_name": "raw_can_16",
            "description": "CAN: Raw data #16"
        },
        {
            "input_name": "raw_can_2",
            "description": "CAN: Raw data #2"
        },
        {
            "input_name": "raw_can_3",
            "description": "CAN: Raw data #3"
        },
        {
            "input_name": "raw_can_4",
            "description": "CAN: Raw data #4"
        },
        {
            "input_name": "raw_can_5",
            "description": "CAN: Raw data #5"
        },
        {
            "input_name": "raw_can_6",
            "description": "CAN: Raw data #6"
        },
        {
            "input_name": "raw_can_7",
            "description": "CAN: Raw data #7"
        },
        {
            "input_name": "raw_can_8",
            "description": "CAN: Raw data #8"
        },
        {
            "input_name": "raw_can_9",
            "description": "CAN: Raw data #9"
        },
        {
            "input_name": "rs232_1",
            "description": "RS-232 #1"
        },
        {
            "input_name": "rs232_2",
            "description": "RS-232 #2"
        },
        {
            "input_name": "rs232_3",
            "description": "RS-232 #3"
        },
        {
            "input_name": "rs232_4",
            "description": "RS-232 #4"
        },
        {
            "input_name": "rs232_5",
            "description": "RS-232 #5"
        },
        {
            "input_name": "rs232_6",
            "description": "RS-232 #6"
        },
        {
            "input_name": "tacho_mileage",
            "description": "TACHO: Mileage"
        },
        {
            "input_name": "tacho_speed",
            "description": "TACHO: Speed"
        },
        {
            "input_name": "temp_sensor",
            "description": "Temperature"
        },
        {
            "input_name": "tire_pressure_1",
            "description": "Tire pressure #1"
        },
        {
            "input_name": "tire_pressure_10",
            "description": "Tire pressure #10"
        },
        {
            "input_name": "tire_pressure_11",
            "description": "Tire pressure #11"
        },
        {
            "input_name": "tire_pressure_12",
            "description": "Tire pressure #12"
        },
        {
            "input_name": "tire_pressure_13",
            "description": "Tire pressure #13"
        },
        {
            "input_name": "tire_pressure_14",
            "description": "Tire pressure #14"
        },
        {
            "input_name": "tire_pressure_15",
            "description": "Tire pressure #15"
        },
        {
            "input_name": "tire_pressure_16",
            "description": "Tire pressure #16"
        },
        {
            "input_name": "tire_pressure_17",
            "description": "Tire pressure #17"
        },
        {
            "input_name": "tire_pressure_18",
            "description": "Tire pressure #18"
        },
        {
            "input_name": "tire_pressure_19",
            "description": "Tire pressure #19"
        },
        {
            "input_name": "tire_pressure_2",
            "description": "Tire pressure #2"
        },
        {
            "input_name": "tire_pressure_20",
            "description": "Tire pressure #20"
        },
        {
            "input_name": "tire_pressure_21",
            "description": "Tire pressure #21"
        },
        {
            "input_name": "tire_pressure_22",
            "description": "Tire pressure #22"
        },
        {
            "input_name": "tire_pressure_23",
            "description": "Tire pressure #23"
        },
        {
            "input_name": "tire_pressure_24",
            "description": "Tire pressure #24"
        },
        {
            "input_name": "tire_pressure_25",
            "description": "Tire pressure #25"
        },
        {
            "input_name": "tire_pressure_26",
            "description": "Tire pressure #26"
        },
        {
            "input_name": "tire_pressure_27",
            "description": "Tire pressure #27"
        },
        {
            "input_name": "tire_pressure_28",
            "description": "Tire pressure #28"
        },
        {
            "input_name": "tire_pressure_29",
            "description": "Tire pressure #29"
        },
        {
            "input_name": "tire_pressure_3",
            "description": "Tire pressure #3"
        },
        {
            "input_name": "tire_pressure_30",
            "description": "Tire pressure #30"
        },
        {
            "input_name": "tire_pressure_4",
            "description": "Tire pressure #4"
        },
        {
            "input_name": "tire_pressure_5",
            "description": "Tire pressure #5"
        },
        {
            "input_name": "tire_pressure_6",
            "description": "Tire pressure #6"
        },
        {
            "input_name": "tire_pressure_7",
            "description": "Tire pressure #7"
        },
        {
            "input_name": "tire_pressure_8",
            "description": "Tire pressure #8"
        },
        {
            "input_name": "tire_pressure_9",
            "description": "Tire pressure #9"
        },
        {
            "input_name": "tire_temperature_1",
            "description": "Tire air temperature #1"
        },
        {
            "input_name": "tire_temperature_10",
            "description": "Tire air temperature #10"
        },
        {
            "input_name": "tire_temperature_11",
            "description": "Tire air temperature #11"
        },
        {
            "input_name": "tire_temperature_12",
            "description": "Tire air temperature #12"
        },
        {
            "input_name": "tire_temperature_13",
            "description": "Tire air temperature #13"
        },
        {
            "input_name": "tire_temperature_14",
            "description": "Tire air temperature #14"
        },
        {
            "input_name": "tire_temperature_15",
            "description": "Tire air temperature #15"
        },
        {
            "input_name": "tire_temperature_16",
            "description": "Tire air temperature #16"
        },
        {
            "input_name": "tire_temperature_17",
            "description": "Tire air temperature #17"
        },
        {
            "input_name": "tire_temperature_18",
            "description": "Tire air temperature #18"
        },
        {
            "input_name": "tire_temperature_19",
            "description": "Tire air temperature #19"
        },
        {
            "input_name": "tire_temperature_2",
            "description": "Tire air temperature #2"
        },
        {
            "input_name": "tire_temperature_20",
            "description": "Tire air temperature #20"
        },
        {
            "input_name": "tire_temperature_21",
            "description": "Tire air temperature #21"
        },
        {
            "input_name": "tire_temperature_22",
            "description": "Tire air temperature #22"
        },
        {
            "input_name": "tire_temperature_23",
            "description": "Tire air temperature #23"
        },
        {
            "input_name": "tire_temperature_24",
            "description": "Tire air temperature #24"
        },
        {
            "input_name": "tire_temperature_25",
            "description": "Tire air temperature #25"
        },
        {
            "input_name": "tire_temperature_26",
            "description": "Tire air temperature #26"
        },
        {
            "input_name": "tire_temperature_27",
            "description": "Tire air temperature #27"
        },
        {
            "input_name": "tire_temperature_28",
            "description": "Tire air temperature #28"
        },
        {
            "input_name": "tire_temperature_29",
            "description": "Tire air temperature #29"
        },
        {
            "input_name": "tire_temperature_3",
            "description": "Tire air temperature #3"
        },
        {
            "input_name": "tire_temperature_30",
            "description": "Tire air temperature #30"
        },
        {
            "input_name": "tire_temperature_4",
            "description": "Tire air temperature #4"
        },
        {
            "input_name": "tire_temperature_5",
            "description": "Tire air temperature #5"
        },
        {
            "input_name": "tire_temperature_6",
            "description": "Tire air temperature #6"
        },
        {
            "input_name": "tire_temperature_7",
            "description": "Tire air temperature #7"
        },
        {
            "input_name": "tire_temperature_8",
            "description": "Tire air temperature #8"
        },
        {
            "input_name": "tire_temperature_9",
            "description": "Tire air temperature #9"
        },
        {
            "input_name": "uds_adblue_tanklevel_absolut",
            "description": "UDS: Level of AdBlue fluid"
        },
        {
            "input_name": "uds_adblue_tanklevel_percent",
            "description": "UDS: Level of AdBlue fluid (percent)"
        },
        {
            "input_name": "uds_ambient_air_temp",
            "description": "UDS: Ambient air temperature"
        },
        {
            "input_name": "uds_battery_state_percent",
            "description": "UDS: Battery level"
        },
        {
            "input_name": "uds_battery_voltage",
            "description": "UDS: Battery voltage"
        },
        {
            "input_name": "uds_consumption",
            "description": "UDS: Fuel consumption"
        },
        {
            "input_name": "uds_consumption_average",
            "description": "UDS: Average fuel consumption"
        },
        {
            "input_name": "uds_consumption_average_high",
            "description": "UDS: Average high fuel consumption"
        },
        {
            "input_name": "uds_consumption_average_low",
            "description": "UDS: Average low fuel consumption"
        },
        {
            "input_name": "uds_consumption_since_reset",
            "description": "UDS: Fuel consumption since reset"
        },
        {
            "input_name": "uds_eco_co2_score",
            "description": "UDS: Environmental score"
        },
        {
            "input_name": "uds_engine_coolant_temp",
            "description": "UDS: Coolant temperature"
        },
        {
            "input_name": "uds_engine_oil_temperature",
            "description": "UDS: Oil temperature"
        },
        {
            "input_name": "uds_fuel_tank_level_absolute",
            "description": "UDS: Fuel level"
        },
        {
            "input_name": "uds_fuel_tank_level_percent",
            "description": "UDS: Fuel level (percent)"
        },
        {
            "input_name": "uds_odometer",
            "description": "UDS: Odometer"
        },
        {
            "input_name": "uds_rpm",
            "description": "UDS: RPM"
        },
        {
            "input_name": "uds_service_days_since_last",
            "description": "UDS: Days since last service"
        },
        {
            "input_name": "uds_service_distance_snc_lst",
            "description": "UDS: Km since last service"
        },
        {
            "input_name": "uds_service_interval_days",
            "description": "UDS: Days till next service"
        },
        {
            "input_name": "uds_service_interval_distance",
            "description": "UDS: Distance to drive till next service"
        },
        {
            "input_name": "uds_service_max_days",
            "description": "UDS: Max days of service interval"
        },
        {
            "input_name": "uds_service_max_distance",
            "description": "UDS: Max km of service interval"
        },
        {
            "input_name": "uds_speed",
            "description": "UDS: Speed"
        },
        {
            "input_name": "uds_steer_angle",
            "description": "UDS: Steer angle"
        },
        {
            "input_name": "uds_tank_level_cng_percent",
            "description": "UDS: Cng fuel tank level (percent)"
        },
        {
            "input_name": "uds_throttle",
            "description": "UDS: Throttle"
        },
        {
            "input_name": "uds_time_since_engine_start",
            "description": "UDS: Run time since engine start"
        },
        {
            "input_name": "uds_tire_pressure_front_left",
            "description": "UDS: Tire pressure front left"
        },
        {
            "input_name": "uds_tire_pressure_front_right",
            "description": "UDS: Tire pressure front right"
        },
        {
            "input_name": "uds_tire_pressure_rear_left",
            "description": "UDS: Tire pressure rear left"
        },
        {
            "input_name": "uds_tire_pressure_rear_right",
            "description": "UDS: Tire pressure rear right"
        },
        {
            "input_name": "user_data_1",
            "description": "Custom user data #1"
        },
        {
            "input_name": "user_data_10",
            "description": "Custom user data #10"
        },
        {
            "input_name": "user_data_11",
            "description": "Custom user data #11"
        },
        {
            "input_name": "user_data_12",
            "description": "Custom user data #12"
        },
        {
            "input_name": "user_data_13",
            "description": "Custom user data #13"
        },
        {
            "input_name": "user_data_14",
            "description": "Custom user data #14"
        },
        {
            "input_name": "user_data_15",
            "description": "Custom user data #15"
        },
        {
            "input_name": "user_data_16",
            "description": "Custom user data #16"
        },
        {
            "input_name": "user_data_17",
            "description": "Custom user data #17"
        },
        {
            "input_name": "user_data_18",
            "description": "Custom user data #18"
        },
        {
            "input_name": "user_data_19",
            "description": "Custom user data #19"
        },
        {
            "input_name": "user_data_2",
            "description": "Custom user data #2"
        },
        {
            "input_name": "user_data_20",
            "description": "Custom user data #20"
        },
        {
            "input_name": "user_data_21",
            "description": "Custom user data #21"
        },
        {
            "input_name": "user_data_22",
            "description": "Custom user data #22"
        },
        {
            "input_name": "user_data_23",
            "description": "Custom user data #23"
        },
        {
            "input_name": "user_data_24",
            "description": "Custom user data #24"
        },
        {
            "input_name": "user_data_25",
            "description": "Custom user data #25"
        },
        {
            "input_name": "user_data_26",
            "description": "Custom user data #26"
        },
        {
            "input_name": "user_data_27",
            "description": "Custom user data #27"
        },
        {
            "input_name": "user_data_28",
            "description": "Custom user data #28"
        },
        {
            "input_name": "user_data_29",
            "description": "Custom user data #29"
        },
        {
            "input_name": "user_data_3",
            "description": "Custom user data #3"
        },
        {
            "input_name": "user_data_30",
            "description": "Custom user data #30"
        },
        {
            "input_name": "user_data_31",
            "description": "Custom user data #31"
        },
        {
            "input_name": "user_data_32",
            "description": "Custom user data #32"
        },
        {
            "input_name": "user_data_4",
            "description": "Custom user data #4"
        },
        {
            "input_name": "user_data_5",
            "description": "Custom user data #5"
        },
        {
            "input_name": "user_data_6",
            "description": "Custom user data #6"
        },
        {
            "input_name": "user_data_7",
            "description": "Custom user data #7"
        },
        {
            "input_name": "user_data_8",
            "description": "Custom user data #8"
        },
        {
            "input_name": "user_data_9",
            "description": "Custom user data #9"
        }
        ]
    }
    ```

#### Errors

[General](../../../../getting-started/errors.md#error-codes) types only.
