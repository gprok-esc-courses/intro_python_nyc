
student_file = open("students.txt", "a")

while True:
    name = input("Student name (exit to stop): ")
    if name == 'exit':
        break 
    grade = input("Grade: ")
    student_file.write(name + "," + grade + "\n")

student_file.close()
