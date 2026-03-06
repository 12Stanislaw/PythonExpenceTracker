import argparse
import datetime
import expense_tracker
import utils

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker Pro")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Load
    subparsers.add_parser("list")

    # Add
    add_p = subparsers.add_parser("add")
    add_p.add_argument("amount", type=float)
    add_p.add_argument("category", choices=utils.ALLOWED_CATEGORIES)
    add_p.add_argument("comment")
    add_p.add_argument("--date", default=datetime.date.today().strftime("%Y-%m-%d"))

    # Delete
    del_p = subparsers.add_parser("delete")
    del_p.add_argument("id", type=int)

    # Edit
    edit_p = subparsers.add_parser("edit")
    edit_p.add_argument("id", type=int)
    edit_p.add_argument("field", choices=["amount", "category", "comment", "date"])
    edit_p.add_argument("value")

    args = parser.parse_args()

    try:
        if args.command == "list":
            expense_tracker.load_data()
        
        elif args.command == "add":
            if args.amount <= 0: raise ValueError("Amount must be positive")
            if utils.is_valid_date(args.date):
                expense_tracker.add_expense(args.amount, args.category, args.comment, args.date)

        elif args.command == "delete":
            expense_tracker.delete_expense(args.id)

        elif args.command == "edit":
            # Тут можна додати специфічну валідацію для value залежно від field
            expense_tracker.redact_expense(args.id, args.field, args.value)
            
    except Exception as e:
        print(f"Runtime Error: {e}")

if __name__ == "__main__":
    main()