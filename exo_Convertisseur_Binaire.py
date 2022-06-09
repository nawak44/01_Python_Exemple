###############################################################################
# se programme sert a convertir un octet en valeur décimal et hexacedimal
# mais python propose deja de base des fonctions capable de le faire
###############################################################################

import math

# teste si le nombre de caractere est bien de 2bits, 4bits, 8bits, 16bits, 32bits
# ne prend pas encore 64bits a cause de nos processeurs limitée pour le moment a 64bits


def test_longueur(valeur):
    carreDeDeux = math.log(len(valeur), 2)
    if carreDeDeux.is_integer() and len(valeur) < 64:
        return True

    print("Le nombre de bits n'est pas bon.")
    return False

# teste si tous les caracteres sont bien dans la Base 2
# donc en binaire 0 ou 1


def test_maxime(bytes):
    for element in bytes:
        # Element est un string, il faut le convertir en int
        elementInt = int(element)
        if elementInt != 0 and elementInt != 1:
            print("La valeur d'un bit n'est pas '0' ou '1'")
            # Ce n'est pas bon, on sort de la boucle et on return false
            return False
    # On a fait tout le tableau, c'est bon
    return True

########## Fonction calcul ##########
# fait le calcul pour chaque Bits avec sa puissance de 2


def convertir_en_decimal(octet):
    i = 0
    resultat = 0
    multiplicateur = 2**(len(octet)-1)
    for bit in octet:
        bit_en_entier = int(bit)
        resultat += bit_en_entier*multiplicateur
        i += 1
        multiplicateur = multiplicateur/2

    return int(resultat)


def ask_input():
    is_valid = False

    while not is_valid:
        binaire = input(
            "Entrez votre octet en binaire : ").strip().replace(' ', '')
        # strip nettoie les espace et les a la ligne de chaque coté du mot
        # replace(caractere_a_remplacer,caractere_a_mettre_a_la_place)
        is_valid = test_longueur(binaire) and test_maxime(binaire)

    return binaire

###############################################################################
###############################################################################
######################### Programme Main ######################################


print("Convertisseur d'octet Binaire en décimal et Hexadecimal.")
binaire = ask_input()
decimal = convertir_en_decimal(binaire)
print("La valeur de l'octet ", binaire, " en décimal est ",
      decimal, " et en hexa ", hex(decimal))
