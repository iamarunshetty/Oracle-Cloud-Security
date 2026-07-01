"""API v1 router — aggregates all endpoint routers under /api/v1."""

from fastapi import APIRouter

from app.api.v1.endpoints import assignments, audit, roles, sod, users

router = APIRouter()

router.include_router(users.router)
router.include_router(roles.router)
router.include_router(assignments.router)
router.include_router(sod.router)
router.include_router(audit.router)
