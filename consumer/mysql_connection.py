import mysql.connector
import os

sql_host = os.getenv("SQL_HOST","localhost")
sql_user = os.getenv("SQL_USER","root")
sql_password = os.getenv("SQL_PASSWORD","password")
sql_db_name = os.getenv("SQL_DB_NAME","mydatabase")

conn = mysql.connector.connect(host=sql_host,user=sql_user,database=sql_db_name)

mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("""
                CREATE TABLE IF NOT EXISTS orders( 
                orderNumber INT ,
                orderDate varchar(255),
                requiredDate varchar(255),
                shippedDate varchar(255),
                status varchar(255),
                comments varchar(255),
                customerNumber INT)""")


mycursor.execute("""
                CREATE TABLE IF NOT EXISTS costumer(
                customerNumber INT
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
                creditLimit FLOAT)""")