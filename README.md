# Inventory system

This is a system that manages the inventory of a business shop that deals in selling different minrrals. it comprises of three main tables:

Products table
this is the main table in the system that stores information about the items in the store, it is not in read-only since one can still add data of a good or commodity that he/she is interestedin.

Vendors Table
this is a table that contains information about the vendors in the store. The main purpose of this table is to contain the vendors_id which is later used in the purchase table to add a vendors who gave services to the customers.

Purchase table
this is the most flexible table, if a purchase is made, datais stored in this table

Relationships
There is a relationship between vendor_id in the vendors table and vendors_id in the purchases table, it is a one to many relationship since one vendor can sell many items to the customers

Language
python

Other used techs:
sqlite3
Argpase
