import random 

data = [] 

for i in range(10):
    value = random.randint(1, 1000)
    data.append(value)

print(data)

print(sum(data))