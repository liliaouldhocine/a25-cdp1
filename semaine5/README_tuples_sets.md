# Exercices sur les Sets et Tuples en Python

## Exercice 1 : Tuples - Bases et Manipulation

### 1.1 : Création et accès (À compléter)

```python
# Créez un tuple avec les éléments: "Python", 3.9, True, 2023
langage = ______

# Accédez au deuxième élément
version = ______

# Essayez de modifier le premier élément (que se passe-t-il ?)
# langage[0] = "Java"

print(f"Langage: {langage}")
print(f"Version: {version}")
```

### 1.2 : Décompactage de tuple (Erreurs à corriger)

```python
# Ce code contient des erreurs de décompactage
coordonnees = (45.5017, -73.5673, "Montréal")

latitude, longitude = coordonnees

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
```

### 1.3 : Méthodes des tuples (À compléter)

```python
# Soit le tuple suivant
notes = (15, 18, 12, 15, 20, 15, 14)

# Trouvez le nombre d'occurrences de 15
count_15 = ______
# Trouvez l'index du premier 20
index_20 = ______
# Vérifiez si 10 est dans le tuple
contient_10 = ______

print(f"Occurrences de 15: {count_15}")
print(f"Index de 20: {index_20}")
print(f"Contient 10: {contient_10}")
```

## Exercice 2 : Tuples - Cas d'Utilisation

### 2.1 : Retour multiple de valeurs (À compléter)

```python
# Simulez une fonction qui retourne min, max et moyenne
def stats(nombres):
    minimum = min(nombres)
    maximum = max(nombres)
    moyenne = sum(nombres) / len(nombres)
    return ______

# Utilisation
donnees = [12, 45, 8, 32, 19]
resultat = stats(donnees)

# Décompactez le résultat
min_val, max_val, moy_val = ______

print(f"Min: {min_val}, Max: {max_val}, Moyenne: {moy_val:.1f}")
```

### 2.2 : Échange de variables (Erreurs à corriger)

```python
# Corrigez cet échange de variables
a = 10
b = 20

a = b
b = a

print(f"a = {a}, b = {b}")  # Devrait être a=20, b=10
```

### 2.3 : Tuple comme clé de dictionnaire (À compléter)

```python
# Créez un dictionnaire utilisant des tuples comme clés
coordonnees_villes = {
    ______: "Paris",
    (40.7128, -74.0060): "New York",
    ______: "Tokyo"
}

# Accédez à la ville aux coordonnées (35.6762, 139.6503)
ville = ______

print(f"Ville à (35.6762, 139.6503): {ville}")
```

## Exercice 3 : Sets - Bases et Opérations

### 3.1 : Création et méthodes de base (À compléter)

```python
# Créez un set avec des fruits
fruits = ______

# Ajoutez "orange"
______
# Ajoutez plusieurs fruits à la fois
______

# Essayez d'ajouter "pomme" à nouveau (que se passe-t-il ?)
______

print(f"Fruits: {fruits}")
```

### 3.2 : Opérations ensemblistes (Erreurs à corriger)

```python
# Ce code contient des erreurs sur les opérations de sets
etudiants_math = {"Alice", "Bob", "Charlie"}
etudiants_physique = {"Bob", "David", "Eve"}

# Ensemble union
tous_etudiants = etudiants_math + etudiants_physique

# Ensemble intersection
commun = etudiants_math and etudiants_physique

print(f"Tous: {tous_etudiants}")
print(f"Commun: {commun}")
```

### 3.3 : Suppression dans les sets (À compléter)

```python
nombres = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Supprimez 3 avec remove()
______
# Supprimez 5 avec discard()
______
# Essayez de supprimer 10 avec remove() puis discard()
______
______

# Supprimez et retournez un élément arbitraire
element = ______

print(f"Set après suppression: {nombres}")
print(f"Élément supprimé: {element}")
```

## Exercice 4 : Sets - Cas d'Utilisation

### 4.1 : Élimination des doublons (À compléter)

```python
# Liste avec doublons
emails = ["alice@test.com", "bob@test.com", "alice@test.com", "charlie@test.com", "bob@test.com"]

# Éliminez les doublons en utilisant un set
emails_uniques = ______

print(f"Emails uniques: {emails_uniques}")
print(f"Nombre d'emails uniques: {len(emails_uniques)}")
```

