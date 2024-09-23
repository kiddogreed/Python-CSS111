# Import the sleep function from the time module, so
# that the sleep function can be used in this program.
from time import sleep

# Prompt the user to enter her name.
name = input("Hello! What is your name? ")

# Print the numbers 3, 2, 1.
for i in range(10, 0, -1):
    print(i, flush=True)
    sleep(0.5)  # Pause for 1/2 second

# Use a Python f-string to format a greeting
# for the user and then print the greeting.
print(f"Welcome to CSE 111, {name}!")



#comment

# This is a comment because it has
# hash symbols at the beginning.



#variables
length = 5
time = 7.2
in_flight = True
first_name = "Cho"



#Data Types

#string
greeting = "Hello"
text = "23"

#bool 
found = True
isOn = False

#int
x = 14
age = 123
days =365

#Float
sample = 7.51
pi = 3.14



#list
colors = ["yellow", "red", "green", "yellow", "blue"]
samples = [6.5, 7.2, 7.0, 8.1, 7.2, 6.8, 6.8]


#dict 
students = {
    "42-039-4736": "Clint Huish",
    "61-315-0160": "Amelia Davis",
    "10-450-1203": "Ana Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Amelia Davis"
}


#stdin
text = input("Please enter your name: ")
color = input("What is your favorite color? ")


#stdout
print(f"Heart rate: {rate}")
print("text")


# Example 1
# Create variables of different data types and then
# print the variable names, data types, and values.
a = "Her name is "  # string
b = "Isabella"      # string
c = a + b           # string plus string makes string
print(f"a: {type(a)} {a}")
print(f"b: {type(b)} {b}")
print(f"c: {type(c)} {c}")
print()
d = False  # boolean
e = True   # boolean
print(f"d: {type(d)} {d}")
print(f"e: {type(e)} {e}")
print()
f = 15     # int
g = 7.62   # float
h = f + g  # int plus float makes float
print(f"f: {type(f)} {f}")
print(f"g: {type(g)} {g}")
print(f"h: {type(h)} {h}")
print()
i = "True"   # string because of the surrounding quotes
j = "2.718"  # string because of the surrounding quotes
print(f"i: {type(i)} {i}")
print(f"j: {type(j)} {j}")


# Example 4
# Compute the total price of a pizza.
# The base price of a large pizza is $10.95
price = 10.95
# Ask the user for the number of toppings.
number_of_toppings = int(input("How many toppings? "))
# Compute the cost of the toppings.
price_per_topping = 1.45
toppings_cost = number_of_toppings * price_per_topping
# Add the cost of the toppings to the price of the pizza.
price = price + toppings_cost
# Print the price for the user to see.
print(f"Price: ${price:.2f}")




#if statement

# Example 62
# Get an account balance as a number from the user.
balance = float(input("Enter the account balance: "))
# If the balance is greater than 500, then
# compute and add interest to the balance.
if balance > 500:
    interest = balance * 0.03
    balance += interest
# Print the balance.
print(f"balance: {balance:.2f}")



#elif
# Example 7
# Get the cost of an item from the user.
cost = float(input("Please enter the cost: "))
# Determine a discount rate based on the cost.
if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20
# Compute the discount amount
# and the discounted cost.
discount = cost * rate
cost -= discount
# Print the discounted cost for the user to see.
print(f"After the discount, you will pay {cost:.2f}")



#and/or/not
if driver >= 54 or (driver >= 32 and passenger >= 54):
    message = "Enjoy the ride!"


