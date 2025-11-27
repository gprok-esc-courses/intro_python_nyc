
data_file = open("data.txt")
lines = data_file.readlines()

words = 0
characters = 0

for line in lines:
    line = line.strip()
    characters = characters + len(line)
    line_words = line.split()
    words = words + len(line_words)

print(f"Words {words}")
print(f"Chars {characters}")