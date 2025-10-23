
n = int(input("Give a number: "))
a = 1 

for i in range(n):
    for j in range(a):
        print('*', end=' ')
    print()
    a = a + 1

# Another solution, without using a
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()