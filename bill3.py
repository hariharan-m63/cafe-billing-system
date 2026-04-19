import pymysql
import csv
from datetime import datetime

class billing:
    def __init__(self):
        self.conn = pymysql.connect( host="localhost",user="root",password="****",database="project")

    def generate_bill(self):
        cursor = self.conn.cursor()

        cart = []
        grand_total = 0
        order_id = datetime.now().strftime("%Y%m%d%H%M%S")

        while True:
            product_id = input("Enter Product ID: ")
            qty = int(input("Enter Quantity: "))

            # Fetch product details
            query = "SELECT product_name, price, quantity FROM items WHERE product_id=%s"
            cursor.execute(query, (product_id,))
            result = cursor.fetchone()

            if result is None:
                print("Product not found!")
                continue

            name, price, stock = result

            if qty > stock:
                print("Insufficient stock!")
                continue

            total = price * qty
            grand_total += total

            cart.append([order_id, product_id, name, price, qty, total])

            # Update stock
            update_q = "UPDATE items SET quantity=%s WHERE product_id=%s"
            cursor.execute(update_q, (stock - qty, product_id))

            # Insert into orders table
            order_q = """
                INSERT INTO orders(order_id, product_id, product_name, price, quantity, total, date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(order_q, (
                order_id, product_id, name, price, qty, total,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))

            self.conn.commit()

            ch = input("Add more items? (y/n): ")
            if ch.lower() != 'y':
                break

        # Generate CSV bill
        filename = f"bill_{order_id}.csv"

        with open(filename, "w",newline="") as f:
            writer = csv.writer(f)

            writer.writerow(["Order ID", "Product ID", "Name", "Price", "Qty", "Total"])
            writer.writerows(cart)
            writer.writerow([])
            writer.writerow(["Grand Total", " = ", grand_total])

        print("\nBill Generated:", filename)
        print("Order ID:", order_id)
        print("Grand Total =", grand_total)

        cursor.close()