#  enumerate(itérable, depart = 0)
une_liste = list(enumerate("Hello"))

print(une_liste)

for index, valeur in enumerate("Hello"): 
    print(f"L'index est : {index}, et la valeur est : {valeur}")