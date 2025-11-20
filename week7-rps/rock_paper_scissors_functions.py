import random

# Rock Paper Scissors

def get_user_choice():
    choice = input("Play P-R-S: ")
    if choice not in "PRS":
        print(choice + + " wrong choice")
        choice = None
    return choice

def generate_computer_choice():
    choice = options[random.randint(0, 2)]
    print(f"Computer: {choice}")
    return choice

def find_winner(computer, user):
    if computer == user:
        print("It's a Tie")
        return None
    elif computer == 'R' and user == 'P':
        return "user"
    elif computer == 'R' and user == 'S':
        return "computer"
    elif computer == 'P' and user == 'S':
        return "user"
    elif computer == 'P' and user == 'R':
        return "computer"
    elif computer == 'S' and user == 'R':
        return "user"
    elif computer == 'S' and user == 'P':
        return "computer"
    
def display_score(computer, user):
    print(f"SCORE User: {user} - Computer: {computer}")

# 1. Define the variables
user_score = 0
computer_score = 0
user_choice = None 
computer_choice = None 
options = ['P', 'R', 'S']

# 2. Repeat until user or computer score becomes 10 
while user_score < 10 and computer_score < 10:

    user_choice = get_user_choice()
    if user_choice is None:
        continue

    computer_choice = generate_computer_choice()

    winner = find_winner(computer_choice, user_choice)
    if winner == 'user':
        user_score = user_score + 1
    elif winner == "computer":
        computer_score = computer_score + 1
    
    display_score(computer_score, user_score)

 

# 8. Display the winner 
if computer_score == 10:
    print("Computer Wins")
else:
    print("User Wins")

