#!/usr/bin/env python3
"""Double-check paths and models: spec vs docs and OBJECTS_INVENTORY."""
import json
import re
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs" / "user-api" / "backend-api" / "resources"
OPENAPI_PATH = Path(__file__).resolve().parent.parent / "navixy-backend-api-openapi.json"
# Suggested schema names from OBJECTS_INVENTORY (57 entries, unique)
INVENTORY_SCHEMA_NAMES = {
    "Bill", "PaymentSystemSettings", "TariffPlan", "Transaction",
    "HistoryTypeEntry", "NotificationEntry", "ApiKey", "EntityField", "Entity",
    "SearchConditions", "Feedback", "Plugin", "ReportScheduleEntry", "Subuser",
    "SecurityGroup", "Tag", "AuditLogEntry", "User", "UserSettings",
    "Checkin", "Department", "Employee", "Value", "Form", "FormFile", "FormTemplate",
    "Place", "Task", "Checkpoint", "Route", "TaskScheduleEntry", "DriverJournalEntry",
    "Garage", "Vehicle", "VehicleStatusListing", "ServiceTask",
    "BeaconDataEntry", "TrackerSource", "CounterValue", "AssetGroupEntry",
    "MapLayer", "RetranslatorProtocol", "Retranslator", "Status", "StatusListing",
    "Tracker", "TrackerOutputInfo", "Group", "Readings", "TrackerRetranslatorBinding",
    "Rule", "ZoneCircle", "ZonePolygon", "ZoneSausage", "ZoneBatchConvertErrors", "ZonePoint",
}

def main():
    spec = json.loads(OPENAPI_PATH.read_text(encoding="utf-8"))
    spec_paths = set(spec["paths"].keys())
    spec_schemas = set(spec.get("components", {}).get("schemas", {}).keys())

    # ---- Paths from docs: URLs in examples + "API path:" lines ----
    url_re = re.compile(r"https?://[^/]+/v2/([a-z0-9_/]+)")
    api_path_re = re.compile(r"API (?:base )?path:\s*`([^`]+)`")
    doc_paths = set()
    for md in DOCS_DIR.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for m in url_re.finditer(text):
            p = "/" + m.group(1).rstrip("/")
            if "?" in p:
                p = p.split("?")[0]
            doc_paths.add(p)
        for m in api_path_re.finditer(text):
            p = "/" + m.group(1).strip("/")
            doc_paths.add(p)

    in_spec_not_doc = spec_paths - doc_paths
    in_doc_not_spec = doc_paths - spec_paths

    print("=== PATHS ===")
    print(f"Spec paths: {len(spec_paths)}")
    print(f"Doc paths (from URLs + API path + actions): {len(doc_paths)}")
    print(f"In spec, not in doc: {len(in_spec_not_doc)}")
    for p in sorted(in_spec_not_doc)[:40]:
        print(f"  {p}")
    if len(in_spec_not_doc) > 40:
        print(f"  ... and {len(in_spec_not_doc) - 40} more")
    print(f"In doc, not in spec: {len(in_doc_not_spec)}")
    for p in sorted(in_doc_not_spec)[:50]:
        print(f"  {p}")
    if len(in_doc_not_spec) > 50:
        print(f"  ... and {len(in_doc_not_spec) - 50} more")

    # ---- Schemas: inventory vs spec ----
    print("\n=== MODELS (OBJECTS_INVENTORY vs components.schemas) ===")
    # Zone is oneOf circle/polygon/sausage - present as composite
    inventory_with_zone = INVENTORY_SCHEMA_NAMES | {"Zone"}
    missing_schemas = inventory_with_zone - spec_schemas
    extra_schemas = spec_schemas - inventory_with_zone
    # Known extra: response wrappers, request schemas, primitives, nested/supporting schemas
    known_extra = {
        "RequestBodyBase", "SuccessResponse", "SuccessResponseWithValue",
        "SuccessResponseWithList", "SuccessResponseWithResult", "ErrorResponse", "ErrorStatus",
        "TrackerReadRequest", "ZoneReadRequest", "LatLng", "ZoneBounds",
        "PluginFilter", "TrackerTagBinding",
    }
    # All *ValueResponse, *ListResponse
    for s in list(spec_schemas):
        if s.endswith("ValueResponse") or s.endswith("ListResponse"):
            known_extra.add(s)
    extra_schemas -= known_extra
    print(f"Inventory schema names (incl. Zone): {len(inventory_with_zone)}")
    print(f"Spec schemas: {len(spec_schemas)}")
    if missing_schemas:
        print(f"Missing from spec (in inventory): {sorted(missing_schemas)}")
    else:
        print("All inventory schemas present in spec.")
    if extra_schemas:
        print(f"Extra in spec (not in inventory, excl. known): {len(extra_schemas)}")
        for s in sorted(extra_schemas)[:30]:
            print(f"  {s}")
        if len(extra_schemas) > 30:
            print(f"  ... and {len(extra_schemas) - 30} more")
    else:
        print("No unexpected extra schemas.")


if __name__ == "__main__":
    main()
