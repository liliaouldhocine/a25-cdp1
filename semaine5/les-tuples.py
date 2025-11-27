un_tuple = (1, 2, 3, 4)

print(un_tuple)

print(un_tuple[0])

a, b, *c = un_tuple

print(a, b, c)

un_tuple2 = (5, 6)

print(un_tuple + un_tuple2)

resultat = un_tuple[0:3]
print(resultat)

resultat = un_tuple[:]
print(resultat)

# --- Déclaration par class
un_tuple3 = tuple(["Hello", 0, True])
print(un_tuple3)

un_tuple3 = tuple("Salut tout le monde")
print(un_tuple3)

# un_tuple3 = tuple(range(4, 12))
# print(un_tuple3)

# Recherche
# print(un_tuple.index(10))
if 10 in un_tuple: 
    print(un_tuple.index(10))
else: 
    print("Nope")

# La méthode count 
print(un_tuple3.count(" "))

