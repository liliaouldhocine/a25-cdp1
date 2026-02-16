# Exercice 1 — Séparer logique et interface

## Objectif

Apprendre à séparer `input/print` de la logique.

## Code donné

```python
def addition():
    a = int(input("Nombre 1 > "))
    b = int(input("Nombre 2 > "))
    print("Résultat :", a + b)

addition()
```

## Travail demandé

Créer cette structure :

```
project/
├── main.py
└── mathlib/
    ├── __init__.py
    ├── engine.py
    └── ui.py
```

Contraintes :

- `engine.py` contient la logique d’addition
- `ui.py` contient input/print
- `main.py` orchestre le tout

Interdiction d’utiliser `input()` dans engine.py.

---

# Exercice 2 — Créer une classe Engine

## Objectif

Créer une classe avec plusieurs méthodes.

## Travail demandé

Créer :

```
calculator/
  engine.py
```

Créer une classe :

```
CalculatorEngine
```

avec méthodes :

```
add(a,b)
sub(a,b)
mul(a,b)
```

Créer `main.py` qui teste ces méthodes.

Contraintes :

- aucune interaction utilisateur
- uniquement appels de méthodes

---

# Exercice 3 — Créer une classe Memory

## Objectif

Comprendre la gestion d’état avec une classe.

Créer :

```
memory/
  memory.py
```

Créer classe :

```
Memory
```

avec :

```
store(name, value)
read(name)
clear(name)
```

Exemple attendu :

```
mem.store("A", 10)
mem.read("A") → 10
```

Pas de input/print dans memory.py.

---

# Exercice 4 — Créer une classe UI

## Objectif

Isoler input/print.

Créer :

```
ui/
  ui_console.py
```

Créer classe :

```
ConsoleUI
```

avec :

```
ask_number()
ask_operator()
show_result(result)
```

Créer un main.py qui utilise ConsoleUI.

---

# Exercice 5 — Créer une classe App (orchestrateur)

## Objectif

Assembler plusieurs classes ensemble.

Structure :

```
app/
  engine.py
  ui.py
  app.py
main.py
```

Créer classe :

```
App
```

avec méthode :

```
run()
```

run() doit :

- demander 2 nombres
- demander opérateur
- afficher résultat

Utiliser :

- Engine
- UI

---

# Exercice 6 — Transformer un script existant

## Code donné

```python
while True:
    a = int(input("> "))
    b = int(input("> "))
    print(a*b)
```

## Travail demandé

Transformer en architecture :

```
project/
  engine.py
  ui.py
  app.py
  main.py
```

Contraintes :

- engine.py sans input/print
- ui.py contient input/print
- app.py orchestre

---

# Exercice 7 — Drill structure package

Créer structure suivante :

```
game/
  engine.py
  ui.py
  app.py
main.py
```

Créer classes :

```
GameEngine
GameUI
GameApp
```

Faire fonctionner le projet.

Fonctionnalité minimale :

afficher :

```
Game started
```

---

# Compétences développées par ces exercices

| Exercice | Compétence            |
| -------- | --------------------- |
| 1        | séparation logique/UI |
| 2        | classes               |
| 3        | gestion état          |
| 4        | UI isolée             |
| 5        | orchestrateur         |
| 6        | transformation script |
| 7        | structure package     |
