print("bienvenue au zoo")
if int(input("veuillez indiquer votre taille(cm):")) > 120:
    print("vous meusurez plus de 120 cm et n'est pas autorisé a jouer gratuitement")
    print("cependant,si votre niveau VIP est supérieur a 3 vous pouvez jouer gratuitement")
    if int(input("veuillez entrer votre niveau VIP(1~5):")) > 3:
        print("votre niveau VIP est supérieur a 3 vous pouvez jouer gratuitement.")
    else:
        print("désolé, toutes les conditions ne sont pas remplies et un billet est nécessaire pour 10euros")
else:
    print("bonne visite")
