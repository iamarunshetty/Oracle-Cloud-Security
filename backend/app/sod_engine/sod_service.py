"""SOD engine stub — structured for full rule evaluation engine implementation."""

from typing import Dict, List

from app.schemas.sod import SodEvaluationRequest, SodEvaluationResponse, SodViolation


class SodEngineService:
    """
    Segregation of Duties evaluation engine.

    Current implementation: stub that returns no violations.
    TODO — Phase 2:
      - Load SOD rule library from DB / Excel upload
      - Detect conflicting role pairs for the proposed assignment
      - Apply risk scoring (CRITICAL / HIGH / MEDIUM / LOW)
      - Support pre-approval simulation mode
      - Persist violations and trigger mitigation workflow
    """

    def evaluate(self, request: SodEvaluationRequest) -> SodEvaluationResponse:
        # Stub — no rule evaluation yet
        violations: List[SodViolation] = []
        risk_summary: Dict[str, int] = {
            "CRITICAL": 0,
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0,
        }

        return SodEvaluationResponse(
            user_id=request.user_id,
            proposed_role_ids=request.proposed_role_ids,
            has_violations=False,
            violations=violations,
            risk_summary=risk_summary,
            recommendation="No SOD rules configured yet. Implement rule library in Phase 2.",
        )
