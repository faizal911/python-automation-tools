import os
import random
import math
from datetime import datetime

filename = "report.txt"

students = {
    "Faizal": 85,
    "Ravi":   72,
    "Ayesha": 91,
    "Zara":   55,
    "Omar":   78
}

def get_grade(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "C"

now = datetime.now()
date_str = now.strftime("%d-%m-%Y")

star = random.choice(list(students.keys()))

# build report
with open(filename, "w") as file:
    file.write(f"Report generated on: {date_str}\n")
    file.write(f"Student of the Day: {star}\n\n")
    file.write("--- All Students ---\n")
    
    marks_list = []
    for name, marks in students.items():
        try:
            grade = get_grade(marks)
            line = f"Student: {name} | Marks: {marks} | Grade: {grade}"
            print(line)
            file.write(line + "\n")
            marks_list.append(marks)
        except ValueError as e:
            print(f"Error for {name}: {e}")

    average = round(sum(marks_list) / len(marks_list), 1)
    print(f"\nAverage Marks: {average}")
    file.write(f"\nAverage Marks: {average}\n")

print(f"Report generated on: {date_str}")
print(f"Student of the Day: {star}")
print("Report saved to report.txt")