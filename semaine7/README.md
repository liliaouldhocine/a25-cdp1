# Exercices Collaboratifs Git/GitHub pour Débutants

## Objectifs

- Apprendre à travailler en équipe avec Git
- Comprendre les conflits et leur résolution
- Maîtriser le workflow collaboratif de base

## Prérequis pour l'Equipe

- Chaque membre a un compte GitHub
- Git installé sur chaque machine
- Communication établie (Discord, Teams, etc.)

---

## Exercice 1 : Premier Projet Collaboratif Simple

### Scénario 1

Créer ensemble un "menu du restaurant" en Python

### Tâches par Rôle (4 personnes)

**Personne 1 :** Chef de projet / Git Master

- Crée le dépôt sur GitHub
- Initialise le projet
- Crée le fichier `menu.py` avec structure de base
- Gère les pull requests

**Personne 2 :** Développeur Entrées

- Crée une fonction `afficher_entrees()`
- Ajoute 3 entrées au menu
- Pousse ses changements

**Personne 3 :** Développeur Plats Principaux

- Crée une fonction `afficher_plats_principaux()`
- Ajoute 3 plats principaux
- Pousse ses changements

**Personne 4 :** Développeur Desserts

- Crée une fonction `afficher_desserts()`
- Ajoute 3 desserts
- Crée le `main()` pour tout afficher

### Instructions Techniques

```python
# Structure de départ (Personne 1)
def main():
    print("=== MENU DU RESTAURANT ===")
    # Les autres ajouteront leur code ici

if __name__ == "__main__":
    main()
```

### Défis Git

1. Chacun travaille sur sa propre branche
2. Résoudre un conflit simulé (deux personnes modifient le même plat)
3. Faire un merge en équipe

---

## Exercice 2 : Gestion de Bibliothèque Partagée

### Scénario 2

Créer un système de gestion de livres collaboratif

### Tâches Divisées

**Fichier : `livres.py`**

```python
# Structure initiale
bibliotheque = []

def ajouter_livre(titre, auteur):
    pass

def afficher_livres():
    pass

def rechercher_livre(titre):
    pass
```

**Répartition :**

- Membre 1 : Implémente `ajouter_livre()`
- Membre 2 : Implémente `afficher_livres()`
- Membre 3 : Implémente `rechercher_livre()`
- Membre 4 : Crée les tests dans `test_bibliotheque.py`

### Défis Collaboration

1. Travailler sur le même fichier sans conflits
2. Utiliser les issues GitHub pour signaler des problèmes
3. Faire des code reviews entre membres

---

## Exercice 3 : Jeu du Pendu Collaboratif

### Scénario 3

Développer un jeu du pendu en équipe

### Architecture du Projet

```txt
pendu/
├── mots.py          (Membre 1 : liste de mots)
├── affichage.py     (Membre 2 : affichage ASCII)
├── jeu.py           (Membre 3 : logique du jeu)
└── main.py          (Membre 4 : point d'entrée)
```

### Tâches Détail

**Membre 1 - `mots.py` :**

```python
def choisir_mot():
    mots = ["python", "programmation", "github", "collaboration"]
    # Retourner un mot aléatoire
```

**Membre 2 - `affichage.py` :**

```python
def afficher_pendu(erreurs):
    # Dessins ASCII selon le nombre d'erreurs
```

**Membre 3 - `jeu.py` :**

```python
def jouer_tour(mot_secret, lettres_trouvees, lettre):
    # Logique du jeu
```

**Membre 4 - `main.py` :**

```python
# Importe tous les modules et orchestre le jeu
```

### Workflow Git

1. Chaque membre crée sa branche : `feature-mots`, `feature-affichage`, etc.
2. Chacun développe indépendamment
3. Merge progressif dans `develop`
4. Résolution des dépendances entre modules

---

## Exercice 4 : Calculateur d'IMC avec Interface

### Scénario 4

Créer un calculateur d'IMC avec différentes fonctionnalités

### Modules à Développer

**Membre 1 :** `calculs.py`

```python
def calculer_imc(poids, taille):
    # IMC = poids / taille²

def interpreter_imc(imc):
    # Retourne la catégorie
```

