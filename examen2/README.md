### **Examen Progressif : Système de Gestion d'une Flotte de Véhicules**

**Durée :** 2 heures  
**Remise :** Un dossier `.zip` avec les fichiers `etape1.py`, `etape2.py`, etc.  
**Consigne Spéciale :** Il est **interdit de modifier les fichiers des étapes précédentes**. Chaque nouvel exercice doit partir d'une **copie du fichier précédent** que vous modifierez et renommerez. Cela simule l'évolution d'un projet.

---

### **Étape 1 : La Fondation**

**Fichier :** `etape1.py`  
**Objectif :** Créer la classe de base avec attributs et méthodes fondamentales.

**Énoncé :**
Créez la classe `Vehicule` qui servira de base à tout le système.

1.  Le constructeur `__init__(self, marque, modele, annee, immatriculation)` initialise ces quatre attributs d'instance.
2.  Ajoutez une méthode d'instance `se_decrire(self)` qui retourne une chaîne formatée : `"[marque] [modele] ([annee]), immat. [immatriculation]"`.
3.  Ajoutez une méthode d'instance `demarrer(self)` qui affiche `"Le véhicule [immatriculation] démarre."`.

**À tester :**

```python
v = Vehicule("Renault", "Clio", 2020, "AB-123-CD")
print(v.se_decrire())
v.demarrer()
```

---

### **Étape 2 : Spécialisation par Héritage**

**Fichier :** `etape2.py` (Copie et modification de `etape1.py`)  
**Objectif :** Introduire l'héritage et le polymorphisme.

**Énoncé :**

1.  **Conservez intacte** la classe `Vehicule` de l'étape 1.
2.  Créez une classe `Voiture` qui hérite de `Vehicule`.
    - Son constructeur prend les paramètres de `Vehicule` **plus** `nombre_portes`.
    - Utilisez `super().__init__()`.
    - **Surchargez** `se_decrire(self)` pour ajouter à la fin de la description : `" | Portes: [nombre_portes]"`.
3.  Créez une classe `Camion` qui hérite de `Vehicule`.
    - Son constructeur prend les paramètres de `Vehicule` **plus** `charge_utile` (en tonnes).
    - Utilisez `super().__init__()`.
    - **Surchargez** `se_decrire(self)` pour ajouter : `" | Charge utile: [charge_utile]t"`.
    - **Surchargez** `demarrer(self)` pour afficher un message spécifique : `"Le camion [immatriculation] démarre avec un grondement."`.

**À tester :**

```python
v = Voiture("Peugeot", "308", 2021, "EF-456-GH", 5)
c = Camion("Volvo", "FH16", 2019, "XX-999-YY", 19)
print(v.se_decrire())
print(c.se_decrire())
c.demarrer()  # Doit afficher le message spécifique
```

---

### **Étape 3 : Contrôle et Encapsulation**

**Fichier :** `etape3.py` (Copie et modification de `etape2.py`)  
**Objectif :** Ajouter un état interne contrôlé via l'encapsulation.

**Énoncé :**

1.  Modifiez le constructeur de `Vehicule` pour y ajouter un attribut "privé" `_en_marche`, initialisé à `False`.
2.  Modifiez la méthode `demarrer(self)` pour qu'elle :
    - Vérifie si `_en_marche` est `False`.
    - Si oui, elle le passe à `True` ET affiche le message.
    - Sinon, elle affiche `"Le véhicule [immatriculation] est déjà en marche."`.
3.  Ajoutez une nouvelle méthode d'instance `arreter(self)` qui fait l'opération inverse.
4.  **Défi (important) :** Assurez-vous que la surcharge de `demarrer` dans `Camion` **conserve cette logique** (vérification de `_en_marche`). Elle doit afficher son message spécifique **uniquement lors d'un vrai démarrage**.

**À tester :**

