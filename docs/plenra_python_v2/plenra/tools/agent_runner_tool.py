from __future__ import annotations

from plenra.core.types import ToolResult


class AgentRunnerTool:
    tool_name = "agent_runner_tool"
    description = "Run an agent by registry key."

    def run(self, payload: dict) -> ToolResult:
        return ToolResult(
            tool_name=self.tool_name,
            status="ok",
            output={
                "description": self.description,
                "received_keys": sorted(payload.keys()),
            },
        )
