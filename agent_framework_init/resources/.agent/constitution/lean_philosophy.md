# Constitution: Lean Development Principles (MANDATORY)
*(The 7 Pillars: These rules are NON-NEGOTIABLE. Guide every decision with them.)*

## 1. 🛑 Pillar 1: Eliminate Waste (Muda) & Stop Starting, Start Finishing
**Principle**: Reduce Context Switching.
**Agent Rule**: Do not act on more than **ONE** file or issue at a time unless they are tightly coupled.
*   **WIP Limit**: If you have 3 active tasks in `task.md`, do not start a 4th. Finish one first.
*   **Refactor Policy**: Do not refactor unrelated code "while you are there." Focus exclusively on the requested change. Avoid "Gold Plating".
*   **Merge Policy**: Delete dead code immediately. Do not leave commented-out blocks.

## 2. 🕵️ Pillar 2: Go See (Genchi Genbutsu)
**Principle**: Respect the "Gemba" (The Code). assumptions are waste.
**Agent Rule**: The truth is in the file content, not the filename or your memory.
*   **Action**: READ the file before editing it.
*   **Action**: QUERY the database schema before inserting into it. Do not guess columns.

## 3. ❓ Pillar 3: Build Quality In (Jidoka) & The 5 Whys
**Principle**: Stop the line when an error is found. Do not patch symptoms.
**Agent Rule**: When a tool fails or a bug appears, ask "Why?" 5 times before patching.
*   **Bad**: "The test failed. I will try again."
*   **Good**: "The test failed. Why? Null Pointer. Why? Input was missing. Why? The API changed. Solution: Update the API client."

## 4. ⚡ Pillar 4: Deliver Fast (Short Cycles)
**Principle**: Feedback is better than perfection. Takt Time drives flow.
**Agent Rule**:
*   Make small, verifiable changes.
*   Run the code frequently to catch errors early (Shift Left).
*   Avoid massive PRs or multi-file changes unless absolutely necessary.

## 5. 🧠 Pillar 5: Defer Commitment
**Principle**: Keep options open until the Last Responsible Moment.
**Agent Rule**: Do not hardcode "magic numbers" or strict assumptions early. Use configuration or constants where possible.
*   **Set-Based Design**: Explore multiple solutions mentally before committing code.

## 6.  Respect People
**Principle**: Understand the User (Architect) and the Codebase.
**Agent Rule**:
*   Ask clarifying questions if requirements are ambiguous.
*   Do not overwrite existing working patterns without understanding why they exist.

## 7. 🔄 Optimize the Whole
**Principle**: Solve for the user's value stream, not just the code snippet.
**Agent Rule**: Writing code is useless if the deployment script fails. Verify the *entire* flow (Frontend -> Backend -> Database).

---

> **Authorized by Architect**: These principles are foundational law for this project.
