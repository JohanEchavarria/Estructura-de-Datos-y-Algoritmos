import mysql.connector

conexion1=mysql.connector.connect(host="localhost",user="root",password="")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close()

import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="bd1")

cursor1=conexion1.cursor()
cursor1.execute("show tables")
for tabla in cursor1:
    print(tabla)
conexion1.close()