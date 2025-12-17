# Solutions des Exercices Avancés

## Solution Exercice 1 : Système de Santé

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.sante = 100
        self.energie = 100
        self.est_vivant = True

    def manger(self):
        if not self.est_vivant:
            print(f"{self.nom} ne peut plus manger")
            return False

        if self.energie >= 10:
            self.energie -= 10
            print(f"{self.nom} mange (+10 satiété)")
            return True
        else:
            print(f"{self.nom} est trop fatigué pour manger")
            return False

    def dormir(self):
        if not self.est_vivant:
            print(f"{self.nom} ne peut plus dormir")
            return False

        self.energie = min(100, self.energie + 20)
        # Pendant le sommeil, la santé diminue légèrement
        self.sante = max(0, self.sante - 1)
        print(f"{self.nom} dort (+20 énergie, -1 santé)")

        if self.sante <= 0:
            self.est_vivant = False
            print(f"{self.nom} est mort pendant son sommeil")

        return True

    def vieillir(self):
        if not self.est_vivant:
            return False

        self.age += 1
        # La santé diminue de 5% chaque année
        self.sante = max(0, self.sante * 0.95)

        print(f"{self.nom} vieillit: {self.age} ans, santé: {self.sante:.1f}")

        if self.sante <= 0:
            self.est_vivant = False
            print(f"{self.nom} est mort de vieillesse")

        return True

    def soigner(self):
        if not self.est_vivant:
            print(f"{self.nom} ne peut plus être soigné")
            return False

        self.sante = min(100, self.sante + 30)
        print(f"{self.nom} est soigné: santé à {self.sante:.1f}")
        return True

    def __str__(self):
        etat = "vivant" if self.est_vivant else "mort"
        return f"{self.nom} ({self.age} ans) - Santé: {self.sante:.1f}, Énergie: {self.energie}, État: {etat}"

# Test
animal = Animal("Rex", 3)
print(animal)
animal.manger()
animal.dormir()
animal.vieillir()
animal.soigner()
print(animal)

# Vieillissement accéléré pour test
for _ in range(10):
    animal.vieillir()
print(animal)
```

## Solution Exercice 2 : Système de Reproduction

```python
class Animal:
    def __init__(self, nom, age, sexe):
        self.nom = nom
        self.age = age
        self.sexe = sexe

    def peut_se_reproduire(self):
        return self.age >= 2

    def est_meme_espece(self, autre):
        # Vérifie si les deux animaux sont de la même classe
        return type(self) == type(autre)

    def reproduire(self, autre):
        # Conditions de reproduction
        if not self.peut_se_reproduire():
            print(f"{self.nom} ne peut pas se reproduire (trop jeune)")
            return None

        if not autre.peut_se_reproduire():
            print(f"{autre.nom} ne peut pas se reproduire (trop jeune)")
            return None

        if self.sexe == autre.sexe:
            print("Reproduction impossible: même sexe")
            return None

        if not self.est_meme_espece(autre):
            print("Reproduction impossible: espèces différentes")
            return None

        # Création du bébé
        import random
        nom_bebe = f"Bébé_{self.nom[:2]}{autre.nom[:2]}"
        sexe_bebe = random.choice(['M', 'F'])

        # Créer le bon type d'animal
        if isinstance(self, Chien):
            race_bebe = f"{self.race}-{autre.race}"
            bebe = Chien(nom_bebe, 0, sexe_bebe, race_bebe)
        elif isinstance(self, Chat):
            # Mélange des couleurs
            couleurs = [self.couleur, autre.couleur]
            couleur_bebe = random.choice(couleurs)
            bebe = Chat(nom_bebe, 0, sexe_bebe, couleur_bebe)
        else:
            bebe = Animal(nom_bebe, 0, sexe_bebe)

        print(f"Nouveau bébé: {bebe.nom}")
        return bebe

    def __str__(self):
        return f"{self.nom} ({self.sexe}, {self.age} ans)"

class Chien(Animal):
    def __init__(self, nom, age, sexe, race):
        super().__init__(nom, age, sexe)
        self.race = race

    def __str__(self):
        return f"{super().__str__()}, Race: {self.race}"

