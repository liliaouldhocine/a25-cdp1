from .engine import Engine
from .ui import UI

class App:
    def __init__(self):
        self.engine = Engine()
        self.ui = UI()

    def run(self):
        a = self.ui.ask_number("Nombre 1 > ")
        op = self.ui.ask_operator()
        b = self.ui.ask_number("Nombre 2 > ")

        try:
            result = self.engine.compute(a, op, b)
            self.ui.show_result(result)
        except ValueError as e:
            self.ui.show_error(str(e))
