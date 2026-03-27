from __future__ import annotations

from plenra.core.types import ToolResult


class MetaControllerTool:
    tool_name = "meta_controller_tool"
    description = "Protect learning and execution from unsafe input."

    def run(self, payload: dict) -> ToolResult:
        return ToolResult(
            tool_name=self.tool_name,
            status="ok",
            output={
                "description": self.description,
                "received_keys": sorted(payload.keys()),
            },
        )
