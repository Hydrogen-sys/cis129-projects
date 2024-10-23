import math

def main():
    # Local variable for the total number of hot dogs needed.
    total = getTotalHotDogs()

    # Named constants for the package sizes
    DOGS = 10   # Hot dogs in a package
    BUNS = 8    # Hot dog buns in a package

    # Local variables
    dogsLeft = (DOGS - total % DOGS) % DOGS  # Left over hot dogs
    bunsLeft = (BUNS - total % BUNS) % BUNS  # Left over hot dog buns
    minDogs = math.ceil(total / DOGS)       # Minimum packages of hot dogs
    minBuns = math.ceil(total / BUNS)       # Minimum packages of hot dog buns

    # Output ----------------------------------------
    # Display the results.
    showResults(dogsLeft, minDogs, bunsLeft, minBuns)

def getTotalHotDogs():
    # Local variables
    people = int(input("Enter the number of people attending the cookout: "))  # Number of people attending
    hotDogs = int(input("Enter the number of hot dogs for each person: "))  # Hot dogs per person

    # Calculate the total number of hot dogs needed.
    total = people * hotDogs
    return total

def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    print("\nHot Dog Cookout Calculator Results:")
    print(f"Minimum number of hot dog packages required: {minDogs}")
    print(f"Minimum number of bun packages required: {minBuns}")
    print(f"Number of hot dogs left over: {dogsLeft}")
    print(f"Number of buns left over: {bunsLeft}")

# Start the program
main()