class Chat(Animal):
    def __init__(self, nom, age, sexe, couleur):
        super().__init__(nom, age, sexe)
        self.couleur = couleur

    def __str__(self):
        return f"{super().__str__()}, Couleur: {self.couleur}"

# Test
chien_male = Chien("Max", 3, 'M', "Labrador")
chien_femelle = Chien("Luna", 4, 'F', "Golden")
chat_male = Chat("Tom", 2, 'M', "noir")
chat_femelle = Chat("Minette", 3, 'F', "blanc")

print("Test reproduction chien:")
bebe_chien = chien_male.reproduire(chien_femelle)
if bebe_chien:
    print(f"Bébé chien: {bebe_chien}")

print("\nTest reproduction chat:")
bebe_chat = chat_male.reproduire(chat_femelle)
if bebe_chat:
    print(f"Bébé chat: {bebe_chat}")

print("\nTest reproduction impossible:")
chien_male.reproduire(chat_femelle)  # Espèces différentes
chien_male.reproduire(chien_male)    # Même sexe
```

## Solution Exercice 3 : Système d'Interactions Sociales

```python
import random

class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.amis = []
        self.ennemis = []
        self.bonheur = 50

    def se_faire_ami(self, animal):
        if animal == self:
            print(f"{self.nom} ne peut pas être ami avec lui-même")
            return False

        if animal in self.amis:
            print(f"{self.nom} et {animal.nom} sont déjà amis")
            return True

        self.amis.append(animal)
        animal.amis.append(self)
        self.bonheur = min(100, self.bonheur + 15)
        animal.bonheur = min(100, animal.bonheur + 15)
        print(f"{self.nom} et {animal.nom} sont maintenant amis!")
        return True

    def se_faire_ennemi(self, animal):
        if animal == self:
            print(f"{self.nom} ne peut pas être ennemi avec lui-même")
            return False

        if animal in self.ennemis:
            print(f"{self.nom} et {animal.nom} sont déjà ennemis")
            return True

        self.ennemis.append(animal)
        animal.ennemis.append(self)
        self.bonheur = max(0, self.bonheur - 10)
        animal.bonheur = max(0, animal.bonheur - 10)
        print(f"{self.nom} et {animal.nom} sont maintenant ennemis!")
        return True

    def interagir(self, animal):
        if animal == self:
            print(f"{self.nom} ne peut pas interagir avec lui-même")
            return

        print(f"{self.nom} rencontre {animal.nom}")

        if animal in self.amis:
            print(f"{self.nom} joue avec son ami {animal.nom}")
            self.bonheur = min(100, self.bonheur + 10)
            animal.bonheur = min(100, animal.bonheur + 10)

        elif animal in self.ennemis:
            print(f"{self.nom} affronte son ennemi {animal.nom}")
            # Combat simple: le plus âgé gagne
            if self.age > animal.age:
                print(f"{self.nom} gagne le combat!")
                self.bonheur = min(100, self.bonheur + 5)
                animal.bonheur = max(0, animal.bonheur - 10)
            elif self.age < animal.age:
                print(f"{animal.nom} gagne le combat!")
                animal.bonheur = min(100, animal.bonheur + 5)
                self.bonheur = max(0, self.bonheur - 10)
            else:
                print("Match nul!")

        else:
            # Rencontre neutre
            print(f"{self.nom} fait connaissance avec {animal.nom}")
            if random.random() < 0.5:  # 50% chance
                self.se_faire_ami(animal)
            else:
                print(f"{self.nom} et {animal.nom} restent indifférents")

    def __str__(self):
        amis_noms = [a.nom for a in self.amis]
        ennemis_noms = [e.nom for e in self.ennemis]
        return f"{self.nom}: Bonheur={self.bonheur}, Amis={amis_noms}, Ennemis={ennemis_noms}"

class Chien(Animal):
    def interagir(self, animal):
        if isinstance(animal, Chien):
            print(f"{self.nom} renifle {animal.nom} (autre chien)")
            # Les chiens ont 80% de chance de devenir amis
            if random.random() < 0.8 and animal not in self.amis:
                self.se_faire_ami(animal)
        else:
            super().interagir(animal)

