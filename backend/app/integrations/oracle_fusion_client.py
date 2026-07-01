"""Oracle Fusion integration client stub.

Phase 2 will implement:
  - OAuth2 client credentials flow to obtain Fusion access tokens
  - SCIM /Users endpoint calls (create/update/deactivate/search)
  - Fusion Security REST API calls (role assignments, contexts)
  - Retry / circuit-breaker handling
  - Rate-limit awareness (Oracle imposes per-minute limits)
"""

import logging
from typing import Any, Dict, Optional

from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()


class OracleFusionClient:
    """
    Thin HTTP wrapper for Oracle Fusion Cloud APIs.

    Currently a stub — replace method bodies in Phase 2 with real httpx calls.
    """

    def __init__(self) -> None:
        self.base_url = settings.ORACLE_FUSION_BASE_URL
        self._token: Optional[str] = None

    # ------------------------------------------------------------------
    # Authentication
    # ------------------------------------------------------------------

    def _get_token(self) -> str:
        """Obtain (or return cached) OAuth2 access token."""
        # TODO Phase 2: implement client-credentials grant
        logger.warning("OracleFusionClient._get_token is a stub — not making real API calls.")
        return "stub-token"

    # ------------------------------------------------------------------
    # SCIM User operations
    # ------------------------------------------------------------------

    def get_user(self, fusion_user_id: str) -> Dict[str, Any]:
        """Fetch a user from Oracle Fusion SCIM API."""
        logger.info("STUB: get_user(%s)", fusion_user_id)
        return {}

    def create_user(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Create a user in Oracle Fusion via SCIM."""
        logger.info("STUB: create_user(%s)", payload.get("userName"))
        return {}

    def update_user(self, fusion_user_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Update a user in Oracle Fusion via SCIM PATCH."""
        logger.info("STUB: update_user(%s)", fusion_user_id)
        return {}

    def deactivate_user(self, fusion_user_id: str) -> bool:
        """Deactivate / lock a user in Oracle Fusion."""
        logger.info("STUB: deactivate_user(%s)", fusion_user_id)
        return True

    # ------------------------------------------------------------------
    # Role / Security operations
    # ------------------------------------------------------------------

    def assign_role(self, fusion_user_id: str, role_code: str) -> bool:
        """Assign a role to a user in Oracle Fusion Security REST API."""
        logger.info("STUB: assign_role user=%s role=%s", fusion_user_id, role_code)
        return True

    def remove_role(self, fusion_user_id: str, role_code: str) -> bool:
        """Remove a role from a user in Oracle Fusion."""
        logger.info("STUB: remove_role user=%s role=%s", fusion_user_id, role_code)
        return True
