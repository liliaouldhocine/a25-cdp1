# Étape 1

class Animal():

    def __init__(self, nom, age) -> None:
        self.nom = nom 
        self.age = age
    
    def manger(self):
        print(f"{self.nom} mange")

    def dormir(self):
        print(f"{self.nom} dort")

    def __str__(self) -> str:
        return f"Animal: {self.nom}, âge: {self.age} ans"
    
    def __eq__(self, value) -> bool:
        return self.age == value.age and self.nom == value.nom
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        if age >= 0:
            self.age = age

class Chien(Animal):
    
    def __init__(self, nom, age, race) -> None:
        Animal.__init__(self, nom, age) 
        self.race = race

    def aboyer(self): 
        print(f"{self.nom} aboie: Woof!")

    def __str__(self) -> str:
        animal_str = Animal.__str__(self)
        return f"{animal_str}, race: {self.race}"

un_chien = Chien("Fido", 5, "Golden Retriever")
# un_chien.manger()
# un_chien.dormir()
# un_chien.aboyer()
# print(un_chien)

class Chat(Animal):

    def __init__(self, nom, age, couleur) -> None:
        Animal.__init__(self, nom, age)
        self.couleur = couleur

    def miauler(self):
        print(f"{self.nom} miaule: Miaou!")

    def __str__(self) -> str:
        animal_str = Animal.__str__(self)
        return f"{animal_str}, couleur: {self.couleur}"
    
un_chat = Chat("Gérard", 2, "noire et orange")
# un_chat.dormir()
# un_chat.manger()
# un_chat.miauler()
# print(un_chat)

class Compagnon():
    def __init__(self, proprietaire) -> None:
        self.proprietaire = proprietaire

    def jouer(self):
        print(f"Je joue avec {self.proprietaire}")

class AnimalDomestique(Animal, Compagnon):
    def __init__(self, nom, age, proprietaire) -> None:
        Animal.__init__(self, nom, age)
        Compagnon.__init__(self, proprietaire)

    def __str__(self) -> str:
        animal_str = Animal.__str__(self)
        return f"{animal_str}, propriétaire: {self.proprietaire}"
    
un_animal_domestique = AnimalDomestique("Achile", 7, "Mathieu")
un_animal_domestique.manger()
un_animal_domestique.dormir()
un_animal_domestique.jouer()
print(un_animal_domestique)