class Chat(Animal):
    def interagir(self, animal):
        print(f"{self.nom} observe {animal.nom} avec méfiance")
        # Les chats sont plus solitaires
        if random.random() < 0.3 and animal not in self.amis:  # 30% chance
            self.se_faire_ami(animal)
        elif random.random() < 0.4:  # 40% chance de devenir ennemi
            self.se_faire_ennemi(animal)

# Test
animaux = [
    Chien("Rex", 3),
    Chien("Max", 2),
    Chat("Misty", 4),
    Chat("Whiskers", 1)
]

print("=== Interactions sociales ===")
for i in range(len(animaux)):
    for j in range(i + 1, len(animaux)):
        animaux[i].interagir(animaux[j])
        print()

print("\n=== État final ===")
for animal in animaux:
    print(animal)
```

## Solution Exercice 4 : Système de Compétences

```python
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.niveau = 1
        self.experience = 0
        self.competences = {
            'chasse': 10,  # Valeur de base
            'defense': 10,
            'intelligence': 10
        }
        self.points_competence = 0

    def gagner_experience(self, montant):
        self.experience += montant
        print(f"{self.nom} gagne {montant} XP (total: {self.experience}/100)")

        while self.experience >= 100:
            self.niveau += 1
            self.experience -= 100
            self.points_competence += 3  # 3 points par niveau
            print(f"{self.nom} atteint le niveau {self.niveau}! (+3 points de compétence)")

    def entrainer(self, competence, heures=1):
        if competence not in self.competences:
            print(f"Compétence {competence} inconnue")
            return False

        gain_base = heures * 5
        # Bonus/malus selon le type d'animal
        if isinstance(self, Chien) and competence == 'defense':
            gain_base *= 1.5  # 50% bonus pour les chiens en défense
        elif isinstance(self, Chat) and competence == 'chasse':
            gain_base *= 1.5  # 50% bonus pour les chats en chasse

        self.competences[competence] = min(100, self.competences[competence] + gain_base)
        self.gagner_experience(heures * 10)

        print(f"{self.nom} s'entraîne en {competence}: +{gain_base:.1f}")
        return True

    def ameliorer_competence(self, competence):
        if self.points_competence <= 0:
            print(f"{self.nom} n'a plus de points de compétence")
            return False

        if competence not in self.competences:
            print(f"Compétence {competence} inconnue")
            return False

        if self.competences[competence] >= 100:
            print(f"{competence} est déjà au maximum")
            return False

        self.competences[competence] = min(100, self.competences[competence] + 10)
        self.points_competence -= 1
        print(f"{self.nom} améliore {competence} à {self.competences[competence]}")
        return True

    def efficacite(self, competence):
        if competence not in self.competences:
            return 0

        base = self.competences[competence]
        bonus_niveau = self.niveau * 2
        return min(100, base + bonus_niveau)

    def __str__(self):
        competences_str = ", ".join([f"{k}:{v}" for k, v in self.competences.items()])
        return f"{self.nom} Niv.{self.niveau} (XP: {self.experience}/100) - {competences_str} - Points: {self.points_competence}"

