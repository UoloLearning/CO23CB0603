# Ask the user for the amount of money they have
money = float(input("How much money do you have? "))

# Define the names and prices of the products as variables
product1_name = "book"
product1_price = 5.99
product2_name = "pen"
product2_price = 1.49
product3_name = "notebook"
product3_price = 2.99

# Compute the total price of all products
total_price = product1_price + product2_price + product3_price

# Check if the user can afford all products
can_afford_all = money >= total_price

# Print the result
print(f"You can afford all products: {can_afford_all}")