**Membre 2 :** `interface.py`

```python
def demander_infos():
    # Demande poids et taille

def afficher_resultat(imc, categorie):
    # Affiche joliment
```

**Membre 3 :** `historique.py`

```python
def sauvegarder_calcul(nom, imc):
    # Sauvegarde dans un fichier

def afficher_historique():
    # Lit le fichier
```

**Membre 4 :** `main.py` et tests

```python
# Orchestre tout + tests unitaires
```

### Défis Avancés

1. Gérer les merge conflicts sur `main.py`
2. Utiliser Git Flow (branches feature/develop/main)
3. Faire des rebases pour garder l'historique propre

---

## Exercice 5 : Système de Tickets de Support

### Scénario 5

Créer un système simple de gestion de tickets

### Structure Collaborative

```txt
tickets/
├── ticket.py        (Classe Ticket - Membre 1)
├── gestion.py       (CRUD tickets - Membre 2)
├── interface.py     (Menu utilisateur - Membre 3)
├── sauvegarde.py    (Fichier JSON - Membre 4)
└── main.py          (Tous ensemble)
```

### Scénario de Conflit Planifié

Etape 1 : Tous modifient `main.py` en même temps
Etape 2 : Résolution des conflits en équipe
Etape 3 : Revue de code croisée

---

## Guide Pratique Git pour Débutants

### Commandes Essentielles pour l'Exercice

```bash
# Cloner le dépôt
git clone <url-du-depot>

# Créer sa branche
git checkout -b ma-fonctionnalite

# Travailler normalement
git add .
git commit -m "Description claire"

# Mettre à jour avec la branche principale
git pull origin main

# Pousser sa branche
git push origin ma-fonctionnalite

# Sur GitHub : créer Pull Request
```

### Règles d'Or pour l'Equipe

1. Toujours pull avant de push
2. Messages de commit clairs : "feat: ajout fonction afficher_menu"
3. Branches descriptives : `feature-menu`, `fix-bug-affichage`
4. Communication : Parler avant de merger
5. Code reviews : Toujours 1 autre membre approuve

### Rôles Rotatifs

Chaque exercice, changez les rôles :

- Git Manager (gère les merges)
- Quality Checker (vérifie le code)
- Documenteur (met à jour README)
- Testeur (écrit les tests)

---

## Exercice Final : Projet Libre

### Consignes

1. Choix du projet : Vote d'équipe (jeu, utilitaire, etc.)
2. Planification : Découpage en 4 parties égales
3. Implémentation : 1h de code synchronisé
4. Intégration : 30 min de merge et tests
5. Rétrospective : 15 min de discussion

### Critères de Succès

- Tous les membres ont commit au moins 2 fois
- Pas de code cassé après merge
- README.md complet
- Projet fonctionnel

### Template README.md Collaboratif

```markdown
# [Nom du Projet]

## Equipe

- [Membre 1] - Rôle/Fonctionnalité
- [Membre 2] - Rôle/Fonctionnalité
- [Membre 3] - Rôle/Fonctionnalité
- [Membre 4] - Rôle/Fonctionnalité

## Installation

1. git clone [url]
2. cd [projet]
3. python main.py

## Fonctionnalités

- [ ] Fonctionnalité 1 (par [Membre])
- [ ] Fonctionnalité 2 (par [Membre])
- [ ] Fonctionnalité 3 (par [Membre])
- [ ] Fonctionnalité 4 (par [Membre])

## Leçons Apprises

- Comment résoudre les conflits Git
- L'importance de la communication
- etc.
```

## Bonus : Script d'Initialisation pour l'Equipe

```python
# setup_team.py - À exécuter par le chef de projet
def initialiser_projet():
    print("=== INITIALISATION DU PROJET ===")
    print("1. Créer dépôt GitHub")
    print("2. Cloner sur toutes les machines")
    print("3. Créer branches :")
    print("   - git checkout -b feature-membre1")
    print("   - git checkout -b feature-membre2")
    print("   - git checkout -b feature-membre3")
    print("   - git checkout -b feature-membre4")
    print("4. Commencer à coder !")

if __name__ == "__main__":
    initialiser_projet()
```
