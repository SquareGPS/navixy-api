#!/usr/bin/env python3
"""Add all endpoints found in docs but missing from OpenAPI spec."""
import re
import json
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs" / "user-api" / "backend-api" / "resources"
OPENAPI_PATH = Path(__file__).resolve().parent.parent / "navixy-backend-api-openapi.json"
PATTERN = re.compile(r"https?://[^/]+/v2/([a-z_/]+)'")

def tag_for_path(p):
    if p.startswith("/tracker"): return "Tracking"
    if p.startswith("/zone"): return "Zones"
    if p.startswith("/track") or p.startswith("/route"): return "Routes"
    if p.startswith("/status"): return "Status"
    if p.startswith("/asset_group"): return "Assets"
    if p.startswith("/beacon"): return "Beacons"
    if p.startswith("/geocoder"): return "Geocoding"
    if p.startswith("/map_layer"): return "Maps"
    if p.startswith("/vehicle"): return "Vehicles"
    if p.startswith("/driver"): return "Drivers"
    if p.startswith("/task"): return "Tasks"
    if p.startswith("/employee"): return "Employees"
    if p.startswith("/place"): return "Places"
    if p.startswith("/form"): return "Forms"
    if p.startswith("/checkin"): return "Check-ins"
    if p.startswith("/user"): return "Users"
    if p.startswith("/subuser"): return "Sub-users"
    if p.startswith("/tag"): return "Tags"
    if p.startswith("/entity"): return "Entities"
    if p.startswith("/history"): return "History"
    if p.startswith("/report"): return "Reports"
    if p.startswith("/notification"): return "Notifications"
    if p.startswith("/plugin"): return "Plugins"
    if p.startswith("/subscription") or p.startswith("/bill") or p.startswith("/tariff") or p.startswith("/payment_system"): return "Billing"
    if p.startswith("/api/key"): return "Users"
    if p.startswith("/garage"): return "Vehicles"
    if p.startswith("/retranslator"): return "Tracking"
    if p.startswith("/department"): return "Tasks"
    if p.startswith("/file") or p.startswith("/dealer") or p.startswith("/delivery") or p.startswith("/timezone"): return "Commons"
    if p.startswith("/apn_settings") or p.startswith("/base") or p.startswith("/feedback") or p.startswith("/transaction"): return "Commons"
    return "Backend"

def op_id(p):
    return p.strip("/").replace("/", "_").replace("-", "_")

def make_operation(path):
    return {
        "post": {
            "tags": [tag_for_path(path)],
            "summary": op_id(path),
            "description": "Backend API endpoint: POST " + path,
            "operationId": op_id(path),
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/RequestBodyBase"}
                    }
                }
            },
            "responses": {
                "200": {"$ref": "#/components/responses/OkValue"},
                "400": {"$ref": "#/components/responses/BadRequest"},
                "404": {"$ref": "#/components/responses/NotFound"},
                "500": {"$ref": "#/components/responses/ServerError"}
            }
        }
    }

def extract_from_docs():
    paths = set()
    for md in DOCS_DIR.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for m in PATTERN.finditer(text):
            path = "/" + m.group(1).rstrip("/")
            paths.add(path)
    return paths

def main():
    docs_paths = extract_from_docs()
    with open(OPENAPI_PATH, encoding="utf-8") as f:
        spec = json.load(f)
    openapi_paths = set(spec["paths"].keys())
    missing = sorted(docs_paths - openapi_paths)
    if not missing:
        print("No missing paths.")
        return
    for path in missing:
        spec["paths"][path] = make_operation(path)
    with open(OPENAPI_PATH, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)
    print(f"Added {len(missing)} paths. Total paths: {len(spec['paths'])}.")

if __name__ == "__main__":
    main()
