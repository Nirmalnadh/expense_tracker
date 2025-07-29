import uuid
from datetime import datetime
from collections import defaultdict

def generate_id():
    return str(uuid.uuid4())[:8]  # 8-char unique ID

def get_today_date():
    return datetime.now().strftime("%Y-%m-%d")

def format_expense_list(expenses):
    if not expenses:
        return "No expenses found."

    lines = []
    for exp in expenses:
        lines.append(f"[{exp.id}] ₹{exp.amount} - {exp.category} on {exp.date}")
    return "\n".join(lines)

def format_summary(expenses):
    if not expenses:
        return "No expenses recorded."

    total = sum(exp.amount for exp in expenses)
    summary = defaultdict(float)
    for exp in expenses:
        summary[exp.category] += exp.amount

    lines = [f"Total Expenses: ₹{total:.2f}", "\nBy Category:"]
    for cat, amt in summary.items():
        lines.append(f"- {cat}: ₹{amt:.2f}")

    return "\n".join(lines)
