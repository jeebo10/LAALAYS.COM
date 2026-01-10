# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user= "root",
#     password= "!@#$%asd!1"

# )



# mycursor =mydb.cursor()
# mycursor.execute("create database Orbitdb")




import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user= "root",
    password="!@#$%asd!1"
)


mysqlcursor =mydb.cursor()
mysqlcursor.execute("create database schoolHormoondb")