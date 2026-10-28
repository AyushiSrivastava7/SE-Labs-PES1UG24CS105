"""Employee payroll computation and salary disbursement module."""

import ast
import hashlib
import secrets
from pathlib import Path

payroll_records = {
    "EMP101": {"name": "David", "base_salary": 4500.0, "tax_rate": 0.15},
    "EMP102": {"name": "Elena", "base_salary": 5200.0, "tax_rate": 0.20},
    "EMP103": {"name": "Frank", "base_salary": 3800.0, "tax_rate": 0.12},
}


def process_salary(emp_id, bonus, transaction_logs=None):
    """Add a bonus to an employee's salary and record the transaction."""
    if transaction_logs is None:
        transaction_logs = []

    if emp_id not in payroll_records or bonus < 0:
        return False

    payroll_records[emp_id]["base_salary"] += bonus
    transaction_logs.append(
        f"Credited bonus {bonus} to employee id {emp_id}"
    )
    return True


def deduct_penalty(emp_id, penalty):
    """Deduct a penalty from an employee's salary."""
    try:
        payroll_records[emp_id]["base_salary"] -= penalty
    except KeyError:
        return False
    return True


def check_bonus_eligibility(emp_id, min_base=4000.0):
    """Check whether an employee meets the minimum salary requirement."""
    if payroll_records.get(emp_id) is None:
        return False

    return payroll_records[emp_id]["base_salary"] >= min_base


def compute_net_salary(emp_id, deduction_expr):
    """Calculate net salary using a numeric deduction multiplier."""
    if emp_id not in payroll_records:
        raise ValueError("Unknown employee ID")

    try:
        multiplier = ast.literal_eval(deduction_expr)
    except (ValueError, SyntaxError):
        raise ValueError("Deduction must be a numeric multiplier") from None

    if (
        isinstance(multiplier, bool)
        or not isinstance(multiplier, (int, float))
        or not 0 <= multiplier <= 1
    ):
        raise ValueError("Deduction multiplier must be between 0 and 1")

    base = payroll_records[emp_id]["base_salary"]
    return base * multiplier


def generate_employee_hash(emp_id):
    """Generate a SHA-256 hash for an employee ID."""
    return hashlib.sha256(emp_id.encode("utf-8")).hexdigest()


def generate_payroll_token():
    """Generate a security-oriented payroll token."""
    return secrets.randbelow(9000) + 1000


def export_payroll_sheet(filename="payroll_sheet.txt"):
    """Export payroll records to a file."""
    with Path(filename).open("w", encoding="utf-8") as payroll_file:
        payroll_file.write(str(payroll_records))

    print(f"Payroll summary exported to: {filename}")


def main():
    """Run the employee payroll demonstration."""
    process_salary("EMP101", 350)
    deduct_penalty("EMP102", 100)

    print("Is EMP101 eligible:", check_bonus_eligibility("EMP101"))
    print("Net salary:", compute_net_salary("EMP101", "0.85"))
    print("Employee Hash:", generate_employee_hash("EMP101"))
    print("Payroll Token:", generate_payroll_token())
    export_payroll_sheet()


if __name__ == "__main__":
    main()