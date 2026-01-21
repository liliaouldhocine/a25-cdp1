la_liste = [1, 5, 7, 84, 52, 43]

# def map_by(une_fonction, une_liste):
#     new_liste = []
#     for item in une_liste:
#         new_liste.append(une_fonction(item))
#     return new_liste

# Utilisation de closer
def multiplier_item(factor):
    def multiplier(item):
        return item * factor
    return multiplier # retourne une fonction

# multiplier_par_2 = multiplier_item(2)
# multiplier_par_3 = multiplier_item(3)
# multiplier_par_4 = multiplier_item(4)
# multiplier_par_5 = multiplier_item(5)

# print("-------- utilisation de map_by --------")
# print(map_by(multiplier_par_2, la_liste ))
# print(map_by(multiplier_par_3, la_liste))
# print(map_by(multiplier_par_5, la_liste))
# print("-------- utilisation de map --------")
# print(list(map(multiplier_par_2, la_liste )))
# print(list(map(multiplier_par_3, la_liste)))
# print(list(map(multiplier_par_5, la_liste)))
print("-------- utilisation de map en utilisant multiplier_item --------")
print(list(map(multiplier_item(2), la_liste )))
print(list(map(multiplier_item(3), la_liste)))
print(list(map(multiplier_item(5), la_liste)))

def doubler(item):
    return item * 2

# map
# print(list(map(double, la_liste)))
# print(list(map(doubler, la_liste)))
# print(tuple(map(doubler, la_liste)))
# print(set(map(doubler, la_liste)))

# ------ filter 



def is_pair(item):
    return not item % 2 # item % 2 == 0

print("-------- utilisation de filter --------")
# print(filter(is_pair, la_liste))
# print(list(filter(is_pair, la_liste)))
# print(set(filter(is_pair, la_liste)))
# print(tuple(filter(is_pair, la_liste)))
# filter()

def is_majeur(item):
    return item >= 18
print(list(filter(is_majeur, la_liste)))

# ------ zip 
une_liste_a = [1, 2, 3, 4]
une_liste_b = ['a', 'b', 'c']
print("-------- utilisation de zip --------")
print(list(zip(une_liste_a, une_liste_b)))

une_liste_c = ["ID", "Name", "email", "password"]
une_liste_d = ["12454", "Mousseau Gerard", "g.mousseau@gmail.com", "@SDFJO$()"]

print(dict(zip(une_liste_c, une_liste_d, strict=True)))