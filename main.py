import argparse
import expense_tracker

#List of allowed categories
allowed_categories = ["grocery", "eating out", "fitness", "health"]

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

#---DELETE EXPENSE---
parser_delete = subparsers.add_parser("delete_expense")
parser_delete.add_argument("expenseID",
                            help = "ID of expense", 
                            type = int)

#Getting arguments to args
args = parser.parse_args()

#Calling functions from expese_tracker.py 
if args.command == "load_data":
    expense_tracker.load_data()

elif args.command == "add_expense":
    expense_tracker.add_expense(args.amount, args.category)

elif args.command == "delete_expense":
    expense_tracker.delete_expense(args.expenseID)
