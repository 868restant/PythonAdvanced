import random
num = random.randint(1,100)
life = 0
while True:
    number = input("Veuillez saisir le numéro que vous souhaitez devinez ? ")
    life = life + 1
    number = int(number)
    if number > num:
        print("votre nombre est trop grand. ")
    elif number < num:
        print("votre nombre est trop petit. ")
    else:
        print("bravo !")
        print("vous avez utilisé " + str(life) + " chance pour trouvé le bon nombre. ")
        break