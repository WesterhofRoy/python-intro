# A simple program to demonstrate variables and user input in Python

number_of_apples = float(input("Enter number of apples: "))
print('user entered', number_of_apples, 'apples')
cost_per_apple = float(input("Enter cost per apple: "))
print('user entered', cost_per_apple, 'dollars per apple')
total_cost = number_of_apples * cost_per_apple
print("Total cost:", int(total_cost+0.5))
