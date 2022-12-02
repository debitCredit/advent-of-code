import re
import os
import sys
import functools
from collections import defaultdict
from collections import Counter


file = os.path.join(sys.path[0], "input.txt")
# file = os.path.join(sys.path[0], "test_input.txt")

trans = str.maketrans("XYZ", "ABC")

ll = [[y for y in x.split()] for x in open(file).read().strip().split('\n')]
ll2  = [[el[0], el[1].translate(trans)] for el in ll]

rules = ["A", "B", "C"]
points = {"A": 1, "B": 2, "C": 3}
score = 0

def determine_winner(game_list, first, second):
    index_to = game_list.index(first)
    index_from = index_to + 1
    elements_after = game_list[index_from:]
    elements_before = game_list[:index_to]
    elements =  elements_after + elements_before
    half = len(elements) // 2
    beating = elements[:half]
    return second not in beating

for l in ll2:
    c += 1
    score += points[l[1]]
    if l[0] == l[1]:
        score += 3
        pass
    else:
        if not determine_winner(rules, *l):
            score += 6

print(score)