# Trouver mot le plus long

#definitions Fonctions
def get_min_max_words(phrase):
    mot = phrase.split(" ") # split(" ") entre "" est le caractere séparateur
    min_mot = min(mot, key=len)
    max_mot = max(mot, key=len)
    return (min_mot, max_mot)

# debut programme
sentense = "un chasseur sachant chasser sans son chien"

# def variable et utilisation Fonction
min_word, max_word = get_min_max_words(sentense)

print("Mot le plus petit" + str(min_word))
print("Mot le plus long" , max_word)
