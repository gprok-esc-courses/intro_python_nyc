
answer = 'y'
total = 0.0 

while answer != 'n':
    price = float(input("Price? ")) 
    total = total + price 
    print(f'Total so far: {total}')
    answer = input("More items? (y/n) ")

print(f'Pay {total}')
