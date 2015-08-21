#!/usr/bin/env python3

# -*- coding: utf-8 -*-

__author__ = 'Rockie Yang'

import os.path
import random
import codecs

progress_file = "progress.data"
import dictionary

class BasicLearner():
    def __init__(self, words, round):
        self.words = words
        self.round = round

    def learn(self):
        for _ in range(self.round):
            self.learn_one_round()

    def get_choices(self, possible_choices, correct_answer, number=4):
        choices = [correct_answer]

        sample = random.sample(possible_choices, number + 2)

        return choices.extend(sample)[:number]

class Kana2RomajiType(BasicLearner):
    def __init__(self, words, show_origin, rounds=1):
        super(words, rounds)
        self.words = words
        self.show_origin = show_origin

    def __iter__(self):
        return self

    def learn_one_round(self):
        for word in self.words:
            prompt = dictionary.kana(word)
            if self.show_origin:
                prompt += "  " + dictionary.origin(word)
            user_input = input(prompt).strip()
            romaji = dictionary.romaji(word)
            if user_input != romaji:
                print('it should be ' + romaji)

#
# class Kana2RomajiChoose(BasicLearner):
#     def __init__(self, words, show_origin, all_romaji, rounds=1):
#         super(words, rounds)
#         self.words = words
#         self.show_origin = show_origin
#         self.all_romaji = all_romaji
#         self.total_romaji = len(all_romaji)
#
#
#
#     def learn_one_round(self):
#         for word in self.words:
#             prompt = dictionary.kana(word)
#             if self.show_origin:
#                 prompt += "  " + dictionary.origin(word)
#
#             romaji = dictionary.romaji(word)
#             choices = '    '.join(self.get_choices(self.all_romaji, romaji))
#             user_input = input(prompt + '\n' + choices).strip()
#
#             if user_input != romaji:
#                 print('it should be ' + romaji)


class Romaji2KanaChoose(BasicLearner):
    def __init__(self, words, show_origin, all_kana, rounds=1):
        super(words, rounds)
        self.words = words
        self.show_origin = show_origin
        self.all_kana = all_kana

    def learn_one_round(self):
        for word in self.words:
            prompt = dictionary.romaji(word)
            if self.show_origin:
                prompt += "  " + dictionary.origin(word)

            kana = dictionary.kana(word)
            choices = '    '.join(self.get_choices(self.all_kana, kana))
            user_input = input(prompt + '\n' + choices).strip()

            if user_input != kana:
                print('it should be ' + kana)

from collections import namedtuple
ScoreRange = namedtuple("ScoreRange", ["begin", "end"])

