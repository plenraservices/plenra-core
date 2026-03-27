from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class RuntimeConfig:
    system_name: str = "Plenra"
    mode: str = "deterministic_fail_closed"
    environment: str = "production_ready_scaffold"
    timezone: str = "Asia/Jerusalem"
    max_override_rate: float = 0.05
    max_agent_iterations: int = 5
    cache_ttl_seconds: int = 3600
    ops_logger_schema_version: str = "OPS-01 v1.1.2"
    explainability_required: bool = True
    full_automation_only: bool = True


@dataclass(slots=True)
class SafetyConfig:
    fail_closed_on_uncertainty: bool = True
    require_gap_attack_question: bool = True
    require_loophole_scan: bool = True
    require_validation_gate: bool = True
    require_copy_source_of_truth: bool = True
    external_execution_tools_are_execution_only: bool = True


@dataclass(slots=True)
class PromptConfig:
    language_default: str = "en"
    return_json_only_by_default: bool = False
    include_behavioral_design_layer: bool = True
    include_explainability_layer: bool = True


@dataclass(slots=True)
class SystemConfig:
    runtime: RuntimeConfig = field(default_factory=RuntimeConfig)
    safety: SafetyConfig = field(default_factory=SafetyConfig)
    prompts: PromptConfig = field(default_factory=PromptConfig)


SYSTEM_CONFIG = SystemConfig()
