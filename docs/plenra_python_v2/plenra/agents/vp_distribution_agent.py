from __future__ import annotations

from plenra.core.base_agent import AgentResult, BaseAgent


class VPDistributionAgent(BaseAgent):
    agent_name = "vp_distribution_agent"
    prompt_key = "vp_distribution_agent"
    mission = "Distribute assets through channel-aware logic."

    def run(self, context: dict) -> AgentResult:
        return AgentResult(
            agent_name=self.agent_name,
            status="ok",
            summary="Distribution scaffold executed.",
            payload={
                "mission": self.mission,
                "prompt": self.get_prompt(),
                "received_keys": sorted(context.keys()),
            },
        )
