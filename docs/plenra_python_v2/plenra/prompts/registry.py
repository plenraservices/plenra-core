from .central_agent_prompt import CENTRAL_AGENT_PROMPT
from .router_micro_agent_prompt import ROUTER_MICRO_AGENT_PROMPT
from .vp_marketing_agent_prompt import VP_MARKETING_AGENT_PROMPT
from .vp_conversion_agent_prompt import VP_CONVERSION_AGENT_PROMPT
from .vp_content_agent_prompt import VP_CONTENT_AGENT_PROMPT
from .vp_distribution_agent_prompt import VP_DISTRIBUTION_AGENT_PROMPT
from .vp_analytics_agent_prompt import VP_ANALYTICS_AGENT_PROMPT
from .vp_tech_agent_prompt import VP_TECH_AGENT_PROMPT
from .silent_bridge_growth_agent_prompt import SILENT_BRIDGE_GROWTH_AGENT_PROMPT
from .solo_revenue_agent_prompt import SOLO_REVENUE_AGENT_PROMPT
from .decision_forecast_optimization_agent_prompt import DECISION_FORECAST_OPTIMIZATION_AGENT_PROMPT
from .expansion_risk_control_central_agent_prompt import EXPANSION_RISK_CONTROL_CENTRAL_AGENT_PROMPT
from .sentinel_agent_prompt import SENTINEL_AGENT_PROMPT

PROMPT_REGISTRY = {
    "central_agent": CENTRAL_AGENT_PROMPT,
    "router_micro_agent": ROUTER_MICRO_AGENT_PROMPT,
    "vp_marketing_agent": VP_MARKETING_AGENT_PROMPT,
    "vp_conversion_agent": VP_CONVERSION_AGENT_PROMPT,
    "vp_content_agent": VP_CONTENT_AGENT_PROMPT,
    "vp_distribution_agent": VP_DISTRIBUTION_AGENT_PROMPT,
    "vp_analytics_agent": VP_ANALYTICS_AGENT_PROMPT,
    "vp_tech_agent": VP_TECH_AGENT_PROMPT,
    "silent_bridge_growth_agent": SILENT_BRIDGE_GROWTH_AGENT_PROMPT,
    "solo_revenue_agent": SOLO_REVENUE_AGENT_PROMPT,
    "decision_forecast_optimization_agent": DECISION_FORECAST_OPTIMIZATION_AGENT_PROMPT,
    "expansion_risk_control_central_agent": EXPANSION_RISK_CONTROL_CENTRAL_AGENT_PROMPT,
    "sentinel_agent": SENTINEL_AGENT_PROMPT,
}
