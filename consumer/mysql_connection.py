import mysql.connector
import os

sql_host = os.getenv("SQL_HOST","localhost")
sql_user = os.getenv("SQL_USER","root")
sql_password = os.getenv("SQL_PASSWORD","password")
sql_db_name = os.getenv("SQL_DB_NAME","mydatabase")

conn = mysql.connector.connect(host=sql_host,user=sql_user,database=sql_db_name)

mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("""use mydatabase;
                    CREATE TABLE IF NOT EXISTS orders( 
                        orderNumber int ,
                        orderDate varchar(255),
                        requiredDate varchar(255),
                        shippedDate varchar(255),
                        status varchar(255),
                        comments varchar(255),
                        customerNumber int )""")

mycursor.execute("""use mydatabase;
                    CREATE TABLE IF NOT EXISTS customer(
                        customerNumber int
                        customerName varchar(255),
                        contactLastName varchar(255),
                        contactFirstName varchar(255),
                        phone varchar(255),
                        addressLine1 varchar(255),
                        addressLine2 varchar(255),
                        city varchar(255),
                        state varchar(255),
                        postalCode varchar(255),
                        country varchar(255),
                        salesRepEmployeeNumber varchar(255),
                        creditLimit float)""")

def insert_data_to_orders_table(data):
    sql = """
    INSERT INTO orders (orderNumber, orderDate, requiredDate,shippedDate,status,comments,customerNumber)
    VALUES (%s,%s,%s,%s,%s,%s,%s);
    """
    for row in data:
        value = int(row["orderNumber"]),row["orderDate"],row["requiredDate"],row["shippedDate"],row["status"],row["comments"],int(row["customerNumber"])
        mycursor.execute(sql,value)

def insert_data_to_customers_table(data):
    sql = """
    INSERT INTO orders (customerNumber, customerName, contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    """
    for row in data:
        value = int(row["customerNumber"]),row["customerName"],row["contactLastName"],row["contactFirstName"],row["phone"],row["addressLine1"],row["addressLine2"],row["city"],row["state"],row["postalCode"],row["country"],row["salesRepEmployeeNumber"],row["creditLimit"]
        mycursor.execute(sql,value)