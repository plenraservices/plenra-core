from __future__ import annotations

from plenra.core.types import ToolResult


class DecisionGateTool:
    tool_name = "decision_gate_tool"
    description = "Run the decision gate against structured input."

    def run(self, payload: dict) -> ToolResult:
        return ToolResult(
            tool_name=self.tool_name,
            status="ok",
            output={
                "description": self.description,
                "received_keys": sorted(payload.keys()),
            },
        )
