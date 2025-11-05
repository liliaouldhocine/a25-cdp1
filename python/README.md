## Exercices sur les Interpréteurs

**Exercice 1 : Premiers pas avec l'interpréteur**

1. Ouvre l'interpréteur Python en ligne de commande
2. Tape `print("Bonjour le monde!")` et appuie sur Entrée
3. Quelle est la différence entre taper du code dans l'interpréteur vs dans un fichier .py ?

**Exercice 2 : Calculs simples**
Dans l'interpréteur, effectue ces calculs :

```python
5 + 3
10 - 2 * 3
(10 - 2) * 3
```

## Exercices sur les Messages et Commentaires

**Exercice 3 : Commentaires basiques**
Corrige ce code en ajoutant des commentaires appropriés :

```python
a = 5
b = 10
resultat = a + b
print(resultat)
```

**Exercice 4 : Commentaires multi-lignes**
Écris un programme qui présente une personne avec :

- Un commentaire en tête décrivant le programme
- Des commentaires expliquant chaque étape
- Un message de fin

**Exercice 5 : Messages utilisateur**
Crée un programme qui :

1. Demande le nom de l'utilisateur
2. Demande son âge
3. Affiche un message personnalisé

## Exercices sur les Types

**Exercice 6 : Reconnaissance des types**
Pour chaque valeur, indique son type :

```python
42
"Python"
3.14
True
'123'
```

**Exercice 7 : Conversions de types**
Complete le code suivant :

```python
# Conversion en entier
nombre_texte = "100"
nombre_entier = _______(nombre_texte)

# Conversion en texte
age = 25
age_texte = _______(age)

# Conversion en float
prix = "15.99"
prix_decimal = _______(prix)
```

**Exercice 8 : Opérations et types**
Devine le résultat de ces opérations, puis teste-les :

```python
5 + 3.0
"Bonjour" + " " + "Monde"
"10" + "5"
int("10") + int("5")
```

## Exercices Combinés

**Exercice 9 : Calculateur simple**

```python
"""
CALCULATRICE SIMPLE
Programme : Effectue des opérations basiques
Auteur : [Ton nom]
Date : [Date]
"""

# Demander deux nombres à l'utilisateur
nombre1 = _______(input("Entrez le premier nombre : "))
nombre2 = _______(input("Entrez le deuxième nombre : "))

# Afficher les résultats des opérations
print("Addition :", _______ + _______)
print("Soustraction :", _______ - _______)
print("Multiplication :", _______ * _______)
```

**Exercice 10 : Profil utilisateur**
Crée un programme complet qui :

- Utilise des commentaires pour expliquer chaque section
- Demande différentes informations (nom, âge, ville, profession)
- Affiche un profil complet avec des messages formatés
- Gère correctement les types de données

## Solutions Guidées

**Indice pour l'exercice 9 :**

```python
# Pour convertir l'input en nombre, utilise float() ou int()
# N'oublie pas les noms de variables dans les print()
```

**Indice pour l'exercice 10 :**

```python
"""
PROFIL UTILISATEUR
Ce programme crée un profil personnel
"""

# Section 1 : Collecte des informations
nom = input("Quel est votre nom ? ")

# Section 2 : Conversions nécessaires
age = int(input("Quel est votre âge ? "))

# Section 3 : Affichage formaté
print(f"Profil de {nom}, {age} ans")
```
