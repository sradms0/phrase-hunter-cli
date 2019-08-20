import re
from os import name, system
from random import choice
from phrasehunter.phrase import Phrase


class Game:
    '''
    A class to representa a phrase-guessing game 

    Attributes
    ----------
    phrases : list
        a list of phrase objects

    active_phrase : str
        the current phrase of the game

    lives : int
        the amount of guesses a player has

    Methods
    -------
    clear()
        Clears the terminal 

    input_guess()
        Returns the status of the guess

    display()
        Prints the self.active_phrase

    remove_life()
        Decrements self.lives

    thank_you()
        Prints a 'Thank You' message

    end(status)
        Ends the game

    __playing()
        Returns the status of the current gameplay

    __reset()
        Resets the game for a new one

    start()
        Initiates gameplay
    '''
    def __init__(self, phrases):
        self.phrases = [Phrase(re.sub(r'\W+', ' ', p).lower()) for p in phrases]
        self.active_phrase = choice(self.phrases)
        self.lives = 5

    def clear(self):
        '''
        Clears the terminal

        Calls the system command based on OS
        '''
        system('cls') if name == 'nt' else system('clear')

    def input_guess(self):
        '''
        Returns the status of the guess

        Takes the guess of the player, checking it against the active phrase

        Raises
        ------
        ValueError
           If the guess is more than one character
        '''
        guess = input('Guess a letter: ').lower()
        if not guess.isalpha() or len(guess) > 1: 
            raise ValueError('One alpha character is required')
        return self.active_phrase.check_guess(guess)

    def display(self):
        '''Prints the self.active_phrase'''
        self.active_phrase.display()
        print(f'lives: {self.lives}')

    def remove_life(self):
        '''Decrements self.lives'''
        self.lives -= 1

    def thank_you(self):
        '''Prints a 'Thank You' message'''
        print("Thanks for playing!")

    def end(self, status):
        '''
        Ends the game
        
        Exits with a status code after the terminal is cleared and the player is thanked 

        Parameters
        ----------
        status : int
            0 or 1 is the expected status code
        '''
        self.clear()
        self.thank_you()
        exit(status)

    @property
    def __playing(self):
        '''
        Returns the status of the current gameplay

        The player is still playing if [s]he has lives and hasn't guessed the active phrase
        '''
        return not self.active_phrase.guessed and self.lives > 0

    def __reset(self):
        '''Resets the game for a new one'''
        self.active_phrase.reset()
        self.lives = 5
        self.active_phrase = choice(self.phrases)

    def start(self):
        '''Initiates gameplay'''
        while self.__playing:
            try:
                self.clear()
                self.display()

                if not self.input_guess(): self.remove_life()

                if not self.__playing:
                    msg = 'You won!'
                    if self.lives == 0: msg = 'You lost!'
                    self.clear()
                    print(msg)
                    self.display()

                    if input('Play again? [Y/N]').lower() == 'y': self.__reset()
                    else: self.end(0)

            except (ValueError, KeyboardInterrupt) as e: 
                if e.__class__.__name__ == 'ValueError': input(f'{e} [ENTER]')
                else: self.end(1)
                continue

            print()

