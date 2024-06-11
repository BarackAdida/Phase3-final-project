# lib/products.py

from config import conn, cursor

class Products:
    def __init__(self, product_id, name, description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS Products(
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER,
            quantity INTEGER
            )
        """

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS Products;
        """
        
        cursor.execute(sql)
        conn.commit()
