__author__ = 'Rockie Yang'
# -*- coding: utf-8 -*-
import hiragana


def level_name(level):
    return level['name']


def level_words(level):
    return level['words']


def placeholder(word):
    return 'placeholder' in word and word['placeholder']


def kana(word):
    return word['kana']


def romaji(word):
    return word['romaji']


def origin(word):
    return word['origin']



def sound(word):
    if 'sound' in word:
        return word['sound']
    else:
        return word['romaji']


from learn import Kana2RomajiType

class Dictionary():
    def __init__(self):
        levels = []
        levels.extend(hiragana.monographs)
        levels.extend(hiragana.diacritics)
        levels.append(hiragana.diagraphs)
        levels.append(hiragana.diagraphsWithDiacritics)

        self.words = []
        self.romajis = {}
        for level in levels:
            for word in level_words(level):
                self.words.append(word)
                self.romajis.append(romaji(word))

        for level in levels:
            Kana2RomajiType(level_words(level, show_origin=False, 2)).learn()

        # dictionary.extend(hiragana.combined)
