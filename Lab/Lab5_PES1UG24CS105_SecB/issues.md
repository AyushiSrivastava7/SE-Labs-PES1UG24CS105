# Lab 5: Identified Issues and Fixes

## Student Information

- **Student Name:** Ayushi Srivastava
- **SRN:** PES1UG24CS105
- **Lab:** Lab 5 – Static Code Analysis

## Overview

Static analysis was performed on `employee_payroll_system.py` using Pylint, Bandit, and Flake8. The initial reports identified code quality problems, potential security risks, and coding style violations.

The following table summarizes the major issues identified and the approaches used to address them.

## Issue Table

| No. | Issue Type | Tool | Description | Fix Approach |
|---:|---|---|---|---|
| 1 | Unsafe evaluation | Bandit (B307) | The original program used `eval()`, which can execute arbitrary Python expressions. | Replaced `eval()` with `ast.literal_eval()` and validated the result to accept only numeric deduction values, excluding Boolean values. |
| 2 | Weak hashing algorithm | Bandit (B324) | MD5 was used to generate a hash and is unsuitable when stronger collision resistance is required. | Replaced MD5 with SHA-256 using the `hashlib` module. |
| 3 | Predictable random values | Bandit (B311) | `random.randint()` was used for token generation, which is not suitable for security-sensitive tokens. | Replaced it with `secrets.randbelow()` to generate a token using a security-oriented random source. |
| 4 | Shell command execution | Bandit (B605) | The program used `os.system()`, which can introduce command-injection risks. | Removed shell command execution from the updated implementation. |
| 5 | Broad exception handling | Bandit (B110) | A bare exception handler suppressed errors and made failures difficult to identify. | Replaced broad exception handling with specific exceptions where needed and removed unnecessary exception suppression. |
| 6 | Mutable default argument | Code quality | A list used as a default argument could be shared between function calls. | Changed the default argument to `None` and initialized the list inside the function. |
| 7 | Unused imports | Pylint and Flake8 | Unnecessary imports reduced code cleanliness. | Removed unused imports, including the unused `math` import. |
| 8 | Unused variables | Pylint and Flake8 | Variables such as `statutory_buffer` and `base` were assigned but not used. | Removed unused variables and simplified the affected logic. |
| 9 | Missing documentation | Pylint | Missing module or function docstrings reduced readability and documentation quality. | Added module and function docstrings. |
| 10 | File encoding and handling | Pylint | File operations did not explicitly specify an encoding. | Used `Path.open()` with `encoding="utf-8"` inside a context manager. |
| 11 | Incorrect comparison with `None` | Flake8 | The original code compared a value with `None` instead of using an identity comparison. | Used `is None` where appropriate. |
| 12 | Formatting violations | Flake8 | The original code contained a long line and a missing final newline. | Reformatted the code and ensured the file ended with a newline. |

## Before-and-After Results

| Tool | Initial Result | Final Result |
|---|---|---|
| Pylint | 5.32/10 | 10.00/10 |
| Bandit | 5 findings | No issues identified |
| Flake8 | 7 violations | 0 violations |

## Conclusion

The identified issues were addressed in the updated implementation. The final reports showed improved code quality, fewer reported security risks, and consistent formatting.

Using multiple static analysis tools provided a more comprehensive review because each tool focuses on a different aspect of software quality.