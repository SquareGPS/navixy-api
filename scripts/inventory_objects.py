#!/usr/bin/env python3
"""
Build an exhaustive inventory of all object/entity structures documented in the
Backend API docs. Ensures no object is overlooked when adding OpenAPI schemas.

Scans docs/user-api/backend-api/resources for:
- Explicit headings: "X object", "X object structure", "Entity description", etc.
- JSON code blocks followed by bullet-list field descriptions (* `field` - type. desc.)
"""
import re
from pathlib import Path
from dataclasses import dataclass

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs" / "user-api" / "backend-api" / "resources"
OUTPUT_MD = Path(__file__).resolve().parent.parent / "OBJECTS_INVENTORY.md"

FIELD_BULLET_PATTERN = re.compile(r"^\*\s+`([a-z_][a-z0-9_]*)`\s*-\s*(.+)", re.MULTILINE)

OBJECT_HEADING_KEYWORDS = [
    "object structure", " object", "entity description", "entity object",
    "object entry", "object:", "object.", " settings", " structure",
    "entry object", "conditions object", "point object", "parameter object",
    "response with errors", "value object", "readings batch",
    "tracker output info", "tracker input types",
]


@dataclass
class ObjectEntry:
    doc_file: str
    heading: str
    suggested_schema_name: str
    has_json_block: bool
    field_count: int
    line_start: int
    notes: str = ""


def suggest_schema_name(heading: str, doc_path: str) -> str:
    h = heading.strip()
    for suffix in [" object structure", " object", " object:", " object.", " structure",
                   " object entry", " entry object", " settings object", " settings",
                   " description", " parameter object fields", " with errors object"]:
        if h.lower().endswith(suffix.lower()):
            h = h[:-len(suffix)].strip()
    if " " in h:
        h = h.split()[0]
    if "_" in h:
        h = "".join(w.capitalize() for w in h.split("_"))
    else:
        h = h.capitalize()
    path_lower = doc_path.lower()
    if "zone" in path_lower:
        if "circle" in heading.lower():
            return "ZoneCircle"
        if "polygon" in heading.lower():
            return "ZonePolygon"
        if "sausage" in heading.lower():
            return "ZoneSausage"
        if "point" in heading.lower() or "zone_point" in path_lower:
            return "ZonePoint"
        if "response with errors" in heading.lower():
            return "ZoneBatchConvertErrors"
        return "Zone" if h == "Entity" else h
    if "tracker" in path_lower and "source" in heading.lower():
        return "TrackerSource"
    if "tracker" in path_lower and "output" in heading.lower():
        return "TrackerOutputInfo"
    if "schedule" in path_lower and "report" in path_lower:
        return "ReportScheduleEntry"
    if "driver" in path_lower and "entry" in path_lower:
        return "DriverJournalEntry"
    if "vehicle" in path_lower and "service" in path_lower and "task" in path_lower:
        return "ServiceTask"
    if "status" in path_lower and "listing" in path_lower:
        return "StatusListing"
    if "task" in path_lower and "schedule" in path_lower and "entry" in heading.lower():
        return "TaskScheduleEntry"
    if "task" in path_lower and "route" in path_lower and "object" in heading.lower():
        return "Route"
    if "task" in path_lower and "checkpoint" in path_lower:
        return "Checkpoint"
    if "task" in path_lower and "task object" in heading.lower():
        return "Task"
    if "form" in path_lower and "file" in heading.lower():
        return "FormFile"
    if "form" in path_lower and "template" in heading.lower():
        return "FormTemplate"
    if "vehicle" in path_lower and "listing" in path_lower:
        return "VehicleStatusListing"
    if "asset" in path_lower and "group" in path_lower:
        return "AssetGroupEntry"
    if "user" in path_lower and "settings" in path_lower:
        return "UserSettings"
    if "audit" in path_lower:
        return "AuditLogEntry"
    if "api" in path_lower and "key" in path_lower:
        return "ApiKey"
    if "security_group" in path_lower:
        return "SecurityGroup"
    if "search_conditions" in path_lower:
        return "SearchConditions"
    if "field" in path_lower and "fields" in path_lower:
        return "EntityField"
    if "retranslator" in path_lower and "protocol" in heading.lower():
        return "RetranslatorProtocol"
    if "retranslator" in path_lower and "binding" in heading.lower():
        return "TrackerRetranslatorBinding"
    if "history" in path_lower and "type" in path_lower:
        return "HistoryTypeEntry"
    if "subuser" in path_lower:
        return "Subuser"
    if "checkin" in path_lower:
        return "Checkin"
    if "map_layer" in path_lower:
        return "MapLayer"
    if "payment_system" in path_lower:
        return "PaymentSystemSettings"
    if "notification" in path_lower:
        return "NotificationEntry"
    if "bill" in path_lower and "bill.md" in path_lower:
        return "Bill"
    if "transaction" in path_lower:
        return "Transaction"
    if "plan" in heading.lower() and "tariff" in path_lower:
        return "TariffPlan"
    return h


