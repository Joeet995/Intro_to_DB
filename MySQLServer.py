import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "yousseftarek95",
    passwd = "1234",
    database = "alx_book_store"
    )

print("Database 'alx_book_store' created successfully!")