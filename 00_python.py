from audioop import reverse


nom = input("Quel est votre Nom?")
print("Vous vous appelez : " + nom)
print(f"Vous vous appelez : {nom}")
print("Vous vous appelez : %s" % nom)
print("Vous vous appelez : ", nom)

# Boucle While ; Boucle tant que la Condition est vraie
age = ""
while age == "":
    age = input("quel est votre age ?")

# Boucle For ; Boucle un certain nombre de fois
for i in range(0, 4):  # enumere toute les cases de 0 à 3
    print(i)

# Inverser une Chaine


def reverse_string1():
    reverse = ""
    for caractere in str:
        reverse = caractere + reverse
        return reverse


def reverse_string2():
    s = str
    return s[::-1]
# [debut : fin : pas][1:4:2]
# commence le tableau au caractere en position 0
# fini en position 7 passe de 2 en 2
