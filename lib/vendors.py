# lib/vendors.py

from config import conn, cursor

class Vendor:
    def __init__(self, vendor_id, name, contact_info):
        self.vendor_id = vendor_id
        self.name = name
        self.contact_info = contact_info

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS Vendors (
            vendor_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            contact_info TEXT
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS Vendors;
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def insert_vendor(cls, name, contact_info):
        sql = """
            INSERT INTO Vendors (name, contact_info) VALUES (?, ?)
        """
        cursor.execute(sql, (name, contact_info))
        conn.commit()
