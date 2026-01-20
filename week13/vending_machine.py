# A vending machine has 3 products A, B, C with price 7.2, 1.8, 12.5 respectively
# User selects product and inputs an amount
# Machine gives change

products = {
    'A': 7.2, 'B': 1.8, 'C': 12.5
}

input_values = [1, 2, 5, 10, 20, 50]
change_values = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1] 

product = input('Select product: ')
if product in products:
    amount = int(input("Give amount: "))
    if amount in input_values:
        change = amount - products[product]
        if change < 0:
            print("Insuficient amount")
        else:
            print("Calculating change")
            for v in change_values:
                if v <= change:
                    print(v, end=' ')
                    change -= v
                if change == 0:
                    break
            print()
    else: 
        print("Invalid amount")
else: 
    print("Product not available")