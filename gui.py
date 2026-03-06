
def write_loaded(data, total):
    if not data:
        print("Empty list")
        return

    # 1. Визначаємо заголовки та ширину колонок (наприклад, 15 символів на кожну)
    # Порада: можна зробити ширину динамічною, але 15-20 зазвичай достатньо
    col_width = 18
    headers = list(data[0].keys())
    
    # Створюємо рядок форматування, наприклад: "{:<18} | {:<18} | ..."
    format_row = " | ".join(["{:<" + str(col_width) + "}"] * len(headers))

    # 2. Виводимо шапку
    header_line = format_row.format(*[h.upper() for h in headers])
    print("\n" + header_line)
    print("-" * len(header_line))

    # 3. Виводимо дані
    for row in data:
        formatted_values = []
        for key in headers:
            value = row[key]
            if key == "amount":
                formatted_values.append(f"{value}$")
            else:
                formatted_values.append(str(value))
        
        print(format_row.format(*formatted_values))
    
    # 4. Підсумок
    print("-" * len(header_line))
    print(f"TOTAL EXPENSES: {total}$".rjust(len(header_line)))

def accept_deleting(rows, expenceID):
    row= rows[expenceID]
    
    print("Expence to delete:")
    print("-" * 20)
    print(f"ID       : {row['ID']}") 
    print(f"Amount   : {row['amount']}")
    print(f"Category : {row['category']}")
    print(f"Comment  : {row['comment']}")

    res = input("You sure [y/n]? ")

    if res.lower() == 'y':
        return True
    elif res.lower() == 'n':
        return False
    else:
        print("Wrong option")
        return False
    
def accept_adding(amount, category, comment, date):
    
    print("Expence to add:")
    print("-" * 20) 
    print(f"Amount   : {amount}")
    print(f"Category : {category}")
    print(f"Comment  : {comment}")
    print(f"Date     : {date}")

    res = input("You sure [y/n]? ")

    if res.lower() == 'y':
        return True
    elif res.lower() == 'n':
        return False
    else:
        print("Wrong option")
        return False


def accept_redacting(row, cvalue, new_value):
    
    print("Your change: ")
    print("-" * 20)
    
    print(f"{cvalue}   : {row[cvalue]} | {new_value}")
    
    res = input("Is that right [y/n]? ")
    if res.lower() == 'y':
        return True
    elif res.lower() == 'n':
        return False
    else:
        print("Wrong option")
        return False
