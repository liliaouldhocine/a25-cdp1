# Exercices Avancés sur les Classes Animal

## Exercice 1 : Système de Santé et Vieillissement

### Code à Développer

```python
# Modifiez la classe Animal pour ajouter un système de santé:
# 1. Ajoutez les attributs: sante (0-100), energie (0-100), est_vivant (booléen)
# 2. La santé diminue de 5% chaque année dans vieillir()
# 3. L'énergie diminue de 10 quand l'animal mange ou dort
# 4. L'énergie se recharge de 20 quand l'animal dort
# 5. Si santé <= 0, est_vivant devient False
# 6. Méthode soigner() qui augmente la santé de 30 (max 100)
# 7. Méthode vieillir() qui augmente l'âge et affecte la santé

class Animal:
    # À modifier
```

### Code à Finaliser

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.sante = 100
        self.energie = 100
        self.est_vivant = True

    def manger(self):
        if self.est_vivant:
            if self.energie >= 10:
                self.energie -= 10
                print(f"{self.nom} mange (+10 satiété)")
                return True
            else:
                print(f"{self.nom} est trop fatigué pour manger")
                return False
        else:
            print(f"{self.nom} ne peut plus manger")
            return False

    def dormir(self):
        if self.est_vivant:
            self.energie = min(100, self.energie + 20)
            print(f"{self.nom} dort (+20 énergie)")
            # La santé diminue pendant le sommeil ?
            # À compléter
        else:
            print(f"{self.nom} ne peut plus dormir")

    def vieillir(self):
        # À compléter: augmente l'âge, santé diminue de 5%
        pass

    def soigner(self):
        # À compléter
        pass

    def __str__(self):
        # À modifier pour inclure santé et énergie
        pass
```

## Exercice 2 : Système de Reproduction

### Code à Développer

```python
# Créez un système de reproduction pour les animaux:
# 1. Ajoutez l'attribut sexe ('M' ou 'F')
# 2. Ajoutez l'attribut peut_se_reproduire (booléen, True si age >= 2)
# 3. Méthode reproduire(autre_animal) qui:
#    - Vérifie si les deux animaux peuvent se reproduire
#    - Vérifie s'ils sont de sexe opposé
#    - Vérifie s'ils sont de la même espèce
#    - Crée un nouvel animal avec un nom généré
# 4. Pour Chat et Chien, surchargez reproduire() pour créer un Chat/Chien

class Animal:
    # À modifier
```

### Code à Corriger

```python
class Animal:
    def __init__(self, nom, age, sexe):
        self.nom = nom
        self.age = age
        self.sexe = sexe

    def peut_se_reproduire(self):
        return self.age >= 2

    def reproduire(self, autre):
        if self.peut_se_reproduire() and autre.peut_se_reproduire():
            if self.sexe != autre.sexe:
                # Problème: comment savoir si même espèce ?
                nom_bebe = f"{self.nom[:3]}{autre.nom[:3]}"
                bebe = Animal(nom_bebe, 0, 'M' if random() > 0.5 else 'F')
                return bebe
        return None

# Le code a plusieurs problèmes à corriger
```

## Exercice 3 : Système d'Interactions Sociales

### Code à Développer

```python
# Créez un système d'interactions entre animaux:
# 1. Attribut amis (liste d'animaux)
# 2. Attribut ennemis (liste d'animaux)
# 3. Méthode se_faire_ami(animal) qui ajoute aux amis
# 4. Méthode se_faire_ennemi(animal) qui ajoute aux ennemis
# 5. Méthode interagir(animal) qui:
#    - Si ami: augmente bonheur des deux
#    - Si ennemi: combat possible
#    - Si neutre: 50% chance de devenir ami
# 6. Différentes interactions pour Chat et Chien

class Animal:
    # À développer
