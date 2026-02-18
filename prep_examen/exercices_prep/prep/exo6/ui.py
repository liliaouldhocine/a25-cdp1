def ask_int(prompt="> "):
    while True:
        raw = input(prompt).strip()
        if raw.lstrip("-").isdigit():
            return int(raw)
        print("Entrée invalide.")

def show(value):
    print(value)
