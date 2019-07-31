import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "sachin"
    passwd = "sachin",
)
print(mydb)
