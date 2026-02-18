# EXAMEN BLANC — Convertisseur d’unités (POO, modules, packages)

Durée suggérée : 45–60 minutes
Objectif : transformer un script en application structurée avec **POO + modules + package**

---

# Code de départ (fourni)

```python
# convertisseur simple

while True:

    print("\nConvertisseur")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Quitter")

    choix = input("> ")

    if choix == "1":
        c = float(input("Celsius > "))
        f = (c * 9/5) + 32
        print("Résultat :", f)

    elif choix == "2":
        f = float(input("Fahrenheit > "))
        c = (f - 32) * 5/9
        print("Résultat :", c)

    elif choix == "3":
        break
```

---

# Travail demandé

Vous devez transformer ce programme en une application Python structurée utilisant :

- un package
- des modules
- la programmation orientée objet

---

# Structure obligatoire

```
converter/
├── main.py
└── unit_converter/
    ├── __init__.py
    ├── engine.py
    ├── ui_console.py
    └── app.py
```

---

# Partie 1 — engine.py (logique)

Créer une classe :

```
ConverterEngine
```

avec méthodes :

```
celsius_to_fahrenheit(c)
fahrenheit_to_celsius(f)
```

Contraintes :

- interdit d’utiliser input()
- interdit d’utiliser print()

---

# Partie 2 — ui_console.py (interface)

Créer une classe :

```
ConsoleUI
```

avec méthodes :

```
show_menu()
ask_choice()
ask_number()
show_result(result)
```

Ce module est le seul autorisé à utiliser input() et print().

---

# Partie 3 — app.py (orchestrateur)

Créer une classe :

```
ConverterApp
```

avec :

```
run()
```

run() doit :

- afficher le menu
- appeler les bonnes méthodes
- utiliser ConverterEngine et ConsoleUI

---

# Partie 4 — main.py

Créer :

```python
from unit_converter.app import ConverterApp

app = ConverterApp()
app.run()
```

---

# Résultat attendu

Le programme doit fonctionner avec :

```
python main.py
```

---

# Contraintes importantes

| Module        | input() autorisé | print() autorisé |
| ------------- | ---------------- | ---------------- |
| engine.py     | ❌               | ❌               |
| ui_console.py | ✅               | ✅               |
| app.py        | ✅               | ✅               |
| main.py       | ❌               | ❌               |

---

# Bonus (optionnel)

Ajouter :

- Kelvin conversions
- validation des entrées

---

# Critères d’évaluation

| Critère            | Points |
| ------------------ | ------ |
| Structure correcte | 25     |
| Classe Engine      | 25     |
| Classe UI          | 20     |
| Classe App         | 20     |
| Fonctionnement     | 10     |

Total : 100 points
