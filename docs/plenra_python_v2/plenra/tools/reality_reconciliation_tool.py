from __future__ import annotations

from plenra.core.types import ToolResult


class RealityReconciliationTool:
    tool_name = "reality_reconciliation_tool"
    description = "Compare expected vs observed system state."

    def run(self, payload: dict) -> ToolResult:
        return ToolResult(
            tool_name=self.tool_name,
            status="ok",
            output={
                "description": self.description,
                "received_keys": sorted(payload.keys()),
            },
        )
