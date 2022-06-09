
###############################################################################
###############################################################################
######################### Programme Main ######################################

print('bonjour premier script python')
print("c'est un calcul d'IMC")
poids = float(input("entrez votre poids (en kg): "))
taille = float(input("entrez votre taille (en mm): "))
IMC = poids/taille**2
IMC = IMC*10000
print("votre IMC est ", IMC)
if IMC < 18.5:
    print("IMC trop bas : ", IMC)
elif 18.5 <= IMC <= 25:
    print("IMC correct : ", IMC)
elif IMC >= 25:
    print("IMC trop haut : ", IMC)
else:
    print("aucun  calcul d'IMC...")
