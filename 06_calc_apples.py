# Lets create a simple program to calculate the cost of apples
# We will use all the things we have learnt so far

# Define a function to calculate total cost
def calculate_total_cost(number_of_apples, cost_per_apple):
    return number_of_apples * cost_per_apple

# Create a function to validate user input
def validate_input(user_input):
    if user_input == "exit":
        exit()                          # exit the program if user input is exit
    if not user_input.isnumeric():
        return False                    # return False if user input is not a number
    if float(user_input) < 1:
        return False                    # return False if user input is negative
    return True                         # return True otherwise

# Create a function to get user input
def get_user_input(prompt):
    user_input = input(prompt)
    while (not validate_input(user_input)):
        user_input = input("Invalid input. Please enter a positive integer: ")
    return float(user_input)

# We can now use the functions we defined above to write our program
# Use an infinite loop to get user input until the user wants to quit (by entering exit)
def main():
    prices = []
    while True:
        # Get user input
        number_of_apples = get_user_input("Enter number of apples: ")
        cost_per_apple = get_user_input("Enter cost per apple: ")

        # Calculate total cost
        total_cost = calculate_total_cost(number_of_apples, cost_per_apple)
        prices.append(total_cost)
        print("Total cost:", total_cost)
        print("different prices so far:", prices)
        print("Total cost so far:", sum(prices))

main()
