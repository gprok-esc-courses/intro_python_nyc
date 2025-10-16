
choice = 'a'

while choice != 'x':
    # Display the menu
    print("MENU")
    print("a. Open file")
    print("b. Save file")
    print("x. EXIT")

# Ask user to select
choice = input("SELECT > ")

# Do the selected action
if choice == 'a':
    print("opening file ...")
elif choice == 'b':
    print("saving file ...")
elif choice == 'x':
    print('bye!')
else:
    print("wrong choice")