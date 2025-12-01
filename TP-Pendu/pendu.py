import random

mots = "pointu raser ruisseau pastorale chiens cadre meteorite effacer naissance facteur"

# sélectionner un mot aléatoire de la liste de mots
liste_de_mot = mots.split()

# Récupérer le mot à trouver à partir d'un nombre random
secret = random.randint(0, len(liste_de_mot) - 1)
secret_word = liste_de_mot[secret]

# Garder les informations liées aux jeu dans un dictionnaire
game = {
    "secret_word": secret_word,
    "guess_word": "_" * len(secret_word),
    "life": 9
}

# début du jeu
print(f"{game['guess_word']} | vie : {game['life']}")

while True:
    # demander au joueur d'entrer une lettre
    lettre = input("Entrez une lettre > ")

    # Si la lettre est dans le mot, on gère l'affichage du mot secret, sinon on enlève une vie
    if lettre in game["secret_word"] and lettre not in game["guess_word"]:
        guess_word_liste = list(game["guess_word"])
        for index, current_letter in enumerate(game["secret_word"]):
            if current_letter == lettre:
                guess_word_liste[index] = lettre
        game["guess_word"] = "".join(guess_word_liste)

    elif lettre not in game["secret_word"]:
        game["life"] -= 1

    print(f"{game['guess_word']} | vie : {game['life']}")

    # si le mot secret n'a plus de _ le joureur a gagné
    if "_" not in game["guess_word"]:
        print("Gagné !")
        break

    # si le nombre de vie est à 0, le joueur a perdu
    elif game["life"] < 1:
        print("Perdu !")
        print(f"Le mot secret était : {game["secret_word"]} !")
        break


