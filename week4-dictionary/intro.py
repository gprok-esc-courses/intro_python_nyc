
students = [
    {'lname': 'Doe', 'fname': 'John', 'gpa': 3.5},
    {'lname': 'Doe', 'fname': 'Mary', 'gpa': 2.5},
    {'lname': 'Wells', 'fname': 'Peter', 'gpa': 1.5},
    {'gpa': 3.8, 'fname': 'Mary', 'lname': 'Smith'}
]

for student in students:
    print(student['lname'], student['gpa'])
