name = 'alex'
address = 'paris'
age = 18
height = 1.83
print("je m'appelle " + name + " j'habite à " + address + " et j'ai " + str(age) + 'ans')
print("je m'appelle %s . j'habite à %s et j'ai %d ans . " % (name,address,age))
print("je m'appelle %s.j'ai %d ans et je mesure %.2f m." % (name,age,height))

print(f"je m'appelle {name}, j'ai {age} ans et je mesure {height} m.")

print("le résultat de 1 + 1 est: %d" % (1*1))
print(f"le résultat de 1 + 1 est:{1*1}")
print("le type de chaine en Python est: %s" %type('chaine'))