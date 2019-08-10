from phrasehunter.character import Character


class Phrase:
    def __init__(self, phrase):
        self.phrase = [Character(c) for c in phrase]

    @property
    def guessed(self):
        return sum( [1 for c in self if c.was_guessed] ) == len(self)
    
    def display(self):
        for c in self.phrase: print(f'{c} ', end='')
        print()

    def index(self, char):
        return [i for i, c in enumerate(self) if c.original == char]

    def __iter__(self):
        yield from self.phrase

    def __len__(self):
        return len(self.phrase)

