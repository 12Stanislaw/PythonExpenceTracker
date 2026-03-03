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
    fieldnames = ["ID","amount", "category", "comment"]


    last_id = 0;
    with open('expenses.csv', mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))
        if reader:
            last_id = int(reader[-1]["ID"])
    new_id = last_id + 1

    with open('expenses.csv', mode='a', newline='',) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        new_row = {
            "ID" : new_id,
            "amount" : amount,
            "category" : category,
            "comment" : comment
        }
        writer.writerow(new_row)

def delete_expense(expenseID):
    line_to_delete = expenseID  # Індекс рядка (починаючи з 0)

    # 1. Читаємо всі дані
    with open("expenses.csv", 'r') as f:
        rows = list(csv.reader(f))

    # 2. Видаляємо рядок
    if 0 <= line_to_delete < len(rows):
        del rows[line_to_delete]

    # 3. Записуємо оновлені дані назад
    with open("expenses.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
