from plenra.agents import AGENT_REGISTRY
from plenra.prompts.registry import PROMPT_REGISTRY
from plenra.tools.registry import TOOL_REGISTRY


def test_registries_have_core_entries():
    assert "central_agent" in AGENT_REGISTRY
    assert "central_agent" in PROMPT_REGISTRY
    assert "audit_logger_tool" in TOOL_REGISTRY
