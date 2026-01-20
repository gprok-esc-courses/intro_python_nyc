import csv 

recipes = []
file = open('recipes.csv')
csv_file = csv.DictReader(file) 
for line in csv_file:
    recipes.append(line)
    print(line)

# find last id
last_id = recipes[-1]['id']
print(last_id)