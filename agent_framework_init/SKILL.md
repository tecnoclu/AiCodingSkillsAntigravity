---
name: Agent Framework Init
description: Initialize a new project with the SnarkTank-based Agent Framework.
---

# Agent Framework Initialization

This skill helps you set up a robust, agentic development environment based on the SnarkTank framework by copying the necessary `.agent` directory structure to your current project.

## 🚀 How to Use

1.  **Initialize Project**: Run the following PowerShell command to copy the framework files from this skill's `resources` directory to your current location:

    ```powershell
    Copy-Item -Recurse -Force "c:\Users\rgonz\Documents - local\Apps\skills\agent_framework_init\resources\.agent" .
    ```

2.  **Verify Installation**:
    *   Check that `.agent/AGENT_HANDOFF.md` exists.
    *   Check that `.agent/STATUS.md` exists.

3.  **Customize**:
    *   Edit `.agent/constitution/data-dictionary.md` to match your database schema.
    *   Edit `.agent/constitution/README.md` to update project-specific details.

4.  **Start coding**: follow the instructions in `.agent/AGENT_HANDOFF.md`.

## 📂 What's Included

*   **`AGENT_HANDOFF.md`**: The "Operating System" bootloader for agents.
*   **`STATUS.md`**: The single source of truth for project status.
*   **Workflows**:
    *   `create-prd.md`: Creating vivid Product Requirements Documents.
    *   `generate-tasks.md`: Breaking PRDs into atomic tasks.
*   **Constitution**:
    *   `README.md`: Core rules.
    *   `lean_philosophy.md`: Development approach.
    *   `error-handling.md`: Robust error patterns.

## 🙌 Shoutouts

This framework is heavily inspired by and based on the **[SnarkTank AI Dev Tasks](https://github.com/snarktank/ai-dev-tasks)** repository. Big thanks to the SnarkTank team for pioneering these agentic workflows!
