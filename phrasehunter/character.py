class Character:
    def __init__(self, char):
        self.__verify_char(char)

        self.__original = char
        self.display = '_'
        self.was_guessed = False

    def check_guess(self, guess):
        self.__verify_char(guess)

        if self.__original == guess:
            self.was_guessed = True
            self.__show()

    def __str__(self):
        return f'{self.display}'

    def __show(self):
        self.display = self.__original

    def __verify_char(self, char):
        if not isinstance(char, str): 
            raise TypeError('A string is required')
        if len(char) != 1 or not str.isalpha(char): 
            raise ValueError('Character of a..z required')
