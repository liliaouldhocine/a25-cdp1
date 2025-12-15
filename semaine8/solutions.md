# Solutions des Exercices

## Solution Exercice 1

### 1.1 : Code à Développer

```python
class Personne:
    def se_presenter(self):
        print("Je suis une personne")

# Utilisation
p = Personne()
p.se_presenter()
```

### 1.2 : Code à Finaliser

```python
class Salut:
    def dire_bonjour(self):
        print("Bonjour !")

personne = Salut()
personne.dire_bonjour()
```

### 1.3 : Code à Corriger

```python
class Animal:
    def faire_du_bruit(self):
        print("Bruit d'animal")

mon_animal = Animal()
mon_animal.faire_du_bruit()
```

## Solution Exercice 2

### 2.1 : Code à Développer

```python
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

# Création d'instances
livre1 = Livre("1984", "George Orwell")
livre2 = Livre("Le Petit Prince", "Saint-Exupéry")

print(f"{livre1.titre} par {livre1.auteur}")
print(f"{livre2.titre} par {livre2.auteur}")
```

### 2.2 : Code à Finaliser

```python
class Etudiant:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

etudiant1 = Etudiant("Alice", 20)
print(f"Nom: {etudiant1.nom}")
print(f"Age: {etudiant1.age}")
```

### 2.3 : Code à Corriger

```python
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

voiture = Voiture("Toyota", "Corolla")
print(voiture.marque)
```

## Solution Exercice 3

### 3.1 : Code à Développer

```python
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt de {montant}€")

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant}€")
            return True
        else:
            print("Fonds insuffisants")
            return False

    def afficher_solde(self):
        print(f"Solde de {self.titulaire}: {self.solde}€")

# Test
compte = CompteBancaire("Alice", 100)
compte.deposer(50)
compte.retirer(30)
compte.afficher_solde()
```

### 3.2 : Code à Finaliser

```python
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def calculer_surface(self):
        return self.longueur * self.largeur

rect = Rectangle(5, 3)
print(f"Périmètre: {rect.calculer_perimetre()}")
print(f"Surface: {rect.calculer_surface()}")
```

### 3.3 : Code à Corriger

```python
class Calculatrice:
    def __init__(self):
        self.resultat = 0

    def addition(self, a, b):
        self.resultat = a + b
        return self.resultat

    def soustraction(self, a, b):
        self.resultat = a - b
        return self.resultat

calc = Calculatrice()
result = calc.addition(5, 3)
print(f"Addition: {result}")
result = calc.soustraction(10, 4)
print(f"Soustraction: {result}")
```

## Solution Exercice 4

### 4.1 : Code à Développer

```python
class Employe:
    nombre_employes = 0

    def __init__(self, nom, poste):
        self.nom = nom
        self.poste = poste
        Employe.nombre_employes += 1

    @classmethod
    def afficher_nombre(cls):
        print(f"Nombre total d'employés: {cls.nombre_employes}")

# Test
e1 = Employe("Alice", "Développeuse")
e2 = Employe("Bob", "Designer")
Employe.afficher_nombre()  # Affiche 2
```

### 4.2 : Code à Finaliser

```python
class Produit:
    taux_tva = 0.2

    def __init__(self, nom, prix_ht):
        self.nom = nom
        self.prix_ht = prix_ht

    @classmethod
    def changer_tva(cls, nouveau_taux):
        cls.taux_tva = nouveau_taux

    def prix_ttc(self):
        return self.prix_ht + (self.prix_ht * self.taux_tva)

Produit.changer_tva(0.2)
p = Produit("Livre", 20)
print(f"Prix TTC: {p.prix_ttc()}")  # 24.0
```

### 4.3 : Code à Corriger

```python
class Mathematic:
    pi = 3.14159

    def __init__(self):
        # self.pi créerait un attribut d'instance, pas de classe
        pass

    @staticmethod
    def carre(x):
        return x * x  # Pas de self dans les méthodes statiques

# Test avec la variable de classe
print(f"PI: {Mathematic.pi}")

# Test méthode statique
print(f"Carré de 5: {Mathematic.carre(5)}")
```

## Solution Exercice 5

### 5.1 : Code à Développer

```python
class Utilitaire:
    @staticmethod
    def est_pair(nombre):
        return nombre % 2 == 0

    @staticmethod
    def celsius_vers_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def est_email_valide(email):
        return '@' in email and '.' in email and len(email) > 5

# Tests
print(f"10 est pair: {Utilitaire.est_pair(10)}")
print(f"25°C = {Utilitaire.celsius_vers_fahrenheit(25)}°F")
print(f"Email valide: {Utilitaire.est_email_valide('test@example.com')}")
```

### 5.2 : Code à Finaliser

```python
class Validateur:
    @staticmethod
    def est_positif(nombre):
        return nombre > 0

    @staticmethod
    def texte_valide(texte):
        return len(texte) >= 3

if Validateur.est_positif(10):
    print("Nombre valide")

if Validateur.texte_valide("ok"):
    print("Texte valide")
```

### 5.3 : Code à Corriger

```python
class Formateur:
    @staticmethod
    def majuscule(texte):
        return texte.upper()

    @staticmethod  # Devrait être statique aussi
    def minuscule(texte):
        return texte.lower()

# Utilisation correcte
resultat = Formateur.majuscule("test")
print(resultat)  # TEST

resultat2 = Formateur.minuscule("TEST")
print(resultat2)  # test
```

## Solution Exercice 6

### 6.1 : Code à Développer

