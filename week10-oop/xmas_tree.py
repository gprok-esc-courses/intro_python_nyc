import random

n = int(input("Give tree base size: ")) 

spaces = n // 2
rows = spaces + 1
asterisks = 1 

for i in range(rows):
    print(' ' * spaces, end='')
    # print('*' * asterisks)
    for j in range(asterisks):
        r = random.randint(1,100)
        if r < 15:
            print('0', end='')
        else:
            print('*', end='')
    print()
    spaces -= 1
    asterisks += 2