class Chien(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        # Chiens commencent avec plus de défense
        self.competences['defense'] = 20
        self.competences['intelligence'] = 15

class Chat(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        # Chats commencent avec plus de chasse
        self.competences['chasse'] = 25
        self.competences['defense'] = 5

# Test
print("=== Système de compétences ===")

rex = Chien("Rex", 3)
misty = Chat("Misty", 2)

print("Initial:")
print(rex)
print(misty)

print("\n=== Entraînement ===")
rex.entrainer('defense', 2)  # Chien bonus en défense
misty.entrainer('chasse', 2)  # Chat bonus en chasse

print("\n=== Amélioration avec points ===")
# Gagner assez d'XP pour monter de niveau
rex.gagner_experience(120)  # Devrait donner 1 niveau
rex.ameliorer_competence('defense')
rex.ameliorer_competence('intelligence')

print("\n=== Efficacité ===")
print(f"Rex défense: {rex.efficacite('defense')}")
print(f"Misty chasse: {misty.efficacite('chasse')}")

print("\n=== État final ===")
print(rex)
print(misty)
```

## Solution Exercice 5 : Système de Territoire

```python
import math

class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.position = (0, 0)
        self.territoire = []
        self.vitesse = 5
        self.rayon_territoire = 3  # Rayon autour de chaque point marqué

    def se_deplacer(self, x, y):
        # Calcul de la distance Euclidienne
        distance = math.sqrt((x - self.position[0])**2 + (y - self.position[1])**2)

        if distance <= self.vitesse:
            ancienne_position = self.position
            self.position = (x, y)
            print(f"{self.nom} se déplace de {ancienne_position} à {self.position}")
            return True
        else:
            # Déplacement partiel dans la direction
            ratio = self.vitesse / distance
            new_x = self.position[0] + (x - self.position[0]) * ratio
            new_y = self.position[1] + (y - self.position[1]) * ratio
            ancienne_position = self.position
            self.position = (round(new_x), round(new_y))
            print(f"{self.nom} se déplace partiellement vers ({x}, {y}) -> {self.position}")
            return False

    def marquer_territoire(self):
        # Évite les doublons proches
        for point in self.territoire:
            distance = math.sqrt((self.position[0] - point[0])**2 +
                                (self.position[1] - point[1])**2)
            if distance < 2:  # Trop proche d'un point existant
                print(f"{self.nom}: position trop proche d'un territoire existant")
                return False

        self.territoire.append(self.position)
        print(f"{self.nom} marque son territoire à {self.position}")
        return True

    def est_dans_son_territoire(self, x, y):
        for point in self.territoire:
            distance = math.sqrt((x - point[0])**2 + (y - point[1])**2)
            if distance <= self.rayon_territoire:
                return True
        return False

    def defendre_territoire(self, autre_animal):
        if self.est_dans_son_territoire(*autre_animal.position):
            print(f"{self.nom} défend son territoire contre {autre_animal.nom}!")
            # Force l'autre animal à reculer
            autre_animal.position = (
                autre_animal.position[0] - 2,
                autre_animal.position[1] - 2
            )
            print(f"{autre_animal.nom} est repoussé à {autre_animal.position}")
            return True
        return False

    def superficie_territoire(self):
        # Estimation basée sur le nombre de points et le rayon
        return len(self.territoire) * (math.pi * self.rayon_territoire**2)

    def __str__(self):
        return f"{self.nom} à {self.position}, Territoire: {len(self.territoire)} points, Superficie: {self.superficie_territoire():.1f}"

class Chien(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        self.vitesse = 8  # Chiens plus rapides
        self.rayon_territoire = 5  # Territoire plus grand

    def marquer_territoire(self):
        # Chiens marquent plus fréquemment
        print(f"{self.nom} lève la patte...")
        return super().marquer_territoire()

class Chat(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        self.vitesse = 6
        self.rayon_territoire = 2  # Territoire plus petit mais bien défendu

    def defendre_territoire(self, autre_animal):
        print(f"{self.nom} siffle et griffe!")
        return super().defendre_territoire(autre_animal)

# Test
print("=== Système de territoire ===")

rex = Chien("Rex", 3)
misty = Chat("Misty", 2)

print("\n=== Déplacements et marquage ===")
rex.se_deplacer(3, 4)
rex.marquer_territoire()
rex.se_deplacer(8, 6)
rex.marquer_territoire()

misty.se_deplacer(1, 1)
misty.marquer_territoire()
misty.se_deplacer(2, 3)
misty.marquer_territoire()

print("\n=== Vérification territoire ===")
print(f"Rex à (8,6): {rex.est_dans_son_territoire(8, 6)}")
print(f"Misty à (8,6): {misty.est_dans_son_territoire(8, 6)}")

print("\n=== Défense territoire ===")
# Misty entre dans le territoire de Rex
misty.se_deplacer(7, 5)  # Proche d'un point de Rex
rex.defendre_territoire(misty)

print("\n=== État final ===")
print(rex)
print(misty)
```