```python
class CompteSecret:
    def __init__(self, code_secret):
        self.__code_secret = code_secret

    def verifier_code(self, code):
        return self.__code_secret == code

    def changer_code(self, ancien_code, nouveau_code):
        if self.verifier_code(ancien_code):
            self.__code_secret = nouveau_code
            print("Code changé")
            return True
        else:
            print("Ancien code incorrect")
            return False

# Test
compte = CompteSecret(1234)
print(f"Code 1234 valide: {compte.verifier_code(1234)}")
print(f"Code 0000 valide: {compte.verifier_code(0000)}")

# Tentative d'accès direct (ne fonctionne pas)
# print(compte.__code_secret)  # AttributeError
```

### 6.2 : Code à Finaliser

```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius  # Privé

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, valeur):
        if valeur < -273.15:
            print("Température impossible")
        else:
            self.__celsius = valeur

temp = Temperature(25)
print(f"Température: {temp.get_celsius()}°C")
temp.set_celsius(30)
print(f"Nouvelle température: {temp.get_celsius()}°C")
```

### 6.3 : Code à Corriger

```python
class Compte:
    def __init__(self, solde):
        self.__solde = solde

    def afficher_solde(self):
        print(f"Solde: {self.__solde}")  # Correction: self.__solde

    def __verifier_solde(self):  # Méthode privée
        return self.__solde > 0

    # Méthode publique pour accéder à la vérification
    def solde_positif(self):
        return self.__verifier_solde()

compte = Compte(100)
compte.afficher_solde()  # Affiche le solde
print(f"Solde positif: {compte.solde_positif()}")  # Utilise méthode publique

# Ces lignes échoueraient (attribut/méthode privé):
# print(compte.__solde)  # AttributeError
# compte.__verifier_solde()  # AttributeError
```

## Solution Exercice 7

### 7.1 : Système d'Inventaire

```python
class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def __str__(self):
        return f"{self.nom}: {self.quantite} x {self.prix}€ = {self.valeur()}€"

    def valeur(self):
        return self.prix * self.quantite

class Inventaire:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)
        print(f"Ajouté: {produit.nom}")

    def supprimer_produit(self, nom):
        for p in self.produits:
            if p.nom == nom:
                self.produits.remove(p)
                print(f"Supprimé: {nom}")
                return True
        print(f"Produit {nom} non trouvé")
        return False

    def chercher_produit(self, nom):
        for p in self.produits:
            if p.nom == nom:
                return p
        return None

    def valeur_totale(self):
        total = 0
        for p in self.produits:
            total += p.valeur()
        return total

    def afficher_inventaire(self):
        print("=== INVENTAIRE ===")
        for p in self.produits:
            print(p)
        print(f"Valeur totale: {self.valeur_totale()}€")

# Test
inventaire = Inventaire()
p1 = Produit("Livre", 15, 10)
p2 = Produit("Stylo", 2, 50)

inventaire.ajouter_produit(p1)
inventaire.ajouter_produit(p2)
inventaire.afficher_inventaire()
```

### 7.2 : Gestion de Cours

```python
class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter_note(self, note):
        if 0 <= note <= 20:
            self.notes.append(note)
            return True
        return False

    def moyenne(self):
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)

class Cours:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []

    def inscrire(self, etudiant):
        self.etudiants.append(etudiant)
        print(f"{etudiant.nom} inscrit au cours {self.nom}")

    def meilleur_etudiant(self):
        if not self.etudiants:
            return None

        meilleur = self.etudiants[0]
        for etudiant in self.etudiants:
            if etudiant.moyenne() > meilleur.moyenne():
                meilleur = etudiant
        return meilleur

    def statistiques(self):
        if not self.etudiants:
            return "Aucun étudiant"

        moyennes = [e.moyenne() for e in self.etudiants]
        moyenne_classe = sum(moyennes) / len(moyennes)

        meilleur = self.meilleur_etudiant()

        return f"""
Statistiques du cours {self.nom}:
- Nombre d'étudiants: {len(self.etudiants)}
- Moyenne de classe: {moyenne_classe:.1f}/20
- Meilleur étudiant: {meilleur.nom} ({meilleur.moyenne():.1f}/20)
"""

# Test
cours = Cours("Python")
alice = Etudiant("Alice")
bob = Etudiant("Bob")

alice.ajouter_note(15)
alice.ajouter_note(18)
bob.ajouter_note(12)
bob.ajouter_note(14)

cours.inscrire(alice)
cours.inscrire(bob)

print(cours.statistiques())
```

### 7.3 : Jeu de Cartes - Corrigé

```python
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur  # Correction: self.valeur
        self.couleur = couleur

    def __str__(self):
        valeurs = {1: "As", 11: "Valet", 12: "Dame", 13: "Roi"}
        valeur_affichage = valeurs.get(self.valeur, str(self.valeur))
        return f"{valeur_affichage} de {self.couleur}"  # Correction: self.

class Jeu:
    def __init__(self):
        self.cartes = []
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        for couleur in couleurs:
            for i in range(1, 14):
                self.cartes.append(Carte(i, couleur))

    def melanger(self):
        # Simulation simple sans import random
        # On inverse simplement l'ordre pour l'exemple
        self.cartes = self.cartes[::-1]

    def afficher(self):
        for carte in self.cartes[:5]:  # Affiche seulement les 5 premières
            print(carte)

# Test
jeu = Jeu()
print("Avant mélange:")
jeu.afficher()

jeu.melanger()
print("\nAprès mélange:")
jeu.afficher()
```
