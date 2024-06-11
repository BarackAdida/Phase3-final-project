# lib/script.py

from config import conn
from purchases import Purchases
from products import Products
from vendors import Vendor 

# Create the Purchases table
Purchases.create_table()

# Create the Products table
Products.create_table()

# Create the Vendor table
Vendor.create_table()

# Close the connection when done
conn.close()
