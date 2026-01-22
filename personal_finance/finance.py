import csv 
from datetime import datetime 

def load_data():
    file = open('finance.csv')
    data = []
    rows = csv.reader(file)
    for row in rows:
        if row[0] != 'id':
            data.append(row)
    return data

def menu():
    print("========== MENU ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expenses by category")
    print("0. Exit")
    choice = int(input("Choose: "))
    return choice

def view_expenses(data):
    for row in data:
        print(f"{row[1]}: cat: {row[2]}, amount: {row[3]}")

def add_expense(next_id):
    d = datetime.today().strftime('%Y-%m-%d')
    category = input('Category: ')
    amount = input('Amount: ')
    expense = [str(next_id), d, category, amount]
    return expense

def by_category(data):
    categories = {}
    for row in data:
        if row[2] in categories:
            categories[row[2]] += float(row[3])
        else:
            categories[row[2]] = float(row[3])
    for cat in categories:
        total = round(categories[cat], 1)
        print(f"{cat}: {total}")

def save_data(data):
    file = open('finance.csv', 'w')
    file.write('id,date,category,amount\n')
    for row in data:
        file.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")
    file.close()
    print("Data saved into the file")

data = load_data()
next_id = int(data[-1][0]) + 1
choice = -1

while choice != 0:
    choice = menu()
    if choice == 1:
        expense = add_expense(next_id)
        data.append(expense)
        next_id += 1
    elif choice == 2:
        view_expenses(data) 
    elif choice == 3:
        by_category(data)
    elif choice == 0:
        save_data(data)
        print("Bye!") 
    else:
        print("ERROR: Wrong choice.")
