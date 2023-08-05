sentence = "Alex est vraiment très beau"
number = 0
for element in sentence:
    if element == 'a':
        number = number + 1
print("il y a " + str(number) + " a dans la chaine qui est comptée. ")
