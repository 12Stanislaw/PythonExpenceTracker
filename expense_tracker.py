import csv
import gui


fieldnames = ["ID", "amount", "category", "comment"]

def get_data():
    try:
        with open('expenses.csv', mode='r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:       #If file doesn't exist create a new one
        with open('expenses.csv', mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        return []

def set_id():

    data = get_data()
    for i in range(len(data)):
        data[i]["ID"] = i+1

    with open("expenses.csv", 'w', encoding='utf-8', newline='') as f:
        # Використовуємо DictWriter, щоб він розумів структуру словників
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()   # Записуємо заголовки (ID, Amount, Category тощо)
        writer.writerows(data) # Записуємо всі змінені рядки
    
    
def load_data():
    set_id() # Оновлюємо ID перед завантаженням
    data_list = get_data() # Отримуємо актуальний список
    
    total = 0.0
    for row in data_list:
        if row.get("amount"):
            try:
                total += float(row["amount"])
            except ValueError:      #If amount is not float at some point
                continue

    gui.write_loaded(tuple(data_list), total)

def add_expense(amount, category, comment):

    accepted = gui.accept_adding(amount, category, comment)

    if accepted:
        data = get_data()
        last_id = 0;
        
        if data:
            last_id = int(data[-1]["ID"])
        new_id = last_id + 1

        with open('expenses.csv', mode='a',  encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            new_row = {
                "ID" : new_id,
                "amount" : amount,
                "category" : category,
                "comment" : comment
            }
            writer.writerow(new_row)
    else:
        return
    

def delete_expense(expenseID):
    line = expenseID -1
    rows = get_data()

    if 0 <= line < len(rows):
        accepted = gui.accept_deleting(rows, line)
            
    if accepted:
        del rows[line]

    # 3. Записуємо оновлені дані назад
    with open("expenses.csv", 'w',encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()  # Write the top row (Date, Category, etc.)
        writer.writerows(rows)
        
    set_id()
