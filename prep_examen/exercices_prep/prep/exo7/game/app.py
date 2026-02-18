from .engine import GameEngine
from .ui import GameUI

class GameApp:
    def __init__(self):
        self.engine = GameEngine()
        self.ui = GameUI()

    def run(self):
        self.ui.show(self.engine.start_message())
