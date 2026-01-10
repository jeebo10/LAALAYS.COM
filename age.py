# import datetime

# def age_calculator(birth_year):
#     today = datetime.date.today()
#     age = today.year - birth_year
#     return age

# year = int(input("fadlan gali sanadka aad dhalatay."))
# month = int(input("gali bisha aad dhalatay."))
# day = int(input("gali maalinta aad dhalatay."))
# birth_date = (datetime.date(year,month,day))


# sanadka = age_calculator(birth_date)

# print("waxaad jirtaa " + str(sanadka) +" sanadood")



import datetime

def age_calculator(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

year = int(input("Fadlan geli sanadka aad dhalatay: "))
month = int(input("Geli bisha aad dhalatay: "))
day = int(input("Geli maalinta aad dhalatay: "))

birth_date = datetime.date(year, month, day)

sanadka = age_calculator(birth_date)

print("Waxaad jirtaa " + str(sanadka) + " sano")
































# import datetime

# def age_calculator(birth_date):
#     today = datetime.date.today()
#     age = today.year - birth_date.year

#     if (today.month, today.day) < (birth_date.month, birth_date.day):
#         age -= 1

#     return age

# year = int(input("Fadlan geli sanadka aad dhalatay: "))
# month = int(input("Geli bisha aad dhalatay: "))
# day = int(input("Geli maalinta aad dhalatay: "))

# birth_date = datetime.date(year, month, day)

# sannadka = age_calculator(birth_date)

# print("Da'daadu waa:", sannadka)

















