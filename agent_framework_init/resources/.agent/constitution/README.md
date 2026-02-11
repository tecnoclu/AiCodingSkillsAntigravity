# [Project Name] Constitution

**Version:** 1.0
**Last Updated:** [Date]
**Status:** Active

---

## 📂 Project Management

> **📖 See [Project Management Guide](../docs/project-management-guide.md)** for how to use PIPELINE.md, workflows, and task tracking

**Quick Reference:**
- **PIPELINE.md** - Active tasks, task queue, and completed work
- **workflows/** - Step-by-step process guides (e.g., `/feature-workflow`)
- **tasks/** - Detailed task specifications and tracking
- **constitution/** - Project rules and standards (you are here)

---

## 🎯 Project Mission

[Brief description of what the project is trying to achieve. Example: Build a comprehensive management system that is Secure, Maintainable, Scalable, and User-friendly.]

---

## 📐 Architecture Principles

### 1. Tech Stack
*(Customize this section for your specific project)*
- **Frontend:** [e.g., React, Vue, Svelte]
- **Backend:** [e.g., Python FastAPI, Node.js, Go]
- **Database:** [e.g., PostgreSQL, MongoDB]
- **Styling:** [e.g., Tailwind CSS, CSS Modules]
- **Testing:** [e.g., Pytest, Vitest, Jest]

### 2. Code Organization
*(Customize directory structure)*
```
project_root/
├── frontend/          # Client-side application
├── backend/           # Server-side application
└── .agent/            # Project management (DO NOT DELETE)
```

### 3. Database Access (CRITICAL)

> **⚠️ ALWAYS use the official client library - NEVER use raw HTTP calls unless absolutely necessary**

**✅ CORRECT:**
```python
# Example: Using an official client
from app.libs.db_client import get_client

client = get_client()
result = await client.table('users').select('*').execute()
```

**❌ WRONG:**
```python
# Avoid raw requests if a client exists
import httpx
response = await httpx.get('https://api.example.com/data')
```

---

## 💻 Coding Standards

### General Rules
- **TypeScript**: Use explicit types, interfaces, and avoid `any`.
- **Python**: Use type hints, Pydantic models, and docstrings.
- **Naming**: Use consistent naming conventions (camelCase for JS/TS, snake_case for Python).
- **Comments**: Explain *why*, not just *what*.

---

## 🔒 Security Standards

1. **Authentication**: Use secure methods (JWT, OAuth) and validate sessions.
2. **Data Protection**: Sanitize inputs, use parameterized queries, and never commit secrets.
3. **Dependencies**: Regularly audit for vulnerabilities.

---

## 🧪 Testing Standards

- **Unit Tests**: Test business logic and individual components.
- **Integration Tests**: Verify that different parts of the system work together.
- **Coverage**: Aim for high code coverage (e.g., 80%+).

---

## 📝 Documentation Standards

- **Code**: JSDoc/docstrings for public functions.
- **Project**: Update READMEs and architecture docs.
- **API**: Maintain clear API documentation (OpenAPI/Swagger).

---

## 🔄 Git Workflow

- **Branches**: usage `feature/...`, `bugfix/...`, `chore/...`
- **Commits**: Use semantic commit messages (e.g., `feat: ...`, `fix: ...`).
- **PRs**: Require review and passing tests before merging.

---

## 🚨 Error Handling Standards

> **📖 See [`error-handling.md`](./error-handling.md)** for complete implementation details.

1. **User-Friendly**: No stack traces or technical jargon for end-users.
2. **Logging**: Log errors with context for debugging.
3. **Consistency**: Use standardized error response formats.

---

## ⚠️ What NOT to Do

- **Never** commit secrets.
- **Never** skip tests for convenience.
- **Never** ignore linter warnings.

---

## 📞 When in Doubt

1. Check this constitution.
2. Review existing code patterns.
3. Ask for clarification/review.

---

## 🔄 Updates to This Constitution

Update this document as the project evolves. Document the reasoning for changes.
