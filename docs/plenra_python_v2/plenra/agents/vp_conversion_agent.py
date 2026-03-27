from __future__ import annotations

from plenra.core.base_agent import AgentResult, BaseAgent


class VPConversionAgent(BaseAgent):
    agent_name = "vp_conversion_agent"
    prompt_key = "vp_conversion_agent"
    mission = "Reduce friction and improve conversion paths."

    def run(self, context: dict) -> AgentResult:
        return AgentResult(
            agent_name=self.agent_name,
            status="ok",
            summary="Conversion scaffold executed.",
            payload={
                "mission": self.mission,
                "prompt": self.get_prompt(),
                "received_keys": sorted(context.keys()),
            },
        )
