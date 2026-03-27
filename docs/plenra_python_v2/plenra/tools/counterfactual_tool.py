from __future__ import annotations

from plenra.core.types import ToolResult


class CounterfactualTool:
    tool_name = "counterfactual_tool"
    description = "Compare baseline and actual outcomes."

    def run(self, payload: dict) -> ToolResult:
        return ToolResult(
            tool_name=self.tool_name,
            status="ok",
            output={
                "description": self.description,
                "received_keys": sorted(payload.keys()),
            },
        )