class Learner():
    def init_data(self):
        dictionary = self.dictionary
        # initialize progress with all (0, 0) (short, long) memory
        for level in dictionary.levels:
            for word in dictionary.level_words(level):
                key = dictionary.kana(word)
                self.progress_data[key] = (0, 0)
                self.origin_map[key] = dictionary.origin(word)
                self.romji_map[key] = dictionary.romaji(word)



    def next(self):
        # if no word is less then thresholdKana2RomajiTypeRound1 learned
        fetchNewKanaRange = ScoreRange(3, 6)
        startPractiseRange = ScoreRange(6, 10)
        startSelectKanaRange = ScoreRange(10, 15)
        startSelectPractiseKanaRange = ScoreRange(5, 10)


        thresholdKana2RomajiTypeRound1 = 3
        thresholdKana2RomajiTypeRound2 = 6
        thresholdKana2RomajiTypeRound3 = 10

        Hiragana
        Kana2RomajiType -> thresholdKana2RomajiType
        -> fecthANeWLevel
        PractiseKana2RomajiType -> thresholdKana2RomajiType
        Romaji2KanaChoose -> thresholdRomaji2KanaChoose
        PractiseRomaji2KanaChoose -> thresholdRomaji2KanaChoose

    def origin(self, key):
        return self.origin_map[key]

    def romaji(self, key):
        return self.romji_map[key]

    def __init__(self, dictionary, practise_dict={}, progress_file = "progress.data", max_learn=50):
        self.practise_dict = practise_dict
        self.practise_words = []
        self.learned = {}
        self.max_learn = max_learn
        self.progress_data = {}
        self.current_learning = []
        self.origin_map = {}
        self.romji_map = {}
        self.dictionary = dictionary
        self.init_data()
        self.load_saved_progress()


    def load_saved_progress(self):
        """ if the progress file exist update with the progress data"""
        if os.path.isfile(progress_file):
            with codecs.open(progress_file, 'r', 'utf-8') as f:
                for line in f.readlines():
                    items = line.split()
                    key = items[0]
                    progress = (int(items[1]), int(items[2]))
                    self.progress_data[key] = progress
                    if progress != (0, 0):
                        self.learned[key] = True

    def get_practise_words(self):

        for item in self.practise_dict:
            word = item.word
            if_char_learned = [(ch in self.learned) for ch in word]
            if all(if_char_learned):
                self.practise_words.append(item)

    def get_review_words(self):
        # review all learned
        for level in self.dictionary.levels:

            for word in self.dictionary.level_words(level):
                if not self.dictionary.placeholder(word):
                    key = self.dictionary.kana(word)
                    mastery = self.progress_data[key]
                    # it has been learned, but short memory is not full
                    if mastery[1] != 0 and mastery[0] < 10:
                        self.current_learning.append(key)

    def get_new_words(self):
        # learn 5 new characters
        new_char = 0
        print("new words to learn are :")
        for level in self.dictionary.levels:
            level_name = self.dictionary.level_name(level)
            if (level_name in self.progress_data) and self.progress_data[level_name] != (0, 0):
                pass
            else:
                self.progress_data[level_name] = (1, 0)
                for word in self.dictionary.level_words(level):
                    key = self.dictionary.kana(word)

                    romaji = self.dictionary.romaji(word)
                    origin = self.dictionary.origin(word)

                    print("    %s   %s   %s" % (key, romaji, origin))
                    new_char += 1
                    if not self.dictionary.placeholder(word):
                        self.current_learning.append(key)

                break

        print("enjoy learning :-) \n")

    def review(self):
        self.get_review_words()
        self.get_practise_words()
        self.learn()

    def learn_new(self):
        self.get_new_words()
        self.learn()

    def play_sound(self, romaji):
        import pyglet

        import urllib.request
        url = "http://www.tokyowithkids.com/fyi/japanese/kana_sounds/"
        urllib.request.urlretrieve(url + romaji + ".wav", "sound/" + romaji + ".wav")

        sound = pyglet.media.load("sound/" + romaji + '.wav')

        sound.play()


    def learn(self):
        running = True

        mastery_change = len(self.current_learning) * 20 / self.max_learn


        learned = 0
        # if still wanna learn and there are things to learn
        while running and len(self.current_learning) > 0 and learned < self.max_learn:
            # shuffle the learning chars every time
            random.shuffle(self.current_learning)

            # learn a round
            learned += len(self.current_learning)

            index = 0

            while index < len(self.current_learning):
                key = self.current_learning[index]
                promt = "%s             %s\n" % (key, self.origin(key))
                self.play_sound(self.romaji(key))
                user_input = input(promt).strip()
                if user_input == "exit":
                    running = False
                    break

                if user_input == self.romaji(key):
                    progress = (self.progress_data[key][0] + mastery_change, self.progress_data[key][1])
                    self.progress_data[key] = progress
                    if progress[0] >= 10:
                        del self.current_learning[index]
                    else:
                        index += 1
                else:
                    print("you typed wrong, it should be: %s" % self.romji_map[key])
                    index += 1

            random.shuffle(self.practise_words)
            for item in self.practise_words[:20]:
                word = item.word
                user_input = input("%s             %s  %s\n" % (word, item.kanji, item.english)).strip()
                if user_input == "exit":
                    running = False
                    break

                if user_input != item.romaji:
                    print("you typed wrong, it should be: %s" % item.romaji)

        # if user does not specify exit in the middle
        # then it means today's learn has been fulfilled
        # update the short memory to long memory
        if running:
            for key in self.progress_data:
                progress = self.progress_data[key]
                if progress[0] >= 10:
                    self.progress_data[key] = (0, progress[1]+1)

    def save_progress_data(self):
        # write back progress data
        with codecs.open(progress_file, "w", 'utf-8') as f:
            for key in self.progress_data:

                progress = self.progress_data[key]
                f.write("%s %s %s\n" % (key, progress[0], progress[1]))



def main():
    learn_type = input("what would you like to do, [review] or [learn new]\n").strip()
    # learn_type = "learn new"
    # learn_type = "review"
    from dictionary import HiraganaDictionary
    dictionary = HiraganaDictionary()
    import basic1000
    practise_dict = basic1000.practise_dict
    learner = Learner(dictionary, practise_dict)
    if learn_type == "review":
        learner.review()

    elif learn_type == "learn new":
        learner.learn_new()
    else:
        print("%s is not a valid option" % learn_type)
        exit(0)


    print("WOW, you have completed the session. See you next time")
    learner.save_progress_data()

if __name__ == "__main__":

    # from basic1000 import Item
    #
    # parser = Parser(Item)
    # items = parser.parse("basic1000.csv")
    main()