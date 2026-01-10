# import random

# number = random.randint(1,10)

# guess=int(input("fadlan geli nambarka aad u malanayso inuu ramdomka yahay, oo u dhaxeeya1 ilaa 10"))

# while guess != number :
#     guess= input(input("fadlan dib u galin numberka."))

# print("waad ku guulaysatay mahadsanid")



import random

number = random.randint(1, 10)

guess = int(input("Fadlan geli nambarka aad u malaynayso inuu randomka yahay (1 ilaa 10): "))

while guess != number:
    guess = int(input("Nambarka waa khalad. Fadlan dib u geli: "))

print("Waad ku guulaysatay mahadsanid!")


# import random

# number = random.randint(1, 10)
# attempts = 0  # Tirinta isku dayada

# print("Waxaad isku dayeysaa inaad heshid nambarka qarsoon ee u dhaxeeya 1 ilaa 10!")

# while True:
#     guess = int(input("Fadlan geli nambarkaaga: "))
#     attempts += 1

#     if guess < number:
#         print("Nambarkaagu wuu ka yar yahay nambarka qarsoon, isku day mar kale.")
#     elif guess > number:
#         print("Nambarkaagu wuu ka weyn yahay nambarka qarsoon, isku day mar kale.")
#     else:
#         print(f"Waad ku guulaysatay! Nambarku waa {number}. Waxaad isku dayday {attempts} jeer.")
#         break