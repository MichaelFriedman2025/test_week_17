mycursor.execute("""use mydatabase;
#                     CREATE TABLE IF NOT EXISTS orders( 
#                         orderNumber int ,
#                         orderDate varchar(255),
#                         requiredDate varchar(255),
#                         shippedDate varchar(255),
#                         status varchar(255),
#                         comments varchar(255),
#                         customerNumber int )""")


# mycursor.execute("""use mydatabase;
#                     CREATE TABLE IF NOT EXISTS costumer(
#                         customerNumber int
#                         customerName varchar(255),
#                         contactLastName varchar(255),
#                         contactFirstName varchar(255),
#                         phone varchar(255),
#                         addressLine1 varchar(255),
#                         addressLine2 varchar(255),
#                         city varchar(255),
#                         state varchar(255),
#                         postalCode varchar(255),
#                         country varchar(255),
#                         salesRepEmployeeNumber varchar(255),
#                         creditLimit float)""")