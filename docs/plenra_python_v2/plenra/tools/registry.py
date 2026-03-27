from .agent_runner_tool import AgentRunnerTool
from .audit_logger_tool import AuditLoggerTool
from .counterfactual_tool import CounterfactualTool
from .dataset_builder_tool import DatasetBuilderTool
from .decision_gate_tool import DecisionGateTool
from .meta_controller_tool import MetaControllerTool
from .prompt_loader_tool import PromptLoaderTool
from .reality_reconciliation_tool import RealityReconciliationTool
from .simulation_tool import SimulationTool
from .state_machine_tool import StateMachineTool

TOOL_REGISTRY = {
    "agent_runner_tool": AgentRunnerTool,
    "audit_logger_tool": AuditLoggerTool,
    "counterfactual_tool": CounterfactualTool,
    "dataset_builder_tool": DatasetBuilderTool,
    "decision_gate_tool": DecisionGateTool,
    "meta_controller_tool": MetaControllerTool,
    "prompt_loader_tool": PromptLoaderTool,
    "reality_reconciliation_tool": RealityReconciliationTool,
    "simulation_tool": SimulationTool,
    "state_machine_tool": StateMachineTool,
}
