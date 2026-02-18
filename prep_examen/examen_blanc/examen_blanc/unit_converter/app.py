from .engine import ConverterEngine
from .ui_console import ConsoleUI

class ConverterApp:
    def __init__(self):
        self.engine = ConverterEngine()
        self.ui = ConsoleUI()

    def run(self):
        while True:
            self.ui.show_menu()
            choice = self.ui.ask_choice()

            if choice == "1":
                c = self.ui.ask_number("Celsius > ")
                result = self.engine.celsius_to_fahrenheit(c)
                self.ui.show_result(result)

            elif choice == "2":
                f = self.ui.ask_number("Fahrenheit > ")
                result = self.engine.fahrenheit_to_celsius(f)
                self.ui.show_result(result)

            elif choice == "3":
                break

            else:
                self.ui.show_error("Choix invalide.")
