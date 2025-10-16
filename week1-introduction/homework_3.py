# Display a simple menu:
# a. Open File
# b. Save File
# c. Delete File
# x. Exit
# SELECT > ___
# If the user select a display a message "File is opening", 
# if b "Saving file ...", 
# if c "File deleted", 
# if x display "Bye!", 
# in any other case display "Wrong selection".


# Display the menu
print("a. Open File")
print("b. Save File")
print("c. Delete File")
print("x. Exit")

# Ask user to select:
choice = input("SELECT > ")

# Process choice
if choice == 'a':
    print("File is opening")
elif choice == 'b':
    print("Saving file ...")
elif choice == 'c':
    print("File deleted")
elif choice == 'x':
    print("Bye!")
else:
    print("Wrong selection")