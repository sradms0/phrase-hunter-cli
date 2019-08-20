class Character:
    '''
    A class to represent a character among others in a phrase

    Attributes
    ----------
    __original : str
        a private placeholder for the original character

    display : str
        the character will display itself or a '_' if is not guessed

    was_guessed : bool
        shows if the character has been guessed

    Methods
    -------
    check_guess(guess)
        Checks if a character string matches self.__original

    original()
        Returns a copy of the original character, self.__original

    __show()
        Shows the original character in self.display

    __verify_char(char)
        Checks if one alpha or space character was taken

    reset(char)
        Sets self.__was_guessed back to False and self.display to hidden  
    '''

    def __init__(self, char):
        '''
        Parameters
        ----------
        char : str
            The string character to be placed in self.__original
        '''
        self.__verify_char(char)

        self.__original = char
        display = '_'
        was_guessed = False

        # allow space: show it in display and don't allow for guessing
        if char.isspace(): 
            display = char
            was_guessed = True
        self.display = display
        self.was_guessed = was_guessed

    def check_guess(self, guess):
        '''
        Checks if a character string matches self.__original

        Parameters
        ----------
        guess : str (1 char)
            The guess to compare to self.__original
        '''

        # check and display if correct guess
        self.__verify_char(guess)
        if self.__original == guess:
            self.was_guessed = True
            self.__show()

    @property
    def original(self):
        '''Returns a copy of the original character, self.__original'''
        return self.__original

    def __str__(self):
        '''Returns a formatted string of the current character display'''
        return f'{self.display}'

    def __show(self):
        '''Shows the original character in self.display'''
        self.display = self.__original

    def __verify_char(self, char):
        '''
        Checks if one alpha or space character was taken
        
        Raises
        ------
        TypeError
            If the character entered is not a string instance

        ValueError
            If the character entered is not alphabetic or a space
        '''

        if not isinstance(char, str): 
            raise TypeError('A string is required')
        if len(char) != 1 or not (char.isspace() or char.isalpha()): 
            raise ValueError('Character of a..z required')

    def reset(self):
        '''Sets self.__was_guessed back to False and self.display to hidden '''
        # only 'reset' if the character is alphabetic
        if not self.original.isspace():
            self.was_guessed = False
            self.display = '_'
