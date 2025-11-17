# Solutions

## Solution Exercice 1

### 1.1 : Validation d'âge

```python
age = 25

if age < 18:
    print("Mineur")
elif age <= 64:
    print("Majeur")
else:
    print("Senior")
```

### 1.2 : Calcul de note

```python
note = 85

if note >= 90:
    print("A")
elif note >= 80:
    print("B")
elif note >= 70:
    print("C")
elif note >= 60:
    print("D")
else:
    print("E")
```

### 1.3 : Saison de l'année

```python
mois = 7

if mois in [12, 1, 2]:
    print("Hiver")
elif mois in [3, 4, 5]:
    print("Printemps")
elif mois in [6, 7, 8]:
    print("Été")
elif mois in [9, 10, 11]:
    print("Automne")
else:
    print("Mois invalide")
```

## Solution Exercice 2

### 2.1 : Accès autorisé

```python
badge_valide = True
utilisateur_banni = False
abonnement_paye = True

acces_autorise = badge_valide and not utilisateur_banni and abonnement_paye

if acces_autorise:
    print("Accès autorisé")
else:
    print("Accès refusé")
```

### 2.2 : Conditions météorologiques

```python
il_pleut = False
temperature = 22
alerte_meteo = False

peut_sortir = not il_pleut and 15 <= temperature <= 30 and not alerte_meteo

if peut_sortir:
    print("Conditions idéales pour sortir")
else:
    print("Mieux vaut rester à l'intérieur")
```

### 2.3 : Validation de données

```python
email = "user@example.com"
age = 25
nom = "Dupont"

email_valide = email != ""
age_valide = 0 <= age <= 120
nom_valide = not any(char.isdigit() for char in nom)

donnees_valides = email_valide and age_valide and nom_valide

if donnees_valides:
    print("Données valides")
else:
    print("Données invalides")
```

## Solution Exercice 3

### 3.1 : Directions

```python
direction = "n"

match direction:
    case "n":
        print("Nord")
    case "s":
        print("Sud")
    case "e":
        print("Est")
    case "w":
        print("Ouest")
    case _:
        print("Direction invalide")
```

### 3.2 : Statut de commande

```python
statut = "expediee"

match statut:
    case "en_attente":
        print("Votre commande est en attente")
    case "expediee":
        print("Votre commande a été expédiée")
    case "livree":
        print("Votre commande a été livrée")
    case "annulee":
        print("Votre commande a été annulée")
    case _:
        print("Statut inconnu")
```

### 3.3 : Types de véhicules

```python
vehicule = "moto"

match vehicule:
    case "voiture":
        print("Véhicule terrestre à 4 roues")
    case "moto":
        print("Véhicule terrestre à 2 roues")
    case "bateau":
        print("Véhicule maritime")
    case "avion":
        print("Véhicule aérien")
    case _:
        print("Type de véhicule non reconnu")
```

## Solution Exercice 4

### 4.1 : Positif ou négatif

```python
nombre = -5

resultat = "positif" if nombre >= 0 else "négatif"
print(f"Le nombre {nombre} est {resultat}")
```

### 4.2 : Majorité légale

```python
age = 20

statut = "majeur" if age >= 18 else "mineur"
print(f"À {age} ans, vous êtes {statut}")
```

### 4.3 : Remise automatique

```python
prix_original = 120

prix_final = prix_original * 0.8 if prix_original > 100 else prix_original
print(f"Prix final : {prix_final}$")
```

## Solution Exercice 5

### 5.1 : Système d'authentification

```python
username = "john_doe"
password = "secret123"
user_blocked = False

username_ok = username != ""
password_ok = len(password) >= 6
not_blocked = not user_blocked

authentification_reussie = username_ok and password_ok and not_blocked

if authentification_reussie:
    print("Authentification réussie")
else:
    print("Échec de l'authentification")
    if not username_ok:
        print("- Le nom d'utilisateur ne peut pas être vide")
    if not password_ok:
        print("- Le mot de passe doit avoir au moins 6 caractères")
    if user_blocked:
        print("- L'utilisateur est bloqué")
```

### 5.2 : Calculateur de catégorie sportive

```python
age = 14

if 6 <= age <= 7:
    categorie = "Poussin"
elif 8 <= age <= 9:
    categorie = "Benjamin"
elif 10 <= age <= 11:
    categorie = "Minime"
elif 12 <= age <= 15:
    categorie = "Cadet"
elif 16 <= age <= 17:
    categorie = "Junior"
elif 18 <= age <= 39:
    categorie = "Senior"
elif age >= 40:
    categorie = "Vétéran"
else:
    categorie = "Trop jeune"

# Utilisation de l'opérateur ternaire pour le message
message = "Bienvenue en compétition !" if categorie != "Trop jeune" else "Revenez quand vous serez plus âgé"

print(f"À {age} ans, catégorie : {categorie}")
print(message)
```
