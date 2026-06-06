import os

filename = "students.txt"

if os.path.exists(filename):
    os.remove(filename)

def add_student(name, marks):
    if marks < 0:
        raise ValueError("Marks cannot be negative.")
    if marks > 100:
        raise ValueError("Marks cannot be greater than 100.")
    with open(filename, "a") as file:
        file.write(f"Student: {name} | Marks: {marks}\n")
    print(f"{name} added successfully.")

def show_students():
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No students found.")

try:
    add_student("Faizal", 85)
except ValueError as e:
    print("Error:", e)

try:
    add_student("Ravi", 110)
except ValueError as e:
    print("Error:", e)

try:
    add_student("Ayesha", 92)
except ValueError as e:
    print("Error:", e)

print("--- All Students ---")
show_students()