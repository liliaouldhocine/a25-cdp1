# Solutions des Exercices

## Solution Exercice 1

### 1.1 : Code à Analyser

```python
x = 10

def modifier_globale():
    x = 20  # Crée une variable locale x, ne modifie pas la globale
    print(f"À l'intérieur: {x}")

modifier_globale()  # Affiche: À l'intérieur: 20
print(f"À l'extérieur: {x}")  # Affiche: À l'extérieur: 10

# Réponse : x reste à 10 car la fonction crée une nouvelle variable locale
```

### 1.2 : Code à Corriger

```python
# Correction : passer les valeurs en paramètre
def calculer_stats(valeurs):  # Ajout du paramètre
    total = sum(valeurs)
    moyenne = total / len(valeurs)
    return total, moyenne

valeurs = [10, 20, 30, 40, 50]
resultat = calculer_stats(valeurs)  # Passage en argument
print(f"Total: {resultat[0]}, Moyenne: {resultat[1]}")
```

### 1.3 : Code à Développer

```python
def ajouter_element(liste, element):
    # Créer une nouvelle liste pour ne pas modifier l'originale
    nouvelle_liste = liste.copy()  # Ou liste[:]
    nouvelle_liste.append(element)
    return nouvelle_liste

# Test
originale = [1, 2, 3]
nouvelle = ajouter_element(originale, 4)
print(f"Originale: {originale}")  # [1, 2, 3]
print(f"Nouvelle: {nouvelle}")    # [1, 2, 3, 4]
```

## Solution Exercice 2

### 2.1 : Code à Analyser

```python
def modifier_parametres(a, b, c):
    a = 100        # a est immuable (int) → modification locale seulement
    b[0] = 200     # b est mutable (list) → modification visible à l'extérieur
    c = c + " modifié"  # c est immuable (str) → modification locale seulement

x = 10
y = [1, 2, 3]
z = "texte"

modifier_parametres(x, y, z)
print(f"x: {x}")  # 10 (inchangé)
print(f"y: {y}")  # [200, 2, 3] (modifié)
print(f"z: {z}")  # "texte" (inchangé)

# Leçon : Seuls les objets mutables peuvent être modifiés de l'intérieur d'une fonction
```

### 2.2 : Code à Corriger

```python
# Correction : utiliser None comme valeur par défaut
def ajouter_historique(action, historique=None):
    if historique is None:
        historique = []
    historique.append(action)
    return historique

# Tests
print("Session 1:", ajouter_historique("login"))      # ['login']
print("Session 2:", ajouter_historique("logout"))     # ['logout']
print("Session 3:", ajouter_historique("update"))     # ['update']
```

### 2.3 : Code à Développer

```python
def fusionner_dicts(dict1, dict2):
    # Créer une copie du premier dictionnaire
    resultat = dict1.copy()
    # Ajouter/mettre à jour avec le second
    resultat.update(dict2)
    return resultat

# Test
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
resultat = fusionner_dicts(d1, d2)

print(f"dict1: {d1}")      # {"a": 1, "b": 2}
print(f"dict2: {d2}")      # {"b": 3, "c": 4}
print(f"Résultat: {resultat}")  # {"a": 1, "b": 3, "c": 4}
```

## Solution Exercice 3

### 3.1 : Code à Analyser

```python
def diviser(a, b):
    if b == 0:
        return  # Retourne None implicitement
    return a / b

resultat1 = diviser(10, 2)  # 5.0
resultat2 = diviser(10, 0)  # None

print(f"10 / 2 = {resultat1}")
print(f"10 / 0 = {resultat2}")  # Affiche "None"
print(f"Type résultat2: {type(resultat2)}")  # <class 'NoneType'>

# Problème : La fonction retourne des types différents selon les cas
# Solution préférable : lever une exception ou retourner une valeur par défaut
```

### 3.2 : Code à Corriger

```python
def trouver_maximum(nombres):
    if not nombres:  # Si liste vide
        return None  # Retourner explicitement None

    maximum = nombres[0]
    for n in nombres:
        if n > maximum:
            maximum = n

    return maximum

# Tests
print(f"Max [1, 5, 3]: {trouver_maximum([1, 5, 3])}")  # 5
print(f"Max []: {trouver_maximum([])}")  # None
print(f"Type retour liste vide: {type(trouver_maximum([]))}")  # <class 'NoneType'>
```

### 3.3 : Code à Développer

```python
def filtrer_nombres_pairs(nombres):
    # Vérifier si l'entrée est une liste
    if not isinstance(nombres, list):
        return []

    # Filtrer les nombres pairs
    resultat = []
    for n in nombres:
        if isinstance(n, (int, float)) and n % 2 == 0:
            resultat.append(n)

    return resultat

# Tests
print(f"Test 1: {filtrer_nombres_pairs([1, 2, 3, 4, 5])}")  # [2, 4]
print(f"Test 2: {filtrer_nombres_pairs([1, 3, 5])}")        # []
print(f"Test 3: {filtrer_nombres_pairs([])}")               # []
print(f"Test 4: {filtrer_nombres_pairs('texte')}")          # []
print(f"Test 5: {filtrer_nombres_pairs(None)}")             # []
```

