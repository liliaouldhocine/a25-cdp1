# Solutions des Exercices

## Solutions Exercice 1 : Code à Corriger

### 1.1 : Parcours de liste (Corrigé)

```python
fruits = ["pomme", "banane", "orange", "kiwi"]

for i, fruit in enumerate(fruits):
    print(f"Fruit {i + 1}: {fruit}")
```

### 1.2 : Somme incorrecte (Corrigé)

```python
nombres = [1, 2, 3, 4, 5]
total = 0

for nombre in nombres:
    total += nombre

print(f"Somme: {total}")
```

### 1.3 : Comptage de voyelles (Corrigé)

```python
texte = "Bonjour le monde"
voyelles = "aeiouy"
compteur = 0

for lettre in texte.lower():
    if lettre in voyelles:
        compteur += 1

print(f"Nombre de voyelles: {compteur}")
```

## Solutions Exercice 2 : Code à Compléter

### 2.1 : Nombres impairs (Complété)

```python
for i in range(1, 21, 2):
    print(i)
```

### 2.2 : Multiples de 5 (Complété)

```python
for nombre in range(0, 51, 5):
    print(nombre)
```

### 2.3 : Carrés des nombres (Complété)

```python
for i in range(1, 11):
    carre = i * i
    print(f"{i}² = {carre}")
```

## Solutions Exercice 3 : Code à Corriger

### 3.1 : Liste numérotée (Corrigé)

```python
couleurs = ["rouge", "vert", "bleu", "jaune"]

for index, couleur in enumerate(couleurs, 1):
    print(f"{index}. {couleur}")
```

### 3.2 : Modification conditionnelle (Corrigé)

```python
nombres = [10, 25, 30, 45, 50]

for index, nombre in enumerate(nombres):
    if index % 2 == 1:
        nombres[index] = nombre * 2

print(nombres)
```

### 3.3 : Recherche d'index (Corrigé)

```python
mots = ["python", "java", "c++", "javascript"]
recherche = "java"

for index, mot in enumerate(mots):
    if mot == recherche:
        print(f"Trouvé à l'index: {index}")
        break
```

## Solutions Exercice 4 : Code à Compléter

### 4.1 : Saisie jusqu'à condition (Complété)

```python
nombre = 0

while not (1 <= nombre <= 100):
    nombre = 50
    if 1 <= nombre <= 100:
        break
    else:
        print("Nombre invalide")

print(f"Nombre valide: {nombre}")
```

### 4.2 : Factorielle (Complété)

```python
n = 5
resultat = 1
i = 1

while i <= n:
    resultat = resultat * i
    i = i + 1

print(f"{n}! = {resultat}")
```

### 4.3 : Compte à rebours (Complété)

```python
compteur = 10

while compteur > 0:
    print(compteur)
    compteur = compteur - 1

print("Décollage !")
```

## Solutions Exercice 5 : Code à Corriger

### 5.1 : Break mal utilisé (Corrigé)

```python
nombres = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

for nombre in nombres:
    if nombre % 2 == 0:
        print("Nombre pair trouvé")
        break

print("Recherche terminée")
```

### 5.2 : Continue incorrect (Corrigé)

```python
nombres = [1, -2, 3, -4, 5, -6]

for nombre in nombres:
    if nombre < 0:
        continue
    print(nombre)
```

### 5.3 : Pass oublié (Corrigé)

```python
notes = [15, 8, 12, 18, 6]

for note in notes:
    if note > 10:
        pass  # À implémenter
    else:
        print(f"Note à améliorer: {note}")
```

## Solutions Exercice 6 : Code à Compléter

### 6.1 : Maximum et minimum (Complété)

```python
temperatures = [22, 18, 25, 20, 17, 23, 19]
max_temp = temperatures[0]
min_temp = temperatures[0]

for temp in temperatures:
    if temp > max_temp:
        max_temp = temp
    if temp < min_temp:
        min_temp = temp

print(f"Max: {max_temp}°C, Min: {min_temp}°C")
```

### 6.2 : Palindrome (Complété)

```python
mot = "ressasser"
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

### 6.3 : Jeu de devinette (Complété)

```python
secret = 42
essais = 0
max_essais = 3

while essais < max_essais:
    essai = 30
    essais += 1

    if essai == secret:
        print("Gagné !")
        break
    elif essai < secret:
        print("Plus grand")
    else:
        print("Plus petit")

    print(f"Essais restants: {max_essais - essais}")

print(f"Perdu ! Le nombre était {secret}")
```
