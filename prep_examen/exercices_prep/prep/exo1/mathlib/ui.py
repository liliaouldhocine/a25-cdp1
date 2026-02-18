def ask_int(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.lstrip("-").isdigit():
            return int(raw)
        print("Entrée invalide, recommence.")

def show_result(result):
    print("Résultat :", result)
