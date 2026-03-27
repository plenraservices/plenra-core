from __future__ import annotations

from plenra.core.types import ToolResult


class SimulationTool:
    tool_name = "simulation_tool"
    description = "Execute supported simulation scenarios."

    def run(self, payload: dict) -> ToolResult:
        return ToolResult(
            tool_name=self.tool_name,
            status="ok",
            output={
                "description": self.description,
                "received_keys": sorted(payload.keys()),
            },
        )
