from config import conn, cursor

class Purchases:
    def __init__(self, product_id, purchase_id, vendor_id):
        self.product_id = product_id
        self.purchase_id = purchase_id
        self.vendor_id = vendor_id

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS Purchases (
            product_id INTEGER,
            purchase_id INTEGER,
            vendor_id INTEGER,
            FOREIGN KEY (product_id) REFERENCES Products(product_id),
            FOREIGN KEY (vendor_id) REFERENCES Vendors(vendor_id)
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS Purchases;
        """
        cursor.execute(sql)
        conn.commit()
