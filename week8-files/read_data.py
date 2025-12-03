
data_file = open("data.txt", "r")
lines = data_file.readlines()

for line in lines:
    line = line.strip()
    print(line)