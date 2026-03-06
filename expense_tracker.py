import csv
import gui
from utils import FIELDS, DB_FILE


def _read_all() -> list:
    if not DB_FILE:
        return []
    with open(DB_FILE, mode='r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def _write_all(data: list):
    with open(DB_FILE, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(data)

    
def update_file_with_sorted_ids(sorted_data):
    # Оновлюємо ID прямо в посортованому списку
    for i, row in enumerate(sorted_data, start=1):
        row["ID"] = i

    # Записуємо цей посортований і пронумерований список у файл
    with open("expenses.csv", 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(sorted_data)

def load_data():
    data = sorted(_read_all(), key=lambda x: x['date'], reverse=True)
    total = sum(float(row["amount"]) for row in data)
    gui.display_expenses(data, total)

def add_expense(amount, category, comment, date):
    if not gui.confirm_action("add", {"amount": amount, "category": category, "comment": comment, "date": date}):
        return

    data = _read_all()
    new_id = max([int(i['ID']) for i in data], default=0) + 1
    
    new_entry = {
        "ID": new_id, "amount": amount, "category": category, 
        "comment": comment, "date": date
    }
    
    # Дописуємо в кінець (Append) - це безпечніше, ніж переписувати все
    with open(DB_FILE, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if f.tell() == 0: writer.writeheader()
        writer.writerow(new_entry)
    print("Successfully added!")

def delete_expense(expense_id):
    data = _read_all()
    # Шукаємо запис по реальному ID, а не по індексу в списку
    entry = next((item for item in data if int(item['ID']) == expense_id), None)
    
    if entry and gui.confirm_action("delete", entry):
        new_data = [item for item in data if int(item['ID']) != expense_id]
        _write_all(new_data)
        print("Deleted.")

def redact_expense(expense_id, field, new_value):
    data = _read_all()
    for row in data:
        if int(row['ID']) == expense_id:
            if gui.confirm_action("edit", {field: new_value}):
                row[field] = new_value
                _write_all(data)
                print("Updated.")
            return
    print("Expense not found.")