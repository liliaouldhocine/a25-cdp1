# Exercices Python - Boucles et Itérations (Code à Corriger/Compléter)

## Exercice 1 : Code à Corriger - Boucle for

### Exercice 1.1 : Parcours de liste (Erreurs à trouver)

```python
fruits = ["pomme", "banane", "orange", "kiwi"]

# Ce code devrait afficher chaque fruit avec son index
for i in fruits:
    print(f"Fruit {fruits[i]}: {i}")
```

### Exercice 1.2 : Somme incorrecte (Erreurs à trouver)

```python
nombres = [1, 2, 3, 4, 5]
total = 0

# Ce code devrait calculer la somme
for i in range(len(nombres)):
    total = i

print(f"Somme: {total}")
```

### Exercice 1.3 : Comptage de voyelles (Erreurs à trouver)

```python
texte = "Bonjour le monde"
voyelles = "aeiouy"
compteur = 0

# Ce code devrait compter les voyelles
for lettre in texte:
    if lettre in voyelles:
        compteur = lettre

print(f"Nombre de voyelles: {compteur}")
```

## Exercice 2 : Code à Compléter - Range()

### Exercice 2.1 : Nombres impairs (À compléter)

```python
# Afficher les nombres impairs de 1 à 20
for i in range(______, ______, ______):
    print(i)
```

### Exercice 2.2 : Multiples de 5 (À compléter)

```python
# Afficher les multiples de 5 de 0 à 50
for nombre in range(______, ______, ______):
    print(nombre)
```

### Exercice 2.3 : Carrés des nombres (À compléter)

```python
# Afficher les carrés des nombres de 1 à 10
for i in range(______, ______):
    carre = ______
    print(f"{i}² = {carre}")
```

## Exercice 3 : Code à Corriger - Enumerate()

### Exercice 3.1 : Liste numérotée (Erreurs à trouver)

```python
couleurs = ["rouge", "vert", "bleu", "jaune"]

# Ce code devrait afficher "1. rouge", "2. vert", etc.
for couleur, index in enumerate(couleurs):
    print(f"{index}. {couleur}")
```

### Exercice 3.2 : Modification conditionnelle (Erreurs à trouver)

```python
nombres = [10, 25, 30, 45, 50]

# Ce code devrait doubler les nombres aux positions impaires
for index in enumerate(nombres):
    if index % 2 == 1:
        nombres[index] = nombres[index] * 2

print(nombres)
```

### Exercice 3.3 : Recherche d'index (Erreurs à trouver)

```python
mots = ["python", "java", "c++", "javascript"]
recherche = "java"

# Ce code devrait trouver l'index du mot recherché
for mot in enumerate(mots):
    if mot == recherche:
        print(f"Trouvé à l'index: {index}")
        break
```

## Exercice 4 : Code à Compléter - Boucle while

### Exercice 4.1 : Saisie jusqu'à condition (À compléter)

```python
nombre = 0

# Continuer tant que le nombre n'est pas entre 1 et 100
while ______:
    nombre = 50  # Simulation saisie
    if 1 <= nombre <= 100:
        ______
    else:
        print("Nombre invalide")

print(f"Nombre valide: {nombre}")
```

### Exercice 4.2 : Factorielle (À compléter)

```python
n = 5
resultat = 1
i = 1

# Calculer la factorielle de n
while ______:
    resultat = ______
    i = ______

print(f"{n}! = {resultat}")
```

### Exercice 4.3 : Compte à rebours (À compléter)

```python
compteur = 10

# Afficher le compte à rebours de 10 à 1
while ______:
    print(compteur)
    ______

print("Décollage !")
```

## Exercice 5 : Code à Corriger - Break, Continue, Pass

### Exercice 5.1 : Break mal utilisé (Erreurs à trouver)

```python
nombres = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

# Ce code devrait s'arrêter au premier nombre pair
for nombre in nombres:
    if nombre % 2 == 0:
        print("Nombre pair trouvé")
    break

print("Recherche terminée")
```

### Exercice 5.2 : Continue incorrect (Erreurs à trouver)

```python
nombres = [1, -2, 3, -4, 5, -6]

# Ce code devrait afficher uniquement les nombres positifs
for nombre in nombres:
    if nombre < 0
        continue
    else
        print(nombre)
```

### Exercice 5.3 : Pass oublié (Erreurs à trouver)

```python
notes = [15, 8, 12, 18, 6]

# Ce code devrait traiter les notes supérieures à 10 plus tard
for note in notes:
    if note > 10:
        # À implémenter
    else:
        print(f"Note à améliorer: {note}")
```

## Exercice 6 : Code à Compléter - Combinaisons

### Exercice 6.1 : Maximum et minimum (À compléter)

```python
temperatures = [22, 18, 25, 20, 17, 23, 19]
max_temp = temperatures[0]
min_temp = ______

for temp in ______:
    if temp > max_temp:
        ______
    if ______:
        min_temp = temp

print(f"Max: {max_temp}°C, Min: {min_temp}°C")
```

### Exercice 6.2 : Palindrome (À compléter)

```python
mot = "ressasser"
est_palindrome = ______

for i in range(______):
    if mot[i] != mot[______]:
        est_palindrome = False
        ______

if est_palindrome:
    print(f"'{mot}' est un palindrome")
else:
    print(f"'{mot}' n'est pas un palindrome")
```

### Exercice 6.3 : Jeu de devinette (À compléter)

```python
secret = 42
essais = 0
max_essais = 3

while ______:
    essai = 30  # Simulation
    ______

    if essai == secret:
        print("Gagné !")
        ______
    elif essai < secret:
        print("Plus grand")
    else:
        print("Plus petit")

    print(f"Essais restants: {max_essais - essais}")

print(f"Perdu ! Le nombre était {secret}")
```
