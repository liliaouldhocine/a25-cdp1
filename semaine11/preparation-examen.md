**Objectif** : Créer une calculatrice simple en Python avec une gestion robuste des erreurs à l'aide des exceptions.

## Énoncé de l'exercice

Vous devez créer une calculatrice interactive qui permet à l'utilisateur d'effectuer des opérations mathématiques de base : addition, soustraction, multiplication et division.

La calculatrice doit :

1. Afficher un menu des opérations disponibles
2. Demander à l'utilisateur de choisir une opération
3. Demander deux nombres à l'utilisateur
4. Afficher le résultat de l'opération
5. Gérer proprement les erreurs à l'aide d'exceptions

### Spécifications détaillées :

1. **Opérations disponibles** :
   - Addition (+)
   - Soustraction (-)
   - Multiplication (\*)
   - Division (/)

2. **Gestion des exceptions** :
   - Si l'utilisateur entre un choix d'opération invalide, afficher un message d'erreur
   - Si l'utilisateur entre une valeur non numérique, afficher un message d'erreur
   - Si l'utilisateur tente une division par zéro, afficher un message d'erreur

3. **Fonctionnement** :
   - La calculatrice continue de fonctionner jusqu'à ce que l'utilisateur décide de quitter
   - Après chaque calcul, proposer à l'utilisateur de continuer ou de quitter

## Structure suggérée

Voici un squelette de code pour aider vos étudiants à démarrer :

```python
def calculatrice():
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

        # Développement ici


calculatrice()
```

## Questions pour guider les étudiants

1. Quelle exception est levée lorsque vous essayez de convertir en nombre une chaîne qui ne contient pas de nombre valide ?
2. Quelle exception est levée lorsque vous essayez de diviser par zéro ?
3. Comment pouvez-vous gérer plusieurs types d'exceptions dans un même bloc try?
4. Quelle est la différence entre `except ValueError` et `except Exception` ?

## Exemple d'exécution attendue

```
=== CALCULATRICE SIMPLE ===

Opérations disponibles :
1. Addition (+)
2. Soustraction (-)
3. Multiplication (*)
4. Division (/)
5. Quitter
Votre choix (1-5) : 1
Entrez le premier nombre : 10
Entrez le deuxième nombre : 5
Résultat : 10 + 5 = 15

Opérations disponibles :
1. Addition (+)
2. Soustraction (-)
3. Multiplication (*)
4. Division (/)
5. Quitter
Votre choix (1-5) : 4
Entrez le premier nombre : 10
Entrez le deuxième nombre : 0
Erreur : Division par zéro impossible!

Opérations disponibles :
1. Addition (+)
2. Soustraction (-)
3. Multiplication (*)
4. Division (/)
5. Quitter
Votre choix (1-5) : 6
Erreur : Choix invalide. Veuillez entrer un nombre entre 1 et 5.

Opérations disponibles :
1. Addition (+)
2. Soustraction (-)
3. Multiplication (*)
4. Division (/)
5. Quitter
Votre choix (1-5) : 2
Entrez le premier nombre : abc
Erreur : Veuillez entrer un nombre valide.
```
