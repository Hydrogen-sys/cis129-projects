# Define the filename
filename = 'grades.txt'

# Initialize a list to store grades
grades = []

# Read the grades from the file
with open(filename, 'r') as file:
    for line in file:
        # Assuming each line contains a single grade
        try:
            grade = int(line.strip())  # Convert the line to an integer
            grades.append(grade)  # Add the grade to the list
        except ValueError:
            print(f"Invalid grade found: {line.strip()}")  # Handle non-integer values

# Calculate total, count, and average
total = sum(grades)
count = len(grades)
average = total / count if count > 0 else 0  # Avoid division by zero

# Display the results
print("Individual Grades:", grades)
print("Total Grades:", total)
print("Count of Grades:", count)
print("Average Grade: {:.2f}".format(average))
