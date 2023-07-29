"""
import random
n = random.randint(0,100)
vies =>0
appreciation = "?"
while vies > '':
    var = input("Entrez un nombre")
    var = int(var)
    if var < n :
        appreciation = "trop bas"
        print(vies, var, appreciation)
    else :
        appreciation = "trop haut"
        print(vies, var, appreciation)
    if var == n:
        appreciation = "bravo !"
        print(vies, var, appreciation)
        break

    vies -= 1
"""

import random
num = random.randint(1,100)
life = 0
while True :
    nombre = input("Entrez un nombre")
    life = life + 1
    nombre = int(nombre)
    if nombre < num :
        print("votre nombre est trop bas")
    else :
        print("votre nombre est trop haut")

    if nombre == num:
        print("bravo !")
        print("vous avez utilisé " + str(life) + " chance pour trouvé le bon nombre")
        break
