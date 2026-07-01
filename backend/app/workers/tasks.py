"""Background tasks for the Oracle Security Workbench."""

import logging
from typing import Any, Dict, List

from app.workers.celery_app import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(
    bind=True,
    max_retries=3,
    default_retry_delay=60,
    name="workers.bulk_user_import",
)
def bulk_user_import(self, rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Process a bulk user import payload (from Excel/CSV upload).

    Arguments:
        rows: list of dicts parsed from the uploaded file, each representing
              one user record.

    Returns:
        A summary dict with counts of created / updated / failed records.

    TODO Phase 2 — replace stub logic with:
      1. Validate each row against UserCreate schema
      2. Look up existing users by username / email
      3. Create or update users in the local DB
      4. Optionally call OracleFusionClient.create_user / update_user
      5. Record per-row audit log entries
      6. Return structured results for display in UI job-status panel
    """
    logger.info("bulk_user_import started: %d rows", len(rows))

    created = 0
    updated = 0
    failed = 0
    errors: List[Dict[str, Any]] = []

    for idx, row in enumerate(rows):
        try:
            # Stub — just validate that at minimum username + email are present
            username = row.get("username") or row.get("Username") or row.get("user_name")
            email = row.get("email") or row.get("Email")

            if not username or not email:
                raise ValueError("Missing required fields: username or email")

            # Placeholder for real DB + Fusion API calls
            logger.debug("Processing row %d: username=%s", idx, username)
            created += 1

        except Exception as exc:
            logger.warning("Row %d failed: %s", idx, exc)
            failed += 1
            errors.append({"row": idx, "error": str(exc), "data": row})

    result = {
        "total": len(rows),
        "created": created,
        "updated": updated,
        "failed": failed,
        "errors": errors,
    }
    logger.info("bulk_user_import complete: %s", result)
    return result
