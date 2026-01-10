from Config import get_connection
connection = get_connection()

cursor = connection.cursor()
cursor.execute("select * from students")
results = cursor.fetchall()

for x in results:
    print(x)