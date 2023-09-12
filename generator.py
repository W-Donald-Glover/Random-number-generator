import random

# Ask the user for the minimum and maximum numbers
min_number = int(input("Enter the minimum number: "))
max_number = int(input("Enter the maximum number: "))

# Generate a random number between min_number and max_number
random_number = random.randint(min_number, max_number)

# Print the random number
print("Random Number between", min_number, "and", max_number, ":", random_number)
