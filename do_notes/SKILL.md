---
name: Do Notes
description: Instructions to look for files in "To_do" folder, analyze them, create tasks/implementation plan, and start working.
---

# Do Notes Instructions

This skill instructs the agent to process todo notes found in a specific folder.

## Workflow

1.  **Locate "To_do" Folder**:
    *   Search for a folder named "To_do" in the current workspace.
    *   Identify all files within this folder (usually text files and other sample files).

2.  **Analyze and Plan**:
    *   Read and analyze the content of the files found in "To_do".
    *   Create a set of actionable tasks based on the analysis.
    *   Create a detailed implementation_plan.md artifact.
    *   **CRITICAL**: As part of this process, generate necessary questions to streamline and polish the implementation plan. If there are ambiguities or missing details, list them as questions for the user in the plan or via 
otify_user if they block progress.

3.  **Cleanup**:
    *   Once the plan is created and tasks are defined, DELETE the files in the "To_do" folder that have been incorporated into the plan.

4.  **Execute**:
    *   Start working on the created tasks immediately.
