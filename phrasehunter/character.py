class Character:
    def __init__(self, char):
        self.__verify_char(char)

        self.__original = char
        display = '_'
        was_guessed = False

        if char.isspace(): 
            display = char
            was_guessed = True
        self.display = display
        self.was_guessed = was_guessed

    def check_guess(self, guess):
        self.__verify_char(guess)

        if self.__original == guess:
            self.was_guessed = True
            self.__show()

    @property
    def original(self):
        return self.__original

    def __str__(self):
        return f'{self.display}'

    def __show(self):
        self.display = self.__original

    def __verify_char(self, char):
        if not isinstance(char, str): 
            raise TypeError('A string is required')
        if len(char) != 1 or not (char.isspace() or char.isalpha()): 
            raise ValueError('Character of a..z required')

    def reset(self):
        if not self.original.isspace():
            self.was_guessed = False
            self.display = '_'
