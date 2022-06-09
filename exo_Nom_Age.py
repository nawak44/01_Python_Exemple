print("Bonjour, ici mon premier exercie en python")

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "" :
        reponse_nom = input("quel est votre nom? ")
    return reponse_nom


def demander_age(nom):
    age_int = -1
    while age_int == -1:
        age_str = input("Bonjour"+nom+"quel est votre age? ")
        try:
            age_int = int(age_str)
        except:
            print("mauvaise saisie")
    return age_int


def afficher_resultat(nom,age):
    if age > 1 :
        print("votre nom est " + nom + " et votre age est de " + str(age) + " ans")
    else :
        print("votre nom est " + nom + " et votre age est de " + str(age) + " an")
    print("l'an prochain tu auras " + str(age+1) + " ans")


nom = demander_nom()
age = demander_age(nom)
afficher_resultat(nom,age)

