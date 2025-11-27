# Solutions des Exercices

## Solution Exercice 1

### 1.1 : Création et accès

```python
langage = ("Python", 3.9, True, 2023)
version = langage[1]

print(f"Langage: {langage}")
print(f"Version: {version}")
# langage[0] = "Java"  # Génère TypeError
```

### 1.2 : Décompactage - Corrigé

```python
coordonnees = (45.5017, -73.5673, "Montréal")

latitude, longitude, ville = coordonnees

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
print(f"Ville: {ville}")
```

### 1.3 : Méthodes des tuples

```python
notes = (15, 18, 12, 15, 20, 15, 14)

count_15 = notes.count(15)
index_20 = notes.index(20)
contient_10 = 10 in notes

print(f"Occurrences de 15: {count_15}")
print(f"Index de 20: {index_20}")
print(f"Contient 10: {contient_10}")
```

## Solution Exercice 2

### 2.1 : Retour multiple de valeurs

```python
def stats(nombres):
    minimum = min(nombres)
    maximum = max(nombres)
    moyenne = sum(nombres) / len(nombres)
    return (minimum, maximum, moyenne)

donnees = [12, 45, 8, 32, 19]
resultat = stats(donnees)

min_val, max_val, moy_val = resultat

print(f"Min: {min_val}, Max: {max_val}, Moyenne: {moy_val:.1f}")
```

### 2.2 : Échange de variables - Corrigé

```python
a = 10
b = 20

a, b = b, a

print(f"a = {a}, b = {b}")
```

### 2.3 : Tuple comme clé de dictionnaire

```python
coordonnees_villes = {
    (48.8566, 2.3522): "Paris",
    (40.7128, -74.0060): "New York",
    (35.6762, 139.6503): "Tokyo"
}

ville = coordonnees_villes[(35.6762, 139.6503)]

print(f"Ville à (35.6762, 139.6503): {ville}")
```

## Solution Exercice 3

### 3.1 : Création et méthodes de base

```python
fruits = {"pomme", "banane", "kiwi"}

fruits.add("orange")
fruits.update(["mangue", "ananas"])
fruits.add("pomme")  # Ne fait rien, déjà présent

print(f"Fruits: {fruits}")
```

### 3.2 : Opérations ensemblistes - Corrigé

```python
etudiants_math = {"Alice", "Bob", "Charlie"}
etudiants_physique = {"Bob", "David", "Eve"}

tous_etudiants = etudiants_math | etudiants_physique
commun = etudiants_math & etudiants_physique

print(f"Tous: {tous_etudiants}")
print(f"Commun: {commun}")
```

### 3.3 : Suppression dans les sets

```python
nombres = {1, 2, 3, 4, 5, 6, 7, 8, 9}

nombres.remove(3)
nombres.discard(5)
# nombres.remove(10)  # Génère KeyError
nombres.discard(10)   # Ne fait rien

element = nombres.pop()

print(f"Set après suppression: {nombres}")
print(f"Élément supprimé: {element}")
```

## Solution Exercice 4

### 4.1 : Élimination des doublons

```python
emails = ["alice@test.com", "bob@test.com", "alice@test.com", "charlie@test.com", "bob@test.com"]

emails_uniques = set(emails)

print(f"Emails uniques: {emails_uniques}")
print(f"Nombre d'emails uniques: {len(emails_uniques)}")
```

### 4.2 : Recherche d'éléments communs - Corrigé

```python
liste1 = ["python", "java", "c++", "javascript", "python"]
liste2 = ["java", "ruby", "python", "go"]

mots_communs = set(liste1) & set(liste2)

print(f"Mots communs: {mots_communs}")
```

### 4.3 : Validation de données uniques

```python
codes_produits = ["A123", "B456", "A123", "C789", "D012", "B456"]

a_doublons = len(codes_produits) != len(set(codes_produits))

if a_doublons:
    print("Erreur: codes dupliqués détectés")
    doublons = {code for code in codes_produits if codes_produits.count(code) > 1}
    print(f"Codes dupliqués: {doublons}")
else:
    print("Tous les codes sont uniques")
```

## Solution Exercice 5

### 5.1 : Différences symétriques

```python
preferences_user1 = {"action", "comedie", "drame"}
preferences_user2 = {"comedie", "romance", "thriller"}

seulement_user1 = preferences_user1 - preferences_user2
seulement_user2 = preferences_user2 - preferences_user1
un_seul = preferences_user1 ^ preferences_user2
tous_films = preferences_user1 | preferences_user2

print(f"Seulement user1: {seulement_user1}")
print(f"Seulement user2: {seulement_user2}")
print(f"Un seul: {un_seul}")
print(f"Tous: {tous_films}")
```

### 5.2 : Vérification de sous-ensembles - Corrigé

```python
competences_requises = {"python", "sql", "git"}
competences_candidat = {"python", "git"}

est_qualifie = competences_requises.issubset(competences_candidat)

if est_qualifie:
    print("Candidat qualifié")
else:
    print("Compétences manquantes:", competences_requises - competences_candidat)
```

### 5.3 : Mise à jour de sets

```python
nombres = {1, 2, 3}

nombres.update([4, 5])
nombres |= {6, 7, 8}
nombres &= {2, 3, 4, 5}

print(f"Set final: {nombres}")
```

## Solution Exercice 6

### 6.1 : Système de tags

```python
articles = [
    ("Python Basics", {"programming", "python", "beginner"}),
    ("IA Revolution", {"ai", "technology", "future"}),
    ("Web Development", {"programming", "web", "javascript"})
]

articles_programming = [titre for titre, tags in articles if "programming" in tags]
tags_communs = set.intersection(*(tags for _, tags in articles))

index_tags = {}
for titre, tags in articles:
    for tag in tags:
        if tag not in index_tags:
            index_tags[tag] = []
        index_tags[tag].append(titre)

print("Articles programming:", articles_programming)
print("Tags communs:", tags_communs)
print("Index tags:", index_tags)
```

### 6.2 : Gestion de permissions - Corrigé

```python
permissions_admin = {"read", "write", "delete", "manage_users"}
permissions_user = {"read", "write"}
permissions_guest = {"read"}

def verifier_permission(permissions_utilisateur, permission):
    return permission in permissions_utilisateur

user_perms = permissions_user
print(f"User peut write: {verifier_permission(user_perms, 'write')}")
print(f"User peut delete: {verifier_permission(user_perms, 'delete')}")
```

### 6.3 : Analyse de données

```python
texte1 = "python est un langage de programmation pythonique"
texte2 = "programmation en python est amusante"

mots_texte1 = set(texte1.split())
mots_texte2 = set(texte2.split())

mots_communs = mots_texte1 & mots_texte2
mots_uniques_texte1 = mots_texte1 - mots_texte2
mots_uniques_texte2 = mots_texte2 - mots_texte1
tous_mots = mots_texte1 | mots_texte2

print(f"Mots communs: {mots_communs}")
print(f"Uniques texte1: {mots_uniques_texte1}")
print(f"Uniques texte2: {mots_uniques_texte2}")
print(f"Total mots uniques: {len(tous_mots)}")
```
