import random
from game.word import words
from game.Parachute import parachuter


class Jumper:
    """Jumper will either keep a string in their parachute if the player guesses right or the jumper will lose a string if the player chooses wrong."""

    def __init__(self):
      self.word = words
      self.guess = ""
      self.reveal = list(len(self.word)*'_')
      self.turns = 4
      self.won = False
      self.lose = False

    def letter_check(self, letter, word):
      """Checks to see if the letter is the chosen word"""

      for i in range(0, len(self.word)):
          letter = self.word[i]
          if self.guess == letter:
              self.reveal[i] = self.guess
      if '_' not in self.reveal:
          return True
      else:
          return False

    def show(self):
      """this prints out the picture of the jumper"""
      print(parachuter[4 - self.turns])
      print(self.reveal)

    def process(self):
        end_game = False
        while end_game == False:
            while self.won == False and self.turns > 0:
                self.show()
                self.guess = input('guess letter: ')
                self.guess = self.guess.upper()

                if self.guess == self.word:
                    self.won = True
                    self.reaveal = self.word
                if len(self.guess) == 1 and self.guess in self.word:
                    self.won = self.letter_check(self.guess, self.word)
                else:
                    self.turns -= 1
                if self.won == True:
                    print(f"The word is {self.word}! You won!")
                    print("")
                    end_game = True
                else:
                    print(" ")
                if self.turns == 0:
                    self.lose = True
                if self.lose == True:
                    print(parachuter[4])
                    print("Splat!")
                    self.lost = False
                    print(f"The word was {self.word}! Try again!")
                    end_game = True
