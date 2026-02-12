import mysql.connector
import os


sql_host = os.getenv("SQL_HOST","localhost")
sql_user = os.getenv("SQL_USER","root")
sql_password = os.getenv("SQL_PASSWORD","password")
sql_db_name = os.getenv("SQL_DB_NAME","mydatabase")

conn = mysql.connector.connect(host=sql_host,user=sql_user,password=sql_password,database=sql_db_name)
mycursor = conn.cursor()