## Solution Exercice 4

### 4.1 : Code à Analyser

```python
def calculer(a, b, operation="addition"):
    if operation == "addition":
        return a + b
    elif operation == "soustraction":
        return a - b
    elif operation == "multiplication":
        return a * b
    else:
        # Gestion des opérations non supportées
        raise ValueError(f"Opération non supportée: {operation}")

resultat1 = calculer(10, 5)
resultat2 = calculer(10, 5, "soustraction")

print(f"Addition: {resultat1}")
print(f"Soustraction: {resultat2}")

# resultat3 = calculer(10, 5, "division")  # Lève ValueError
```

### 4.2 : Code à Corriger

```python
# Amélioration : utiliser **kwargs pour plus de flexibilité
def creer_personne(nom, **infos):
    personne = {"nom": nom}
    personne.update(infos)
    return personne

# Tests
p1 = creer_personne("Alice", age=25, ville="Paris", profession="Développeuse")
p2 = creer_personne("Bob", ville="Lyon")
p3 = creer_personne("Charlie", email="charlie@test.com", profession="Designer")

print(f"Personne 1: {p1}")
print(f"Personne 2: {p2}")
print(f"Personne 3: {p3}")
```

### 4.3 : Code à Développer

```python
def traiter_commandes(*args, **kwargs):
    resultat = {
        "commandes_executees": [],
        "options": {},
        "erreurs": []
    }

    # Traiter les commandes
    for cmd in args:
        if isinstance(cmd, str):
            resultat["commandes_executees"].append(cmd)
        else:
            resultat["erreurs"].append(f"Commande invalide: {cmd}")

    # Traiter les options
    resultat["options"] = kwargs

    return resultat

# Tests
print(traiter_commandes("start", "stop", "pause", verbose=True, mode="fast"))
# {'commandes_executees': ['start', 'stop', 'pause'], 'options': {'verbose': True, 'mode': 'fast'}, 'erreurs': []}

print(traiter_commandes(123, "test", timeout=10))
# {'commandes_executees': ['test'], 'options': {'timeout': 10}, 'erreurs': ['Commande invalide: 123']}
```

## Solution Exercice 5

### 5.1 : Code à Analyser

```python
def compte_a_rebours(n):
    if n <= 0:
        print("Terminé !")
    else:
        print(n)
        compte_a_rebours(n - 1)

print("Compte à rebours de 5:")
compte_a_rebours(5)  # Fonctionne bien

print("\nCompte à rebours de 1000:")
# compte_a_rebours(1000)  # Risque de RecursionError

# Limite : Python a une limite de récursion (environ 1000 appels)
```

### 5.2 : Code à Corriger

```python
# Correction de la fonction Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Correction

# Test
print(f"Fibonacci(5): {fibonacci(5)}")  # 5
print(f"Fibonacci(10): {fibonacci(10)}")  # 55

# Note : Cette version est très inefficace pour les grands nombres
```

### 5.3 : Code à Développer

```python
def parcourir_dossier(chemin, profondeur_max=10, profondeur_actuelle=0, deja_vus=None):
    """
    Parcours récursif avec sécurité contre les boucles infinies
    """

    # Initialiser l'ensemble des dossiers déjà visités
    if deja_vus is None:
        deja_vus = set()

    # Vérifier la profondeur maximale
    if profondeur_actuelle >= profondeur_max:
        return ["... (profondeur max atteinte)"]

    # Vérifier les boucles
    if chemin in deja_vus:
        return [f"... (boucle détectée: {chemin})"]

    # Ajouter le chemin actuel aux visités
    deja_vus.add(chemin)

    # Simulation de structure de dossiers
    structure = {
        "racine": ["fichier1.txt", "fichier2.txt", "dossier1", "dossier2"],
        "dossier1": ["fichier3.txt", "dossier3"],
        "dossier2": ["fichier4.txt"],
        "dossier3": ["fichier5.txt", "dossier4"],
        "dossier4": ["fichier6.txt", "dossier1"]  # Boucle !
    }

    fichiers = []

    if chemin in structure:
        for element in structure[chemin]:
            if element.startswith("fichier"):
                fichiers.append(element)
            elif element.startswith("dossier"):
                # Appel récursif avec mise à jour des paramètres
                sous_fichiers = parcourir_dossier(
                    element,
                    profondeur_max,
                    profondeur_actuelle + 1,
                    deja_vus.copy()  # Important : copier l'ensemble
                )
                fichiers.extend(sous_fichiers)

    return fichiers

# Test
resultat = parcourir_dossier("racine")
print(f"Fichiers trouvés: {resultat}")
```
