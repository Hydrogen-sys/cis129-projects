import csv

# Define the student records
students = [
    {"Name": "Alice", "Age": 20, "Major": "Computer Science"},
    {"Name": "Bob", "Age": 22, "Major": "Mathematics"},
    {"Name": "Charlie", "Age": 21, "Major": "Physics"},
]

# Specify the CSV file name
csv_file = "student_records.csv"

# Write the records to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=students[0].keys())
    writer.writeheader()
    for student in students:
        writer.writerow(student)

print(f"Student records have been written to {csv_file}.")
Student records have been written to student_records.csv.
