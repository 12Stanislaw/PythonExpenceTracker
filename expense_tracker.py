import csv
import gui


def load_data():
    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)

        data_list = []
        for row in reader:
            data_list.append(row)
        
        total = 0.0
        for row in data_list:
            for key, value in row.items():
                if key == "amount":
                    total += float(value)

        gui.write_loaded(tuple(data_list), total)
        



def add_expense(amount, category, comment):
    fieldnames = ["amount", "category", "comment"]

    with open('expenses.csv', mode='a', newline='',) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        new_row = {
            "amount" : amount,
            "category" : category,
            "comment" : comment
        }
        writer.writerow(new_row)

def delete_expense(expenseID):
    print(f"Deleted expense with ID={expenseID}")