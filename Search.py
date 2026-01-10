# from Config import get_connection

# connection = get_connection()
# mycursor = connection.cursor()

# keyword = input("Fadlan gali magaca qofka aad baadhayso: ")

# query = "SELECT * FROM students WHERE studentName LIKE %s"

# mycursor.execute(query, ("%" + keyword + "%",))

# for x in mycursor:
#     print(x)




from Config import get_connection
connection = get_connection()

mycursor = connection.cursor()

keyword =input(print("Fadlan gali magaca qofka aad baadhayso:"))

query = "select * from students where studentName like %s"

mycursor.execute(query, ("%{}%" .format(keyword),))

for x in mycursor:
    print(x)

