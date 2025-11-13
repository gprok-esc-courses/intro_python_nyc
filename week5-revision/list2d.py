# Create a 2D list of 
# of 5 rows and 6 cols
# and fill with random numbers 10 to 99.
import random

data = [] 

# For every row
for i in range(5):
    row = []
    # For every column
    for j in range(6):
        row.append(random.randint(10, 99))
    data.append(row)

for i in range(5):
    print(data[i])

# Each row represents a year, 
# and each col the sales of month
# Find the total per year, 
# and then the year with the max total
totals = []

for i in range(5):
    total = sum(data[i])
    totals.append(total)

print(totals)
m = max(totals)
print(f'Maximum sales: {m}')
p = totals.index(m)
print(f'Index of max: {p}')