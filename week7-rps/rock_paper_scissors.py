import random

# Rock Paper Scissors

# 1. Define the variables
user_score = 0
computer_score = 0
user_choice = None 
computer_choice = None 
options = ['P', 'R', 'S']

# 2. Repeat until user or computer score becomes 10 
while user_score < 10 and computer_score < 10:

    # 3. Ask user to play 
    user_choice = input("Play P-R-S: ")
    # 4. If user selection is wrong display error message and skip the rest
    if user_choice not in "PRS":
        print(user_choice + " wrong choice")
        continue

    # 5. Generate choice for the computer 
    computer_choice = options[random.randint(0, 2)]
    print(f"Computer: {computer_choice}")

    # 6. Find the winner (if any) 
    if computer_choice == user_choice:
        print("It's a Tie")
    elif computer_choice == 'R' and user_choice == 'P':
        user_score = user_score + 1
    elif computer_choice == 'R' and user_choice == 'S':
        computer_score = computer_score + 1
    elif computer_choice == 'P' and user_choice == 'S':
        user_score = user_score + 1
    elif computer_choice == 'P' and user_choice == 'R':
        computer_score = computer_score + 1
    elif computer_choice == 'S' and user_choice == 'R':
        user_score = user_score + 1
    elif computer_choice == 'S' and user_choice == 'P':
        computer_score = computer_score + 1

    # 7. Display score
    print(f"SCORE User: {user_score} - Computer: {computer_score}")
 

# 8. Display the winner 
if computer_score == 10:
    print("Computer Wins")
else:
    print("User Wins")

