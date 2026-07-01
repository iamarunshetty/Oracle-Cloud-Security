# Oracle Fusion Security Administration Workbench

Enterprise-grade Python platform for managing Oracle Fusion Cloud user lifecycle, role administration, SOD analysis, security context management, and environment migration activities.

---

## Architecture Overview

```
Oracle-Cloud-Security/
├── backend/              # FastAPI application (Python 3.11)
│   ├── app/
│   │   ├── api/          # REST API endpoints (versioned under /api/v1)
│   │   ├── core/         # Config, database, logging
│   │   ├── models/       # SQLAlchemy ORM models
│   │   ├── schemas/      # Pydantic request/response schemas
│   │   ├── repositories/ # Data access layer
│   │   ├── services/     # Business logic
│   │   ├── integrations/ # Oracle Fusion API client
│   │   ├── sod_engine/   # Segregation of Duties analysis
│   │   └── workers/      # Celery background tasks
│   ├── alembic/          # Database migrations
│   ├── requirements.txt
│   ├── pyproject.toml
│   └── Dockerfile
├── frontend/             # React placeholder (Phase 2)
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Quick Start

### Prerequisites

- Python 3.11+
- Redis (for background workers)
- SQL Server OR SQLite (default for local dev)
- Node.js 20+ (for frontend, Phase 2)

### 1. Clone and configure

```bash
git clone https://github.com/iamarunshetty/Oracle-Cloud-Security.git
cd Oracle-Cloud-Security

# Copy and edit environment variables
cp .env.example .env
# Edit .env — set DATABASE_URL, REDIS_URL, Oracle Fusion credentials, etc.
```

### 2. Install Python dependencies

```bash
cd backend
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run database migrations

```bash
# Uses SQLite by default (DATABASE_URL=sqlite:///./dev.db)
alembic upgrade head
```

### 4. Start the API

```bash
# Development (auto-reload)
uvicorn run:app --reload

# Or
python run.py
```

API will be available at: http://localhost:8000  
Interactive docs (Swagger): http://localhost:8000/docs  
ReDoc: http://localhost:8000/redoc  
Health check: http://localhost:8000/health

### 5. Start the Celery worker (optional)

```bash
celery -A app.workers.celery_app worker --loglevel=info
```

---

## Docker Compose (recommended for local dev)

Starts the API, Celery worker, and Redis in one command.

```bash
docker-compose up --build
```

| Service | URL / Port |
|---------|-----------|
| API | http://localhost:8000 |
| Redis | localhost:6379 |

> **SQL Server:** By default, Docker Compose uses SQLite. To use SQL Server locally, uncomment the `db` service in `docker-compose.yml` and update `DATABASE_URL`.

---

## API Endpoints

All endpoints are versioned under `/api/v1`.

| Module | Method | Path | Description |
|--------|--------|------|-------------|
| Users | GET | `/api/v1/users/` | List users |
| Users | POST | `/api/v1/users/` | Create user |
| Users | GET | `/api/v1/users/{id}` | Get user |
| Users | PATCH | `/api/v1/users/{id}` | Update user |
| Users | DELETE | `/api/v1/users/{id}` | Delete user |
| Users | POST | `/api/v1/users/{id}/lock` | Lock user |
| Users | POST | `/api/v1/users/{id}/unlock` | Unlock user |
| Users | POST | `/api/v1/users/{id}/suspend` | Suspend user |
| Users | GET | `/api/v1/users/search` | Search users |
| Roles | GET | `/api/v1/roles/` | List roles |
| Roles | POST | `/api/v1/roles/` | Create role |
| Roles | GET | `/api/v1/roles/{id}` | Get role |
| Roles | PATCH | `/api/v1/roles/{id}` | Update role |
| Roles | DELETE | `/api/v1/roles/{id}` | Delete role |
| Assignments | POST | `/api/v1/assignments/` | Assign role to user |
| Assignments | DELETE | `/api/v1/assignments/{user_id}/roles/{role_id}` | Remove role from user |
| Assignments | GET | `/api/v1/assignments/{user_id}/roles` | List user role assignments |
| SOD | POST | `/api/v1/sod/evaluate` | Evaluate SOD conflicts (stub) |
| Audit | GET | `/api/v1/audit/` | List audit logs |
| Audit | POST | `/api/v1/audit/search` | Search audit logs |

---

## Database Migrations (Alembic)

```bash
# Apply all pending migrations
alembic upgrade head

# Create a new migration
alembic revision --autogenerate -m "your description"

# Roll back one migration
alembic downgrade -1

# View migration history
alembic history
```

---

## Background Jobs (Celery)

### Bulk user import

```python
from app.workers.tasks import bulk_user_import

# Dispatch asynchronously
result = bulk_user_import.delay(rows=[
    {"username": "jdoe", "email": "jdoe@example.com", "first_name": "John"},
    ...
])

# Check status
print(result.status)
print(result.get(timeout=60))
```

---

## Configuration

All configuration is managed through environment variables. See `.env.example` for the full list.

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | SQLAlchemy connection string (SQLite or SQL Server) |
| `REDIS_URL` | Redis connection URL |
| `CELERY_BROKER_URL` | Celery broker URL (typically same as Redis) |
| `ORACLE_FUSION_BASE_URL` | Oracle Fusion Cloud instance URL |
| `AZURE_TENANT_ID` | Microsoft Entra ID tenant for authentication |
| `SECRET_KEY` | JWT signing secret (use a long random string in production) |
| `LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) |
| `CORS_ORIGINS` | Comma-separated list of allowed frontend origins |

---

## Implementation Roadmap

### Phase 1 (Current) — Foundation scaffold ✅
- FastAPI + SQLAlchemy + Alembic setup
- Core models: User, Role, UserRoleAssignment, AuditLog
- CRUD API endpoints for users, roles, assignments
- SOD evaluation stub
- Celery + Redis worker setup
- Bulk user import task (stub)
- Docker Compose environment

### Phase 2 — Core features
- [ ] Oracle Fusion SCIM + Security REST API integration
- [ ] Microsoft Entra ID authentication (JWT validation)
- [ ] Role-based access control (SecurityAdmin, Auditor, etc.)
- [ ] Full SOD rule engine with conflict detection + risk scoring
- [ ] Bulk file processing (Excel/CSV) with validation reports
- [ ] React frontend — Users, Roles, Audit modules
- [ ] Approval workflow for role assignments

### Phase 3 — Advanced features
- [ ] Security context management (BU, Ledger, Project, Legal Entity)
- [ ] Role mining + similarity analysis
- [ ] Environment migration engine (DEV → UAT → PROD)
- [ ] SOD mitigation tracking + exception workflows
- [ ] Executive compliance dashboard

### Phase 4 — AI & optimization
- [ ] AI Security Assistant (RAG + LLM for natural language queries)
- [ ] SOD risk prediction
- [ ] Performance optimization for 100k+ users
- [ ] Power BI / Excel / PDF reporting

---

## Contributing

1. Install dev dependencies: `pip install -r requirements-dev.txt`
2. Format code: `black app/`
3. Lint: `ruff check app/`
4. Run tests: `pytest`

---

## License

MIT