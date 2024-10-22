#Author John Russelle Domingo
#Date: OCT19_2024
#Desc:
"""Download both of these files: products.csv and request.csv and save them in the same folder where you will save your Python program.
Open the products.csv file in VS Code and examine it. Notice that each row in this file contains three values separated by commas: a product number, a product name, and a retail price. Also, notice that each product number in the products.csv file is unique. This means that your program can read the products.csv file into a dictionary and use the product numbers as keys in the dictionary.
In VS Code, create a new file and save it as receipt.py in the same folder where you saved the products.csv and request.csv files.
In receipt.py, write a function named read_dictionary that will open a CSV file for reading and use a csv.reader to read each row and populate a compound dictionary with the contents of the products.csv file. The read_dictionary function must have this header and documentation string:"""
import csv

def read_dictionary(filename, key_column_index):
        
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}

    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the headers row
        for row in reader:
            key = row[key_column_index]  # Use the key_column_index to get the key
            compound_dict[key] = row  # Store the entire row as a list

    return compound_dict
  
  
def main():
    # Call the read_dictionary function and store the dictionary in products_dict
    products_dict = read_dictionary("wk5\\products.csv", 0)
    
    # Print the compound dictionary
    print("Products Dictionary:")
    for key, value in products_dict.items():
        print(f"{key}: {value}")
    
    
    print("Requested Items")      
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
                product_name = products_dict[product_number]["Name"] # Adjust as per actual CSV column name
                product_price = float(products_dict[product_number]["Price"])  # Adjust as per actual CSV column name
                
                # Print the product details
                print(f"{product_name}: {requested_quantity} @ {product_price:.2f}")
                #print(f"Product: {product_name}, Quantity: {requested_quantity}, Price: {product_price:.2f}")
            else:
                print(f"Product number {product_number} not found in products_dict.")


if __name__ == '__main__':
    main()
  