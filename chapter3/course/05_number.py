num = 5

number = int(input("veuillez devinez un numero :"))
if number == num:
    print("felicitation")

else:
    print("mauvaise reponse encore une fois ")
    number = int(input("veuillez devinez un numero :"))
    if number == num:
        print("felicitation")
    else:
        print("mauvaise reponse encore une fois ")
        number = int(input("veuillez devinez un numero :"))
        if number == num:
            print("felicitation")
        else:
            print("désolé, vous avez mal deviné")




