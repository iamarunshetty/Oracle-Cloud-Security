"""FastAPI application factory."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as v1_router
from app.core.config import get_settings
from app.core.logging import configure_logging

settings = get_settings()


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""

    configure_logging()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=(
            "Enterprise-grade Oracle Fusion Security Administration Workbench API. "
            "Manages user lifecycle, role administration, SOD analysis, and migration activities."
        ),
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    # ------------------------------------------------------------------
    # Middleware
    # ------------------------------------------------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ------------------------------------------------------------------
    # Health check (outside versioned prefix for easy load-balancer probing)
    # ------------------------------------------------------------------
    @app.get("/health", tags=["Health"], summary="Health check")
    def health() -> dict:
        return {"status": "ok", "version": settings.APP_VERSION, "env": settings.ENVIRONMENT}

    # ------------------------------------------------------------------
    # API v1 routes
    # ------------------------------------------------------------------
    app.include_router(v1_router, prefix=settings.API_V1_PREFIX)

    return app
