# OpenAPI Spec Assessment & Optimization Guide

**File:** `navixy-backend-api-openapi.json`  
**Size:** ~18,700 lines | **Paths:** **378** (all POST)  
**Date:** 2026-03-04

**Path count:** The spec contains **378 paths**. Paths are synced from `docs/user-api/backend-api/resources` via `scripts/add_missing_endpoints.py`. The script matches both single- and double-quoted example URLs; a double-check added **12 missing paths** (e.g. `/data/import/list`, `/data/import/read`, `/employee/import/start`, `/employee/import/read`, `/employee/import/list`, `/employee/import/download_failed`).

---

## 1. Current State Summary

### 1.1 Component schemas (only 6)

| Schema | Purpose | Used in |
|--------|---------|--------|
| `SuccessResponse` | `{ success: boolean }` | Base for other success types |
| `SuccessResponseWithValue` | success + `value: object` | **Most operations** (200 response) |
| `SuccessResponseWithList` | success + `list: object[]` | 2 operations |
| `SuccessResponseWithResult` | success + `result: object` | 1 operation |
| `ErrorResponse` | success + `status` | 400/404/500 responses |
| `ErrorStatus` | `{ code, description }` | Nested in ErrorResponse |

### 1.2 Component responses (3)

- `BadRequest`, `NotFound`, `ServerError` — all use `ErrorResponse` schema. **Good:** already reused via `$ref`.

### 1.3 What's missing

- **No domain models:** no `Tracker`, `Zone`, `Vehicle`, `Route`, `User`, etc. Response payloads are typed as generic `object` or `array` of `object`.
- **No reusable request schema:** every path defines the same request body inline (see below).
- **No operation-level parameters:** everything is in the JSON body (hash + endpoint-specific fields).

---

## 2. Duplication & Bloat

### 2.1 Request body (largest source of duplication)

**Every** operation uses the same inline request schema:

```json
"requestBody": {
  "required": true,
  "content": {
    "application/json": {
      "schema": {
        "type": "object",
        "required": ["hash"],
        "properties": {
          "hash": {
            "type": "string",
            "description": "Session hash (API key) for authentication"
          }
        },
        "additionalProperties": true
      }
    }
  }
}
```

- Repeated **366 times** (every operation).
- ~15 lines per operation → **~5,500 lines** of identical schema.
- Endpoints that need extra fields (e.g. `tracker_id`, `from`, `to`) could extend a base schema instead of re-declaring `hash` every time.

### 2.2 200 response block

Each operation repeats:

```json
"200": {
  "description": "Successful response",
  "content": {
    "application/json": {
      "schema": { "$ref": "#/components/schemas/SuccessResponseWithValue" }
    }
  }
}
```

- Repeated 366 times (and similar for List/Result).
- ~8 lines × 366 → **~2,900 lines** that could be replaced by a single reusable response + `$ref`.

### 2.3 Weak typing of success payloads

- `SuccessResponseWithValue`: `value` is `type: "object"` with no properties.
- `SuccessResponseWithList`: `list` is `array` of `object` with no `items` schema.
- `SuccessResponseWithResult`: `result` is `type: "object"` with no properties.

So the spec is consistent but gives no structure for domain data (trackers, zones, routes, etc.), which limits codegen, validation, and docs.

---

## 3. Optimization Recommendations

### 3.1 Quick wins (reduce size and repetition)

1. **Add a single request-base schema**  
   - Add to `components.schemas`:
     - `RequestBodyBase`: `required: ["hash"]`, `properties.hash`, `additionalProperties: true`.
   - Replace every inline request `schema` with:
     - `"schema": { "$ref": "#/components/schemas/RequestBodyBase" }`.
   - **Effect:** remove ~1,500 lines, one place to document/auth request shape.
   - For endpoints with extra required/optional fields, use `allOf: [ { $ref: "#/components/schemas/RequestBodyBase" }, { type: "object", required: [...], properties: { ... } } ]`.

2. **Reusable 200 response components**  
   - Add to `components.responses`:
     - `OkValue`: description + content with `SuccessResponseWithValue`.
     - `OkList`: same with `SuccessResponseWithList`.
     - `OkResult`: same with `SuccessResponseWithResult`.
   - In each operation, use:
     - `"200": { "$ref": "#/components/responses/OkValue" }` (or OkList/OkResult where appropriate).
   - **Effect:** remove ~800 lines and centralize success response shape.

3. **Optional: default responses**  
   - If every operation has the same 400/404/500, consider documenting a single place (e.g. in `info` or a small doc) that "all operations support BadRequest/NotFound/ServerError" and then reference them once per operation (already done) or rely on tooling that supports default responses to reduce repetition further.

