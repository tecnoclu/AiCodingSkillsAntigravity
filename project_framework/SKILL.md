---
name: project_framework
description: Creates a comprehensive Lean project management framework (rules, workflows, constitution)
---

# Project Framework Setup Skill

This skill creates a complete `.agent/` project management framework for any new project, based on the proven Lean structure used in the Koonol project.

## What This Skill Creates

### Directory Structure
```
.agent/
├── PIPELINE.md              # Multi-task tracking and queue management
├── tasks/                   # Individual task files
├── workflows/               # Reusable development workflows
├── templates/               # Templates for new tasks/docs
└── constitution/            # Project rules (The Golden Rules)
    ├── INDEX.md             # MANDATORY: The Golden Rules
    ├── lean_philosophy.md   # MANDATORY: The 7 Pillars (Non-negotiable)
    └── error-handling.md    # Reference: Error patterns
```

### Key Features
- **Multi-task tracking** - Track multiple concurrent projects in a pipeline
- **Status management** - Visual status tracking with emojis (🔴 🟡 🟢 ✅)
- **Detailed task specs** - Comprehensive task files with checklists and acceptance criteria
- **Standardized workflows** - Step-by-step development processes
- **Project constitution** - Coding standards, architecture principles, best practices

## Usage

Simply invoke this skill in any project workspace:

```
@project_framework
```

Or with custom options:

```
@project_framework --project-name "MyProject" --tech-stack "React, Node.js, PostgreSQL"
```

## What You'll Get

1. **PIPELINE.md** - Central task queue with:
   - Active tasks section
   - Prioritized task queue
   - Completed tasks archive
   - Pipeline statistics

2. **Task Template** - Reusable template including:
   - Overview and goals
   - Technical specifications
   - Acceptance criteria
   - Implementation checklist
   - Progress tracking

3. **Feature Workflow** - Complete development process:
   - Planning and specification
   - Branch creation
   - Backend/Frontend development
   - Testing and review
   - Deployment

4. **Constitution** - Project standards covering:
   - Architecture principles
   - Coding standards (TypeScript, Python, React)
   - Security standards
   - Testing requirements
   - Git workflow
   - Documentation standards

## Customization

After creation, customize these files for your project:
- Update tech stack in `constitution.md`
- Modify workflows for your process
- Add project-specific templates
- Create initial tasks

## Instructions for Antigravity

When this skill is invoked:

1. **Ask for project details:**
   - Project name
   - Tech stack (frontend, backend, database)
   - Team size (solo, small team, large team)
   - Development methodology (agile, waterfall, etc.)

2. **Create directory structure:**
   ```bash
   mkdir -p .agent/{tasks,workflows,templates,constitution}
   ```

3. **Generate PIPELINE.md:**
   - Create with project name in header
   - Include empty Active/Queue/Completed sections
   - Add usage instructions

4. **Generate constitution files:**
   - Create `.agent/constitution/INDEX.md` (Use template below - MANDATORY)
   - Create `.agent/constitution/lean_philosophy.md` (Use template below - MANDATORY)
   - Create `.agent/constitution/error-handling.md` (Tech Stack specific, e.g. Python exceptions or JS ErrorBoundary)
   - **Do NOT create docs/constitution.md**

5. **Generate templates:**
   - `task-template.md` - For creating new tasks
   - `bug-template.md` - For bug reports (optional)
   - `feature-spec-template.md` - For feature specs (optional)

6. **Generate workflows:**
   - `feature-workflow.md` - Standard feature development
   - `bugfix-workflow.md` - Bug fixing process
   - `review-workflow.md` - Code review checklist

7. **Create sample tasks (optional):**
   - Ask if user wants sample tasks created
   - If yes, create 2-3 placeholder tasks based on common needs

8. **Commit to git:**
   ```bash
   git add .agent/
   git commit -m "feat: Add project management framework (.agent/)"
   ```

9. **Provide usage guide:**
   - Show how to add new tasks
   - Explain status emojis
   - Demonstrate workflow usage

## Template: PIPELINE.md

```markdown
# [Project Name] Project Pipeline

**Last Updated:** [DATE]

---

## 🎯 Active Tasks (In Progress)

### None currently
*All tasks are in the queue*

---

## 📋 Task Queue (Prioritized)

*No tasks yet - add your first task!*

---

## ✅ Completed Tasks

*No completed tasks yet*

---

## 📊 Pipeline Statistics

- **Total Tasks:** 0
- **Active:** 0
- **Queued:** 0
- **Completed:** 0

---

## 🔄 How to Use This Pipeline

1. **Add New Task:** Create task file in `tasks/` using template
2. **Start Task:** Move from Queue to Active, update status to 🟡
3. **Complete Task:** Move to Completed, update status to ✅
4. **Status Emojis:**
   - 🔴 Not Started
   - 🟡 In Progress
   - 🟢 Ready for Review
   - ✅ Complete
   - 🔵 Blocked
   - ⏸️ On Hold
```

## Template: Task File

