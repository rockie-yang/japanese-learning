__author__ = 'Rockie Yang'
# -*- coding: utf-8 -*-
import hiragana

class HiraganaDictionary():
    levels = []
    levels.extend(hiragana.basic)
    levels.extend(hiragana.voiced)

    @staticmethod
    def level_name(level):
        return level[0][0]

    @staticmethod
    def level_words(level):
        return level[1:]

    @staticmethod
    def placeholder(t):
        return len(t) > 3

    @staticmethod
    def key(t):
        return t[0]

    @staticmethod
    def romaji(t):
        return t[1]

    @staticmethod
    def origin(t):
        return t[2]

# dictionary.extend(hiragana.combined)