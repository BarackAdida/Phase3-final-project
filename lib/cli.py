import argparse
from products import Products
from vendors import Vendor
from purchases import Purchases

def add_purchase():
    product_id = int(input("Enter product ID: "))
    purchase_id = int(input("Enter purchase ID: "))
    vendor_id = int(input("Enter vendor ID: "))
    purchaser = input("Enter purchaser: ")

    Purchases.insert_purchase(product_id, purchase_id, vendor_id, purchaser)
    print("Purchase added successfully.")

def add_vendor():
    name = input("Enter vendor name: ")
    contact_info = input("Enter vendor contact info: ")
    
    Vendor.insert_vendor(name, contact_info)
    print("Vendor added successfully.")

def add_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    
    Products.insert_product(name, description, price, quantity)
    print("Product added successfully.")

def view_table(table_name):
    if table_name == "products":
        Products.display_products()
    elif table_name == "vendors":
        print("Vendor table is not available.")
    elif table_name == "purchases":
        Purchases.display_purchases()
    else:
        print("Invalid table name.")

def main():
    parser = argparse.ArgumentParser(description="Inventory Management System")
    parser.add_argument("--view", metavar="table_name", help="View a table (products/vendors/purchases)")
    args = parser.parse_args()

    if args.view:
        view_table(args.view)
    else:
        user_name = input("Enter your username: ")
        print(f"Welcome, {user_name}!")

        print("What would you like to do?")
        print("1. Add a purchase")
        print("2. Add a vendor")
        print("3. Add a product")
        print("4. View a table")
        choice = int(input("Enter your choice (1/2/3/4): "))

        # Perform action based on user's choice
        if choice == 1:
            add_purchase()
        elif choice == 2:
            add_vendor()
        elif choice == 3:
            add_product()
        elif choice == 4:
            table_name = input("Enter table name (products/vendors/purchases): ")
            view_table(table_name)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
