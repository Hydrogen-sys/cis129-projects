In [1]: # Lab 5 The Bottle Return Program

   ...: 

   ...: # Author: Riley Cast

   ...: # Date: 2024-10-16 

   ...: # This program calculates the total payout for a week's worth of bottle returns.

   ...: 

   ...: # Step 1: Declare variables below 

   ...: total_bottles = 0  # Variable to store the total number of bottles collected

   ...: today_bottles = 0  # Variable to store the number of bottles collected for a single day

   ...: counter = 1  # Counter for the day of the week (1-7)

   ...: total_payout = 0  # Variable to store the total payout

   ...: keep_going = "y"  # Variable to control the loop (y = continue, n = stop)

   ...: 

   ...: # Step 2: Loop to run program again

   ...: while keep_going == "y":  # This loop continues as long as the user enters 'y'

   ...:     # Step 3: Code to set value of variables

   ...:     # Reset the total bottles and payout for each new week

   ...:     total_bottles = 0

   ...:     total_payout = 0

   ...:     # Code to set value of variable totalBottles 

   ...:     for day in range(1, 8):

   ...:         today_bottles = int(input(f"Enter number of bottles returned for day #{day}: "))

   ...:         total_bottles += today_bottles

   ...:     # Code to set value of variable totalPayout

   ...:     total_payout = total_bottles * 0.10  # Calculate the total payout directly

   ...:     # Code to print the number of total bottles and total payout

   ...:     print(f"The total number of bottles collected is {total_bottles}")

   ...:     print(f"The total paid out is ${total_payout:.1f}")

   ...: 

   ...:     # Ask the user if they want to run the program again

   ...:     keep_going = input("Do you want to enter another week’s worth of data? (Enter y or n): ")
