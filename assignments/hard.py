
file = open('recipes.csv')
lines = file.readlines()

for line in lines:
    line = line.strip()
    split_quotes = line.split('"')
    if len(split_quotes) > 1:
        # print(split_quotes)
        first_part = split_quotes[0].split(',')
        second_part = split_quotes[1]
        third_part = split_quotes[2].split(',')
        # print(first_part)
        # print(third_part)
        data = first_part[0:-1]
        data.append(second_part)
        data.append(third_part[1])
        print(data)