import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="!@#$%asd!1",
    database="orbitdb"
)

mysqlcursor =mydb.cursor()

mysqlcursor.execute("create Table students (studentId int Auto_increment primary key, studentName varchar(255), studentPhone int(16), studentClass varchar(50), studentAddress varchar(100))")


















