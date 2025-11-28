# Examen : Découverte des Types en Python

**Durée : 2h00**  
**Niveau : Débutant**  
**Objectif :** Évaluer la compréhension des types de base et leur manipulation

---

## Exercice 1 : Développement - Gestion de Bibliothèque Simple

### Contexte

Vous devez créer un système simple pour gérer des livres dans une bibliothèque en utilisant seulement des variables et des structures de données de base.

### À réaliser :

```python
# EXERCICE 1 - SYSTÈME BIBLIOTHÈQUE
# Créez le système en utilisant uniquement des listes, dictionnaires et variables

# 1. Créez une liste de livres (chaque livre est un dictionnaire)
# Structure d'un livre: titre, auteur, année, statut ("disponible" ou "emprunté")
livres = [
    ______  # Livre 1: "1984", "George Orwell", 1949, "disponible"
    ______  # Livre 2: "Python pour les nuls", "John Doe", 2020, "disponible"
    ______  # Livre 3: "Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954, "emprunté"
    ______  # Ajoutez au moins 2 livres supplémentaires
]

# 2. Affichez tous les livres disponibles
print("=== LIVRES DISPONIBLES ===")
______  # Parcourez la liste et affichez seulement les livres disponibles

# 3. Empruntez un livre (changez son statut)
livre_a_emprunter = "1984"
print(f"\n=== EMPRUNT DE '{livre_a_emprunter}' ===")
______  # Trouvez le livre et changez son statut en "emprunté"

# 4. Retournez un livre
livre_a_retourner = "Le Seigneur des Anneaux"
print(f"\n=== RETOUR DE '{livre_a_retourner}' ===")
______  # Trouvez le livre et changez son statut en "disponible"

# 5. Calculez des statistiques
print("\n=== STATISTIQUES ===")
total_livres = ______
livres_disponibles = 0
______  # Comptez les livres disponibles

pourcentage_disponibles = (livres_disponibles / total_livres) * 100

print(f"Total livres: {total_livres}")
print(f"Livres disponibles: {livres_disponibles}")
print(f"Pourcentage disponibles: {pourcentage_disponibles:.1f}%")

# 6. Recherche par auteur
auteur_recherche = "George Orwell"
print(f"\n=== RECHERCHE PAR AUTEUR '{auteur_recherche}' ===")
______  # Affichez tous les livres de cet auteur
```

---

## Exercice 2 : Debugging - Correction d'Erreurs

### Contexte

Ce code pour gérer un inventaire contient plusieurs erreurs de types et de syntaxe. Corrigez-les.

### Code à corriger :

```python
# EXERCICE 2 - CORRECTION D'ERREURS
# Corrigez toutes les erreurs dans ce code

# Données de l'inventaire
produits = ["pommes", "bananes", "oranges", "kiwis"]
stocks = [15, 8, 12, 5]
prix = [1.2, 0.8, 1.5, 2.0]

# 1. Affichage de l'inventaire
print("=== INVENTAIRE ===")
for i in range(len(produits))
    print(f"{produits[i]} - Stock: {stocks[i]} - Prix: {prix[i]}$")

# 2. Calcul du stock total
stock_total = sum(stocks)
print("\nStock total: {stock_total}")

# 3. Produit le plus cher
index_plus_cher = prix.index(max(prix))
produit_plus_cher = produits(index_plus_cher)
print(f"Produit le plus cher: {produit_plus_cher}")

# 4. Produits en rupture de stock
ruptures = []
for i in range(len(stocks)):
    if stocks[i] = 0:
        ruptures.append(produits[i])

print(f"Produits en rupture: {ruptures}")

# 5. Ajout d'un nouveau produit
nouveau_produit = "mangues"
nouveau_stock = 10
nouveau_prix = 1.8

produits.append(nouveau_produit)
stocks = stocks + nouveau_stock
prix.append(nouveau_prix)

print(f"\nAprès ajout de {nouveau_produit}:")
print(f"Produits: {produits}")
print(f"Stocks: {stocks}")
print(f"Prix: {prix}")

# 6. Vérification des types
print(f"\nTypes des données:")
print(f"Type de produits: type(produits)")
print(f"Type de stocks: type(stocks)")
print(f"Type de prix: type(prix)")
```

**Instructions :**

1. Identifiez et corrigez les erreurs
2. Le code doit fonctionner parfaitement après correction

---

## Exercice 3 : Complétion - Système de Notes (10 points)

### Contexte

Complétez le code pour créer un système de gestion des notes sans utiliser de fonctions.

### Code à compléter :

```python
# EXERCICE 3 - SYSTÈME DE NOTES
# Complétez les parties manquantes

# 1. Données des étudiants et leurs notes
# Utilisez un dictionnaire où la clé est le nom et la valeur est une liste de notes
etudiants_notes = {
    "Alice": [15, 18, 12],
    "Bob": [8, 14, 16],
    "Charlie": [20, 19, 18],
    "David": [10, 11, 9]
}

# 2. Affichage des notes de chaque étudiant
print("=== NOTES DES ÉTUDIANTS ===")
______  # Parcourez le dictionnaire et affichez nom + notes

# 3. Calcul des moyennes individuelles
print("\n=== MOYENNES INDIVIDUELLES ===")
moyennes = {}  # Dictionnaire pour stocker les moyennes

______  # Calculez la moyenne de chaque étudiant et stockez-la

# 4. Trouver le meilleur étudiant
print("\n=== CLASSEMENT ===")
meilleur_etudiant = None
meilleure_moyenne = 0

______  # Trouvez l'étudiant avec la meilleure moyenne

print(f"Meilleur étudiant: {meilleur_etudiant} avec {meilleure_moyenne:.2f}/20")

# 5. Statistiques de la classe
print("\n=== STATISTIQUES CLASSE ===")
toutes_notes = []
______  # Rassemblez toutes les notes dans une liste

moyenne_generale = ______  # Calculez la moyenne générale
meilleure_note = ______    # Trouvez la meilleure note
pire_note = ______         # Trouvez la pire note

print(f"Moyenne générale: {moyenne_generale:.2f}/20")
print(f"Meilleure note: {meilleure_note}/20")
print(f"Pire note: {pire_note}/20")

# 6. Distribution des notes
print("\n=== DISTRIBUTION DES NOTES ===")
notes_tranches = {
    "16-20": 0,
    "14-15": 0,
    "12-13": 0,
    "10-11": 0,
    "0-9": 0
}

______  # Comptez combien de notes tombent dans chaque tranche

for tranche, count in notes_tranches.items():
    print(f"{tranche}: {count} notes")

# 7. Ajout d'un nouvel étudiant
print("\n=== AJOUT NOUVEL ÉTUDIANT ===")
nouvel_etudiant = "Eve"
nouvelles_notes = [17, 16, 15]

______  # Ajoutez le nouvel étudiant au dictionnaire

print(f"Après ajout de {nouvel_etudiant}:")
print(etudiants_notes)
```

---

## Critères d'Évaluation

- **Exactitude** : Le code fonctionne correctement
- **Bon usage des types** : Listes, dictionnaires, tuples utilisés appropriément
- **Lisibilité** : Code clair et bien présenté
- **Gestion des données** : Manipulation correcte des structures

**Conseils :**

- Utilisez `for` loops pour parcourir les listes/dictionnaires
- Attention aux indices et aux types de données
- Testez chaque partie avant de passer à la suivante

Bon courage !
