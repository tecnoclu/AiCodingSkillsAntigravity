# Constitution: Localization (i18n) & Internationalization Standards
*(MANDATORY: Enforced for all new features and refactors)*

To ensure Koonol works seamlessly across different regions/countries (e.g., Nicaragua, Mexico, USA, Europe), all code must adhere to the following standards.

## 1. User Interface (Frontend)
*   **No Hardcoded Text**: All user-facing text must be wrapped in translation hooks.
    *   **Bad**: `<h1>Settings</h1>`
    *   **Good**: `<h1>{t('settings.title')}</h1>`
*   **Dynamic Formatting**: Use libraries for numbers, dates, and currencies.
    *   **Dates**: Use `Intl.DateTimeFormat` or `date-fns` with locale.
    *   **Currency**: NEVER hardcode symbols like `$`. Use `Intl.NumberFormat` with the company's configurated currency code.

## 2. Backend API
*   **Error Messages**: Return machine-readable error codes alongside human-readable default messages.
    *   **Example**: `{"code": "INVENTORY_LOW", "message": "Insufficient inventory", "params": {"available": 5}}`
*   **Dates**: Always exchange dates in **ISO 8601** format (UTC preferred). Let the frontend handle local timezone display.
*   **Currency**:
    *   Store monetary values as `Decimal` or `Numeric` in the database.
    *   Associative records (e.g., Payments, Sales) MUST store the `currency` code (ISO 4217, e.g., 'USD', 'NIO') alongside the amount.

## 3. Database
*   **Encoding**: Ensure all text columns use `UTF-8` to support special characters (e.g., Spanish accents, emojis).
*   **Currency Columns**: Tables dealing with money should include a `currency` column if the system supports multi-currency context per record.

## 4. Code Review Checklist
- [ ] Are all new UI strings in `en.json` (and other locale files)?
- [ ] Are dates formatted dynamically based on user locale?
- [ ] Is currency displayed using the dynamic company setting, not hardcoded '$'?
