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
        pass
    elif choice == 0:
        pass 
    else:
        print("ERROR: Wrong choice.")
