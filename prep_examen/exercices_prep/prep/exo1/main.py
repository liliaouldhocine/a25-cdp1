from mathlib.engine import add
from mathlib.ui import ask_int, show_result

def main():
    a = ask_int("Nombre 1 > ")
    b = ask_int("Nombre 2 > ")
    show_result(add(a, b))

if __name__ == "__main__":
    main()
