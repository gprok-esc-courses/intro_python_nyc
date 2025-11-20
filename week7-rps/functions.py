
def find_even_total(data_list):
    counter = 0
    for value in data_list:
        if value % 2 == 0:
            # counter = counter + 1
            counter += 1
    return counter



data = [2, 5, 7, 1, 2, 6, 9, 11, 12]
even_total = find_even_total(data)
print(even_total) # 4

data = [1, 3, 5, 7, 9]
even_total = find_even_total(data)
print(even_total) # 0

data = [2, 4, 6, 8, 12, 14]
even_total = find_even_total(data)
print(even_total) # 6