liste_nombres = [1, 6, 98, 52, 1045, 3]
liste_nombres.sort()
# 1) classez la liste
print(liste_nombres)
# 2) supprimez le premier élément de la liste
liste_nombres.remove(1)
# 3) ajoutez le nombre "1097" à la fin de la liste
liste_nombres.append(1097)
# 4) récupérez le deuxième élément dans une variable "deuxieme_element"
deuxieme_element = liste_nombres[1]
print(deuxieme_element) # la console devrait afficher "6" !

# 5) affichez la longueur de la liste
print(len(liste_nombres))

print(liste_nombres)