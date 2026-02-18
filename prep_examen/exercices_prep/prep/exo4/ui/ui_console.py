class ConsoleUI:
    def ask_number(self):
        while True:
            raw = input("Nombre > ").strip()
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
