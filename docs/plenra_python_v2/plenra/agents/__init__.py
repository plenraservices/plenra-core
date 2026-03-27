from .central_agent import CentralAgent
from .router_micro_agent import RouterMicroAgent
from .vp_marketing_agent import VPMarketingAgent
from .vp_conversion_agent import VPConversionAgent
from .vp_content_agent import VPContentAgent
from .vp_distribution_agent import VPDistributionAgent
from .vp_analytics_agent import VPAnalyticsAgent
from .vp_tech_agent import VPTechAgent
from .silent_bridge_growth_agent import SilentBridgeGrowthAgent
from .solo_revenue_agent import SoloRevenueAgent
from .decision_forecast_optimization_agent import DecisionForecastOptimizationAgent
from .expansion_risk_control_central_agent import ExpansionRiskControlCentralAgent
from .sentinel_agent import SentinelAgent

AGENT_REGISTRY = {
    "central_agent": CentralAgent,
    "router_micro_agent": RouterMicroAgent,
    "vp_marketing_agent": VPMarketingAgent,
    "vp_conversion_agent": VPConversionAgent,
    "vp_content_agent": VPContentAgent,
    "vp_distribution_agent": VPDistributionAgent,
    "vp_analytics_agent": VPAnalyticsAgent,
    "vp_tech_agent": VPTechAgent,
    "silent_bridge_growth_agent": SilentBridgeGrowthAgent,
    "solo_revenue_agent": SoloRevenueAgent,
    "decision_forecast_optimization_agent": DecisionForecastOptimizationAgent,
    "expansion_risk_control_central_agent": ExpansionRiskControlCentralAgent,
    "sentinel_agent": SentinelAgent,
}
