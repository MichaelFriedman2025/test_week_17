import mysql.connector
import os


sql_host = os.getenv("SQL_HOST","localhost")
sql_user = os.getenv("SQL_USER","root")
# sql_password = os.getenv("SQL_PASSWORD","1234")

mydb = mysql.connector.connect(host=sql_host,user=sql_user)
mycursor = mydb.cursor()