### 3.2 Medium-term (better typing and tooling)

4. **Introduce domain schemas**  
   - Add schemas for main resources, e.g.:
     - `Tracker`, `TrackerList`, `Zone`, `ZoneList`, `Vehicle`, `Route`, `User`, etc.
   - Source: Navixy docs (e.g. MCP) or backend DTOs.
   - Use them where the API returns a single resource or a list:
     - e.g. `SuccessResponseWithValue` with `value` as `$ref: "#/components/schemas/Tracker"` for tracker/read;
     - or a generic `SuccessResponseWithListOfTrackers` with `items: { $ref: "#/components/schemas/Tracker" }`.
   - **Effect:** better client codegen, validation, and documentation; more schemas but a much richer spec.

5. **Tighten SuccessResponse variants**  
   - Keep `SuccessResponseWithValue` generic for "any object" endpoints, but add specific response schemas where the shape is known, e.g.:
     - `TrackerReadResponse` with `value` ref to `Tracker`.
   - Optionally use `oneOf` / `discriminators` if the same endpoint can return different shapes (e.g. by type field).

6. **Parameter reuse**  
   - If many endpoints share the same query or body parameters (e.g. `from`, `to`, `tracker_id`), define them once in `components.parameters` or in small schemas and reference them (e.g. in `allOf` with `RequestBodyBase`).

### 3.3 Optional tooling

7. **Pre/post processing**  
   - Use a script or OpenAPI plugin to:
     - Replace inline "hash-only" request bodies with `$ref` to `RequestBodyBase`.
     - Replace repeated 200 blocks with `$ref` to `OkValue`/`OkList`/`OkResult`.
   - Run after generating the spec from another source (if applicable) to keep the canonical spec small and consistent.

8. **Split by tag**  
   - If the file becomes hard to navigate, consider splitting paths by tag into multiple files and using `$ref` or a bundler (e.g. `openapi-cli`, `redocly`) to produce one bundled spec for codegen/docs.

---

## 4. Expected Impact

| Change | Lines saved (approx.) | Benefit |
|--------|------------------------|---------|
| Request body → `RequestBodyBase` ref | ~5,500 | Smaller spec, single source of truth for auth body |
| 200 response → `OkValue`/`OkList`/`OkResult` ref | ~2,900 | Smaller spec, consistent success contract |
| Add domain schemas (Tracker, Zone, etc.) | +500–2000 (net) | Better typing, codegen, and docs |

Net effect of quick wins: **~8,400 fewer lines** and a clearer structure with only a couple of new components. Domain schemas increase size but greatly improve usability.

---

## 5. Next Steps

1. Add `RequestBodyBase` and replace all 366 inline request schemas with `$ref` (and `allOf` where extra fields exist).
2. Add `OkValue`, `OkList`, `OkResult` and replace inline 200 response blocks with `$ref`.
3. (Optional) Add a small script to automate (1) and (2) for future spec regeneration.
4. (Medium-term) From Navixy docs or backend, add domain schemas for key resources and wire them into success response schemas.

If you want, the quick wins (1–2) can be applied directly to `navixy-backend-api-openapi.json`; domain models can be added incrementally afterward.

---

## 6. Plan: Reuse Object Structures as Schemas & Add Descriptions

**Goal:** (1) Turn resource object structures from the docs into reusable OpenAPI component schemas. (2) Replace boilerplate operation descriptions with real descriptions and add missing parameter/schema descriptions.

**Mandatory checklist:** Use **[OBJECTS_INVENTORY.md](OBJECTS_INVENTORY.md)** so that **no documented object is overlooked**. The inventory is generated by `scripts/inventory_objects.py` and lists every object/entity structure found in the docs (57 entries). When adding a schema, mark its row as `Done` in the Status column; when all rows are done, every available object is covered.

### 6.1 Current gap

| Area | Current state | Target |
|------|----------------|--------|
| **Operation description** | Only `"Backend API endpoint: POST /path"` | Short human-readable summary (e.g. "Gets tracker info by ID") plus optional details. |
| **Request/response bodies** | Generic `object` / `array of object` | Typed schemas (Tracker, Zone, Vehicle, etc.) with property types and descriptions. |
| **Object structures** | Described only in docs (JSON blocks + bullet lists like `* \`id\` - int. Description.`) | Defined once in `components.schemas`, referenced in operations. |

**Source of truth:** `docs/user-api/backend-api/resources/` — each resource has (or links to):

