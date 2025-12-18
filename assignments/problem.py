
file = open('recipes.csv')

lines = file.readlines()

for line in lines:
    line = line.strip()
    data = line.split(',')
    print(data)