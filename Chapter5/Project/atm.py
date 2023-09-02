name = input("veuillez entrer votre nom ")
money = 5000000
def query():
    print("bonjour il vous reste un solde de "+str(money) + " euros")
def saving():
    print("combien voulez-vous économiser ?")
    solde = int(input("veuillez entrer"))
    print("------dépot-------")
    print(str(name), " bonjour, votre dépot de " + str(solde) + " euros a été accepté")
    global money
    money = solde + money
    print(str(name) + " bonjour, il vous reste un solde de " + str(money) + " euros")
def get_money():
    print("combien voulez vous retirer?")
    solde = int(input("veuillez entrer"))
    print("----------retraits----------")
    print(str(name), " bonjour, votre retrait de " + str(solde) + " euros a été accepté")
    global money
    money = money - solde
    print(str(name) + " bonjour, il vous reste un solde de " + str(money) + " euros")
    choose_category()
    return
def main():
    print("sortie du programme")


def welcome():
    print("bonjour " + str(name) + " bienvenue à ATM veuillez selectionner l'opération")

def choose_category():
    print("------menue principal--------")
    print(' vérifiez le solde [1] \n'
        'dépots [2] \n'
        'retraits [3] \n'
        'sortie [4]\n')
    choose = input("veuillez entrez votre choix")
    if choose == '1':
        query()
        choose_category()
        return
    if choose == '2':
        saving()
        choose_category()
        return
    if choose == '3':
        get_money()
        choose_category()
        return
    if choose == '4':
        return

welcome()
choose_category()

