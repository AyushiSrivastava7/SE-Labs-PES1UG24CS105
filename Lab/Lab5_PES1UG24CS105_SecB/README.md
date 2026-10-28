# Lab 5: Static Code Analysis

## Student Information

- **Student Name:** Ayushi Srivastava
- **SRN:** PES1UG24CS105
- **Course:** Software Engineering
- **Lab:** Lab 5 – Static Code Analysis
- **Assigned Repository:** [Employee Payroll System](https://github.com/SETAPESU26/L5_44_employee_payroll_system)

## 1. Objective

The objective of this lab was to improve the quality, security, readability, and maintainability of a Python program using static code analysis tools.

Pylint, Bandit, and Flake8 were used to identify potential programming errors, security vulnerabilities, and coding style violations. The issues were then addressed, and the tools were run again to verify the improvements.

## 2. Tools Used

- **Pylint:** Checks code quality, programming practices, unused variables, and documentation.
- **Bandit:** Identifies common security vulnerabilities and unsafe Python coding patterns.
- **Flake8:** Checks Python style, formatting, unused imports, and PEP 8 compliance.

## 3. Environment Setup

A Python virtual environment was created and activated before installing the required tools.

```bash
python3 -m venv venv
source venv/bin/activate
pip install pylint bandit flake8
```

## 4. Static Analysis Commands

The following commands were used to generate the initial reports:

```bash
pylint employee_payroll_system.py > pylint_report_before.txt 2>&1
bandit -r employee_payroll_system.py > bandit_report_before.txt 2>&1
flake8 employee_payroll_system.py > flake8_report_before.txt 2>&1
```

After the code was updated, the tools were run again:

```bash
pylint employee_payroll_system.py > pylint_report_after.txt 2>&1
bandit -r employee_payroll_system.py > bandit_report_after.txt 2>&1
flake8 employee_payroll_system.py > flake8_report_after.txt 2>&1
```

## 5. Issues Addressed

The main improvements included:

1. Replaced unsafe `eval()` usage with `ast.literal_eval()` and validated the resulting value.
2. Replaced MD5 hashing with SHA-256.
3. Replaced predictable random number generation with the `secrets` module for token generation.
4. Removed unsafe shell command execution through `os.system()`.
5. Improved exception handling and removed bare exception blocks.
6. Replaced a mutable default argument with `None` and initialized the list inside the function.
7. Removed unused imports and variables.
8. Added module and function docstrings.
9. Specified UTF-8 encoding for file operations.
10. Corrected formatting and comparison issues reported by Flake8.

## 6. Before-and-After Results

| Tool | Before | After |
|---|---|---|
| Pylint | 5.32/10 | 10.00/10 |
| Bandit | 5 findings | 0 findings |
| Flake8 | 7 violations | 0 violations |

### Pylint

The initial Pylint score was 5.32/10. The report identified issues involving documentation, unused variables, and code quality.

After the fixes, the score increased to 10.00/10.

### Bandit

The initial report contained five findings involving exception handling, unsafe evaluation, MD5 hashing, predictable random number generation, and shell command execution.

After the fixes, Bandit reported no issues.

### Flake8

The initial report contained seven violations involving unused imports, line length, exception handling, unused variables, comparisons with `None`, and a missing final newline.

After the fixes, Flake8 reported no violations.

## 7. Files Included

- `employee_payroll_system.py` — Updated Python program.
- `pylint_report_before.txt` — Initial Pylint report.
- `pylint_report_after.txt` — Final Pylint report.
- `bandit_report_before.txt` — Initial Bandit report.
- `bandit_report_after.txt` — Final Bandit report.
- `flake8_report_before.txt` — Initial Flake8 report.
- `flake8_report_after.txt` — Final Flake8 report.
- `issues.md` — Identified issues and their fixes.
- `reflection.md` — Reflection on static code analysis.

## 8. Conclusion

This lab demonstrated how static code analysis can identify potential bugs, security vulnerabilities, and coding style problems before a program is deployed.

The final results showed a Pylint score of 10.00/10, no Bandit findings, and no Flake8 violations. These improvements demonstrate the importance of static analysis in developing secure, readable, and maintainable Python programs.