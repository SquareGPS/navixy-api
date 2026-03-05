#!/usr/bin/env python3
"""
Wire read/list paths to typed response schemas.
Adds *ValueResponse and *ListResponse schemas and Ok* response components,
then sets each path's 200 response to the appropriate $ref.
"""
import json
from pathlib import Path

OPENAPI_PATH = Path(__file__).resolve().parent.parent / "navixy-backend-api-openapi.json"

# Path -> ("value" | "list", schema_name). Tracker and Zone already wired.
PATH_WIRING = [
    ("/tag/list", "list", "Tag"),
    ("/vehicle/read", "value", "Vehicle"),
    ("/vehicle/list", "list", "Vehicle"),
    ("/task/read", "value", "Task"),
    ("/task/list", "list", "Task"),
    ("/employee/read", "value", "Employee"),
    ("/employee/list", "list", "Employee"),
    ("/place/read", "value", "Place"),
    ("/place/list", "list", "Place"),
    ("/form/read", "value", "Form"),
    ("/checkin/read", "value", "Checkin"),
    ("/checkin/list", "list", "Checkin"),
    ("/subuser/list", "list", "Subuser"),
    ("/entity/read", "value", "Entity"),
    ("/entity/list", "list", "Entity"),
    ("/notification/list", "list", "NotificationEntry"),
    ("/plugin/list", "list", "Plugin"),
    ("/bill/list", "list", "Bill"),
    ("/tariff/list", "list", "TariffPlan"),
    ("/department/list", "list", "Department"),
    ("/garage/list", "list", "Garage"),
    ("/payment_system/list", "list", "PaymentSystemSettings"),
    ("/retranslator/list", "list", "Retranslator"),
    ("/transaction/list", "list", "Transaction"),
    ("/map_layer/read", "value", "MapLayer"),
    ("/map_layer/list", "list", "MapLayer"),
    ("/status/list", "list", "Status"),
    ("/asset_group/list", "list", "AssetGroupEntry"),
    ("/api/key/list", "list", "ApiKey"),
    ("/form/template/read", "value", "FormTemplate"),
    ("/form/template/list", "list", "FormTemplate"),
    ("/report/schedule/list", "list", "ReportScheduleEntry"),
    ("/retranslator/protocol/list", "list", "RetranslatorProtocol"),
    ("/tracker/group/list", "list", "Group"),
    ("/tracker/rule/list", "list", "Rule"),
    ("/task/checkpoint/read", "value", "Checkpoint"),
    ("/task/checkpoint/list", "list", "Checkpoint"),
    ("/task/route/list", "list", "Route"),
    ("/task/schedule/read", "value", "TaskScheduleEntry"),
    ("/task/schedule/list", "list", "TaskScheduleEntry"),
    ("/driver/journal/entry/list", "list", "DriverJournalEntry"),
    ("/vehicle/service_task/read", "value", "ServiceTask"),
    ("/vehicle/service_task/list", "list", "ServiceTask"),
    ("/user/settings/read", "value", "UserSettings"),
    ("/subuser/security_group/list", "list", "SecurityGroup"),
]


def make_value_response_schema(schema_name: str) -> dict:
    return {
        "allOf": [
            {"$ref": "#/components/schemas/SuccessResponse"},
            {
                "type": "object",
                "properties": {
                    "value": {"$ref": f"#/components/schemas/{schema_name}"}
                }
            }
        ],
        "description": f"Success response with a single {schema_name.replace('_', ' ').lower()}"
    }


def make_list_response_schema(schema_name: str) -> dict:
    return {
        "allOf": [
            {"$ref": "#/components/schemas/SuccessResponse"},
            {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {"$ref": f"#/components/schemas/{schema_name}"}
                    }
                }
            }
        ],
        "description": f"Success response with list of {schema_name.replace('_', ' ').lower()}s"
    }


def main():
    spec = json.loads(OPENAPI_PATH.read_text(encoding="utf-8"))
    schemas = spec.setdefault("components", {}).setdefault("schemas", {})
    responses = spec.setdefault("components", {}).setdefault("responses", {})

    # Collect response schema names and response refs we need
    to_add_schemas = {}  # name -> schema dict
    to_add_responses = {}  # name -> response dict
    path_updates = []  # (path, response_ref)

    for path, kind, schema_name in PATH_WIRING:
        if kind == "value":
            resp_schema_name = f"{schema_name}ValueResponse"
            resp_ref_name = f"Ok{schema_name}Value"
        else:
            resp_schema_name = f"{schema_name}ListResponse"
            resp_ref_name = f"Ok{schema_name}List"

        if resp_schema_name not in schemas:
            if kind == "value":
                to_add_schemas[resp_schema_name] = make_value_response_schema(schema_name)
            else:
                to_add_schemas[resp_schema_name] = make_list_response_schema(schema_name)

        if resp_ref_name not in responses:
            to_add_responses[resp_ref_name] = {
                "description": f"Successful response with {'a single' if kind == 'value' else 'list of'} {schema_name.replace('_', ' ').lower()}{'s' if kind == 'list' else ''}",
                "content": {
                    "application/json": {
                        "schema": {"$ref": f"#/components/schemas/{resp_schema_name}"}
                    }
                }
            }

        path_updates.append((path, resp_ref_name))

    # Add schemas (order: value responses first, then list responses, so refs to item schemas already exist)
    for name, schema in to_add_schemas.items():
        if name not in schemas:
            schemas[name] = schema
            print(f"  schema: {name}")

    for name, resp in to_add_responses.items():
        if name not in responses:
            responses[name] = resp
            print(f"  response: {name}")

    # Wire paths
    paths = spec.get("paths", {})
    wired = 0
    missing = []
    for path, resp_ref_name in path_updates:
        if path not in paths:
            missing.append(path)
            continue
        post = paths[path].get("post")
        if not post:
            missing.append(path)
            continue
        r200 = post.get("responses", {}).get("200")
        current_ref = r200.get("$ref") if isinstance(r200, dict) else None
        if current_ref != f"#/components/responses/{resp_ref_name}":
            post.setdefault("responses", {})["200"] = {"$ref": f"#/components/responses/{resp_ref_name}"}
            wired += 1
            print(f"  wired: {path} -> {resp_ref_name}")

    if missing:
        print("  paths not found:", missing)

    OPENAPI_PATH.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Done. Added {len(to_add_schemas)} response schemas, {len(to_add_responses)} response refs, wired {wired} paths.")


if __name__ == "__main__":
    main()
