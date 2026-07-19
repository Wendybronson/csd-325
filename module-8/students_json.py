# ---------------------------------------------------------
# Wendy Bronson
# Module 8.2 Assignment: JSON Student List
# Date: July 2026
#
# Purpose:
# Load student data from a JSON file, print the original
# list, add a new student, print the updated list, and
# save the updated data back to the JSON file.
# ---------------------------------------------------------

import json


def print_students(student_list):
    """Print each student's information."""
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']}, "
            f"Email = {student['Email']}"
        )


# Load the original student list.
with open("Student.json", "r") as file:
    students = json.load(file)

# Print original list.
print("This is the original Student list.")
print_students(students)

# Add my student information.
new_student = {
    "F_Name": "Wendy",
    "L_Name": "Bronson",
    "Student_ID": 12345,
    "Email": "wbronson@my365.bellevue.edu"
}

students.append(new_student)

# Print updated list.
print("\nThis is the updated Student list.")
print_students(students)

# Save updated list back to JSON file.
with open("Student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nThe Student.json file has been updated.")