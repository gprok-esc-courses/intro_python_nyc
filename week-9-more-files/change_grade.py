
students = []
infile = open("students.csv")
lines = infile.readlines()

for line in lines:
    line = line.strip()
    student = line.split(',')
    students.append(student)
infile.close()

id = input("ID: ")
grade = input("Grade: ")

for student in students:
    if student[0] == id:
        student[2] = grade 
        break

outfile = open("students.csv", "w")
for student in students:
    line = f"{student[0]},{student[1]},{student[2]}\n"
    outfile.write(line)
outfile.close()