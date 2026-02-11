# Constitution: Error Prevention Protocol
*(MANDATORY: Follow this protocol for all database interactions and critical flows)*

## 🛡️ Core Principle: "Verify, Don't Assume"
**Objective:** Eliminate runtime errors (500s), logic gaps, and data corruption by enforcing strict verification steps.

---

### 1. 🕵️ Phase 1: Reconnaissance (Before Coding)
**Mandatory Action**: You MUST query the live database schema before writing code.
*   **Do NOT trust ORM models** or code comments; they may be outdated.
*   **Do NOT assume constraints**; verify them.

#### Required SQL Verification Queries:
1.  **Check Columns & Nullability**:
    ```sql
    SELECT column_name, data_type, is_nullable, column_default 
    FROM information_schema.columns 
    WHERE table_name = 'target_table';
    ```
    *   *Self-Correction*: "Am I inserting a NULL into a NOT NULL column?"

2.  **Check Constraints (Keys & Checks)**:
    ```sql
    SELECT conname, pg_get_constraintdef(oid) 
    FROM pg_constraint 
    WHERE conrelid = 'target_table'::regclass;
    ```
    *   *Self-Correction*: "Am I violating a unique constraint or a check constraint (e.g., balance >= 0)?"

3.  **Check Foreign Keys**:
    *   *Self-Correction*: "Does the `company_id` or `user_id` I am using actually exist in the referenced table?"

---

### 2. 🛡️ Phase 2: Defensive Implementation
**Mandatory Action**: Wrap all external interactions in specific error handling blocks.

1.  **No Naked database calls**:
    ```python
    try:
        result = db.execute(query)
    except integrity_error:
        # Handle duplicate keys or foreign key violations explicitly
        return formatted_error("Conflict", 409)
    except Exception as e:
        log_error(e)
        return formatted_error("Internal Error", 500)
    ```

2.  **Explicit Null Handling**:
    *   Assume every optional input is `None`.
    *   Use `.get('field', default_value)` instead of `['field']` unless validated.

3.  **Precision Matters**:
    *   **Currency**: ALWAYS use `Decimal`. NEVER `float`.
    *   **Dates**: ALWAYS use UTC ISO 8601.

---

### 3. 🚦 Phase 3: Pre-Commit Checklist
Before submitting code, you must verify:
- [ ] Did I run the SQL queries to check the actual schema?
- [ ] Did I handle the "Record Not Found" (404) case?
- [ ] Did I handle the "Permission Denied" (403) case?
- [ ] Did I verify that my test inputs (IDs, FKs) actually exist in the DB?

---

> **Authorized by User**: implemented as a core workflow rule on 2026-02-06.
