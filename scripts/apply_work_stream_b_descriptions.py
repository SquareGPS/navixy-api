#!/usr/bin/env python3
"""
Work stream B: Pull operation descriptions from docs into the OpenAPI spec.
Scans docs under resources for "API path:" and "### action" sections,
extracts the first paragraph as description, and updates spec paths.
Skips paths that already have a non-boilerplate description (e.g. tracker/zone pilot).
"""
import re
import json
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs" / "user-api" / "backend-api" / "resources"
OPENAPI_PATH = Path(__file__).resolve().parent.parent / "navixy-backend-api-openapi.json"

# Boilerplate we replace
BOILERPLATE_PREFIX = "Backend API endpoint: POST "

# Match "API path: `/path`" or "API base path: `/path`"
API_PATH_RE = re.compile(r"API (?:base )?path:\s*`([^`]+)`")
# Match "### action name" (action can have \ for escape, e.g. list\_ids)
SECTION_HEADING_RE = re.compile(r"^###\s+(.+)$", re.MULTILINE)


def normalize_action(heading: str) -> str:
    """Convert ### heading to path segment: unescape \\_ to _, spaces to _, strip backticks."""
    s = heading.replace("\\_", "_").strip().strip("`")
    return s.replace(" ", "_")


def first_paragraph(lines: list[str]) -> str:
    """First paragraph: lines until ** or #### or ### or blank line before **."""
    out = []
    for line in lines:
        s = line.strip()
        if not s:
            if out:
                break
            continue
        if s.startswith("**") or s.startswith("####") or s.startswith("###"):
            break
        # Skip markdown links and code that might be on first line
        out.append(s)
    return " ".join(out).strip() if out else ""


def extract_descriptions_from_file(md_path: Path) -> list[tuple[str, str]]:
    """Parse one .md file; return list of (path, description)."""
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    results = []
    current_api_path = None
    # Split by ### to get sections
    parts = SECTION_HEADING_RE.split(text)
    # parts[0] = before first ###, parts[1]=heading1, parts[2]=content1, parts[3]=heading2, ...
    if len(parts) < 2:
        return results
    # Before first ###, find last API path
    pre = parts[0]
    for m in API_PATH_RE.finditer(pre):
        current_api_path = m.group(1).strip().strip("/")
    i = 1
    while i + 1 < len(parts):
        heading = parts[i].strip()
        content = parts[i + 1]
        # Update current_api_path if there's one in this section's content (before next ###)
        first_block = content.split("###")[0] if "###" in content else content
        for m in API_PATH_RE.finditer(first_block):
            current_api_path = m.group(1).strip().strip("/")
        action = normalize_action(heading)
        if not action or action.startswith("/"):
            i += 2
            continue
        base = (current_api_path or "").strip("/")
        if not base:
            i += 2
            continue
        # Path: base already ends with action (e.g. /beacon/data/read + read) or base + "/" + action
        if base.endswith("/" + action) or base == action:
            path = "/" + base
        else:
            path = "/" + base + "/" + action
        if "`" in path:
            i += 2
            continue
        lines = content.splitlines()
        desc = first_paragraph(lines)
        if desc:
            results.append((path, desc))
        i += 2
    return results


def collect_all_descriptions() -> dict[str, str]:
    """Walk docs and build path -> description map. Later docs can override."""
    path_to_desc = {}
    for md in sorted(DOCS_DIR.rglob("*.md")):
        for path, desc in extract_descriptions_from_file(md):
            path_to_desc[path] = desc
    return path_to_desc


def main():
    path_to_desc = collect_all_descriptions()
    print(f"Collected {len(path_to_desc)} path descriptions from docs.")

    spec = json.loads(OPENAPI_PATH.read_text(encoding="utf-8"))
    paths = spec.get("paths", {})
    updated = 0
    skipped_no_desc = 0
    skipped_has_custom = 0
    not_in_spec = []

    for path, desc in sorted(path_to_desc.items()):
        if path not in paths:
            not_in_spec.append(path)
            continue
        post = paths[path].get("post")
        if not post:
            continue
        current = (post.get("description") or "").strip()
        if not current.startswith(BOILERPLATE_PREFIX):
            skipped_has_custom += 1
            continue
        # Truncate long descriptions to a reasonable length (e.g. first sentence or 300 chars)
        if len(desc) > 400:
            desc = desc[:397].rsplit(" ", 1)[0] + "..."
        post["description"] = desc
        updated += 1
        if updated <= 10:
            print(f"  {path}: {desc[:60]}...")

    if not_in_spec and len(not_in_spec) <= 30:
        print(f"  Paths in docs but not in spec ({len(not_in_spec)}): {not_in_spec[:20]}...")
    elif not_in_spec:
        print(f"  Paths in docs but not in spec: {len(not_in_spec)}")

    OPENAPI_PATH.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Done. Updated {updated} operations. Skipped (already custom): {skipped_has_custom}. Not in spec: {len(not_in_spec)}.")


if __name__ == "__main__":
    main()
