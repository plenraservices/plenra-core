from enum import Enum


class LearningEligibility(str, Enum):
    ELIGIBLE = "eligible"
    BLOCKED = "blocked"


class PerformanceStatus(str, Enum):
    SCALE = "scale"
    OBSERVE = "observe"
    ITERATE = "iterate"
    COOLDOWN = "cooldown"
    TERMINATE = "terminate"


class EvaluationResult(str, Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"
    NEUTRAL = "neutral"


class ConfidenceLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
