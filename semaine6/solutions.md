# Solutions des Exercices

## Solution Exercice 1

### 1.1 : Code à Développer

```python
def bonjour():
    print("Bonjour !")

bonjour()
bonjour()
bonjour()
```

### 1.2 : Code à Finaliser

```python
def afficher_message():
    print("Python est génial !")

afficher_message()
```

### 1.3 : Code à Corriger

```python
def dire_bonjour():
    print("Hello World")

dire_bonjour()
```

## Solution Exercice 2

### 2.1 : Code à Développer

```python
def carre(nombre):
    return nombre * nombre

print(carre(5))  # 25
print(carre(3))  # 9
print(carre(10)) # 100
```

### 2.2 : Code à Finaliser

```python
def est_pair(nombre):
    return nombre % 2 == 0

print(est_pair(4))   # True
print(est_pair(7))   # False
```

### 2.3 : Code à Corriger

```python
def addition(a, b):
    result = a + b
    return result

print(addition(5, 3))  # 8
```

## Solution Exercice 3

### 3.1 : Code à Développer

```python
def presentation(nom, age):
    print(f"Je m'appelle {nom} et j'ai {age} ans.")

presentation("Alice", 25)
presentation("Bob", 30)
```

### 3.2 : Code à Finaliser

```python
def calculer_moyenne(note1, note2, note3):
    total = note1 + note2 + note3
    return total / 3

moyenne1 = calculer_moyenne(15, 12, 18)
moyenne2 = calculer_moyenne(10, 8, 12)

print(f"Moyenne 1: {moyenne1}")
print(f"Moyenne 2: {moyenne2}")
```

### 3.3 : Code à Corriger

```python
def afficher_info(prenom, nom, age):
    print(f"Nom: {prenom} {nom}")
    print(f"Age: {age} ans")

# Correction de l'ordre des arguments
afficher_info("Alice", "Dupont", 25)
```

## Solution Exercice 4

### 4.1 : Code à Développer

```python
def multiplier_par_deux(x):
    return x * 2

def ajouter_cinq(x):
    return x + 5

# Utilisation comme variable
operation = multiplier_par_deux
print(operation(10))  # 20

operation = ajouter_cinq
print(operation(10))  # 15
```

### 4.2 : Code à Finaliser

```python
def saluer():
    return "Bonjour"

def dire_au_revoir():
    return "Au revoir"

message_func = saluer
message = message_func()
print(message)
```

### 4.3 : Code à Corriger

```python
def carre(x):
    return x * x

def cube(x):
    return x * x * x

operation = carre
resultat1 = operation(3)  # 9

operation = cube
resultat2 = operation(2)  # 8

print(f"Carre: {resultat1}")
print(f"Cube: {resultat2}")
```

## Solution Exercice 5

### 5.1 : Code à Développer

```python
def decrire_rectangle(longueur, largeur):
    print(f"Rectangle de {longueur}cm par {largeur}cm")
    print(f"Périmètre: {(longueur + largeur) * 2}cm")
    print(f"Aire: {longueur * largeur}cm²")

decrire_rectangle(10, 5)
decrire_rectangle(7, 3)
```

### 5.2 : Code à Finaliser

```python
def creer_email(prenom, nom, domaine):
    email = f"{prenom.lower()}.{nom.lower()}@{domaine}.com"
    return email

email1 = creer_email("jean", "dupont", "entreprise")
email2 = creer_email("entreprise", "jean", "dupont")

print(f"Email 1: {email1}")
print(f"Email 2: {email2}")
```

### 5.3 : Code à Corriger

```python
def decrire_personne(nom, age, ville):
    print(f"{nom} a {age} ans et habite à {ville}")

# Correction de l'ordre
decrire_personne("Alice", 25, "Paris")
```

## Solution Exercice 6

### 6.1 : Code à Développer

```python
def echanger(a, b):
    return b, a

x = 10
y = 20
print(f"Avant: x={x}, y={y}")

x, y = echanger(x, y)
print(f"Après: x={x}, y={y}")

# Autre test
a = "hello"
b = "world"
a, b = echanger(a, b)
print(f"a={a}, b={b}")
```

