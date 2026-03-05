import csv
import gui



fieldnames = ["ID", "amount", "category", "comment", "date"]

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

def add_expense(amount, category, comment, date):
    new_expense = {
        "amount": amount,
        "category": category,
        "comment": comment,
        "date": date
    }

    # Викликаємо акцептацію перед записом
    if gui.accept_adding(amount, category, comment, date):
        try:
            with open("expenses.csv", "a", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                if f.tell() == 0:
                    writer.writeheader()
                    
                writer.writerow(new_expense)
                
            print(f"Successfully added!")
        except Exception as e:
            print(f"An error occurred while saving: {e}")
    else:
        print("Addition cancelled by user.")

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


def redact_expense(expenseID, cvalue, new_value):
    data = get_data()
    
    index = expenseID - 1
    row = data[index]

    accepted = gui.accept_redacting(row, cvalue, new_value)
    
    if accepted: 
        if 0 <= index < len(data):
            if cvalue == "amount":
                row[cvalue] = float(new_value)
            else:
                row[cvalue] = new_value
            data[index] = row

        with open("expenses.csv", 'w',encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()  # Write the top row (Date, Category, etc.)
            writer.writerows(data)

