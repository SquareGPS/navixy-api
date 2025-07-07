---
title: Sensor inputs
description: API call to get descriptions of all sensor inputs existing in the system.
---

# Input name

API base path: `/tracker/sensor/input_name`.

API call to get all sensor inputs and state fields existing in the system and their descriptions.

## API actions

### list

This will provide translations of all sensor inputs and state fields present in the system.\
These translations (field `description` in response) will be given in the language according to the user's locale.\
For state fields, the value type and descriptions (translations) of possible values are also provided if available.

#### Parameters

Only API key `hash`.

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/tracker/sensor/input_name/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
https://api.eu.navixy.com/v2/tracker/sensor/input_name/list?hash=a6aa75587e5c59c32d347da438505fc3
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

For every input following properties returned: `input_name` and `description`.

`input_name` is an enum member, same as in [sensor object](index.md).

`description` is made in current user's language (according to [locale settings](../../../commons/user/settings/index.md)).

<details>

<summary>Example response</summary>

```json
{
  "list": [
    {
      "input_name": "acceleration",
      "description": "Acceleration"
    },
    {
      "input_name": "air_pressure",
      "description": "Air pressure"
    },
    {
      "input_name": "alt_large_assign",
      "description": "ALT large assign [N]"
    },
    {
      "input_name": "alt_medium_assign",
      "description": "ALT medium assign [N]"
    },
    {
      "input_name": "alt_small_assign",
      "description": "ALT small assign [N]"
    },
    {
      "input_name": "analog",
      "description": "Analog sensor [N]"
    },
    {
      "input_name": "avl_io",
      "description": "AVL IO [N]"
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
      "input_name": "battery_level_of",
      "description": "Battery level [N]"
    },
    {
      "input_name": "battery_voltage",
      "description": "Battery voltage"
    },
    {
      "input_name": "ble_analog",
      "description": "BLE: Analog [N]"
    },
    {
      "input_name": "ble_battery_level",
      "description": "BLE: Battery level [N]"
    },
    {
      "input_name": "ble_battery_voltage",
      "description": "BLE: Battery voltage [N]"
    },
    {
      "input_name": "ble_frequency",
      "description": "BLE: LLS frequency [N]"
    },
    {
      "input_name": "ble_humidity",
      "description": "BLE: Humidity sensor [N]"
    },
    {
      "input_name": "ble_input_status",
      "description": "BLE: Input status [N]"
    },
    {
      "input_name": "ble_lls_height",
      "description": "BLE: LLS height [N]"
    },
    {
      "input_name": "ble_lls_level",
      "description": "BLE: LLS level [N]"
    },
    {
      "input_name": "ble_lls_level_raw",
      "description": "BLE: LLS level raw [N]"
    },
    {
      "input_name": "ble_lls_pressure",
      "description": "BLE: LLS pressure [N]"
    },
    {
      "input_name": "ble_lls_temperature",
      "description": "BLE: LLS temperature [N]"
    },
    {
      "input_name": "ble_luminosity",
      "description": "BLE: Luminosity [N]"
    },
    {
      "input_name": "ble_output_status",
      "description": "BLE: Output status [N]"
    },
    {
      "input_name": "ble_pitch",
      "description": "BLE: Pitch angle [N]"
    },
    {
      "input_name": "ble_roll",
      "description": "BLE: Roll angle [N]"
    },
    {
      "input_name": "ble_signal_strength",
      "description": "BLE: Signal strength [N]"
    },
    {
      "input_name": "ble_temp_sensor",
      "description": "BLE: Temperature sensor [N]"
    },
    {
      "input_name": "ble_tire_pressure",
      "description": "BLE: Tire pressure [N]"
    },
    {
      "input_name": "ble_tire_temperature",
      "description": "BLE: Tire air temperature [N]"
    },
    {
      "input_name": "ble_user_data",
      "description": "BLE: Custom user data [N]"
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
      "input_name": "calamp_accum",
      "description": "CalAmp Accumulator [N]"
    },
    {
      "input_name": "can_16bit_r",
      "description": "CAN16BITR [N]"
    },
    {
      "input_name": "can_32bit_r",
      "description": "CAN32BITR [N]"
    },
    {
      "input_name": "can_8bit_r",
      "description": "CAN8BITR [N]"
    },
    {
      "input_name": "can_adblue_level",
      "description": "CAN: Level of AdBlue fluid"
    },
    {
      "input_name": "can_alternator_current",
      "description": "CAN: Alternator current"
    },
    {
      "input_name": "can_alternator_voltage",
      "description": "CAN: Alternator voltage"
    },
    {
      "input_name": "can_ambient_air_temp",
      "description": "CAN: Ambient air temperature"
    },
    {
      "input_name": "can_avg_fuel_economy",
      "description": "CAN: Average fuel economy"
    },
    {
      "input_name": "can_axle_load",
      "description": "CAN: Axle load [N]"
    },
    {
      "input_name": "can_barometric_pressure",
      "description": "CAN: Barometric pressure"
    },
    {
      "input_name": "can_battery_level",
      "description": "CAN: Battery level (SoC)"
    },
    {
      "input_name": "can_battery_potential",
      "description": "CAN: Battery potential"
    },
    {
      "input_name": "can_battery_temperature",
      "description": "CAN: Battery temperature"
    },
    {
      "input_name": "can_battery_voltage",
      "description": "CAN: Battery voltage"
    },
    {
      "input_name": "can_bellow_press_front_left",
      "description": "CAN: Bellow pressure front left"
    },
    {
      "input_name": "can_bellow_press_front_right",
      "description": "CAN: Bellow pressure front right"
    },
    {
      "input_name": "can_bellow_press_rear_left",
      "description": "CAN: Bellow pressure rear left"
    },
    {
      "input_name": "can_bellow_press_rear_right",
      "description": "CAN: Bellow pressure rear right"
    },
    {
      "input_name": "can_brake_pedal_position",
      "description": "CAN: Brake pedal position"
    },
    {
      "input_name": "can_cab_interior_temp",
      "description": "CAN: Cab interior temperature"
    },
    {
      "input_name": "can_cargo_ambient_temp",
      "description": "CAN: Cargo ambient temperature"
    },
    {
      "input_name": "can_charging_system_voltage",
      "description": "CAN: Charging system potential (voltage)"
    },
    {
      "input_name": "can_consumption",
      "description": "CAN: Total fuel used"
    },
    {
      "input_name": "can_consumption_relative",
      "description": "CAN: Fuel consumed (counter)"
    },
    {
      "input_name": "can_coolant_level",
      "description": "CAN: Coolant level"
    },
    {
      "input_name": "can_coolant_t",
      "description": "CAN: Coolant temperature"
    },
    {
      "input_name": "can_e_battery_health",
      "description": "CAN: Battery health (SoH)"
    },
    {
      "input_name": "can_e_charger_current",
      "description": "CAN: Charger current"
    },
    {
      "input_name": "can_e_charger_current_actual",
      "description": "CAN: Charger current actual"
    },
    {
      "input_name": "can_e_charger_energy",
      "description": "CAN: Charger energy"
    },
    {
      "input_name": "can_e_charger_voltage",
      "description": "CAN: Charger voltage"
    },
    {
      "input_name": "can_e_charger_voltage_actual",
      "description": "CAN: Charger voltage actual"
    },
    {
      "input_name": "can_e_current_range",
      "description": "CAN: Current Range"
    },
    {
      "input_name": "can_e_electric_consumption",
      "description": "CAN: Power Consumption"
    },
    {
      "input_name": "can_e_full_battery_capacity",
      "description": "CAN: Full battery capacity"
    },
    {
      "input_name": "can_e_remain_battery_capacity",
      "description": "CAN: Remaining battery capacity"
    },
    {
      "input_name": "can_e_remaining_charge_time",
      "description": "CAN: Remaining charge time"
    },
    {
      "input_name": "can_eco_duration",
      "description": "CAN: ECO duration"
    },
    {
      "input_name": "can_eco_score",
      "description": "CAN: ECO score"
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
      "input_name": "can_engine_manifold_pressure",
      "description": "CAN: Engine intake manifold pressure"
    },
    {
      "input_name": "can_engine_manifold_temp",
      "description": "CAN: Engine intake manifold temperature"
    },
    {
      "input_name": "can_engine_oil_level",
      "description": "CAN: Engine oil level"
    },
    {
      "input_name": "can_engine_percent_torque",
      "description": "CAN: Actual engine percent torque"
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
      "description": "CAN: Fuel level [N]"
    },
    {
      "input_name": "can_fuel_economy",
      "description": "CAN: Fuel economy"
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
      "input_name": "can_fuel_temperature",
      "description": "CAN: Fuel temperature"
    },
    {
      "input_name": "can_gross_combo_vehicle_weight",
      "description": "CAN: Gross combination vehicle weight"
    },
    {
      "input_name": "can_idle_consumption",
      "description": "CAN: Total fuel used in idle"
    },
    {
      "input_name": "can_idle_engine_hours",
      "description": "CAN: Idle engine hours"
    },
    {
      "input_name": "can_intake_air_t",
      "description": "CAN: Intake air temp."
    },
    {
      "input_name": "can_intercooler_temperature",
      "description": "CAN: Intercooler temperature"
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
      "input_name": "can_oil_pressure",
      "description": "CAN: Engine oil pressure"
    },
    {
      "input_name": "can_oil_temperature",
      "description": "CAN: Engine oil temperature"
    },
    {
      "input_name": "can_param",
      "description": "CAN [N]"
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
      "input_name": "can_pto_oil_temperature",
      "description": "CAN: PTO oil temperature"
    },
    {
      "input_name": "can_r_prefix",
      "description": "CAN: R-prefix"
    },
    {
      "input_name": "can_road_surface_temp",
      "description": "CAN: Road surface temperature"
    },
    {
      "input_name": "can_rpm",
      "description": "CAN: RPM"
    },
    {
      "input_name": "can_service_brake_pressure",
      "description": "CAN: The pneumatic pressure in the service brake circuit or reservoir [N]"
    },
    {
      "input_name": "can_service_distance",
      "description": "CAN: Service distance"
    },
    {
      "input_name": "can_sli_battery_net_current",
      "description": "CAN: SLI battery net current [N]"
    },
    {
      "input_name": "can_speed",
      "description": "CAN: Speed"
    },
    {
      "input_name": "can_tacho_performance",
      "description": "CAN: Tachograph performance"
    },
    {
      "input_name": "can_throttle",
      "description": "CAN: Throttle"
    },
    {
      "input_name": "can_total_fuel_used",
      "description": "CAN: Engine total fuel used"
    },
    {
      "input_name": "can_total_fuel_used_gas",
      "description": "CAN: Total fuel used (gas)"
    },
    {
      "input_name": "can_total_power_takeoff_hours",
      "description": "CAN: Total power takeoff hours"
    },
    {
      "input_name": "can_transmission_oil_level",
      "description": "CAN: Transmission oil level"
    },
    {
      "input_name": "can_transmission_oil_pressure",
      "description": "CAN: Transmission oil pressure"
    },
    {
      "input_name": "can_transmission_oil_temp",
      "description": "CAN: Transmission oil temperature"
    },
    {
      "input_name": "can_trip_fuel_used",
      "description": "CAN: Engine trip fuel"
    },
    {
      "input_name": "can_trip_fuel_used_gas",
      "description": "CAN: Trip fuel (gaseous)"
    },
    {
      "input_name": "can_turbo_oil_temperature",
      "description": "CAN: Turbo oil temperature"
    },
    {
      "input_name": "can_washer_fluid_level",
      "description": "CAN: Washer fluid level"
    },
    {
      "input_name": "cornering",
      "description": "Cornering"
    },
    {
      "input_name": "cornering_rad",
      "description": "Cornering"
    },
    {
      "input_name": "counter",
      "description": "Counter [N]"
    },
    {
      "input_name": "custom_param",
      "description": "Custom [N]"
    },
    {
      "input_name": "ext_battery_voltage",
      "description": "External battery voltage"
    },
    {
      "input_name": "ext_temp_sensor",
      "description": "External temperature [N]"
    },
    {
      "input_name": "field",
      "description": "Field [N]"
    },
    {
      "input_name": "flex_id",
      "description": "Flex ID [N]"
    },
    {
      "input_name": "flex_id_signed",
      "description": "Flex ID (signed) [N]"
    },
    {
      "input_name": "freq",
      "description": "Frequency sensor [N]"
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
      "input_name": "humidity",
      "description": "Relative humidity sensor [N]"
    },
    {
      "input_name": "humidity_internal",
      "description": "Relative humidity"
    },
    {
      "input_name": "hw_mileage",
      "description": "Mileage"
    },
    {
      "input_name": "illuminance_internal",
      "description": "Illuminance"
    },
    {
      "input_name": "impulse_counter",
      "description": "Impulse counter [N]"
    },
    {
      "input_name": "io_port",
      "description": "I/O port [N]"
    },
    {
      "input_name": "lls_level",
      "description": "LLS: Level [N]"
    },
    {
      "input_name": "lls_level_raw",
      "description": "LLS: Level (raw) [N]"
    },
    {
      "input_name": "lls_temperature",
      "description": "LLS: Temperature [N]"
    },
    {
      "input_name": "modbus",
      "description": "Modbus [N]"
    },
    {
      "input_name": "obd_absolute_load_value",
      "description": "OBD: Absolute load value"
    },
    {
      "input_name": "obd_barometric_pressure",
      "description": "OBD: Barometric pressure"
    },
    {
      "input_name": "obd_consumption",
      "description": "OBD: Fuel consumption"
    },
    {
      "input_name": "obd_control_module_voltage",
      "description": "OBD: Control module voltage"
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
      "description": "OBD: Time run with MIL on"
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
      "description": "OBD: Run time since engine start"
    },
    {
      "input_name": "passengers_entered",
      "description": "Passenger counter: Entry [N]"
    },
    {
      "input_name": "passengers_exit",
      "description": "Passenger counter: Exit [N]"
    },
    {
      "input_name": "passengers_remaining",
      "description": "Passenger counter: Remaining"
    },
    {
      "input_name": "pdop",
      "description": "PDOP"
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
      "input_name": "raw_can",
      "description": "CAN: Raw data [N]"
    },
    {
      "input_name": "raw_obd",
      "description": "OBD: Raw data [N]"
    },
    {
      "input_name": "rs232",
      "description": "RS-232 [N]"
    },
    {
      "input_name": "rs485",
      "description": "RS-485 [N]"
    },
    {
      "input_name": "stt_large_assign",
      "description": "STT large assign [N]"
    },
    {
      "input_name": "stt_medium_assign",
      "description": "STT medium assign [N]"
    },
    {
      "input_name": "stt_small_assign",
      "description": "STT small assign [N]"
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
      "input_name": "tire_pressure",
      "description": "Tire pressure [N]"
    },
    {
      "input_name": "tire_sensor_battery_voltage",
      "description": "Tire sensor voltage [N]"
    },
    {
      "input_name": "tire_sensor_status",
      "description": "Tire sensor status [N]"
    },
    {
      "input_name": "tire_temperature",
      "description": "Tire air temperature [N]"
    },
    {
      "input_name": "total_passengers_entered",
      "description": "Passenger counter: Entry total [N]"
    },
    {
      "input_name": "total_passengers_exit",
      "description": "Passenger counter: Exit total [N]"
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
      "input_name": "user_data",
      "description": "Custom user data [N]"
    },
    {
      "input_name": "val",
      "description": "VAL [N]"
    },
    {
      "input_name": "vdop",
      "description": "VDOP"
    },
    {
      "input_name": "remote_ip",
      "description": "remote_ip",
      "value_type": "String"
    },
    {
      "input_name": "chat_availability",
      "description": "chat_availability",
      "value_type": "Boolean"
    },
    {
      "input_name": "stt_mode",
      "description": "STT mode",
      "value_type": "Integer"
    },
    {
      "input_name": "alt_mode",
      "description": "ALT mode",
      "value_type": "Integer"
    },
    {
      "input_name": "event_code",
      "description": "Event code",
      "value_type": "String"
    },
    {
      "input_name": "sub_event_code",
      "description": "Subevent code",
      "value_type": "String"
    },
    {
      "input_name": "event_id",
      "description": "Event ID",
      "value_type": "Integer"
    },
    {
      "input_name": "status",
      "description": "Status (state)",
      "value_type": "String"
    },
    {
      "input_name": "ext_status",
      "description": "Extended status (state)",
      "value_type": "String"
    },
    {
      "input_name": "hardware_key",
      "description": "Hardware key",
      "value_type": "String"
    },
    {
      "input_name": "new_driver_name",
      "description": "Driver name",
      "value_type": "String"
    },
    {
      "input_name": "driver_ident_state",
      "description": "Driver identified",
      "value_type": "Boolean"
    },
    {
      "input_name": "driver_code",
      "description": "driver_code",
      "value_type": "Boolean"
    },
    {
      "input_name": "moving",
      "description": "Moving",
      "value_type": "Boolean"
    },
    {
      "input_name": "strap_bolt_cut",
      "description": "Seal opened",
      "value_type": "Boolean"
    },
    {
      "input_name": "external_power_state",
      "description": "External power state",
      "value_type": "Boolean"
    },
    {
      "input_name": "charging_status",
      "description": "Charging status",
      "value_type": "Integer"
    },
    {
      "input_name": "gps_status",
      "description": "GPS status",
      "value_type": "Boolean"
    },
    {
      "input_name": "battery_health_1",
      "description": "Battery health 1",
      "value_type": "Boolean"
    },
    {
      "input_name": "battery_health_2",
      "description": "Battery health 2",
      "value_type": "Boolean"
    },
    {
      "input_name": "battery_health_3",
      "description": "Battery health 3",
      "value_type": "Boolean"
    },
    {
      "input_name": "battery_health_4",
      "description": "Battery health 4",
      "value_type": "Boolean"
    },
    {
      "input_name": "backup_battery_health",
      "description": "Backup battery health",
      "value_type": "Boolean"
    },
    {
      "input_name": "ble_beacon_id",
      "description": "BLE: ID",
      "value_type": "String"
    },
    {
      "input_name": "ble_mac",
      "description": "BLE: MAC address",
      "value_type": "String"
    },
    {
      "input_name": "ble_magnet_sensor_1",
      "description": "Magnetic Bluetooth sensor 1",
      "value_type": "Boolean"
    },
    {
      "input_name": "ble_magnet_sensor_2",
      "description": "Magnetic Bluetooth sensor 2",
      "value_type": "Boolean"
    },
    {
      "input_name": "ble_magnet_sensor_3",
      "description": "Magnetic Bluetooth sensor 3",
      "value_type": "Boolean"
    },
    {
      "input_name": "ble_magnet_sensor_4",
      "description": "Magnetic Bluetooth sensor 4",
      "value_type": "Boolean"
    },
    {
      "input_name": "ble_magnet_sensor_5",
      "description": "Magnetic Bluetooth sensor 5",
      "value_type": "Boolean"
    },
    {
      "input_name": "ble_magnet_sensor_6",
      "description": "Magnetic Bluetooth sensor 6",
      "value_type": "Boolean"
    },
    {
      "input_name": "ble_magnet_sensor_7",
      "description": "Magnetic Bluetooth sensor 7",
      "value_type": "Boolean"
    },
    {
      "input_name": "ble_magnet_sensor_8",
      "description": "Magnetic Bluetooth sensor 8",
      "value_type": "Boolean"
    },
    {
      "input_name": "ble_magnet_sensor_9",
      "description": "Magnetic Bluetooth sensor 9",
      "value_type": "Boolean"
    },
    {
      "input_name": "ble_magnet_sensor_10",
      "description": "Magnetic Bluetooth sensor 10",
      "value_type": "Boolean"
    },
    {
      "input_name": "lock_state",
      "description": "Lock state",
      "value_type": "String"
    },
    {
      "input_name": "lock_status",
      "description": "Lock status",
      "value_type": "String"
    },
    {
      "input_name": "lock_state_raw",
      "description": "Raw lock status: Raw data",
      "value_type": "Integer"
    },
    {
      "input_name": "lock_command_result",
      "description": "Lock/unlock command result",
      "value_type": "String"
    },
    {
      "input_name": "door_state_1",
      "description": "Door state 1",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_2",
      "description": "Door state 2",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_3",
      "description": "Door state 3",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_4",
      "description": "Door state 4",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_5",
      "description": "Door state 5",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_6",
      "description": "Door state 6",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_7",
      "description": "Door state 7",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_8",
      "description": "Door state 8",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_9",
      "description": "Door state 9",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_10",
      "description": "Door state 10",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_11",
      "description": "Door state 11",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_12",
      "description": "Door state 12",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_13",
      "description": "Door state 13",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_14",
      "description": "Door state 14",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_15",
      "description": "Door state 15",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_state_16",
      "description": "Door state 16",
      "value_type": "Boolean"
    },
    {
      "input_name": "door_status_1",
      "description": "Door status 1",
      "value_type": "Integer"
    },
    {
      "input_name": "door_status_2",
      "description": "Door status 2",
      "value_type": "Integer"
    },
    {
      "input_name": "door_status_3",
      "description": "Door status 3",
      "value_type": "Integer"
    },
    {
      "input_name": "door_status_4",
      "description": "Door status 4",
      "value_type": "Integer"
    },
    {
      "input_name": "light_state_1",
      "description": "Light sensor status 1",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_2",
      "description": "Light sensor status 2",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_3",
      "description": "Light sensor status 3",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_4",
      "description": "Light sensor status 4",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_5",
      "description": "Light sensor status 5",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_6",
      "description": "Light sensor status 6",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_7",
      "description": "Light sensor status 7",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_8",
      "description": "Light sensor status 8",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_9",
      "description": "Light sensor status 9",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_10",
      "description": "Light sensor status 10",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_11",
      "description": "Light sensor status 11",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_12",
      "description": "Light sensor status 12",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_13",
      "description": "Light sensor status 13",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_14",
      "description": "Light sensor status 14",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_15",
      "description": "Light sensor status 15",
      "value_type": "Boolean"
    },
    {
      "input_name": "light_state_16",
      "description": "Light sensor status 16",
      "value_type": "Boolean"
    },
    {
      "input_name": "tacho_vin",
      "description": "TACHO: VIN",
      "value_type": "String"
    },
    {
      "input_name": "tacho_card1_sn",
      "description": "TACHO: Card 1 number",
      "value_type": "String"
    },
    {
      "input_name": "tacho_card2_sn",
      "description": "TACHO: Card 2 number",
      "value_type": "String"
    },
    {
      "input_name": "tacho_vin_last_download",
      "description": "tacho_vin_last_download",
      "value_type": "String"
    },
    {
      "input_name": "tacho_card1_last_download",
      "description": "tacho_card1_last_download",
      "value_type": "String"
    },
    {
      "input_name": "tacho_card2_last_download",
      "description": "tacho_card2_last_download",
      "value_type": "String"
    },
    {
      "input_name": "obd_vin",
      "description": "VIN",
      "value_type": "String"
    },
    {
      "input_name": "obd_mil_status",
      "description": "OBD: MIL status (check engine)",
      "value_type": "Boolean"
    },
    {
      "input_name": "obd_dtc_number",
      "description": "Errors",
      "value_type": "Integer"
    },
    {
      "input_name": "obd_dtc_codes",
      "description": "DTC",
      "value_type": "String"
    },
    {
      "input_name": "obd_dtc_cleared_distance",
      "description": "OBD: Mileage after DTC reset",
      "value_type": "Double"
    },
    {
      "input_name": "obd_mil_activated_distance",
      "description": "OBD: Distance with MIL on",
      "value_type": "Double"
    },
    {
      "input_name": "obd_four_wheel_drive",
      "description": "OBD: 4x4",
      "value_type": "Boolean"
    },
    {
      "input_name": "obd_electronic_lock_status",
      "description": "OBD: Electronic lock status",
      "value_type": "Integer"
    },
    {
      "input_name": "can_hand_brake_state",
      "description": "Car is on handbrake",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_hood_state",
      "description": "Hood",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Closed",
        "1": "Opened"
      }
    },
    {
      "input_name": "can_airbag_state",
      "description": "Airbag",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Not used",
        "1": "Fired"
      }
    },
    {
      "input_name": "can_trunk_state",
      "description": "Trunk",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Closed",
        "1": "Opened"
      }
    },
    {
      "input_name": "can_seat_belt_driver_state",
      "description": "Driver seat belt",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Locked",
        "1": "Unlocked"
      }
    },
    {
      "input_name": "can_seat_belt_passenger_state",
      "description": "Passenger seat belt",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Locked",
        "1": "Unlocked"
      }
    },
    {
      "input_name": "can_door_state",
      "description": "Door",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Closed",
        "1": "Opened"
      }
    },
    {
      "input_name": "can_door_driver_state",
      "description": "Driver door",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Closed",
        "1": "Opened"
      }
    },
    {
      "input_name": "can_door_passenger_state",
      "description": "Passenger door",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Closed",
        "1": "Opened"
      }
    },
    {
      "input_name": "can_cruise_control",
      "description": "CAN: Cruise Control",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_brake_state",
      "description": "CAN: Brake pedal",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_selected_gear",
      "description": "CAN: Selected Gear",
      "value_type": "Integer"
    },
    {
      "input_name": "can_retarder_location",
      "description": "CAN: Retarder location",
      "value_type": "Integer"
    },
    {
      "input_name": "can_e_fast_charge",
      "description": "CAN: Fast charge",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_active_charge_mode",
      "description": "CAN: Active charge mode",
      "value_type": "Integer"
    },
    {
      "input_name": "can_e_charger_control_mode",
      "description": "CAN: Charger control mode",
      "value_type": "Integer"
    },
    {
      "input_name": "can_e_charger_status",
      "description": "CAN: Charger status",
      "value_type": "Integer"
    },
    {
      "input_name": "can_e_charger_internal_fault",
      "description": "CAN: Charger internal fault",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_charger_plugged",
      "description": "CAN: Charger plugged",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_powertrain_state",
      "description": "CAN: Powertrain state",
      "value_type": "Integer"
    },
    {
      "input_name": "can_e_charging_active",
      "description": "CAN: Charging active",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_park_brake",
      "description": "CAN: Park brake active",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_helmet_status",
      "description": "CAN: Helmet status",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_top_case_sensor",
      "description": "CAN: Top case sensor",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_driving_direction",
      "description": "CAN: Driving direction",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_ignition_state",
      "description": "CAN: Ignition state",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_engine_state",
      "description": "CAN: Engine state",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_footbrake_state",
      "description": "CAN: Footbrake state",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_webasto_state",
      "description": "CAN: Webasto",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_roof_state",
      "description": "CAN: Roof",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_front_left_door",
      "description": "CAN: Front left door",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_front_right_door",
      "description": "CAN: Front right door",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_rear_left_door",
      "description": "CAN: Rear left door",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_rear_right_door",
      "description": "CAN: Rear right door",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_oil_pressure_or_level",
      "description": "CAN: Oil pressure/level",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_coolant_temp_or_level",
      "description": "CAN: Coolant liquid temperature/level",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_eps_state",
      "description": "CAN: EPS state",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_lights_failure",
      "description": "CAN: Lights failure",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_low_tire_pressure",
      "description": "CAN: Low tire pressure",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_brake_pad_wear",
      "description": "CAN: Wear of brake pads",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_warning",
      "description": "CAN: Warning",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_abs_state",
      "description": "CAN: ABS state",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_low_fuel",
      "description": "CAN: Low fuel",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_glow_plug_indicator",
      "description": "CAN: Glow plug indicator",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_electronics_power_control",
      "description": "CAN: Electronic Power Control",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_parking_lights",
      "description": "CAN: Parking lights",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_dipped_headlights",
      "description": "CAN: Dipped headlights",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_full_beam_headlights",
      "description": "CAN: Full beam headlights",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_ready_to_drive",
      "description": "CAN: Ready to drive",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_automatic_retarder",
      "description": "CAN: Automatic retarder",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_manual_retarder",
      "description": "CAN: Manual retarder",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_air_conditioning",
      "description": "CAN: Air conditioning",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_rear_fog_lights",
      "description": "CAN: Rear fog lights",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_front_fog_lights",
      "description": "CAN: Front fog lights",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_additional_front_fog_lights",
      "description": "CAN: Additional front fog lights",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_additional_rear_lights",
      "description": "CAN: Additional rear lights",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_light_signal",
      "description": "CAN: Light signal",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_rear_left_seat_belt_state",
      "description": "Rear left passenger belt",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Locked",
        "1": "Unlocked"
      }
    },
    {
      "input_name": "can_rear_right_seat_belt_state",
      "description": "Rear right passenger belt",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Locked",
        "1": "Unlocked"
      }
    },
    {
      "input_name": "can_rear_centre_seat_belt_state",
      "description": "Rear center passenger belt",
      "value_type": "Boolean",
      "value_titles": {
        "0": "Locked",
        "1": "Unlocked"
      }
    },
    {
      "input_name": "can_front_passenger_presence",
      "description": "CAN: Front passenger presence",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_front_diff_locked",
      "description": "CAN: Front differential locked",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_rear_diff_locked",
      "description": "CAN: Rear differential locked",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_central_diff_4hi_locked",
      "description": "CAN: Central differential (4HI) locked",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_central_diff_4lo_locked",
      "description": "CAN: Central differential with reductor (4LO) locked",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_trailer_axle_lift_active_1",
      "description": "CAN: Trailer axle lift 1",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_trailer_axle_lift_active_2",
      "description": "CAN: Trailer axle lift 2",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_clutch_state",
      "description": "CAN: Clutch state",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_pto_drive_engagement",
      "description": "CAN: PTO drive engagement",
      "value_type": "String"
    },
    {
      "input_name": "can_adblue_status",
      "description": "CAN: AdBlue status",
      "value_type": "String"
    },
    {
      "input_name": "can_mil_indicator",
      "description": "CAN: MIL indicator",
      "value_type": "String"
    },
    {
      "input_name": "can_current_gear",
      "description": "CAN: Current gear",
      "value_type": "Integer"
    },
    {
      "input_name": "can_pto_state",
      "description": "CAN: PTO state",
      "value_type": "String"
    },
    {
      "input_name": "can_j1939_fault_codes",
      "description": "CAN: J1939 DTC",
      "value_type": "String"
    },
    {
      "input_name": "can_j1708_fault_codes",
      "description": "can_j1708_fault_codes",
      "value_type": "String"
    },
    {
      "input_name": "can_e_charger_bms_com_timeout",
      "description": "CAN: Charger BMS COM timeout",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_charger_crc_violation",
      "description": "CAN: Charger CRC violation",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_charger_mc_violation",
      "description": "CAN: Charger MC violation",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_malfunction_indicator",
      "description": "CAN: Malfunction indicator",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_vehicle_available",
      "description": "CAN: Vehicle available",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_kill_switch_active",
      "description": "CAN: Kill switch active",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_kickstand_release",
      "description": "CAN: Kickstand release",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_over_under_temperature",
      "description": "CAN: Over/under temperature",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_battery_on_off",
      "description": "CAN: Battery on/off",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_warning_undervoltage",
      "description": "CAN: Undervoltage",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_warning_overvoltage",
      "description": "CAN: Overvoltage",
      "value_type": "Boolean"
    },
    {
      "input_name": "can_e_warning_overcurrent",
      "description": "CAN: Overcurrent",
      "value_type": "Boolean"
    },
    {
      "input_name": "uds_vin",
      "description": "UDS: VIN",
      "value_type": "String"
    },
    {
      "input_name": "uds_sb_lock_status_front_left",
      "description": "UDS: Lock status of the front left seatbelt",
      "value_type": "Boolean",
      "value_titles": {
        "0": "unlocked",
        "1": "locked"
      }
    },
    {
      "input_name": "uds_sb_lock_status_front_right",
      "description": "UDS: Lock status of the front right seatbelt",
      "value_type": "Boolean",
      "value_titles": {
        "0": "unlocked",
        "1": "locked"
      }
    },
    {
      "input_name": "uds_sb_lock_status_rear_left",
      "description": "UDS: Lock status of the back left seatbelt",
      "value_type": "Boolean",
      "value_titles": {
        "0": "unlocked",
        "1": "locked"
      }
    },
    {
      "input_name": "uds_sb_lock_status_rear_right",
      "description": "UDS: Lock status of the back right seatbelt",
      "value_type": "Boolean",
      "value_titles": {
        "0": "unlocked",
        "1": "locked"
      }
    },
    {
      "input_name": "uds_sb_lock_status_rear_middle",
      "description": "UDS: Lock status of the back rear middle seatbelt",
      "value_type": "Boolean",
      "value_titles": {
        "0": "unlocked",
        "1": "locked"
      }
    },
    {
      "input_name": "uds_sb_indicator_lamp",
      "description": "UDS: Seatbelt unfastened warning lamp",
      "value_type": "Boolean",
      "value_titles": {
        "0": "off",
        "1": "on"
      }
    },
    {
      "input_name": "uds_dtc_service_codes",
      "description": "UDS: DTC",
      "value_type": "String"
    },
    {
      "input_name": "uds_park_brake_status",
      "description": "UDS: Handbrake status",
      "value_type": "Integer",
      "value_titles": {
        "0": "in rest position",
        "1": "pulled",
        "2": "pressed",
        "3": "fault"
      }
    },
    {
      "input_name": "uds_boot_status",
      "description": "UDS: State of boot",
      "value_type": "Boolean",
      "value_titles": {
        "0": "closed",
        "1": "open"
      }
    },
    {
      "input_name": "uds_hood_status",
      "description": "UDS: State of hood",
      "value_type": "Boolean",
      "value_titles": {
        "0": "closed",
        "1": "open"
      }
    },
    {
      "input_name": "uds_mil",
      "description": "UDS: MIL status (check engine)",
      "value_type": "Boolean"
    },
    {
      "input_name": "uds_general_door_status",
      "description": "UDS: Door state",
      "value_type": "Integer",
      "value_titles": {
        "0": "closed",
        "1": "open",
        "2": "not installed"
      }
    },
    {
      "input_name": "uds_door_status_front_left",
      "description": "UDS: Door front left",
      "value_type": "Integer",
      "value_titles": {
        "0": "closed",
        "1": "open",
        "2": "not installed"
      }
    },
    {
      "input_name": "uds_door_status_front_right",
      "description": "UDS: Door front right",
      "value_type": "Integer",
      "value_titles": {
        "0": "closed",
        "1": "open",
        "2": "not installed"
      }
    },
    {
      "input_name": "uds_door_status_rear_left",
      "description": "UDS: Door rear left",
      "value_type": "Integer",
      "value_titles": {
        "0": "closed",
        "1": "open",
        "2": "not installed"
      }
    },
    {
      "input_name": "uds_door_status_rear_right",
      "description": "UDS: Door rear right",
      "value_type": "Integer",
      "value_titles": {
        "0": "closed",
        "1": "open",
        "2": "not installed"
      }
    },
    {
      "input_name": "uds_pass_airbag_switch",
      "description": "UDS: Passenger airbag",
      "value_type": "Boolean",
      "value_titles": {
        "0": "closed",
        "1": "open"
      }
    },
    {
      "input_name": "uds_airbag_warning_lamp",
      "description": "UDS: Warning lamp for airbag",
      "value_type": "Boolean",
      "value_titles": {
        "0": "off",
        "1": "on"
      }
    },
    {
      "input_name": "uds_warn_brake_lining_wear",
      "description": "UDS: Brake lining wear",
      "value_type": "Integer",
      "value_titles": {
        "0": "OK or none active",
        "1": "active or 1 stage reached",
        "2": "2 stage reached"
      }
    },
    {
      "input_name": "uds_warn_brake_fluid_level_low",
      "description": "UDS: Brake fluid level low",
      "value_type": "Boolean",
      "value_titles": {
        "0": "no",
        "1": "yes"
      }
    },
    {
      "input_name": "uds_warn_coolant_level_low",
      "description": "UDS: Coolant level low",
      "value_type": "Boolean",
      "value_titles": {
        "0": "no",
        "1": "yes"
      }
    },
    {
      "input_name": "presence_device_absent",
      "description": "Identifier of the absent presence device",
      "value_type": "String"
    },
    {
      "input_name": "absent_device_recovered",
      "description": "Identifier of the absent device that was recovered",
      "value_type": "String"
    }
  ],
  "success": true
}
```

</details>

#### Errors

[General](../../../../errors.md#error-codes) types only.
