import re
import os
import sys
import functools
from collections import defaultdict
from collections import Counter


file = os.path.join(sys.path[0], "input.txt")
# file = os.path.join(sys.path[0], "test_input.txt")


ll = [[y for y in x.split()] for x in open(file).read().strip().split('\n')]

rules = ["A", "B", "C"]
points_hands = {"A": 1, "B": 2, "C": 3}
points_result = {"Y": 3, "X": 0, "Z": 6}
score = 0

def determine_play(game_list, first, outcome):
    index_to = game_list.index(first)
    index_from = index_to + 1
    elements_after = game_list[index_from:]
    elements_before = game_list[:index_to]
    elements =  elements_after + elements_before
    half = len(elements) // 2
    if outcome == "Z":
        return elements[0]
    if outcome == "X":
        return elements[1]

def determine_result(game_list, first, outcome):
    # draw
    if outcome == "Y":
        return first
    else:
        return determine_play(game_list, first, outcome)

for l in ll:
    hand_to_play = determine_result(rules, *l)
    score += points_result[l[1]]
    score += points_hands[hand_to_play]

print(score)
