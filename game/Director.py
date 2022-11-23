from game.Jumper import Jumper
from game.word import words
from game.console import Console


class Director:

    def __init__(self):
        self.new_round = True
        self.console = Console()
        self.jumper = Jumper()
        self.word = words

    def game_round(self):
        while self.new_round:
            self.get_letter()
            self.set_jumper()
            self.set_pass()

    def get_letter(self):
        self.word

    def set_jumper(self):
        self.jumper.process()

    def set_pass(self):
        pass
