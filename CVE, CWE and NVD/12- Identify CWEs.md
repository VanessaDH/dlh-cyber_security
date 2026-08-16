# CWE Analysis: `get_user()` Function

## The Code

```python
import sqlite3
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username='" + username + "';"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user
```

## 1. Identified Weakness

The `username` parameter is concatenated directly into a SQL query string instead of being passed as a parameterized value. This means any input can alter the structure of the SQL query itself, not just its data — the classic definition of an injection flaw.

## 2. CWE Classification

**Primary: CWE-89 — Improper Neutralization of Special Elements used in an SQL Command ("SQL Injection")**
The root cause: user-controlled input (`username`) is inserted into a SQL statement via string concatenation without sanitization, escaping, or parameterization.

**Related/contributing: CWE-20 — Improper Input Validation**
No validation is performed on `username` before it's used — no length checks, allow-listing, or type checks — which is the broader weakness category SQL injection often falls under.

**Secondary (minor): CWE-404 — Improper Resource Shutdown or Release**
If `cursor.execute(query)` raises an exception (which it will on malicious input causing malformed SQL, or any DB error), `conn.close()` on the last line never executes, leaking the database connection. There's no `try/finally` or context manager to guarantee cleanup.

## 3. Security Implications and Attack Scenarios

**SQL Injection (CWE-89) — the critical issue:**

An attacker could supply a crafted `username` value to manipulate the query. Examples:

- **Authentication bypass**: `username = "admin' --"` turns the query into:
  ```sql
  SELECT * FROM users WHERE username='admin' --';
  ```
  The `--` comments out the rest of the query, potentially returning the admin user without needing a password check elsewhere in the flow.

- **Data exfiltration via UNION**: `username = "' UNION SELECT username, password, NULL FROM users --"` could be used to pull data from other tables/columns than intended, exposing credentials or sensitive fields.

- **Destructive queries** (if the driver/config allows multiple statements): `username = "'; DROP TABLE users; --"` could delete or corrupt data.

- **Blind/boolean-based injection**: even without visible output, an attacker can infer data by crafting inputs that change query truthiness (`' OR '1'='1`) and observing behavior differences.

**Impact**: unauthorized data access, authentication bypass, data tampering or loss, and potentially full database compromise — all from a single unsanitized string concatenation.

## 4. Recommended Fixes

**Fix the SQL injection (CWE-89) — use parameterized queries:**

```python
import sqlite3

def get_user(username):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = ?;"
        cursor.execute(query, (username,))
        return cursor.fetchone()
```

Key changes:
- The `?` placeholder lets the SQLite driver handle the value safely — user input is always treated as data, never as part of the SQL syntax, eliminating the injection vector entirely.
- Using `with sqlite3.connect(...)` as a context manager ensures the connection is properly closed even if an exception occurs, addressing the CWE-404 resource-leak issue.

**Additional hardening (addressing CWE-20):**
- Validate `username` format before querying (e.g., expected length, allowed characters) as defense-in-depth, even though parameterization already neutralizes injection.
- Avoid `SELECT *` — explicitly select only the columns needed (e.g., `id, username, email`), so sensitive fields (like password hashes) aren't unnecessarily pulled into application memory or accidentally exposed elsewhere in the code.
- Add error handling (`try/except`) around the database call to fail gracefully and avoid leaking internal error details (like raw SQL errors) back to end users, which can itself aid attackers in crafting further attacks.
- Use least-privilege database credentials so that even if injection were somehow possible, the account running these queries can't perform destructive operations like `DROP TABLE`.
