---
name: Text Note Processor
description: Scans the 'Text notes' folder for tasks, executes them, and deletes the processed files.
---

# Text Note Processor Instructions

This skill allows the agent to process ad-hoc tasks written in text files within a specific "Text notes" directory.

## Trigger
This skill should be invoked when the user explicitly instructs to "read text notes" or "process text notes".

## Workflow

1.  **Locate Directory**:
    *   Look for a directory named `Text notes` in the root of the current project/workspace.
    *   If not found, inform the user that no "Text notes" folder exists.

2.  **Scan for Files**:
    *   List all `.txt` files within the `Text notes` directory.
    *   If the directory is empty, inform the user there are no notes to process.

3.  **Process Each File**:
    *   For each text file found:
        a.  **Read**: Read the full content of the file.
        b.  **Analyze**: Determine if the content represents a valid, actionable task for the agent (e.g., "Fix the navigation bar", "Create a new controller").
        c.  **Execute**: If valid, perform the task using available tools (coding, terminal, etc.).
            *   *Note*: Treat the file content as a direct prompt/request from the user.
        d.  **Delete**: Upon successful completion of the task (or if the task was fully addressed), **DELETE** the text file to mark it as done.
        e.  **Report**: Briefly summarize what was done for that note.

4.  **Completion**:
    *   After processing all files, provide a final summary of actions taken.

## Safety & Errors
*   If a note is vague or impossible to understand, do NOT delete it. Skip it and report the issue to the user.
*   Only delete the file if the task was ACTIONED.
