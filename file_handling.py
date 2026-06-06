
# with  open("students.txt","w") as file:
#     file.write("Student: faizal |  grade: A\n")
#     file.write("Student: ravi   |  grade: B\n")
#     file.write("Student: ayesha |  grade: A+\n")

# with open("students.txt", "r") as file:
#  content = file.read()
# print(content)

# with open("students.txt","a")as file:
#     file.write("student:  zara  | grade: A\n")


# with open("students.txt","r") as file:
#     for line in file:
#         print(line.strip())

#   ----------------------------------------------------------

# with open("students.txt","w") as file:
#     file.write("student : Sara   | Grade: A\n")
#     file.write("student : Ravi   | Grade: B\n")
#     file.write("student : Faizal | Grade: A+\n")

# with open("students.txt","a")as file:
#     file.write("student : Zara   | Grade: A+\n")

# with open("students.txt","r") as file:
#    for line in file:
#             print(line.strip())

#   ----------------------------------------------------------

# students = [
#     "Student: Faizal | Grade: A\n",
#     "Student: Ravi   | Grade: B\n",
#     "Student: Ayesha | Grade: A+\n"
# ]
# with open("students.txt", "w") as file:
#     file.writelines(students)


# with open("students.txt","r") as file:
#    for line in file:
#             print(line.strip())    

#   ----------------------------------------------------------

# import os

# if os.path.exists("students.txt"):
#     with open("students.txt","r") as file:
#         print(file.read())
# else:
#     print("File not found.")

#   ----------------------------------------------------------

# import csv

# with open("students.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","Grade"])
#     writer.writerow(["Faizal", "A"])
#     writer.writerow(["Sara","A"])
#     writer.writerow(["Ravi","B"])

# with open("students.csv","r")as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

#   ----------------------------------------------------------

import os

filename = "students.txt"

def add_student(name, grade):
    with open(filename, "a") as file:
        file.write(f"Student: {name} | Grade: {grade}\n")

def show_students():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())
    else:
        print("No students found.")

def delete_file():
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully")
    else:
        print("File doesn't exist.")

add_student("Faizal", "A")
add_student("Ravi", "B")
add_student("Ayesha", "A+")
print("--- All Students ---")
show_students()
delete_file()