"""Employee payroll processing with safer input and file handling."""

import ast
import hashlib
import secrets
from pathlib import Path

payroll_records = {
    "E001": {"base_salary": 50000},
    "E002": {"base_salary": 60000},
}


def process_salary(emp_id, bonus, transaction_logs=None):
    """Credit a valid bonus to an employee's salary."""
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
    """Deduct a non-negative penalty from an employee's salary."""
    if emp_id not in payroll_records or penalty < 0:
        return False

    payroll_records[emp_id]["base_salary"] -= penalty
    return True


def calculate_net_salary(emp_id, deduction_expr):
    """Calculate net salary using a safely parsed numeric deduction."""
    if emp_id not in payroll_records:
        return None

    try:
        deduction = ast.literal_eval(deduction_expr)
    except (ValueError, SyntaxError):
        return None

    if not isinstance(deduction, (int, float)) or isinstance(
        deduction, bool
    ):
        return None

    base_salary = payroll_records[emp_id]["base_salary"]
    if deduction < 0 or deduction > base_salary:
        return None

    return base_salary - deduction


def generate_employee_hash(emp_id):
    """Generate a SHA-256 digest for an employee identifier."""
    return hashlib.sha256(emp_id.encode("utf-8")).hexdigest()


def generate_payroll_token():
    """Generate a security-oriented four-digit payroll token."""
    return secrets.randbelow(9000) + 1000


def export_payroll_summary(filename):
    """Export payroll records to a text file."""
    output_path = Path(filename)
    with output_path.open("w", encoding="utf-8") as payroll_file:
        for emp_id, record in payroll_records.items():
            payroll_file.write(
                f"{emp_id}: {record['base_salary']}\n"
            )

    print(f"Payroll summary exported to: {output_path}")


def main():
    """Run a small payroll processing demonstration."""
    process_salary("E001", 1000)
    deduct_penalty("E002", 500)
    print("Payroll summary:")
    for emp_id, record in payroll_records.items():
        print(f"{emp_id}: {record['base_salary']}")


if __name__ == "__main__":
    main()
