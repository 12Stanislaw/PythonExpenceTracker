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
    
def update_file_with_sorted_ids(sorted_data):
    # Оновлюємо ID прямо в посортованому списку
    for i, row in enumerate(sorted_data, start=1):
        row["ID"] = i

    # Записуємо цей посортований і пронумерований список у файл
    with open("expenses.csv", 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_data)

def load_data():
    # 1. Отримуємо дані
    data_list = get_data() 
    if not data_list:
        gui.write_loaded([], 0)
        return

    # 2. Сортуємо список (від нових до старих)
    # Тепер весь список у пам'яті вже в правильному порядку
    sorted_data = sorted(data_list, key=lambda x: x['date'], reverse=True)

    # 3. Перезаписуємо файл із НОВИМИ ID на основі сортування
    # Ми передаємо вже посортований список у функцію запису
    update_file_with_sorted_ids(sorted_data)

    # 4. Рахуємо суму
    total = sum(float(row["amount"]) for row in sorted_data if row.get("amount"))

    # 5. Виводимо актуальні (вже пронумеровані) дані
    gui.write_loaded(tuple(sorted_data), total)

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

