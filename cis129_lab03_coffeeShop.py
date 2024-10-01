In [1]: # Get the number of items from the user(this part hurt my head)
   ...: num_coffees = int(input("Enter the number of coffees: "))
   ...: num_muffins = int(input("Enter the number of muffins: "))
   ...: num_sandwiches = int(input("Enter the number of sandwiches: "))
   ...: num_cookies = int(input("Enter the number of cookies: "))
   ...: 
   ...: # Set the prices of the items(the menu)
   ...: coffee_price = 5
   ...: muffin_price = 4
   ...: sandwich_price = 8
   ...: cookie_price = 2
   ...: 
   ...: # Calculate the cost of each item(the math part)
   ...: coffee_cost = num_coffees * coffee_price
   ...: muffin_cost = num_muffins * muffin_price
   ...: sandwich_cost = num_sandwiches * sandwich_price
   ...: cookie_cost = num_cookies * cookie_price
   ...: 
   ...: # Calculate the subtotal(also math)
   ...: subtotal = coffee_cost + muffin_cost + sandwich_cost + cookie_cost
   ...: 
   ...: # Calculate the tax (6% of the subtotal)
   ...: tax = subtotal * 0.06
   ...: 
   ...: # Calculate the total cost(what the customer has to pay)
   ...: total_cost = subtotal + tax
   ...: 
   ...: # Print the results(your reciept)
   ...: print("Subtotal:", subtotal)
   ...: print("Tax:", tax)
   ...: print("Total Cost:", total_cost)
   ...: # Print a thank you message and the order summary
   ...: print("\nThank you for your order!")
   ...: print("Here's what you bought:")
   ...: if num_coffees > 0:
   ...:     print(f"- {num_coffees} coffee(s) - ${coffee_cost:.2f}")
   ...: if num_muffins > 0:
   ...:     print(f"- {num_muffins} muffin(s) - ${muffin_cost:.2f}")
   ...: if num_sandwiches > 0:
   ...:     print(f"- {num_sandwiches} sandwich(es) - ${sandwich_cost:.2f}")
   ...: if num_cookies > 0:
   ...:     print(f"- {num_cookies} cookie(s) - ${cookie_cost:.2f}")
   ...: print(f"\nYour total is ${total_cost:.2f}")
