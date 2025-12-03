# Manage coffee shop orders
# Users can add orders and view statistics (number of orders, total profit)
# Data will be stored in a text file, as comma separated values (customer, product, price)

import os 

filename = "orders.csv"

def create_file(filename):
    if not os.path.isfile(filename):
        file = open(filename, "w")
        file.close()

def load_orders_from_file(filename):
    data = []
    file = open(filename)
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        order = line.split(',')
        order[2] = float(order[2])
        data.append(order)
    return data 

def get_menu_choice():
    print()
    print("=== COFFEE SHOP MENU ===")
    print("1. Add order")
    print("2. Statistics")
    print("0. EXIT")
    choice = int(input("Choose: "))
    return choice

def add_order(orders, filename):
    print("= ADD ORDER =")
    customer = input("Customer: ")
    product = input("Product: ")
    price = float(input("Price: "))
    order = [customer, product, price]
    orders.append(order)
    file = open(filename, "a")
    line = f"{customer},{product},{price}\n"
    file.write(line)
    file.close()

def statistics(orders):
    print("= STATISTICS =")
    print(f"Total orders: {len(orders)}")
    total = 0
    for order in orders:
        total += order[2]
    print(f"Total profit: {total}")


orders = []

create_file(filename)
orders = load_orders_from_file(filename)

choice = 1
while choice != 0:
    choice = get_menu_choice()
    if choice == 1:
        add_order(orders, filename) 
    elif choice == 2:
        statistics(orders)
    elif choice == 0:
        print("Bye!")
    else:
        print(f"Wrong choice {choice}")