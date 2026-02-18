class ConsoleUI:
    def show_menu(self):
        print("\nConvertisseur")
        print("1. Celsius → Fahrenheit")
        print("2. Fahrenheit → Celsius")
        print("3. Quitter")

    def ask_choice(self):
        return input("> ").strip()

    def ask_number(self, prompt):
        while True:
            raw = input(prompt).strip()
            try:
                return float(raw)
            except ValueError:
                print("Entrée invalide.")

    def show_result(self, result):
        print("Résultat :", result)

    def show_error(self, msg):
        print("Erreur :", msg)
