# Constants for seating sections
SECTION_A = "A"
SECTION_B = "B"
SECTION_C = "C"

# Constants for seat prices
PRICE_A = 20
PRICE_B = 15
PRICE_C = 10

# Constants for seat capacities
CAPACITY_A = 300
CAPACITY_B = 500
CAPACITY_C = 200

def get_valid_tickets(section, capacity):
  """
  Prompts the user for the number of tickets sold for a given section,
  validates the input, and returns the valid number of tickets.

  Args:
    section: The name of the seating section (e.g., "A", "B", "C").
    capacity: The maximum number of seats in the section.

  Returns:
    The number of tickets sold for the section.
  """

  while True:
    try:
      tickets_sold = int(input(f"Enter number of tickets sold for section {section}: "))
      if 0 <= tickets_sold <= capacity:
        return tickets_sold
      else:
        print(f"Invalid input. Please enter a number between 0 and {capacity} for section {section}.")
    except ValueError:
      print("Invalid input. Please enter a valid number.")

def calculate_section_income(section, tickets_sold, price):
  """
  Calculates the income generated from ticket sales for a given section.

  Args:
    section: The name of the seating section (e.g., "A", "B", "C").
    tickets_sold: The number of tickets sold for the section.
    price: The price of a ticket in the section.

  Returns:
    The income generated from the section.
  """

  return tickets_sold * price

def main():
  """
  Main function to handle ticket sales and income calculation.
  """

  print("Welcome to the Theater Ticket Sales System!")
  print(f"Section {SECTION_A}: ${PRICE_A}, Capacity: {CAPACITY_A}")
  print(f"Section {SECTION_B}: ${PRICE_B}, Capacity: {CAPACITY_B}")
  print(f"Section {SECTION_C}: ${PRICE_C}, Capacity: {CAPACITY_C}")

  total_income = 0

  # Get ticket sales for each section
  tickets_a = get_valid_tickets(SECTION_A, CAPACITY_A)
  income_a = calculate_section_income(SECTION_A, tickets_a, PRICE_A)
  total_income += income_a
  print(f"Subtotal for Section {SECTION_A}: ${income_a}")

  tickets_b = get_valid_tickets(SECTION_B, CAPACITY_B)
  income_b = calculate_section_income(SECTION_B, tickets_b, PRICE_B)
  total_income += income_b
  print(f"Subtotal for Section {SECTION_B}: ${income_b}")

  tickets_c = get_valid_tickets(SECTION_C, CAPACITY_C)
  income_c = calculate_section_income(SECTION_C, tickets_c, PRICE_C)
  total_income += income_c
  print(f"Subtotal for Section {SECTION_C}: ${income_c}")

  print(f"Total income: ${total_income}")
  print(f"Tickets sold: Section {SECTION_A}: {tickets_a}, Section {SECTION_B}: {tickets_b}, Section {SECTION_C}: {tickets_c}")

if __name__ == "__main__":
  main()
