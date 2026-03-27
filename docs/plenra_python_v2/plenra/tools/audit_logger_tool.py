from __future__ import annotations

from plenra.core.types import ToolResult


class AuditLoggerTool:
    tool_name = "audit_logger_tool"
    description = "Log auditable system events."

    def run(self, payload: dict) -> ToolResult:
        return ToolResult(
            tool_name=self.tool_name,
            status="ok",
            output={
                "description": self.description,
                "received_keys": sorted(payload.keys()),
            },
        )
