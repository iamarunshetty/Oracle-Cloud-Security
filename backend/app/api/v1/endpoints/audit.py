"""Audit log API endpoints."""

from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.audit_log import AuditLogResponse, AuditLogSearch
from app.services.audit_service import AuditService

router = APIRouter(prefix="/audit", tags=["Audit Logs"])


def _svc(db: Session = Depends(get_db)) -> AuditService:
    return AuditService(db)


@router.get("/", response_model=List[AuditLogResponse])
def list_audit_logs(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    svc: AuditService = Depends(_svc),
):
    """List recent audit log entries (newest first)."""
    return svc.list_logs(skip=skip, limit=limit)


@router.post("/search", response_model=List[AuditLogResponse])
def search_audit_logs(
    payload: AuditLogSearch,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    svc: AuditService = Depends(_svc),
):
    """Search audit logs by actor, action, resource, status, and date range."""
    return svc.search_logs(payload, skip=skip, limit=limit)