def count_fields_after_line(text: str, start: int) -> int:
    """Count field bullets in the same section (before next same-or-higher level heading)."""
    lines = text.splitlines()
    count = 0
    in_section = True
    for i in range(start, len(lines)):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            continue  # skip over code block, keep counting after it
        if stripped.startswith("#"):
            break
        if FIELD_BULLET_PATTERN.match(stripped):
            count += 1
    return count


def has_json_block_after(text: str, heading_line: int) -> bool:
    lines = text.splitlines()
    for i in range(heading_line, min(heading_line + 80, len(lines))):
        if lines[i].strip().startswith("```json"):
            return True
        if i > heading_line and re.match(r"^#+\s", lines[i]):
            break
    return False


def scan_file(md_path: Path) -> list:
    try:
        text = md_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []
    rel_path = str(md_path.relative_to(DOCS_DIR))
    entries = []
    lines = text.splitlines()

    for i, line in enumerate(lines):
        if not line.strip().startswith("#"):
            continue
        heading_text = line.lstrip("#").strip()
        is_object = any(kw in heading_text.lower() for kw in OBJECT_HEADING_KEYWORDS)
        if not is_object and re.match(r"^####\s+(circle|polygon|sausage)\s*:?\.?$", line.strip(), re.I):
            is_object = True
        if not is_object:
            continue
        has_json = has_json_block_after(text, i)
        field_count = count_fields_after_line(text, i + 1)
        if field_count == 0 and not has_json:
            continue
        suggested = suggest_schema_name(heading_text, rel_path)
        notes = ""
        if "input types" in heading_text.lower():
            notes = "enum list, not schema"
        entries.append(
            ObjectEntry(
                doc_file=rel_path,
                heading=heading_text,
                suggested_schema_name=suggested,
                has_json_block=has_json,
                field_count=field_count,
                line_start=i + 1,
                notes=notes,
            )
        )
    return entries


def main():
    all_entries = []
    seen = set()

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        for entry in scan_file(md_file):
            key = (entry.doc_file, entry.suggested_schema_name, entry.heading[:40])
            if key in seen:
                continue
            seen.add(key)
            all_entries.append(entry)

    all_entries.sort(key=lambda e: (e.doc_file, e.line_start))

    # Add response-only objects (structure defined under #### Response, no ## object heading)
    response_only = [
        ("commons/notification.md", "NotificationEntry", "Notification list item (id, message, show_till)", 3),
        ("commons/history/history_type.md", "HistoryTypeEntry", "History type list item (type, description)", 2),
        ("tracking/beacon/index.md", "BeaconDataEntry", "BLE beacon data entry", 6),
        ("tracking/tracker/counter.md", "CounterValue", "Counter value (id, type, multiplier) in response", 3),
        ("tracking/tracker/README.md", "TrackerSource", "Tracker source (nested in Tracker object)", 9),
    ]
    for doc_file, schema_name, heading, field_count in response_only:
        if any(e.doc_file == doc_file and e.suggested_schema_name == schema_name for e in all_entries):
            continue
        all_entries.append(
            ObjectEntry(
                doc_file=doc_file,
                heading=heading,
                suggested_schema_name=schema_name,
                has_json_block=True,
                field_count=field_count,
                line_start=0,
                notes="Response-only; no ## object heading in doc",
            )
        )
    all_entries.sort(key=lambda e: (e.doc_file, e.line_start))

    out_lines = [
        "# Backend API: Object structures inventory",
        "",
        "Exhaustive list of every object/entity structure documented in "
        "`docs/user-api/backend-api/resources`. Use this checklist when adding "
        "OpenAPI component schemas so that **no object is overlooked**.",
        "",
        "Generated by `scripts/inventory_objects.py`. Re-run to refresh.",
        "",
        "| # | Doc file | Section / heading | Suggested schema name | Fields | JSON | Status | Notes |",
        "|---|----------|--------------------|------------------------|--------|------|--------|-------|",
    ]

    for idx, e in enumerate(all_entries, 1):
        json_yes = "yes" if e.has_json_block else "—"
        heading_short = (e.heading[:48] + "..") if len(e.heading) > 50 else e.heading
        out_lines.append(
            f"| {idx} | `{e.doc_file}` | {heading_short} | `{e.suggested_schema_name}` | {e.field_count} | {json_yes} | | {e.notes} |"
        )

    out_lines.extend([
        "",
        "## Summary",
        "",
        f"- **Total object/structure definitions found:** {len(all_entries)}",
        "- **Status column:** fill with `Done` when the schema is added and wired to paths.",
        "- **Nested objects:** some sections define sub-objects (e.g. Tracker output info, Zone circle/polygon/sausage); each needs a schema or nested `$ref`.",
        "",
        "## Path → schema mapping (maintain when wiring)",
        "",
        "| Path | Request schema | Response value/list schema |",
        "|------|----------------|----------------------------|",
        "| `/tracker/read` | RequestBodyBase + tracker_id | Tracker |",
        "| `/tracker/list` | RequestBodyBase | Tracker (list) |",
        "| `/zone/read` | RequestBodyBase + id | ZoneCircle / ZonePolygon / ZoneSausage |",
        "",
    ])

    OUTPUT_MD.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Wrote {OUTPUT_MD}. Total entries: {len(all_entries)}.")


if __name__ == "__main__":
    main()
