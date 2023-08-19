import random
money = 10000
for i in range(1,21):
    solde = random.randint(1,10)
    if money == 0:
        print("nous avons plus de salaire, donc nous l'aurons le mois prochain ")
        break
    if solde <= 5 :
        print("employer " + str(i) + " le score de performance est " + str(solde) + " , " + str(solde) +
              " et en dessous de 5 donc pas de salaire")
    else:
        money = money - 1000
        print("verser a l'employer " + str(i) + " un salaire de 1000$ ce qui laise " + str(money) + "$ sur le compte")
if money > 0:
    print("il vous reste " + str(money) + "$ sur votre compte vous pouvez "
                                          " acheter a manger et a boire donc vous n'etes pas pauvres")
if money == 0:
    print("il vous restes " + str(money) + "$ sur votre compte vous pouvez " 
                                           " pas acheter a manger et a boire donc vous devener pauvre ")