```python
c = Camion("Volvo", "FH16", 2019, "XX-999-YY", 19)
c.demarrer()  # "Le camion XX-999-YY démarre avec un grondement."
c.demarrer()  # "Le véhicule XX-999-YY est déjà en marche." (Logique de Vehicule)
c.arreter()
c.demarrer()  # Message spécifique du camion à nouveau
```

---

### **Étape 4 : Méthodes de Classe et Gestion de Flotte**

**Fichier :** `etape4.py` (Copie et modification de `etape3.py`)  
**Objectif :** Introduire des concepts au niveau de la classe.

**Énoncé :**

1.  Ajoutez à la classe `Vehicule` une **variable de classe** `_vehicules_crees = []`.
2.  Modifiez le constructeur `__init__` de `Vehicule` pour qu'il ajoute **l'instance elle-même** (`self`) à cette liste à chaque création.
3.  Créez une **méthode de classe** `afficher_flotte(cls)` qui :
    - Parcourt `cls._vehicules_crees`.
    - Affiche pour chaque véhicule son immatriculation et son état (`"en marche"` ou `"à l'arrêt"`).
4.  Créez une **méthode statique** `verifier_immatriculation(immat)` qui retourne `True` si l'immatriculation passée en argument contient un tiret, sinon `False`.

**À tester :**

```python
v1 = Voiture("Peugeot", "308", 2021, "EF-456-GH", 5)
v2 = Camion("Renault", "T", 2020, "ZZ-TOP-01", 15)
v1.demarrer()
Vehicule.afficher_flotte()
print(Vehicule.verifier_immatriculation("123456"))  # False
```

---

### **Étape 5 : Composition et Projet Synthèse**

**Fichier :** `etape5.py` (Copie et modification de `etape4.py`)  
**Objectif :** Combiner les concepts dans un système plus large.

**Énoncé :**

1.  Créez une nouvelle classe **`Flotte`** (dans le même fichier).
    - Constructeur : `__init__(self, nom)` initialise `nom` et une liste vide `_vehicules`.
    - Méthode `ajouter_vehicule(self, vehicule)` : ajoute un objet `Vehicule` à la liste.
    - Méthode `generer_rapport(self)` :
      - Affiche `"=== Rapport de la flotte: [nom] ==="`.
      - Utilise `Vehicule.afficher_flotte()` pour lister tous les véhicules créés.
      - Affiche aussi uniquement les véhicules **de cette flotte** et leur description.
2.  **Modifiez la méthode de classe `Vehicule.afficher_flotte(cls)`** pour qu'elle accepte un paramètre optionnel `flotte=None`.
    - Si `flotte` n'est pas fourni, elle se comporte comme avant.
    - Si une `flotte` (objet de la classe `Flotte`) est fournie, elle n'affiche que les véhicules présents dans `flotte._vehicules`.

**À tester :**

```python
# Création des véhicules
v1 = Voiture("Toyota", "Yaris", 2022, "AA-111-BB", 3)
v2 = Camion("MAN", "TGX", 2021, "CC-222-DD", 20)
v3 = Voiture("Fiat", "500", 2023, "EE-333-FF", 3)

# Création et peuplement des flottes
flotte_a = Flotte("Livraisons Urbaines")
flotte_a.ajouter_vehicule(v1)
flotte_a.ajouter_vehicule(v2)

flotte_b = Flotte("Service Commercial")
flotte_b.ajouter_vehicule(v3)

# Rapports
print("\n--- Tous les véhicules créés ---")
Vehicule.afficher_flotte()

print("\n--- Rapport flotte A ---")
flotte_a.generer_rapport()

print("\n--- Rapport flotte B ---")
flotte_b.generer_rapport()
```

---

### **Logique d'Évaluation**

- **Respect de la progression et consignes (non-modification des anciens fichiers)**
- **Étape 1 (Fondation)**
- **Étape 2 (Héritage/Polymorphisme)**
- **Étape 3 (Encapsulation/État)**
- **Étape 4 (Méthodes de classe/statiques)**
- **Étape 5 (Composition/Synthèse)**
