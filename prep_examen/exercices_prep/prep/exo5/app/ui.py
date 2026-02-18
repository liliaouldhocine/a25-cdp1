class UI:
    def ask_number(self, prompt):
        while True:
            raw = input(prompt).strip()
            try:
                return float(raw)
            except ValueError:
                print("Entrée invalide.")

    def ask_operator(self):
        while True:
            op = input("Opérateur (+ - * /) > ").strip()
            if op in {"+", "-", "*", "/"}:
                return op
            print("Opérateur invalide.")

    def show_result(self, result):
        print("Résultat :", result)

    def show_error(self, msg):
        print("Erreur :", msg)
