import random 

results = [0, 0, 0, 0, 0, 0, 0]

for i in range(1000):
    value = random.randint(1, 6)
    results[value] = results[value] + 1 

print(results)