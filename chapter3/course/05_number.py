num = 5

number = int(input("veuillez devinez un numero :"))
if number == num:
    print("felicitation")
else:
    number = int(input("veuillez devinez un numero :"))
    if number % num:
        print("mauvaise reponse encore une fois ")
else:
    print("felicitation pour votre bonne reponse")

    number = int(input("veuillez devinez un numero :"))
    if number % num:
        print("mauvaise reponse encore une fois")

    number = int(input("veuillez devinez un nombre "))
    if number % num:
        print("mauvaise reponse encore une fois")
else:
    print("vous avez mal devine")
print("mauvaise reponse encore une fois ")



