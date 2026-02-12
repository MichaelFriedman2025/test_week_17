from connection import mycursor


def ten_costumers_with_high_order():
    res = mycursor.execute("""
        SELECT c.customerName, c.customerNumber FROM customers c
        JOIN orders o
        ON c.customerNumber = o.customerNumber
    """)
