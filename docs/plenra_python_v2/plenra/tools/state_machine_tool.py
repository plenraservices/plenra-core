from __future__ import annotations

from plenra.core.types import ToolResult


class StateMachineTool:
    tool_name = "state_machine_tool"
    description = "Advance state using official transition rules."

    def run(self, payload: dict) -> ToolResult:
        return ToolResult(
            tool_name=self.tool_name,
            status="ok",
            output={
                "description": self.description,
                "received_keys": sorted(payload.keys()),
            },
        )
