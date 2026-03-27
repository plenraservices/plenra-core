from plenra.logic.agent_runtime import run_agent
from plenra.prompts.registry import PROMPT_REGISTRY
from plenra.tools.registry import TOOL_REGISTRY


def run_demo() -> None:
    print(run_agent("central_agent", {"surface": "budget_increase"}))
    print(PROMPT_REGISTRY["vp_marketing_agent"][:120])
    tool = TOOL_REGISTRY["audit_logger_tool"]()
    print(tool.run({"event_type": "decision_event"}))


if __name__ == "__main__":
    run_demo()
