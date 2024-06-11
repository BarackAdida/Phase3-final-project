from config import conn
from purchases import Purchases
from products import Products
from vendors import Vendor

# Create the tables
Purchases.create_table()
Products.create_table()
Vendor.create_table()
# Purchases.alter_purchases()
# Insert data into the Vendors table
# Vendor.insert_vendor("Lapilly Barack", "0100699066")

# Insert data into the Products table
# Products.insert_product("Red Beryl", "The cool one,shines", 8000000, 180)

conn.close()


