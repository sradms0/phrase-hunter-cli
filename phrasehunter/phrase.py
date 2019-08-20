from phrasehunter.character import Character


class Phrase:
    '''
    A class to represent a phrase of characters

    Attributes
    ----------
    phrase : list
        a list of character objects

    Methods
    -------
    guessed()
        Returns the guess-status of the phrase

    display()
        Prints all characters in the phrase

    index(char)
        Returns a list of indices pointing to where char is in self.phrases

    check_guess(guess)
        Checks if a guess is in the self.phrases

    reset()
        Resets all characters in self.phrases
    '''
    def __init__(self, phrase):
        '''
        Parameters
        ----------
        phrase : str
            The string containing characters to be instantiated as Character objects
        '''
        self.phrase = [Character(c) for c in phrase]

    @property
    def guessed(self):
        '''
        Returns the guess-status of the phrase

        If the sum of guessed characters, represented as 1, equals the length
        of the phrase, then the phrase has been guessed
        '''
        return sum( [1 for c in self if c.was_guessed] ) == len(self)
    
    def display(self):
        '''Prints all characters in the phrase'''
        for c in self.phrase: print(f'{c} ', end='')
        print()

    def index(self, char):
        '''
        Returns a list of indices pointing to where char is in self.phrases

        Parameters
        ----------
        char : str
            The character to find in the phrase
        '''
        return [i for i, c in enumerate(self) if c.original == char]

    def check_guess(self, guess):
        '''
        Checks if a guess is in the self.phrases

        If the guess is correct, this method will return True

        Parameters
        ----------
        guess : str
            The guess that is compared to all characters in the phrase
        '''
        char_indices = self.index(guess)
        if len(char_indices) > 0:
            for c in self: c.check_guess(guess)
            return True

    def reset(self):
        '''Resets all characters in self.phrases'''
        for c in self.phrase: c.reset()

    def __iter__(self):
        '''Uses the phrase of characters, self.phrase, as the iterable'''
        yield from self.phrase

    def __len__(self):
        '''Returns the length of the list self.phrase'''
        return len(self.phrase)

    def __str__(self):
        '''Returns the a formatted string of all original characters of each character object'''
        return ''.join([f'{c.original}' for c in self.phrase])

