# Déclaration des sets 
a = {1, 2, 4, 5, 11, "A", 'B'}
print(a)

print(2 in a)

le_set = set([1,5,8,79,41,35,201,-65])

print(le_set)

# --- Les méthodes des sets 

le_set_copy = le_set.copy()

print(le_set_copy)

le_set_copy.add(100)
print(le_set_copy)
le_set_copy.add(100)
le_set_copy.add(100)
le_set_copy.add(100)
le_set_copy.add(100)
print(le_set_copy)

le_set_copy.remove(100)
print(le_set_copy)
le_set_copy.discard(-65)
print(le_set_copy)

# La méthode 
resultat = le_set.pop()
print(resultat)

le_set.update([11, 5, 4, 88, 54, 7])
print(le_set)

# La partie intéressante des sets - comparaisons des sets 

a = {1, 'b', 'o', 41, 8, -5}
b = {9, 10, 'h', -5, 'b', 'n'}

# c = a.intersection(b)
c = a & b
print(c)

# a.intersection_update(b)
# print(a)

# c = a.union(b)
c = a | b
print(c)

c = a.difference(b)
# a.difference_update(b)
print(c)

# isdijoint issubset issuperset 

# print(a.isdisjoint(b))
# print((a.difference(b)).isdisjoint(b))

print(a.issubset(b))
print((a.intersection(b)).issubset(b))

print(a.issuperset(b))
print((a.union(b)).issuperset(b))