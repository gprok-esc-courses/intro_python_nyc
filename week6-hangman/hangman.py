import random

wrong = []
correct = []

# 1. Genereate random word 

words = ["inheritance", "polymorphism", "encapsulation",
         "functional", "concurrent", "object", "strategy",
         "compiler", "interpreter", "statement"]
pos = random.randint(0, len(words)-1)
word = words[pos]

print(word)

# Repeat until HANGED or FOUND
while True:
    # 2. Generate the secret (e.g. for airplane -> a------e)

    secret = word[0]
    for i in range(1, len(word)-1):
        if word[i] in correct:
            secret = secret + word[i]
        else:
            secret = secret + '-'
    secret = secret + word[-1]

    print(secret)

    # 5. Check Found
    if secret == word:
        print(word)
        print("CONGRATS, FOUND!")
        break


    # 3. Play and keep wrong and correct guess somewhere

    letter = input("Guess a letter: ")

    if letter in word:
        if letter not in correct:
            correct.append(letter)
    else:
        if letter not in wrong:
            wrong.append(letter)

    print(correct)
    print(wrong)

    # 4. Check Hanged
    if len(wrong) == 6:
        print("YOU ARE HANGED")
        break

    



# OTHER WAYS TO CREATE THE SECRET

# another apporach
# secret = word[0] + ('-' * (len(word)-2)) + word[-1]
# print(secret)

# another, as a list
# secret_list = [ word[0] ]
# for i in range(len(word)-2):
#     secret_list.append('-')
# secret_list.append(word[-1])
# print(secret_list)