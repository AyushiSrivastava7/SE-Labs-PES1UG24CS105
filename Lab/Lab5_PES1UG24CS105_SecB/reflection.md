# Lab 5: Reflection on Static Code Analysis

## Student Information

- **Student Name:** Ayushi Srivastava
- **SRN:** PES1UG24CS105
- **Lab:** Lab 5 – Static Code Analysis

## 1. What is the importance of static code analysis?

Static code analysis helps identify programming errors, security vulnerabilities, and coding standard violations without executing a program. It allows developers to find problems early, making them easier to understand and fix.

In this lab, Pylint helped improve code quality, Bandit identified potentially unsafe coding patterns, and Flake8 highlighted formatting and style violations.

## 2. What issues did you identify in the original program?

The original program contained several issues, including unsafe use of `eval()`, MD5 hashing, predictable random number generation, shell command execution, broad exception handling, unused imports and variables, and formatting violations.

These findings demonstrated that code can appear to work while still containing security risks and maintainability problems.

## 3. Which issue was the most important to fix, and why?

The unsafe use of `eval()` was one of the most important issues because it can execute arbitrary Python expressions. If untrusted input reaches this function, it may allow unintended code execution.

I replaced `eval()` with `ast.literal_eval()` and added validation to ensure that the deduction was a numeric value rather than a Boolean. I also checked that the deduction was non-negative and did not exceed the employee's salary.

Other security-related improvements included replacing MD5 with SHA-256, using the `secrets` module for token generation, and removing unsafe shell command execution.

## 4. How did the static analysis results change after fixing the issues?

The results improved significantly after the code was updated.

- **Pylint:** The score increased from 5.32/10 to 10.00/10.
- **Bandit:** The initial five findings were reduced to zero.
- **Flake8:** The initial seven violations were reduced to zero.

These results indicate that the updated implementation addressed the issues reported by the three tools.

## 5. What challenges did you face while fixing the issues?

One challenge was understanding the findings from the different tools because they focused on different aspects of the code. Some findings were related to security, while others involved code quality and formatting.

Another challenge was verifying that the changes did not introduce additional problems. I addressed this by rerunning all three tools after updating the program and checking their final reports.

## 6. Can static analysis tools replace manual code review and testing?

No. Static analysis tools are useful, but they cannot detect every possible bug or security vulnerability. They may also report findings that require further investigation.

Manual code review and testing are still necessary to verify program behavior, validate requirements, and identify logical errors that automated tools might miss. Static analysis should complement these practices rather than replace them.

## 7. What did you learn from this lab?

I learned that static analysis is an important part of software development because it helps identify potential problems before code is deployed.

I also learned that different tools serve different purposes: Pylint focuses on code quality, Bandit focuses on common security issues, and Flake8 checks style and formatting.

Most importantly, I learned that fixing issues is only part of the process. Rerunning the tools and reviewing their final reports is necessary to verify that the changes improved the code.

## Conclusion

This lab improved my understanding of code quality, secure programming practices, and maintainable Python development. The improved Pylint score and the reduction in Bandit findings and Flake8 violations demonstrated the benefits of static code analysis.