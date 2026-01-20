import csv 

def menu():
    print("""===== RECIPES APP MENU ======  
1. Add new recipe
2. View all recipes
3. Search
4. Delete recipe 
5. Statistics 
6. Recommend recipe
0. Save and exit
============================= """)
    choice = int(input("Select (0 - 6): "))
    return choice
    
choice = -1

### Load recipes from the file
recipes = {}
file = open('recipes.csv')
csv_file = csv.DictReader(file) 
for line in csv_file:
    id = int(line['id'])
    recipes[id] = line
# for id in recipes:
#     print(id, recipes[id])

next_id = max(recipes.keys()) + 1

while choice != 0:
    choice = menu()
    print(choice)
    if choice == 1:
        # Ask user for new recipes data
        # recipes[next_id] = {'id': id, 'name': name, 'cuisine': cuisine, etc}
        # increase next_id
        print("Adding a new recipe ...")
    elif choice == 2:
        # For each id in the recipes
        # print the recipe
        print("All recipes ...")
    elif choice == 3:
        # Ask search term from the user
        term = input("Give search term: ")
        # Display the recipes who have the term in category, cuisine or ingredient 
        for id in recipes:
            recipe = recipes[id]
            if recipe['category'] == term:
                print(recipe['name'])
        print("Searching ...")
    elif choice == 4:
        # Ask user for id to delete (as an int)
        # pop the id from the dictionary
        print("Deleting recipe ...")
    elif choice == 5:
        # Go through the dictionary count recipes by cuisine and display the result
        # Go through the dictionary count recipes by ingredient and display the result (more difficult)
        print("Displaying stats ...")
    elif choice == 6:
        # Ask user for category
        # Find a random recipe in this category and display it
        print("Recommended recipe ...")
    elif choice == 0:
        # Save the dictioary into the file
        print("Bye bye")
    else: 
        print("Wrong choice")