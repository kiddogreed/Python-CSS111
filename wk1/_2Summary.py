#todo
# write a comment
# use the input and print functions
# use the int and float functions to convert a value from a string to a number
# store a value in a variable
# perform arithmetic
# write if … elif … else statements
# use the logical operators and, or, not



# Get user input
name = input("What is your name? ")

# Convert input to float
age = float(input("How old are you? "))

# Perform arithmetic
years_until_100 = 100 - age

# Use if-elif-else statement
if years_until_100 > 0:
    print(f"Hello, {name}! You will be 100 in {years_until_100} years.")
elif years_until_100 == 0:
    print(f"Hello, {name}! You are already 100 years old.")
else:
    print(f"Hello, {name}! You are older than 100 years old.")