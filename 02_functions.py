"""
Functions.
This program shows how to use functions in Python.
We are going to write the same program as in 01_variables.py, but this time we will use functions.
We will also do some more calculations on the total cost, like adding tax and discount.
"""

# Define a function to get user input
def get_user_input(prompt):
    return float(input(prompt))

# Define a function to calculate total cost
def calculate_total_cost(number_of_apples, cost_per_apple):
    return number_of_apples * cost_per_apple

# Define a function to calculate tax
def calculate_tax(total_cost, tax_rate):
    return total_cost * tax_rate

# Define a function to calculate discount
def calculate_discount(total_cost, discount_rate):
    return total_cost * discount_rate

# Define a function to calculate final cost
def calculate_final_cost(total_cost, tax, discount):
    return total_cost + tax - discount

# We can now use the functions we defined above to write our program

# Get user input
number_of_apples = get_user_input("Enter number of apples: ")
print('user entered', number_of_apples, 'apples')
cost_per_apple = get_user_input("Enter cost per apple: ")
print('user entered', cost_per_apple, 'dollars per apple')

# Calculate total cost
total_cost = calculate_total_cost(number_of_apples, cost_per_apple)
print("Total cost:", total_cost)

# Calculate tax
tax_rate = 0.1
tax = calculate_tax(total_cost, tax_rate)
print("Tax:", tax)

# Calculate discount
discount_rate = 0.05
discount = calculate_discount(total_cost, discount_rate)
print("Discount:", discount)

# Calculate final cost
final_cost = calculate_final_cost(total_cost, tax, discount)
print("Final cost:", final_cost)

# We can also use the functions we defined above to write a different program

# to keep things simple, we will use the same functions as above, but this time we will use them to calculate the cost of TVs
# we will also create a new function to calculate the final cost in a single function call
# We can call funtions from within other functions

# Define a function to calculate final cost
def direct_calculate_final_cost(number_of_tvs, cost_per_tv, tax_rate, discount_rate):
    total_cost = calculate_total_cost(number_of_tvs, cost_per_tv)
    tax = calculate_tax(total_cost, tax_rate)
    discount = calculate_discount(total_cost, discount_rate)
    return total_cost + tax - discount

# Get user input
number_of_tvs = get_user_input("Enter number of TVs: ")
print('user entered', number_of_tvs, 'TVs')
cost_per_tv = get_user_input("Enter cost per TV: ")
print('user entered', cost_per_tv, 'dollars per TV')

tvs_final_cost = direct_calculate_final_cost(number_of_tvs, cost_per_tv, 0.1, 0.05)
print("Final cost:", tvs_final_cost)