- **Object structure:** JSON code block + bullet list of fields (`* \`field\` - type. Description.`).
- **API actions:** Heading per action (e.g. `### read`, `### list`), short description, parameters table, response example, errors.

### 6.2 Work stream A: Reuse object structures as schemas

1. **Inventory and prioritize resources**
   - **Use [OBJECTS_INVENTORY.md](OBJECTS_INVENTORY.md)** — it lists every object/structure definition found in the docs (explicit headings + response-only shapes). Re-run `scripts/inventory_objects.py` after doc changes to refresh.
   - Prioritize by traffic or dependency: e.g. Tracker, Zone, Vehicle, Place, User first; then sub-resources and smaller entities.

2. **Define extraction rules**
   - **From docs:** JSON block → infer types; bullet list `* \`name\` - type. desc.` → property name, type, description. Handle `optional`, `nullable`, `int array`, `object`, `[enum](...)`, `[date/time](...)`.
   - **Nested objects:** Define separate schemas (e.g. `TrackerSource`, `ZoneCenter`, `ZoneBounds`) and `$ref` from parent.
   - **Variants:** Some resources have multiple shapes (e.g. Zone: circle / polygon / sausage). Model with `oneOf` + discriminator or separate schemas (e.g. `ZoneCircle`, `ZonePolygon`, `ZoneSausage`) and a common base if useful.

3. **Add schemas to the spec**
   - Add each model under `components.schemas` with `type`, `properties`, `required`, `description` (and nested `$ref` where needed).
   - Add small shared primitives if reused (e.g. `LatLng`, `Location`) to avoid duplication.

4. **Wire schemas into operations**
   - For each path, set request body schema (e.g. `allOf: [RequestBodyBase, TrackerReadRequest]`) and/or response schema (e.g. `value` → `$ref: "#/components/schemas/Tracker"`, or `list` → `items: $ref Tracker`).
   - Use operation-specific response schemas where the wrapper differs (e.g. `TrackerReadResponse` with `value: $ref Tracker`).

5. **Tooling option**
   - **Script:** Parse markdown (JSON block + bullet list regex) per resource file, output OpenAPI schema JSON; maintain a mapping from path/action to schema name and run script when docs change.
   - **Manual:** Author/curate schemas in the spec and copy descriptions from docs (slower but full control).

### 6.3 Work stream B: Add and fix descriptions

**Status:** In progress. A script **`scripts/apply_work_stream_b_descriptions.py`** parses docs for "API path:" and "### action" sections, extracts the first paragraph as the operation description, and updates the spec. **266 operations** now have real descriptions (pilot tracker/zone + bulk update); **100** still use boilerplate where the doc path or structure doesn’t match.

1. **Operation-level descriptions**
   - For each path + method, set `summary` and `description` from the docs action heading and first paragraph (e.g. "Gets tracker info by ID" for `tracker/read`).
   - Optionally add a second paragraph for constraints, permissions, or links to full docs.

2. **Request body / parameters**
   - Where the request has more than `hash`, define a schema (or extend `RequestBodyBase` with `allOf`) and add `description` for each property from the docs parameters table.
   - Keep parameter tables in docs as source; sync key names and descriptions into the spec.

3. **Response and schema property descriptions**
   - Ensure each component schema has a top-level `description`.
   - Ensure each property has a `description` (from the bullet list in the docs). Optional: mark deprecated, format, examples.

4. **Source → spec sync**
   - Prefer a single source of truth: either docs (and generate/update spec) or spec (and generate doc snippets). If docs remain source, add a script or CI step to pull descriptions and structure into the spec when docs change.

### 6.4 Phasing

