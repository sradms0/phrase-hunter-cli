from os import name, system
from random import choice
from phrasehunter.phrase import Phrase


class Game:
    def __init__(self, phrases):
        self.phrases = [Phrase(p) for p in phrases]
        self.active_phrase = choice(self.phrases)
        self.lives = 5

    def clear(self):
        system('cls') if name == 'nt' else system('clear')

    def input_guess(self):
        return self.active_phrase.check_guess(input('Guess a letter: '))

    def display(self):
        self.active_phrase.display()
        print(f'lives: {self.lives}')

    def remove_life(self):
        self.lives -= 1

    def start(self):
        while not self.active_phrase.guessed and self.lives > 0:
            self.clear()
            self.display()
            if not self.input_guess(): self.remove_life()
            print()
        else:
            msg = 'You won!'
            if self.lives == 0: msg = 'You lost!'
            self.clear()
            print(msg)
            self.display()

