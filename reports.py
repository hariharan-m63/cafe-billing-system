import pymysql

class reports:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", password="****", database="project")

    def daily_report(self):
        cursor = self.conn.cursor()

        date = input("Enter date (YYYY-MM-DD): ")

        q = """
            SELECT product_id, product_name, SUM(quantity), SUM(total)
            FROM orders
            WHERE DATE(date) = %s
            GROUP BY product_id, product_name
        """

        cursor.execute(q, (date,))
        results = cursor.fetchall()

        print("\n--- Daily Sales Report ---")
        print("Product ID | Name | Total Qty | Total Amount")
        print("-" * 50)

        grand_total = 0

        for row in results:
            print(row[0], "|", row[1], "|", row[2], "|", row[3])
            grand_total += row[3]

        print("\nGrand Total =", grand_total)

        cursor.close()

    def monthly_report(self):
        cursor = self.conn.cursor()

        year = input("Enter year (YYYY): ")
        month = input("Enter month (MM): ")

        q = """
            SELECT product_id, product_name, SUM(quantity), SUM(total)
            FROM orders
            WHERE YEAR(date) = %s AND MONTH(date) = %s
            GROUP BY product_id, product_name
        """

        cursor.execute(q, (year, month))
        results = cursor.fetchall()

        print("\n--- Monthly Sales Report ---")
        print("Product ID | Name | Total Qty | Total Amount")
        print("-" * 50)

        grand_total = 0

        for row in results:
            print(row[0], "|", row[1], "|", row[2], "|", row[3])
            grand_total += row[3]

        print("\nGrand Total =", grand_total)

        cursor.close()