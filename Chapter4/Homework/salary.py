import random
money = 10000
for i in range(1,21):
    level = random.randint(1,10)
    if money == 0:
        print("nous avons plus de salaire, donc nous l'aurons le mois prochain ")
        break
    if level <= 5 :
        print("employer " + str(i) + " le score de performance est " + str(level) + " , " + str(level) +
              " et en dessous de 5 donc pas de salaire")
    else:
        money = money - 1000
        print("verser a l'employer " + str(i) + " un salaire de 1000$ ce qui laise " + str(money) + "$ sur le compte")




