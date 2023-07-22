'''
import random
random_number = random.randint(1, 10)
count = 0
while True:
    if count == 3:
        print("Game over, vous avez échoué!")
        break
    number = int(input("Veuillez entrer un nombre: "))
    count = count + 1
    if number < random_number:
        print("votre nombre est trop petit.")
    elif number > random_number:
        print("votre nombres est trop grand.")
    else:
        print("Vous avez bien deviné le nombre et vous avez deviné " + str(count) + " fois au total")
        break
'''
import random
num = random.randint(1,10)

number = int(input("veuillez devinez un numero :"))
if number < num :
    print("votre nombre est trop petit")
if number > num :
    print("votre nombre est trop grand")
if number == num:
    print("felicitation")

else:
    print("mauvaise reponse encore une fois ")
    number = int(input("veuillez devinez un numero :"))
    if number > num :
        print("votre nombre est trop grand")
    if number < num:
        print("votre nombre est trop petit")
    if number == num:
        print("felicitation")
    else:
        print("mauvaise reponse encore une fois ")
        number = int(input("veuillez devinez un numero :"))
        if number < num :
            print("votre nombre est trop petit")
        if number > num :
            print("votre nombre esr trop grand")
        if number == num:
            print("felicitation")
        else:
            print("vous avez épuiser vos trois chance, est vous n'avez pas deviné le bon nombre")

