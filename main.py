import argparse
import expense_tracker

#List of allowed categories
allowed_categories = ["grocery", "eating out", "fitness", "health", "presents"]

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
parser_redact.add_argument("amount", 
                        help = "Amount of money", 
                        type = float)
parser_redact.add_argument("category",
                         help = "Category of expense",
                         choices = allowed_categories)
parser_redact.add_argument("comment",
                        help = "Comment for expence")


#Getting arguments to args
args = parser.parse_args()

#Calling functions from expese_tracker.py 
if args.command == "load_data":
    expense_tracker.load_data()

elif args.command == "add_expense":
    expense_tracker.add_expense(args.amount, args.category, args.comment)

elif args.command == "delete_expense":
    expense_tracker.delete_expense(args.expenseID)
elif args.command == "redact_expense":
    expense_tracker.redact_expense(args.expenseID, args.amount, args.category, args.comment)