# 🤖 AGENT BOOTLOADER

> **STOP! READ THIS FIRST.**
> This file contains the STRICT operating procedures for this project.

## 🛑 CRITICAL RULES

1.  **NO FREESTYLING**: Do not create files or start coding without an active `AT-X` task.
2.  **STATUS IS GOD**: `.agent/STATUS.md` is the single source of truth.
3.  **TOKEN EFFICIENCY**: Do NOT read all `constitution/*.md` files at start. Only read what you need, when you need it.

## 🚀 STARTUP SEQUENCE

### Step 1: Check Status
Read `.agent/STATUS.md` to see Active PRDs, Active Tasks, and Backlog.

### Step 2: Determine Action

#### A. New Feature Request?
1.  Run workflow: `.agent/workflows/create-prd.md`
2.  Output: `.agent/tasks/prd-[feature].md`
3.  **STOP** and ask for user approval.

#### B. PRD Approved?
1.  Run workflow: `.agent/workflows/generate-tasks.md`
2.  Output: `.agent/tasks/AT-[X]-task-[feature].md`
3.  Update `.agent/STATUS.md` to link the new task.
4.  **STOP** and ask for user approval.

#### C. Existing Task?
1.  Read the task file: `.agent/tasks/AT-[X]-task-[feature].md`
2.  Read the linked PRD (if available).
3.  **EXECUTE** the task.

## 📚 KNOWLEDGE BASE (Read on Demand)

- **Core Rules**: `.agent/constitution/README.md` (Read this if new)
- **Database**: `.agent/constitution/data-dictionary.md`
- **Errors**: `.agent/constitution/error-handling.md`
- **Philosophy**: `.agent/constitution/lean_philosophy.md`
- **Localization**: `.agent/constitution/localization.md` (for any new coding)

## 🛠️ UTILITIES

- **Logs**: `[Path/To/Your/Log/File]` (Check this for debugging)
- **Schema**: `[Path/To/Your/Schema]` (e.g., supabase/functions/, models/, etc.)

---
**VERIFY:** Before marking a task complete, update `.agent/STATUS.md` and the specific `AT-X` file.
