__author__ = 'Rockie Yang'

class Item():
    def __init__(self, line):
        self.items = line.split(';')
        if len(self.items) < 4:
            raise SyntaxError("not parsable, it should have at least 4 items split with ;")
        else:
            self.word = self.items[0]
            self.kanji = self.items[1]
            self.english = self.items[2]
            self.romaji = self.items[3].strip()

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.word, self.romaji, self.kanji, self.english)
