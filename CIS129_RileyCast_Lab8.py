def is_palindrome(text):
  """
  Checks if a string is a palindrome, ignoring case, spaces, and punctuation.

  Args:
    text: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """

  # Convert the string to lowercase and remove spaces and punctuation
  clean_text = ''.join(c for c in text.lower() if c.isalnum())

  # Create a stack (using a list) to store the characters
  stack = []
  for char in clean_text:
    stack.append(char)

  # Compare the characters in the stack with the characters in the original string
  for char in clean_text:
    if char != stack.pop():
      return False

  # If all characters match, the string is a palindrome
  return True

# Get user input
user_input = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(user_input):
  print(f"'{user_input}' is a palindrome.")
else:
  print(f"'{user_input}' is not a palindrome.")
