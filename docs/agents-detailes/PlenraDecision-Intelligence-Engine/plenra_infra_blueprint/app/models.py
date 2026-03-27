from datetime import datetime

from sqlalchemy import JSON, Boolean, DateTime, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class DecisionEvent(Base):
    __tablename__ = "decision_events"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    decision_id: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    vertical_id: Mapped[str] = mapped_column(Text, nullable=False)
    decision_action: Mapped[str] = mapped_column(Text, nullable=False)
    decision_status: Mapped[str] = mapped_column(Text, nullable=False)
    budget_delta_percent: Mapped[float] = mapped_column(Numeric, nullable=False)
    gate_severity: Mapped[str] = mapped_column(Text, nullable=False)
    requires_manual_review: Mapped[bool] = mapped_column(Boolean, nullable=False)
    input_snapshot: Mapped[dict] = mapped_column(JSON, nullable=False)
    derived_fields: Mapped[dict] = mapped_column(JSON, nullable=False)
    debug_trace: Mapped[dict] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