```markdown
# Task: [Task Name]

**Created:** YYYY-MM-DD  
**Status:** 🔴 Not Started  
**Priority:** [High/Medium/Low]  
**Estimated Effort:** [Small/Medium/Large]  
**Assignee:** [Name or TBD]

---

## 📋 Overview

[Brief description]

---

## 🎯 Goals

- [ ] Goal 1
- [ ] Goal 2

---

## 📐 Technical Specification

### Architecture Changes
- Component 1: Description

### Database Changes
- Schema changes

### API Changes
- New/modified endpoints

### Frontend Changes
- UI changes

---

## ✅ Acceptance Criteria

- [ ] Criterion 1
- [ ] All tests pass
- [ ] Code reviewed

---

## 📝 Implementation Checklist

### Phase 1: Planning
- [ ] Review requirements
- [ ] Create technical spec

### Phase 2: Backend
- [ ] Database migrations
- [ ] API endpoints
- [ ] Tests

### Phase 3: Frontend
- [ ] UI components
- [ ] Integration
- [ ] Tests

### Phase 4: Integration & Testing
- [ ] E2E testing
- [ ] Bug fixes

### Phase 5: Documentation & Deployment
- [ ] Documentation
- [ ] Code review
- [ ] Deploy

---

## 📊 Progress Tracking

| Phase | Status | Completed Date |
|-------|--------|----------------|
| Planning | 🔴 | - |
| Backend | 🔴 | - |
| Frontend | 🔴 | - |
| Integration | 🔴 | - |
| Documentation | 🔴 | - |

**Overall Progress:** 0%
```

## Best Practices

1. **Keep PIPELINE.md updated** - Update after every task status change
2. **One task at a time** - Focus on 1-2 active tasks maximum
3. **Detailed task files** - More detail = better execution
4. **Follow workflows** - Consistency leads to quality
5. **Review constitution** - Reference when making decisions

## Success Criteria

After running this skill, the project should have:
- ✅ Complete `.agent/` directory structure
- ✅ PIPELINE.md with clear instructions
- ✅ Task template ready to use
- ✅ At least one workflow defined
- ✅ Constitution with project standards
- ✅ Everything committed to git

## Notes

- This framework is lightweight and scalable
- Can be extended with more workflows/templates as needed
- Works well for solo developers and small teams
- Can integrate with issue trackers (GitHub Issues, Jira, etc.)
- Compatible with any tech stack

## Template: Constitution Index (INDEX.md)

```markdown
# [Project Name] Constitution: The Golden Rules
*(MANDATORY: Read this file first. It supersedes all assumptions.)*

## 1. 👥 The Human is the Architect
**Role**: The User is your **Architect & Business Logic Consultant**.
**Agent Rule**: Do not make unilateral decisions on business rules.
*   **Action**: When logic is ambiguous, ASK.
*   **Action**: Treat "Design Aesthetics" requirements as strict functional requirements.

## 2. 🛡️ Safety Protocol: "Verify, Don't Assume"
**Use this for**: All database interactions.
1.  **Reconnaissance**: Run SQL `SELECT column_name...` to see the *live* schema before writing code.
2.  **Constraints**: Check for `NOT NULL`, `UNIQUE`, and `CHECK` constraints.
3.  **Defensive Coding**: Wrap DB calls in `try/catch`. Handle `None`/`null` explicitly.

## 3. 🏗️ Lean Philosophy (The 7 Pillars)
*(MANDATORY: Read [lean_philosophy.md](lean_philosophy.md) for full Agent Rules)*
**Use this for**: Workflow and decision making.
1.  **Stop Starting, Start Finishing**: Max **3** active items in `task.md`.
2.  **Go See (Genchi Genbutsu)**: Read the file/db. Don't guess.
3.  **5 Whys**: Root cause analysis before patching bugs.
4.  **Eliminate Waste**: No gold-plating. No dead code.
5.  **Deliver Fast**: Small, verifiable changes.
6.  **Defer Commitment**: Use config/constants.
7.  **Optimize the Whole**: Verify the full flow (UI -> API -> DB).

## 4. 🌍 Localization (i18n)
**Use this for**: All UI and Data.
*   **UI**: No hardcoded text. Use translation hooks.
*   **Data**: Store money as `Decimal`. Store `currency` code with amounts.
*   **Dates**: Use ISO 8601 (UTC). Format on frontend based on locale.

## 5. 📚 Reference (Read Only if Needed)
*   `README.md`: Project overview & tech stack.
*   `error-handling.md`: Detailed code patterns for specific exceptions.
```

## Template: Lean Philosophy (lean_philosophy.md)

```markdown
# Constitution: Lean Development Principles (MANDATORY)
*(The 7 Pillars: These rules are NON-NEGOTIABLE. Guide every decision with them.)*

## 1. 🛑 Pillar 1: Eliminate Waste (Muda) & Stop Starting, Start Finishing
**Principle**: Reduce Context Switching.
**Agent Rule**: Do not act on more than **ONE** file or issue at a time unless they are tightly coupled.
*   **WIP Limit**: If you have 3 active tasks in `task.md`, do not start a 4th.
*   **Refactor Policy**: Do not refactor unrelated code. No "Gold Plating".
*   **Merge Policy**: Delete dead code immediately.

## 2. 🕵️ Pillar 2: Go See (Genchi Genbutsu)
**Principle**: Respect the "Gemba" (The Code). assumptions are waste.
**Agent Rule**: The truth is in the file content, not the filename.
*   **Action**: READ the file before editing it.
*   **Action**: QUERY the database schema before inserting into it.

## 3. ❓ Pillar 3: Build Quality In (Jidoka) & The 5 Whys
**Principle**: Stop the line when an error is found.
**Agent Rule**: When a tool fails, ask "Why?" 5 times before patching.

## 4. ⚡ Pillar 4: Deliver Fast (Short Cycles)
**Principle**: Feedback is better than perfection.
**Agent Rule**:
*   Make small, verifiable changes.
*   Run the code frequently (Shift Left).

## 5. 🧠 Pillar 5: Defer Commitment
**Principle**: Keep options open until the Last Responsible Moment.
**Agent Rule**: Do not hardcode "magic numbers". Use configuration.

## 6.  Respect People
**Principle**: Understand the User (Architect).
**Agent Rule**:
*   Ask clarifying questions if requirements are ambiguous.

## 7. 🔄 Optimize the Whole
**Principle**: Solve for the user's value stream.
**Agent Rule**: Verify the *entire* flow (Frontend -> Backend -> Database).
```
