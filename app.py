import argparse
from expense import Expense
from storage import save_expense, load_expenses
from utils import generate_id, get_today_date, format_expense_list, format_summary

def main():
    parser = argparse.ArgumentParser(description="💸 Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add Expense Command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount spent")
    add_parser.add_argument("--category", type=str, required=True, help="Expense category")

    # List Expenses
    list_parser = subparsers.add_parser("list", help="List all expenses")

    # Summary
    summary_parser = subparsers.add_parser("summary", help="View expense summary")

    args = parser.parse_args()

    if args.command == "add":
        expense = Expense(
            id=generate_id(),
            amount=args.amount,
            category=args.category,
            date=get_today_date()
        )
        save_expense(expense)
        print("✅ Expense added successfully!")

    elif args.command == "list":
        expenses = load_expenses()
        print("\n--- All Expenses ---")
        print(format_expense_list(expenses))

    elif args.command == "summary":
        expenses = load_expenses()
        print("\n--- Expense Summary ---")
        print(format_summary(expenses))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
