import math


###############################################################################
###############################################################################
######################### Programme Main ######################################

print("calcul pythagore")
a = int(input("entrer la valeur du petit coté : "))
b = int(input("entrez la valeur du grand coté : "))
a = a*a
b = b*b
c = a+b
d = math.sqrt(c)
print("l'hypothenuse est de : ", d)
