from engine import multiply
from ui import ask_int, show

class App:
    def run(self):
        while True:
            a = ask_int("> ")
            b = ask_int("> ")
            show(multiply(a, b))
