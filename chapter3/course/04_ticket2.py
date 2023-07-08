print("bienvenu au zoo!")
height =int(input("veuillez idiquer votre taille (cm):"))
vip_level =int(input("veuillez entrer votre niveau VIP(1~5)"))
day =int(input("veuillez entrer la date du jour(1~31)"))
if height < 120:
    print("vous pouvez jouer gratuitement si vous mesurez moins de 120cm")
elif vip_level > 3:
    print("votre niveau vip est supérieur a 3 et pouvez jouez gratuitrmrnt.")
elif day==1:
    print("aujourd'hui le premier jour libre pour visite")
else:
    print("désolé,toutes les conditions ne sont pas remplies et un billet est nécessaire pour 10euros.")

print("Bonne visite")