| Phase | Scope | Deliverable |
|-------|--------|-------------|
| **1. Pilot** | 1–2 resources (e.g. Tracker + Zone) | Schemas `Tracker`, `TrackerSource`, `Zone*`, plus operation descriptions and request/response wiring for tracker/* and zone/* paths. |
| **2. Core resources** | Vehicle, Place, Status, Task, User (and key sub-resources) | Full schemas + descriptions for these paths. |
| **3. Rest of resources** | Remaining paths (subuser, tag, report, history, etc.) | All paths have real descriptions; all documented object structures exist as schemas and are referenced where applicable. |
| **4. Automation (optional)** | Doc parsing + mapping | Script(s) to update schemas and/or descriptions from docs on change. |

### 6.5 Concrete next steps

1. **Map path → doc section:** Build a table or script: for each OpenAPI path (e.g. `/tracker/read`), which doc file and which heading hold the description and parameters.
2. **Pilot:** Add `Tracker` and `TrackerSource` (and Zone variants) to `components.schemas`; add operation descriptions for all `tracker/*` and `zone/*`; set `value`/`list` to `$ref` where appropriate. Mark the corresponding rows in **OBJECTS_INVENTORY.md** as `Done`.
3. **Request schemas:** For operations that require more than `hash`, introduce small request schemas (e.g. `TrackerReadRequest`: `tracker_id`) and use `allOf` with `RequestBodyBase`.
4. **Iterate:** Work through **OBJECTS_INVENTORY.md** until every row has Status `Done`; then add automation if desired.

---

## 7. Double-check: Paths & models

**Script:** `scripts/check_paths_and_models.py` — compares spec paths/schemas to docs and OBJECTS_INVENTORY.

**Paths:**
- **Spec:** 378 paths (after adding 12 previously missing: `add_missing_endpoints.py` was updated to match double-quoted example URLs; added e.g. `/data/import/list`, `/data/import/read`, `/employee/import/*`).
- **Docs:** Many "API path" lines are base paths (e.g. `/zone`); full paths come from example URLs. Any path that appears in a doc example URL is now matched (single or double quote).
- **In spec but not in doc URLs:** ~29 paths (e.g. `/user/api_key/list`, `/zone/upload`) — may use different URL style in docs or be documented elsewhere.

**Models (OBJECTS_INVENTORY):**
- **57** object/structure entries; all have a corresponding schema in the spec (Status = Done).
- **Spec** has 119 component schemas (57 inventory + response wrappers, request schemas, primitives, and supporting schemas such as `PluginFilter`, `TrackerTagBinding`, `Zone`, etc.).
- Nothing from the inventory was missed.

---

## 8. Geo Links pilot: endpoint-specific body and descriptions

For base path `/tracker/location/link`, the following approach was applied and can be reused for other endpoint groups:

1. **Short body description**  
   - `RequestBodyBase` description was shortened to one line: *"Endpoint-specific parameters. See operation schema and Backend API docs per path."* No auth text in the body.

2. **No “other properties”**  
   - Each geo link operation uses a **dedicated request schema** (e.g. `LocationLinkCreateRequest`, `LocationLinkReadRequest`) with only the parameters documented in the Backend API docs. Each of these schemas has **`additionalProperties: false`**, so there is no generic “other properties” parameter.

3. **Richer descriptions**  
   - Operation descriptions were taken from the docs and expanded with: what the call does, required sub-user rights where relevant, and error codes (e.g. 201, 204, 217, 236, 268) with short explanations.  
   - Request schema properties use the same wording as the docs (e.g. “Session ID”, “Link description. Printable characters, max length 255.”).

4. **Nested request types**  
   - Shared structures (e.g. `LocationLinkLifetime`, `LocationLinkDisplayOptions`, `LocationLinkParams`, `LocationLinkTrackerEntry`) are defined as separate schemas and referenced so the request body is fully typed and documented.

**Request schemas added:** `LocationLinkLifetime`, `LocationLinkDisplayOptions`, `LocationLinkParams`, `LocationLinkTrackerEntry`, `LocationLinkCreateRequest`, `LocationLinkUpdateRequest`, `LocationLinkReadRequest`, `LocationLinkListRequest`, `LocationLinkDeleteRequest`, `LocationLinkStatusChangeRequest`.  
**Paths updated:** `/tracker/location/link/create`, `/update`, `/read`, `/list`, `/delete`, `/status/change`.

5. **Incorporate docs: response schemas, examples, parameter text**  
   - **Response object schema:** Added `LocationLink` (and `LocationLinkValueResponse` / `LocationLinkListResponse`) so `read` and `list` have a typed response body matching the doc’s Response JSON.  
   - **Request examples:** Each geo link operation has an `example` in `requestBody.content['application/json']` taken from the doc (e.g. create/update body without hash; read/list/delete/status/change with id, offset/limit, or is_active).  
   - **Response examples:** `OkLocationLinkValue` and `OkLocationLinkList` include an `example` with the same shape as in the doc (success + value object, or success + list of link objects).  
   - **Parameter descriptions:** Aligned with the doc’s Parameters tables (e.g. “Link’s description. Only printable characters. Max length: 255.”, “Optional. Offset, default is 0.”, “Optional. Limit, default is 10,000.”).  

Repeating this for other endpoint groups (tracker, zone, vehicle, etc.): define response schemas from the doc’s Response JSON, add request/response examples from the doc’s examples, and copy parameter/restriction text from the Parameters tables into the spec.