```

### Code à Finaliser

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.amis = []
        self.ennemis = []
        self.bonheur = 50  # 0-100

    def se_faire_ami(self, animal):
        if animal not in self.amis and animal != self:
            self.amis.append(animal)
            animal.amis.append(self)  # Réciproque
            print(f"{self.nom} et {animal.nom} sont maintenant amis")
            # À compléter: augmenter bonheur

    def se_faire_ennemi(self, animal):
        # À compléter
        pass

    def interagir(self, animal):
        if animal in self.amis:
            print(f"{self.nom} joue avec {animal.nom}")
            self.bonheur = min(100, self.bonheur + 10)
            animal.bonheur = min(100, animal.bonheur + 10)
        elif animal in self.ennemis:
            # À compléter: comportement d'ennemi
            pass
        else:
            # 50% chance de devenir ami
            # À compléter
            pass

    def __str__(self):
        # À modifier pour inclure amis/ennemis
        return f"{self.nom}: {len(self.amis)} amis, {len(self.ennemis)} ennemis"
```

## Exercice 4 : Système de Compétences et Niveaux

### Code à Développer

```python
# Créez un système de compétences pour les animaux:
# 1. Attribut niveau (1-10)
# 2. Attribut experience (0-100)
# 3. Dictionnaire competences: {'chasse': 0, 'defense': 0, 'intelligence': 0}
# 4. Méthode gagner_experience(montant) qui augmente l'expérience
# 5. Quand experience >= 100, niveau augmente, expérience revient à 0
# 6. Méthode entrainer(competence) qui augmente la compétence
# 7. Chat: meilleur en chasse, Chien: meilleur en défense
```

### Code à Finaliser

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.niveau = 1
        self.experience = 0
        self.competences = {
            'chasse': 0,
            'defense': 0,
            'intelligence': 0
        }

    def gagner_experience(self, montant):
        self.experience += montant
        if self.experience >= 100:
            self.niveau += 1
            self.experience = self.experience - 100
            print(f"{self.nom} atteint le niveau {self.niveau}!")
            # À compléter: points de compétence à distribuer

    def entrainer(self, competence, heures=1):
        if competence in self.competences:
            gain = heures * 5
            self.competences[competence] = min(100, self.competences[competence] + gain)
            self.gagner_experience(heures * 10)
            print(f"{self.nom} s'est entraîné en {competence} (+{gain})")
        else:
            print(f"Compétence {competence} inconnue")

    def efficacite(self, competence):
        # À compléter: calcul basé sur niveau et compétence
        pass

    def __str__(self):
        # À compléter: afficher niveau et compétences
        pass
```

## Exercice 5 : Système de Territoire et Déplacements

### Code à Développer

```python
# Créez un système de territoire pour les animaux:
# 1. Attribut position (x, y)
# 2. Attribut territoire (liste des positions contrôlées)
# 3. Attribut vitesse (1-10)
# 4. Méthode se_deplacer(x, y) qui vérifie si le déplacement est possible
# 5. Méthode marquer_territoire() qui ajoute la position actuelle au territoire
# 6. Méthode est_dans_son_territoire(x, y) qui vérifie
# 7. Chat: territoire plus petit mais défendu agressivement
# 8. Chien: territoire plus grand mais moins défendu
```

### Code à Corriger

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.position = (0, 0)
        self.territoire = []
        self.vitesse = 5

    def se_deplacer(self, x, y):
        distance = abs(x - self.position[0]) + abs(y - self.position[1])
        if distance <= self.vitesse:
            self.position = (x, y)
            print(f"{self.nom} se déplace vers ({x}, {y})")
            return True
        else:
            print(f"Trop loin! Vitesse max: {self.vitesse}")
            return False

    def marquer_territoire(self):
        # Problème: comment éviter les doublons ?
        self.territoire.append(self.position)

    def est_dans_son_territoire(self, x, y):
        # Problème: ne vérifie que l'exacte position
        return (x, y) in self.territoire

    # À corriger: prendre en compte un rayon autour des positions
```
