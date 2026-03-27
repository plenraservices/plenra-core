from __future__ import annotations

from plenra.core.types import ToolRequest


def validate_tool_request(request: ToolRequest) -> list[str]:
    errors: list[str] = []
    if not request.tool_name:
        errors.append("tool_name_required")
    if not request.scope:
        errors.append("scope_required")
    if not isinstance(request.payload, dict):
        errors.append("payload_must_be_object")
    return errors
