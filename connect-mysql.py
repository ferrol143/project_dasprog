import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password= ''
)

if conn.is_connected():
    print("konek")
else:
    print("tidak terkoneksi")