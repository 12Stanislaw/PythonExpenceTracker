import datetime

ALLOWED_CATEGORIES = ["grocery", "eating out", "fitness", "health", "presents"]
FIELDS = ["ID", "amount", "category", "comment", "date"]
DB_FILE = "expenses.csv"

def is_valid_date(date_str):
    """Перевіряє формат дати (YYYY-MM-DD) та чи не з майбутнього вона."""
    try:
        input_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.date.today()
        
        if input_date > today:
            print(f"Error: Date {date_str} is in the future! Today is {today}.")
            return False
        return True
    except ValueError:
        print(f"Error: '{date_str}' is not a valid date. Use YYYY-MM-DD format (e.g., 2024-05-20).")
        return False