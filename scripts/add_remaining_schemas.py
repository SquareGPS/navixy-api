#!/usr/bin/env python3
"""Add all remaining object schemas from OBJECTS_INVENTORY to the OpenAPI spec."""
import json
from pathlib import Path

OPENAPI_PATH = Path(__file__).resolve().parent.parent / "navixy-backend-api-openapi.json"

# Schemas already in spec (pilot)
EXISTING = {
    "LatLng", "ZoneBounds", "ZonePoint", "TrackerSource", "TrackerTagBinding",
    "Tracker", "TrackerOutputInfo", "ZoneCircle", "ZonePolygon", "ZoneSausage", "Zone",
    "TrackerValueResponse", "TrackerListResponse", "ZoneValueResponse", "ZoneListResponse",
    "TrackerReadRequest", "ZoneReadRequest", "RequestBodyBase",
    "SuccessResponse", "SuccessResponseWithValue", "SuccessResponseWithList", "SuccessResponseWithResult",
    "ErrorResponse", "ErrorStatus",
}

# All remaining schemas: name -> OpenAPI schema dict (from docs)
# Order matters: refs must come after referenced schemas
REMAINING_SCHEMAS = {
    "PluginFilter": {
        "type": "object",
        "description": "Model filter for plugin applicability",
        "properties": {
            "exclusion": {"type": "boolean", "description": "If true, values lists models NOT supported"},
            "values": {"type": "array", "items": {"type": "string"}, "description": "Regexes for models"}
        }
    },
    "Bill": {
        "type": "object",
        "description": "Bill (order) object",
        "properties": {
            "order_id": {"type": "integer", "description": "Unique bill ID"},
            "created": {"type": "string", "format": "date-time", "description": "When the bill was created"},
            "sum": {"type": "number", "description": "Bill sum in default currency of the panel"},
            "status": {"type": "string", "enum": ["created", "settled", "canceled"], "description": "Bill order status"},
            "positions": {"type": "array", "items": {"type": "string"}, "description": "List of position names"},
            "link": {"type": "string", "description": "URL to order"}
        }
    },
    "Transaction": {
        "type": "object",
        "description": "Billing transaction object",
        "properties": {
            "description": {"type": "string"},
            "type": {"type": "string", "description": "Type of transaction"},
            "subtype": {"type": "string", "description": "Subtype of transaction"},
            "timestamp": {"type": "string", "format": "date-time"},
            "user_id": {"type": "integer"},
            "dealer_id": {"type": "integer"},
            "tracker_id": {"type": "integer", "description": "0 if not associated with tracker"},
            "amount": {"type": "number"},
            "new_balance": {"type": "number"},
            "old_balance": {"type": "number"},
            "bonus_amount": {"type": "number"},
            "new_bonus": {"type": "number"},
            "old_bonus": {"type": "number"}
        }
    },
    "ApiKey": {
        "type": "object",
        "description": "API key object",
        "properties": {
            "hash": {"type": "string", "description": "Hash of the API key (32 chars)"},
            "create_date": {"type": "string", "format": "date-time", "description": "Key creation date"},
            "title": {"type": "string", "description": "Key title"}
        }
    },
    "Tag": {
        "type": "object",
        "description": "Tag object for quick searches",
        "properties": {
            "id": {"type": "integer", "description": "Tag ID"},
            "avatar_file_name": {"type": "string", "description": "Avatar file name"},
            "name": {"type": "string", "description": "Tag name"},
            "color": {"type": "string", "description": "Tag color in 3-byte RGB hex format"}
        }
    },
    "Plugin": {
        "type": "object",
        "description": "Plugin object",
        "properties": {
            "id": {"type": "integer"},
            "type": {"type": "string"},
            "ui_module": {"type": "string"},
            "module": {"type": "string"},
            "filter": {"$ref": "#/components/schemas/PluginFilter"},
            "parameters": {"type": "object", "description": "Plugin-specific parameters"}
        }
    },
    "ReportScheduleEntry": {
        "type": "object",
        "description": "Report schedule entry",
        "properties": {
            "id": {"type": "integer"},
            "enabled": {"type": "boolean"},
            "parameters": {"type": "object", "description": "Schedule parameters (period, report, emails, etc.)"},
            "fire_time": {"type": "string", "description": "Last schedule fire time"},
            "last_result": {"type": "object", "properties": {"success": {"type": "boolean"}, "id": {"type": "integer"}}}
        }
    },
    "Status": {
        "type": "object",
        "description": "Working status object",
        "properties": {
            "id": {"type": "integer", "description": "Unique identifier of the working status"},
            "label": {"type": "string", "description": "Human-readable label"},
            "color": {"type": "string", "description": "Hex RGB color for display"}
        }
    },
    "StatusListing": {
        "type": "object",
        "description": "Status listing object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "statuses": {"type": "array", "items": {"$ref": "#/components/schemas/Status"}}
        }
    },
    "MapLayer": {
        "type": "object",
        "description": "Map layer metadata",
        "properties": {
            "id": {"type": "integer", "description": "Map layer entity ID"},
            "label": {"type": "string", "description": "Map layer name"}
        }
    },
    "Group": {
        "type": "object",
        "description": "Tracker group object",
        "properties": {
            "id": {"type": "integer", "description": "Group ID"},
            "title": {"type": "string", "description": "Group title"},
            "color": {"type": "string", "description": "Group color in web format (without #)"}
        }
    },
    "Subuser": {
        "type": "object",
        "description": "Sub-user object",
        "properties": {
            "id": {"type": "integer", "nullable": True},
            "activated": {"type": "boolean"},
            "login": {"type": "string"},
            "first_name": {"type": "string"},
            "middle_name": {"type": "string"},
            "last_name": {"type": "string"},
            "legal_type": {"type": "string", "enum": ["legal_entity", "individual", "sole_trader"]},
            "phone": {"type": "string"},
            "post_country": {"type": "string"},
            "post_index": {"type": "string"},
            "post_region": {"type": "string"},
            "post_city": {"type": "string"},
            "post_street_address": {"type": "string"},
            "registered_country": {"type": "string"},
            "registered_index": {"type": "string"},
            "registered_region": {"type": "string"},
            "registered_city": {"type": "string"},
            "registered_street_address": {"type": "string"},
            "state_reg_num": {"type": "string"},
            "tin": {"type": "string"},
            "legal_name": {"type": "string"},
            "iec": {"type": "string"},
            "security_group_id": {"type": "integer", "nullable": True},
            "creation_date": {"type": "string", "format": "date-time"}
        }
    },
    "SecurityGroup": {
        "type": "object",
        "description": "Security group object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "rights": {"type": "object", "description": "Rights configuration"}
        }
    },
    "NotificationEntry": {
        "type": "object",
        "description": "Notification list item",
        "properties": {
            "id": {"type": "integer", "description": "Notification ID"},
            "message": {"type": "string", "description": "Notification message"},
            "show_till": {"type": "string", "format": "date-time", "description": "Date until notification should be shown"}
        }
    },
    "HistoryTypeEntry": {
        "type": "object",
        "description": "History event type entry",
        "properties": {
            "type": {"type": "string", "description": "History event type"},
            "description": {"type": "string", "description": "Localized description"}
        }
    },
    "BeaconDataEntry": {
        "type": "object",
        "description": "BLE beacon data entry",
        "properties": {
            "tracker_id": {"type": "integer"},
            "hardware_id": {"type": "string"},
            "rssi": {"type": "integer", "description": "Received signal strength indicator"},
            "get_time": {"type": "string", "format": "date-time"},
            "latitude": {"type": "number"},
            "longitude": {"type": "number"},
            "ext_data": {"type": "object", "description": "Additional beacon data"}
        }
    },
    "CounterValue": {
        "type": "object",
        "description": "Counter value (e.g. odometer, engine hours)",
        "properties": {
            "id": {"type": "integer"},
            "type": {"type": "string", "enum": ["odometer", "engine_hours"]},
            "multiplier": {"type": "number"}
        }
    },
    "Feedback": {
        "type": "object",
        "description": "Feedback object",
        "properties": {
            "id": {"type": "integer"},
            "message": {"type": "string"},
            "created": {"type": "string", "format": "date-time"}
        }
    },
    "Entity": {
        "type": "object",
        "description": "Entity (customizable object) definition",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "fields": {"type": "array", "description": "Entity field definitions"}
        }
    },
    "EntityField": {
        "type": "object",
        "description": "Entity field object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "type": {"type": "string"},
            "required": {"type": "boolean"}
        }
    },
    "SearchConditions": {
        "type": "object",
        "description": "Entity search conditions",
        "properties": {}
    },
    "User": {
        "type": "object",
        "description": "User object (simplified; full structure in docs)",
        "properties": {
            "id": {"type": "integer"},
            "login": {"type": "string"},
            "first_name": {"type": "string"},
            "last_name": {"type": "string"},
            "email": {"type": "string"},
            "phone": {"type": "string"},
            "activated": {"type": "boolean"},
            "creation_date": {"type": "string", "format": "date-time"}
        }
    },
    "UserSettings": {
        "type": "object",
        "description": "User settings object",
        "properties": {
            "locale": {"type": "string"},
            "timezone": {"type": "string"},
            "unit_system": {"type": "string"}
        }
    },
    "AuditLogEntry": {
        "type": "object",
        "description": "Audit log entry",
        "properties": {
            "id": {"type": "integer"},
            "user_id": {"type": "integer"},
            "action": {"type": "string"},
            "timestamp": {"type": "string", "format": "date-time"},
            "details": {"type": "object"}
        }
    },
    "Vehicle": {
        "type": "object",
        "description": "Vehicle object",
        "properties": {
            "id": {"type": "integer"},
            "tracker_id": {"type": "integer"},
            "tracker_label": {"type": "string"},
            "label": {"type": "string"},
            "max_speed": {"type": "integer"},
            "model": {"type": "string"},
            "type": {"type": "string", "enum": ["truck", "car", "bus", "special"]},
            "subtype": {"type": "string"},
            "garage_id": {"type": "integer", "nullable": True},
            "reg_number": {"type": "string"},
            "vin": {"type": "string"},
            "manufacture_year": {"type": "integer"},
            "color": {"type": "string"},
            "avatar_file_name": {"type": "string", "nullable": True},
            "tags": {"type": "array", "items": {"type": "integer"}}
        }
    },
    "VehicleStatusListing": {
        "type": "object",
        "description": "Vehicle status listing object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "statuses": {"type": "array", "items": {"$ref": "#/components/schemas/Status"}}
        }
    },
    "Garage": {
        "type": "object",
        "description": "Garage object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "organization_name": {"type": "string"}
        }
    },
    "ServiceTask": {
        "type": "object",
        "description": "Vehicle service task object",
        "properties": {
            "id": {"type": "integer"},
            "tracker_id": {"type": "integer"},
            "vehicle_id": {"type": "integer"},
            "label": {"type": "string"},
            "status": {"type": "string"},
            "created": {"type": "string", "format": "date-time"},
            "due_date": {"type": "string", "format": "date-time", "nullable": True}
        }
    },
    "DriverJournalEntry": {
        "type": "object",
        "description": "Driver journal entry",
        "properties": {
            "id": {"type": "integer"},
            "tracker_id": {"type": "integer"},
            "driver_id": {"type": "integer"},
            "start_time": {"type": "string", "format": "date-time"},
            "end_time": {"type": "string", "format": "date-time", "nullable": True}
        }
    },
    "Place": {
        "type": "object",
        "description": "Place/POI object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "address": {"type": "string"},
            "lat": {"type": "number"},
            "lng": {"type": "number"},
            "radius": {"type": "integer"},
            "tags": {"type": "array", "items": {"type": "integer"}}
        }
    },
    "Task": {
        "type": "object",
        "description": "Field service task object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "status": {"type": "string"},
            "tracker_id": {"type": "integer"},
            "employee_id": {"type": "integer", "nullable": True},
            "place_id": {"type": "integer", "nullable": True},
            "creation_date": {"type": "string", "format": "date-time"},
            "tags": {"type": "array", "items": {"type": "integer"}}
        }
    },
    "Checkpoint": {
        "type": "object",
        "description": "Task checkpoint object",
        "properties": {
            "id": {"type": "integer"},
            "task_id": {"type": "integer"},
            "label": {"type": "string"},
            "order": {"type": "integer"},
            "lat": {"type": "number"},
            "lng": {"type": "number"}
        }
    },
    "Route": {
        "type": "object",
        "description": "Task route object",
        "properties": {
            "id": {"type": "integer"},
            "task_id": {"type": "integer"},
            "label": {"type": "string"},
            "tracker_id": {"type": "integer"},
            "checkpoints": {"type": "array", "items": {"$ref": "#/components/schemas/Checkpoint"}}
        }
    },
    "TaskScheduleEntry": {
        "type": "object",
        "description": "Task schedule entry",
        "properties": {
            "id": {"type": "integer"},
            "task_id": {"type": "integer"},
            "tracker_id": {"type": "integer"},
            "start": {"type": "string", "format": "date-time"},
            "end": {"type": "string", "format": "date-time"}
        }
    },
    "Employee": {
        "type": "object",
        "description": "Employee object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "tracker_id": {"type": "integer", "nullable": True},
            "email": {"type": "string"},
            "phone": {"type": "string"},
            "tags": {"type": "array", "items": {"type": "integer"}}
        }
    },
    "Department": {
        "type": "object",
        "description": "Department object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "parent_id": {"type": "integer", "nullable": True}
        }
    },
    "Checkin": {
        "type": "object",
        "description": "Check-in object",
        "properties": {
            "id": {"type": "integer"},
            "tracker_id": {"type": "integer"},
            "template_id": {"type": "integer"},
            "creation_date": {"type": "string", "format": "date-time"},
            "form_data": {"type": "object"}
        }
    },
    "Form": {
        "type": "object",
        "description": "Form object",
        "properties": {
            "id": {"type": "integer"},
            "template_id": {"type": "integer"},
            "task_id": {"type": "integer", "nullable": True},
            "fields": {"type": "array"}
        }
    },
    "FormFile": {
        "type": "object",
        "description": "Form file object",
        "properties": {
            "id": {"type": "integer"},
            "form_id": {"type": "integer"},
            "field_id": {"type": "string"},
            "file_name": {"type": "string"},
            "size": {"type": "integer"}
        }
    },
    "FormTemplate": {
        "type": "object",
        "description": "Form template object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "fields": {"type": "array"}
        }
    },
    "Value": {
        "type": "object",
        "description": "Form field value (field-type-specific; type and value or type-specific fields)",
        "properties": {
            "type": {"type": "string"},
            "value": {}
        }
    },
    "Rule": {
        "type": "object",
        "description": "Tracker rule object",
        "properties": {
            "id": {"type": "integer"},
            "tracker_id": {"type": "integer"},
            "label": {"type": "string"},
            "template_id": {"type": "integer"},
            "enabled": {"type": "boolean"},
            "conditions": {"type": "object"},
            "actions": {"type": "object"}
        }
    },
    "Readings": {
        "type": "object",
        "description": "Readings batch object",
        "properties": {
            "tracker_id": {"type": "integer"},
            "sensors": {"type": "array", "description": "Sensor readings"}
        }
    },
    "RetranslatorProtocol": {
        "type": "object",
        "description": "Retranslator protocol object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"}
        }
    },
    "Retranslator": {
        "type": "object",
        "description": "Retranslator object",
        "properties": {
            "id": {"type": "integer"},
            "tracker_id": {"type": "integer"},
            "protocol_id": {"type": "integer"},
            "enabled": {"type": "boolean"}
        }
    },
    "TrackerRetranslatorBinding": {
        "type": "object",
        "description": "Tracker retranslator binding",
        "properties": {
            "tracker_id": {"type": "integer"},
            "retranslator_id": {"type": "integer"}
        }
    },
    "AssetGroupEntry": {
        "type": "object",
        "description": "Asset group object entry",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "trackers": {"type": "array", "items": {"type": "integer"}}
        }
    },
    "ZoneBatchConvertErrors": {
        "type": "object",
        "description": "Zone batch convert response with errors",
        "properties": {
            "errors": {"type": "object", "description": "Parameter errors if present"},
            "limit_exceeded": {"type": "boolean"}
        }
    },
    "PaymentSystemSettings": {
        "type": "object",
        "description": "Payment system settings",
        "properties": {
            "id": {"type": "integer"},
            "type": {"type": "string"},
            "enabled": {"type": "boolean"}
        }
    },
    "TariffPlan": {
        "type": "object",
        "description": "Tariff plan object",
        "properties": {
            "id": {"type": "integer"},
            "label": {"type": "string"},
            "tracker_limit": {"type": "integer"},
            "features": {"type": "array", "items": {"type": "string"}}
        }
    },
}


def main():
    with open(OPENAPI_PATH, encoding="utf-8") as f:
        spec = json.load(f)

    schemas = spec["components"]["schemas"]
    to_add = {k: v for k, v in REMAINING_SCHEMAS.items() if k not in schemas and k not in EXISTING}
    if not to_add:
        print("No new schemas to add.")
        return

    # Insert before RequestBodyBase (so order: existing... then new, then RequestBodyBase)
    for name, schema in to_add.items():
        schemas[name] = schema

    with open(OPENAPI_PATH, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)

    print(f"Added {len(to_add)} schemas: {', '.join(sorted(to_add.keys()))}")


if __name__ == "__main__":
    main()
