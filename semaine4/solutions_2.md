# Solutions

## Solution Exercice 1

### 1.1 : Parcours de liste

```python
fruits = ["pomme", "banane", "orange", "kiwi"]

for fruit in fruits:
    print(fruit)
```

### 1.2 : Somme des éléments

```python
nombres = [5, 12, 8, 3, 15]
somme = 0

for nombre in nombres:
    somme += nombre

print(f"La somme est : {somme}")
```

### 1.3 : Comptage de caractères

```python
texte = "programmation python avancee"
compteur = 0

for lettre in texte:
    if lettre == 'a':
        compteur += 1

print(f"La lettre 'a' apparaît {compteur} fois")
```

## Solution Exercice 2

### 2.1 : Nombres pairs

```python
for i in range(0, 21, 2):
    print(i)
```

### 2.2 : Table de multiplication

```python
nombre = 7

for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")
```

### 2.3 : Compte à rebours

```python
for i in range(10, 0, -1):
    print(i)
print("Décollage !")
```

## Solution Exercice 3

### 3.1 : Liste numérotée

```python
villes = ["Paris", "Lyon", "Marseille", "Toulouse"]

for index, ville in enumerate(villes):
    print(f"{index + 1}. {ville}")
```

### 3.2 : Recherche d'élément

```python
nombres = [10, 25, 30, 45, 50]
recherche = 30

for index, nombre in enumerate(nombres):
    if nombre == recherche:
        print(f"Trouvé à la position {index}")
        break
```

### 3.3 : Modification sélective

```python
nombres = [1, 2, 3, 4, 5, 6]
resultat = []

for index, nombre in enumerate(nombres):
    if index % 2 == 0:  # positions paires
        resultat.append(nombre * 2)
    else:
        resultat.append(nombre)

print(resultat)
```

## Solution Exercice 4

### 4.1 : Saisie contrôlée

```python
nombre = 0

while nombre < 1 or nombre > 10:
    nombre = 5  # Simulation d'une saisie
    if 1 <= nombre <= 10:
        print(f"Nombre valide : {nombre}")
    else:
        print("Erreur : entrez un nombre entre 1 et 10")
        nombre = 0  # Pour continuer la boucle
```

### 4.2 : Devinette de nombre

```python
nombre_secret = 42
essai = 0
trouve = False

while not trouve:
    essai = 25  # Simulation d'une saisie
    if essai == nombre_secret:
        print("Bravo ! Vous avez trouvé le nombre secret.")
        trouve = True
    elif essai < nombre_secret:
        print("Trop petit, essayez encore.")
    else:
        print("Trop grand, essayez encore.")
```

### 4.3 : Calcul de factorielle

```python
nombre = 5
factorial = 1
compteur = 1

while compteur <= nombre:
    factorial *= compteur
    compteur += 1

print(f"La factorielle de {nombre} est {factorial}")
```

## Solution Exercice 5

### 5.1 : Recherche avec break

```python
nombres = [15, 8, 23, 42, 7, 19]
recherche = 42

for nombre in nombres:
    print(f"Vérification de {nombre}")
    if nombre == recherche:
        print("Nombre trouvé !")
        break
else:
    print("Nombre non trouvé")
```

### 5.2 : Filtrage avec continue

```python
nombres = [5, -2, 10, -8, 3, -1, 7]

for nombre in nombres:
    if nombre < 0:
        continue
    print(f"Nombre positif : {nombre}")
```

### 5.3 : Structure avec pass

```python
nombres = [1, 2, 3, 4, 5]

for nombre in nombres:
    if nombre % 2 == 0:
        # À implémenter : traitement des nombres pairs
        pass
    else:
        print(f"Nombre impair : {nombre}")
```

## Solution Exercice 6

### 6.1 : Statistiques d'une liste

```python
nombres = [12, 45, 8, 32, 19, 67, 23]

if nombres:
    minimum = nombres[0]
    maximum = nombres[0]
    somme = 0

    for nombre in nombres:
        if nombre < minimum:
            minimum = nombre
        if nombre > maximum:
            maximum = nombre
        somme += nombre

    moyenne = somme / len(nombres)

    print(f"Minimum : {minimum}")
    print(f"Maximum : {maximum}")
    print(f"Moyenne : {moyenne:.2f}")
else:
    print("La liste est vide")
```

### 6.2 : Palindrome

```python
mot = "radar"
est_palindrome = True

for i in range(len(mot) // 2):
    if mot[i] != mot[len(mot) - 1 - i]:
        est_palindrome = False
        break

if est_palindrome:
    print(f"'{mot}' est un palindrome")
else:
    print(f"'{mot}' n'est pas un palindrome")
```

### 6.3 : Jeu de devinette amélioré

```python
nombre_secret = 50
essais_max = 5
essais = 0

while essais < essais_max:
    essai = 30  # Simulation d'une saisie
    essais += 1

    if essai == nombre_secret:
        print(f"Bravo ! Trouvé en {essais} essai(s)")
        break
    elif essai < nombre_secret:
        print("Trop petit")
    else:
        print("Trop grand")

    if abs(essai - nombre_secret) <= 5:
        print("Vous êtes très proche !")

    print(f"Il vous reste {essais_max - essais} essai(s)")
else:
    print(f"Perdu ! Le nombre était {nombre_secret}")
```
