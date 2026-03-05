import argparse
import expense_tracker

#List of allowed categories
allowed_categories = ["grocery", "eating out", "fitness", "health", "presents"]
characteristics = ["amount", "category", "comment"]
#---CREATING MAIN PARSER---
parser = argparse.ArgumentParser("Expence tracker")

#---CREATING SUB PARSERS---
subparsers = parser.add_subparsers(dest="command", help= "Commads")

#---LOAD_DATA---
subparsers.add_parser("load_data", help = "Show all expenses")

#---ADD EXPENSE---
parser_add = subparsers.add_parser("add_expense")
parser_add.add_argument("amount", 
                        help = "Amount of money", 
                        type = float)
parser_add.add_argument("category",
                         help = "Category of expense",
                         choices = allowed_categories)
parser_add.add_argument("comment",
                        help = "Comment for expence")

#---DELETE EXPENSE---
parser_delete = subparsers.add_parser("delete_expense")
parser_delete.add_argument("expenseID",
                            help = "ID of expense", 
                            type = int)

#---REDACT EXPENSE---
parser_redact = subparsers.add_parser("redact_expense")
parser_redact.add_argument("expenseID",
                            help = "ID of expense", 
                            type = int)
parser_redact.add_argument("cvalue",
                           help = "What do you want to change?",
                           choices=characteristics)
parser_redact.add_argument("new_value",
                           help = "Type your change",
                           )


#Getting arguments to args
args = parser.parse_args()

#Calling functions from expese_tracker.py 
if args.command == "load_data":
    expense_tracker.load_data()

elif args.command == "add_expense":

    if args.amount < 0:
        print("Error: Amount cannot be negative.")
    else:
        expense_tracker.add_expense(args.amount, args.category, args.comment)

elif args.command == "delete_expense":
    expense_tracker.delete_expense(args.expenseID)

elif args.command == "redact_expense":
    valid = True
    final_value = args.new_value

    # 1. Якщо змінюємо amount — перевіряємо, чи це додатнє число
    if args.cvalue == "amount":
        try:
            final_value = float(args.new_value)
            if final_value < 0:  
                print("Error: New amount cannot be negative.")
                valid = False
        except ValueError:
            print("Error: 'amount' must be a number.")
            valid = False

    # 2. Якщо змінюємо category — перевіряємо, чи вона є в списку дозволених
    elif args.cvalue == "category":
        if args.new_value not in allowed_categories:
            print(f"Error: Invalid category. Choose from: {', '.join(allowed_categories)}")
            valid = False

    # Якщо все ок — викликаємо функцію
    if valid:
        expense_tracker.redact_expense(args.expenseID, args.cvalue, final_value)