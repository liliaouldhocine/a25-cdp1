# Examen de Programmation Python - Calculatrice Améliorée

**Durée : 2 heures**

## Contexte

Vous disposez d'une calculatrice simple. Vous devez l'améliorer avec deux fonctionnalités principales :

1. **Calculs avec plusieurs nombres** (plus de 2 opérandes)
2. **Système de mémoire** pour stocker et réutiliser des résultats

## Code de départ

```python
def calcularice():
    """
    Fonction principale de la calculatrice
    """
    print("=== CALCULATRICE SIMPLE ===")

    while True:
        # Afficher le menu
        print("\nOpérations disponibles :")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Quitter")

        try:
            choix = input("Quel est votre choix (1-5) : ")
            if choix == '5':
                print("Merci d'avoir utilisé la calculatrice. Au revoir !")
                break;

            if choix not in ['1', '2', '3', '4']:
                raise ValueError("Choix invalide. Veuillez entrer un nombre entre 1 et 5")

            try :
                num1 = float(input("Entrez le premier nombre : "))
                num2 = float(input("Entrez le deuxième nombre : "))
            except ValueError:
                raise ValueError("Veuillez entrer un nombre valide.")

            if choix == '1': # addition
                resultat = num1 + num2
                operateur = "+"
            elif choix == '2':  # soustraction
                resultat = num1 - num2
                operateur = "-"
            elif choix == '3':  # multiplication
                resultat = num1 * num2
                operateur = "*"
            elif choix == '4':  # division
                if num2 == 0:
                    raise ZeroDivisionError("Division par zéro est impossible ! ")
                resultat = num1 / num2
                operateur = "/"

            # affichage du resultat
            print(f"Résultat : {num1} {operateur} {num2} = {resultat}")

        except ValueError as ve :
            print(f"Erreur : {ve}")
        except ZeroDivisionError as zde:
            print(f"Erreur: {zde}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")


calcularice()
```

## Partie 1 : Calculs avec plusieurs nombres (1 heure)

### 1.1 Modification du menu

Ajoutez cette option au menu principal :

```
6. Opérations multiples (plus de 2 nombres)
```

### 1.2 Nouveau mode de saisie

Quand l'utilisateur choisit 6, demandez :

1. L'opération souhaitée (+, -, \*, /)
2. Combien de nombres il veut utiliser (minimum 2)
3. Les nombres un par un

**Exemple d'exécution :**

```
=== MODE OPÉRATIONS MULTIPLES ===
Opération (+, -, *, /) : +
Combien de nombres voulez-vous additionner ? : 4

Entrez le nombre 1 : 5
Entrez le nombre 2 : 3
Entrez le nombre 3 : 2
Entrez le nombre 4 : 6

Calcul : 5 + 3 + 2 + 6 = 16
```

### 1.3 Implémentation

Créez une fonction pour gérer ce mode :

```python
def operations_multiples():
    """
    Gère les calculs avec plus de 2 nombres
    """
    # À implémenter
    pass
```

**Règles importantes :**

- Pour la **soustraction** : `a - b - c - d`
- Pour la **multiplication** : `a × b × c × d`
- Pour la **division** : `a ÷ b ÷ c ÷ d`
- **Attention aux divisions par zéro** !

### 1.4 Gestion des erreurs

- Vérifier que le nombre d'opérandes est ≥ 2
- Vérifier que tous les nombres sont valides
- Pour la division, vérifier qu'aucun dénominateur n'est 0 (après le premier)

## Partie 2 : Système de mémoire

### 2.1 Variables à ajouter

Ajoutez ces variables au début de la fonction `calcularice()` :

```python
memories = {}  # Dictionnaire pour stocker les valeurs
current_memory = "M1"  # Mémoire active par défaut
```

### 2.2 Menu de la mémoire

Ajoutez cette option au menu principal :

```
7. Gestion de la mémoire
```

Quand l'utilisateur choisit 7, affichez :

```
=== GESTION DE LA MÉMOIRE (Active: M1) ===
a. Stocker le dernier résultat
b. Utiliser une mémoire dans un calcul
c. Afficher toutes les mémoires
d. Effacer une mémoire
e. Retour au menu principal
```

### 2.3 Fonctions à implémenter

#### a. Stocker un résultat

- Stocker le dernier résultat calculé dans la mémoire active
- Si pas de résultat disponible, afficher un message d'erreur
- Exemple : "Résultat 15.5 stocké dans M1"

#### b. Utiliser une mémoire

