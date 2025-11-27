
data_file = open("data.txt")
lines = data_file.readlines()

for line in lines:
    line = line.strip()
    print(line)