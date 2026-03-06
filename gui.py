
def display_expenses(data, total):
    if not data:
        print("\n--- No expenses found ---")
        return

    col_w = 15
    header = " | ".join([f"{h.upper():<{col_w}}" for h in data[0].keys()])
    print(f"\n{header}\n{'-'*len(header)}")

    for row in data:
        line = " | ".join([f"{str(v):<{col_w}}" for v in row.values()])
        print(line)
    
    print(f"{'-'*len(header)}\nTOTAL: {total}$".rjust(len(header)))

def confirm_action(action_type, details) -> bool:
    print(f"\nConfirm {action_type}:")
    for k, v in details.items():
        print(f"  {k}: {v}")
    return input("Proceed? (y/n): ").lower() == 'y'