# num1 = int(input("please enter number 1:"))
# num2 = int(input("please enter number 2:"))
# 1
# print(num1+num2)





# # Get the number of manufactured items
# num_items = int(input("Enter the number of manufactured items: "))

# # Get the number of items per box
# items_per_box = int(input("Enter the number of items per box: "))

# # Calculate the number of boxes needed (consider integer division for whole boxes)
# num_boxes = num_items // items_per_box

# # Check if there are any leftover items for the last box
# leftover_items = num_items % items_per_box

# # Print the results
# print(f"Number of boxes needed: {num_boxes}")

# if leftover_items > 0:
#   print(f"Leftover items for the last box: {leftover_items}")
# else:
#   print("All items fit perfectly into boxes.")


# Ask the user for the number of manufactured items
num_items = int(input("Enter the number of manufactured items: "))

# Ask the user for the number of items per box
items_per_box = int(input("Enter the number of items per box: "))

# Calculate the number of boxes needed
# Use the ceiling logic to account for the last box which may have fewer items
num_boxes = (num_items + items_per_box - 1) // items_per_box

# Print the result
print(f"The number of boxes required: {num_boxes}")