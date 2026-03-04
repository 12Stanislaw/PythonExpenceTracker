import csv
import gui

def set_id():
    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        data = list(reader)
 
    for i in range(len(data)):
        data[i]["ID"] = i+1

    with open("expenses.csv", 'w', encoding='utf-8', newline='') as f:
        # Використовуємо DictWriter, щоб він розумів структуру словників
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()   # Записуємо заголовки (ID, Amount, Category тощо)
        writer.writerows(data) # Записуємо всі змінені рядки
    
    

def load_data():
    
    set_id()

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
    line = expenseID
    # 1. Читаємо всі дані
    with open("expenses.csv", 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    

        # 2. Видаляємо рядок
        if 0 <= line < len(rows):
            accepted = gui.accept_deleting(rows, line)
            
        if accepted:
            del rows[line]

        # 3. Записуємо оновлені дані назад
        with open("expenses.csv", 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()  # Write the top row (Date, Category, etc.)
            writer.writerows(rows)
        
        set_id()
