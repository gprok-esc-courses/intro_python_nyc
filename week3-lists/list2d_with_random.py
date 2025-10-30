import random 

data = []

for r in range(3):
    row = []
    for c in range(3):
        value = random.randint(10, 99)
        row.append(value)
    data.append(row)

print(data)

# Another way to initialize a 2D list

data2 = [
    [random.randint(10, 99) for i in range(3)]
    for j in range(3)
]
print(data2)
