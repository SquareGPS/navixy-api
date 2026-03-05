#!/usr/bin/env python3
"""Apply OpenAPI quick wins: RequestBodyBase ref and OkValue/OkList/OkResult/OkSuccess refs."""
import json
from pathlib import Path

OPENAPI_PATH = Path(__file__).resolve().parent.parent / "navixy-backend-api-openapi.json"

REQUEST_BODY_BASE = {
    "type": "object",
    "description": "Request body contains only endpoint-specific parameters. Authentication is via the session hash in the request header (see Security); do not send hash in the body. The set of allowed parameters depends on the endpoint: see each operation description or the Backend API documentation for the list of parameters for a given path. Additional properties may be sent for endpoint-specific parameters not listed here.",
    "properties": {},
    "additionalProperties": True,
}


def is_request_body_base(schema):
    """True if schema is the standard request body (no hash in body; endpoint params only)."""
    if not isinstance(schema, dict):
        return False
    if schema.get("$ref"):
        return False
    if schema.get("type") != "object":
        return False
    # Old shape: required ["hash"], properties.hash; or new shape: no required hash, optional description
    req = schema.get("required") or []
    props = schema.get("properties") or {}
    if req == ["hash"] and "hash" in props and props.get("hash", {}).get("type") == "string":
        return True
    if not req and not props and schema.get("additionalProperties") is True:
        return True
    return False


def get_200_schema_ref(operation):
    """Return the $ref string for the 200 response schema, or None."""
    try:
        content = operation["responses"]["200"]["content"]["application/json"]
        schema = content.get("schema")
        if not schema:
            return None
        return schema.get("$ref")
    except (KeyError, TypeError):
        return None


def main():
    with open(OPENAPI_PATH, encoding="utf-8") as f:
        spec = json.load(f)

    components = spec.setdefault("components", {})
    schemas = components.setdefault("schemas", {})
    responses = components.setdefault("responses", {})

    # 1. Add RequestBodyBase schema
    schemas["RequestBodyBase"] = REQUEST_BODY_BASE

    # 2. Add reusable 200 response components
    responses["OkValue"] = {
        "description": "Successful response",
        "content": {
            "application/json": {
                "schema": {"$ref": "#/components/schemas/SuccessResponseWithValue"}
            }
        },
    }
    responses["OkList"] = {
        "description": "Successful response",
        "content": {
            "application/json": {
                "schema": {"$ref": "#/components/schemas/SuccessResponseWithList"}
            }
        },
    }
    responses["OkResult"] = {
        "description": "Successful response",
        "content": {
            "application/json": {
                "schema": {"$ref": "#/components/schemas/SuccessResponseWithResult"}
            }
        },
    }
    responses["OkSuccess"] = {
        "description": "Successful response",
        "content": {
            "application/json": {
                "schema": {"$ref": "#/components/schemas/SuccessResponse"}
            }
        },
    }

    schema_ref_to_response = {
        "#/components/schemas/SuccessResponseWithValue": "#/components/responses/OkValue",
        "#/components/schemas/SuccessResponseWithList": "#/components/responses/OkList",
        "#/components/schemas/SuccessResponseWithResult": "#/components/responses/OkResult",
        "#/components/schemas/SuccessResponse": "#/components/responses/OkSuccess",
    }

    req_replaced = 0
    res_replaced = 0

    for path, path_item in spec.get("paths", {}).items():
        for method, operation in list(path_item.items()):
            if method.startswith("x-") or method not in ("get", "post", "put", "patch", "delete"):
                continue
            if not isinstance(operation, dict):
                continue

            # Replace requestBody schema with $ref if it's the hash-only schema
            req = operation.get("requestBody")
            if req and isinstance(req, dict):
                content = req.get("content") or {}
                aj = content.get("application/json")
                if aj and isinstance(aj, dict):
                    schema = aj.get("schema")
                    if schema and is_request_body_base(schema):
                        aj["schema"] = {"$ref": "#/components/schemas/RequestBodyBase"}
                        req_replaced += 1

            # Replace 200 response with $ref
            res = operation.get("responses") or {}
            if "200" in res and isinstance(res["200"], dict) and "$ref" not in res["200"]:
                ref = get_200_schema_ref(operation)
                if ref and ref in schema_ref_to_response:
                    res["200"] = {"$ref": schema_ref_to_response[ref]}
                    res_replaced += 1

    with open(OPENAPI_PATH, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)

    print(f"Quick wins applied: {req_replaced} request bodies -> RequestBodyBase, {res_replaced} responses -> OkValue/OkList/OkResult/OkSuccess.")


if __name__ == "__main__":
    main()