### 6.2 : Code à Finaliser

```python
def appliquer_tva(prix_ht, taux_tva):
    tva = prix_ht * taux_tva
    return prix_ht + tva

prix_base = 100
taux = 0.2

prix_final = appliquer_tva(prix_base, taux)
print(f"Prix TTC: {prix_final}")
```

### 6.3 : Code à Corriger

```python
def modifier_liste(liste):
    liste.append("nouvel_element")
    return liste

ma_liste = [1, 2, 3]
ma_liste = modifier_liste(ma_liste)

print(ma_liste)  # [1, 2, 3, 'nouvel_element']
```

## Solution Exercice 7

### 7.1 : Code à Développer

```python
def somme_nombres(*nombres):
    total = 0
    for n in nombres:
        total += n
    return total

print(somme_nombres(1, 2, 3))        # 6
print(somme_nombres(10, 20))         # 30
print(somme_nombres(1, 2, 3, 4, 5))  # 15
```

### 7.2 : Code à Finaliser

```python
def concatener_mots(*mots):
    phrase = " ".join(mots)
    return phrase

phrase1 = concatener_mots("Bonjour", "le", "monde")
phrase2 = concatener_mots("Python", "c'est", "génial", "!")
phrase3 = concatener_mots("Test")

print(phrase1)
print(phrase2)
print(phrase3)
```

### 7.3 : Code à Corriger

```python
def afficher_infos(nom, *autres):
    print(f"Nom: {nom}")
    print(f"Autres informations: {autres}")

afficher_infos("Alice", "Développeuse", "Paris", 25)
```

## Solution Exercice 8

### 8.1 : Calculateur Géométrique

```python
def aire_rectangle(longueur, largeur):
    return longueur * largeur

def perimetre_rectangle(longueur, largeur):
    return 2 * (longueur + largeur)

def aire_cercle(rayon):
    return 3.14159 * rayon * rayon

def volume_sphere(rayon):
    return (4/3) * 3.14159 * rayon * rayon * rayon

# Tests
print(f"Aire rectangle 5x3: {aire_rectangle(5, 3)}")
print(f"Périmètre rectangle 5x3: {perimetre_rectangle(5, 3)}")
print(f"Aire cercle rayon 4: {aire_cercle(4):.2f}")
print(f"Volume sphère rayon 3: {volume_sphere(3):.2f}")
```

### 8.2 : Gestionnaire de Contacts

```python
def ajouter_contact(contacts, nom, telephone, email):
    contacts[nom] = {
        "telephone": telephone,
        "email": email
    }
    return contacts

def afficher_contacts(contacts):
    for nom, infos in contacts.items():
        print(f"{nom}:")
        print(f"  Téléphone: {infos['telephone']}")
        print(f"  Email: {infos['email']}")

def rechercher_contact(contacts, nom):
    if nom in contacts:
        return contacts[nom]
    else:
        return None

# Utilisation
mes_contacts = {}
ajouter_contact(mes_contacts, "Alice", "0123456789", "alice@test.com")
ajouter_contact(mes_contacts, "Bob", "0987654321", "bob@test.com")

afficher_contacts(mes_contacts)
contact = rechercher_contact(mes_contacts, "Alice")
print(f"\nRecherche Alice: {contact}")
```

### 8.3 : Système de Calcul de Notes

```python
def calculer_moyenne_etudiant(notes):
    total = 0
    for note in notes:
        total += note  # Correction: += au lieu de =
    return total / len(notes)

def determiner_appreciation(moyenne):
    if moyenne >= 16:
        return "Excellent"
    elif moyenne >= 14:
        return "Très bien"
    elif moyenne >= 12:
        return "Bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Insuffisant"

# Tests
notes_alice = [15, 18, 12]
moyenne = calculer_moyenne_etudiant(notes_alice)
appreciation = determiner_appreciation(moyenne)

print(f"Moyenne: {moyenne:.1f}")
print(f"Appréciation: {appreciation}")
```
