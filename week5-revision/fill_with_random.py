# Create a list
# fill the list with N random values
# where N is also random (10, 50)

import random 

data = []
n = random.randint(10, 50) 

for _ in range(n):
    data.append(random.randint(1, 100))

print(data)

# If I wanted unique values
data = []

for _ in range(n):
    while True:
        value = random.randint(1, 100)
        if value not in data:
            data.append(value)
            break
        else:
            print(f'Duplicate {value}')
print(data)