### 4.2 : Recherche d'éléments communs (Erreurs à corriger)

```python
# Trouvez les mots communs aux deux listes
liste1 = ["python", "java", "c++", "javascript", "python"]
liste2 = ["java", "ruby", "python", "go"]

mots_communs = []

for mot in liste1:
    if mot in liste2:
        mots_communs = mot

print(f"Mots communs: {mots_communs}")
```

### 4.3 : Validation de données uniques (À compléter)

```python
# Liste de codes produits, doivent être uniques
codes_produits = ["A123", "B456", "A123", "C789", "D012", "B456"]

# Vérifiez s'il y a des doublons
a_doublons = ______

if a_doublons:
    print("Erreur: codes dupliqués détectés")
    # Trouvez les codes dupliqués
    doublons = ______
    print(f"Codes dupliqués: {doublons}")
else:
    print("Tous les codes sont uniques")
```

## Exercice 5 : Sets - Opérations Avancées

### 5.1 : Différences symétriques (À compléter)

```python
preferences_user1 = {"action", "comedie", "drame"}
preferences_user2 = {"comedie", "romance", "thriller"}

# Films aimés par user1 mais pas user2
seulement_user1 = ______
# Films aimés par user2 mais pas user1
seulement_user2 = ______
# Films aimés par un seul des deux
un_seul = ______
# Tous les films uniques
tous_films = ______

print(f"Seulement user1: {seulement_user1}")
print(f"Seulement user2: {seulement_user2}")
print(f"Un seul: {un_seul}")
print(f"Tous: {tous_films}")
```

### 5.2 : Vérification de sous-ensembles (Erreurs à corriger)

```python
# Ce code vérifie mal les sous-ensembles
competences_requises = {"python", "sql", "git"}
competences_candidat = {"python", "git"}

est_qualifie = competences_requises in competences_candidat

if est_qualifie:
    print("Candidat qualifié")
else:
    print("Compétences manquantes:", competences_requises - competences_candidat)
```

### 5.3 : Mise à jour de sets (À compléter)

```python
# Set initial
nombres = {1, 2, 3}

# Ajoutez plusieurs éléments avec update()
______

# Effectuez une union avec un autre set
autres_nombres = {6, 7, 8}
______

# Gardez seulement l'intersection avec {2, 3, 4, 5}
______

print(f"Set final: {nombres}")
```

## Exercice 6 : Projets Complets

### 6.1 : Système de tags (À développer)

```python
# Créez un système de gestion de tags pour des articles
articles = [
    ("Python Basics", {"programming", "python", "beginner"}),
    ("IA Revolution", {"ai", "technology", "future"}),
    ("Web Development", {"programming", "web", "javascript"})
]

# Trouvez tous les articles avec le tag "programming"
articles_programming = ______

# Trouvez les tags communs à tous les articles
tags_communs = ______

# Créez un index inversé tag -> articles
index_tags = {}
______

print("Articles programming:", articles_programming)
print("Tags communs:", tags_communs)
print("Index tags:", index_tags)
```

### 6.2 : Gestion de permissions (Erreurs à corriger)

```python
# Système de permissions avec sets
permissions_admin = {"read", "write", "delete", "manage_users"}
permissions_user = {"read", "write"}
permissions_guest = {"read"}

# Vérification des permissions (code incorrect)
def verifier_permission(utilisateur, permission):
    if permission in utilisateur:
        return True
    else:
        return False

# Test
user_perms = permissions_user
print(f"User peut write: {verifier_permission(user_perms, 'write')}")
print(f"User peut delete: {verifier_permission(user_perms, 'delete')}")
```

### 6.3 : Analyse de données (À développer)

```python
# Analyse de fréquences de mots dans des textes
texte1 = "python est un langage de programmation pythonique"
texte2 = "programmation en python est amusante"

# Extrayez les mots uniques de chaque texte
mots_texte1 = ______
mots_texte2 = ______

# Analyse
mots_communs = ______
mots_uniques_texte1 = ______
mots_uniques_texte2 = ______
tous_mots = ______

print(f"Mots communs: {mots_communs}")
print(f"Uniques texte1: {mots_uniques_texte1}")
print(f"Uniques texte2: {mots_uniques_texte2}")
print(f"Total mots uniques: {len(tous_mots)}")
```
