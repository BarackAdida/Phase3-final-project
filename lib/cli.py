# cli.py

import argparse
from products import Products
from vendors import Vendor
from purchases import Purchases

def add_purchase():
    # Prompt for purchase details
    product_id = int(input("Enter product ID: "))
    purchase_id = int(input("Enter purchase ID: "))
    vendor_id = int(input("Enter vendor ID: "))
    purchaser = input("Enter purchaser: ")
    
    # Add the purchase to the Purchases table
    Purchases.insert_purchase(product_id, purchase_id, vendor_id, purchaser)
    print("Purchase added successfully.")

def add_vendor():
    # Prompt for vendor details
    name = input("Enter vendor name: ")
    contact_info = input("Enter vendor contact info: ")
    
    # Add the vendor to the Vendors table
    Vendor.insert_vendor(name, contact_info)
    print("Vendor added successfully.")

def add_product():
    # Prompt for product details
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    
    # Add the product to the Products table
    Products.insert_product(name, description, price, quantity)
    print("Product added successfully.")

def main():
    # Prompt for user's name
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")

    # Prompt for action
    print("What would you like to do?")
    print("1. Add a purchase")
    print("2. Add a vendor")
    print("3. Add a product")
    choice = int(input("Enter your choice (1/2/3): "))

    # Perform action based on user's choice
    if choice == 1:
        add_purchase()
    elif choice == 2:
        add_vendor()
    elif choice == 3:
        add_product()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
