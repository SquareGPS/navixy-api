#!/usr/bin/env python3
"""Apply OpenAPI quick wins: RequestBodyBase ref and OkValue/OkList/OkResult/OkSuccess refs."""
import json
from pathlib import Path

OPENAPI_PATH = Path(__file__).resolve().parent.parent / "navixy-backend-api-openapi.json"

REQUEST_BODY_BASE = {
    "type": "object",
    "required": ["hash"],
    "properties": {
        "hash": {
            "type": "string",
            "description": "Session hash (API key) for authentication",
        }
    },
    "additionalProperties": True,
}


def is_request_body_base(schema):
    """True if schema is the standard hash-only request body."""
    if not isinstance(schema, dict):
        return False
    if schema.get("$ref"):
        return False
    if schema.get("type") != "object":
        return False
    req = schema.get("required")
    if req != ["hash"]:
        return False
    props = schema.get("properties") or {}
    if "hash" not in props or not isinstance(props["hash"], dict):
        return False
    if props["hash"].get("type") != "string":
        return False
    if schema.get("additionalProperties") is not True:
        return False
    return True


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
