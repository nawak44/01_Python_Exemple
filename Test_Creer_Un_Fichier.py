

def creationFichier():
    nomFichier = input("quel nom veux tu pour le fichier?")
    fichier = open(nomFichier+".txt", "a")
    #fichier.write("Bonjour monde")
    fichier.close()
    return nomFichier


def ecritureFichier(nomFichier):
    temp = open(fichier+".txt", "a")
    note = input("que voulez vous écrire?")
    temp.write(note)
    temp.close()

###############################################################################
###############################################################################
######################### Programme Main ######################################


print("création d'un fichier avec Python")
fichier = creationFichier()
ecritureFichier(fichier)
