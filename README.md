# Demo App

A simple Flask application.

## Setup
1. Clone the repo-
2. Run pip install -r requirements.txt
3. Run python app.py
4. END
```


--

---

## What your scanner should find

| Finding | Type | Severity |
|---------|------|----------|
| DB_PASSWORD hardcoded | HARDCODED_SECRET | CRITICAL |
| STRIPE_KEY hardcoded | HARDCODED_SECRET | CRITICAL |
| AWS keys hardcoded | HARDCODED_SECRET | CRITICAL |
| SQL injection in get_user | SQL_INJECTION | CRITICAL |
| SQL injection in get_orders | SQL_INJECTION | CRITICAL |
| Open S3 bucket | OPEN_S3 | HIGH |
| Wildcard IAM permissions | OPEN_S3 | HIGH |
| JWT no expiry | JWT_NO_EXPIRY | HIGH |
| CORS allows all origins | CORS_MISCONFIGURATION | HIGH |
| process_order() complexity 20+ | HIGH_COMPLEXITY | HIGH |
| Duplicate tax logic | DUPLICATE_LOGIC | MEDIUM |
| No input validation | MISSING_VALIDATION | MEDIUM |
| No unit tests in payments | MISSING_TESTS | MEDIUM |
| Unused imports | UNUSED_IMPORT | LOW |
| No docstrings | MISSING_DOCSTRINGS | LOW |

---

## Expected score
```
CRITICAL findings: 5 × 20 = 100 penalty
HIGH findings:     5 × 10 = 50  penalty
MEDIUM findings:   3 × 5  = 15  penalty
LOW findings:      2 × 1  = 2   penalty
                           ─────
Total penalty:             167
health_score = max(0, 100 - 167) = 0
