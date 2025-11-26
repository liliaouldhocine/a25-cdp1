# Solutions des Exercices

## Solution Exercice 1

### 1.1 : Déclaration basique

```python
personne = {"nom": "Dupont", "age": 25, "ville": "Paris"}
print(personne)
```

### 1.2 : Depuis une liste de tuples

```python
donnees = [("nom", "Alice"), ("age", 30), ("metier", "ingenieure")]
personne = dict(donnees)
print(personne)
```

### 1.3 : Avec dict() - Corrigé

```python
etudiant = dict(
    nom="Martin",
    prenom="Pierre",
    notes=[15, 18, 12]
)
print(etudiant)
```

## Solution Exercice 2

### 2.1 : Accès simple

```python
livre = {
    "titre": "1984",
    "auteur": "George Orwell",
    "annee": 1949,
    "pages": 328
}

titre = livre["titre"]
annee = livre["annee"]

print(f"'{titre}' publié en {annee}")
```

### 2.2 : Accès sécurisé - Corrigé

```python
config = {"host": "localhost", "port": 8080}

print(f"Host: {config['host']}")
print(f"Database: {config.get('database', 'Non spécifié')}")
print(f"Port: {config.get('port')}")
```

### 2.3 : Valeurs par défaut

```python
utilisateur = {"nom": "Alice", "age": 25}

ville = utilisateur.get("ville", "Non spécifiée")
profession = utilisateur.get("profession", "Sans emploi")

print(f"Ville: {ville}")
print(f"Profession: {profession}")
```

## Solution Exercice 3

### 3.1 : Ajout et modification

```python
inventaire = {"pommes": 10, "bananes": 5}

inventaire["oranges"] = 8
inventaire["bananes"] = 7
inventaire["pommes"] += 3

print(inventaire)
```

### 3.2 : update() - Corrigé

```python
base = {"a": 1, "b": 2}
nouveau = {"b": 3, "c": 4}

base.update(nouveau)

print(base)
```

### 3.3 : setdefault()

```python
stats = {"visites": 100}

stats.setdefault("telechargements", 0)
stats.setdefault("visites", 200)

print(stats)
```

## Solution Exercice 4

### 4.1 : Suppression basique

```python
donnees = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

del donnees["c"]
valeur_d = donnees.pop("d")
element = donnees.popitem()

print(f"Donnees: {donnees}")
print(f"Valeur de d: {valeur_d}")
print(f"Element supprimé: {element}")
```

### 4.2 : Nettoyage conditionnel - Corrigé

```python
produits = {
    "livre": 15,
    "stylo": None,
    "cahier": 8,
    "gomme": None,
    "regle": 12
}

cles_a_supprimer = [cle for cle, valeur in produits.items() if valeur is None]

# Cette ligne est l'équivalent de ces 4 lignes de code
# cles_a_supprimer = []
# for cle, valeur in produits.items():
#     if valeur is None:
#         cle_a_supprimer.append(cle)

for cle in cles_a_supprimer:
    del produits[cle]

print(produits)
```

### 4.3 : pop() avec défaut

```python
config = {"theme": "sombre", "langue": "fr"}

ancien_theme = config.pop("theme", "clair")
volume = config.pop("volume", 50)

print(f"Ancien theme: {ancien_theme}")
print(f"Volume: {volume}")
```

## Solution Exercice 5

### 5.1 : Copie superficielle

```python
original = {"a": 1, "b": [2, 3], "c": {"d": 4}}

copie = original.copy()

copie["a"] = 10
copie["b"].append(4)

print(f"Original: {original}")
print(f"Copie: {copie}")
```

### 5.2 : Deepcopy - Corrigé

```python
import copy

niveau1 = {"donnees": [1, 2, 3], "config": {"resolu": False}}
niveau2 = copy.deepcopy(niveau1)

niveau2["donnees"].append(4)
niveau2["config"]["resolu"] = True

print(f"Niveau 1: {niveau1}")
print(f"Niveau 2: {niveau2}")
```

### 5.3 : Comparaison de copies

```python
d1 = {"a": 1, "b": 2}
d2 = d1.copy()
d3 = d1

print(f"d1 == d2: {d1 == d2}")
print(f"d1 is d2: {d1 is d2}")
print(f"d1 is d3: {d1 is d3}")
```

## Solution Exercice 6

### 6.1 : Parcours des clés

```python
employe = {"nom": "Alice", "age": 30, "poste": "Developpeur", "salaire": 50000}

for cle in employe:
    print(f"- {cle}")

if "experience" in employe:
    print("Experience trouvée")
else:
    print("Experience non trouvée")
```

### 6.2 : Parcours des valeurs - Corrigé

```python
notes = {"math": 15, "francais": 12, "histoire": 18, "sport": 16}

total = 0
for note in notes.values():
    total += note

print(f"Moyenne: {total / len(notes)}")
```

### 6.3 : Parcours des items

```python
inventaire = {"pommes": 10, "bananes": 5, "oranges": 8, "kiwis": 3}

for produit, quantite in inventaire.items():
    print(f"{produit}: {quantite} unités")

max_produit = max(inventaire, key=inventaire.get)
max_quantite = inventaire[max_produit]

print(f"Produit le plus stocké: {max_produit} ({max_quantite} unités)")
```

## Solution Exercice 7

### 7.1 : keys(), values(), items()

```python
config = {"host": "localhost", "port": 8080, "debug": True}

cles = list(config.keys())
valeurs = list(config.values())
items = list(config.items())

print(f"Clés: {cles}")
print(f"Valeurs: {valeurs}")
print(f"Items: {items}")
```

### 7.2 : fromkeys() - Corrigé

```python
cles = ["nom", "age", "ville"]
valeur_par_defaut = "inconnu"

resultat = dict.fromkeys(cles, valeur_par_defaut)

print(resultat)
```

### 7.3 : Comprehension de dictionnaire

```python
nombres = [1, 2, 3, 4, 5]

carres = {n: n**2 for n in nombres}

print(carres)
```
