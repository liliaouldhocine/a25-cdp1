# ÉNONCÉ — Jeu du mot secret (type “Pendu”) en POO + modules + packages

## Contexte

Vous avez reçu une version du jeu écrite dans **un seul fichier**. https://github.com/liliaouldhocine/a25-cdp1/blob/main/TP-Pendu/pendu.py
Votre mission est de transformer ce code en un projet Python bien organisé, utilisant :

- un **package** (dossier Python)
- plusieurs **modules** (fichiers `.py`)
- la **programmation orientée objet (POO)**

---

## Objectifs pédagogiques

À la fin, vous devez être capables de :

1. structurer un projet Python en plusieurs fichiers
2. créer et utiliser des **classes**
3. isoler la logique du jeu (règles) de l’interface (console)
4. importer correctement depuis un package

---

## Fonctionnement attendu du jeu (identique à la version donnée)

- Un mot secret est choisi aléatoirement dans une liste.
- Le joueur entre une lettre à chaque tour.
- Si la lettre est dans le mot, elle apparaît dans le mot “deviné”.
- Sinon, le joueur perd 1 vie.
- Le joueur gagne quand il n’y a plus de `_`.
- Le joueur perd quand les vies tombent à 0.
- Le jeu affiche après chaque tour :
  - le mot deviné (ex: `_a__e`)
  - les vies restantes

---

## Structure obligatoire du projet

Votre projet doit respecter cette structure :

```
pendu/
├── main.py
└── hangman/
    ├── __init__.py
    ├── words.py
    ├── game_state.py
    ├── game.py
    └── ui.py
```

---

## Rôle de chaque module (obligatoire)

### 1) `words.py`

**Responsabilité : gérer la source de mots**

- contenir la liste de mots (ou une chaîne de mots)
- fournir une fonction (ou méthode) pour choisir un mot aléatoire

* Attendu (minimum) : une fonction `pick_secret_word()`.

---

### 2) `game_state.py`

**Responsabilité : représenter l’état du jeu**
Vous devez créer une classe `GameState` qui contient :

- `secret_word` (str)
- `guess_word` (str, avec `_`)
- `life` (int)

Et au moins ces méthodes :

- `is_won()` → True/False
- `is_lost()` → True/False

---

### 3) `game.py`

**Responsabilité : logique du jeu**
Vous devez créer une classe `HangmanGame` (ou `Game`) qui :

- possède un `GameState`
- gère un tour de jeu avec une méthode `play_turn(letter)`
  - met à jour `guess_word` si lettre correcte
  - enlève une vie si lettre incorrecte
  - ne pénalise pas si la lettre a déjà été proposée (optionnel mais recommandé)

* Attendu : **aucun `input()` ni `print()` dans ce fichier**.

---

### 4) `ui.py`

**Responsabilité : interface console**
Créer une classe `ConsoleUI` qui contient :

- `ask_letter()` → demande une lettre
- `show_status(guess_word, life)` → affiche l’état
- `show_win()` / `show_lose(secret_word)` → messages de fin

* Attendu : c’est ici qu’il y a `input()` et `print()`.

---

### 5) `main.py`

**Responsabilité : démarrer le jeu**
`main.py` doit :

- créer l’UI
- créer le jeu (en choisissant un mot secret)
- lancer la boucle principale jusqu’à victoire ou défaite

Exemple d’import attendu :

```python
from hangman.game import HangmanGame
from hangman.ui import ConsoleUI
```

---

## Contraintes obligatoires

- Vous devez utiliser **au moins 2 classes** (`GameState` et `HangmanGame` minimum)
- Vous devez utiliser un **package** (`hangman/`)
- Vous devez séparer :
  - la **logique** (game.py, game_state.py)
  - l’**interface** (ui.py)

---

## Bonus (optionnel, mais très bon pour progresser)

Choisir au moins **2 bonus** :

1. Empêcher les entrées invalides :

- vide
- plus d’une lettre
- chiffres / symboles

2. Afficher les lettres déjà proposées.

3. Ne pas retirer de vie si la lettre a déjà été testée.

4. Mode “rejouer” (relancer une partie).

5. Choisir le nombre de vies au début.

---

## Critères de réussite (comment je teste votre travail)

Votre projet est réussi si :

- `python main.py` lance le jeu sans erreurs
- les imports fonctionnent correctement
- la logique du jeu est correcte (gagner/perdre)
- la structure des fichiers est respectée
- votre code est clair et bien organisé

---

## Livrables à remettre

Vous devez remettre :

- tout le dossier du projet (`pendu/`)
- tous les fichiers `.py`
- (optionnel) un petit `README.md` expliquant comment lancer
