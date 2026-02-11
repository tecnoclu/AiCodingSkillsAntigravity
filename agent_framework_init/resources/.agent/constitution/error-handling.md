# Error Handling Constitution

## Overview

This document defines the error handling standards and best practices for the [Project Name] application. All developers must follow these guidelines to ensure consistent, user-friendly error handling across the entire application.

## Core Principles

1. **User-First**: Users should never see technical errors, stack traces, or cryptic messages.
2. **Graceful Degradation**: The app should continue functioning when non-critical errors occur.
3. **Actionable Feedback**: Error messages should guide users on how to resolve the issue.
4. **Comprehensive Logging**: All errors should be logged with sufficient context for debugging.
5. **Consistent UX**: Error handling should be consistent across all features.

## Frontend Error Handling

### Error Boundaries

#### Global Error Boundary
- **Location**: `src/components/errors/GlobalErrorBoundary.tsx`
- **Purpose**: Catch all unhandled errors in the application.

```tsx
<GlobalErrorBoundary>
  <App />
</GlobalErrorBoundary>
```

#### Route Error Boundary
- **Location**: `src/components/errors/RouteErrorBoundary.tsx`
- **Purpose**: Catch errors at the route level without crashing the entire app.

```tsx
<RouteErrorBoundary>
  <YourRouteComponent />
</RouteErrorBoundary>
```

### API Error Handling

#### Using the API Error Handler

```typescript
import { apiFetch, ApiError } from '@/utils/apiErrorHandler';

try {
  const data = await apiFetch('/api/endpoint', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
} catch (error) {
  if (error instanceof ApiError) {
    // Show user-friendly message
    toast.error(error.userMessage?.message || 'An error occurred');
  }
}
```

## Backend Error Handling

### Using Custom Exceptions

```python
from app.libs.error_types import (
    NotFoundError,
    ValidationError,
    AuthenticationError,
    BusinessRuleError,
)

# Not found
raise NotFoundError("Resource", details={"id": resource_id})

# Validation error
raise ValidationError(
    "Invalid input",
    details={"field": "email", "value": email}
)
```

### Error Response Format

All backend errors should follow a standardized format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "User-friendly message",
    "timestamp": "ISO-8601 Timestamp",
    "request_id": "uuid",
    "details": {
      "field": "value"
    }
  }
}
```

## Error Logging Strategy

### Frontend Logging
- Log errors to console with context.
- Integrate with monitoring service (e.g., Sentry) in production.

### Backend Logging
- Use standard logging library.
- Log error context, user ID, and stack trace for debugging.

## Best Practices

### DO ✅
- Use custom exceptions for business logic errors.
- Provide actionable error messages.
- Log errors with sufficient context.
- Filter sensitive data from error responses.

### DON'T ❌
- Expose stack traces to users.
- Log sensitive data (passwords, tokens, etc.).
- Swallow errors silently.
- Use generic "Something went wrong" without context.

## Updates
This document should be updated when error handling patterns change or new error types are added.
