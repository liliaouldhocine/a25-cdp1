# Exercices sur les Fonctions en Python

## Exercice 1 : Définition Basique et Appel

### 1.1 : Code à Développer

Créez une fonction `bonjour()` qui affiche "Bonjour !" lorsqu'elle est appelée. Appelez-la trois fois.

### 1.2 : Code à Finaliser

```python
# Complétez cette fonction
def ______():
    print("Python est génial !")

# Appelez la fonction
______
```

### 1.3 : Code à Corriger

```python
# Ce code contient des erreurs, corrigez-les
function dire_bonjour
    print("Hello World")

direBonjour()
```

## Exercice 2 : Retour de Valeurs

### 2.1 : Code à Développer

Créez une fonction `carre()` qui prend un nombre en paramètre et retourne son carré. Testez avec plusieurs nombres.

### 2.2 : Code à Finaliser

```python
def est_pair(nombre):
    # Retourne True si le nombre est pair, False sinon
    ______

# Test
print(est_pair(4))   # Devrait afficher True
print(est_pair(7))   # Devrait afficher False
```

### 2.3 : Code à Corriger

```python
def addition(a, b):
    result = a + b

print(addition(5, 3))  # Devrait afficher 8
```

## Exercice 3 : Paramètres et Arguments

### 3.1 : Code à Développer

Créez une fonction `presentation()` qui prend deux paramètres : `nom` et `age`. La fonction doit afficher "Je m'appelle [nom] et j'ai [age] ans."

### 3.2 : Code à Finaliser

```python
def calculer_moyenne(note1, note2, note3):
    # Calcule et retourne la moyenne des trois notes
    ______

# Test avec différentes valeurs
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

# Ce code ne fonctionne pas comme attendu
afficher_info(25, "Alice", "Dupont")
```

## Exercice 4 : Fonctions comme Variables

### 4.1 : Code à Développer

Créez une fonction `multiplier_par_deux()` et une fonction `ajouter_cinq()`. Créez ensuite une variable `operation` qui peut contenir l'une ou l'autre fonction et l'appeler.

### 4.2 : Code à Finaliser

```python
def saluer():
    return "Bonjour"

def dire_au_revoir():
    return "Au revoir"

# Stockez la fonction saluer dans une variable
message_func = ______

# Utilisez la variable pour appeler la fonction
message = ______
print(message)
```

### 4.3 : Code à Corriger

```python
def carre(x):
    return x * x

def cube(x):
    return x * x * x

# Problème ici
operation = carre
resultat = operation(3)  # Doit retourner 9

operation = cube
resultat = operation(2)  # Doit retourner 8

print(resultat)
```

## Exercice 5 : Paramètres Positionnels

### 5.1 : Code à Développer

Créez une fonction `decrire_rectangle()` qui prend `longueur` et `largeur` comme paramètres positionnels et affiche les dimensions.

### 5.2 : Code à Finaliser

```python
def creer_email(prenom, nom, domaine):
    # Crée un email au format prenom.nom@domaine.com
    # Tous en minuscules
    ______

# Test avec différents ordres
email1 = creer_email("jean", "dupont", "entreprise")
email2 = creer_email("entreprise", "jean", "dupont")  # Que se passe-t-il ?

print(f"Email 1: {email1}")
print(f"Email 2: {email2}")
```

### 5.3 : Code à Corriger

```python
def decrire_personne(nom, age, ville):
    print(f"{nom} a {age} ans et habite à {ville}")

# Les arguments sont dans le mauvais ordre
decrire_personne(25, "Paris", "Alice")
```

## Exercice 6 : Variables comme Arguments

### 6.1 : Code à Développer

Créez une fonction `echanger()` qui échange les valeurs de deux variables. Testez avec différentes variables.

### 6.2 : Code à Finaliser

```python
def appliquer_tva(prix_ht, taux_tva):
    # Calcule le prix TTC
    ______

# Utilisez des variables comme arguments
prix_base = 100
taux = 0.2

prix_final = ______
print(f"Prix TTC: {prix_final}")
```

### 6.3 : Code à Corriger

```python
def modifier_liste(liste):
    liste.append("nouvel_element")

ma_liste = [1, 2, 3]
modifier_liste(ma_liste)

print(ma_liste)  # Que contient ma_liste maintenant ?
```

## Exercice 7 : Nombre Indéfini d'Arguments

### 7.1 : Code à Développer

Créez une fonction `somme_nombres()` qui peut prendre n'importe quel nombre d'arguments et retourne leur somme.

### 7.2 : Code à Finaliser

```python
def concatener_mots(*mots):
    # Concatène tous les mots avec un espace
    ______

# Test avec différents nombres d'arguments
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
    print(f"Autres: {autres}")

# Problème avec l'appel
afficher_infos("Alice", "Développeuse", "Paris", 25)
```

## Exercice 8 : Projets Complets

### 8.1 : Calculateur Géométrique (à Développer)

Créez plusieurs fonctions pour calculer :

- `aire_rectangle(longueur, largeur)`
- `perimetre_rectangle(longueur, largeur)`
- `aire_cercle(rayon)`
- `volume_sphere(rayon)`

Testez toutes les fonctions.

### 8.2 : Gestionnaire de Contacts (à Finaliser)

```python
def ajouter_contact(contacts, nom, telephone, email):
    # Ajoute un contact au dictionnaire
    ______

def afficher_contacts(contacts):
    # Affiche tous les contacts
    ______

def rechercher_contact(contacts, nom):
    # Recherche un contact par nom
    ______

# Utilisation
mes_contacts = {}
ajouter_contact(mes_contacts, "Alice", "0123456789", "alice@test.com")
ajouter_contact(mes_contacts, "Bob", "0987654321", "bob@test.com")

afficher_contacts(mes_contacts)
rechercher_contact(mes_contacts, "Alice")
```

### 8.3 : Système de Calcul de Notes (à Corriger)

```python
def calculer_moyenne_etudiant(notes):
    total = 0
    for note in notes:
        total = note
    return total / len(notes)

def determiner_appreciation(moyenne):
    if moyenne >= 16:
        return "Excellent"
    elif moyenne >= 14
        return "Très bien"
    elif moyenne >= 12
        return "Bien"
    elif moyenne >= 10:
        return "Passable"
    else return "Insuffisant"

# Tests
notes_alice = [15, 18, 12]
moyenne = calculer_moyenne_etudiant(notes_alice)
appreciation = determiner_appreciation(moyenne)

print(f"Moyenne: {moyenne}")
print(f"Appréciation: {appreciation}")
```
