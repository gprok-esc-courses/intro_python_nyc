**Midterm Assignment**
# Recipe Collection

### Overview

Create an application to manage personal recipes. The application will help user to organize their favorite recipes, search 

### Objectives

**To apply topics covered so far in class**:  
Control structuree (selection, repetition)  
Lists, Dictionaries  
File handling  
Data validation  
**To develop logical thinking and problem solving skills**  

### Data File Structure
For each recipe we will keep:  
1. ID: a unique number
2. Name of the dish
3. Cuisine type (e.g. Italian, Chinese, Middle East, etc)
4. Difficulty (Easy, Medium, or Difficult)
5. Peparation time
6. Ingredients
7. Category (Breakfast, Lunch, Dinner, Snack, Dessert)
A sample ```recipes.csv``` file is provided.

### Menu System 
A menu will help the user to select actions. 

```
===== RECIPES APP MENU ======  
1. Add new recipe
2. View all recipes
3. Search
4. Delete recipe 
5. Statistics 
6. Recommend recipe
0. Save and exit
=============================
Select (0 - 6): 
```

### Specifications 

1. A new recipe will recive the next available id, which is the id of the current last recipe plus one. You need to establish a mechanism to find the next id. 
2. Display the id and the name of each recipe in alphabetical order.
3. Search by cuisine, category, or ingredient.
4. The id of a deleted recipe will not be reused.
5. Display Number of recipes by cuisine, and number of recipes by ingredient.
6. Ask user for the category and randomly display a recipe of this category.