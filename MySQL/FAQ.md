# FAQ

## How to Truncate table by disabling foreign key checks ?

```sql
-- Truncate table disabling foreign key checks
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE students;
SET FOREIGN_KEY_CHECKS = 1;
```