- Avant de demander un nombre, proposer : "Utiliser une mémoire ? (o/n)"
- Si oui, afficher les mémoires disponibles et leur contenu
- L'utilisateur peut choisir une mémoire dont la valeur sera utilisée

#### c. Afficher les mémoires

- Afficher toutes les mémoires de M1 à M5
- Indiquer "vide" si une mémoire n'a pas de valeur
- Exemple : `M1: 15.50 | M2: vide | M3: -3.00`

#### d. Effacer une mémoire

- Permettre d'effacer une mémoire spécifique ou toutes

### 2.4 Exemple d'utilisation

```
Menu principal > 7
=== GESTION DE LA MÉMOIRE ===
a. Stocker le dernier résultat
b. Utiliser une mémoire dans un calcul
c. Afficher toutes les mémoires
d. Effacer une mémoire
e. Retour

Choix : c

Mémoires actuelles :
M1: 15.50
M2: vide
M3: 8.25
M4: vide
M5: vide
```

## Partie 3 : Intégration

### 3.1 Utilisation combinée

- Permettre d'utiliser une mémoire dans le mode "opérations multiples"
- Le résultat d'une opération multiple peut être stocké en mémoire

### 3.2 Menu principal mis à jour

Votre menu principal final doit ressembler à :

```
=== CALCULATRICE AMÉLIORÉE ===

Opérations disponibles :
1. Addition (+) [2 nombres]
2. Soustraction (-) [2 nombres]
3. Multiplication (*) [2 nombres]
4. Division (/) [2 nombres]
5. Opérations multiples (+, -, *, /)
6. Gestion de la mémoire
7. Quitter
```

## Règles et consignes

### 1. Structure du code

- Conservez la structure actuelle
- Ajoutez des fonctions pour les nouvelles fonctionnalités
- Commentez les sections importantes

### 2. Gestion des erreurs (OBLIGATOIRE)

Pour chaque saisie utilisateur :

- Vérifier le type (nombre entier/décimal)
- Vérifier les valeurs autorisées
- Gérer les divisions par zéro
- Messages d'erreur clairs en français

### 3. Exemples de tests à faire

```python
# Test 1 : Addition multiple
5 + 3 + 2 + 6 = 16

# Test 2 : Soustraction multiple
20 - 5 - 3 - 2 = 10

# Test 3 : Division avec mémoire
# Stocker 100 dans M1
# Faire : M1 ÷ 2 ÷ 5 = 10
```

## Guide étape par étape

### Étape 1 : Commencez par les opérations multiples (1h)

1. Ajoutez l'option 6 au menu
2. Créez la fonction `operations_multiples()`
3. Testez avec l'addition d'abord
4. Puis les autres opérations

### Étape 2 : Implémentez la mémoire

1. Ajoutez les variables `memories` et `current_memory`
2. Créez le sous-menu mémoire
3. Implémentez stockage et rappel
4. Testez avec des calculs simples

### Étape 3 : Intégrez et testez

1. Vérifiez que tout fonctionne ensemble
2. Testez des cas complexes
3. Corrigez les bugs

## Conseils importants

1. **Fonctions utiles** :

```python
# Pour gérer plusieurs nombres
nombres = []
for i in range(nombre_operandes):
    valeur = float(input(f"Entrez le nombre {i+1} : "))
    nombres.append(valeur)

# Pour afficher le calcul
calcul = " + ".join(str(n) for n in nombres)
print(f"Calcul : {calcul} = {resultat}")
```

2. **Gestion mémoire simple** :

```python
# Stockage
memories = {"M1": None, "M2": None, "M3": None, "M4": None, "M5": None}

# Vérifier si une mémoire a une valeur
if memories["M1"] is not None:
    print(f"M1 contient : {memories['M1']}")
else:
    print("M1 est vide")
```

3. **Priorités** :

- Commencez par ce qui vous semble le plus simple
- Testez chaque fonction avant de passer à la suivante
- Ne passez pas plus de 20 minutes sur un problème bloquant

## Questions fréquentes anticipées

**Q : Comment gérer un nombre variable d'opérandes ?**
R : Utilisez une boucle `for` avec `range(nombre_operandes)`

**Q : Comment afficher un calcul comme "5 + 3 + 2" ?**
R : Accumulez les nombres dans une liste, puis utilisez `join()`

**Q : Que faire si l'utilisateur veut utiliser une mémoire vide ?**
R : Afficher un message d'erreur et redemander

## Solution minimale acceptable

Si vous manquez de temps, priorisez :

1. Opérations multiples pour l'addition seulement
2. Stockage et rappel de mémoire (sans effacement)
3. Menu fonctionnel même incomplet

**Bonne chance !**
