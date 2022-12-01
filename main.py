from distutils.log import error
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    database='project2',
    password= ''
)

def masukkan_data():
    global conn 

    print()

    data = input("Masukkan data (judul komik, penulis komik, penerbit komik)  = ").split(',')

    try:
        insert = conn.cursor()
        query = "INSERT INTO produk(judul_komik, penulis_komik, penerbit_komik) VALUES(%s,%s,%s)"
        
        value = data

        insert.execute(query, value)
        conn.commit()
        print("Data berhasil di masukkan")
        conn.close()
        

    except mysql.connector.Error as errors:
        print("Data tidak berhasil dimasukkan {}".format(errors))

def readData():
    global conn

    read = conn.cursor()
    query = "SELECT * FROM produk"

    read.execute(query)
    result = read.fetchall()

    print()

    for i in range(len(result)):
     print("=====================")
     print("id              :", result[i][0])    
     print("Judul Komik     :", result[i][1])
     print("Penulis Komik   :", result[i][2])
     print("Penerbit Komik  :", result[i][3])
     print("====================")

    conn.close()

def update_data():
    global conn
    try:   
        update  = conn.cursor()

        print()
        
        jk,pk,pek,id = input("Ubah data (judul_komik,penulis_komik,penerbit_komik,id yang ingin di ubah) = ").split(",")
        
        query= "UPDATE produk SET judul_komik=%s, penulis_komik=%s,penerbit_komik=%s WHERE id=%s"
        value = (jk,pk,pek,id)
        update.execute(query,value)
        conn.commit()
        
        print("Data berhasil di update")

        conn.close()

    except mysql.connector.Error as errors:
        print("Data tidak berhasil diupdate {}".format(errors))


def hapus_data():
    global conn

    print()

    id = input("Input Id data yang ingin anda hapus = ")

    delete=conn.cursor()
    query=("DELETE FROM produk WHERE id="+id+"")

    delete.execute(query)
    print("Data berhasil dihapus")
    conn.commit()


print("=================================")
print("APLIKASI PENGELOLAAN BUKU KOMIK")
print("=================================")
print("1. Read Data")
print("2. Insert Data")
print("3. Update Data")
print("4. Delete Data")
print("=================================")

start = int(input("Pilih 1-4 : "))

if start == 1:
    readData()
elif start == 2:
    masukkan_data()
elif start == 3:
    update_data()
elif start == 4:
    hapus_data()
else:
    print("Pilihanmu tidak tersedia kawan!")



