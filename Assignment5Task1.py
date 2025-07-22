# Step 1: Create a dictionary with student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Ethan": 74
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display the marks or show a message if not found
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student not found.")
