# Create an empty list
data = [] 

# Ask the user 5 times to give a value
# and put it in the list
for i in range(5):
    value = int(input('Give value: '))
    data.append(value)

print(data)