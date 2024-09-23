# import datetime

# # Get the current day of the week
# current_day = datetime.datetime.now().strftime("%A")

# # Ask the user for the subtotal
# subtotal = float(input("Enter the subtotal: $"))

# # Define the sales tax rate
# sales_tax_rate = 0.06

# # Initialize discount variables
# discount_rate = 0.10
# discount = 0.0

# # Check if today is Tuesday or Wednesday and the subtotal is $50 or more
# if current_day in ["Tuesday", "Wednesday"] and subtotal >= 50:
#     discount = subtotal * discount_rate
#     subtotal -= discount

# # Calculate the sales tax
# sales_tax = subtotal * sales_tax_rate

# # Calculate the total amount due
# total = subtotal + sales_tax

# # Print the discount, if applicable
# if discount > 0:
#     print(f"Discount applied: ${discount:.2f}")
# else:
#     if current_day in ["Tuesday", "Wednesday"]:
#         difference = 50 - subtotal
#         if difference > 0:
#             print(f"Spend ${difference:.2f} more to receive a 10% discount!")

# # Print the sales tax and total amount due
# print(f"Sales tax: ${sales_tax:.2f}")
# print(f"Total amount due: ${total:.2f}")




# Import the datetime class from the datetime module
from datetime import datetime

# Ask the user for the subtotal
subtotal = float(input("Enter the subtotal: $"))

# Get the current day of the week
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()  # Monday is 0, Tuesday is 1, ..., Sunday is 6

# Initialize the discount and tax variables
discount = 0.0
sales_tax_rate = 0.06

# Check if today is Tuesday (1) or Wednesday (2) and if the subtotal is $50 or more
if day_of_week in [1, 2] and subtotal >= 50:
    discount = subtotal * 0.10  # 10% discount
    subtotal -= discount
    print(f"Discount applied: ${discount:.2f}")
else:
    if day_of_week in [1, 2] and subtotal < 50:
        print(f"Spend ${50 - subtotal:.2f} more to get a 10% discount.")

# Calculate the sales tax and total amount due
sales_tax = subtotal * sales_tax_rate
total = subtotal + sales_tax

# Print the sales tax and total amount due
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total amount due: ${total:.2f}")
