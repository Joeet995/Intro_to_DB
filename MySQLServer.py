import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "yousseftarek95",
    password = "2597",
    )

mycursor = mydb.cursor()

mycursor.execute("CREAT DATABASE IF NOT EXISTS alx_book_store")

print("Database 'alx_book_store' created successfully!")