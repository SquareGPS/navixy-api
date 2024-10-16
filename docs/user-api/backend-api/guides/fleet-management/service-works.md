# Managing Vehicles and Service Works

In the Navixy API, the vehicle object stores comprehensive information about a vehicle, such as its VIN, chassis number, license plate, type, dimensions, load capacity, fuel consumption, insurance details, and more. You can link a vehicle to a tracker to monitor various parameters like fuel consumption per trip and schedule timely maintenance based on mileage or engine hours.

Service works are crucial for cost and risk management in vehicle maintenance. Regular maintenance helps prevent breakdowns, ensuring vehicles remain operational and safe. For example, replacing spare parts based on usage, scheduling tire replacements, and ordering necessary parts in advance can prevent delays and reduce the risk of cargo loss.

## Vehicle Creation

To create a vehicle object, specify all relevant information about the vehicle. You can link the vehicle to a tracker by providing its ID in the `tracker_id` parameter.

### Example

Creating a Ford Transit cargo van vehicle object:

```shell
curl -X POST '{{ extra.api_example_url }}/vehicle/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "a6aa75587e5c59c32d347da438505fc3",
        "vehicle": {
            "additional_info": "January 2021",
            "avatar_file_name": null,
            "chassis_number": "",
            "color": "Blue",
            "frame_number": "",
            "free_insurance_policy_number": "",
            "free_insurance_valid_till": null,
            "fuel_cost": 4,
            "fuel_grade": "",
            "fuel_tank_volume": 80,
            "fuel_type": "diesel",
            "garage_id": null,
            "gross_weight": null,
            "icon_color": "1E96DC",
            "icon_id": null,
            "label": "Ford 53196",
            "liability_insurance_policy_number": "54687965555er2152",
            "liability_insurance_valid_till": "2022-01-12",
            "manufacture_year": 2019,
            "max_speed": 100,
            "model": "Transit",
            "norm_avg_fuel_consumption": 8.3,
            "passengers": 3,
            "payload_height": 2550,
            "payload_length": 5531,
            "payload_weight": 1529,
            "payload_width": 2059,
            "reg_number": "A53196BC",
            "subtype": "minivan",
            "tags": [],
            "tracker_id": 841400,
            "trailer": null,
            "type": "truck",
            "tyre_size": "R15",
            "tyres_number": 4,
            "vin": "XTA235KM35698512",
            "wheel_arrangement": "4x2"
        }
    }'
```

The platform will respond with:

```json
{
    "success": true,
    "id": 96175
}
```

## Service Work Creation

After creating a vehicle object and assigning a device, you can create service works to manage vehicle maintenance. Each service work represents a specific maintenance task with conditions based on mileage or engine hours.

### Example

Creating service works for oil change, brakes replacement, and spark plug replacement.

#### Oil Change

```shell
curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "a6aa75587e5c59c32d347da438505fc3",
        "task": {
            "vehicle_id": 96175,
            "comment": "Oil Ford Formula F 5W30",
            "conditions": {
                "engine_hours": {
                    "limit": 328,
                    "notification_interval": 18
                }
            },
            "cost": 28,
            "description": "Oil Change",
            "file_ids": [],
            "notifications": {
                "sms_phones": ["79995699997"],
                "emails": ["myemail@gmail.com"],
                "push_enabled": true
            },
            "repeat": false,
            "unplanned": false
        }
    }'
```

#### Brakes Replacement

```shell
curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/create' \
    -H 'Content-Type: application/json' \
    -d '{
        "hash": "a6aa75587e5c59c32d347da438505fc3",
        "task": {
            "vehicle_id": 96175,
            "comment": "ATE",
            "conditions": {
                "mileage": {
                    "limit": 78000,
                    "notification_interval": 75000
                }
            },
            "cost": 200,
            "description": "Brakes Change",
            "file_ids": [],
            "notifications": {
                "sms_phones": ["79995699997"],
                "emails": ["myemail@gmail.com"],
                "push_enabled": true
            },
            "repeat": false,
            "unplanned": false
        }
    }'
```

The platform will respond with the ID of the created service work:

```json
{
    "success": true,
    "id": 42401
}
```