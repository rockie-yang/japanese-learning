# -*- coding: utf-8 -*-
__author__ = 'Rockie Yang'
from unidecode import unidecode

import codecs

class Parser():
    def __init__(self, Item, parse_long_vowel=False):
        self.Item = Item
        self.parse_long_vowel = parse_long_vowel

    def parse(self, file):
        words = []
        with codecs.open(file, 'r', 'utf-8') as f:
            for line in f.readlines():
                try:
                    item = self.Item(line, self.parse_long_vowel)
                    # print(str(item))
                    words.append(item)
                except SyntaxError as e:
                    pass

        return words

class Item():
    @staticmethod
    def is_valid(items):
        return len(items) >= 4

    def __init__(self, line, parse_long_vowel=False):
        self.items = line.split(';')
        if len(self.items) < 4:
            raise SyntaxError("not parsable, it should have at least 4 items split with ;")
        else:
            self.word = self.items[0]
            self.kanji = self.items[1]
            self.english = self.items[2]
            item3 = self.items[3].strip()
            romaji = unidecode(item3)
            if not parse_long_vowel and romaji != item3:
                raise SyntaxError("not parsable, it has long vowel romaji, ignore it")

            # TODO all - is removed at the moment, it might need be checked
            self.romaji = romaji.replace('-', '')

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.word, self.romaji, self.kanji, self.english)


parser = Parser(Item)
practise_dict = parser.parse("basic1000.csv")