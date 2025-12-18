# Lecture et Écriture dans des Fichiers en Python

## 1. Écrire dans un Fichier (Write)

### Écrire en écrasant le contenu existant

```python
# Ouverture en mode 'w' (write) - crée ou écrase le fichier
with open("mon_fichier.txt", "w") as fichier:
    fichier.write("Bonjour le monde!\n")
    fichier.write("Ceci est la deuxième ligne.\n")
    fichier.write("Troisième ligne.\n")

print("Fichier écrit avec succès")
```

### Écrire plusieurs lignes en une fois

```python
lignes = [
    "Alice: 25 ans\n",
    "Bob: 30 ans\n",
    "Charlie: 35 ans\n"
]

with open("personnes.txt", "w") as f:
    f.writelines(lignes)
```

## 2. Ajouter à un Fichier (Append)

### Ajouter sans écraser

```python
# Mode 'a' (append) - ajoute à la fin du fichier
with open("journal.txt", "a") as f:
    f.write("=== Nouvelle entrée ===\n")
    f.write("Date: 2024-01-15\n")
    f.write("Événement: Cours Python\n")
    f.write("\n")  # Ligne vide
```

## 3. Lire un Fichier (Read)

### Lire tout le contenu

```python
# Mode 'r' (read) - lecture seule
with open("mon_fichier.txt", "r") as f:
    contenu = f.read()
    print("Contenu complet:")
    print(contenu)
```

### Lire ligne par ligne

```python
with open("mon_fichier.txt", "r") as f:
    print("Ligne par ligne:")
    for ligne in f:
        print(f"Ligne: {ligne.strip()}")  # strip() enlève \n
```

### Lire dans une liste

```python
with open("mon_fichier.txt", "r") as f:
    lignes = f.readlines()
    print(f"Nombre de lignes: {len(lignes)}")
    for i, ligne in enumerate(lignes, 1):
        print(f"Ligne {i}: {ligne.strip()}")
```

### Lire seulement quelques lignes

```python
with open("mon_fichier.txt", "r") as f:
    premiere_ligne = f.readline()  # Lit une ligne
    print(f"Première ligne: {premiere_ligne.strip()}")

    deux_lignes = f.read(50)  # Lit 50 caractères
    print(f"50 caractères suivants: {deux_lignes}")
```

## 4. Exemples Complets

### Exemple 1 : Carnet d'adresses simple

```python
# Écrire des contacts
contacts = [
    "Alice,alice@email.com,0123456789\n",
    "Bob,bob@email.com,0987654321\n",
    "Charlie,charlie@email.com,0112233445\n"
]

with open("contacts.csv", "w") as f:
    f.write("Nom,Email,Téléphone\n")
    f.writelines(contacts)

# Lire les contacts
with open("contacts.csv", "r") as f:
    print("Carnet d'adresses:")
    for ligne in f:
        nom, email, tel = ligne.strip().split(",")
        print(f"{nom}: {email} - {tel}")
```

### Exemple 2 : Journal de notes

```python
# Ajouter une note
def ajouter_note(note):
    with open("notes.txt", "a") as f:
        f.write(f"{note}\n")

# Lire toutes les notes
def lire_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            return [note.strip() for note in notes]
    except FileNotFoundError:
        return []

# Utilisation
ajouter_note("Acheter du lait")
ajouter_note("Appeler le médecin")
ajouter_note("Faire les exercices Python")

notes = lire_notes()
print("Mes notes:")
for i, note in enumerate(notes, 1):
    print(f"{i}. {note}")
```

### Exemple 3 : Compteur de visites

```python
# Lire le compteur
def lire_compteur():
    try:
        with open("compteur.txt", "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

# Incrémenter le compteur
def incrementer_compteur():
    compteur = lire_compteur() + 1
    with open("compteur.txt", "w") as f:
        f.write(str(compteur))
    return compteur

# Test
for _ in range(3):
    nouveau_total = incrementer_compteur()
    print(f"Visite #{nouveau_total}")
```

## 5. Gestion des Erreurs

```python
try:
    with open("fichier_inexistant.txt", "r") as f:
        contenu = f.read()
except FileNotFoundError:
    print("Erreur: Fichier non trouvé")
except PermissionError:
    print("Erreur: Permission refusée")
except Exception as e:
    print(f"Erreur inattendue: {e}")
```

## 6. Modes d'Ouverture

| Mode   | Description                       |
| ------ | --------------------------------- |
| `"r"`  | Lecture seule (défaut)            |
| `"w"`  | Écriture (crée ou écrase)         |
| `"a"`  | Ajout à la fin                    |
| `"r+"` | Lecture et écriture               |
| `"w+"` | Lecture/écriture (crée ou écrase) |
| `"a+"` | Lecture/ajout à la fin            |

## 7. Bonnes Pratiques

**Toujours utiliser `with`** : Ferme automatiquement le fichier

```python
# ✅ BON
with open("fichier.txt", "r") as f:
    contenu = f.read()

# ❌ MAUVAIS (peut oublier de fermer)
f = open("fichier.txt", "r")
contenu = f.read()
f.close()  # Peut être oublié
```

**Vérifier si un fichier existe :**

```python
import os

if os.path.exists("mon_fichier.txt"):
    print("Le fichier existe")
else:
    print("Le fichier n'existe pas")
```

**Lire un fichier JSON (si besoin de structure) :**

```python
import json

# Écrire
donnees = {"nom": "Alice", "age": 25, "ville": "Paris"}
with open("data.json", "w") as f:
    json.dump(donnees, f)

# Lire
with open("data.json", "r") as f:
    donnees_lues = json.load(f)
    print(donnees_lues["nom"])  # Alice
```

C'est l'essentiel pour commencer avec les fichiers en Python !
