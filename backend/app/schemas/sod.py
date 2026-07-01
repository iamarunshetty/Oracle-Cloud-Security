"""SOD Pydantic schemas (stub — ready for full engine implementation)."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from app.schemas.base import OrmBase


class SodEvaluationRequest(OrmBase):
    """Request to evaluate SOD conflicts for a proposed role assignment."""

    user_id: str
    proposed_role_ids: List[str]
    context: Optional[Dict[str, Any]] = None


class SodViolation(OrmBase):
    rule_id: str
    rule_name: str
    risk_level: str  # CRITICAL | HIGH | MEDIUM | LOW
    conflicting_role_1: str
    conflicting_role_2: str
    description: Optional[str] = None


class SodEvaluationResponse(OrmBase):
    """SOD evaluation result."""

    user_id: str
    proposed_role_ids: List[str]
    has_violations: bool
    violations: List[SodViolation]
    risk_summary: Dict[str, int]  # {"CRITICAL": 0, "HIGH": 1, ...}
    recommendation: str
