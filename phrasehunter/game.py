import re
from os import name, system
from random import choice
from phrasehunter.phrase import Phrase


class Game:
    def __init__(self, phrases):
        self.phrases = [Phrase(re.sub(r'\W+', ' ', p).lower()) for p in phrases]
        self.active_phrase = choice(self.phrases)
        self.lives = 5

    def clear(self):
        system('cls') if name == 'nt' else system('clear')

    def input_guess(self):
        guess = input('Guess a letter: ').lower()
        if not guess.isalpha() or len(guess) > 1: 
            raise ValueError('One alpha character is required')
        return self.active_phrase.check_guess(guess)

    def display(self):
        self.active_phrase.display()
        print(f'lives: {self.lives}')

    def remove_life(self):
        self.lives -= 1

    def start(self):
        while not self.active_phrase.guessed and self.lives > 0:
            self.clear()
            self.display()
            try:
                if not self.input_guess(): self.remove_life()
            except (ValueError, KeyboardInterrupt) as e: 
                if e.__class__.__name__ == 'ValueError':
                    input(f'{e} [ENTER]')
                else: 
                    self.clear()
                    print("Thanks for playing!")
                    exit(1)

                continue
            print()
        else:
            msg = 'You won!'
            if self.lives == 0: msg = 'You lost!'
            self.clear()
            print(msg)
            self.display()

