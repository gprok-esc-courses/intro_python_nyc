
def menu():
    print("=== MENU PRODUCTS ===")
    print("1. Add product")
    print("2. Change price")
    print("3. Delete product")
    print("4. Display products")
    print("0. Exit")
    ch = int(input("Choose: "))
    return ch

def load_next_id():
    file = open('next.txt')
    line = file.readline()
    n = int(line.strip())
    file.close()
    return n

def load_products():
    p = {}
    file = open('products.csv')
    lines = file.readlines()
    for line in lines[1:]:
        line = line.strip().split(',')
        p[line[0]] = line
    file.close()
    return p

def display_products(plist):
    for id in plist:
        product = plist[id]
        print(f"{product[0]}. {product[1]}, price: {product[2]}")

def add_product():
    name = input("Name: ")
    price = input("Price: ")
    return name, price

def save_data(plist, n):
    file = open('next.txt', 'w')
    file.write(str(n))
    file.close 
    file = open('products.csv', 'w')
    file.write('id,name,price\n')
    for id in plist:
        product = plist[id]
        s = f"{product[0]},{product[1]},{product[2]}\n"
        file.write(s)
    file.close()

next = load_next_id()
products = load_products()
choice = -1
while choice != 0:
    choice = menu()
    if choice == 1:
        name, price = add_product()
        products[next] = [next, name, price]
        next = next + 1 
    elif choice == 2:
        id = input("Product ID: ")
        price = input("New Price: ")
        if id in products:
            products[id][2] = price
    elif choice == 3:
        id = input("Product ID: ")
        if id in products:
            products.pop(id) 
    elif choice == 4:
        display_products(products)
    elif choice == 0:
        save_data(products, next)
