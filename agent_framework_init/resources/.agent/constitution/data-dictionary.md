# Data Dictionary

This document defines the valid values for enum-like fields, critical business rules, and database constraints. **All agents must reference this document** to ensure consistency.

---

## [Domain Entity Example: User Roles]

### `role_type` (TEXT)

**Valid Values:**
| Value | Description | Permissions |
|-------|-------------|-------------|
| `admin` | System Administrator | Full access |
| `editor` | Content Editor | Can edit content, cannot manage users |
| `viewer` | Read-only User | View access only |

**Database Constraint:**
```sql
CHECK (role_type IN ('admin', 'editor', 'viewer'))
```

---

## [Domain Entity Example: Order Status]

### `status` (TEXT)

**Valid Values:**
- `draft` - Initial state
- `pending` - Awaiting processing
- `completed` - Successfully finished
- `cancelled` - Terminated

**Business Rules:**
- An order cannot move from `cancelled` back to `draft`.
- Only `admin` can set status to `completed` manually.

---

## Best Practices for Agents

1. **Always validate enum values** before inserting/updating.
2. **Reference this document** when working with these fields.
3. **Update this document** if new values are added (with user approval).
4. **Add database constraints** for new enum fields.
5. **Add database comments** explaining the values.
