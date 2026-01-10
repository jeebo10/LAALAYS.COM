import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="!@#$%asd!1",
        database="orbitdb"
    )
    
    return connection


