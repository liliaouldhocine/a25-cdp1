nombre = 0

while not (1 <= nombre <= 100):
    nombre = int(input("Entrez une valeur : "))
    if 1 <= nombre <= 100:
        break
    else:
        print("Nombre invalide")

print(f"Nombre valide: {nombre}")