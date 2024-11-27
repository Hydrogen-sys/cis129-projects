# Open the file for writing
with open('grades.txt', 'w') as file:
    while True:
        grade = int(input("Enter a grade (negative number to quit): "))
        if grade < 0:
            break  # Exit the loop if a negative number is entered
        file.write(str(grade) + '\n')  # Write the grade to the file

print("Grades saved to grades.txt")
