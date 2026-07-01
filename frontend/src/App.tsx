import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

// Module placeholder pages — replace with full implementations in Phase 2
const Placeholder: React.FC<{ module: string }> = ({ module }) => (
  <div style={{ padding: 40, fontFamily: "sans-serif" }}>
    <h2>Oracle Security Workbench — {module}</h2>
    <p>
      This module is a <strong>scaffold placeholder</strong>. Full implementation is planned for
      Phase 2. See <code>frontend/README.md</code> for implementation notes.
    </p>
  </div>
);

const queryClient = new QueryClient();

const App: React.FC = () => (
  <QueryClientProvider client={queryClient}>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/users" replace />} />
        <Route path="/users/*" element={<Placeholder module="User Management" />} />
        <Route path="/roles/*" element={<Placeholder module="Role Management" />} />
        <Route path="/sod/*" element={<Placeholder module="SOD Analysis" />} />
        <Route path="/migration/*" element={<Placeholder module="Environment Migration" />} />
        <Route path="/approvals/*" element={<Placeholder module="Approvals" />} />
        <Route path="/audit/*" element={<Placeholder module="Audit & Compliance" />} />
        <Route path="/ai-assistant/*" element={<Placeholder module="AI Security Assistant" />} />
        <Route path="*" element={<Placeholder module="404 — Page Not Found" />} />
      </Routes>
    </BrowserRouter>
  </QueryClientProvider>
);

export default App;
