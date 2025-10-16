
# Get a sentence
sentence = input("Type a sentence: ")

# Get a character
ch = input("Type a character: ")

counter = 0

for c in sentence:
    if c == ch:
        counter = counter + 1

print("Character", ch, "found", counter, "times")

print(sentence.count(ch))