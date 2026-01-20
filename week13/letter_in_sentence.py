# Ask user to type a sentence and find and display how many times each letter appears in sentence
# Example: Hello World
# h: 1, e: 1, l: 3, o: 2, w: 1, r: 1, d: 1

sentence = input("Type a sentence: ")

sentence_lower = sentence.lower()

counts = {}

for letter in sentence_lower:
    if letter.isalpha(): 
        if letter in counts: 
            counts[letter] += 1 
        else: 
            counts[letter] = 1

for letter in counts:
    print(f"{letter}: {counts[letter]}")