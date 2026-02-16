from tictactoe.ui import ConsoleUI
from tictactoe.board import Board
from tictactoe.game import Game

# Responsabilités :

# créer les objets
# démarrer le jeu

def main():
    ui = ConsoleUI()
    board = Board(3)
    game = Game(ui, board)
    game.run()

if __name__ == "__main__":
    main()