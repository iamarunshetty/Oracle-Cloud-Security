"""SOD (Segregation of Duties) API endpoints — stub for Phase 2 full implementation."""

from fastapi import APIRouter

from app.schemas.sod import SodEvaluationRequest, SodEvaluationResponse
from app.sod_engine.sod_service import SodEngineService

router = APIRouter(prefix="/sod", tags=["SOD Analysis"])

_engine = SodEngineService()


@router.post("/evaluate", response_model=SodEvaluationResponse)
def evaluate_sod(payload: SodEvaluationRequest):
    """
    Evaluate SOD conflicts for a proposed set of role assignments.

    Phase 1 — returns stub response with no violations.
    Phase 2 — full rule engine with conflict detection, risk scoring, and
    mitigation workflow integration.
    """
    return _engine.evaluate(payload)
