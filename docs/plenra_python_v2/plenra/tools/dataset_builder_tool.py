from __future__ import annotations

from plenra.core.types import ToolResult


class DatasetBuilderTool:
    tool_name = "dataset_builder_tool"
    description = "Route trusted records into learning-safe structures."

    def run(self, payload: dict) -> ToolResult:
        return ToolResult(
            tool_name=self.tool_name,
            status="ok",
            output={
                "description": self.description,
                "received_keys": sorted(payload.keys()),
            },
        )
