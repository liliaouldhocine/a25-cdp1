# Exercices Avancés sur les Fonctions - Défis et Limites

## Exercice 1 : Portée des Variables et Effets de Bord

### 1.1 : Code à Analyser

```python
x = 10

def modifier_globale():
    x = 20
    print(f"À l'intérieur: {x}")

modifier_globale()
print(f"À l'extérieur: {x}")

# Question : Quelle est la valeur finale de x ? Pourquoi ?
```

### 1.2 : Code à Corriger

```python
# Ce code a un problème de portée
def calculer_stats():
    total = sum(valeurs)
    moyenne = total / len(valeurs)
    return total, moyenne

valeurs = [10, 20, 30, 40, 50]
resultat = calculer_stats()
print(f"Total: {resultat[0]}, Moyenne: {resultat[1]}")

# Problème : la fonction utilise une variable définie à l'extérieur
```

### 1.3 : Code à Développer

```python
# Créez une fonction qui ne modifie pas la liste originale
def ajouter_element(liste, element):
    # DOIT retourner une nouvelle liste avec l'élément ajouté
    # NE DOIT PAS modifier la liste originale
    pass

# Test
originale = [1, 2, 3]
nouvelle = ajouter_element(originale, 4)
print(f"Originale: {originale}")  # Devrait être [1, 2, 3]
print(f"Nouvelle: {nouvelle}")    # Devrait être [1, 2, 3, 4]
```

## Exercice 2 : Paramètres Mutables et Immuables

### 2.1 : Code à Analyser

```python
def modifier_parametres(a, b, c):
    a = 100
    b[0] = 200
    c = c + " modifié"

x = 10
y = [1, 2, 3]
z = "texte"

modifier_parametres(x, y, z)
print(f"x: {x}")  # ?
print(f"y: {y}")  # ?
print(f"z: {z}")  # ?

# Question : Quelles variables sont modifiées ? Pourquoi ?
```

### 2.2 : Code à Corriger

```python
# Ce code a un problème avec les paramètres mutables par défaut
def ajouter_historique(action, historique=[]):
    historique.append(action)
    return historique

# Tests
print("Session 1:", ajouter_historique("login"))
print("Session 2:", ajouter_historique("logout"))
print("Session 3:", ajouter_historique("update"))

# Problème : toutes les sessions partagent le même historique !
```

### 2.3 : Code à Développer

```python
# Créez une fonction qui fusionne deux dictionnaires sans modifier les originaux
def fusionner_dicts(dict1, dict2):
    # DOIT retourner un nouveau dictionnaire fusionné
    # NE DOIT PAS modifier dict1 ni dict2
    # En cas de clés en commun, dict2 écrase dict1
    pass

# Test
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
resultat = fusionner_dicts(d1, d2)

print(f"dict1: {d1}")      # Devrait être {"a": 1, "b": 2}
print(f"dict2: {d2}")      # Devrait être {"b": 3, "c": 4}
print(f"Résultat: {resultat}")  # Devrait être {"a": 1, "b": 3, "c": 4}
```

## Exercice 3 : Valeurs de Retour et Cas Limites

### 3.1 : Code à Analyser

```python
def diviser(a, b):
    if b == 0:
        return  # Que retourne-t-on ici ?
    return a / b

resultat1 = diviser(10, 2)
resultat2 = diviser(10, 0)

print(f"10 / 2 = {resultat1}")
print(f"10 / 0 = {resultat2}")
print(f"Type résultat2: {type(resultat2)}")

# Question : Quel est le problème avec cette fonction ?
```

### 3.2 : Code à Corriger

```python
# Ce code ne gère pas bien tous les cas de retour
def trouver_maximum(nombres):
    if not nombres:  # Si liste vide
        return  # Problème ici

    maximum = nombres[0]
    for n in nombres:
        if n > maximum:
            maximum = n

    return maximum

# Tests
print(f"Max [1, 5, 3]: {trouver_maximum([1, 5, 3])}")
print(f"Max []: {trouver_maximum([])}")
print(f"Type retour liste vide: {type(trouver_maximum([]))}")

# Problème : que devrait retourner une liste vide ?
```

### 3.3 : Code à Développer

