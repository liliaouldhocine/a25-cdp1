import copy
# LES DICTIONNAIRES
#-----------------------------------------

une_liste = [1, 2]
# 0 => 1
# 1 => 2

a = {
    "name":"lilia",
    "age": 41,
    9: "coucou",
    True: "la cle est un booléen",
    1: "la cle est un entier",
    "age": 25
}

# CLÉ (uniques) => Valeur

# print(a)
# print(a["age"])
# print(a[True])
# print(a[9])
# print(a[1])
# print(a["age"])

#-----------------------------------------

un_dict = {
    "nom": "dufour",
    "prenom": "marc",
    "age": 25,
    0: 0,
    True: "ceci est un True",
    "adresse": {
        "numero": 64,
        "rue": "St-Jacques",
        "ville": "Charlemagne",
        "code_postal": "J5Z1Z4"
    },
    "notes": [85, 92, 99, 74],
    "date_naisance": "26/11/2025"
}

# un_etudiant = dict(name="jean", age="33", les_notes=[85, 92, 99, 74])

# print(un_etudiant)
# print(un_dict)

# ===  OPERATEUR IN et les METHODES GET, COPY et CLEAR ===

# for item in un_dict:
#     print(item)

# print()

# for valeur in un_dict.values():
#     print(valeur)

# print()

# for cle in un_dict.keys():
#     print(cle)

# print()

# for item in un_dict.items():
#     print(item)

# print(item)

# for cle, valeur in un_dict.items():
#     print(cle, valeur)

# print(item)

# print(un_dict["date_naissance"])

# if "date_naissance" in un_dict:
#     print(un_dict["date_naissance"])
# else:
#     print("non existant")

# print()

# if un_dict.get("date_naissance"):           
#     print(un_dict.get("date_naissance"))
# else:
#     print("non existant")

# print()

# if un_dict.get("date_naissance", "0/0/0000"):           
#     print(un_dict.get("date_naissance", "0/0/0000"))
# else:
#     print("non existant")

#  === COPY ===

# un_dict2 = un_dict      #SHALOW COPY
# un_dict2["prenom"] = "julien"

# print(un_dict["prenom"])
# print(un_dict2["prenom"])
# print()

# un_dict2["adresse"]["ville"] = "Montreal"
# print(un_dict["adresse"]["ville"])
# print(un_dict2["adresse"]["ville"])
# print()

# un_dict2 = copy.deepcopy(un_dict)

# un_dict2["adresse"]["ville"] = "Quebec"
# print(un_dict["adresse"]["ville"])
# print(un_dict2["adresse"]["ville"])

#  === SUPRIMER DES ELEMENT DU DICTIONNAIRE ===

# result = un_dict.pop(True)

# print(result)
# print(un_dict)
# print()

# result1 = un_dict.popitem()
# print(result1)
# print(un_dict)

# print()
# cle, valeur = un_dict.popitem()
# print(cle, valeur)
# print(un_dict)

# print()

#  === METHODE UPDATE ===

# un_dict.update({"age": 27})
# print(un_dict)
# print()

# un_dict["age"] = 35
# print(un_dict)
# print()

# un_dict.update({"statut": "inscrit"})
# print(un_dict)
# print()

# un_dict.setdefault("presence", False)
# un_dict.update({"presence": True})
# print(un_dict)

#  === APPEND ===

nouvelle_note = 65

if 'notes' in un_dict: 
    un_dict['notes'].append(nouvelle_note)
else:
    un_dict['notes'] = [nouvelle_note]

un_dict.setdefault('notes', [])
un_dict['notes'].append(nouvelle_note)
print(un_dict)