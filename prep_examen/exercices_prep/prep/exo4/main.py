from ui.ui_console import ConsoleUI

def main():
    ui = ConsoleUI()
    a = ui.ask_number()
    op = ui.ask_operator()
    b = ui.ask_number()
    ui.show_result((a, op, b))

if __name__ == "__main__":
    main()
