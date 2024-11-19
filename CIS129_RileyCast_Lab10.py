def format_check_protected(amount):
    # Convert the amount to a string and strip any extra spaces
    amount_str = str(amount).strip()
    
    # Ensure there are no more than 10 characters (including the leading asterisks)
    if len(amount_str) > 10:
        return "Error: Amount too large"
    
    # Calculate how many leading asterisks are needed
    leading_asterisks = '*' * (10 - len(amount_str))
    
    # Return the formatted amount
    return leading_asterisks + amount_str

# Input from the user
user_input = float(input("Enter a dollar amount: "))
formatted_amount = format_check_protected(user_input)
print("Check-protected amount:", formatted_amount)
