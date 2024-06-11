# lib/config.py

import sqlite3

# Establish connection to the database
conn = sqlite3.connect("db/inventory.db")
cursor = conn.cursor()
