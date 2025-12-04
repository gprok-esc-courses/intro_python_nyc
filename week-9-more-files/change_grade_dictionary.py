
students = []
infile = open("students.csv")
lines = infile.readlines()

for line in lines:
    line = line.strip()
    data = line.split(',')
    student = {'id': data[0], 'name': data[1], 'gpa': data[2]}
    students.append(student)
infile.close()

id = input("ID: ")
grade = input("Grade: ")

for student in students:
    if student['id'] == id:
        student['gpa'] = grade 
        break

outfile = open("students.csv", "w")
for student in students:
    line = f"{student['id']},{student['name']},{student['gpa']}\n"
    outfile.write(line)
outfile.close()