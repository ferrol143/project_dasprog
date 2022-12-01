import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password= ''
)

mycoon= conn.cursor()
mycoon.execute("CREATE DATABASE project2")

print("berhasil")