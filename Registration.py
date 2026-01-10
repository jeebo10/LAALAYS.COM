# #system student registration

from Config import get_connection
connection = get_connection()

mycursor = connection.cursor()

studentName=input("fadlad gali magaca ardayga oo dhamaystiran: ")
studentphone=input("fadlad gali telefoonkiisa: ")
studentclass=input("fadlad gali fasalka ardayga: ")
studentAddress=input("fadlad gali address-ka ardayga: ")

query = "insert into students (studentName, studentphone, studentclass, studentAddress) values (%s, %s, %s, %s)"
values = (studentName, studentphone, studentclass, studentAddress)

mycursor.execute(query, values)
connection.commit()

print(mycursor.rowcount, "ayaa la galiyay.")




