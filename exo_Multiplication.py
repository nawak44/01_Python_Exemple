# Importation
import random

# Fonction


def faireCalcul():
    compteur = 0
    while compteur < 5:
        a = random.randrange(11)
        b = random.randrange(11)
        c = a*b
        d = -1
        compteur += 1
        while c != d:
            print("combien font ", a, "*", b, "? ")
            d = int(input())
            if c != d:
                print("c'est une erreur, recommence")
    else:
        rep = (input("c'est bon, on refait une partie ? y/n "))
        return rep

###############################################################################
###############################################################################
######################### Programme Main ######################################


print("....")
print("Programme de jeux Mathematique")
rep = input("On fait une partie? y/n ")
while rep == 'y':
    rep = faireCalcul()
else:
    print("")
    print("Kenavo")
