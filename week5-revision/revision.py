import random

# simple list
simple_list = [3, True, 8.90, "Test", [1, 2, 3]]

print(simple_list[4][1])  # 2

list2d = [
    [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
]

print(len(list2d)) # 3
print(len(list2d[1])) # 4

print(list2d[2][3]) # 12

# Initialize a list 
data1 = []
for i in range(100):
    data1.append(0)
print(data1)
# Same thing
data1 = [0] * 100
print(data1)
# Initialize a list with random values
data1 = []
for i in range(100):
    data1.append(random.randint(1, 100))
print(data1)
# Same thing
data1 = [random.randint(1, 100) for i in range(100)] 
print(data1)

# Initialize a 2D list