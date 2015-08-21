__author__ = 'Rockie Yang'
import os
import codecs


class Progress():
    def __init__(self, words, progress_file = "progress.data"):
        self.progress_file = progress_file
        # self.practise_dict = practise_dict
        self.progress_data = {}
        self.words = words


    def init_progress(self):
        for word in self.words:
            self.progress_data[word] = (0, 0)

    def load_progress(self):
        """ if the progress file exist update with the progress data"""
        if os.path.isfile(self.progress_file):
            with codecs.open(self.progress_file, 'r', 'utf-8') as f:
                for line in f.readlines():
                    items = line.split()
                    key = items[0]
                    progress = int(items[1])

                    self.progress_data[key] = progress

    def save_progress(self):
        # write back progress data
        with codecs.open(self.progress_file, "w", 'utf-8') as f:
            for key in self.progress_data:

                progress = self.progress_data[key]
                f.write("%s %s\n" % (key, progress))

    def inc(self, word):
        self.progress_data[word] += 1


    def learnt(self):
        learnt_word = [word for word,progress in self.progress_data.items() if progress > 0]
        return learnt_word

    def least_familar_words(self, num):
        learnt_word = self.learnt()
        learnt_word.sort()
        return learnt_word[:num]

    def all_in_range(self, score_range):
        meet = (score_range.begin < score < score_range.end for score in self.progress_data.values())
        return all(meet)
