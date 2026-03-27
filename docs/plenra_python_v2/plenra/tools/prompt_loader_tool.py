from __future__ import annotations

from plenra.core.types import ToolResult


class PromptLoaderTool:
    tool_name = "prompt_loader_tool"
    description = "Load agent prompts by key."

    def run(self, payload: dict) -> ToolResult:
        return ToolResult(
            tool_name=self.tool_name,
            status="ok",
            output={
                "description": self.description,
                "received_keys": sorted(payload.keys()),
            },
        )
