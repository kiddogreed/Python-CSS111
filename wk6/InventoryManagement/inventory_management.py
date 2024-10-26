# inventory_management.py

import csv
import os
import sys
from datetime import datetime

# File paths for data storage
PRODUCTS_FILE = "wk6\InventoryManagement\products.csv"
SALES_FILE = "wk6\InventoryManagement\sales.csv"

# ---------------- Inventory Management Functions ----------------

def read_products(filename=PRODUCTS_FILE):
    """Reads product data from CSV and returns as a dictionary."""
    products = {}
    try:
        with open(filename, mode="r", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product_id = row['product_id']
                products[product_id] = {
                    'name': row['name'],
                    'price': float(row['price']),
                    'stock': int(row['stock'])
                }
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    return products

def add_product(product_details):
    """Adds a new product to the inventory."""
    products = read_products()
    product_id = product_details['product_id']
    if product_id in products:
        print("Product already exists.")
    else:
        products[product_id] = {
            'name': product_details['name'],
            'price': float(product_details['price']),
            'stock': int(product_details['stock'])
        }
        write_products(products)
        print("Product added successfully.")

def update_stock(product_id, quantity):
    """Updates the stock level for a specified product."""
    products = read_products()
    if product_id in products:
        products[product_id]['stock'] += quantity
        write_products(products)
        print("Stock updated successfully.")
    else:
        print("Product not found.")

def process_sale(sales_data):
    """Processes a sale and updates inventory."""
    products = read_products()
    product_id = sales_data['product_id']
    if product_id in products and products[product_id]['stock'] >= sales_data['quantity']:
        products[product_id]['stock'] -= sales_data['quantity']
        write_products(products)
        record_sale(sales_data)
        print("Sale processed successfully.")
    else:
        print("Insufficient stock or product not found.")

def generate_sales_report():
    """Generates and prints a sales report."""
    try:
        with open(SALES_FILE, mode="r", newline='') as file:
            reader = csv.DictReader(file)
            print("Sales Report:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No sales data available.")

def generate_inventory_report():
    """Generates and prints an inventory report."""
    products = read_products()
    print("Inventory Report:")
    for product_id, details in products.items():
        print(f"ID: {product_id}, Name: {details['name']}, Stock: {details['stock']}, Price: ${details['price']}")
        if details['stock'] < 10:
            print(" - Low Stock!")

def calculate_revenue():
    """Calculates total revenue from sales data."""
    total_revenue = 0.0
    try:
        with open(SALES_FILE, mode="r", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                total_revenue += float(row['price']) * int(row['quantity'])
    except FileNotFoundError:
        print("No sales data available.")
    print(f"Total Revenue: ${total_revenue:.2f}")

def exit_system():
    """Exits the program."""
    print("Exiting the system.")
    sys.exit(0)

# ---------------- Helper Functions ----------------

def write_products(products, filename=PRODUCTS_FILE):
    """Writes product data to CSV."""
    with open(filename, mode="w", newline='') as file:
        fieldnames = ['product_id', 'name', 'price', 'stock']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product_id, details in products.items():
            writer.writerow({
                'product_id': product_id,
                'name': details['name'],
                'price': details['price'],
                'stock': details['stock']
            })

def record_sale(sales_data):
    """Records a sale to the sales CSV file."""
    with open(SALES_FILE, mode="a", newline='') as file:
        fieldnames = ['product_id', 'quantity', 'price', 'date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if os.stat(SALES_FILE).st_size == 0:  # Check if file is empty
            writer.writeheader()
        writer.writerow({
            'product_id': sales_data['product_id'],
            'quantity': sales_data['quantity'],
            'price': sales_data['price'],
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

# ---------------- User Interface ----------------

def main_menu():
    """Displays the main menu and routes the user to various functions."""
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Stock")
        print("3. Process Sale")
        print("4. Generate Sales Report")
        print("5. Generate Inventory Report")
        print("6. Calculate Revenue")
        print("7. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            product_details = {
                'product_id': input("Enter product ID: "),
                'name': input("Enter product name: "),
                'price': input("Enter product price: "),
                'stock': input("Enter initial stock level: ")
            }
            add_product(product_details)
        elif choice == '2':
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity to add/subtract: "))
            update_stock(product_id, quantity)
        elif choice == '3':
            sales_data = {
                'product_id': input("Enter product ID: "),
                'quantity': int(input("Enter quantity sold: ")),
                'price': float(input("Enter sale price: "))
            }
            process_sale(sales_data)
        elif choice == '4':
            generate_sales_report()
        elif choice == '5':
            generate_inventory_report()
        elif choice == '6':
            calculate_revenue()
        elif choice == '7':
            exit_system()
        else:
            print("Invalid option. Please choose again.")

# ---------------- Run Program ----------------
if __name__ == "__main__":
    main_menu()
