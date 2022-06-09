# 1) Créez une variable de type dictionnaire appelée "chaussure"
chaussure = {}
""" 2) Ajoutez les éléments suivants dans le dictionnaire :
   - clef "taille" avec la valeur 42
   - clef "marque" avec la valeur "Nike"
   - clef "race" avec la valeur "berger-allemand"
"""
chaussure['taille'] = 42
chaussure['marque'] = "nike"
chaussure['race'] = "berger-allemand"

print(chaussure)
# 3) On s'est trompés ! Supprimez la clef "race" du dictionnaire :)
del chaussure['race']
chaussure.pop('race')

# 4) Récupérez la taille de la chaussure dans une variable appelée "taille"
taille = chaussure['taille']
print(f"La taille de la chaussure est {taille}")  # 42 normalement !