
# In each example find student 3 and print its name and GPA

# This is a list of lists. Every element (sub-list) in the list is a student
students1 = [
    [1, 'A B', 3.7],
    [2, 'C D', 2.9],
    [3, 'E F', 4.0],
    [4, 'G H', 3.2]
]

for s in students1:
    if s[0] == 3:
        print(1, s[1], s[2])


students2 = [
    {'id':1, 'name':'A B', 'gpa':3.7},
    {'id':2, 'name':'C D', 'gpa':2.9},
    {'id':3, 'name':'E F', 'gpa':4.0},
    {'id':4, 'name':'G H', 'gpa':3.2}
]

for student in students2:
    if student['id'] == 3:
        s = student
        print(2, s['name'], s['gpa'])

students3 = {
    1: {'id':1, 'name':'A B', 'gpa':3.7},
    2: {'id':2, 'name':'C D', 'gpa':2.9},
    3: {'id':3, 'name':'E F', 'gpa':4.0},
    4: {'id':4, 'name':'G H', 'gpa':3.2}
}

if 3 in students3:
    s = students3[3]
    print(3, s['name'], s['gpa'])