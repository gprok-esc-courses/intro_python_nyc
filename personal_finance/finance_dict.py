import csv
from datetime import datetime

def load_data():
    file = open('finance.csv')
    data = {}
    rows = csv.DictReader(file)
    for row in rows:
        id = int(row['id'])
        data[id] = row
    return data

def menu():
    print("========== MENU ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expenses by category")
    print("4. Delete expense")
    print("0. Exit")
    choice = int(input("Choose: "))
    return choice

def view_expenses(data):
    for key in data:
        row = data[key]
        print(f"{row['date']}: cat: {row['category']}, amount: {row['amount']}")


def add_expense(next_id):
    d = datetime.today().strftime('%Y-%m-%d')
    category = input('Category: ')
    amount = input('Amount: ')
    expense = {'id': str(next_id), 'date': d, 
               'category': category, 'amount': amount}
    return expense

def save_data(data):
    file = open('finance.csv', 'w')
    file.write('id,date,category,amount\n')
    for key in data:
        row = data[key]
        file.write(f"{row['id']},{row['date']},{row['category']},{row['amount']}\n")
    file.close()
    print("Data saved into the file")

def by_category(data):
    categories = {}
    for key in data:
        row = data[key]
        if row['category'] in categories:
            categories[row['category']] += float(row['amount'])
        else:
            categories[row['category']] = float(row['amount'])
    for cat in categories:
        total = round(categories[cat], 1)
        print(f"{cat}: {total}")

def get_expense_position(data):
    id = int(input("Give expense ID to be deleted: "))
    if id in data:
        return id
    return None

data = load_data()
keys = list(data.keys())
next_id = max(keys) + 1

choice = -1

while choice != 0:
    choice = menu()
    if choice == 1:
        expense = add_expense(next_id)
        id = int(expense['id'])
        data[id] = expense
        next_id += 1
    elif choice == 2:
        view_expenses(data)
    elif choice == 3:
        by_category(data)
    elif choice == 4:
        index = get_expense_position(data)
        if index is not None:
            data.pop(index)
        else:
            print("Id not found")
    elif choice == 0:
        save_data(data)
        print("Bye!") 
    else:
        print("ERROR: Wrong choice.")