#!/usr/bin/python

__author__ = 'Rockie Yang'

import os.path
from dictionary import dictionary

progress_file = "progress.data"

progress_data = {}
current_learning = []
origin_map = {}
rom_map = {}

# initialize progress with all (0, 0) (short, long) memory
for (jp, rom, origin) in dictionary:
    progress_data[jp] = (0, 0)
    origin_map[jp] = origin
    rom_map[jp] = rom

# if the progress file exist update with the progress data
if os.path.isfile(progress_file):
    with open(progress_file) as f:
        for line in f.readlines():
            items = line.split()
            progress_data[items[0]] = (int(items[1]), int(items[2]))

learn_type = raw_input("what would you like to do, review or learnnew\n")


if learn_type == "review":
    # review all learned
    for (jp, rom, origin) in dictionary:
        mastery = progress_data[jp]
        # it has been learned, but short memory is not full
        if mastery[1] != 0 and mastery[0] < 10:
            current_learning.append(jp)

elif learn_type == "learnnew":
    # learn 5 new characters
    new_char = 0
    print("new words to learn are :")
    for (jp, rom, origin) in dictionary:
        mastery = progress_data[jp]
        if new_char < 5 and mastery == (0, 0):
            current_learning.append(jp)
            print("    %s   %s   %s" % (jp, rom, origin))
            new_char += 1

    print("enjoy learning :-) \n")

import random

running = True
max_learn = 50
mastery_change = len(current_learning) * 20 / max_learn

learned = 0l
# if still wanna learn and there are things to learn
while running and len(current_learning) > 0 and learned < max_learn:
    # shuffle the learning chars every time
    random.shuffle(current_learning)

    # learn a round
    learned += len(current_learning)

    index = 0

    while index < len(current_learning):
        jp = current_learning[index]
        user_input = raw_input("%s             %s\n" % (jp, origin_map[jp]))
        if user_input == "exit":
            running = False
            break

        if user_input == rom_map[jp]:
            progress = (progress_data[jp][0] + mastery_change, progress_data[jp][1])
            progress_data[jp] = progress
            if progress[0] >= 10:
                del current_learning[index]
            else:
                index += 1
        else:
            print("you typed wrong, it should be: %s" % rom_map[jp])
            index += 1


# if user does not specify exit in the middle
# then it means today's learn has been fulfilled
# update the short memory to long memory
if running:
    for key in progress_data:
        progress = progress_data[key]
        if progress[0] >= 10:
            progress_data[key] = (0, progress[1]+1)

# write back progress data
with open(progress_file, "w") as f:
    for jp, rom, origin in dictionary:
        progress = progress_data[jp]
        f.write("%s %s %s\n" % (jp, progress[0], progress[1]))

print("WOW, you have completed the session. See you next time")