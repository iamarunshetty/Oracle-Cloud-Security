# Frontend — Oracle Fusion Security Administration Workbench

> **Status: Phase 1 scaffold — placeholder only.**
> Full React implementation is planned for Phase 2.

## Tech Stack (planned)

| Layer | Technology |
|-------|-----------|
| Framework | React 18 + TypeScript |
| UI Library | Material UI (MUI) v6 |
| Routing | React Router v6 |
| Server state | TanStack Query (React Query) v5 |
| HTTP client | Axios |
| Build tool | Vite |
| Linting | ESLint + TypeScript-ESLint |

## Module Structure

```
src/
├── users/          # User management: create, search, lock, bulk import
├── roles/          # Role management: assign, remove, expiry, bulk operations
├── contexts/       # Data security: BU, ledger, inventory, project security
├── sod/            # SOD analysis: violation detection, risk scoring, mitigation
├── migration/      # Environment migration: export/compare/import DEV→UAT→PROD
├── approvals/      # Approval workflow: requests, review, approval actions
├── audit/          # Audit & compliance: logs, reports, dashboard
├── ai-assistant/   # AI assistant: natural-language queries, role recommendations
├── components/     # Shared UI components (layout, tables, forms, dialogs)
└── hooks/          # Shared custom React hooks (useApi, usePagination, etc.)
```

## Getting Started (local development)

```bash
# Install dependencies
cd frontend
npm install

# Start dev server (proxies /api to http://localhost:8000)
npm run dev
```

The app will be available at http://localhost:3000.

## Phase 2 Implementation Notes

Each module directory will contain:

- `pages/` — Route-level page components
- `components/` — Module-specific UI components
- `hooks/` — Module-specific React hooks
- `api.ts` — API call definitions (using Axios + React Query)
- `types.ts` — TypeScript types for the module's domain objects

### Priority order (recommended)

1. **Users** — User list, create, search, lock/unlock/suspend
2. **Roles** — Role list, assign/remove, bulk operations
3. **Audit** — Audit log viewer with filters
4. **SOD** — Violation heatmap and pre-approval simulation
5. **Migration** — Environment comparison matrix
6. **Approvals** — Workflow request/approval flow
7. **AI Assistant** — Natural language query interface
8. **Contexts** — Data security context management

### Authentication

Phase 2 will integrate Microsoft Entra ID (MSAL) for SSO.
See [MSAL React documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/tutorial-v2-react).
