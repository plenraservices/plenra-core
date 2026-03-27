from __future__ import annotations

from plenra.core.base_agent import AgentResult, BaseAgent


class VPMarketingAgent(BaseAgent):
    agent_name = "vp_marketing_agent"
    prompt_key = "vp_marketing_agent"
    mission = "Design demand creation, positioning, hooks, and traffic logic."

    def run(self, context: dict) -> AgentResult:
        return AgentResult(
            agent_name=self.agent_name,
            status="ok",
            summary="Marketing scaffold executed.",
            payload={
                "mission": self.mission,
                "prompt": self.get_prompt(),
                "received_keys": sorted(context.keys()),
            },
        )
