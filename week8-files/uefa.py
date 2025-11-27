
uefa_file = open('uefa.csv', encoding='utf-8')
lines = uefa_file.readlines() 

country = input("Country: ")
counter = 0

for line in lines:
    line = line.strip()
    data = line.split(',')
    if data[4] == country:
        counter = counter + 1

print(f'{country} appears {counter} times')