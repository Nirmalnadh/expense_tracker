# --- storage.py ---
import csv
from expense import Expense

CSV_FILE = 'expenses.csv'

def save_expense(expense):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'amount', 'category', 'date'])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(expense.to_dict())

def load_expenses():
    expenses = []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(Expense.from_dict(row))
    except FileNotFoundError:
        pass
    return expenses

def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [e for e in expenses if e.id != expense_id]
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'amount', 'category', 'date'])
        writer.writeheader()
        for e in expenses:
            writer.writerow(e.to_dict())