```python
# Créez une fonction qui retourne toujours le même type
def filtrer_nombres_pairs(nombres):
    # DOIT toujours retourner une liste
    # Si aucun nombre pair, retourner une liste vide
    # Si nombres n'est pas une liste, retourner une liste vide
    pass

# Tests
print(f"Test 1: {filtrer_nombres_pairs([1, 2, 3, 4, 5])}")  # [2, 4]
print(f"Test 2: {filtrer_nombres_pairs([1, 3, 5])}")        # []
print(f"Test 3: {filtrer_nombres_pairs([])}")               # []
print(f"Test 4: {filtrer_nombres_pairs('texte')}")          # []
print(f"Test 5: {filtrer_nombres_pairs(None)}")             # []
```

## Exercice 4 : Paramètres et Surcharge

### 4.1 : Code à Analyser

```python
def calculer(a, b, operation="addition"):
    if operation == "addition":
        return a + b
    elif operation == "soustraction":
        return a - b
    elif operation == "multiplication":
        return a * b
    # Problème : que se passe-t-il pour d'autres opérations ?

resultat1 = calculer(10, 5)
resultat2 = calculer(10, 5, "soustraction")
resultat3 = calculer(10, 5, "division")

print(f"Addition: {resultat1}")
print(f"Soustraction: {resultat2}")
print(f"Division: {resultat3}")

# Question : Quel est le problème ici ?
```

### 4.2 : Code à Corriger

```python
# Ce code utilise trop de paramètres optionnels
def creer_personne(nom, age=0, ville="", profession="", telephone="", email=""):
    personne = {
        "nom": nom,
        "age": age,
        "ville": ville,
        "profession": profession,
        "telephone": telephone,
        "email": email
    }
    return personne

# Tests
p1 = creer_personne("Alice", 25, "Paris", "Développeuse", "0123456789", "alice@test.com")
p2 = creer_personne("Bob", ville="Lyon")
p3 = creer_personne("Charlie", email="charlie@test.com", profession="Designer")

print(f"Personne 1: {p1}")
print(f"Personne 2: {p2}")
print(f"Personne 3: {p3}")

# Problème : difficile de se souvenir de l'ordre des paramètres optionnels
```

### 4.3 : Code à Développer

```python
# Créez une fonction plus flexible avec *args et **kwargs
def traiter_commandes(*args, **kwargs):
    """
    args: liste des commandes
    kwargs: options supplémentaires
    Retourne un dictionnaire avec le résultat
    """
    resultat = {
        "commandes_executees": [],
        "options": {},
        "erreurs": []
    }

    # À compléter
    # 1. Ajoutez chaque commande de args à commandes_executees
    # 2. Ajoutez chaque option de kwargs à options
    # 3. Si une commande n'est pas une string, ajoutez une erreur

    return resultat

# Tests
print(traiter_commandes("start", "stop", "pause", verbose=True, mode="fast"))
print(traiter_commandes(123, "test", timeout=10))  # 123 n'est pas une string valide
```

## Exercice 5 : Récursivité et Limites

### 5.1 : Code à Analyser

```python
def compte_a_rebours(n):
    if n <= 0:
        print("Terminé !")
    else:
        print(n)
        compte_a_rebours(n - 1)

# Test
print("Compte à rebours de 5:")
compte_a_rebours(5)

print("\nCompte à rebours de 1000:")
compte_a_rebours(1000)  # Que se passe-t-il ?

# Question : Quelle est la limite de cette fonction ?
```

### 5.2 : Code à Corriger

```python
# Ce code a un problème de récursivité infinie
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n) + fibonacci(n - 1)  # ERREUR ici !

# Test - NE PAS EXÉCUTER TEL QUEL !
# print(fibonacci(5))  # Va planter

# Correction nécessaire
```

### 5.3 : Code à Développer

```python
# Créez une fonction récursive avec une limite de sécurité
def parcourir_dossier(chemin, profondeur_max=10, profondeur_actuelle=0):
    """
    Simule le parcours d'une arborescence de dossiers
    chemin: string représentant le chemin
    profondeur_max: sécurité contre la récursivité infinie
    Retourne la liste de tous les "fichiers" trouvés
    """

    # Simulation de structure de dossiers
    structure = {
        "racine": ["fichier1.txt", "fichier2.txt", "dossier1", "dossier2"],
        "dossier1": ["fichier3.txt", "dossier3"],
        "dossier2": ["fichier4.txt"],
        "dossier3": ["fichier5.txt", "dossier4"],  # Boucle potentielle
        "dossier4": ["fichier6.txt", "dossier1"]   # Boucle !
    }

    # À compléter avec sécurité contre récursivité infinie
    pass

# Test
resultat = parcourir_dossier("racine")
print(f"Fichiers trouvés: {resultat}")
```
