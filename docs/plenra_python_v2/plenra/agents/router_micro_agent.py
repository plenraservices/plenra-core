from __future__ import annotations

from plenra.core.base_agent import AgentResult, BaseAgent


class RouterMicroAgent(BaseAgent):
    agent_name = "router_micro_agent"
    prompt_key = "router_micro_agent"
    mission = "Route work to the correct agent or logic surface."

    def run(self, context: dict) -> AgentResult:
        return AgentResult(
            agent_name=self.agent_name,
            status="ok",
            summary="Router scaffold executed.",
            payload={
                "mission": self.mission,
                "prompt": self.get_prompt(),
                "received_keys": sorted(context.keys()),
            },
        )
