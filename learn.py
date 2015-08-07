#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Rockie Yang'

import os.path
import random

progress_file = "progress.data"



class Learner():
    def init_data(self):
        dictionary = self.dictionary
        # initialize progress with all (0, 0) (short, long) memory
        for level in dictionary.levels:
            for word in dictionary.level_words(level):
                key = dictionary.key(word)
                self.progress_data[key] = (0, 0)
                self.origin_map[key] = dictionary.origin(word)
                self.romji_map[key] = dictionary.romaji(word)

    def origin(self, key):
        return self.origin_map[key]

    def romaji(self, key):
        return self.romji_map[key]

    def __init__(self, dictionary, progress_file = "progress.data", max_learn=50):
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
            with open(progress_file) as f:
                for line in f.readlines():
                    items = line.split()
                    self.progress_data[items[0]] = (int(items[1]), int(items[2]))



    def get_review_words(self):
        # review all learned
        for level in self.dictionary.levels:

            for word in self.dictionary.level_words(level):
                if not self.dictionary.placeholder(word):
                    key = self.dictionary.key(word)
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
            if (level_name not in self.progress_data) or self.progress_data[level_name] != (0, 0):
                self.progress_data[level_name] = (1, 0)
                for word in self.dictionary.level_words(level):
                    key = self.dictionary.key(word)

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
        self.learn()

    def learn_new(self):
        self.get_new_words()
        self.learn()



    def learn(self):
        running = True

        mastery_change = len(self.current_learning) * 20 / self.max_learn


        learned = 0l
        # if still wanna learn and there are things to learn
        while running and len(self.current_learning) > 0 and learned < self.max_learn:
            # shuffle the learning chars every time
            random.shuffle(self.current_learning)

            # learn a round
            learned += len(self.current_learning)

            index = 0

            while index < len(self.current_learning):
                key = self.current_learning[index]
                user_input = raw_input("%s             %s\n" % (key, self.origin(key))).strip()
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
                    print("you typed wrong, it should be: %s" % self.romji_map(key))
                    index += 1


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
        with open(progress_file, "w") as f:
            for key in self.progress_data:

                progress = self.progress_data[key]
                f.write("%s %s %s\n" % (key, progress[0], progress[1]))

class Parser():
    def __init__(self, Item):
        self.Item = Item

    def parse(self, file):
        items = []
        with open(file) as f:
            for line in f.readlines():
                try:
                    item = self.Item(line)
                    print(str(item))
                    items.append(item)
                except SyntaxError as e:
                    pass

        return items

def main():
    # learn_type = raw_input("what would you like to do, [review] or [learn new]\n").strip()
    # learn_type = "learn new"
    learn_type = "review"
    from dictionary import HiraganaDictionary
    dictionary = HiraganaDictionary()
    learner = Learner(dictionary)
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
    from basic1000 import Item

    parser = Parser(Item)
    items = parser.parse("basic1000.txt")
    main()