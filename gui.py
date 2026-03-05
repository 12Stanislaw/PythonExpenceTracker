
def write_loaded(data, total):
    if not data:
        print("Empty list")
        return

    headers = list(data[0].keys())
    
    # Виводимо шапку
    header_line = " | ".join(headers)
    print(header_line)
    print("-" * len(header_line))

    # 2. Виводимо рядки з форматуванням ціни
    for row in data:
        formatted_row = []
        for key, value in row.items():
            # Якщо це колонка з ціною — додаємо знак $
            if key == "amount":
                formatted_row.append(f"{value}$")
            else:
                formatted_row.append(str(value))

        print(" | ".join(formatted_row))
    
    print("-" * len(header_line))
    print(f"Total expenses: {total}$")


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
