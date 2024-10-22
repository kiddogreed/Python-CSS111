# Author: John Russelle Domingo
# Date: OCT19_2024
# Updated: Oct22_2024
# Desc:
"""
This program reads data from two CSV files: products.csv and request.csv,
and generates a receipt for a store transaction, including total, sales tax,
and itemized details. It also includes error handling for common file-related
exceptions.
"""

import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary where the values are lists
        containing the entire row (including the key).
    """
    compound_dict = {}

    try:
        with open(filename, mode='r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the headers row
            for row in reader:
                key = row[key_column_index]  # Use the key_column_index to get the key
                compound_dict[key] = row  # Store the entire row as a list
        return compound_dict

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except PermissionError:
        print(f"Error: You do not have permission to read the file {filename}.")
        return None


def main():
    try:
        # Store name and details
        store_name = "Russelle's Corner Store"
        tax_rate = 0.06
        
        # Call the read_dictionary function and store the dictionary in products_dict
        products_dict = read_dictionary("wk5\\products.csv", 0)
        
        if products_dict is None:
            return  # Exit if products_dict could not be loaded

        print(f"\n{store_name}")
        print("------------------------------")

        # Variables for tracking totals
        total_quantity = 0
        subtotal = 0.0

        print("Requested Items\n")

        # Open the request.csv file for reading
        with open("wk5\\request.csv", mode='r', newline='', encoding='utf-8') as request_file:
            request_reader = csv.reader(request_file)

            # Skip the first line (header)
            next(request_reader)
            
            # Loop through each row in the request.csv file
            for row in request_reader:
                product_number = row[0]  # Assume first column is product number
                requested_quantity = int(row[1])  # Assume second column is requested quantity
                
                # Find the corresponding product in the products_dict
                if product_number in products_dict:
                    product_details = products_dict[product_number]
                    product_name = product_details[1]  # "Name" is the second item in the row
                    product_price = float(product_details[2])  # "Price" is the third item in the row
                    
                    # Calculate line total
                    line_total = requested_quantity * product_price

                    # Print the product details
                    print(f"{product_name}: {requested_quantity} @ ${product_price:.2f} = ${line_total:.2f}")

                    # Update totals
                    total_quantity += requested_quantity
                    subtotal += line_total
                else:
                    print(f"Product number {product_number} not found in products_dict.")

        # Sales tax and total
        sales_tax = subtotal * tax_rate
        total = subtotal + sales_tax

        print("\n------------------------------")
        print(f"Number of items: {total_quantity}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax (6%): ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")
        print("\nThank you for shopping at Russelle's Corner Store!")

        # Print the current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\nDate and Time: {current_datetime}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: A key error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Protect main function 
if __name__ == "__main__":
    main()
