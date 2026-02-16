# Responsabilités :

# demander une position
# afficher des messages

class ConsoleUI: 
    def ask_position(self, size, player_name):
        maximum = size ** 2
        while True:
            try: 
                pos = int(input(f"{player_name} [1-{maximum}] ? > "))
                if pos < 1 or pos > maximum :
                    print(f"Erreur: Choisissez un nombre entre 1 et {maximum}.")
                    continue

                return pos

            except ValueError:
                self.message("\nErreur: Veuillez entrer un nombre!")

    def message(self, text):
        print(text)

    def ask_restart(self):
        while True: 
            choise = input("Voulez-vous rejouer ? (o/n) > ").strip().lower()

            if choise in ('o', 'oui'): 
                return True
            
            if choise in ('n', 'non') : 
                return False
            
            print("Veuillez entrer o/oui ou n/non")