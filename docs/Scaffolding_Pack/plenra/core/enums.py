from enum import Enum


class DecisionStatus(str, Enum):
    PASS = "pass"
    HOLD = "hold"
    REDUCE = "reduce"
    STOP = "stop"
    COOLDOWN = "cooldown"
    MANUAL_REVIEW = "manual_review"


class DecisionAction(str, Enum):
    SCALE_UP = "scale_up"
    MAINTAIN = "maintain"
    REDUCE_15 = "reduce_15"
    REDUCE_30 = "reduce_30"
    PAUSE = "pause"
    START_COOLDOWN = "start_cooldown"
    SEND_TO_REVIEW = "send_to_review"


class GateSeverity(str, Enum):
    SAFE = "safe"
    WARNING = "warning"
    DANGER = "danger"


class PerformanceStatus(str, Enum):
    SCALE = "scale"
    OBSERVE = "observe"
    ITERATE = "iterate"
    COOLDOWN = "cooldown"
    TERMINATE = "terminate"


class LearningEligibility(str, Enum):
    ELIGIBLE = "eligible"
    BLOCKED = "blocked"
    REVIEW = "review"


class TrustLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RunMode(str, Enum):
    DETERMINISTIC = "deterministic"
    FAIL_CLOSED = "fail_closed"
    SAFE_FALLBACK = "safe_fallback"
